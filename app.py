import json
import os
import time
from datetime import datetime
import streamlit as st

# ==============================================================================
# KONFIGURACJA STRONY STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="Golem XV — Ludzie: Droga do Rzeczywistości",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# WBUDOWANA BAZA STARTOWA (DZIAŁA NAWET GDY WGRASZ SAM PLIK app.py NA GITHUB)
# ==============================================================================
DEFAULT_SEED = {
    "projectMeta": {
        "title": "Golem XV — Ludzie: Droga do Rzeczywistości",
        "subtitle": "Mapa projektu badawczego — siedem powiązanych ścieżek (A–G)",
        "overarchingGoal": (
            "Zrozumieć człowieka jako organizm biologiczny, umysł, twórcę technologii "
            "i część ziemskiej biosfery, a jednocześnie zbadać możliwości jego "
            "funkcjonowania poza naturalnym środowiskiem Ziemi."
        ),
        "organizationalRule": (
            "Każda ścieżka ma własne pytania badawcze, bibliografię i cele. Wspólne "
            "podstawy naukowe pozwalają łączyć wiedzę, ale nie oznaczają konieczności "
            "równoległego studiowania wszystkich dziedzin. Filozofia pozostaje przekrojową "
            "warstwą interpretacyjną. Pozostałe projekty rozwijają się w miarę dostępnego "
            "czasu i zainteresowania."
        ),
        "foundations": [
            "Matematyka i logika",
            "Informatyka",
            "Programowanie",
            "Fizyka",
            "Elektronika",
            "Chemia",
            "Biologia",
            "Sztuczna inteligencja",
        ],
        "fgRelation": {
            "summary": "Oba projekty badają człowieka w relacji ze środowiskiem, ale z różnych perspektyw:",
            "fPerspective": (
                "Projekt F — kosmos: jak stworzyć sztuczne środowisko podtrzymujące życie tam, "
                "gdzie naturalne warunki są dla człowieka nieprzyjazne. Koncentruje się na "
                "inżynierii środowiska i adaptacji do warunków pozaziemskich."
            ),
            "gPerspective": (
                "Projekt G — Ziemia: jak żyć w istniejącym, złożonym ekosystemie i chronić "
                "jego zdolność do podtrzymywania życia. Koncentruje się na ekologii, zdrowiu "
                "człowieka, zrównoważonej technologii i ochronie biosfery."
            ),
        },
    },
    "tracks": [
        {
            "id": "A",
            "code": "Projekt A",
            "name": "Człowiek biocyfrowo-robotyczny",
            "color": "#38bdf8",
            "goal": "Wspomaganie, naprawa i rozszerzanie możliwości ludzkiego organizmu.",
            "guidingQuestion": "Jak technologia może wspierać i rozszerzać możliwości człowieka?",
            "note": "",
            "sections": [
                {
                    "title": "Zakres badawczy",
                    "items": [
                        "Medycyna regeneracyjna, protezy i sztuczne narządy.",
                        "Robotyka, bioelektronika i inżynieria biomedyczna.",
                        "Interfejsy mózg–komputer.",
                        "Wspomaganie ludzkich zmysłów i funkcji ruchowych.",
                    ],
                }
            ],
        },
        {
            "id": "B",
            "code": "Projekt B",
            "name": "Cyfrowy umysł",
            "color": "#a855f7",
            "goal": "Poznanie zasad działania mózgu i zbadanie możliwości jego komputerowego modelowania.",
            "guidingQuestion": "Czy można odtworzyć działanie umysłu w komputerze i co oznaczałoby takie odtworzenie?",
            "note": "Pełne przeniesienie umysłu do komputera pozostaje hipotetycznym celem badawczym.",
            "sections": [
                {
                    "title": "Zakres badawczy",
                    "items": [
                        "Neurobiologia i neuronauka obliczeniowa.",
                        "Modelowanie neuronów i sieci neuronalnych.",
                        "Konektomika i poznanie.",
                        "Świadomość oraz hipotetyczna emulacja całego mózgu.",
                    ],
                }
            ],
        },
        {
            "id": "C",
            "code": "Projekt C",
            "name": "Maszyny analogowe i obliczanie przez fizykę",
            "color": "#f59e0b",
            "goal": "Poznanie alternatywnych sposobów realizowania obliczeń.",
            "guidingQuestion": "Jak wykorzystać właściwości fizyczne układów do efektywnego obliczania i modelowania procesów podobnych do pracy mózgu?",
            "note": "",
            "sections": [
                {
                    "title": "Zakres badawczy",
                    "items": [
                        "Komputery analogowe i mechaniczne.",
                        "Elektronika analogowa i układy dynamiczne.",
                        "Komputery neuromorficzne.",
                        "Fizyczne modele neuronów.",
                        "Systemy hybrydowe analogowo-cyfrowe.",
                    ],
                }
            ],
        },
        {
            "id": "D",
            "code": "Projekt D",
            "name": "„Frankenstein”: tworzenie człowieka i science fiction",
            "color": "#10b981",
            "goal": "Poznanie naukowych możliwości tworzenia, odtwarzania i modyfikowania organizmów.",
            "guidingQuestion": "Co można rzeczywiście stworzyć lub zmodyfikować w żywym organizmie, a co pozostaje fikcją?",
            "note": "",
            "sections": [
                {
                    "title": "Zakres badawczy",
                    "items": [
                        "Genetyka, DNA i regulacja genów.",
                        "Embriologia i rozwój organizmu.",
                        "Klonowanie i komórki macierzyste.",
                        "Inżynieria tkankowa i sztuczne narządy.",
                        "Biologia syntetyczna i edycja genomu.",
                        "Bioetyka oraz naukowe podstawy science fiction.",
                    ],
                }
            ],
        },
        {
            "id": "E",
            "code": "Projekt E",
            "name": "Filozofia jako warstwa przekrojowa",
            "color": "#eab308",
            "goal": "Interpretowanie osiągnięć nauki i badanie granic poznania.",
            "guidingQuestion": "Co wiemy, jak to uzasadniamy i jakie konsekwencje wynikają z naszej wiedzy?",
            "note": "Filozofia pozostaje osobnym obszarem nauki, rozwijanym niezależnie. W tym projekcie jest nakładką interpretacyjną na pozostałe ścieżki, a nie dodatkowym obowiązkowym przedmiotem.",
            "sections": [
                {
                    "title": "Zakres badawczy",
                    "items": [
                        "Filozofia starożytna: Platon, Arystoteles i stoicy.",
                        "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
                        "Filozofia umysłu: świadomość, tożsamość i natura myślenia.",
                        "Filozofia techniki: wpływ technologii na człowieka i społeczeństwo.",
                        "Etyka tworzenia, modyfikowania i ulepszania organizmów.",
                    ],
                }
            ],
        },
        {
            "id": "F",
            "code": "Projekt F",
            "name": "Człowiek w kosmosie",
            "color": "#6366f1",
            "goal": "Poznanie sposobów przystosowania technologii, organizmu człowieka i środowiska życia do podróży kosmicznych oraz długotrwałej obecności poza Ziemią.",
            "guidingQuestion": "Jak stworzyć warunki, w których człowiek może bezpiecznie podróżować i żyć poza Ziemią, nie zakładając, że jego organizm łatwo przystosuje się do każdego środowiska?",
            "note": "",
            "sections": [
                {
                    "title": "A. Technologia podróży kosmicznych",
                    "items": [
                        "Mechanika orbitalna i podstawy astronautyki.",
                        "Napędy rakietowe i przyszłe koncepcje napędu.",
                        "Konstrukcja statków kosmicznych i habitatów.",
                        "Systemy podtrzymywania życia: tlen, woda, żywność i gospodarka odpadami.",
                        "Osłony przed promieniowaniem i mikrometeoroidami.",
                        "Robotyka, automatyzacja i autonomiczne systemy.",
                        "Energetyka, magazynowanie energii i niezawodność urządzeń.",
                        "Wykorzystanie zasobów lokalnych na Księżycu i Marsie.",
                    ],
                },
                {
                    "title": "B. Przystosowanie organizmu człowieka",
                    "items": [
                        "Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.",
                        "Promieniowanie kosmiczne i jego skutki biologiczne.",
                        "Równowaga, wzrok, sen i rytm dobowy.",
                        "Żywienie, ćwiczenia i profilaktyka zdrowotna astronautów.",
                        "Medycyna kosmiczna i samodzielna diagnostyka.",
                        "Biologia regeneracji i możliwości ograniczania skutków długich misji.",
                        "Granice biologicznej adaptacji człowieka do innych warunków grawitacyjnych.",
                    ],
                },
                {
                    "title": "C. Długotrwałe życie poza Ziemią",
                    "items": [
                        "Zamknięte i częściowo zamknięte systemy podtrzymywania życia.",
                        "Uprawa roślin i produkcja żywności w habitatach.",
                        "Psychologia izolacji i funkcjonowanie małych załóg.",
                        "Budowa baz księżycowych i marsjańskich.",
                        "Terraformowanie jako odrębna, wysoce spekulatywna koncepcja.",
                        "Etyka ekspansji kosmicznej i ochrona innych światów przed biologicznym skażeniem.",
                    ],
                },
            ],
        },
        {
            "id": "G",
            "code": "Projekt G",
            "name": "Człowiek na Ziemi: adaptacja i ochrona ekosystemu",
            "color": "#22c55e",
            "goal": "Zrozumienie zależności między ludzkim organizmem, cywilizacją techniczną i ziemskim środowiskiem oraz opracowanie sposobów życia, które nie niszczą podstaw własnego istnienia.",
            "guidingQuestion": "Jak człowiek może przystosować swoje życie i technologię do warunków Ziemi, chroniąc jednocześnie ekosystemy, od których zależy?",
            "note": "",
            "sections": [
                {
                    "title": "A. Człowiek jako organizm ziemski",
                    "items": [
                        "Fizjologia człowieka i adaptacja do temperatury, wysokości oraz wysiłku.",
                        "Wpływ środowiska na zdrowie, odporność i rozwój.",
                        "Relacje człowieka z mikroorganizmami i mikrobiomem.",
                        "Znaczenie wody, powietrza, gleby i pożywienia.",
                        "Ograniczenia biologiczne człowieka i zdolność organizmu do adaptacji.",
                        "Wpływ miejskiego środowiska, hałasu, światła i zanieczyszczeń na organizm.",
                    ],
                },
                {
                    "title": "B. Ekologia i funkcjonowanie ekosystemów",
                    "items": [
                        "Ekologia organizmów, populacji i całych ekosystemów.",
                        "Różnorodność biologiczna i stabilność środowiska.",
                        "Obiegi węgla, azotu, fosforu i wody.",
                        "Gleby, lasy, oceany i ekosystemy słodkowodne.",
                        "Zależności pokarmowe i wzajemne powiązania gatunków.",
                        "Zmiany klimatu, zanieczyszczenia i utrata siedlisk.",
                        "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.",
                    ],
                },
                {
                    "title": "C. Technologia przyjazna środowisku",
                    "items": [
                        "Odnawialne źródła energii i magazynowanie energii.",
                        "Efektywność energetyczna budynków, transportu i przemysłu.",
                        "Gospodarka obiegu zamkniętego i ograniczanie odpadów.",
                        "Oczyszczanie wody i powietrza.",
                        "Rolnictwo zrównoważone i ochrona gleb.",
                        "Materiały biodegradowalne i ograniczanie toksycznych substancji.",
                        "Monitoring środowiska z wykorzystaniem czujników, satelitów i sztucznej inteligencji.",
                        "Ocena rzeczywistego wpływu technologii na środowisko w całym cyklu jej życia.",
                    ],
                },
                {
                    "title": "D. Cywilizacja a granice środowiskowe",
                    "items": [
                        "Zużycie zasobów i możliwości ich odtwarzania.",
                        "Rozwój miast i infrastruktury.",
                        "Bezpieczeństwo żywnościowe i wodne.",
                        "Odporność społeczeństw na katastrofy i zmiany klimatyczne.",
                        "Konflikt między krótkoterminowym zyskiem a długoterminową stabilnością.",
                        "Polityka środowiskowa, ekonomia ekologiczna i odpowiedzialność międzypokoleniowa.",
                    ],
                },
            ],
        },
    ],
    "subprojects": [
        {
            "id": "sub-1",
            "trackId": "A",
            "secondaryTracks": ["B", "E"],
            "branchTopic": "Interfejsy mózg–komputer.",
            "title": "Dekodowanie intencji ruchowej i sprzężenie czuciowe w neuroprotezach",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:00:00Z",
            "description": "Badanie dwukierunkowych interfejsów korowo-obwodowych pozwalających nie tylko sterować efektorami, ale też odbierać sygnały proprioceptywne i dotykowe.",
            "philosophicalNote": "Pytanie o granice schematu ciała i podmiotowości: kiedy sztuczny efektor staje się integralną częścią doświadczenia użytkownika?",
            "workspace": {
                "hypotheses": [
                    {
                        "id": "hyp-1",
                        "statement": "Zamknięcie pętli sprzężenia zwrotnego o opóźnieniu < 25 ms znacząco przyspiesza neuroplastyczną integrację protezy ze schematem ciała.",
                        "status": "W weryfikacji",
                        "author": "Administrator",
                        "approvalStatus": "approved",
                    }
                ],
                "notes": [
                    {
                        "id": "note-1",
                        "title": "Granica inwazyjności a stabilność sygnału",
                        "content": "Matryce mikroelektrod zapewniają wysoką rozdzielczość przestrzenną, ale ulegają gliozie. Alternatywą są podejścia wewnątrznaczyniowe (Stentrode) oraz optogenetyczne.",
                        "author": "Administrator",
                        "createdAt": "2026-10-25T12:10:00Z",
                        "approvalStatus": "approved",
                    }
                ],
                "bibliography": [
                    {
                        "id": "bib-1",
                        "citation": "Lebedev, M. A., & Nicolelis, M. A. (2017). Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation. Physiological Reviews.",
                        "url": "https://doi.org/10.1152/physrev.00027.2016",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    }
                ],
            },
        },
        {
            "id": "sub-2",
            "trackId": "C",
            "secondaryTracks": ["B", "A"],
            "branchTopic": "Komputery neuromorficzne.",
            "title": "Oscylatory relaksacyjne i memrystorowe synapsy w obliczeniach ciągłych",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:15:00Z",
            "description": "Środowisko badawcze poświęcone fizycznej realizacji impulsowych sieci neuronowych (SNN) w domenie analogowej bez dyskretyzacji zegarowej.",
            "philosophicalNote": "Czy obliczanie ciągłe realizowane bezpośrednio przez prawa fizyki układu analogowego przekracza ograniczenia klasycznych modeli symbolicznych?",
            "workspace": {
                "hypotheses": [
                    {
                        "id": "hyp-2",
                        "statement": "Szum termiczny w układach submikronowych może pełnić funkcję rezonansu stochastycznego, obniżając próg energetyczny detekcji słabych sygnałów.",
                        "status": "Hipoteza otwarta",
                        "author": "Administrator",
                        "approvalStatus": "approved",
                    }
                ],
                "notes": [
                    {
                        "id": "note-2",
                        "title": "Porównanie modelu Hodgkina-Huxleya i obwodu FitzHugh-Nagumo",
                        "content": "Układ analogowy FHN pozwala odwzorować pobudliwość błony przy użyciu pojedynczego nieliniowego elementu i indukcyjności (lub żyratora CMOS).",
                        "author": "Administrator",
                        "createdAt": "2026-10-25T12:20:00Z",
                        "approvalStatus": "approved",
                    }
                ],
                "bibliography": [
                    {
                        "id": "bib-2",
                        "citation": "Indiveri, G., et al. (2011). Neuromorphic silicon neuron circuits. Frontiers in Neuroscience.",
                        "url": "https://doi.org/10.3389/fnins.2011.00073",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    }
                ],
            },
        },
        {
            "id": "sub-3",
            "trackId": "F",
            "secondaryTracks": ["G", "D"],
            "branchTopic": "Zamknięte i częściowo zamknięte systemy podtrzymywania życia.",
            "title": "Bioregeneracyjne systemy podtrzymywania życia (BLSS) — obieg pierwiastków w habitacie i na Ziemi",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:30:00Z",
            "description": "Porównanie małych, sztucznie domykanych pętli metabolicznych (fotobioreaktory mikroglonowe + uprawy hydroponiczne) z buforową pojemnością ziemskich ekosystemów.",
            "philosophicalNote": "Próba odtworzenia biosfery w skali mikro uwidacznia niewidoczne na co dzień usługi ekosystemowe Ziemi (Projekt G) oraz kruchość sztucznych habitatów (Projekt F).",
            "workspace": {
                "hypotheses": [
                    {
                        "id": "hyp-3",
                        "statement": "Stabilność mikrobiomu ryzosfery w zamkniętym habitacie wymaga kontrolowanej redundancji gatunkowej wzorowanej na naturalnych glebach z Projektu G.",
                        "status": "W weryfikacji",
                        "author": "Administrator",
                        "approvalStatus": "approved",
                    }
                ],
                "notes": [
                    {
                        "id": "note-3",
                        "title": "Wnioski z eksperymentów MELiSSA i BIOS-3",
                        "content": "Największym wyzwaniem pozostaje pełna mineralizacja odpadów lignocelulozowych oraz utrzymanie równowagi stechiometrycznej O2/CO2 przy zmiennym metabolizmie załogi.",
                        "author": "Administrator",
                        "createdAt": "2026-10-25T12:35:00Z",
                        "approvalStatus": "approved",
                    }
                ],
                "bibliography": [
                    {
                        "id": "bib-3",
                        "citation": "Lasseur, C., et al. (2010). MELiSSA: The European project of closed life support system. Gravitational and Space Biology.",
                        "url": "",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    }
                ],
            },
        },
    ],
    "materials": [
        {
            "id": "mat-1",
            "trackId": "E",
            "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "subprojectId": None,
            "title": "Granice modeli formalnych a interpretacja stanów umysłowych i biologicznych",
            "type": "Artykuł / Notatka przekrojowa",
            "author": "Administrator",
            "content": "Rozróżnienie między symulacją składniową (syntaktyczną) a realizacją właściwości przyczynowych układu fizycznego — punkt styku Projektu B, C oraz E.",
            "url": "",
            "status": "approved",
            "createdAt": "2026-10-25T11:50:00Z",
        },
        {
            "id": "mat-2",
            "trackId": "B",
            "branchTopic": "Neurobiologia i neuronauka obliczeniowa.",
            "subprojectId": "sub-1",
            "title": "Zestawienie rozdzielczości czasowo-przestrzennej metod neuroobrazowania (EEG, fNIRS, fMRI, ECoG)",
            "type": "Zestaw danych / Opracowanie",
            "author": "Dr Janina Kowalska (Gość)",
            "content": "Porównanie pasma przenoszenia, stosunku sygnału do szumu (SNR) oraz biokompatybilności długoterminowej dla zastosowań w Projektach A i B.",
            "url": "https://example.org/neuro-resolution-matrix",
            "status": "pending",
            "createdAt": "2026-10-25T13:10:00Z",
        },
    ],
    "graphLinks": [
        {"id": "lnk-1", "source": "A", "target": "B", "label": "Interfejsy mózg–komputer i dekodowanie sygnałów nerwowych", "status": "approved"},
        {"id": "lnk-2", "source": "B", "target": "C", "label": "Fizyczne i neuromorficzne modele sieci neuronalnych", "status": "approved"},
        {"id": "lnk-3", "source": "A", "target": "D", "label": "Inżynieria tkankowa, sztuczne narządy i medycyna regeneracyjna", "status": "approved"},
        {"id": "lnk-4", "source": "F", "target": "G", "label": "Zamknięte obiegi materii (BLSS) vs. ziemska biosfera i ekologia", "status": "approved"},
        {"id": "lnk-5", "source": "A", "target": "F", "label": "Medycyna kosmiczna, ochrona organizmu i robotyka autonomiczna", "status": "approved"},
        {"id": "lnk-6", "source": "D", "target": "F", "label": "Biologia regeneracji i odporność radiacyjna w długich misjach", "status": "approved"},
        {"id": "lnk-7", "source": "E", "target": "A", "label": "Filozofia techniki i etyka ulepszania człowieka", "status": "approved"},
        {"id": "lnk-8", "source": "E", "target": "B", "label": "Filozofia umysłu, świadomość i granice modeli obliczeniowych", "status": "approved"},
        {"id": "lnk-9", "source": "E", "target": "D", "label": "Bioetyka edycji genomu i granice tworzenia organizmów", "status": "approved"},
        {"id": "lnk-10", "source": "E", "target": "F", "label": "Etyka ekspansji kosmicznej i ochrona planetarna", "status": "approved"},
        {"id": "lnk-11", "source": "E", "target": "G", "label": "Odpowiedzialność międzypokoleniowa i filozofia przyrody", "status": "approved"},
    ],
}

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_FILE = os.path.join(DATA_DIR, "database.json")
SEED_FILE = os.path.join(DATA_DIR, "seed.json")


def load_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    if os.path.exists(SEED_FILE):
        try:
            with open(SEED_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            save_db(data)
            return data
        except Exception:
            pass
    data = json.loads(json.dumps(DEFAULT_SEED))
    save_db(data)
    return data


def save_db(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_all_branches_for_track(tracks, track_id):
    for t in tracks:
        if t["id"] == track_id:
            items = []
            for sec in t.get("sections", []):
                items.extend(sec.get("items", []))
            return items
    return []


def count_pending(db):
    total = 0
    for m in db.get("materials", []):
        if m.get("status") == "pending":
            total += 1
    for sp in db.get("subprojects", []):
        if sp.get("status") == "pending":
            total += 1
        ws = sp.get("workspace", {})
        for col in ("hypotheses", "notes", "bibliography"):
            for item in ws.get(col, []):
                if item.get("approvalStatus") == "pending":
                    total += 1
    for lnk in db.get("graphLinks", []):
        if lnk.get("status") == "pending":
            total += 1
    return total


# ==============================================================================
# INICJALIZACJA STANU SESJI
# ==============================================================================
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "selected_subproject_id" not in st.session_state:
    st.session_state.selected_subproject_id = "sub-1"
if "preselect_track" not in st.session_state:
    st.session_state.preselect_track = "A"
if "preselect_branch" not in st.session_state:
    st.session_state.preselect_branch = ""

db = load_db()
pending_count = count_pending(db)
tracks_by_id = {t["id"]: t for t in db["tracks"]}

# ==============================================================================
# PASEK BOCZNY: ROLA UŻYTKOWNIKA (GOŚĆ vs ADMINISTRATOR) I SZYBKIE AKCJE
# ==============================================================================
with st.sidebar:
    st.markdown("## 🧬 Golem XV")
    st.caption("Ludzie: Droga do Rzeczywistości — Platforma Badawcza")
    st.divider()

    if st.session_state.is_admin:
        st.success("★ **Tryb Administratora**\nPełne uprawnienia do zatwierdzania zgłoszeń i publikacji.")
        if st.button("Wyloguj do trybu Gościa", use_container_width=True):
            st.session_state.is_admin = False
            st.rerun()
    else:
        st.info(
            "👁 **Tryb Gościa / Obserwatora**\n"
            "Możesz dodawać materiały, nowe podprojekty i uruchamiać środowiska badawcze. "
            "Publiczna publikacja wymaga zatwierdzenia przez Administratora."
        )
        with st.expander("🔐 Logowanie Administratora"):
            admin_pass = st.text_input("Hasło Administratora", type="password", placeholder="Domyślne: golem15")
            if st.button("Zaloguj jako Administrator", use_container_width=True):
                expected = os.environ.get("GOLEM_ADMIN_PASSWORD", "golem15")
                if admin_pass == expected:
                    st.session_state.is_admin = True
                    st.rerun()
                else:
                    st.error("Nieprawidłowe hasło administratora.")

    st.divider()
    st.markdown("### 📊 Statystyki projektu")
    col_s1, col_s2 = st.columns(2)
    col_s1.metric("Ścieżki główne", len(db["tracks"]))
    col_s2.metric("Środowiska", len(db["subprojects"]))
    col_s3, col_s4 = st.columns(2)
    col_s3.metric("Materiały", len(db["materials"]))
    col_s4.metric("Do akceptacji", pending_count)

    st.divider()
    st.download_button(
        "⬇ Pobierz kopię bazy JSON",
        data=json.dumps(db, ensure_ascii=False, indent=2),
        file_name="golem_xv_database.json",
        mime="application/json",
        use_container_width=True,
    )

# ==============================================================================
# NAGŁÓWEK GŁÓWNY
# ==============================================================================
st.title("🧬 Golem XV — Ludzie: Droga do Rzeczywistości")
st.markdown(f"**Cel nadrzędny:** {db['projectMeta']['overarchingGoal']}")

with st.expander("📐 Wspólne podstawy naukowe, zasada organizacyjna oraz relacja Projektów F i G", expanded=False):
    st.markdown("**Wspólne podstawy:** " + " • ".join(f"`{f}`" for f in db["projectMeta"]["foundations"]))
    st.markdown(f"**Zasada organizacyjna:** {db['projectMeta']['organizationalRule']}")
    st.info(
        f"**Relacja między projektami F i G:**\n"
        f"- {db['projectMeta']['fgRelation']['fPerspective']}\n"
        f"- {db['projectMeta']['fgRelation']['gPerspective']}"
    )

# ==============================================================================
# ZAKŁADKI GŁÓWNE APLIKACJI
# ==============================================================================
tab_map, tab_ws, tab_mat, tab_new, tab_graph, tab_admin = st.tabs([
    "🗺️ Mapa 7 Ścieżek (A–G)",
    f"🔬 Środowiska Badawcze ({len(db['subprojects'])})",
    f"📚 Materiały Badawcze ({len(db['materials'])})",
    "🚀 + Uruchom Podprojekt / Dodaj Materiał",
    "🕸️ Powiązania Międzyścieżkowe",
    f"🛡️ Autoryzacja Administratora ({pending_count})",
])

# ------------------------------------------------------------------------------
# ZAKŁADKA 1: MAPA 7 ŚCIEŻEK (A-G)
# ------------------------------------------------------------------------------
with tab_map:
    st.subheader("Siedem powiązanych ścieżek badawczych (Projekty A–G)")
    st.caption(
        "Każda ścieżka posiada własne pytanie przewodnie, zakres i odnogi badawcze. "
        "Możesz uruchamiać nowe środowiska badawcze oraz dodawać materiały do każdej odnogi."
    )

    for track in db["tracks"]:
        tid = track["id"]
        sub_list = [
            s for s in db["subprojects"]
            if s["trackId"] == tid and (s["status"] == "approved" or st.session_state.is_admin)
        ]
        mat_list = [
            m for m in db["materials"]
            if m["trackId"] == tid and (m["status"] == "approved" or st.session_state.is_admin)
        ]

        with st.container(border=True):
            c_head1, c_head2 = st.columns([4, 1])
            with c_head1:
                badge = " • WARSTWA PRZEKROJOWA" if tid == "E" else ""
                st.markdown(f"### {track['code']} — {track['name']}{badge}")
                st.markdown(f"**Cel:** {track['goal']}")
                st.markdown(f"> **Pytanie przewodnie:** *{track['guidingQuestion']}*")
                if track.get("note"):
                    st.warning(track["note"])
            with c_head2:
                st.metric("Aktywne środowiska", len(sub_list))
                st.metric("Materiały", len(mat_list))

            cols_sec = st.columns(len(track["sections"]))
            for idx, sec in enumerate(track["sections"]):
                with cols_sec[idx]:
                    st.markdown(f"**{sec['title']}:**")
                    for item in sec["items"]:
                        st.markdown(f"- {item}")

            if sub_list:
                st.markdown("**Powiązane podprojekty i środowiska badawcze w tej ścieżce:**")
                for sp in sub_list:
                    st.markdown(f"- 🔬 **{sp['title']}** *(odnoga: {sp.get('branchTopic', 'Ogólna')})*")

# ------------------------------------------------------------------------------
# ZAKŁADKA 2: ŚRODOWISKA BADAWCZE I PODPROJEKTY
# ------------------------------------------------------------------------------
with tab_ws:
    st.subheader("🔬 Wirtualne Środowiska Badawcze i Podprojekty")
    visible_sps = [
        sp for sp in db["subprojects"]
        if sp.get("status") == "approved" or st.session_state.is_admin
    ]

    if not visible_sps:
        st.info("Brak zatwierdzonych środowisk badawczych. Utwórz nowe w zakładce „🚀 + Uruchom Podprojekt / Dodaj Materiał”.")
    else:
        col_sel, col_filter = st.columns([2, 1])
        with col_filter:
            track_filter = st.selectbox(
                "Filtruj wg ścieżki (A–G)",
                options=["WSZYSTKIE"] + [t["id"] for t in db["tracks"]],
                format_func=lambda x: "Wszystkie ścieżki (A–G)" if x == "WSZYSTKIE" else f"{tracks_by_id[x]['code']} — {tracks_by_id[x]['name']}",
            )
        filtered_sps = [
            sp for sp in visible_sps
            if track_filter == "WSZYSTKIE" or sp["trackId"] == track_filter or track_filter in sp.get("secondaryTracks", [])
        ]

        if not filtered_sps:
            st.warning("Brak podprojektów dla wybranej ścieżki.")
        else:
            with col_sel:
                selected_sp_id = st.selectbox(
                    "Wybierz aktywne środowisko badawcze:",
                    options=[sp["id"] for sp in filtered_sps],
                    format_func=lambda sid: next(
                        (f"[{s['trackId']}] {s['title']} ({'Oczekuje na zgodę' if s['status'] == 'pending' else 'Aktywne'})" for s in filtered_sps if s["id"] == sid),
                        sid,
                    ),
                )

            active_sp = next((s for s in filtered_sps if s["id"] == selected_sp_id), filtered_sps[0])
            ws = active_sp.setdefault("workspace", {"hypotheses": [], "notes": [], "bibliography": []})

            with st.container(border=True):
                st.markdown(f"## {active_sp['title']}")
                sec_tracks = ", ".join(f"Projekt {t}" for t in active_sp.get("secondaryTracks", []))
                status_txt = "🟢 Zatwierdzone środowisko badawcze" if active_sp.get("status") == "approved" else "🟡 Oczekuje na zgodę Administratora"
                st.caption(
                    f"**Główna ścieżka:** Projekt {active_sp['trackId']} | "
                    f"**Odnoga:** {active_sp.get('branchTopic', 'Ogólna')} | "
                    f"**Powiązania:** {sec_tracks or 'Brak'} | "
                    f"**Autor:** {active_sp.get('author', 'Gość')} | {status_txt}"
                )
                st.write(active_sp.get("description", ""))
                if active_sp.get("philosophicalNote"):
                    st.info(f"**Nakładka interpretacyjna (Projekt E — Filozofia):** {active_sp['philosophicalNote']}")

            col_h, col_n, col_b = st.columns(3)

            # Kolumna 1: Hipotezy badawcze
            with col_h:
                st.markdown("#### 1. Hipotezy badawcze")
                hyps = [
                    h for h in ws.get("hypotheses", [])
                    if h.get("approvalStatus", "approved") == "approved" or st.session_state.is_admin
                ]
                for h in hyps:
                    with st.container(border=True):
                        badge = "⏳ Do akceptacji" if h.get("approvalStatus") == "pending" else h.get("status", "Hipoteza otwarta")
                        st.caption(f"Status: **{badge}** | Autor: {h.get('author', 'Gość')}")
                        st.write(h["statement"])
                with st.popover("➕ Dodaj hipotezę do środowiska", use_container_width=True):
                    with st.form(f"form_hyp_{active_sp['id']}"):
                        h_stmt = st.text_area("Treść hipotezy badawczej")
                        h_stat = st.selectbox("Status", ["Hipoteza otwarta", "W weryfikacji", "Potwierdzona częściowo", "Wymaga korekty"])
                        h_auth = st.text_input("Autor", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
                        if st.form_submit_button("Zapisz hipotezę"):
                            if h_stmt.strip():
                                ws.setdefault("hypotheses", []).append({
                                    "id": f"hyp-{int(time.time()*1000)}",
                                    "statement": h_stmt.strip(),
                                    "status": h_stat,
                                    "author": h_auth.strip() or "Gość",
                                    "approvalStatus": "approved" if st.session_state.is_admin else "pending",
                                })
                                save_db(db)
                                st.success("Zapisano hipotezę!")
                                st.rerun()

            # Kolumna 2: Notatnik laboratoryjny
            with col_n:
                st.markdown("#### 2. Notatnik badawczy")
                notes = [
                    n for n in ws.get("notes", [])
                    if n.get("approvalStatus", "approved") == "approved" or st.session_state.is_admin
                ]
                for n in notes:
                    with st.container(border=True):
                        st.markdown(f"**{n['title']}**")
                        if n.get("approvalStatus") == "pending":
                            st.caption("⏳ Oczekuje na akceptację Administratora")
                        st.write(n["content"])
                        st.caption(f"Autor: {n.get('author', 'Gość')}")
                with st.popover("➕ Dodaj notatkę badawczą", use_container_width=True):
                    with st.form(f"form_note_{active_sp['id']}"):
                        n_title = st.text_input("Tytuł obserwacji / notatki")
                        n_content = st.text_area("Treść notatki")
                        n_auth = st.text_input("Autor", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
                        if st.form_submit_button("Zapisz notatkę"):
                            if n_title.strip() and n_content.strip():
                                ws.setdefault("notes", []).append({
                                    "id": f"note-{int(time.time()*1000)}",
                                    "title": n_title.strip(),
                                    "content": n_content.strip(),
                                    "author": n_auth.strip() or "Gość",
                                    "createdAt": datetime.utcnow().isoformat() + "Z",
                                    "approvalStatus": "approved" if st.session_state.is_admin else "pending",
                                })
                                save_db(db)
                                st.success("Zapisano notatkę!")
                                st.rerun()

            # Kolumna 3: Bibliografia i materiały
            with col_b:
                st.markdown("#### 3. Bibliografia i źródła")
                bibs = [
                    b for b in ws.get("bibliography", [])
                    if b.get("approvalStatus", "approved") == "approved" or st.session_state.is_admin
                ]
                for b in bibs:
                    with st.container(border=True):
                        st.write(f"📖 {b['citation']}")
                        if b.get("url"):
                            st.markdown(f"[🔗 Link / DOI]({b['url']})")
                        st.caption(f"Dodał(a): {b.get('addedBy', 'Gość')}")
                with st.popover("➕ Dodaj źródło bibliograficzne", use_container_width=True):
                    with st.form(f"form_bib_{active_sp['id']}"):
                        b_cit = st.text_area("Cytowanie (Autor, rok, tytuł, źródło)")
                        b_url = st.text_input("Link / DOI (opcjonalnie)")
                        b_auth = st.text_input("Dodał(a)", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
                        if st.form_submit_button("Dodaj źródło"):
                            if b_cit.strip():
                                ws.setdefault("bibliography", []).append({
                                    "id": f"bib-{int(time.time()*1000)}",
                                    "citation": b_cit.strip(),
                                    "url": b_url.strip(),
                                    "addedBy": b_auth.strip() or "Gość",
                                    "approvalStatus": "approved" if st.session_state.is_admin else "pending",
                                })
                                save_db(db)
                                st.success("Dodano pozycję bibliograficzną!")
                                st.rerun()

# ------------------------------------------------------------------------------
# ZAKŁADKA 3: REPOZYTORIUM MATERIAŁÓW BADAWCZYCH
# ------------------------------------------------------------------------------
with tab_mat:
    st.subheader("📚 Repozytorium Materiałów Badawczych")
    c_m1, c_m2 = st.columns([1, 2])
    with c_m1:
        m_track_filter = st.selectbox(
            "Ścieżka projektu",
            options=["WSZYSTKIE"] + [t["id"] for t in db["tracks"]],
            format_func=lambda x: "Wszystkie ścieżki (A–G)" if x == "WSZYSTKIE" else f"{tracks_by_id[x]['code']} — {tracks_by_id[x]['name']}",
            key="mat_track_filter",
        )
    with c_m2:
        m_search = st.text_input("Szukaj w materiałach (tytuł, treść, autor, odnoga)...")

    mats = [
        m for m in db["materials"]
        if (m.get("status") == "approved" or st.session_state.is_admin)
        and (m_track_filter == "WSZYSTKIE" or m["trackId"] == m_track_filter)
        and (
            not m_search.strip()
            or m_search.lower() in f"{m.get('title','')} {m.get('content','')} {m.get('author','')} {m.get('branchTopic','')}".lower()
        )
    ]

    if not mats:
        st.info("Brak materiałów dla wybranych kryteriów.")
    for m in mats:
        with st.container(border=True):
            status_badge = "🟢 Zatwierdzony" if m.get("status") == "approved" else "🟡 Oczekuje na zgodę Administratora"
            st.caption(f"**Projekt {m['trackId']}** • {m.get('type', 'Materiał')} • Odnoga: *{m.get('branchTopic') or 'Ogólna'}* • {status_badge}")
            st.markdown(f"### {m['title']}")
            st.write(m["content"])
            if m.get("url"):
                st.markdown(f"[🔗 Otwórz źródło zewnętrzne / DOI]({m['url']})")
            st.caption(f"Zgłosił(a): **{m.get('author', 'Gość')}**")

# ------------------------------------------------------------------------------
# ZAKŁADKA 4: DODAWANIE PODPROJEKTÓW I MATERIAŁÓW PRZEZ GOŚCI / ADMINA
# ------------------------------------------------------------------------------
with tab_new:
    st.subheader("🚀 Inicjowanie nowych podprojektów / środowisk oraz dodawanie materiałów")
    if not st.session_state.is_admin:
        st.info(
            "Jako **Gość / Obserwator zewnętrzny** możesz swobodnie zgłaszać nowe materiały oraz inicjować "
            "podprojekty i środowiska badawcze dla dowolnej odnogi projektów A–G. Po zatwierdzeniu przez "
            "Administratora staną się one widoczne dla wszystkich odwiedzających."
        )

    col_form_sp, col_form_mat = st.columns(2)

    with col_form_sp:
        st.markdown("### 🔬 1. Uruchom nowy podprojekt i środowisko badawcze")
        sp_track = st.selectbox(
            "Wybierz główną ścieżkę (Projekt A–G)",
            options=[t["id"] for t in db["tracks"]],
            format_func=lambda x: f"{tracks_by_id[x]['code']} — {tracks_by_id[x]['name']}",
            key="new_sp_track",
        )
        available_branches = get_all_branches_for_track(db["tracks"], sp_track)
        with st.form("create_subproject_form"):
            sp_branch = st.selectbox("Odnoga badawcza z zakresu ścieżki", options=available_branches + ["Inna / Nowa odnoga badawcza"])
            sp_custom_branch = st.text_input("Jeśli wybrano inną odnogę — wpisz jej nazwę (opcjonalnie)")
            sp_title = st.text_input("Tytuł podprojektu / środowiska badawczego*")
            sp_secondary = st.multiselect(
                "Powiązane ścieżki dodatkowe",
                options=[t["id"] for t in db["tracks"] if t["id"] != sp_track],
                default=["E"] if sp_track != "E" else [],
            )
            sp_desc = st.text_area("Cel i opis problemu badawczego*")
            sp_hyp = st.text_input("Hipoteza startowa (automatycznie otworzy moduł hipotez)")
            sp_phil = st.text_input("Nakładka interpretacyjna (Projekt E — Filozofia)")
            sp_author = st.text_input("Autor / Inicjator*", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator zewnętrzny")

            if st.form_submit_button("🚀 Uruchom środowisko badawcze", use_container_width=True):
                if not sp_title.strip() or not sp_desc.strip():
                    st.error("Podaj tytuł oraz opis podprojektu.")
                else:
                    final_branch = sp_custom_branch.strip() if sp_custom_branch.strip() else sp_branch
                    approval = "approved" if st.session_state.is_admin else "pending"
                    new_sp = {
                        "id": f"sub-{int(time.time()*1000)}",
                        "trackId": sp_track,
                        "secondaryTracks": sp_secondary,
                        "branchTopic": final_branch,
                        "title": sp_title.strip(),
                        "author": sp_author.strip() or "Gość",
                        "status": approval,
                        "createdAt": datetime.utcnow().isoformat() + "Z",
                        "description": sp_desc.strip(),
                        "philosophicalNote": sp_phil.strip(),
                        "workspace": {
                            "hypotheses": [
                                {
                                    "id": f"hyp-{int(time.time()*1000)}",
                                    "statement": sp_hyp.strip(),
                                    "status": "Hipoteza otwarta",
                                    "author": sp_author.strip() or "Gość",
                                    "approvalStatus": approval,
                                }
                            ] if sp_hyp.strip() else [],
                            "notes": [],
                            "bibliography": [],
                        },
                    }
                    db["subprojects"].insert(0, new_sp)
                    save_db(db)
                    if st.session_state.is_admin:
                        st.success("Nowe środowisko badawcze zostało uruchomione i opublikowane!")
                    else:
                        st.success("Środowisko badawcze zostało utworzone i przekazane do akceptacji Administratora!")
                    st.rerun()

    with col_form_mat:
        st.markdown("### 📚 2. Dodaj nowy materiał badawczy")
        mat_track = st.selectbox(
            "Wybierz ścieżkę dla materiału (Projekt A–G)",
            options=[t["id"] for t in db["tracks"]],
            format_func=lambda x: f"{tracks_by_id[x]['code']} — {tracks_by_id[x]['name']}",
            key="new_mat_track",
        )
        mat_branches = get_all_branches_for_track(db["tracks"], mat_track)
        with st.form("create_material_form"):
            mat_branch = st.selectbox("Odnoga zakresu", options=mat_branches + ["Ogólna dla ścieżki"])
            mat_type = st.selectbox(
                "Typ materiału",
                [
                    "Artykuł / Opracowanie naukowe",
                    "Zestaw danych / Pomiary",
                    "Model matematyczny / Symulacja",
                    "Analiza filozoficzna / Bioetyczna",
                    "Bibliografia / Źródło zewnętrzne",
                ],
            )
            mat_title = st.text_input("Tytuł materiału*")
            mat_content = st.text_area("Treść / Abstrakt / Wnioski badawcze*")
            mat_url = st.text_input("Link zewnętrzny / DOI (opcjonalnie)")
            mat_author = st.text_input("Autor zgłoszenia*", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator zewnętrzny")

            if st.form_submit_button("📥 Wyślij materiał badawczy", use_container_width=True):
                if not mat_title.strip() or not mat_content.strip():
                    st.error("Wypełnij tytuł oraz opis materiału.")
                else:
                    new_mat = {
                        "id": f"mat-{int(time.time()*1000)}",
                        "trackId": mat_track,
                        "branchTopic": mat_branch,
                        "subprojectId": None,
                        "title": mat_title.strip(),
                        "type": mat_type,
                        "author": mat_author.strip() or "Gość",
                        "content": mat_content.strip(),
                        "url": mat_url.strip(),
                        "status": "approved" if st.session_state.is_admin else "pending",
                        "createdAt": datetime.utcnow().isoformat() + "Z",
                    }
                    db["materials"].insert(0, new_mat)
                    save_db(db)
                    if st.session_state.is_admin:
                        st.success("Materiał został opublikowany!")
                    else:
                        st.success("Materiał został zapisany i oczekuje na zatwierdzenie przez Administratora!")
                    st.rerun()

# ------------------------------------------------------------------------------
# ZAKŁADKA 5: POWIĄZANIA MIĘDZYŚCIEŻKOWE (GRAF RELACJI A-G)
# ------------------------------------------------------------------------------
with tab_graph:
    st.subheader("🕸️ Relacje międzyścieżkowe (A–G) oraz oś Kosmos (F) ↔ Ziemia (G)")
    links = [
        l for l in db.get("graphLinks", [])
        if l.get("status", "approved") == "approved" or st.session_state.is_admin
    ]
    for lnk in links:
        s_tr = tracks_by_id.get(lnk["source"], {"code": lnk["source"], "name": ""})
        t_tr = tracks_by_id.get(lnk["target"], {"code": lnk["target"], "name": ""})
        st.markdown(f"- **{s_tr['code']} ({s_tr['name']})** ↔ **{t_tr['code']} ({t_tr['name']})**: {lnk['label']}")

# ------------------------------------------------------------------------------
# ZAKŁADKA 6: PANEL AUTORYZACJI ADMINISTRATORA (MODERACJA)
# ------------------------------------------------------------------------------
with tab_admin:
    st.subheader("🛡️ Centrum Autoryzacji Administratora")
    if not st.session_state.is_admin:
        st.warning("Zaloguj się jako Administrator w pasku bocznym po lewej stronie, aby zatwierdzać lub odrzucać zgłoszenia gości.")
    else:
        pending_sps = [s for s in db["subprojects"] if s.get("status") == "pending"]
        pending_mats = [m for m in db["materials"] if m.get("status") == "pending"]

        if pending_count > 0:
            if st.button(f"✓ Zatwierdź wszystkie oczekujące zgłoszenia ({pending_count})", type="primary"):
                for s in db["subprojects"]:
                    s["status"] = "approved"
                    ws = s.get("workspace", {})
                    for col in ("hypotheses", "notes", "bibliography"):
                        for item in ws.get(col, []):
                            item["approvalStatus"] = "approved"
                for m in db["materials"]:
                    m["status"] = "approved"
                for l in db.get("graphLinks", []):
                    l["status"] = "approved"
                save_db(db)
                st.success("Zatwierdzono wszystkie oczekujące elementy!")
                st.rerun()

        col_mod1, col_mod2 = st.columns(2)
        with col_mod1:
            st.markdown(f"#### Oczekujące podprojekty i środowiska ({len(pending_sps)})")
            if not pending_sps:
                st.caption("Brak oczekujących podprojektów.")
            for sp in pending_sps:
                with st.container(border=True):
                    st.markdown(f"**[Projekt {sp['trackId']}] {sp['title']}**")
                    st.caption(f"Odnoga: {sp.get('branchTopic')} | Autor: {sp.get('author')}")
                    st.write(sp.get("description"))
                    c1, c2 = st.columns(2)
                    if c1.button("✓ Zatwierdź", key=f"app_sp_{sp['id']}", use_container_width=True):
                        sp["status"] = "approved"
                        save_db(db)
                        st.rerun()
                    if c2.button("✕ Odrzuć", key=f"del_sp_{sp['id']}", use_container_width=True):
                        db["subprojects"] = [x for x in db["subprojects"] if x["id"] != sp["id"]]
                        save_db(db)
                        st.rerun()

        with col_mod2:
            st.markdown(f"#### Oczekujące materiały badawcze ({len(pending_mats)})")
            if not pending_mats:
                st.caption("Brak oczekujących materiałów.")
            for m in pending_mats:
                with st.container(border=True):
                    st.markdown(f"**[Projekt {m['trackId']}] {m['title']}**")
                    st.caption(f"Typ: {m.get('type')} | Autor: {m.get('author')}")
                    st.write(m.get("content"))
                    c1, c2 = st.columns(2)
                    if c1.button("✓ Zatwierdź", key=f"app_m_{m['id']}", use_container_width=True):
                        m["status"] = "approved"
                        save_db(db)
                        st.rerun()
                    if c2.button("✕ Odrzuć", key=f"del_m_{m['id']}", use_container_width=True):
                        db["materials"] = [x for x in db["materials"] if x["id"] != m["id"]]
                        save_db(db)
                        st.rerun()
