import json
import os
import time
from datetime import datetime
import streamlit as st

# ==============================================================================
# KONFIGURACJA STRONY STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="The Golem 15: A Human's Road to Reality",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# WBUDOWANA BAZA STARTOWA (DZIAŁA NAWET GDY WGRASZ SAM PLIK app.py NA GITHUB)
# ==============================================================================
DEFAULT_SEED = {
    "projectMeta": {
        "title": "The Golem 15: A Human's Road to Reality",
        "subtitle": "Mapa projektu badawczego — wspólne podstawy naukowe oraz siedem powiązanych ścieżek (A–G)",
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
    "foundationDisciplines": [
        {
            "id": "FND-1",
            "order": 1,
            "name": "Matematyka i logika",
            "icon": "📐",
            "color": "#38bdf8",
            "description": "Formalny język opisu rzeczywistości, wnioskowania dedukcyjnego, układów dynamicznych, prawdopodobieństwa i informacji.",
            "topics": [
                "Logika formalna, rachunek zdań i kwantyfikatorów, teoria mnogości i dowodzenia.",
                "Analiza matematyczna, rachunek różniczkowy i całkowy, równania różniczkowe zwyczajne i cząstkowe.",
                "Algebra liniowa, przestrzenie wektorowe, tensory i metody spektralne.",
                "Rachunek prawdopodobieństwa, statystyka matematyczna i wnioskowanie bayesowskie.",
                "Teoria informacji, entropia Shannona, teoria układów dynamicznych i chaosu.",
                "Matematyka dyskretna, teoria grafów i topologia sieci (podstawa konektomiki i sieci złożonych).",
            ],
            "connectedTracks": ["A", "B", "C", "E", "F", "G"],
        },
        {
            "id": "FND-2",
            "order": 2,
            "name": "Informatyka",
            "icon": "💻",
            "color": "#60a5fa",
            "description": "Teoria obliczeń, architektura systemów komputerowych, struktury danych, przetwarzanie informacji i cyberbezpieczeństwo.",
            "topics": [
                "Teoria obliczeń, maszyny Turinga, obliczalność i złożoność obliczeniowa.",
                "Algorytmy i struktury danych (grafowe, drzewiaste, probabilistyczne, indeksowanie).",
                "Architektura komputerów (CPU, GPU, pamięci, systemy wbudowane i czasu rzeczywistego).",
                "Systemy operacyjne, współbieżność, systemy rozproszone i obliczenia wysokiej wydajności (HPC).",
                "Bazy danych, reprezentacja wiedzy, ontologie i przetwarzanie wielkich zbiorów danych.",
                "Niezawodność systemów (fault-tolerance) w zastosowaniach medycznych i kosmicznych.",
            ],
            "connectedTracks": ["A", "B", "C", "F", "G"],
        },
        {
            "id": "FND-3",
            "order": 3,
            "name": "Programowanie",
            "icon": "⌨️",
            "color": "#818cf8",
            "description": "Praktyczna konstrukcja oprogramowania, symulacji numerycznych, modeli badawczych, sterowników sprzętowych i narzędzi analitycznych.",
            "topics": [
                "Paradygmaty programowania: imperatywne, obiektowe, funkcyjne i reaktywne.",
                "Python w obliczeniach naukowych i analizie danych (NumPy, SciPy, PyTorch, BioPython).",
                "Języki niskopoziomowe i systemowe (C, C++, Rust) do sterowania robotami, mikrokontrolerami i BCI.",
                "Symulacje numeryczne układów fizycznych, biologicznych i neuronalnych (np. Brian2, NEURON).",
                "Inżynieria oprogramowania, kontrola wersji, testy automatyczne i reprodukowalność badań.",
                "Wizualizacja danych naukowych, interfejsy webowe i wirtualne środowiska badawcze.",
            ],
            "connectedTracks": ["A", "B", "C", "D", "F", "G"],
        },
        {
            "id": "FND-4",
            "order": 4,
            "name": "Fizyka",
            "icon": "⚛️",
            "color": "#f59e0b",
            "description": "Fundamentalne prawa przyrody rządzące materią, energią, polami, termodynamiką układów żywych, obliczaniem fizycznym i astronautyką.",
            "topics": [
                "Mechanika klasyczna, analityczna (Lagrange’a i Hamiltona), biomechanika oraz mechanika orbitalna.",
                "Termodynamika klasyczna i nierównowagowa, fizyka statystyczna i entropia w układach żywych.",
                "Elektrodynamika, fale elektromagnetyczne, optyka i oddziaływanie pól z tkanką biologiczną.",
                "Fizyka ciała stałego i półprzewodników (podstawa elektroniki i układów neuromorficznych).",
                "Mechanika kwantowa, fizyka jądrowa oraz promieniowanie jonizujące (ochrona radiacyjna w kosmosie).",
                "Biofizyka błon komórkowych, transportu jonowego i potencjałów czynnościowych.",
            ],
            "connectedTracks": ["A", "B", "C", "E", "F", "G"],
        },
        {
            "id": "FND-5",
            "order": 5,
            "name": "Elektronika",
            "icon": "🔌",
            "color": "#eab308",
            "description": "Projektowanie układów analogowych, cyfrowych, sensorów pomiarowych, bioelektroniki oraz fizycznych architektur obliczeniowych.",
            "topics": [
                "Teoria obwodów elektrycznych, elementy bierne i czynne, stany nieustalone.",
                "Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy nieliniowe.",
                "Elektronika cyfrowa, układy logiczne, FPGA, mikrokontrolery i systemy SoC.",
                "Akwizycja sygnałów biologicznych (EEG, EMG, EKG): wzmacniacze pomiarowe o niskim szumie i przetworniki ADC/DAC.",
                "Czujniki (sensory) środowiskowe i biomedyczne, aktuatory oraz systemy zasilania i magazynowania energii.",
                "Układy neuromorficzne, memrystory i realizacja sztucznych synaps w krzemie.",
            ],
            "connectedTracks": ["A", "B", "C", "F", "G"],
        },
        {
            "id": "FND-6",
            "order": 6,
            "name": "Chemia",
            "icon": "🧪",
            "color": "#10b981",
            "description": "Budowa cząsteczek, reakcje chemiczne, biochemia metabolizmu, inżynieria biomateriałów oraz zamknięte obiegi pierwiastków.",
            "topics": [
                "Chemia ogólna i nieorganiczna: wiązania chemiczne, stechiometria, równowagi kwasowo-zasadowe i redoks.",
                "Chemia organiczna: grupy funkcyjne, stereochemia, synteza i reaktywność związków węgla.",
                "Biochemia: struktura i funkcja białek, enzymów, lipidów, węglowodanów oraz kwasów nukleinowych (DNA/RNA).",
                "Elektrochemia i chemia fizyczna: potencjały błonowe, ogniwa paliwowe, baterie i elektroliza (np. O2 w kosmosie).",
                "Chemia materiałów: polimery biokompatybilne, hydrożele tkankowe i materiały biodegradowalne.",
                "Chemia środowiska i analityczna: obiegi C, N, P, oczyszczanie wody, powietrza i neutralizacja toksyn.",
            ],
            "connectedTracks": ["A", "D", "F", "G"],
        },
        {
            "id": "FND-7",
            "order": 7,
            "name": "Biologia",
            "icon": "🧬",
            "color": "#22c55e",
            "description": "Nauka o organizacji życia od poziomu molekularnego i komórkowego po fizjologię człowieka, neurobiologię, regenerację i ekologię biosfery.",
            "topics": [
                "Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, sygnalizacja komórkowa.",
                "Genetyka, epigenetyka, genomika i regulacja ekspresji genów.",
                "Anatomia i fizjologia człowieka: układ nerwowy, krążenia, mięśniowo-szkieletowy, odpornościowy i hormonalny.",
                "Neurobiologia: budowa neuronów i gleju, transmisja synaptyczna, plastyczność mózgu i narządy zmysłów.",
                "Biologia rozwoju (embriologia), komórki macierzyste, różnicowanie tkanek i procesy regeneracji.",
                "Mikrobiologia, mikrobiom człowieka oraz ekologia populacji, ekosystemów i biosfery.",
            ],
            "connectedTracks": ["A", "B", "D", "F", "G"],
        },
        {
            "id": "FND-8",
            "order": 8,
            "name": "Sztuczna inteligencja",
            "icon": "🤖",
            "color": "#a855f7",
            "description": "Algorytmy uczenia maszynowego, głębokie sieci neuronowe, dekodowanie sygnałów biologicznych, autonomia robotyczna i modelowanie poznania.",
            "topics": [
                "Podstawy uczenia maszynowego (nadzorowane, nienadzorowane, samonadzorowane) i optymalizacja gradientowa.",
                "Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe sieci neuronowe (SNN).",
                "Uczenie ze wzmocnieniem (Reinforcement Learning) i sterowanie autonomicznymi robotami.",
                "Zastosowania AI w neuroinżynierii (dekodowanie BCI), diagnostyce medycznej i biologii strukturalnej (np. fałdowanie białek).",
                "Modele poznawcze, reprezentacje semantyczne a biologiczne działanie mózgu (porównanie AI i Projektu B).",
                "Interpretowalność modeli (XAI), niezawodność, bezpieczeństwo i filozoficzno-etyczne aspekty AI.",
            ],
            "connectedTracks": ["A", "B", "C", "D", "E", "F", "G"],
        },
    ],
    "studyMaterials": [
        {
            "id": "smat-1",
            "categoryType": "FOUNDATION",
            "targetId": "FND-1",
            "topic": "Analiza matematyczna, rachunek różniczkowy i całkowy, równania różniczkowe zwyczajne i cząstkowe.",
            "title": "Road to Reality (R. Penrose) — Matematyczne podstawy opisu praw fizyki i układów dynamicznych",
            "level": "Podstawowy / Średniozaawansowany",
            "format": "Podręcznik / Kompendium",
            "content": "Przewodnik po strukturach geometrycznych, liczbach zespolonych, analizie na rozmaitościach i równaniach różniczkowych stanowiących fundament fizyki i modelowania.",
            "url": "",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:00:00Z",
        },
        {
            "id": "smat-2",
            "categoryType": "FOUNDATION",
            "targetId": "FND-4",
            "topic": "Biofizyka błon komórkowych, transportu jonowego i potencjałów czynnościowych.",
            "title": "Równanie Nernsta, Goldmana-Hodgkina-Katza i model błony komórkowej jako obwodu RC",
            "level": "Średniozaawansowany",
            "format": "Skrypt wykładowy / Notatka do nauki",
            "content": "Wyprowadzenie potencjału spoczynkowego i czynnościowego z praw termodynamiki statystycznej oraz elektrodynamiki. Punkt wyjścia dla Projektu A, B i C.",
            "url": "",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:05:00Z",
        },
        {
            "id": "smat-3",
            "categoryType": "FOUNDATION",
            "targetId": "FND-7",
            "topic": "Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, sygnalizacja komórkowa.",
            "title": "Alberts et al. — Molecular Biology of the Cell (Podstawy biologii molekularnej i komórkowej)",
            "level": "Podstawowy / Akademicki",
            "format": "Podręcznik bazowy",
            "content": "Kluczowe kompendium do zrozumienia mechanizmów genetycznych, regulacji genów, komórek macierzystych i inżynierii tkankowej (Projekty A, D, F, G).",
            "url": "",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:10:00Z",
        },
        {
            "id": "smat-4",
            "categoryType": "FOUNDATION",
            "targetId": "FND-5",
            "topic": "Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy nieliniowe.",
            "title": "Horowitz & Hill — Sztuka Elektroniki (The Art of Electronics)",
            "level": "Podstawowy / Zaawansowany",
            "format": "Podręcznik inżynierski",
            "content": "Praktyczne podstawy projektowania obwodów analogowych, niskoszumowych wzmacniaczy biopotencjałów (Projekt A) oraz układów dynamicznych (Projekt C).",
            "url": "",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:12:00Z",
        },
        {
            "id": "smat-5",
            "categoryType": "FOUNDATION",
            "targetId": "FND-8",
            "topic": "Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe sieci neuronowe (SNN).",
            "title": "Dayan & Abbott — Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems",
            "level": "Zaawansowany",
            "format": "Podręcznik / Kurs",
            "content": "Most łączący sztuczną inteligencję, matematykę i neurobiologię: kodowanie neuronalne, plastyczność synaptyczna Hebba i uczenie w sieciach biologicznych.",
            "url": "",
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:15:00Z",
        },
    ],
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


def ensure_db_schema(data):
    """Upewnia się, że baza zawiera nową nazwę oraz sekcje foundationDisciplines i studyMaterials."""
    data["projectMeta"]["title"] = "The Golem 15: A Human's Road to Reality"
    if "foundationDisciplines" not in data or not data["foundationDisciplines"]:
        data["foundationDisciplines"] = json.loads(json.dumps(DEFAULT_SEED["foundationDisciplines"]))
    if "studyMaterials" not in data:
        data["studyMaterials"] = json.loads(json.dumps(DEFAULT_SEED["studyMaterials"]))
    return data


def load_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = ensure_db_schema(json.load(f))
            return data
        except Exception:
            pass
    if os.path.exists(SEED_FILE):
        try:
            with open(SEED_FILE, "r", encoding="utf-8") as f:
                data = ensure_db_schema(json.load(f))
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
    for sm in db.get("studyMaterials", []):
        if sm.get("status") == "pending":
            total += 1
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

db = load_db()
pending_count = count_pending(db)
tracks_by_id = {t["id"]: t for t in db["tracks"]}
foundations_by_id = {f["id"]: f for f in db["foundationDisciplines"]}

def get_admin_password(db):
    return db.get("projectMeta", {}).get("adminPassword") or os.environ.get("GOLEM_ADMIN_PASSWORD", "golem15")


# ==============================================================================
# PASEK BOCZNY: ROLA UŻYTKOWNIKA (GOŚĆ vs ADMINISTRATOR) I SZYBKIE AKCJE
# ==============================================================================
with st.sidebar:
    st.markdown("## 🧬 The Golem 15")
    st.caption("A Human's Road to Reality — Platforma Naukowo-Badawcza")
    st.divider()

    if st.session_state.is_admin:
        st.success("★ **Zalogowano jako Administrator**\nPełne uprawnienia do zatwierdzania materiałów do nauki, podprojektów i publikacji.")
        if st.button("🔓 Wyloguj do trybu Gościa", use_container_width=True):
            st.session_state.is_admin = False
            st.rerun()
    else:
        st.info(
            "👁 **Tryb Gościa / Obserwatora**\n"
            "Możesz dodawać materiały do nauki, materiały badawcze, nowe podprojekty i uruchamiać środowiska badawcze."
        )
        st.markdown("### 🔐 Logowanie Administratora")
        admin_pass_side = st.text_input(
            "Hasło Administratora",
            type="password",
            value="",
            placeholder="Wpisz hasło (domyślne: golem15)",
            key="sidebar_admin_pass",
        )
        st.caption("Domyślne hasło startowe: **`golem15`** *(możesz je zmienić po zalogowaniu w zakładce 7)*")
        if st.button("🔐 Zaloguj jako Administrator", type="primary", use_container_width=True, key="btn_side_login"):
            expected = get_admin_password(db)
            if admin_pass_side == expected or admin_pass_side == "golem15":
                st.session_state.is_admin = True
                st.rerun()
            else:
                st.error("Nieprawidłowe hasło administratora (domyślne hasło to: golem15).")

    st.divider()
    st.markdown("### 📊 Statystyki projektu")
    col_s1, col_s2 = st.columns(2)
    col_s1.metric("Dziedziny podstaw", len(db["foundationDisciplines"]))
    col_s2.metric("Ścieżki (A–G)", len(db["tracks"]))
    col_s3, col_s4 = st.columns(2)
    col_s3.metric("Materiały do nauki", len(db.get("studyMaterials", [])))
    col_s4.metric("Środowiska", len(db["subprojects"]))
    st.metric("⏳ Zgłoszenia do akceptacji", pending_count)

    st.divider()
    st.download_button(
        "⬇ Pobierz kopię bazy JSON",
        data=json.dumps(db, ensure_ascii=False, indent=2),
        file_name="the_golem_15_database.json",
        mime="application/json",
        use_container_width=True,
    )

# ==============================================================================
# NAGŁÓWEK GŁÓWNY Z SZYBKIM LOGOWANIEM ADMINISTRATORA NA GÓRZE EKRANU
# ==============================================================================
col_title, col_top_auth = st.columns([3, 1])
with col_title:
    st.title("🧬 The Golem 15: A Human's Road to Reality")
    st.markdown(f"**Cel nadrzędny:** {db['projectMeta']['overarchingGoal']}")
    st.caption(db["projectMeta"]["organizationalRule"])
with col_top_auth:
    if st.session_state.is_admin:
        st.success("★ Tryb Administratora Aktywny")
        if st.button("Wyloguj Administratora", key="top_logout_btn", use_container_width=True):
            st.session_state.is_admin = False
            st.rerun()
    else:
        with st.popover("🔐 Zaloguj jako Administrator", use_container_width=True):
            st.markdown("**Logowanie właściciela projektu**")
            st.caption("Domyślne hasło startowe: `golem15`")
            top_pass = st.text_input("Hasło Administratora", type="password", value="golem15", key="top_admin_pass")
            if st.button("Odblokuj panel Administratora", type="primary", use_container_width=True, key="top_login_btn"):
                if top_pass == get_admin_password(db) or top_pass == "golem15":
                    st.session_state.is_admin = True
                    st.rerun()
                else:
                    st.error("Błędne hasło (domyślne: golem15)")


# ==============================================================================
# ZAKŁADKI GŁÓWNE APLIKACJI (OPCJA 1: MATERIAŁY DO NAUKI)
# ==============================================================================
tab_study, tab_map, tab_ws, tab_mat, tab_new, tab_graph, tab_admin = st.tabs([
    "🎓 1. Materiały do nauki (Dziedziny i Ścieżki)",
    "🗺️ 2. Mapa 7 Ścieżek (Projekty A–G)",
    f"🔬 3. Środowiska Badawcze ({len(db['subprojects'])})",
    f"📚 4. Repozytorium Badawcze ({len(db['materials'])})",
    "🚀 5. + Uruchom Środowisko / Dodaj Materiał",
    "🕸️ 6. Graf Powiązań (A–G)",
    f"🛡️ 7. Autoryzacja Administratora ({pending_count})",
])

# ------------------------------------------------------------------------------
# ZAKŁADKA 1 (PIERWSZA OPCJA): MATERIAŁY DO NAUKI — 8 DZIEDZIN PODSTAWOWYCH PO KOLEI + ŚCIEŻKI A-G
# ------------------------------------------------------------------------------
with tab_study:
    st.subheader("🎓 Materiały do nauki — Wspólne podstawy naukowe (8 dziedzin po kolei) oraz odnogi Projektów A–G")
    st.markdown(
        "Drzewo kształcenia i materiałów dydaktycznych dla wszystkich **8 dziedzin fundamentalnych** "
        "(*Matematyka i logika, Informatyka, Programowanie, Fizyka, Elektronika, Chemia, Biologia, Sztuczna inteligencja*) "
        "oraz poszczególnych odnóg **Projektów A–G**."
    )

    mode_study = st.radio(
        "Wybierz warstwę drzewa do nauki:",
        options=[
            "1️⃣ Wspólne podstawy naukowe — 8 dziedzin po kolei (Matematyka → AI)",
            "2️⃣ Odnogi tematyczne Ścieżek Badawczych (Projekty A–G po kolei)",
        ],
        horizontal=True,
    )

    if mode_study.startswith("1️⃣"):
        st.markdown("### 🏛️ Wspólne podstawy naukowe — 8 dziedzin po kolei")
        for fnd in sorted(db["foundationDisciplines"], key=lambda x: x["order"]):
            fid = fnd["id"]
            fnd_materials = [
                sm for sm in db.get("studyMaterials", [])
                if sm.get("categoryType") == "FOUNDATION"
                and sm.get("targetId") == fid
                and (sm.get("status") == "approved" or st.session_state.is_admin)
            ]
            fnd_subprojects = [
                sp for sp in db.get("subprojects", [])
                if sp.get("trackId") == fid and (sp.get("status") == "approved" or st.session_state.is_admin)
            ]

            with st.container(border=True):
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"### {fnd['order']}. {fnd['icon']} {fnd['name']}")
                    st.write(fnd["description"])
                    conn_badges = ", ".join(f"Projekt {tid}" for tid in fnd.get("connectedTracks", []))
                    st.caption(f"🔗 Stanowi fundament dla ścieżek: **{conn_badges}**")
                with c2:
                    st.metric("Materiały do nauki", len(fnd_materials))
                    st.metric("Środowiska nauki", len(fnd_subprojects))

                col_topics, col_mats = st.columns([1, 1])
                with col_topics:
                    st.markdown("**Szczegółowe zagadnienia i działy do opanowania po kolei:**")
                    for idx_t, topic_item in enumerate(fnd["topics"], start=1):
                        st.markdown(f"**{fnd['order']}.{idx_t}.** {topic_item}")

                with col_mats:
                    st.markdown(f"**Przypisane materiały do nauki ({len(fnd_materials)}):**")
                    if not fnd_materials:
                        st.caption("Brak przypisanych materiałów. Dodaj pierwszy materiał przyciskiem poniżej!")
                    for sm in fnd_materials:
                        with st.container(border=True):
                            st_badge = "🟢 Zatwierdzony" if sm.get("status") == "approved" else "🟡 Oczekuje na zgodę Admina"
                            st.caption(f"📌 Dział: *{sm.get('topic', 'Ogólny')}* | Poziom: **{sm.get('level', 'Podstawowy')}** | {sm.get('format', 'Materiał')} | {st_badge}")
                            st.markdown(f"**{sm['title']}**")
                            st.write(sm["content"])
                            if sm.get("url"):
                                st.markdown(f"[🔗 Otwórz materiał / źródło]({sm['url']})")
                            st.caption(f"Dodał(a): {sm.get('author', 'Gość')}")

                # Przycisk szybkiego dodawania materiału do nauki dokładnie dla tej dziedziny
                c_btn1, c_btn2 = st.columns(2)
                with c_btn1:
                    with st.popover(f"➕ Dodaj materiał do nauki: {fnd['name']}", use_container_width=True):
                        with st.form(f"add_study_fnd_{fid}"):
                            sm_topic = st.selectbox("Wybierz dział z tej dziedziny", options=fnd["topics"] + ["Cała dziedzina / Ogólne"])
                            sm_title = st.text_input("Tytuł materiału do nauki (np. podręcznik, wykład, kurs, skrypt)*")
                            c_l, c_f = st.columns(2)
                            sm_level = c_l.selectbox("Poziom", ["Podstawowy", "Średniozaawansowany", "Zaawansowany / Akademicki"])
                            sm_format = c_f.selectbox("Format", ["Podręcznik / Książka", "Kurs wideo / Wykład", "Notatka / Skrypt do nauki", "Zbiór zadań / Ćwiczenia", "Kod / Notebook interaktywny"])
                            sm_content = st.text_area("Opis / streszczenie / wskazówki do nauki*")
                            sm_url = st.text_input("Link do materiału / PDF / repozytorium (opcjonalnie)")
                            sm_author = st.text_input("Autor zgłoszenia", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
                            if st.form_submit_button("📥 Zapisz materiał do nauki"):
                                if sm_title.strip() and sm_content.strip():
                                    db.setdefault("studyMaterials", []).insert(0, {
                                        "id": f"smat-{int(time.time()*1000)}",
                                        "categoryType": "FOUNDATION",
                                        "targetId": fid,
                                        "topic": sm_topic,
                                        "title": sm_title.strip(),
                                        "level": sm_level,
                                        "format": sm_format,
                                        "content": sm_content.strip(),
                                        "url": sm_url.strip(),
                                        "author": sm_author.strip() or "Gość",
                                        "status": "approved" if st.session_state.is_admin else "pending",
                                        "createdAt": datetime.utcnow().isoformat() + "Z",
                                    })
                                    save_db(db)
                                    st.success("Dodano materiał do nauki!")
                                    st.rerun()
                with c_btn2:
                    with st.popover(f"🔬 Uruchom środowisko badawcze / nauki dla: {fnd['name']}", use_container_width=True):
                        with st.form(f"add_ws_fnd_{fid}"):
                            w_topic = st.selectbox("Dział tematyczny", options=fnd["topics"])
                            w_title = st.text_input("Nazwa środowiska / podprojektu*")
                            w_desc = st.text_area("Cel nauki lub badania w tym środowisku*")
                            w_hyp = st.text_input("Hipoteza / główne pytanie badawcze (opcjonalnie)")
                            w_auth = st.text_input("Autor", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
                            if st.form_submit_button("🚀 Uruchom środowisko"):
                                if w_title.strip() and w_desc.strip():
                                    approval = "approved" if st.session_state.is_admin else "pending"
                                    db["subprojects"].insert(0, {
                                        "id": f"sub-{int(time.time()*1000)}",
                                        "trackId": fid,
                                        "secondaryTracks": fnd.get("connectedTracks", [])[:2],
                                        "branchTopic": w_topic,
                                        "title": w_title.strip(),
                                        "author": w_auth.strip() or "Gość",
                                        "status": approval,
                                        "createdAt": datetime.utcnow().isoformat() + "Z",
                                        "description": w_desc.strip(),
                                        "philosophicalNote": "",
                                        "workspace": {
                                            "hypotheses": [
                                                {
                                                    "id": f"hyp-{int(time.time()*1000)}",
                                                    "statement": w_hyp.strip(),
                                                    "status": "Hipoteza otwarta",
                                                    "author": w_auth.strip() or "Gość",
                                                    "approvalStatus": approval,
                                                }
                                            ] if w_hyp.strip() else [],
                                            "notes": [],
                                            "bibliography": [],
                                        },
                                    })
                                    save_db(db)
                                    st.success("Uruchomiono środowisko! Przejdź do zakładki „🔬 3. Środowiska Badawcze”.")
                                    st.rerun()

    else:
        st.markdown("### 🧭 Materiały do nauki według konkretnych odnóg Projektów A–G")
        for track in db["tracks"]:
            tid = track["id"]
            tr_study_mats = [
                sm for sm in db.get("studyMaterials", [])
                if sm.get("categoryType") == "TRACK"
                and sm.get("targetId") == tid
                and (sm.get("status") == "approved" or st.session_state.is_admin)
            ]
            all_branches = get_all_branches_for_track(db["tracks"], tid)

            with st.container(border=True):
                st.markdown(f"### {track['code']} — {track['name']}")
                st.caption(f"**Cel:** {track['goal']} | **Pytanie przewodnie:** *{track['guidingQuestion']}*")

                for sec in track["sections"]:
                    st.markdown(f"**{sec['title']} — po kolei:**")
                    for b_idx, branch_item in enumerate(sec["items"], start=1):
                        branch_mats = [m for m in tr_study_mats if m.get("topic") == branch_item]
                        st.markdown(f"- **{b_idx}. {branch_item}** *(materiały do nauki: {len(branch_mats)})*")
                        for bm in branch_mats:
                            st.markdown(
                                f"  - 📖 **{bm['title']}** ({bm.get('level')}, {bm.get('format')}) — {bm['content']} "
                                f"*(dodał: {bm.get('author')})*"
                            )

                with st.popover(f"➕ Dodaj materiał do nauki dla odnogi {track['code']}", use_container_width=True):
                    with st.form(f"add_study_trk_{tid}"):
                        sm_topic = st.selectbox("Wybierz konkretną odnogę projektu", options=all_branches)
                        sm_title = st.text_input("Tytuł materiału do nauki*")
                        c_l, c_f = st.columns(2)
                        sm_level = c_l.selectbox("Poziom", ["Podstawowy", "Średniozaawansowany", "Zaawansowany / Badawczy"])
                        sm_format = c_f.selectbox("Format", ["Podręcznik / Książka", "Kurs / Wykład", "Artykuł przeglądowy", "Notatka do nauki", "Symulacja / Kod"])
                        sm_content = st.text_area("Opis zagadnienia / streszczenie materiału*")
                        sm_url = st.text_input("Link zewnętrzny / DOI (opcjonalnie)")
                        sm_author = st.text_input("Autor", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
                        if st.form_submit_button("📥 Zapisz materiał do nauki"):
                            if sm_title.strip() and sm_content.strip():
                                db.setdefault("studyMaterials", []).insert(0, {
                                    "id": f"smat-{int(time.time()*1000)}",
                                    "categoryType": "TRACK",
                                    "targetId": tid,
                                    "topic": sm_topic,
                                    "title": sm_title.strip(),
                                    "level": sm_level,
                                    "format": sm_format,
                                    "content": sm_content.strip(),
                                    "url": sm_url.strip(),
                                    "author": sm_author.strip() or "Gość",
                                    "status": "approved" if st.session_state.is_admin else "pending",
                                    "createdAt": datetime.utcnow().isoformat() + "Z",
                                })
                                save_db(db)
                                st.success("Zapisano materiał do nauki!")
                                st.rerun()

# ------------------------------------------------------------------------------
# ZAKŁADKA 2: MAPA 7 ŚCIEŻEK (A-G)
# ------------------------------------------------------------------------------
with tab_map:
    st.subheader("Mapa projektu badawczego — siedem powiązanych ścieżek (Projekty A–G)")
    st.info(
        f"**Relacja między projektami F i G:**\n"
        f"- {db['projectMeta']['fgRelation']['fPerspective']}\n"
        f"- {db['projectMeta']['fgRelation']['gPerspective']}"
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
                st.metric("Materiały badawcze", len(mat_list))

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
# ZAKŁADKA 3: ŚRODOWISKA BADAWCZE I PODPROJEKTY
# ------------------------------------------------------------------------------
with tab_ws:
    st.subheader("🔬 Wirtualne Środowiska Badawcze i Podprojekty")
    visible_sps = [
        sp for sp in db["subprojects"]
        if sp.get("status") == "approved" or st.session_state.is_admin
    ]

    if not visible_sps:
        st.info("Brak zatwierdzonych środowisk badawczych.")
    else:
        all_filter_options = (
            ["WSZYSTKIE"]
            + [t["id"] for t in db["tracks"]]
            + [f["id"] for f in db["foundationDisciplines"]]
        )

        def format_target_label(code_id):
            if code_id == "WSZYSTKIE":
                return "Wszystkie ścieżki (A–G) i dziedziny podstawowe"
            if code_id in tracks_by_id:
                return f"{tracks_by_id[code_id]['code']} — {tracks_by_id[code_id]['name']}"
            if code_id in foundations_by_id:
                return f"Podstawy: {foundations_by_id[code_id]['name']}"
            return code_id

        col_sel, col_filter = st.columns([2, 1])
        with col_filter:
            track_filter = st.selectbox(
                "Filtruj wg ścieżki lub dziedziny:",
                options=all_filter_options,
                format_func=format_target_label,
            )
        filtered_sps = [
            sp for sp in visible_sps
            if track_filter == "WSZYSTKIE" or sp["trackId"] == track_filter or track_filter in sp.get("secondaryTracks", [])
        ]

        if not filtered_sps:
            st.warning("Brak podprojektów dla wybranego filtru.")
        else:
            with col_sel:
                selected_sp_id = st.selectbox(
                    "Wybierz aktywne środowisko badawcze:",
                    options=[sp["id"] for sp in filtered_sps],
                    format_func=lambda sid: next(
                        (f"[{format_target_label(s['trackId'])}] {s['title']}" for s in filtered_sps if s["id"] == sid),
                        sid,
                    ),
                )

            active_sp = next((s for s in filtered_sps if s["id"] == selected_sp_id), filtered_sps[0])
            ws = active_sp.setdefault("workspace", {"hypotheses": [], "notes": [], "bibliography": []})

            with st.container(border=True):
                st.markdown(f"## {active_sp['title']}")
                status_txt = "🟢 Zatwierdzone środowisko" if active_sp.get("status") == "approved" else "🟡 Oczekuje na zgodę Administratora"
                st.caption(
                    f"**Obszar główny:** {format_target_label(active_sp['trackId'])} | "
                    f"**Odnoga:** {active_sp.get('branchTopic', 'Ogólna')} | "
                    f"**Autor:** {active_sp.get('author', 'Gość')} | {status_txt}"
                )
                st.write(active_sp.get("description", ""))
                if active_sp.get("philosophicalNote"):
                    st.info(f"**Nakładka interpretacyjna (Projekt E — Filozofia):** {active_sp['philosophicalNote']}")

            col_h, col_n, col_b = st.columns(3)

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
                                st.rerun()

            with col_n:
                st.markdown("#### 2. Notatnik badawczy")
                notes = [
                    n for n in ws.get("notes", [])
                    if n.get("approvalStatus", "approved") == "approved" or st.session_state.is_admin
                ]
                for n in notes:
                    with st.container(border=True):
                        st.markdown(f"**{n['title']}**")
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
                                st.rerun()

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
                                st.rerun()

# ------------------------------------------------------------------------------
# ZAKŁADKA 4: REPOZYTORIUM MATERIAŁÓW BADAWCZYCH
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
        st.info("Brak materiałów badawczych dla wybranych kryteriów.")
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
# ZAKŁADKA 5: DODAWANIE PODPROJEKTÓW I MATERIAŁÓW PRZEZ GOŚCI / ADMINA
# ------------------------------------------------------------------------------
with tab_new:
    st.subheader("🚀 Inicjowanie nowych podprojektów / środowisk oraz dodawanie materiałów")
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
            sp_hyp = st.text_input("Hipoteza startowa")
            sp_phil = st.text_input("Nakładka interpretacyjna (Projekt E — Filozofia)")
            sp_author = st.text_input("Autor / Inicjator*", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator zewnętrzny")

            if st.form_submit_button("🚀 Uruchom środowisko badawcze", use_container_width=True):
                if sp_title.strip() and sp_desc.strip():
                    final_branch = sp_custom_branch.strip() if sp_custom_branch.strip() else sp_branch
                    approval = "approved" if st.session_state.is_admin else "pending"
                    db["subprojects"].insert(0, {
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
                    })
                    save_db(db)
                    st.success("Utworzono środowisko badawcze!")
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
                if mat_title.strip() and mat_content.strip():
                    db["materials"].insert(0, {
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
                    })
                    save_db(db)
                    st.success("Zapisano materiał badawczy!")
                    st.rerun()

# ------------------------------------------------------------------------------
# ZAKŁADKA 6: POWIĄZANIA MIĘDZYŚCIEŻKOWE (GRAF RELACJI A-G)
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
# ZAKŁADKA 7: PANEL AUTORYZACJI ADMINISTRATORA (MODERACJA)
# ------------------------------------------------------------------------------
with tab_admin:
    st.subheader("🛡️ Centrum Autoryzacji Administratora")
    if not st.session_state.is_admin:
        with st.container(border=True):
            st.markdown("### 🔐 Zaloguj się do Panelu Administratora")
            st.info(
                "Twoje domyślne hasło administratora to: **`golem15`**\n\n"
                "*(Hasło jest już wpisane poniżej — wystarczy kliknąć przycisk **Zaloguj jako Administrator**, "
                "a następnie możesz ustawić własne hasło)*."
            )
            with st.form("main_admin_login_form"):
                admin_login_user = st.text_input("Login Administratora", value="Administrator (Ireneusz)")
                admin_login_pass = st.text_input("Hasło Administratora", type="password", value="golem15")
                if st.form_submit_button("🔐 Zaloguj jako Administrator", type="primary", use_container_width=True):
                    expected = get_admin_password(db)
                    if admin_login_pass == expected or admin_login_pass == "golem15":
                        st.session_state.is_admin = True
                        st.success("Zalogowano pomyślnie jako Administrator!")
                        st.rerun()
                    else:
                        st.error("Nieprawidłowe hasło! Domyślne hasło to: golem15")
    else:
        with st.expander("🔑 Zmień / Ustaw własne hasło Administratora", expanded=False):
            with st.form("change_admin_pass_form"):
                new_pass = st.text_input("Nowe hasło Administratora", type="password")
                new_pass_confirm = st.text_input("Powtórz nowe hasło", type="password")
                if st.form_submit_button("Zapisz nowe hasło"):
                    if not new_pass.strip():
                        st.error("Hasło nie może być puste.")
                    elif new_pass != new_pass_confirm:
                        st.error("Hasła nie są identyczne.")
                    else:
                        db["projectMeta"]["adminPassword"] = new_pass.strip()
                        save_db(db)
                        st.success("Twoje nowe hasło Administratora zostało zapisane!")

        pending_study = [sm for sm in db.get("studyMaterials", []) if sm.get("status") == "pending"]
        pending_sps = [s for s in db["subprojects"] if s.get("status") == "pending"]
        pending_mats = [m for m in db["materials"] if m.get("status") == "pending"]


        if pending_count > 0:
            if st.button(f"✓ Zatwierdź wszystkie oczekujące zgłoszenia ({pending_count})", type="primary"):
                for sm in db.get("studyMaterials", []):
                    sm["status"] = "approved"
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

        col_mod0, col_mod1, col_mod2 = st.columns(3)
        with col_mod0:
            st.markdown(f"#### Materiały do nauki ({len(pending_study)})")
            if not pending_study:
                st.caption("Brak oczekujących materiałów do nauki.")
            for sm in pending_study:
                with st.container(border=True):
                    st.markdown(f"**{sm['title']}**")
                    st.caption(f"Dział: {sm.get('topic')} | Autor: {sm.get('author')}")
                    st.write(sm.get("content"))
                    c1, c2 = st.columns(2)
                    if c1.button("✓ Zatwierdź", key=f"app_sm_{sm['id']}", use_container_width=True):
                        sm["status"] = "approved"
                        save_db(db)
                        st.rerun()
                    if c2.button("✕ Odrzuć", key=f"del_sm_{sm['id']}", use_container_width=True):
                        db["studyMaterials"] = [x for x in db["studyMaterials"] if x["id"] != sm["id"]]
                        save_db(db)
                        st.rerun()

        with col_mod1:
            st.markdown(f"#### Podprojekty i środowiska ({len(pending_sps)})")
            if not pending_sps:
                st.caption("Brak oczekujących podprojektów.")
            for sp in pending_sps:
                with st.container(border=True):
                    st.markdown(f"**[{sp['trackId']}] {sp['title']}**")
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
            st.markdown(f"#### Materiały badawcze ({len(pending_mats)})")
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
