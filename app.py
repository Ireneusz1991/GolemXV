import hashlib
import hmac
import json
import os
import secrets
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
        "adminAuth": {
            "algorithm": "pbkdf2_sha256",
            "iterations": 260000,
            "salt": "9f4d8a2c6e1b3f7a5c8d0e2f4a6b8c1d",
            "hash": "673a07dbc15ac855752d7c521ffc31e200302b03a3b296310b742421cbfd4d62",
        },
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
            "topic": "Algebra liniowa, przestrzenie wektorowe, rachunek macierzowy i teoria operatorów.",
            "title": "I. Matematyka (PL → EN): Podręczniki matematyki i algebry liniowej (OpenAGH, ZPE, Skoczylas, Penrose) oraz Gilbert Strang",
            "level": "Podstawowy / Akademicki (Etap 1: Najpierw)",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów — "
                "darmowe e-podręczniki OpenAGH (Matematyka, Algebra liniowa, Analiza matematyczna), Zintegrowana Platforma Edukacyjna (ZPE), "
                "Marian Gewert i Zbigniew Skoczylas („Algebra liniowa 1–2”, „Analiza matematyczna 1–2”), Tadeusz Krasiński („Algebra liniowa”) "
                "oraz Roger Penrose („Droga do rzeczywistości”, wyd. polskie).\n"
                "2. Uzupełniająco (Po angielsku): Gilbert Strang — „Introduction to Linear Algebra” (MIT 18.06) oraz OpenStax Mathematics."
            ),
            "url": "https://open.agh.edu.pl/",
            "links": [
                {"label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki akademickie (Matematyka, Algebra liniowa, Analiza)", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Matematyka i logika po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 OpenStax Polska — Darmowe podręczniki akademickie po polsku", "url": "https://openstax.pl/pl/zasoby"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Podręczniki algebry liniowej i analizy matematycznej", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT 18.06 + wykłady)", "url": "https://math.mit.edu/~gs/linearalgebra/"},
                {"label": "🇬🇧 OpenStax Mathematics (Calculus / Linear Algebra)", "url": "https://openstax.org/subjects/math"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:00:00Z",
        },
        {
            "id": "smat-1b",
            "categoryType": "FOUNDATION",
            "targetId": "FND-2",
            "topic": "Architektura systemów komputerowych, systemy wbudowane, praca w czasie rzeczywistym (RTOS) i obliczenia rozproszone.",
            "title": "I. Informatyka (PL → EN): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II”, Cormen („Wprowadzenie do algorytmów”), Ważniak MIMUW",
            "level": "Podstawowy (Etap 1: Najpierw)",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Helion) — fundamentalna książka "
                "wyjaśniająca od podstaw, jak z przekaźników, bramek logicznych i tranzystorów powstaje komputer; "
                "Thomas H. Cormen i współautorzy — „Wprowadzenie do algorytmów” (PWN); Andrew S. Tanenbaum — „Strukturalna organizacja komputerów” (Helion); "
                "darmowe kursy akademickie Ważniak MIMUW (Uniwersytet Warszawski) oraz ZPE Informatyka.\n"
                "2. Uzupełniająco (Po angielsku): Charles Petzold — „Code” oraz MIT OCW 6.006."
            ),
            "url": "https://wazniak.mimuw.edu.pl/",
            "links": [
                {"label": "🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Wydawnictwo Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 Ważniak MIMUW (Uniwersytet Warszawski) — Darmowe polskie wykłady z informatyki i architektury komputerów", "url": "https://wazniak.mimuw.edu.pl/"},
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Informatyka i algorytmika po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 T. H. Cormen et al. — „Wprowadzenie do algorytmów” (Księgarnia PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Charles Petzold — „Code” (Strona autora z interaktywnymi symulacjami bramek)", "url": "https://codehiddenlanguage.com/"},
                {"label": "🇬🇧 MIT OCW 6.006 — Introduction to Algorithms", "url": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:02:00Z",
        },
        {
            "id": "smat-1c",
            "categoryType": "FOUNDATION",
            "targetId": "FND-3",
            "topic": "Obliczenia naukowe w Pythonie (NumPy, SciPy, PyTorch, JAX) oraz symulacje numeryczne.",
            "title": "I. Programowanie (PL → EN): Eric Matthes — „Python. Instrukcje dla programisty”, oficjalna polska dokumentacja Pythona i obliczenia naukowe",
            "level": "Podstawowy (Etap 1: Najpierw)",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Eric Matthes — „Python. Instrukcje dla programisty. Wydanie III” (Helion) — praktyczny podręcznik "
                "programowania od podstaw z ćwiczeniami; oficjalny polski przewodnik po języku Python (docs.python.org/pl); "
                "Wes McKinney — „Python w analizie danych (NumPy, pandas)” (Helion); kursy programowania Ważniak MIMUW i ZPE.\n"
                "2. Uzupełniająco (Po angielsku): Eric Matthes — „Python Crash Course”, Scientific Python Lectures oraz symulator sieci neuronowych Brian2."
            ),
            "url": "https://docs.python.org/pl/3/tutorial/",
            "links": [
                {"label": "🇵🇱 Oficjalny samouczek języka Python po polsku (docs.python.org/pl)", "url": "https://docs.python.org/pl/3/tutorial/"},
                {"label": "🇵🇱 Eric Matthes — „Python. Instrukcje dla programisty” (Wydawnictwo Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 Ważniak MIMUW — Wstęp do programowania (kurs akademicki po polsku)", "url": "https://wazniak.mimuw.edu.pl/"},
                {"label": "🇵🇱 ZPE — Programowanie i algorytmy w języku Python (po polsku)", "url": "https://zpe.gov.pl/"},
                {"label": "🇬🇧 Eric Matthes — „Python Crash Course” (Repozytorium ćwiczeń i kodu)", "url": "https://ehmatthes.github.io/pcc_3e/"},
                {"label": "🇬🇧 Scientific Python Lectures (NumPy, SciPy, Matplotlib)", "url": "https://lectures.scientific-python.org/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:03:00Z",
        },
        {
            "id": "smat-2",
            "categoryType": "FOUNDATION",
            "targetId": "FND-4",
            "topic": "Mechanika klasyczna, elektrodynamika i termodynamika układów otwartych (dalekich od równowagi).",
            "title": "II. Fizyka i Komputery Kwantowe (PL → EN): OpenStax „Fizyka dla szkół wyższych Tom 1–3” (PL), Halliday & Resnick, Griffiths („Wstęp do mechaniki kwantowej”) oraz Nielsen & Chuang",
            "level": "Podstawowy → Zaawansowany",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Darmowy, trzytomowy podręcznik akademicki OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3”; "
                "David Halliday, Robert Resnick, Jearl Walker — „Podstawy fizyki. Tom 1–5” (PWN); Richard P. Feynman — „Feynmana wykłady z fizyki” (PWN); "
                "David J. Griffiths — „Wstęp do mechaniki kwantowej” (polskie wydanie PWN) oraz e-podręczniki fizyki OpenAGH.\n"
                "2. Uzupełniająco (Po angielsku — etap zaawansowany): David J. Griffiths — „Introduction to Quantum Mechanics” oraz "
                "Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”."
            ),
            "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1",
            "links": [
                {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (darmowy podręcznik PL online/PDF)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 2” (Elektrodynamika, termodynamika — PL)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2"},
                {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 3” (Optyka i fizyka kwantowa — PL)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3"},
                {"label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki z fizyki ogólnej", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Halliday/Resnick „Podstawy fizyki” oraz Griffiths „Wstęp do mechaniki kwantowej”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 David J. Griffiths — „Introduction to Quantum Mechanics” (Cambridge University Press)", "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"},
                {"label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”", "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:05:00Z",
        },
        {
            "id": "smat-4",
            "categoryType": "FOUNDATION",
            "targetId": "FND-5",
            "topic": "Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy nieliniowe.",
            "title": "II. Elektronika (PL → EN): Horowitz & Hill („Sztuka elektroniki”), polskie kursy Forbot, ZPE, OpenAGH oraz układy cyfrowe",
            "level": "Podstawowy / Zaawansowany",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Paul Horowitz, Winfield Hill — „Sztuka elektroniki. Część 1 i 2” (polskie wydanie WKŁ); "
                "Bogdan Głocki — „Układy cyfrowe” (WSiP); darmowe polskojęzyczne kursy podstaw elektroniki i techniki cyfrowej Forbot; "
                "materiały Zintegrowanej Platformy Edukacyjnej (ZPE) oraz e-podręczniki elektroniki OpenAGH.\n"
                "2. Uzupełniająco (Po angielsku): All About Circuits Textbook oraz MIT OCW Circuits and Electronics."
            ),
            "url": "https://zpe.gov.pl/",
            "links": [
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika analogowa i układy cyfrowe po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 Forbot — Darmowe kursy podstaw elektroniki i techniki cyfrowej po polsku", "url": "https://forbot.pl/blog/kurs-elektroniki-poziom-1-spis-tresci-id5159"},
                {"label": "🇵🇱 OpenAGH — Polskie e-podręczniki akademickie z elektroniki i elektrotechniki", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Paul Horowitz, Winfield Hill — „Sztuka elektroniki” (Wydawnictwa Komunikacji i Łączności — WKŁ)", "url": "https://wkl.com.pl/"},
                {"label": "🇬🇧 All About Circuits — Textbook of Analog & Digital Electronics", "url": "https://www.allaboutcircuits.com/textbook/"},
                {"label": "🇬🇧 MIT OCW — Circuits and Electronics", "url": "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:12:00Z",
        },
        {
            "id": "smat-4b",
            "categoryType": "FOUNDATION",
            "targetId": "FND-6",
            "topic": "Biochemia: struktura i funkcja białek, enzymów, lipidów oraz kwasów nukleinowych (DNA/RNA).",
            "title": "III. Chemia i Biochemia (PL → EN): Stryer („Biochemia” PWN), Bielański, Jones & Atkins, McMurry oraz OpenStax Chemistry 2e",
            "level": "Podstawowy / Akademicki (Etap 2: Następnie)",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Akademickie podręczniki chemii ogólnej, organicznej i biochemii w polskich wydaniach — "
                "Jeremy M. Berg, John L. Tymoczko, Lubert Stryer — „Biochemia” (PWN); Robert K. Murray et al. — „Biochemia Harpera” (PZWL); "
                "Loretta Jones, Peter Atkins — „Chemia ogólna. Cząsteczki, materia, reakcje” (PWN); Adam Bielański — „Podstawy chemii nieorganicznej” (PWN); "
                "John McMurry — „Chemia organiczna” (PWN) oraz darmowe materiały ZPE i OpenAGH.\n"
                "2. Uzupełniająco (Po angielsku): OpenStax „Chemistry 2e” oraz „Organic Chemistry” (darmowe podręczniki online)."
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Stryer „Biochemia”, Jones & Atkins „Chemia ogólna”, McMurry „Chemia organiczna”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki akademickie z chemii ogólnej i fizycznej", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Chemia ogólna, organiczna i biochemia po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — „Biochemia Harpera”", "url": "https://pzwl.pl/"},
                {"label": "🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej online/PDF", "url": "https://openstax.org/details/books/chemistry-2e"},
                {"label": "🇬🇧 OpenStax Organic Chemistry — Darmowy podręcznik chemii organicznej", "url": "https://openstax.org/details/books/organic-chemistry"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:13:00Z",
        },
        {
            "id": "smat-3",
            "categoryType": "FOUNDATION",
            "targetId": "FND-7",
            "topic": "Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, sygnalizacja komórkowa.",
            "title": "III. Biologia i Genetyka (PL → EN): Terence A. Brown („Genomy” PWN), „Biologia Campbella” (Rebis), Alberts („Podstawy biologii komórki”) oraz OpenStax Biology 2e",
            "level": "Podstawowy / Akademicki (Etap 2: Następnie)",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Terence A. Brown — „Genomy” (Wydawnictwo Naukowe PWN); "
                "Neil A. Campbell i współautorzy — „Biologia Campbella” (polskie wydanie, Dom Wydawniczy REBIS); "
                "Bruce Alberts i współautorzy — „Podstawy biologii komórki. Część 1–2” (PWN); Piotr Węgleński (red.) — „Genetyka molekularna” (PWN) "
                "oraz polskojęzyczne materiały ZPE.\n"
                "2. Uzupełniająco (Po angielsku): OpenStax „Biology 2e” oraz darmowe zasoby NCBI Bookshelf."
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 Terence A. Brown — „Genomy” oraz B. Alberts — „Podstawy biologii komórki” (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)", "url": "https://www.rebis.com.pl/"},
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biologia komórki i genetyka po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii online/PDF", "url": "https://openstax.org/details/books/biology-2e"},
                {"label": "🇬🇧 Terence A. Brown — „Genomes” (Darmowy dostęp w bazie NCBI Bookshelf)", "url": "https://www.ncbi.nlm.nih.gov/books/NBK21128/"},
                {"label": "🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell (Alberts)", "url": "https://www.ncbi.nlm.nih.gov/books/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:10:00Z",
        },
        {
            "id": "smat-5",
            "categoryType": "FOUNDATION",
            "targetId": "FND-8",
            "topic": "Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe sieci neuronowe (SNN).",
            "title": "IV & V. Sztuczna Inteligencja (PL → EN): Aurélien Géron („Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” PL), Goodfellow („Deep Learning” PWN) oraz Dayan & Abbott",
            "level": "Średniozaawansowany / Zaawansowany",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku): Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i TensorFlow. Wydanie III” (Helion); "
                "Ian Goodfellow, Yoshua Bengio, Aaron Courville — „Deep Learning. Systemy uczące się” (polskie wydanie PWN); "
                "Stuart Russell, Peter Norvig — „Sztuczna inteligencja. Nowe spojrzenie” (Helion) oraz Ryszard Tadeusiewicz — „Sieci neuronowe”.\n"
                "2. Uzupełniająco (Po angielsku): Géron — „Hands-On Machine Learning” (notebooki GitHub) oraz Peter Dayan, L. F. Abbott — „Theoretical Neuroscience”."
            ),
            "url": "https://helion.pl/",
            "links": [
                {"label": "🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” (Wydawnictwo Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 Ian Goodfellow, Yoshua Bengio, Aaron Courville — „Deep Learning. Systemy uczące się” (PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 OpenStax Polska — Wprowadzenie do nauki o danych i Pythonie (po polsku)", "url": "https://openstax.pl/pl/zasoby"},
                {"label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Oficjalne notebooki GitHub)", "url": "https://github.com/ageron/handson-ml3"},
                {"label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                {"label": "🇬🇧 Neuromatch Academy — Computational Neuroscience & Deep Learning", "url": "https://compneuro.neuromatch.io/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:15:00Z",
        },
        {
            "id": "smat-a1",
            "categoryType": "TRACK",
            "targetId": "A",
            "topic": "Medycyna regeneracyjna, protezy i sztuczne narządy.",
            "title": "IV. Projekt A (PL → EN): Kalat („Biologiczne podstawy psychologii”), anatomia i fizjologia (Bochenek, Traczyk, Konturek), biofizyka, robotyka i BCI oraz OpenStax Anatomy 2e",
            "level": "Podstawowy → Zaawansowany",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku):\n"
                "• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n"
                "• Akademickie podręczniki anatomii i fizjologii człowieka: Władysław Traczyk, Andrzej Trzebski — „Fizjologia człowieka” (PZWL); "
                "Stanisław Konturek — „Fizjologia człowieka”; Adam Bochenek, Michał Reicher — „Anatomia człowieka” (PZWL).\n"
                "• Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: Feliks Jaroszyk (red.) — „Biofizyka” (PZWL); Jan Marciniak — „Biomateriały” (Politechnika Śląska); "
                "seria „Biocybernetyka i Inżynieria Biomedyczna 2000” (PAN, red. M. Nałęcz, R. Tadeusiewicz).\n"
                "• Podręczniki robotyki, elektroniki i układów sterowania (K. Tchoń i współautorzy — „Manipulatory i roboty mobilne”; A. Géron — wyd. Helion).\n"
                "2. Uzupełniająco (Po angielsku): OpenStax „Anatomy and Physiology 2e”, Géron „Hands-On ML” oraz literatura z neuroprotetyki i BCI."
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia (Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)", "url": "https://pzwl.pl/"},
                {"label": "🇵🇱 OpenAGH — Polskie materiały z inżynierii biomedycznej, biocybernetyki i automatyki", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” (Helion)", "url": "https://helion.pl/"},
                {"label": "🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik anatomii i fizjologii)", "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"},
                {"label": "🇬🇧 MIT OCW — Introduction to Robotics & Control Systems", "url": "https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:18:00Z",
        },
        {
            "id": "smat-b1",
            "categoryType": "TRACK",
            "targetId": "B",
            "topic": "Neurobiologia i neuronauka obliczeniowa.",
            "title": "V. Projekt B (PL → EN): Kalat, Longstaff („Neurobiologia”), Nęcka („Psychologia poznawcza”), Seung („Konektom”), Miłkowski & Poczobut oraz Kandel, Dayan & Abbott, Izhikevich i Sandberg & Bostrom",
            "level": "Podstawowy → Zaawansowany",
            "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku):\n"
                "• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n"
                "• Podręczniki neurobiologii i fizjologii układu nerwowego: Alan Longstaff — „Neurobiologia. Krótkie wykłady” (PWN); "
                "T. Górska, A. Grabowska, J. Zagrodzka (red.) — „Mózg a zachowanie” (PWN).\n"
                "• Podręczniki psychologii poznawczej: Edward Nęcka, Jarosław Orzechowski, Błażej Szymura — „Psychologia poznawcza” (PWN).\n"
                "• Wprowadzenia do filozofii umysłu, kognitywistyki i konektomiki: Marcin Miłkowski, Robert Poczobut (red.) — „Przewodnik po filozofii umysłu” (WAM); "
                "Sebastian Seung — „Konektom. Jak połączenia w mózgu kształtują naszą tożsamość” (wyd. polskie); wykłady prof. Włodzisława Ducha (UMK).\n"
                "2. Następnie i na zaawansowanym etapie (Po angielsku): Kandel („Principles of Neural Science”), Squire („Fundamental Neuroscience”), "
                "Dayan & Abbott („Theoretical Neuroscience”), Izhikevich („Dynamical Systems in Neuroscience”), Miller, Churchland & Sejnowski oraz Sandberg & Bostrom („Whole Brain Emulation: A Roadmap”)."
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Kalat „Biologiczne podstawy psychologii”, Longstaff „Neurobiologia”, Nęcka „Psychologia poznawcza”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 Prof. Włodzisław Duch (UMK) — Polskie wykłady z kognitywistyki, neuroinformatyki i modelowania mózgu", "url": "https://www.fizyka.umk.pl/~duch/"},
                {"label": "🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu, kognitywistyka i problem świadomości (po polsku)", "url": "https://ccpress.pl/"},
                {"label": "🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (Darmowy PDF książki)", "url": "https://www.izhikevich.org/publications/dsn.pdf"},
                {"label": "🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Pełny raport PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                {"label": "🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                {"label": "🇬🇧 Paul Miller — „An Introductory Course in Computational Neuroscience” (MIT Press)", "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"},
                {"label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain” (MIT Press)", "url": "https://mitpress.mit.edu/9780262531207/the-computational-brain/"},
                {"label": "🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” & Larry Squire — „Fundamental Neuroscience”", "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:19:00Z",
        },
        {
            "id": "smat-6",
            "categoryType": "TRACK",
            "targetId": "C",
            "topic": "Elektronika analogowa i układy dynamiczne.",
            "title": "Projekt C (PL → EN): Elektronika analogowa (Horowitz & Hill, OpenAGH, ZPE, Forbot), przetworniki ADC/DAC, sieci neuronowe (Osowski, Tadeusiewicz) i Neuromorphic Computing",
            "level": "Podstawowy / Akademicki",
            "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
            "content": (
                "Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne.\n"
                "1. W pierwszej kolejności (Po polsku): Podręczniki akademickie z elektroniki analogowej (Paul Horowitz, Winfield Hill — „Sztuka elektroniki”; "
                "e-podręczniki OpenAGH): wzmacniacze, oscylatory, filtry, sprzężenie zwrotne i układy dynamiczne; materiały o przetwornikach A/C i C/A (ZPE, Forbot); "
                "Stanisław Osowski — „Sieci neuronowe do przetwarzania informacji” (Oficyna PW) oraz Ryszard Tadeusiewicz — „Sieci neuronowe”.\n"
                "2. Uzupełniająco (Po angielsku): Analog computing, neuromorphic computing, analog neural networks i fizyczne modele neuronów."
            ),
            "url": "https://zpe.gov.pl/",
            "links": [
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz C/A", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki z elektroniki i układów dynamicznych", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Forbot — Praktyczne kursy elektroniki analogowej i pomiarów po polsku", "url": "https://forbot.pl/"},
                {"label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering", "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"},
                {"label": "🇬🇧 arXiv — Neural and Evolutionary Computing (Neuromorphic & Analog NN)", "url": "https://arxiv.org/list/cs.NE/recent"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:20:00Z",
        },
        {
            "id": "smat-7",
            "categoryType": "TRACK",
            "targetId": "D",
            "topic": "Biologia syntetyczna i edycja genomu.",
            "title": "Projekt D (PL → EN): Biologia komórki (Alberts), genetyka (Brown, Węgleński), embriologia (Bartel), inżynieria tkankowa, bioetyka (PAN) i Stanisław Lem („Summa technologiae”)",
            "level": "Podstawowy → Badawczy",
            "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
            "content": (
                "Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka.\n"
                "1. W pierwszej kolejności (Po polsku): Bruce Alberts — „Podstawy biologii komórki” (PWN); Terence A. Brown — „Genomy” (PWN); "
                "Hieronim Bartel — „Embriologia. Podręcznik dla studentów” (PZWL); literatura o komórkach macierzystych, inżynierii tkankowej i medycynie regeneracyjnej (PZWL / PWN); "
                "stanowiska Komitetu Bioetyki PAN; Stanisław Lem — „Summa technologiae” (klasyczna analiza inżynierii biologicznej a science fiction).\n"
                "2. Uzupełniająco (Po angielsku): National Academies (odpowiedzialny rozwój biologii syntetycznej), NCBI Bookshelf, ISSCR i Nature."
            ),
            "url": "https://bioetyka.pan.pl/",
            "links": [
                {"label": "🇵🇱 Komitet Bioetyki Polskiej Akademii Nauk (PAN) — Opracowania i stanowiska bioetyczne po polsku", "url": "https://bioetyka.pan.pl/"},
                {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Hieronim Bartel „Embriologia”, medycyna regeneracyjna i komórki macierzyste", "url": "https://pzwl.pl/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Biologia komórki (Alberts), Genomy (Brown), Genetyka molekularna (Węgleński)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biotechnologia, genetyka i inżynieria genetyczna po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇬🇧 National Academies — Odpowiedzialny rozwój biologii syntetycznej", "url": "https://www.nationalacademies.org/"},
                {"label": "🇬🇧 NCBI Bookshelf — Developmental Biology & Cell Biology", "url": "https://www.ncbi.nlm.nih.gov/books/"},
                {"label": "🇬🇧 ISSCR — International Society for Stem Cell Research", "url": "https://www.isscr.org/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:22:00Z",
        },
        {
            "id": "smat-8",
            "categoryType": "TRACK",
            "targetId": "E",
            "topic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "title": "Projekt E (Filozofia — PL w pierwszej kolejności): Alan Chalmers, Thomas S. Kuhn, Michał Heller, Władysław Tatarkiewicz, filozofia starożytna (Wolne Lektury) i bioetyka",
            "level": "Podstawowy / Akademicki",
            "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
            "content": (
                "1. W pierwszej kolejności (Po polsku):\n"
                "• Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n"
                "• Thomas S. Kuhn — „Struktura rewolucji naukowych”\n"
                "• Michał Heller — „Filozofia nauki. Wprowadzenie” oraz „Filozofia przyrody” (Copernicus Center Press)\n"
                "• Filozofia starożytna po polsku: Platon („Państwo”, „Timajos”), Arystoteles („Metafizyka”, „O duszy”), stoicy (Marek Aureliusz — „Rozmyślania”, Seneka, Epiktet) "
                "w serwisie Wolne Lektury oraz Władysław Tatarkiewicz — „Historia filozofii. Tom 1–3” (PWN)\n"
                "• Filozofia umysłu, techniki i bioetyka: M. Miłkowski, R. Poczobut (red.) — „Przewodnik po filozofii umysłu”; Kazimierz Szewczyk — „Bioetyka. Tom 1–2” (PWN).\n"
                "2. Uzupełniająco (Po angielsku): Stanford Encyclopedia of Philosophy (SEP) oraz Internet Encyclopedia of Philosophy (IEP)."
            ),
            "url": "https://ccpress.pl/",
            "links": [
                {"label": "🇵🇱 Copernicus Center Press — Książki ks. prof. Michała Hellera i filozofia nauki po polsku", "url": "https://ccpress.pl/"},
                {"label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Darmowe polskie wykłady z filozofii nauki, umysłu i etyki", "url": "https://www.copernicuscenter.edu.pl/"},
                {"label": "🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka)", "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Kuhn „Struktura rewolucji naukowych”, Tatarkiewicz „Historia filozofii”, Szewczyk „Bioetyka”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Stanford Encyclopedia of Philosophy (Filozofia nauki, umysłu i bioetyka)", "url": "https://plato.stanford.edu/"},
                {"label": "🇬🇧 Internet Encyclopedia of Philosophy (IEP)", "url": "https://iep.utm.edu/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:25:00Z",
        },
        {
            "id": "smat-9",
            "categoryType": "TRACK",
            "targetId": "F",
            "topic": "Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.",
            "title": "Projekt F (Człowiek w kosmosie — PL → EN): Polska Agencja Kosmiczna (POLSA), ESERO Polska (Centrum Nauki Kopernik), medycyna kosmiczna i astronautyka oraz darmowe źródła NASA i ESA",
            "level": "Podstawowy / Zaawansowany",
            "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
            "content": (
                "Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.\n"
                "1. W pierwszej kolejności (Po polsku): Materiały edukacyjne i badawcze Polskiej Agencji Kosmicznej (POLSA); "
                "polskojęzyczne scenariusze i opracowania ESERO Polska (Biuro Edukacji Kosmicznej ESA przy Centrum Nauki Kopernik) dot. życia w mikrograwitacji, "
                "ochrony radiacyjnej, mechaniki orbitalnej i budowy habitatów; polskie podręczniki fizyki (OpenStax Fizyka PL), mechaniki nieba oraz medycyny lotniczej i kosmicznej (K. Kwarecki, PZWL).\n"
                "2. Darmowe źródła międzynarodowe (NASA i ESA): NASA Fundamentals of Human Health, ESA Teach with Space, ESA Human and Robotic Exploration."
            ),
            "url": "https://esero.kopernik.org.pl/",
            "links": [
                {"label": "🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o załogowych misjach kosmicznych i habitatach", "url": "https://esero.kopernik.org.pl/"},
                {"label": "🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja, nauka, medycyna i technologie kosmiczne po polsku", "url": "https://polsa.gov.pl/"},
                {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych” (Mechanika, grawitacja, ruch orbitalny po polsku)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                {"label": "🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)", "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"},
                {"label": "🛰️ ESA — Edukacja kosmiczna (Teach with Space)", "url": "https://education.esa.int/teach-with-space/"},
                {"label": "👩‍🚀 ESA — Eksploracja załogowa i robotyczna (Human and Robotic Exploration)", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:28:00Z",
        },
        {
            "id": "smat-10",
            "categoryType": "TRACK",
            "targetId": "G",
            "topic": "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.",
            "title": "Projekt G (Człowiek na Ziemi — PL → EN): Jan Krystek („Ochrona środowiska dla inżynierów”), January Weiner („Życie i ewolucja biosfery”), Politechnika Śląska, GIOŚ i ESA Education",
            "level": "Podstawowy / Inżynierski",
            "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
            "content": (
                "Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa.\n"
                "1. W pierwszej kolejności (Po polsku):\n"
                "• Jan Krystek — „Ochrona środowiska dla inżynierów” (Wydawnictwo Naukowe PWN).\n"
                "• January Weiner — „Życie i ewolucja biosfery. Podręcznik ekologii ogólnej” (PWN) — fundamentalny polski podręcznik funkcjonowania ekosystemów.\n"
                "• Czesława Rosik-Dulewska — „Podstawy gospodarki odpadami” (PWN).\n"
                "• Bezpłatne materiały Politechniki Śląskiej i OpenAGH dot. ochrony wód, powietrza i gleby oraz raporty GIOŚ (Państwowy Monitoring Środowiska).\n"
                "2. Uzupełniająco: Europejska Agencja Środowiska (EEA — serwis w jęz. polskim) oraz ESA Education."
            ),
            "url": "https://www.polsl.pl/",
            "links": [
                {"label": "🇵🇱 Politechnika Śląska — Bezpłatne materiały dotyczące podstaw ochrony środowiska", "url": "https://www.polsl.pl/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz January Weiner „Życie i ewolucja biosfery”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ) — Państwowy Monitoring Środowiska (wody, powietrze, gleby)", "url": "https://www.gios.gov.pl/"},
                {"label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie materiały o ekologii, odnawialnych źródłach energii i ochronie środowiska", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Europejska Agencja Środowiska (EEA po polsku — klimat, bioróżnorodność, GOZ, LCA)", "url": "https://www.eea.europa.eu/pl"},
                {"label": "🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska", "url": "https://education.esa.int/teach-with-space/"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:30:00Z",
        },
    ],
    "supplementaryLibrary": {
        "title": "BIBLIOTEKA PROJEKTU GOLEM 15 — Literatura polskojęzyczna (w pierwszej kolejności) i anglojęzyczna (I–VI oraz Projekty C–G)",
        "description": "Kompletna bibliografia projektu z priorytetem dla literatury i źródeł polskojęzycznych: Wspólne podstawy (I. Matematyka i Informatyka, II. Fizyka i Komputery Kwantowe, III. Chemia, Biologia i Genetyka), IV. Projekt A, V. Projekt B, VI. Kolejność czytania oraz Biblioteka uzupełniająca do Projektów C, D, E, F i G.",
        "readingOrder": {
            "title": "VI. KOLEJNOŚĆ CZYTANIA — Plan lektur krok po kroku (w pierwszej kolejności wydania i źródła polskojęzyczne)",
            "principle": "Zasada: zaczynamy od polskojęzycznych podręczników podstawowych i bezpłatnych źródeł po polsku (OpenStax Polska, OpenAGH, ZPE, Ważniak MIMUW) — najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja. Literatura anglojęzyczna stanowi rozwinięcie specjalistyczne i badawcze. Pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi.",
            "stages": [
                {
                    "stage": "1. Najpierw (Fundamenty po polsku: obliczenia, Python, matematyka i fizyka)",
                    "items": [
                        "🇵🇱 Charles Petzold — *Kod. Ukryty język komputerów. Wydanie II* — [Wydawnictwo Helion](https://helion.pl/) (oryg. *Code*: [codehiddenlanguage.com](https://codehiddenlanguage.com/))",
                        "🇵🇱 Eric Matthes — *Python. Instrukcje dla programisty* — [Wydawnictwo Helion](https://helion.pl/) + [Polski samouczek Python](https://docs.python.org/pl/3/tutorial/)",
                        "🇵🇱 Podstawy matematyki i algebry liniowej — [OpenAGH Matematyka (PL)](https://open.agh.edu.pl/) | [ZPE Matematyka (PL)](https://zpe.gov.pl/) | [OpenStax Polska](https://openstax.pl/pl/zasoby)",
                        "🇵🇱 Podręcznik fizyki ogólnej po polsku — [OpenStax Fizyka dla szkół wyższych Tom 1–3 (darmowy PL)](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1) | Halliday & Resnick *Podstawy fizyki* ([PWN](https://ksiegarnia.pwn.pl/))",
                    ],
                },
                {
                    "stage": "2. Następnie (Genomy, chemia, biologia i psychologia biologiczna po polsku)",
                    "items": [
                        "🇵🇱 Terence A. Brown — *Genomy* (polskie wydanie) — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                        "🇵🇱 Podstawy chemii, biologii i biochemii po polsku — *Biologia Campbella* ([Rebis](https://www.rebis.com.pl/)), Stryer *Biochemia* ([PWN](https://ksiegarnia.pwn.pl/)), Alberts *Podstawy biologii komórki* ([PWN](https://ksiegarnia.pwn.pl/)), [ZPE](https://zpe.gov.pl/)",
                        "🇵🇱 James W. Kalat — *Biologiczne podstawy psychologii* (polskie wydanie) — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                    ],
                },
                {
                    "stage": "3. Później (Neurobiologia, konektomika, neuronauka obliczeniowa i WBE)",
                    "items": [
                        "🇵🇱 Alan Longstaff — *Neurobiologia. Krótkie wykłady* ([PWN](https://ksiegarnia.pwn.pl/)), E. Nęcka — *Psychologia poznawcza* ([PWN](https://ksiegarnia.pwn.pl/)) oraz 🇵🇱 Sebastian Seung — *Konektom. Jak połączenia w mózgu kształtują naszą tożsamość* (wyd. polskie)",
                        "🇬🇧 Peter Dayan, L. F. Abbott — *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems* — [MIT Press](https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/)",
                        "🇬🇧 Eugene M. Izhikevich — *Dynamical Systems in Neuroscience* — [Pełny PDF autora](https://www.izhikevich.org/publications/dsn.pdf)",
                        "🇬🇧 Anders Sandberg, Nick Bostrom — *Whole Brain Emulation: A Roadmap* — [Pełny raport PDF (FHI Oxford)](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)",
                    ],
                },
                {
                    "stage": "4. Na zaawansowanym etapie (Mechanika kwantowa, neurobiologia akademicka i obliczenia kwantowe)",
                    "items": [
                        "🇵🇱/🇬🇧 David J. Griffiths — *Wstęp do mechaniki kwantowej* ([polskie wydanie PWN](https://ksiegarnia.pwn.pl/)) / *Introduction to Quantum Mechanics* ([CUP](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E))",
                        "🇬🇧 Eric R. Kandel i współautorzy — *Principles of Neural Science* — [McGraw Hill](https://www.mheducation.com/)",
                        "🇬🇧 Larry Squire i współautorzy — *Fundamental Neuroscience* — [ScienceDirect](https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience)",
                        "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — *The Computational Brain* — [MIT Press](https://mitpress.mit.edu/9780262531207/the-computational-brain/)",
                        "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — *Quantum Computation and Quantum Information* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)",
                    ],
                },
            ],
        },
        "rules": [
            "W pierwszej kolejności korzystać z literatury oraz darmowych źródeł polskojęzycznych (OpenStax Polska, e-podręczniki OpenAGH, Zintegrowana Platforma Edukacyjna ZPE, Ważniak MIMUW, polskie wydania PWN, Helion, PZWL i Copernicus Center Press).",
            "Zasada czytania: najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja.",
            "Książki specjalistyczne i anglojęzyczne wprowadzać po opanowaniu podstaw danego obszaru po polsku.",
            "Przed zakupem sprawdzać dokładny tytuł, autora, wydanie i dostępność polskiego przekładu.",
            "W szybko rozwijających się dziedzinach korzystać również z aktualnych przeglądów naukowych i dokumentacji instytucji badawczych (PAN, POLSA, GIOŚ, NASA, ESA).",
            "Rozróżniać wiedzę potwierdzoną, aktywne badania, hipotezy i spekulacje (pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi).",
            "Traktować bibliografię jako zasób długoterminowy, a nie listę lektur do przeczytania w całości od razu.",
        ],
        "projects": [
            {
                "trackId": "FND-1",
                "title": "I. MATEMATYKA I INFORMATYKA (Wspólne podstawy — PL w pierwszej kolejności)",
                "sequenceLabel": "Etap czytania",
                "sequence": "Najpierw (po polsku): Petzold (Kod. Ukryty język komputerów) → Matthes (Python. Instrukcje dla programisty) → Polskie podręczniki matematyki i algebry liniowej (OpenAGH, ZPE, Skoczylas) → Uzupełniająco (EN): Gilbert Strang (Introduction to Linear Algebra).",
                "links": [
                    {"label": "🇵🇱 Wydawnictwo Helion — Polskie wydania: Charles Petzold „Kod” oraz Eric Matthes „Python. Instrukcje dla programisty”", "url": "https://helion.pl/"},
                    {"label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki: Matematyka i Algebra Liniowa", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇵🇱 Ważniak MIMUW (UW) — Darmowe polskie kursy akademickie z matematyki i informatyki", "url": "https://wazniak.mimuw.edu.pl/"},
                    {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Matematyka, logika i informatyka po polsku", "url": "https://zpe.gov.pl/"},
                    {"label": "🇵🇱 Oficjalna dokumentacja i samouczek Pythona po polsku", "url": "https://docs.python.org/pl/3/tutorial/"},
                    {"label": "🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT 18.06)", "url": "https://math.mit.edu/~gs/linearalgebra/"},
                    {"label": "🇬🇧 Charles Petzold — Code (Strona książki i symulacje)", "url": "https://codehiddenlanguage.com/"},
                    {"label": "🇬🇧 Eric Matthes — Python Crash Course (Zasoby i ćwiczenia)", "url": "https://ehmatthes.github.io/pcc_3e/"}
                ],
                "groups": [
                    {
                        "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
                        "items": [
                            "1. Charles Petzold — *Kod. Ukryty język komputerów. Wydanie II.* — [Wydawnictwo Helion](https://helion.pl/)",
                            "2. Eric Matthes — *Python. Instrukcje dla programisty. Wydanie III.* — [Wydawnictwo Helion](https://helion.pl/) + [Samouczek Python PL](https://docs.python.org/pl/3/tutorial/)",
                            "3. Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów: M. Gewert, Z. Skoczylas (*Algebra liniowa*, *Analiza matematyczna*), T. Krasiński (*Algebra liniowa* PWN) oraz darmowe zasoby: [OpenAGH Matematyka](https://open.agh.edu.pl/) | [ZPE Matematyka](https://zpe.gov.pl/) | [Ważniak MIMUW](https://wazniak.mimuw.edu.pl/)",
                            "4. Thomas H. Cormen i współautorzy — *Wprowadzenie do algorytmów* (polskie wydanie, [PWN](https://ksiegarnia.pwn.pl/)) oraz Roger Penrose — *Droga do rzeczywistości* (wyd. polskie).",
                        ],
                    },
                    {
                        "heading": "2. Anglojęzyczne (uzupełniające)",
                        "items": [
                            "5. Gilbert Strang — *Introduction to Linear Algebra.* — [MIT Linear Algebra](https://math.mit.edu/~gs/linearalgebra/)",
                            "6. Charles Petzold — *Code.* — [codehiddenlanguage.com](https://codehiddenlanguage.com/)",
                            "7. Eric Matthes — *Python Crash Course.* — [ehmatthes.github.io/pcc_3e](https://ehmatthes.github.io/pcc_3e/)",
                        ],
                    },
                ],
            },
            {
                "trackId": "FND-4",
                "title": "II. FIZYKA I KOMPUTERY KWANTOWE (Wspólne podstawy — PL w pierwszej kolejności)",
                "sequenceLabel": "Etap czytania",
                "sequence": "Najpierw (po polsku): OpenStax „Fizyka dla szkół wyższych Tom 1–3”, Halliday & Resnick „Podstawy fizyki” oraz polskie podręczniki elektroniki (Horowitz & Hill „Sztuka elektroniki”, ZPE, Forbot) → Na zaawansowanym etapie: Griffiths („Wstęp do mechaniki kwantowej” PL / EN) oraz Nielsen i Chuang.",
                "links": [
                    {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3” (pełny darmowy podręcznik po polsku)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Halliday & Resnick „Podstawy fizyki”, Feynman „Wykłady z fizyki”, Griffiths „Wstęp do mechaniki kwantowej”", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki fizyki, elektroniki i układów cyfrowych", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇵🇱 Forbot — Kursy podstaw elektroniki i techniki cyfrowej po polsku", "url": "https://forbot.pl/blog/kurs-elektroniki-poziom-1-spis-tresci-id5159"},
                    {"label": "🇬🇧 David J. Griffiths — Introduction to Quantum Mechanics (CUP)", "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"},
                    {"label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — Quantum Computation and Quantum Information", "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"}
                ],
                "groups": [
                    {
                        "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
                        "items": [
                            "1. Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach: *OpenStax Fizyka dla szkół wyższych Tom 1–3* ([darmowy dostęp PL](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1)), D. Halliday, R. Resnick, J. Walker — *Podstawy fizyki* ([PWN](https://ksiegarnia.pwn.pl/)), R. P. Feynman — *Feynmana wykłady z fizyki* (PWN), D. J. Griffiths — *Wstęp do mechaniki kwantowej* (polskie wydanie PWN).",
                            "2. Podręczniki podstaw elektroniki i układów cyfrowych po polsku: P. Horowitz, W. Hill — *Sztuka elektroniki. Cz. 1–2* (WKŁ), B. Głocki — *Układy cyfrowe* (WSiP), [ZPE Elektronika](https://zpe.gov.pl/), [OpenAGH](https://open.agh.edu.pl/) oraz [Kursy Forbot](https://forbot.pl/).",
                        ],
                    },
                    {
                        "heading": "2. Anglojęzyczne (etap zaawansowany)",
                        "items": [
                            "3. David J. Griffiths — *Introduction to Quantum Mechanics.* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E)",
                            "4. Michael A. Nielsen, Isaac L. Chuang — *Quantum Computation and Quantum Information.* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)",
                        ],
                    },
                ],
            },
            {
                "trackId": "FND-7",
                "title": "III. CHEMIA, BIOLOGIA I GENETYKA (Wspólne podstawy — PL w pierwszej kolejności)",
                "sequenceLabel": "Etap czytania",
                "sequence": "Następnie (w pierwszej kolejności po polsku): Terence A. Brown („Genomy” PWN) → „Biologia Campbella” (wyd. polskie Rebis) i B. Alberts („Podstawy biologii komórki” PWN) → Polskie podręczniki chemii i biochemii (Stryer „Biochemia”, Jones & Atkins, McMurry) → Uzupełniająco (EN): OpenStax Chemistry 2e i Biology 2e.",
                "links": [
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — T.A. Brown „Genomy”, Stryer „Biochemia”, Alberts „Podstawy biologii komórki”, Jones & Atkins „Chemia ogólna”", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 Dom Wydawniczy REBIS — „Biologia Campbella” (polskie wydanie)", "url": "https://www.rebis.com.pl/"},
                    {"label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki chemii ogólnej, biochemii, biologii i genetyki", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej", "url": "https://openstax.org/details/books/chemistry-2e"},
                    {"label": "🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii", "url": "https://openstax.org/details/books/biology-2e"},
                    {"label": "🇬🇧 Terence A. Brown — Genomes (NCBI Bookshelf)", "url": "https://www.ncbi.nlm.nih.gov/books/NBK21128/"}
                ],
                "groups": [
                    {
                        "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
                        "items": [
                            "1. Terence A. Brown — *Genomy.* (polskie wydanie) — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                            "2. *Biologia Campbella* — polskie wydanie ([Dom Wydawniczy REBIS](https://www.rebis.com.pl/)) oraz Bruce Alberts i współautorzy — *Podstawy biologii komórki* ([PWN](https://ksiegarnia.pwn.pl/)).",
                            "3. Akademickie podręczniki chemii ogólnej, organicznej i biochemii po polsku: L. Stryer i współautorzy — *Biochemia* (PWN), L. Jones, P. Atkins — *Chemia ogólna* (PWN), A. Bielański — *Podstawy chemii nieorganicznej* (PWN), J. McMurry — *Chemia organiczna* (PWN), [OpenAGH Chemia](https://open.agh.edu.pl/) i [ZPE](https://zpe.gov.pl/).",
                        ],
                    },
                    {
                        "heading": "2. Anglojęzyczne (uzupełniające)",
                        "items": [
                            "4. *OpenStax Chemistry 2e* — podręcznik chemii ogólnej: [https://openstax.org/details/books/chemistry-2e](https://openstax.org/details/books/chemistry-2e)",
                            "5. *OpenStax Biology 2e* — podręcznik biologii: [https://openstax.org/details/books/biology-2e](https://openstax.org/details/books/biology-2e)",
                            "6. Akademickie podręczniki biochemii i biologii molekularnej — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/)",
                        ],
                    },
                ],
            },
            {
                "trackId": "A",
                "title": "IV. PROJEKT A — CZŁOWIEK BIOCYFROWO-ROBOTYCZNY (PL w pierwszej kolejności)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "W pierwszej kolejności po polsku: Biologiczne podstawy psychologii (Kalat, PWN) oraz anatomia i fizjologia człowieka (Bochenek, Traczyk, Konturek) → Biofizyka, biomechanika i biomateriały (Jaroszyk, Marciniak, Tadeusiewicz) → Robotyka, elektronika, sterowanie i uczenie maszynowe (Géron wyd. polskie Helion) → Neuroprotetyka i interfejsy mózg–komputer (BCI).",
                "links": [
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — James W. Kalat „Biologiczne podstawy psychologii” oraz podręczniki biofizyki i robotyki", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia człowieka (Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)", "url": "https://pzwl.pl/"},
                    {"label": "🇵🇱 Wydawnictwo Helion — Aurélien Géron „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” (wyd. polskie)", "url": "https://helion.pl/"},
                    {"label": "🇵🇱 OpenAGH — Polskie materiały z inżynierii biomedycznej, biocybernetyki i automatyki", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik online/PDF)", "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"},
                    {"label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Repozytorium GitHub)", "url": "https://github.com/ageron/handson-ml3"}
                ],
                "groups": [
                    {
                        "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
                        "items": [
                            "1. James W. Kalat — *Biologiczne podstawy psychologii.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                            "2. Akademickie podręczniki anatomii i fizjologii człowieka: A. Bochenek, M. Reicher — *Anatomia człowieka* ([PZWL](https://pzwl.pl/)); W. Traczyk, A. Trzebski — *Fizjologia człowieka z elementami fizjologii stosowanej i klinicznej* (PZWL); S. Konturek — *Fizjologia człowieka*.",
                            "3. Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: F. Jaroszyk (red.) — *Biofizyka* (PZWL); J. Marciniak — *Biomateriały* (Politechnika Śląska); seria *Biocybernetyka i Inżynieria Biomedyczna 2000* (PAN, red. M. Nałęcz, R. Tadeusiewicz) — [OpenAGH](https://open.agh.edu.pl/).",
                            "4. Podręczniki robotyki, elektroniki, układów sterowania i AI po polsku: K. Tchoń i współautorzy — *Manipulatory i roboty mobilne*; A. Géron — *Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow* ([Helion](https://helion.pl/)).",
                        ],
                    },
                    {
                        "heading": "2. Anglojęzyczne (uzupełniające i specjalistyczne)",
                        "items": [
                            "5. *OpenStax Anatomy and Physiology 2e.* — [https://openstax.org/details/books/anatomy-and-physiology-2e](https://openstax.org/details/books/anatomy-and-physiology-2e)",
                            "6. Géron — *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.* — [GitHub ageron/handson-ml3](https://github.com/ageron/handson-ml3)",
                            "7. Akademickie podręczniki inżynierii tkankowej, neuroprotetyki i interfejsów mózg–komputer — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | [Physiological Reviews BCI](https://doi.org/10.1152/physrev.00027.2016)",
                        ],
                    },
                ],
            },
            {
                "trackId": "B",
                "title": "V. PROJEKT B — CYFROWY UMYSŁ (PL w pierwszej kolejności)",
                "sequenceLabel": "Kolejność czytania (Etapy 2 → 3 → 4)",
                "sequence": "W pierwszej kolejności po polsku: Kalat („Biologiczne podstawy psychologii”), Longstaff („Neurobiologia”), Nęcka („Psychologia poznawcza”), Miłkowski i Poczobut („Przewodnik po filozofii umysłu”) oraz Seung („Konektom” — wyd. polskie) → Później (EN): Dayan & Abbott („Theoretical Neuroscience”), Izhikevich („Dynamical Systems in Neuroscience”), Sandberg & Bostrom („Whole Brain Emulation: A Roadmap”) → Na zaawansowanym etapie: Kandel („Principles of Neural Science”), Squire („Fundamental Neuroscience”), Churchland & Sejnowski („The Computational Brain”).",
                "links": [
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — J.W. Kalat „Biologiczne podstawy psychologii”, A. Longstaff „Neurobiologia”, E. Nęcka „Psychologia poznawcza”", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 Prof. Włodzisław Duch (UMK) — Polskojęzyczne materiały z kognitywistyki, neuroinformatyki i modelowania mózgu", "url": "https://www.fizyka.umk.pl/~duch/"},
                    {"label": "🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu, kognitywistyka i problem świadomości po polsku", "url": "https://ccpress.pl/"},
                    {"label": "🇬🇧 Eugene M. Izhikevich — Dynamical Systems in Neuroscience (Darmowy PDF autora)", "url": "https://www.izhikevich.org/publications/dsn.pdf"},
                    {"label": "🇬🇧 Anders Sandberg, Nick Bostrom — Whole Brain Emulation: A Roadmap (PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                    {"label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                    {"label": "🇬🇧 Paul Miller — An Introductory Course in Computational Neuroscience", "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"},
                    {"label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — The Computational Brain", "url": "https://mitpress.mit.edu/9780262531207/the-computational-brain/"},
                    {"label": "🇬🇧 Larry Squire et al. — Fundamental Neuroscience (ScienceDirect)", "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"}
                ],
                "groups": [
                    {
                        "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
                        "items": [
                            "1. James W. Kalat — *Biologiczne podstawy psychologii.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                            "2. Podręczniki neurobiologii i fizjologii układu nerwowego po polsku: Alan Longstaff — *Neurobiologia. Krótkie wykłady* ([PWN](https://ksiegarnia.pwn.pl/)); T. Górska, A. Grabowska, J. Zagrodzka (red.) — *Mózg a zachowanie* (PWN).",
                            "3. Podręczniki psychologii poznawczej i konektomiki po polsku: Edward Nęcka, Jarosław Orzechowski, Błażej Szymura — *Psychologia poznawcza* ([PWN](https://ksiegarnia.pwn.pl/)); Sebastian Seung — *Konektom. Jak połączenia w mózgu kształtują naszą tożsamość* (polskie wydanie).",
                            "4. Wprowadzenia do filozofii umysłu, kognitywistyki i problemu świadomości po polsku: Marcin Miłkowski, Robert Poczobut (red.) — *Przewodnik po filozofii umysłu*; wykłady z neuroinformatyki prof. Włodzisława Ducha ([UMK](https://www.fizyka.umk.pl/~duch/)) oraz [Centrum Kopernika / CCPress](https://ccpress.pl/).",
                        ],
                    },
                    {
                        "heading": "2. Anglojęzyczne (etapy 3 i 4 — zaawansowane modelowanie i neuronauka)",
                        "items": [
                            "5. Eric R. Kandel i współautorzy — *Principles of Neural Science.* — [McGraw Hill](https://www.mheducation.com/)",
                            "6. Larry Squire i współautorzy — *Fundamental Neuroscience.* — [ScienceDirect](https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience)",
                            "7. Peter Dayan, L. F. Abbott — *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems.* — [MIT Press](https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/)",
                            "8. Eugene M. Izhikevich — *Dynamical Systems in Neuroscience.* — [Pełny PDF autora](https://www.izhikevich.org/publications/dsn.pdf)",
                            "9. Sebastian Seung — *Connectome: How the Brain's Wiring Makes Us Who We Are.* — [Seung Lab MIT](https://seunglab.org/)",
                            "10. Paul Miller — *An Introductory Course in Computational Neuroscience.* — [MIT Press](https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/)",
                            "11. Patricia S. Churchland, Terrence J. Sejnowski — *The Computational Brain.* — [MIT Press](https://mitpress.mit.edu/9780262531207/the-computational-brain/)",
                            "12. Anders Sandberg, Nick Bostrom — *Whole Brain Emulation: A Roadmap.* — [Pełny raport PDF](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)",
                        ],
                    },
                ],
            },
            {
                "trackId": "C",
                "title": "Projekt C — Maszyny analogowe i obliczenia fizyczne (PL w pierwszej kolejności)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Elektronika analogowa (po polsku: Horowitz & Hill, OpenAGH, ZPE, Forbot) → układy dynamiczne → modelowanie matematyczne (Osowski, Tadeusiewicz) → fizyczne modele neuronów → obliczenia neuromorficzne.",
                "links": [
                    {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz C/A", "url": "https://zpe.gov.pl/"},
                    {"label": "🇵🇱 OpenAGH — E-podręczniki z elektroniki, układów dynamicznych i fizyki po polsku", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇵🇱 Forbot — Kursy elektroniki analogowej, wzmacniaczy operacyjnych i ADC/DAC po polsku", "url": "https://forbot.pl/"},
                    {"label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering", "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"},
                    {"label": "🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks", "url": "https://arxiv.org/list/cs.NE/recent"},
                    {"label": "🇬🇧 MIT OCW — Circuits & Electronics", "url": "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"}
                ],
                "groups": [
                    {
                        "heading": "1. Po polsku (w pierwszej kolejności)",
                        "items": [
                            "Podręczniki akademickie z elektroniki analogowej: Paul Horowitz, Winfield Hill — *Sztuka elektroniki* (wyd. polskie WKŁ); wzmacniacze, oscylatory, filtry, sprzężenie zwrotne i układy dynamiczne — [E-podręczniki OpenAGH](https://open.agh.edu.pl/)",
                            "Materiały dydaktyczne o przetwornikach analogowo-cyfrowych (ADC) i cyfrowo-analogowych (DAC) — [Materiały ZPE](https://zpe.gov.pl/) | [Kursy Forbot](https://forbot.pl/)",
                            "Polska literatura o sieciach neuronowych i biocybernetyce: Stanisław Osowski — *Sieci neuronowe do przetwarzania informacji* (Oficyna Wydawnicza PW); Ryszard Tadeusiewicz — *Sieci neuronowe*.",
                            "Zintegrowana Platforma Edukacyjna — punkt wyjścia do szukania materiałów o elektronice: [https://zpe.gov.pl/](https://zpe.gov.pl/)",
                        ],
                    },
                    {
                        "heading": "2. Po angielsku (uzupełniające i badawcze)",
                        "items": [
                            "Materiały techniczne dotyczące analog computing — [MIT OpenCourseWare Electronics](https://ocw.mit.edu/search/?q=analog+computing)",
                            "Materiały badawcze dotyczące neuromorphic computing i analog neural networks — [Frontiers in Neuromorphic Engineering](https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering)",
                            "Publikacje o fizycznych modelach neuronów oraz analogowych i hybrydowych procesorach — [arXiv cs.NE](https://arxiv.org/list/cs.NE/recent) | [Neuronal Dynamics (EPFL)](https://neuronaldynamics.epfl.ch/)",
                        ],
                    },
                ],
            },
            {
                "trackId": "D",
                "title": "Projekt D — „Frankenstein”: biotechnologia i tworzenie organizmów (PL w pierwszej kolejności)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "W pierwszej kolejności po polsku: Biologia komórki (Alberts, PWN) → genetyka (Brown „Genomy”, Węgleński) → embriologia (Bartel „Embriologia”, PZWL) → komórki macierzyste i inżynieria tkankowa → biologia syntetyczna, bioetyka (Komitet Bioetyki PAN) i nauka a SF (Stanisław Lem „Summa technologiae”).",
                "links": [
                    {"label": "🇵🇱 Komitet Bioetyki Polskiej Akademii Nauk (PAN) — Stanowiska i opracowania bioetyczne po polsku", "url": "https://bioetyka.pan.pl/"},
                    {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Hieronim Bartel „Embriologia”, histologia i medycyna regeneracyjna", "url": "https://pzwl.pl/"},
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Alberts „Podstawy biologii komórki”, Brown „Genomy”, Węgleński „Genetyka molekularna”", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 ZPE — Biologia komórki, genetyka i biotechnologia po polsku", "url": "https://zpe.gov.pl/"},
                    {"label": "🇬🇧 National Academies — Responsible Development of Synthetic Biology", "url": "https://www.nationalacademies.org/"},
                    {"label": "🇬🇧 NCBI Bookshelf — Darmowe podręczniki biologii komórki, genetyki i embriologii", "url": "https://www.ncbi.nlm.nih.gov/books/"},
                    {"label": "🇬🇧 ISSCR — International Society for Stem Cell Research", "url": "https://www.isscr.org/"}
                ],
                "groups": [
                    {
                        "heading": "1. Po polsku (w pierwszej kolejności)",
                        "items": [
                            "Podręczniki akademickie z biologii komórki, genetyki i biologii rozwoju: B. Alberts — *Podstawy biologii komórki* ([PWN](https://ksiegarnia.pwn.pl/)), T. A. Brown — *Genomy* (PWN), P. Węgleński — *Genetyka molekularna* (PWN) oraz [ZPE Biologia](https://zpe.gov.pl/).",
                            "Podręczniki z embriologii i komórek macierzystych po polsku: Hieronim Bartel — *Embriologia. Podręcznik dla studentów* ([PZWL](https://pzwl.pl/)).",
                            "Literatura o inżynierii tkankowej, medycynie regeneracyjnej, bioetyce i granicach SF: publikacje [Komitetu Bioetyki PAN](https://bioetyka.pan.pl/), K. Szewczyk — *Bioetyka* (PWN) oraz Stanisław Lem — *Summa technologiae*.",
                        ],
                    },
                    {
                        "heading": "2. Po angielsku (uzupełniające i badawcze)",
                        "items": [
                            "National Academies — materiały o odpowiedzialnym rozwoju biologii syntetycznej: [https://www.nationalacademies.org/](https://www.nationalacademies.org/)",
                            "Publikacje akademickie o stem cells, developmental biology, tissue engineering i synthetic biology — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | [ISSCR](https://www.isscr.org/) | [Nature Synthetic Biology](https://www.nature.com/subjects/synthetic-biology)",
                        ],
                    },
                ],
            },
            {
                "trackId": "E",
                "title": "Projekt E — Filozofia (PL w pierwszej kolejności)",
                "sequenceLabel": "Zastosowanie",
                "sequence": "Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.",
                "links": [
                    {"label": "🇵🇱 Copernicus Center Press (ks. prof. Michał Heller — „Filozofia nauki. Wprowadzenie”)", "url": "https://ccpress.pl/"},
                    {"label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Wykłady i kursy po polsku", "url": "https://www.copernicuscenter.edu.pl/"},
                    {"label": "🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka)", "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"},
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — T.S. Kuhn „Struktura rewolucji naukowych”, W. Tatarkiewicz „Historia filozofii”, K. Szewczyk „Bioetyka”", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇬🇧 Stanford Encyclopedia of Philosophy (SEP)", "url": "https://plato.stanford.edu/"},
                    {"label": "🇬🇧 Internet Encyclopedia of Philosophy (IEP)", "url": "https://iep.utm.edu/"}
                ],
                "groups": [
                    {
                        "heading": "1. Po polsku (w pierwszej kolejności)",
                        "items": [
                            "Alan Chalmers — *Czym jest to, co zwiemy nauką?* — [Katalog Biblioteki Narodowej](https://katalogi.bn.org.pl/)",
                            "Thomas S. Kuhn — *Struktura rewolucji naukowych.* — [Wydawnictwo PWN / Aletheia](https://ksiegarnia.pwn.pl/)",
                            "Michał Heller — *Filozofia nauki. Wprowadzenie* oraz *Filozofia przyrody* — [Copernicus Center Press](https://ccpress.pl/)",
                            "Władysław Tatarkiewicz — *Historia filozofii. Tom 1–3* (PWN) oraz klasyka filozofii starożytnej w polskich przekładach ([Wolne Lektury](https://wolnelektury.pl/katalog/gatunek/filozofia/)).",
                        ],
                    },
                    {
                        "heading": "2. Obszary do dalszego uzupełnienia (PL i EN)",
                        "items": [
                            "Filozofia starożytna: Platon (*Państwo*, *Timajos*), Arystoteles (*Metafizyka*, *O duszy*) i stoicy (*Rozmyślania* Marka Aureliusza, Seneka, Epiktet) — [Wolne Lektury: Filozofia (PL)](https://wolnelektury.pl/katalog/gatunek/filozofia/) | [SEP Ancient Philosophy](https://plato.stanford.edu/)",
                            "Filozofia umysłu i problem świadomości — M. Miłkowski, R. Poczobut (red.) *Przewodnik po filozofii umysłu* (PL) | [Centrum Kopernika (PL)](https://www.copernicuscenter.edu.pl/) | [SEP Philosophy of Mind](https://plato.stanford.edu/entries/mind-identity/)",
                            "Filozofia techniki, bioetyka i etyka środowiskowa — K. Szewczyk *Bioetyka Tom 1–2* (PWN), S. Lem *Summa technologiae*, [Komitet Bioetyki PAN](https://bioetyka.pan.pl/) | [SEP Philosophy of Technology](https://plato.stanford.edu/entries/technology/)",
                        ],
                    },
                ],
            },
            {
                "trackId": "F",
                "title": "Projekt F — Człowiek w kosmosie (PL w pierwszej kolejności + darmowe źródła NASA i ESA)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Podstawy fizyki (OpenStax Fizyka PL) → mechanika orbitalna → technika kosmiczna (POLSA, ESERO Polska) → fizjologia kosmiczna (medycyna lotnicza i kosmiczna, NASA/ESA) → systemy podtrzymywania życia i habitaty.",
                "links": [
                    {"label": "🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o eksploracji kosmosu, mikrograwitacji i habitatach", "url": "https://esero.kopernik.org.pl/"},
                    {"label": "🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja kosmiczna, inżynieria i medycyna kosmiczna po polsku", "url": "https://polsa.gov.pl/"},
                    {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (Mechanika, grawitacja, ruch orbitalny po polsku)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                    {"label": "🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)", "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"},
                    {"label": "🛰️ ESA — Edukacja kosmiczna (Teach with Space)", "url": "https://education.esa.int/teach-with-space/"},
                    {"label": "👩‍🚀 ESA — Eksploracja załogowa (Human and Robotic Exploration)", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"},
                    {"label": "🌱 MELiSSA Foundation — Systemy podtrzymywania życia (BLSS)", "url": "https://www.melissafoundation.org/"}
                ],
                "groups": [
                    {
                        "heading": "1. Po polsku (w pierwszej kolejności)",
                        "items": [
                            "ESERO Polska (Biuro Edukacji Kosmicznej ESA przy Centrum Nauki Kopernik) — polskojęzyczne materiały dydaktyczne o bazach księżycowych/marsjańskich, fizjologii w mikrograwitacji i mechanice orbitalnej: [https://esero.kopernik.org.pl/](https://esero.kopernik.org.pl/)",
                            "Polska Agencja Kosmiczna (POLSA) — opracowania o technologiach kosmicznych, sektorze kosmicznym i medycynie kosmicznej po polsku: [https://polsa.gov.pl/](https://polsa.gov.pl/)",
                            "Podręczniki polskojęzyczne: *OpenStax Fizyka dla szkół wyższych Tom 1* (mechanika i grawitacja po polsku), Krzysztof Kwarecki (red.) — *Medycyna lotnicza i kosmiczna* (PZWL), literatura Polskiego Towarzystwa Astronautycznego (*Astronautyka*).",
                        ],
                    },
                    {
                        "heading": "2. Darmowe źródła międzynarodowe (NASA i ESA)",
                        "items": [
                            "NASA — zdrowie człowieka w kosmosie: [https://www.nasa.gov/reference/fundamentals-of-human-health/](https://www.nasa.gov/reference/fundamentals-of-human-health/)",
                            "ESA — edukacja kosmiczna: [https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)",
                            "ESA — eksploracja załogowa: [https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)",
                        ],
                    },
                    {
                        "heading": "3. Tematy do dalszego studiowania",
                        "items": [
                            "Fizjologia człowieka w mikrograwitacji — [NASA Human Research Program](https://www.nasa.gov/hrp/)",
                            "Promieniowanie kosmiczne i ochrona biologiczna — [NASA Space Radiation](https://www.nasa.gov/hrp/elements/radiation/)",
                            "Mechanika orbitalna i napędy — [MIT OCW Space Systems Engineering](https://ocw.mit.edu/search/?q=orbital+mechanics)",
                            "Systemy podtrzymywania życia — [Projekt ESA MELiSSA](https://www.melissafoundation.org/)",
                            "Projektowanie habitatów i statków kosmicznych — [NASA NTRS](https://ntrs.nasa.gov/)",
                            "Uprawa żywności, odzysk wody i wykorzystanie zasobów lokalnych (ISRU) — [NASA ISRU](https://www.nasa.gov/mission_pages/station/research/news/b4h-3rd/ev-isru)",
                            "Psychologia izolacji i medycyna długotrwałych misji — [ESA Human Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)",
                        ],
                    },
                ],
            },
            {
                "trackId": "G",
                "title": "Projekt G — Człowiek na Ziemi i ochrona ekosystemu (PL w pierwszej kolejności)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "W pierwszej kolejności po polsku: Podstawy ekologii i funkcjonowanie ekosystemów (January Weiner „Życie i ewolucja biosfery”, PWN) → presje środowiskowe i monitoring (GIOŚ, Politechnika Śląska) → technologie ochronne i inżynieria środowiska (Jan Krystek „Ochrona środowiska dla inżynierów”, Rosik-Dulewska) → ekonomia i polityka środowiskowa (EEA PL).",
                "links": [
                    {"label": "🇵🇱 Politechnika Śląska — Materiały dotyczące podstaw ochrony środowiska po polsku", "url": "https://www.polsl.pl/"},
                    {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz January Weiner „Życie i ewolucja biosfery”", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ — Państwowy Monitoring Środowiska w Polsce)", "url": "https://www.gios.gov.pl/"},
                    {"label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie materiały o ekologii, odnawialnych źródłach energii i ochronie środowiska", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇵🇱 Europejska Agencja Środowiska (EEA w języku polskim — Ekonomia ekologiczna, GOZ, LCA)", "url": "https://www.eea.europa.eu/pl"},
                    {"label": "🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska", "url": "https://education.esa.int/teach-with-space/"}
                ],
                "groups": [
                    {
                        "heading": "1. Po polsku (w pierwszej kolejności)",
                        "items": [
                            "Jan Krystek — *Ochrona środowiska dla inżynierów.* — [Księgarnia Naukowa PWN](https://ksiegarnia.pwn.pl/)",
                            "January Weiner — *Życie i ewolucja biosfery. Podręcznik ekologii ogólnej* ([PWN](https://ksiegarnia.pwn.pl/)) oraz Czesława Rosik-Dulewska — *Podstawy gospodarki odpadami* (PWN).",
                            "Podręczniki akademickie z ekologii, ochrony środowiska i OZE — [OpenAGH (PL)](https://open.agh.edu.pl/) | [ZPE Ekologia (PL)](https://zpe.gov.pl/)",
                            "Materiały polskich uczelni i instytucji dotyczące ochrony wód, powietrza i gleby — [Politechnika Śląska](https://www.polsl.pl/) | [GIOŚ Monitoring Środowiska](https://www.gios.gov.pl/)",
                        ],
                    },
                    {
                        "heading": "2. Źródła bezpłatne",
                        "items": [
                            "Politechnika Śląska — materiały dotyczące podstaw ochrony środowiska: [https://www.polsl.pl/](https://www.polsl.pl/)",
                            "Europejska Agencja Środowiska (serwis po polsku): [https://www.eea.europa.eu/pl](https://www.eea.europa.eu/pl)",
                            "ESA Education — edukacja o Ziemi, klimacie i obserwacji środowiska: [https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)",
                        ],
                    },
                    {
                        "heading": "3. Tematy do dalszego studiowania",
                        "items": [
                            "Ekologia populacji i ekosystemów — J. Weiner *Życie i ewolucja biosfery* (PWN) | [OpenStax Biology: Ecology](https://openstax.org/details/books/biology-2e)",
                            "Różnorodność biologiczna i ochrona siedlisk — [GIOŚ](https://www.gios.gov.pl/) | [IPBES Global Assessment](https://www.ipbes.net/)",
                            "Obiegi biogeochemiczne i funkcjonowanie gleby — [FAO Soils Portal](https://www.fao.org/soils-portal/en/)",
                            "Zmiany klimatu oraz zanieczyszczenia — [Nauka o Klimacie (PL)](https://naukaoklimacie.pl/) | [Raporty IPCC](https://www.ipcc.ch/)",
                            "Ochrona przyrody, renaturyzacja i odbudowa ekosystemów — [EEA Nature & Biodiversity (PL)](https://www.eea.europa.eu/pl)",
                            "Odnawialne źródła energii i efektywność energetyczna — [OpenAGH Energetyka (PL)](https://open.agh.edu.pl/) | [IEA Renewables](https://www.iea.org/)",
                            "Gospodarka obiegu zamkniętego — [EEA Circular Economy (PL)](https://www.eea.europa.eu/pl)",
                            "Ocena cyklu życia produktów (LCA) i ekonomia ekologiczna — [European Platform on LCA](https://eplca.jrc.ec.europa.eu/)",
                            "Monitoring środowiska z użyciem czujników, satelitów i AI — [POLSA Obserwacja Ziemi (PL)](https://polsa.gov.pl/) | [ESA Copernicus](https://earth.esa.int/)",
                        ],
                    },
                ],
            },
        ],
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
                        "id": "bib-1-pl",
                        "citation": "🇵🇱 Kalat, J. W. — Biologiczne podstawy psychologii (Wydawnictwo Naukowe PWN) oraz Tadeusiewicz, R., Nałęcz, M. (red.) — Biocybernetyka i Inżynieria Biomedyczna (PAN / PWN).",
                        "url": "https://ksiegarnia.pwn.pl/",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    },
                    {
                        "id": "bib-1",
                        "citation": "🇬🇧 Lebedev, M. A., & Nicolelis, M. A. (2017). Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation. Physiological Reviews.",
                        "url": "https://doi.org/10.1152/physrev.00027.2016",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    },
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
                        "id": "bib-2-pl",
                        "citation": "🇵🇱 Horowitz, P., Hill, W. — Sztuka elektroniki (WKŁ) oraz Osowski, S. — Sieci neuronowe do przetwarzania informacji (Oficyna Wydawnicza Politechniki Warszawskiej).",
                        "url": "https://open.agh.edu.pl/",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    },
                    {
                        "id": "bib-2",
                        "citation": "🇬🇧 Indiveri, G., et al. (2011). Neuromorphic silicon neuron circuits. Frontiers in Neuroscience.",
                        "url": "https://doi.org/10.3389/fnins.2011.00073",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    },
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
                        "id": "bib-3-pl",
                        "citation": "🇵🇱 Weiner, J. — Życie i ewolucja biosfery. Podręcznik ekologii ogólnej (Wydawnictwo Naukowe PWN) oraz Krystek, J. — Ochrona środowiska dla inżynierów (PWN).",
                        "url": "https://ksiegarnia.pwn.pl/",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    },
                    {
                        "id": "bib-3",
                        "citation": "🇬🇧 Lasseur, C., et al. (2010). MELiSSA: The European project of closed life support system. Gravitational and Space Biology.",
                        "url": "https://www.melissafoundation.org/",
                        "addedBy": "Administrator",
                        "approvalStatus": "approved",
                    },
                ],
            },
        },
    ],
    "materials": [
        {
            "id": "mat-13",
            "trackId": "E",
            "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "subprojectId": None,
            "title": "BIBLIOTEKA PROJEKTU — VI. Kolejność czytania i zasady pracy z literaturą (w pierwszej kolejności źródła polskojęzyczne)",
            "type": "Przewodnik metodologiczny GOLEM 15",
            "author": "Administrator",
            "content": (
                "1. Najpierw (po polsku): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Helion); "
                "Eric Matthes — „Python. Instrukcje dla programisty” (Helion); Podstawy matematyki i algebry liniowej (OpenAGH, ZPE, Skoczylas); "
                "Podręcznik fizyki ogólnej po polsku (OpenStax „Fizyka dla szkół wyższych Tom 1–3”, Halliday & Resnick „Podstawy fizyki”).\n"
                "2. Następnie (po polsku): Terence A. Brown — „Genomy” (PWN); Podstawy chemii, biologii i biochemii („Biologia Campbella” Rebis, Stryer „Biochemia” PWN, Alberts „Podstawy biologii komórki” PWN); "
                "James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n"
                "3. Później (PL i EN): A. Longstaff „Neurobiologia” (PWN), E. Nęcka „Psychologia poznawcza” (PWN), S. Seung „Konektom” (wyd. polskie); "
                "Dayan & Abbott „Theoretical Neuroscience”; Izhikevich „Dynamical Systems in Neuroscience”; Sandberg & Bostrom „Whole Brain Emulation: A Roadmap”.\n"
                "4. Na zaawansowanym etapie: D. J. Griffiths — „Wstęp do mechaniki kwantowej” (wyd. polskie PWN / CUP); Kandel — „Principles of Neural Science”; "
                "Squire — „Fundamental Neuroscience”; Churchland & Sejnowski — „The Computational Brain”; Nielsen i Chuang — „Quantum Computation and Quantum Information”.\n\n"
                "Zasada: Zaczynamy od polskojęzycznych podręczników i otwartych zasobów po polsku — najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja. "
                "Pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi."
            ),
            "url": "https://open.agh.edu.pl/",
            "links": [
                {"label": "1️⃣ 🇵🇱 Etap I (Po polsku): Petzold „Kod”, Matthes „Python” (Helion), OpenAGH Matematyka oraz OpenStax Fizyka Tom 1–3 (PL)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                {"label": "2️⃣ 🇵🇱 Etap II (Po polsku): T.A. Brown „Genomy”, „Biologia Campbella”, Stryer „Biochemia” oraz J.W. Kalat „Biologiczne podstawy psychologii” (PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "3️⃣ 🇵🇱/🇬🇧 Etap III: Longstaff „Neurobiologia”, Seung „Konektom” (PL) + Dayan & Abbott, Izhikevich, Sandberg & Bostrom (WBE Roadmap PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                {"label": "4️⃣ 🇵🇱/🇬🇧 Etap IV: Griffiths „Wstęp do mechaniki kwantowej” (PWN) + Kandel, Squire, Churchland & Sejnowski, Nielsen & Chuang", "url": "https://mitpress.mit.edu/9780262533393/the-computational-brain/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:25:00Z",
        },
        {
            "id": "mat-8",
            "trackId": "B",
            "branchTopic": "Modelowanie neuronów i sieci neuronalnych.",
            "subprojectId": "sub-1",
            "title": "BIBLIOTEKA PROJEKTU — I. Matematyka i Informatyka (w pierwszej kolejności po polsku: Petzold, Matthes, OpenAGH, ZPE, Ważniak MIMUW + Strang)",
            "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "1. W pierwszej kolejności — Polskojęzyczne:\n"
                "• Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II.” (Wydawnictwo Helion)\n"
                "• Eric Matthes — „Python. Instrukcje dla programisty. Wydanie III.” (Wydawnictwo Helion) + oficjalny polski samouczek Pythona\n"
                "• Podręczniki matematyki i algebry liniowej po polsku: e-podręczniki OpenAGH, ZPE, Ważniak MIMUW, M. Gewert i Z. Skoczylas („Algebra liniowa”, „Analiza matematyczna”), "
                "T. H. Cormen i współautorzy („Wprowadzenie do algorytmów”, PWN), R. Penrose („Droga do rzeczywistości”, wyd. polskie).\n\n"
                "2. Uzupełniająco — Anglojęzyczne:\n"
                "• Gilbert Strang — „Introduction to Linear Algebra.”\n"
                "• Charles Petzold — „Code: The Hidden Language of Computer Hardware and Software.”\n"
                "• Eric Matthes — „Python Crash Course.”"
            ),
            "url": "https://open.agh.edu.pl/",
            "links": [
                {"label": "🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” oraz Eric Matthes — „Python. Instrukcje dla programisty” (Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 OpenAGH — Darmowe e-podręczniki akademickie: Matematyka i Algebra Liniowa po polsku", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Ważniak MIMUW (UW) — Darmowe kursy akademickie z matematyki i informatyki po polsku", "url": "https://wazniak.mimuw.edu.pl/"},
                {"label": "🇵🇱 Oficjalny samouczek języka Python po polsku (docs.python.org/pl)", "url": "https://docs.python.org/pl/3/tutorial/"},
                {"label": "🇬🇧 Gilbert Strang — „Introduction to Linear Algebra” & MIT 18.06", "url": "https://math.mit.edu/~gs/linearalgebra/"},
                {"label": "🇬🇧 Charles Petzold — „Code” (Oficjalna strona autora)", "url": "https://codehiddenlanguage.com/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:00:00Z",
        },
        {
            "id": "mat-9",
            "trackId": "C",
            "branchTopic": "Komputery analogowe i mechaniczne.",
            "subprojectId": "sub-2",
            "title": "BIBLIOTEKA PROJEKTU — II. Fizyka i Komputery Kwantowe (w pierwszej kolejności po polsku: OpenStax Fizyka PL, Halliday & Resnick, Griffiths PWN, Horowitz & Hill + Nielsen & Chuang)",
            "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "1. W pierwszej kolejności — Polskojęzyczne:\n"
                "• Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach: OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3” (darmowy podręcznik PL); "
                "D. Halliday, R. Resnick, J. Walker — „Podstawy fizyki. Tom 1–5” (PWN); R. P. Feynman — „Feynmana wykłady z fizyki” (PWN); "
                "David J. Griffiths — „Wstęp do mechaniki kwantowej” (polskie wydanie PWN).\n"
                "• Podręczniki podstaw elektroniki i układów cyfrowych po polsku: P. Horowitz, W. Hill — „Sztuka elektroniki. Cz. 1–2” (WKŁ); B. Głocki — „Układy cyfrowe” (WSiP); ZPE i kursy Forbot.\n\n"
                "2. Uzupełniająco — Anglojęzyczne:\n"
                "• David J. Griffiths — „Introduction to Quantum Mechanics.”\n"
                "• Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information.”"
            ),
            "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1",
            "links": [
                {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tomy 1–3” (darmowy podręcznik akademicki po polsku)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Halliday & Resnick „Podstawy fizyki” oraz D.J. Griffiths „Wstęp do mechaniki kwantowej”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 ZPE / OpenAGH / Forbot — Podstawy elektroniki analogowej i układów cyfrowych po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇬🇧 David J. Griffiths — „Introduction to Quantum Mechanics” (Cambridge University Press)", "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"},
                {"label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”", "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:05:00Z",
        },
        {
            "id": "mat-10",
            "trackId": "D",
            "branchTopic": "Genetyka, DNA i regulacja genów.",
            "subprojectId": None,
            "title": "BIBLIOTEKA PROJEKTU — III. Chemia, Biologia i Genetyka (w pierwszej kolejności po polsku: Brown „Genomy”, „Biologia Campbella”, Alberts, Stryer + OpenStax 2e)",
            "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "1. W pierwszej kolejności — Polskojęzyczne:\n"
                "• Terence A. Brown — „Genomy” (polskie wydanie, Wydawnictwo Naukowe PWN).\n"
                "• „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS) oraz Bruce Alberts i współautorzy — „Podstawy biologii komórki” (PWN).\n"
                "• Akademickie podręczniki chemii ogólnej, organicznej i biochemii po polsku: L. Stryer — „Biochemia” (PWN), L. Jones & P. Atkins — „Chemia ogólna” (PWN), "
                "A. Bielański — „Podstawy chemii nieorganicznej” (PWN), J. McMurry — „Chemia organiczna” (PWN) oraz darmowe zasoby OpenAGH i ZPE.\n\n"
                "2. Uzupełniająco — Anglojęzyczne:\n"
                "• OpenStax „Chemistry 2e” — podręcznik chemii ogólnej.\n"
                "• OpenStax „Biology 2e” — podręcznik biologii.\n"
                "• Akademickie podręczniki biochemii i biologii molekularnej (NCBI Bookshelf)."
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 Terence A. Brown — „Genomy”, L. Stryer — „Biochemia”, B. Alberts — „Podstawy biologii komórki” (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)", "url": "https://www.rebis.com.pl/"},
                {"label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki chemii, biochemii, biologii i genetyki", "url": "https://open.agh.edu.pl/"},
                {"label": "🇬🇧 OpenStax „Chemistry 2e” — darmowy podręcznik chemii ogólnej online", "url": "https://openstax.org/details/books/chemistry-2e"},
                {"label": "🇬🇧 OpenStax „Biology 2e” — darmowy podręcznik biologii online", "url": "https://openstax.org/details/books/biology-2e"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:10:00Z",
        },
        {
            "id": "mat-11",
            "trackId": "A",
            "branchTopic": "Interfejsy mózg–komputer.",
            "subprojectId": "sub-1",
            "title": "BIBLIOTEKA PROJEKTU — IV. Projekt A: Człowiek biocyfrowo-robotyczny (w pierwszej kolejności po polsku: Kalat, Bochenek, Traczyk, Jaroszyk, Marciniak, Tadeusiewicz, Géron PL + OpenStax Anatomy 2e)",
            "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "1. W pierwszej kolejności — Polskojęzyczne:\n"
                "• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n"
                "• Akademickie podręczniki anatomii i fizjologii człowieka: A. Bochenek, M. Reicher — „Anatomia człowieka” (PZWL); W. Traczyk, A. Trzebski — „Fizjologia człowieka” (PZWL); S. Konturek — „Fizjologia człowieka”.\n"
                "• Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: F. Jaroszyk (red.) — „Biofizyka” (PZWL); J. Marciniak — „Biomateriały”; "
                "seria „Biocybernetyka i Inżynieria Biomedyczna 2000” (PAN, red. M. Nałęcz, R. Tadeusiewicz).\n"
                "• Podręczniki robotyki, elektroniki, sterowania i uczenia maszynowego po polsku: K. Tchoń i współautorzy — „Manipulatory i roboty mobilne”; "
                "Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i TensorFlow” (wyd. polskie Helion).\n\n"
                "2. Uzupełniająco — Anglojęzyczne:\n"
                "• OpenStax „Anatomy and Physiology 2e.”\n"
                "• Aurélien Géron — „Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.”\n"
                "• Akademickie podręczniki inżynierii tkankowej, neuroprotetyki i interfejsów mózg–komputer."
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia człowieka (Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)", "url": "https://pzwl.pl/"},
                {"label": "🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i TensorFlow” (Wydawnictwo Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 OpenAGH — Inżynieria biomedyczna, biocybernetyka i automatyka po polsku", "url": "https://open.agh.edu.pl/"},
                {"label": "🇬🇧 OpenStax „Anatomy and Physiology 2e” — darmowy podręcznik online", "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"},
                {"label": "🇬🇧 IEEE EMBS — Engineering in Medicine and Biology (Neuroprotetyka i BCI)", "url": "https://www.embs.org/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:15:00Z",
        },
        {
            "id": "mat-12",
            "trackId": "B",
            "branchTopic": "Świadomość oraz hipotetyczna emulacja całego mózgu.",
            "subprojectId": "sub-1",
            "title": "BIBLIOTEKA PROJEKTU — V. Projekt B: Cyfrowy umysł (w pierwszej kolejności po polsku: Kalat, Longstaff, Nęcka, Seung „Konektom”, Miłkowski & Poczobut + Kandel, Squire, Dayan & Abbott, Izhikevich, Sandberg & Bostrom)",
            "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "1. W pierwszej kolejności — Polskojęzyczne:\n"
                "• James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN).\n"
                "• Podręczniki neurobiologii i fizjologii układu nerwowego po polsku: Alan Longstaff — „Neurobiologia. Krótkie wykłady” (PWN); T. Górska, A. Grabowska, J. Zagrodzka — „Mózg a zachowanie” (PWN).\n"
                "• Podręczniki psychologii poznawczej i konektomiki po polsku: Edward Nęcka, Jarosław Orzechowski, Błażej Szymura — „Psychologia poznawcza” (PWN); "
                "Sebastian Seung — „Konektom. Jak połączenia w mózgu kształtują naszą tożsamość” (wyd. polskie).\n"
                "• Wprowadzenia do filozofii umysłu i problemu świadomości po polsku: M. Miłkowski, R. Poczobut (red.) — „Przewodnik po filozofii umysłu”; "
                "wykłady z kognitywistyki i neuroinformatyki prof. Włodzisława Ducha (UMK) oraz publikacje Centrum Kopernika.\n\n"
                "2. Uzupełniająco i na zaawansowanym etapie — Anglojęzyczne:\n"
                "• Eric R. Kandel i współautorzy — „Principles of Neural Science.”\n"
                "• Larry Squire i współautorzy — „Fundamental Neuroscience.”\n"
                "• Peter Dayan, L. F. Abbott — „Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems.”\n"
                "• Eugene M. Izhikevich — „Dynamical Systems in Neuroscience.”\n"
                "• Paul Miller — „An Introductory Course in Computational Neuroscience.”\n"
                "• Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain.”\n"
                "• Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap.”"
            ),
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — J.W. Kalat „Biologiczne podstawy psychologii”, A. Longstaff „Neurobiologia”, E. Nęcka „Psychologia poznawcza”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 Prof. Włodzisław Duch (UMK) — Polskie wykłady z kognitywistyki, neuroinformatyki i modelowania mózgu", "url": "https://www.fizyka.umk.pl/~duch/"},
                {"label": "🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu i kognitywistyka po polsku", "url": "https://ccpress.pl/"},
                {"label": "🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                {"label": "🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (MIT Press / PDF autora)", "url": "https://www.izhikevich.org/publications/dsn.pdf"},
                {"label": "🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Technical Report PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                {"label": "🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” & Larry Squire et al. — „Fundamental Neuroscience”", "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:20:00Z",
        },
        {
            "id": "mat-3",
            "trackId": "C",
            "branchTopic": "Elektronika analogowa i układy dynamiczne.",
            "subprojectId": "sub-2",
            "title": "GOLEM 15 — Projekt C: Maszyny analogowe i obliczenia fizyczne (w pierwszej kolejności po polsku: Horowitz & Hill, OpenAGH, ZPE, Forbot, Osowski + Neuromorphic Computing)",
            "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne.\n\n"
                "1. W pierwszej kolejności — Po polsku: Podręczniki akademickie z elektroniki analogowej (P. Horowitz, W. Hill — „Sztuka elektroniki”; e-podręczniki OpenAGH: "
                "wzmacniacze, oscylatory, filtry, sprzężenie zwrotne, układy dynamiczne), materiały dydaktyczne o przetwornikach A/C i C/A (ZPE, kursy Forbot), "
                "polska literatura o sieciach neuronowych (S. Osowski, R. Tadeusiewicz).\n"
                "2. Uzupełniająco — Po angielsku: Materiały techniczne dot. analog computing, badania dot. neuromorphic computing i analog neural networks, "
                "publikacje o fizycznych modelach neuronów oraz analogowych i hybrydowych procesorach."
            ),
            "url": "https://zpe.gov.pl/",
            "links": [
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz C/A: https://zpe.gov.pl/", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 OpenAGH — Polskie e-podręczniki akademickie: Elektronika i układy dynamiczne", "url": "https://open.agh.edu.pl/"},
                {"label": "🇵🇱 Forbot — Kursy elektroniki analogowej i cyfrowej po polsku", "url": "https://forbot.pl/"},
                {"label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering", "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"},
                {"label": "🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks", "url": "https://arxiv.org/list/cs.NE/recent"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:00:00Z",
        },
        {
            "id": "mat-4",
            "trackId": "D",
            "branchTopic": "Biologia syntetyczna i edycja genomu.",
            "subprojectId": None,
            "title": "GOLEM 15 — Projekt D: „Frankenstein” — biotechnologia i tworzenie organizmów (w pierwszej kolejności po polsku: Alberts, Brown, Bartel „Embriologia”, Komitet Bioetyki PAN, Lem „Summa technologiae”)",
            "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka.\n\n"
                "1. W pierwszej kolejności — Po polsku: Podręczniki akademickie z biologii komórki, genetyki i biologii rozwoju (B. Alberts „Podstawy biologii komórki” PWN, "
                "T.A. Brown „Genomy” PWN, P. Węgleński „Genetyka molekularna” PWN); podręczniki z embriologii i komórek macierzystych (H. Bartel „Embriologia” PZWL); "
                "literatura o inżynierii tkankowej, medycynie regeneracyjnej i bioetyce (Komitet Bioetyki PAN, K. Szewczyk „Bioetyka” PWN) oraz Stanisław Lem — „Summa technologiae”.\n"
                "2. Uzupełniająco — Po angielsku: National Academies — materiały o odpowiedzialnym rozwoju biologii syntetycznej; publikacje akademickie o stem cells, "
                "developmental biology, tissue engineering i synthetic biology."
            ),
            "url": "https://bioetyka.pan.pl/",
            "links": [
                {"label": "🇵🇱 Komitet Bioetyki PAN — Stanowiska i opracowania bioetyczne po polsku", "url": "https://bioetyka.pan.pl/"},
                {"label": "🇵🇱 PZWL Wydawnictwo Lekarskie — H. Bartel „Embriologia”, komórki macierzyste i medycyna regeneracyjna", "url": "https://pzwl.pl/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Alberts „Podstawy biologii komórki”, Brown „Genomy”, Węgleński „Genetyka molekularna”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biologia i biotechnologia po polsku", "url": "https://zpe.gov.pl/"},
                {"label": "🇬🇧 National Academies — Biologia syntetyczna: https://www.nationalacademies.org/", "url": "https://www.nationalacademies.org/"},
                {"label": "🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell & Developmental Biology", "url": "https://www.ncbi.nlm.nih.gov/books/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:05:00Z",
        },
        {
            "id": "mat-5",
            "trackId": "E",
            "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "subprojectId": None,
            "title": "GOLEM 15 — Projekt E: Filozofia nauki, umysłu, techniki i bioetyka (w pierwszej kolejności po polsku: Chalmers, Kuhn, Heller, Tatarkiewicz, Wolne Lektury)",
            "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "Zastosowanie: Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.\n\n"
                "1. W pierwszej kolejności — Po polsku:\n"
                "  • Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n"
                "  • Thomas S. Kuhn — „Struktura rewolucji naukowych”\n"
                "  • Michał Heller — „Filozofia nauki. Wprowadzenie” oraz „Filozofia przyrody” (Copernicus Center Press)\n"
                "  • Władysław Tatarkiewicz — „Historia filozofii. Tom 1–3” (PWN) oraz klasyka filozofii starożytnej po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka) w serwisie Wolne Lektury\n"
                "  • Marcin Miłkowski, Robert Poczobut (red.) — „Przewodnik po filozofii umysłu” oraz Kazimierz Szewczyk — „Bioetyka. Tom 1–2” (PWN).\n"
                "2. Uzupełniająco — Po angielsku: Stanford Encyclopedia of Philosophy (SEP) oraz Internet Encyclopedia of Philosophy (IEP)."
            ),
            "url": "https://ccpress.pl/",
            "links": [
                {"label": "🇵🇱 Copernicus Center Press — Michał Heller „Filozofia nauki. Wprowadzenie”", "url": "https://ccpress.pl/"},
                {"label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Wykłady z filozofii nauki i umysłu po polsku", "url": "https://www.copernicuscenter.edu.pl/"},
                {"label": "🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, stoicy)", "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Kuhn, Tatarkiewicz, Szewczyk („Bioetyka”)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Stanford Encyclopedia of Philosophy (SEP — Nauka, Umysł, Technika, Bioetyka)", "url": "https://plato.stanford.edu/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:10:00Z",
        },
        {
            "id": "mat-6",
            "trackId": "F",
            "branchTopic": "Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.",
            "subprojectId": "sub-3",
            "title": "GOLEM 15 — Projekt F: Człowiek w kosmosie (w pierwszej kolejności po polsku: POLSA, ESERO Polska, OpenStax Fizyka PL, medycyna kosmiczna + darmowe źródła NASA i ESA)",
            "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.\n\n"
                "1. W pierwszej kolejności — Po polsku: Materiały edukacyjne i badawcze Polskiej Agencji Kosmicznej (POLSA) oraz ESERO Polska (Centrum Nauki Kopernik / ESA) "
                "dot. załogowych misji kosmicznych, życia w mikrograwitacji, ochrony przed promieniowaniem i projektowania habitatów; "
                "OpenStax Polska — „Fizyka dla szkół wyższych” (mechanika i grawitacja po polsku); K. Kwarecki (red.) — „Medycyna lotnicza i kosmiczna” (PZWL).\n"
                "2. Darmowe źródła międzynarodowe: NASA (zdrowie człowieka w kosmosie), ESA (edukacja kosmiczna — Teach with Space), ESA (eksploracja załogowa i robotyczna)."
            ),
            "url": "https://esero.kopernik.org.pl/",
            "links": [
                {"label": "🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o eksploracji kosmosu i habitatach", "url": "https://esero.kopernik.org.pl/"},
                {"label": "🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja, nauka i medycyna kosmiczna po polsku", "url": "https://polsa.gov.pl/"},
                {"label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (Mechanika i grawitacja po polsku)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                {"label": "🚀 NASA — Zdrowie człowieka w kosmosie: https://www.nasa.gov/reference/fundamentals-of-human-health/", "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"},
                {"label": "🛰️ ESA — Edukacja kosmiczna: https://education.esa.int/teach-with-space/", "url": "https://education.esa.int/teach-with-space/"},
                {"label": "👩‍🚀 ESA — Eksploracja załogowa: https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:15:00Z",
        },
        {
            "id": "mat-7",
            "trackId": "G",
            "branchTopic": "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.",
            "subprojectId": "sub-3",
            "title": "GOLEM 15 — Projekt G: Człowiek na Ziemi i ochrona ekosystemu (w pierwszej kolejności po polsku: Krystek, Weiner „Życie i ewolucja biosfery”, Politechnika Śląska, GIOŚ, EEA PL + ESA Education)",
            "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa.\n\n"
                "1. W pierwszej kolejności — Po polsku: Jan Krystek — „Ochrona środowiska dla inżynierów” (PWN); "
                "January Weiner — „Życie i ewolucja biosfery. Podręcznik ekologii ogólnej” (PWN); Czesława Rosik-Dulewska — „Podstawy gospodarki odpadami” (PWN); "
                "bezpłatne materiały Politechniki Śląskiej i OpenAGH dot. ochrony wód, powietrza i gleby; raporty GIOŚ (Państwowy Monitoring Środowiska) oraz serwis Europejskiej Agencji Środowiska po polsku (EEA PL).\n"
                "2. Uzupełniająco: ESA Education (Ziemia, klimat, obserwacja środowiska) oraz raporty IPCC i IPBES."
            ),
            "url": "https://www.polsl.pl/",
            "links": [
                {"label": "🇵🇱 Politechnika Śląska — Podstawy ochrony środowiska po polsku: https://www.polsl.pl/", "url": "https://www.polsl.pl/"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz January Weiner „Życie i ewolucja biosfery”", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 GIOŚ — Państwowy Monitoring Środowiska w Polsce (wody, powietrze, gleby)", "url": "https://www.gios.gov.pl/"},
                {"label": "🇵🇱 Europejska Agencja Środowiska (EEA w języku polskim)", "url": "https://www.eea.europa.eu/pl"},
                {"label": "🌍 ESA Education — Ziemia, klimat i obserwacja środowiska: https://education.esa.int/teach-with-space/", "url": "https://education.esa.int/teach-with-space/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:20:00Z",
        },
        {
            "id": "mat-1",
            "trackId": "E",
            "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "subprojectId": None,
            "title": "Granice modeli formalnych a interpretacja stanów umysłowych i biologicznych (Heller, Miłkowski & Poczobut, SEP)",
            "type": "Artykuł / Notatka przekrojowa",
            "author": "Administrator",
            "content": "Rozróżnienie między symulacją składniową (syntaktyczną) a realizacją właściwości przyczynowych układu fizycznego — punkt styku Projektu B, C oraz E. W pierwszej kolejności opracowania polskojęzyczne (Centrum Kopernika, M. Heller, M. Miłkowski & R. Poczobut).",
            "url": "https://ccpress.pl/",
            "links": [
                {"label": "🇵🇱 Centrum Kopernika / CCPress — Filozofia nauki i granice modeli matematycznych", "url": "https://ccpress.pl/"},
                {"label": "🇬🇧 Stanford Encyclopedia of Philosophy — Models in Science", "url": "https://plato.stanford.edu/entries/models-science/"},
                {"label": "🇬🇧 SEP — The Chinese Room Argument & Syntax vs Semantics", "url": "https://plato.stanford.edu/entries/chinese-room/"}
            ],
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
            "url": "https://ksiegarnia.pwn.pl/",
            "links": [
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Neurobiologia i metody neuroobrazowania (Kalat, Longstaff)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Physiological Reviews — Brain-Machine Interfaces (Lebedev & Nicolelis)", "url": "https://doi.org/10.1152/physrev.00027.2016"}
            ],
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
    "verifiedResearchers": [
        {
            "id": "res-founder",
            "name": "Ireneusz",
            "handle": "@ireneusz-architekt",
            "roleTitle": "Inicjator i Główny Architekt Projektu The Golem 15",
            "specialization": "ALL",
            "specializationLabel": "Wszystkie ścieżki (A–G) i Wspólne Podstawy (1–8)",
            "affiliation": "The Golem 15: A Human's Road to Reality",
            "orcid": "",
            "bio": "Twórca architektury badawczej The Golem 15 łączącej 8 fundamentów naukowych z 7 ścieżkami (A–G).",
            "aiVerificationScore": 100,
            "aiVerificationSummary": "Założyciel projektu — pełny rygor metodologiczny i epistemiczny.",
            "badge": "★ Założyciel & Kurator",
            "status": "active",
            "joinedAt": "2026-10-25T10:00:00Z",
            "auth": {
                "algorithm": "pbkdf2_sha256",
                "iterations": 260000,
                "salt": "9f4d8a2c6e1b3f7a5c8d0e2f4a6b8c1d",
                "hash": "673a07dbc15ac855752d7c521ffc31e200302b03a3b296310b742421cbfd4d62",
            },
        },
        {
            "id": "res-neuro-b",
            "name": "Dr hab. Marek Nowak (Zespół Neuroinformatyki)",
            "handle": "@m-nowak-neuro",
            "roleTitle": "Stały Badacz — Neurobiologia Obliczeniowa i Układy Neuromorficzne",
            "specialization": "B",
            "specializationLabel": "Projekt B — Cyfrowy Umysł / Projekt C — Maszyny analogowe",
            "affiliation": "Zespół Modelowania Układów Nerwowych",
            "orcid": "https://orcid.org/",
            "bio": "Badania nad modelami biofizycznymi Hodgkina–Huxleya, dynamiką populacji neuronalnych (Dayan & Abbott, Izhikevich) i estymacją pasma synaptycznego.",
            "aiVerificationScore": 95,
            "aiVerificationSummary": "Zweryfikowano przez AI: wysoki rygor matematyczno-biofizyczny, poprawna separacja modeli empirycznych od hipotez WBE.",
            "badge": "✓ Stały Badacz (AI 95/100)",
            "status": "active",
            "joinedAt": "2026-10-25T12:00:00Z",
            "auth": {
                "algorithm": "pbkdf2_sha256",
                "iterations": 260000,
                "salt": "9f4d8a2c6e1b3f7a5c8d0e2f4a6b8c1d",
                "hash": "673a07dbc15ac855752d7c521ffc31e200302b03a3b296310b742421cbfd4d62",
            },
        },
        {
            "id": "res-bio-dfg",
            "name": "Dr Anna Wiśniewska (Zespół Biotechnologii i Biosfery)",
            "handle": "@a-wisniewska-bio",
            "roleTitle": "Stały Badacz — Inżynieria Tkankowa, BLSS i Ekologia Systemowa",
            "specialization": "D",
            "specializationLabel": "Projekt D — Biotechnologia / Oś Kosmos (F) ↔ Ziemia (G)",
            "affiliation": "Laboratorium Biologii Syntetycznej i Ekosystemów Zamkniętych",
            "orcid": "https://orcid.org/",
            "bio": "Analiza rusztowań 3D (scaffolds), hodowli organoidów oraz bilansu tlenowo-węglowego w zamkniętych obiegach podtrzymywania życia (MELiSSA / LCA).",
            "aiVerificationScore": 92,
            "aiVerificationSummary": "Zweryfikowano przez AI: pełna zgodność z bioetyką (Projekt E) i literaturą polsko- oraz anglojęzyczną.",
            "badge": "✓ Stały Badacz (AI 92/100)",
            "status": "active",
            "joinedAt": "2026-10-25T12:30:00Z",
            "auth": {
                "algorithm": "pbkdf2_sha256",
                "iterations": 260000,
                "salt": "9f4d8a2c6e1b3f7a5c8d0e2f4a6b8c1d",
                "hash": "673a07dbc15ac855752d7c521ffc31e200302b03a3b296310b742421cbfd4d62",
            },
        },
    ],
}

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_FILE = os.path.join(DATA_DIR, "database.json")
SEED_FILE = os.path.join(DATA_DIR, "seed.json")


def ensure_db_schema(data):
    """Upewnia się, że baza zawiera nową nazwę oraz sekcje foundationDisciplines, studyMaterials, supplementaryLibrary i materials."""
    data["projectMeta"]["title"] = "The Golem 15: A Human's Road to Reality"
    data["projectMeta"].pop("adminPassword", None)
    if "adminAuth" not in data["projectMeta"] or not isinstance(data["projectMeta"]["adminAuth"], dict):
        data["projectMeta"]["adminAuth"] = json.loads(json.dumps(DEFAULT_SEED["projectMeta"]["adminAuth"]))
    if "foundationDisciplines" not in data or not data["foundationDisciplines"]:
        data["foundationDisciplines"] = json.loads(json.dumps(DEFAULT_SEED["foundationDisciplines"]))
    seed_smat_by_id = {sm["id"]: sm for sm in DEFAULT_SEED["studyMaterials"]}
    data.setdefault("studyMaterials", [])
    existing_smat_ids = set()
    for idx, sm in enumerate(data["studyMaterials"]):
        existing_smat_ids.add(sm["id"])
        if sm["id"] in seed_smat_by_id:
            data["studyMaterials"][idx] = json.loads(json.dumps(seed_smat_by_id[sm["id"]]))
    for sm in DEFAULT_SEED["studyMaterials"]:
        if sm["id"] not in existing_smat_ids:
            data["studyMaterials"].append(json.loads(json.dumps(sm)))

    seed_mat_by_id = {m["id"]: m for m in DEFAULT_SEED["materials"]}
    data.setdefault("materials", [])
    existing_mat_ids = set()
    for idx, m in enumerate(data["materials"]):
        existing_mat_ids.add(m["id"])
        if m["id"] in seed_mat_by_id:
            data["materials"][idx] = json.loads(json.dumps(seed_mat_by_id[m["id"]]))
    for m in DEFAULT_SEED["materials"]:
        if m["id"] not in existing_mat_ids:
            data["materials"].append(json.loads(json.dumps(m)))

    data["supplementaryLibrary"] = json.loads(json.dumps(DEFAULT_SEED["supplementaryLibrary"]))
    if "verifiedResearchers" not in data or not isinstance(data["verifiedResearchers"], list):
        data["verifiedResearchers"] = json.loads(json.dumps(DEFAULT_SEED["verifiedResearchers"]))
    else:
        existing_res_ids = {r.get("id") for r in data["verifiedResearchers"]}
        for r_seed in DEFAULT_SEED["verifiedResearchers"]:
            if r_seed["id"] not in existing_res_ids:
                data["verifiedResearchers"].append(json.loads(json.dumps(r_seed)))
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
# INICJALIZACJA STANU SESJI, KRYPTOGRAFIA (PBKDF2-SHA256) I ASYSTENT AI BADACZY
# ==============================================================================
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "active_researcher" not in st.session_state:
    st.session_state.active_researcher = None
if "failed_admin_attempts" not in st.session_state:
    st.session_state.failed_admin_attempts = 0

db = load_db()
pending_count = count_pending(db)
tracks_by_id = {t["id"]: t for t in db["tracks"]}
foundations_by_id = {f["id"]: f for f in db["foundationDisciplines"]}


def compute_pbkdf2_hash(password: str, salt_hex: str, iterations: int = 260000) -> str:
    salt_bytes = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt_bytes, int(iterations))
    return dk.hex()


def create_admin_auth_record(new_password: str, iterations: int = 260000) -> dict:
    salt_hex = secrets.token_hex(16)
    hash_hex = compute_pbkdf2_hash(new_password, salt_hex, iterations)
    return {
        "algorithm": "pbkdf2_sha256",
        "iterations": iterations,
        "salt": salt_hex,
        "hash": hash_hex,
    }


def verify_admin_password(candidate_password: str, db_data: dict) -> bool:
    if not candidate_password:
        return False
    env_secret = os.environ.get("GOLEM_ADMIN_PASSWORD")
    if not env_secret:
        try:
            env_secret = st.secrets.get("GOLEM_ADMIN_PASSWORD")
        except Exception:
            env_secret = None
    if env_secret and hmac.compare_digest(candidate_password.encode("utf-8"), str(env_secret).encode("utf-8")):
        return True

    auth = db_data.get("projectMeta", {}).get("adminAuth") or DEFAULT_SEED["projectMeta"]["adminAuth"]
    salt_hex = auth.get("salt", "")
    expected_hash = auth.get("hash", "")
    iterations = int(auth.get("iterations", 260000))
    if not salt_hex or not expected_hash:
        return False
    try:
        candidate_hash = compute_pbkdf2_hash(candidate_password, salt_hex, iterations)
        return hmac.compare_digest(candidate_hash, expected_hash)
    except Exception:
        return False


def verify_researcher_password(candidate_password: str, researcher_record: dict) -> bool:
    if not candidate_password or not researcher_record or researcher_record.get("status") != "active":
        return False
    auth = researcher_record.get("auth", {})
    salt_hex = auth.get("salt", "")
    expected_hash = auth.get("hash", "")
    iterations = int(auth.get("iterations", 260000))
    if not salt_hex or not expected_hash:
        return False
    try:
        candidate_hash = compute_pbkdf2_hash(candidate_password, salt_hex, iterations)
        return hmac.compare_digest(candidate_hash, expected_hash)
    except Exception:
        return False


def can_auto_approve() -> bool:
    """Zwraca True, jeśli użytkownik to Administrator lub zalogowany na stałe Zweryfikowany Badacz."""
    return bool(st.session_state.is_admin or st.session_state.active_researcher)


def get_contributor_signature() -> str:
    if st.session_state.is_admin:
        return "Ireneusz (Administrator ★)"
    if st.session_state.active_researcher:
        r = st.session_state.active_researcher
        return f"{r['name']} (✓ Stały Badacz)"
    return "Gość / Obserwator"


DOMAIN_KEYWORDS = {
    "FND-1": ["macierz", "wektor", "pochodna", "całka", "prawdopodobieństwo", "statystyk", "logik", "algebr", "strang", "dowód", "równan"],
    "FND-2": ["algorytm", "złożoność", "architektur", "komputer", "petzold", "system", "sieć", "baza", "pamięć", "struktura danych"],
    "FND-3": ["python", "kod", "funkcj", "test", "symulacj", "numpy", "scipy", "repozytorium", "program", "matthes", "git"],
    "FND-4": ["fizyk", "mechanik", "termodynamik", "elektromagnet", "kwant", "griffiths", "nielsen", "energia", "pole", "fala"],
    "FND-5": ["elektronik", "układ", "czujnik", "wzmacniacz", "przetwornik", "adc", "dac", "mikrokontroler", "sygnał", "sprzężenie"],
    "FND-6": ["chemi", "wiązani", "reakcj", "organicz", "biochemi", "białk", "enzym", "openstax", "stężeni", "termochemi"],
    "FND-7": ["biologi", "komórk", "genom", "dna", "rna", "ewolucj", "fizjologi", "campbell", "brown", "tkank", "homeostaz"],
    "FND-8": ["uczenie maszynowe", "sieć neuronowa", "ai", "gradient", "model", "géron", "klasyfikacj", "transformer", "dane", "walidacj"],
    "A": ["bionicz", "protez", "interfejs", "bci", "eeg", "biomateriał", "kalat", "sterowani", "rehabilitacj", "implant", "aktuator"],
    "B": ["neuron", "synaps", "konektom", "izhikevich", "dayan", "kandel", "hodgkin", "emulacj", "wbe", "poznawcz", "pamięć"],
    "C": ["analog", "neuromorficz", "oscylator", "memrystor", "dynamik", "filtr", "fizyczn", "sprzężenie", "układ"],
    "D": ["komórki macierzyste", "tkank", "organoid", "crispr", "embriologi", "syntetyczn", "bioetyk", "regeneracj", "rusztowani"],
    "E": ["filozofi", "chalmers", "kuhn", "heller", "świadomoś", "etyk", "falsyfikacj", "paradygmat", "tożsamoś", "ontologi"],
    "F": ["mikrograwitacj", "kosmos", "promieniowani", "orbital", "habitat", "blss", "melissa", "nasa", "esa", "podtrzymywania życia"],
    "G": ["ekologi", "ekosystem", "bioróżnorodnoś", "klimat", "lca", "obieg", "gleb", "krystek", "renaturyzacj", "energia"],
}


def evaluate_researcher_application_ai(
    name: str,
    spec_code: str,
    sample_text: str,
    citation_text: str,
    q1_epistemic: str,
    q2_methodology: str,
) -> dict:
    """
    Delikatny Asystent Weryfikacji Badacza AI:
    Ocenia kalibrację epistemiczną (Zasada 5 Golema 15), spójność metodologiczną próbki badawczej
    oraz ugruntowanie w literaturze, zwracając wynik 0–100 pkt i konstruktywne wskazówki.
    """
    score = 0
    feedback = []

    # 1. Kalibracja epistemiczna (0-40 pkt)
    if q1_epistemic.startswith("Hipoteza / długoterminowy cel"):
        score += 20
        feedback.append("🟢 **Kalibracja epistemiczna (Zasada 5):** Poprawnie odróżniono wiedzę potwierdzoną od długoterminowych celów badawczych (WBE).")
    else:
        score += 5
        feedback.append("🟡 **Wskazówka epistemiczna AI:** W projekcie The Golem 15 pełna emulacja mózgu (WBE) jest traktowana jako mapa drogowa i hipoteza badawcza, a nie wiedza już potwierdzona.")

    if q2_methodology.startswith("Od podręczników podstawowych"):
        score += 20
        feedback.append("🟢 **Rygor źródłowy (Zasady 1–4):** Właściwa hierarchia źródeł (podręczniki akademickie, otwarte zasoby badawcze i recenzowane przeglądy).")
    else:
        score += 5
        feedback.append("🟡 **Wskazówka metodologiczna AI:** Zgodnie z zasadami biblioteki Golem 15 pracę zaczynamy od bezpłatnych podręczników podstawowych i weryfikowalnych przeglądów.")

    # 2. Analiza semantyczna próbki badawczej (0-35 pkt)
    clean_sample = (sample_text or "").strip()
    text_lower = f"{clean_sample} {citation_text or ''}".lower()
    if len(clean_sample) >= 140:
        score += 18
        feedback.append("🟢 **Struktura wypowiedzi badawczej:** Próbka ma odpowiednią szczegółowość merytoryczną.")
    elif len(clean_sample) >= 70:
        score += 12
        feedback.append("🔵 **Struktura wypowiedzi:** Opis jest zwięzły — dodanie 1–2 zdań o metodzie pomiarowej lub modelu zwiększy precyzję.")
    else:
        score += 4
        feedback.append("🟡 **Delikatna podpowiedź AI:** Rozwiń próbkę badawczą do min. 2–3 zdań opisujących problem, metodę lub model.")

    domain_terms = DOMAIN_KEYWORDS.get(spec_code, []) + [
        "model", "analiza", "pomiar", "hipotez", "eksperyment", " równani", "system", "badani", "dane", "mechanizm", "weryfikacj"
    ]
    matched_terms = [kw.strip() for kw in domain_terms if kw in text_lower]
    if len(matched_terms) >= 3:
        score += 17
        feedback.append(f"🟢 **Spójność terminologiczna ze ścieżką ({spec_code}):** Wykryto pojęcia dziedzinowe ({', '.join(matched_terms[:5])}).")
    elif len(matched_terms) >= 1:
        score += 11
        feedback.append(f"🔵 **Terminologia dziedzinowa:** Wykryto odniesienia ({', '.join(matched_terms[:3])}).")
    else:
        score += 5
        feedback.append("🟡 **Podpowiedź AI:** Warto użyć w opisie konkretnych pojęć technicznych lub nazw modeli z wybranej dziedziny.")

    # 3. Weryfikacja ugruntowania bibliograficznego (0-25 pkt)
    clean_cit = (citation_text or "").strip()
    scholarly_markers = ["openstax", "pwn", "petzold", "matthes", "strang", "griffiths", "nielsen", "brown", "campbell", "kalat", "kandel", "dayan", "izhikevich", "chalmers", "kuhn", "heller", "krystek", "nasa", "esa", "doi", "http", "wydawnictwo", "podręcznik", "nature", "science", "ieee", "arxiv"]
    has_marker = any(m in text_lower for m in scholarly_markers)
    if len(clean_cit) >= 15 and has_marker:
        score += 25
        feedback.append("🟢 **Ugruntowanie w literaturze:** Przywołano weryfikowalne źródło naukowe / podręcznik z kanonu projektu.")
    elif len(clean_cit) >= 10:
        score += 16
        feedback.append("🔵 **Źródło bibliograficzne:** Podano źródło — warto dodać autora, wydawnictwo (np. PWN, OpenStax) lub link DOI/URL.")
    else:
        score += 4
        feedback.append("🟡 **Delikatna podpowiedź AI:** Dopisz przynajmniej jedno źródło literaturowe (np. Kalat, Petzold, Kandel, OpenStax, Chalmers, NASA/ESA lub link DOI).")

    score = min(100, max(0, score))
    passed = score >= 75
    summary = (
        f"Pozytywna weryfikacja metodologiczna AI ({score}/100 pkt) w obszarze {spec_code}."
        if passed
        else f"Wynik wstępny {score}/100 pkt (próg automatycznej autoryzacji: 75/100 pkt) — skorzystaj z podpowiedzi AI powyżej."
    )
    return {
        "score": score,
        "passed": passed,
        "summary": summary,
        "feedback": feedback,
    }


def ai_suggest_material_metadata(title: str, content: str, target_code: str) -> dict:
    """Delikatny Asystent AI podpowiadający klasyfikację epistemiczną i powiązane lektury polskojęzyczne."""
    txt = f"{title} {content}".lower()
    if any(w in txt for w in ["spekulac", "przeniesienie umysłu", "świadomość maszynowa", "hipotetycz", "dalekosiężn"]):
        epistemic = "🟣 Spekulacja / Eksperyment myślowy"
    elif any(w in txt for w in ["hipotez", "propozycj", "weryfikacj", "wbe", "roadmap"]):
        epistemic = "🟡 Hipoteza badawcza"
    elif any(w in txt for w in ["przegląd", "bci", "organoid", "neuromorficz", "melissa", "crispr", "doi.org"]):
        epistemic = "🔵 Aktywne badania"
    else:
        epistemic = "🟢 Wiedza potwierdzona"

    pl_recommendations = {
        "FND-1": "🇵🇱 Podręczniki algebry liniowej i analizy matematycznej (PWN / ZPE) + G. Strang",
        "FND-2": "🇵🇱 Charles Petzold — Kod. Ukryty język komputerów (Wyd. II)",
        "FND-3": "🇵🇱 Eric Matthes — Python. Instrukcje dla programisty",
        "FND-4": "🇵🇱 Fizyka dla szkół wyższych (OpenStax Polska) + D. J. Griffiths",
        "FND-5": "🇵🇱 Podstawy elektroniki i układów cyfrowych (ZPE / PWN)",
        "FND-6": "🇵🇱 Akademickie podręczniki chemii ogólnej i biochemii (PWN) + OpenStax Chemistry 2e",
        "FND-7": "🇵🇱 Biologia Campbella oraz Terence A. Brown — Genomy (PWN)",
        "FND-8": "🇵🇱 Aurélien Géron — Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow (Helion)",
        "A": "🇵🇱 James W. Kalat — Biologiczne podstawy psychologii (PWN) + podręczniki biofizyki i robotyki",
        "B": "🇵🇱 James W. Kalat — Biologiczne podstawy psychologii (PWN) + Dayan & Abbott / Izhikevich",
        "C": "🇵🇱 Podręczniki elektroniki analogowej i układów dynamicznych (ZPE / PWN)",
        "D": "🇵🇱 Terence A. Brown — Genomy + Biologia Campbella + literatura z inżynierii tkankowej",
        "E": "🇵🇱 Alan Chalmers — Czym jest to, co zwiemy nauką?, T. S. Kuhn, Michał Heller — Filozofia nauki",
        "F": "🇵🇱 Materiały fizjologii i techniki kosmicznej + NASA Human Health / ESA Teach with Space",
        "G": "🇵🇱 Jan Krystek — Ochrona środowiska dla inżynierów (PWN) + materiały Politechniki Śląskiej",
    }
    return {
        "epistemicStatus": epistemic,
        "recommendedLiterature": pl_recommendations.get(target_code, "🇵🇱 Biblioteka Projektu The Golem 15 (Sekcje I–VI)"),
    }


# ==============================================================================
# PASEK BOCZNY: ROLA UŻYTKOWNIKA (GOŚĆ vs STAŁY BADACZ vs ADMINISTRATOR)
# ==============================================================================
with st.sidebar:
    st.markdown("## 🧬 The Golem 15")
    st.caption("A Human's Road to Reality — Architektura Orientacyjna & Badawcza")
    st.divider()

    active_researchers_list = [r for r in db.get("verifiedResearchers", []) if r.get("status") == "active"]

    if st.session_state.is_admin:
        st.success("★ **Tryb Właściciela / Administratora**\nPełne uprawnienia do moderacji, zarządzania stałymi badaczami i publikacji natychmiastowej.")
        if st.button("🔓 Wyloguj do trybu Gościa", use_container_width=True):
            st.session_state.is_admin = False
            st.rerun()
    elif st.session_state.active_researcher:
        cur_r = st.session_state.active_researcher
        st.success(
            f"🧑‍🔬 **Stały Zweryfikowany Badacz**\n"
            f"**{cur_r['name']}**\n"
            f"*{cur_r.get('roleTitle', '')}*\n\n"
            f"✓ Twoje materiały, podprojekty i notatki są **publikowane od razu bez kolejki moderacji**."
        )
        if st.button("🔓 Wyloguj z konta Badacza", use_container_width=True):
            st.session_state.active_researcher = None
            st.rerun()
    else:
        st.info(
            "👁 **Tryb Gościa / Obserwatora**\n"
            "Zgłoszenia gości trafiają do kolejki. **Zaloguj się jako Stały Badacz** lub przejdź **2-minutową weryfikację AI** w zakładce 7, aby publikować na stałe bez kolejki!"
        )
        with st.expander("🧑‍🔬 Logowanie Stałego Badacza", expanded=False):
            if active_researchers_list:
                sel_res_id = st.selectbox(
                    "Wybierz profil Badacza",
                    options=[r["id"] for r in active_researchers_list],
                    format_func=lambda rid: next((f"{r['name']} ({r.get('specialization', 'ALL')})" for r in active_researchers_list if r["id"] == rid), rid),
                    key="side_res_select",
                )
                res_pass = st.text_input("Hasło Badacza", type="password", value="", key="side_res_pass")
                if st.button("🧑‍🔬 Zaloguj jako Stały Badacz", type="primary", use_container_width=True, key="btn_res_login"):
                    target_r = next((r for r in active_researchers_list if r["id"] == sel_res_id), None)
                    if verify_researcher_password(res_pass, target_r):
                        st.session_state.active_researcher = target_r
                        st.rerun()
                    else:
                        time.sleep(0.5)
                        st.error("Nieprawidłowe hasło Badacza.")
                st.caption("Nowy badacz? Przejdź do zakładki **🧑‍🔬 7. Badacze i Weryfikacja AI**, aby utworzyć stałe konto.")

    st.divider()
    st.markdown("### 📊 Kompas Projektu")
    col_s1, col_s2 = st.columns(2)
    col_s1.metric("Dziedziny (1–8)", len(db["foundationDisciplines"]))
    col_s2.metric("Ścieżki (A–G)", len(db["tracks"]))
    col_s3, col_s4 = st.columns(2)
    col_s3.metric("Materiały i książki", len(db.get("studyMaterials", [])) + len(db.get("materials", [])))
    col_s4.metric("Stali Badacze", len(active_researchers_list))
    st.metric("⏳ Kolejka gości", pending_count)

    st.divider()
    st.download_button(
        "⬇ Pobierz kopię bazy JSON",
        data=json.dumps(db, ensure_ascii=False, indent=2),
        file_name="the_golem_15_database.json",
        mime="application/json",
        use_container_width=True,
    )

    if not st.session_state.is_admin:
        st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
        with st.expander("🔒 Autoryzacja właściciela", expanded=False):
            admin_pass_side = st.text_input(
                "Klucz dostępu",
                type="password",
                value="",
                placeholder="Wprowadź hasło właściciela",
                key="sidebar_admin_pass",
            )
            if st.button("Odblokuj", use_container_width=True, key="btn_side_login"):
                if st.session_state.failed_admin_attempts >= 5:
                    time.sleep(2.0)
                if verify_admin_password(admin_pass_side, db):
                    st.session_state.is_admin = True
                    st.session_state.failed_admin_attempts = 0
                    st.rerun()
                else:
                    st.session_state.failed_admin_attempts += 1
                    time.sleep(0.6)
                    st.error("Brak autoryzacji — nieprawidłowy klucz dostępu.")

# ==============================================================================
# ARCHITEKTURA ORIENTACYJNA UI (WZOROWANA NA MOST WIEDZY, OSF, RESEARCHHUB I HEPTABASE)
# ==============================================================================
st.markdown(
    """
    <style>
    .golem-wayfinding-shell {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.96) 0%, rgba(30, 41, 59, 0.92) 100%);
        border: 1px solid rgba(56, 189, 248, 0.28);
        border-radius: 14px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 1rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.35);
    }
    .golem-wayfinding-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 0.85rem;
        margin-top: 0.8rem;
    }
    .golem-axis-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 10px;
        padding: 0.75rem 0.9rem;
    }
    .golem-axis-title {
        font-size: 0.74rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #38bdf8;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }
    .golem-pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.32rem;
    }
    .golem-pill {
        display: inline-block;
        padding: 0.18rem 0.55rem;
        border-radius: 999px;
        font-size: 0.74rem;
        font-weight: 600;
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.3);
        color: #e2e8f0;
    }
    .golem-epistemic-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 0.45rem;
        margin-top: 0.65rem;
        padding-top: 0.6rem;
        border-top: 1px dashed rgba(148, 163, 184, 0.2);
        font-size: 0.76rem;
        color: #cbd5e1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.session_state.is_admin or st.session_state.active_researcher:
    col_title, col_top_auth = st.columns([3, 1])
    with col_title:
        st.title("🧬 The Golem 15: A Human's Road to Reality")
        st.markdown(f"**Cel nadrzędny:** {db['projectMeta']['overarchingGoal']}")
    with col_top_auth:
        if st.session_state.is_admin:
            st.success("★ Administrator (Pełna kontrola)")
            if st.button("Wyloguj Administratora", key="top_logout_btn", use_container_width=True):
                st.session_state.is_admin = False
                st.rerun()
        elif st.session_state.active_researcher:
            st.success(f"🧑‍🔬 Stały Badacz: {st.session_state.active_researcher['name']}")
            if st.button("Wyloguj Badacza", key="top_res_logout_btn", use_container_width=True):
                st.session_state.active_researcher = None
                st.rerun()
else:
    st.title("🧬 The Golem 15: A Human's Road to Reality")
    st.markdown(f"**Cel nadrzędny:** {db['projectMeta']['overarchingGoal']}")

st.markdown(
    f"""
    <div class="golem-wayfinding-shell">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
            <div>
                <span style="font-size:0.76rem; text-transform:uppercase; letter-spacing:0.08em; color:#38bdf8; font-weight:700;">
                    🧭 Architektura Orientacyjna Projektu (Standard OSF / ResearchHub / Most Wiedzy / Heptabase)
                </span>
                <div style="font-size:0.84rem; color:#cbd5e1; margin-top:0.15rem;">
                    {db['projectMeta']['organizationalRule']}
                </div>
            </div>
        </div>
        <div class="golem-wayfinding-grid">
            <div class="golem-axis-card">
                <div class="golem-axis-title">🏛️ Oś I: Wspólne Podstawy (8 Dziedzin po kolei)</div>
                <div class="golem-pill-row">
                    <span class="golem-pill">1. Matematyka</span>
                    <span class="golem-pill">2. Informatyka</span>
                    <span class="golem-pill">3. Programowanie</span>
                    <span class="golem-pill">4. Fizyka</span>
                    <span class="golem-pill">5. Elektronika</span>
                    <span class="golem-pill">6. Chemia</span>
                    <span class="golem-pill">7. Biologia</span>
                    <span class="golem-pill">8. AI</span>
                </div>
            </div>
            <div class="golem-axis-card">
                <div class="golem-axis-title">🗺️ Oś II: 7 Ścieżek Badawczych (Projekty A–G)</div>
                <div class="golem-pill-row">
                    <span class="golem-pill">A: Bio-Cyfrowy</span>
                    <span class="golem-pill">B: Cyfrowy Umysł</span>
                    <span class="golem-pill">C: Analog / Neuromorf</span>
                    <span class="golem-pill">D: Biotechnologia</span>
                    <span class="golem-pill">E: Filozofia (Przekrojowa)</span>
                    <span class="golem-pill">F: Kosmos (BLSS)</span>
                    <span class="golem-pill">G: Ziemia (Ekosystem)</span>
                </div>
            </div>
            <div class="golem-axis-card">
                <div class="golem-axis-title">🧑‍🔬 Oś III: Autoryzacja Epistemiczna i Zespół</div>
                <div style="font-size:0.8rem; color:#e2e8f0; line-height:1.45;">
                    • <strong>Stali Badacze ({len(active_researchers_list)})</strong>: publikacja natychmiastowa po weryfikacji AI<br/>
                    • <strong>Priorytet źródeł</strong>: 🇵🇱 literatura polska → 🇬🇧 światowa
                </div>
            </div>
        </div>
        <div class="golem-epistemic-bar">
            <strong>Statusy Epistemiczne (Zasada 5):</strong>
            <span>🟢 Wiedza potwierdzona (podręczniki)</span> •
            <span>🔵 Aktywne badania (przeglądy / eksperymenty)</span> •
            <span>🟡 Hipoteza badawcza (modele)</span> •
            <span>🟣 Spekulacja / cel długoterminowy (np. pełne WBE)</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("🔍 Globalny Nawigator & Wyszukiwarka Fasetowa (Przeszukaj jednocześnie 8 dziedzin, 7 ścieżek, Bibliotekę i Badaczy)", expanded=False):
    g_col1, g_col2 = st.columns([3, 1])
    with g_col1:
        global_query = st.text_input(
            "Wpisz pojęcie, autora, technologię lub temat (np. Petzold, Kalat, Kandel, CRISPR, neuromorficzne, OpenStax, MELiSSA):",
            key="global_wayfinding_search",
        )
    with g_col2:
        global_scope = st.selectbox(
            "Zakres fasetowy:",
            ["Cały projekt (Wszystkie warstwy)", "Tylko polskojęzyczne (🇵🇱)", "Podstawy (1–8)", "Ścieżki (A–G)", "Stali Badacze"],
            key="global_wayfinding_scope",
        )
    if global_query.strip():
        q_low = global_query.strip().lower()
        hits = []
        if global_scope in ("Cały projekt (Wszystkie warstwy)", "Podstawy (1–8)"):
            for fnd in db["foundationDisciplines"]:
                blob = f"{fnd['name']} {fnd['description']} {' '.join(fnd['topics'])}".lower()
                if q_low in blob:
                    hits.append(f"🏛️ **Podstawy {fnd['order']}: {fnd['name']}** — {fnd['description']} *(Zakładka 1)*")
        if global_scope in ("Cały projekt (Wszystkie warstwy)", "Ścieżki (A–G)"):
            for tr in db["tracks"]:
                blob = f"{tr['code']} {tr['name']} {tr['goal']} {tr['guidingQuestion']}".lower()
                if q_low in blob:
                    hits.append(f"🗺️ **{tr['code']} — {tr['name']}** — {tr['goal']} *(Zakładka 2)*")
        for sm in db.get("studyMaterials", []):
            if sm.get("status") != "approved" and not can_auto_approve():
                continue
            blob = f"{sm.get('title','')} {sm.get('content','')} {sm.get('topic','')}".lower()
            if global_scope == "Tylko polskojęzyczne (🇵🇱)" and "🇵🇱" not in f"{sm.get('title','')} {sm.get('content','')} {json.dumps(sm.get('links',[]), ensure_ascii=False)}":
                continue
            if q_low in blob:
                hits.append(f"🎓 **Materiał do nauki [{sm.get('targetId')}]: {sm['title']}** — {sm['content'][:160]}... *(Zakładka 1)*")
        for m in db.get("materials", []):
            if m.get("status") != "approved" and not can_auto_approve():
                continue
            blob = f"{m.get('title','')} {m.get('content','')} {m.get('branchTopic','')}".lower()
            if global_scope == "Tylko polskojęzyczne (🇵🇱)" and "🇵🇱" not in f"{m.get('title','')} {m.get('content','')} {json.dumps(m.get('links',[]), ensure_ascii=False)}":
                continue
            if q_low in blob:
                hits.append(f"📚 **Repozytorium [Projekt {m.get('trackId')}]: {m['title']}** — {m['content'][:160]}... *(Zakładka 4)*")
        if global_scope in ("Cały projekt (Wszystkie warstwy)", "Stali Badacze"):
            for r in active_researchers_list:
                blob = f"{r['name']} {r.get('roleTitle','')} {r.get('bio','')} {r.get('specializationLabel','')}".lower()
                if q_low in blob:
                    hits.append(f"🧑‍🔬 **Stały Badacz: {r['name']}** ({r.get('roleTitle')}) — {r.get('bio')} *(Zakładka 7)*")
        if hits:
            st.success(f"Znaleziono {len(hits)} dopasowań w architekturze projektu:")
            for h_item in hits[:15]:
                st.markdown(f"- {h_item}")
        else:
            st.warning("Brak bezpośrednich dopasowań — spróbuj wpisać inne słowo kluczowe lub nazwisko autora.")


# ==============================================================================
# ZAKŁADKI GŁÓWNE APLIKACJI (OPCJA 1: MATERIAŁY DO NAUKI)
# ==============================================================================
tab_study, tab_map, tab_ws, tab_mat, tab_new, tab_graph, tab_researchers, tab_admin = st.tabs([
    "🎓 1. Materiały do nauki (Dziedziny i Biblioteka)",
    "🗺️ 2. Mapa 7 Ścieżek (Projekty A–G)",
    f"🔬 3. Środowiska Badawcze ({len(db['subprojects'])})",
    f"📚 4. Repozytorium Badawcze ({len(db['materials'])})",
    "🚀 5. + Uruchom Środowisko / Dodaj Materiał",
    "🕸️ 6. Graf Powiązań (A–G)",
    f"🧑‍🔬 7. Badacze i Weryfikacja AI ({len(active_researchers_list)})",
    f"🛡️ 8. Autoryzacja Administratora ({pending_count})",
])

# ------------------------------------------------------------------------------
# ZAKŁADKA 1 (PIERWSZA OPCJA): MATERIAŁY DO NAUKI — 8 DZIEDZIN + ŚCIEŻKI A-G + BIBLIOTEKA UZUPEŁNIAJĄCA (C-G)
# ------------------------------------------------------------------------------
with tab_study:
    st.subheader("🎓 Materiały do nauki — Wspólne podstawy (8 dziedzin), Ścieżki A–G oraz Biblioteka materiałów uzupełniających")
    st.markdown(
        "Drzewo kształcenia, bibliografia i materiały dydaktyczne dla **8 dziedzin fundamentalnych** "
        "(*Matematyka i logika, Informatyka, Programowanie, Fizyka, Elektronika, Chemia, Biologia, Sztuczna inteligencja*), "
        "odnóg **Projektów A–G** oraz **Biblioteki materiałów uzupełniających (Projekty C, D, E, F i G)**."
    )

    mode_study = st.radio(
        "Wybierz warstwę drzewa do nauki:",
        options=[
            "1️⃣ Wspólne podstawy naukowe — 8 dziedzin po kolei (Matematyka → AI)",
            "2️⃣ Odnogi tematyczne Ścieżek Badawczych (Projekty A–G po kolei)",
            "3️⃣ GOLEM 15 — Biblioteka materiałów uzupełniających (Projekty C, D, E, F, G + Zasady korzystania)",
        ],
        horizontal=True,
    )

    supp_lib = db.get("supplementaryLibrary", DEFAULT_SEED["supplementaryLibrary"])
    supp_by_track = {p["trackId"]: p for p in supp_lib.get("projects", [])}

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
                            if sm.get("links"):
                                st.markdown("**🔗 Odnośniki i linki źródłowe:**")
                                for lnk in sm["links"]:
                                    st.markdown(f"- [🔗 {lnk['label']}]({lnk['url']})")
                            elif sm.get("url"):
                                st.markdown(f"[🔗 Otwórz materiał / źródło]({sm['url']})")
                            st.caption(f"Dodał(a): {sm.get('author', 'Gość')}")

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
                            sm_author = st.text_input("Autor zgłoszenia", value=get_contributor_signature())
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
                                        "status": "approved" if can_auto_approve() else "pending",
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
                            w_auth = st.text_input("Autor", value=get_contributor_signature())
                            if st.form_submit_button("🚀 Uruchom środowisko"):
                                if w_title.strip() and w_desc.strip():
                                    approval = "approved" if can_auto_approve() else "pending"
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

    elif mode_study.startswith("2️⃣"):
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

                if tid in supp_by_track:
                    sp_proj = supp_by_track[tid]
                    st.info(f"**{sp_proj['sequenceLabel']}:** {sp_proj['sequence']}")

                for sec in track["sections"]:
                    st.markdown(f"**{sec['title']} — po kolei:**")
                    for b_idx, branch_item in enumerate(sec["items"], start=1):
                        branch_mats = [m for m in tr_study_mats if m.get("topic") == branch_item]
                        st.markdown(f"- **{b_idx}. {branch_item}** *(materiały do nauki: {len(branch_mats)})*")
                        for bm in branch_mats:
                            url_part = f" — [🔗 Główny link]({bm['url']})" if bm.get("url") else ""
                            st.markdown(
                                f"  - 📖 **{bm['title']}** ({bm.get('level')}, {bm.get('format')}) — {bm['content']}{url_part} "
                                f"*(dodał: {bm.get('author')})*"
                            )
                            for lnk in bm.get("links", []):
                                st.markdown(f"    - 🔗 [{lnk['label']}]({lnk['url']})")

                if tid in supp_by_track:
                    with st.expander(f"📚 Biblioteka materiałów uzupełniających i odnośników dla {track['code']}", expanded=True):
                        sp_proj = supp_by_track[tid]
                        cols_g = st.columns(len(sp_proj["groups"]))
                        for g_idx, grp in enumerate(sp_proj["groups"]):
                            with cols_g[g_idx]:
                                st.markdown(f"**{grp['heading']}:**")
                                for itm in grp["items"]:
                                    st.markdown(f"- {itm}")
                        if sp_proj.get("links"):
                            st.markdown("**🔗 Bezpośrednie odnośniki i linki źródłowe:**")
                            for lnk in sp_proj["links"]:
                                st.markdown(f"- [{lnk['label']}]({lnk['url']})")

                with st.popover(f"➕ Dodaj materiał do nauki dla odnogi {track['code']}", use_container_width=True):
                    with st.form(f"add_study_trk_{tid}"):
                        sm_topic = st.selectbox("Wybierz konkretną odnogę projektu", options=all_branches)
                        sm_title = st.text_input("Tytuł materiału do nauki*")
                        c_l, c_f = st.columns(2)
                        sm_level = c_l.selectbox("Poziom", ["Podstawowy", "Średniozaawansowany", "Zaawansowany / Badawczy"])
                        sm_format = c_f.selectbox("Format", ["Podręcznik / Książka", "Kurs / Wykład", "Artykuł przeglądowy", "Notatka do nauki", "Symulacja / Kod"])
                        sm_content = st.text_area("Opis zagadnienia / streszczenie materiału*")
                        sm_url = st.text_input("Link zewnętrzny / DOI (opcjonalnie)")
                        sm_author = st.text_input("Autor", value=get_contributor_signature())
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
                                    "status": "approved" if can_auto_approve() else "pending",
                                    "createdAt": datetime.utcnow().isoformat() + "Z",
                                })
                                save_db(db)
                                st.success("Zapisano materiał do nauki!")
                                st.rerun()

    else:
        st.markdown(f"### 📖 {supp_lib['title']}")
        st.markdown(f"*{supp_lib['description']}*")

        with st.container(border=True):
            st.markdown("#### 📜 Zasady korzystania z biblioteki")
            for r_idx, rule_txt in enumerate(supp_lib.get("rules", []), start=1):
                st.markdown(f"**{r_idx}.** {rule_txt}")

        reading_order = supp_lib.get("readingOrder")
        if reading_order:
            with st.container(border=True):
                st.markdown(f"### 🧭 {reading_order.get('title', 'VI. KOLEJNOŚĆ CZYTANIA')}")
                ro_cols = st.columns(len(reading_order.get("stages", [])))
                for s_idx, stage in enumerate(reading_order.get("stages", [])):
                    with ro_cols[s_idx]:
                        st.markdown(f"#### {stage['stage']}")
                        for b_item in stage.get("items", []):
                            st.markdown(f"- {b_item}")
                if reading_order.get("principle"):
                    st.info(f"**Zasada:** {reading_order['principle']}")

        for sp_proj in supp_lib.get("projects", []):
            tid = sp_proj["trackId"]
            cat_type = "FOUNDATION" if tid.startswith("FND-") else "TRACK"
            tr_study_mats = [
                sm for sm in db.get("studyMaterials", [])
                if sm.get("categoryType") == cat_type
                and sm.get("targetId") == tid
                and (sm.get("status") == "approved" or st.session_state.is_admin)
            ]
            if tid in foundations_by_id:
                all_branches = foundations_by_id[tid].get("topics", ["Ogólne"])
            else:
                all_branches = get_all_branches_for_track(db["tracks"], tid) or ["Ogólne"]

            with st.container(border=True):
                st.markdown(f"### {sp_proj['title']}")
                st.info(f"**{sp_proj['sequenceLabel']}:** {sp_proj['sequence']}")

                cols_grp = st.columns(len(sp_proj["groups"]))
                for g_idx, grp in enumerate(sp_proj["groups"]):
                    with cols_grp[g_idx]:
                        st.markdown(f"#### {grp['heading']}")
                        for item_txt in grp["items"]:
                            st.markdown(f"- {item_txt}")

                if sp_proj.get("links"):
                    st.markdown("#### 🔗 Bezpośrednie linki i odnośniki do źródeł")
                    for lnk in sp_proj["links"]:
                        st.markdown(f"- [{lnk['label']}]({lnk['url']})")

                if tr_study_mats:
                    st.markdown(f"**Przypisane karty materiałów do nauki ({len(tr_study_mats)}):**")
                    for bm in tr_study_mats:
                        url_part = f" — [🔗 Otwórz główne źródło]({bm['url']})" if bm.get("url") else ""
                        st.markdown(f"- 📖 **{bm['title']}** (*{bm.get('format')}*, poziom: *{bm.get('level')}*): {bm['content']}{url_part}")
                        for lnk in bm.get("links", []):
                            st.markdown(f"  - 🔗 [{lnk['label']}]({lnk['url']})")

                with st.popover(f"➕ Dodaj nową pozycję do biblioteki ({sp_proj['title']})", use_container_width=True):
                    with st.form(f"add_supp_lib_{tid}"):
                        sm_topic = st.selectbox("Dział / odnoga projektu", options=all_branches)
                        sm_title = st.text_input("Tytuł pozycji / źródła*")
                        c_l, c_f = st.columns(2)
                        sm_level = c_l.selectbox("Poziom", ["Podstawowy (Bezpłatny)", "Akademicki / Podręcznik", "Badawczy / Przegląd naukowy"])
                        sm_format = c_f.selectbox("Kategoria", ["Po polsku", "Po angielsku", "Darmowe źródło online", "Temat do dalszego studiowania"])
                        sm_content = st.text_area("Opis / zakres zastosowania*")
                        sm_url = st.text_input("Link URL (opcjonalnie)")
                        sm_author = st.text_input("Dodał(a)", value=get_contributor_signature())
                        if st.form_submit_button("📥 Dodaj do biblioteki"):
                            if sm_title.strip() and sm_content.strip():
                                db.setdefault("studyMaterials", []).insert(0, {
                                    "id": f"smat-{int(time.time()*1000)}",
                                    "categoryType": cat_type,
                                    "targetId": tid,
                                    "topic": sm_topic,
                                    "title": sm_title.strip(),
                                    "level": sm_level,
                                    "format": sm_format,
                                    "content": sm_content.strip(),
                                    "url": sm_url.strip(),
                                    "author": sm_author.strip() or "Gość",
                                    "status": "approved" if can_auto_approve() else "pending",
                                    "createdAt": datetime.utcnow().isoformat() + "Z",
                                })
                                save_db(db)
                                st.success("Dodano pozycję do biblioteki projektu!")
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
                        h_auth = st.text_input("Autor", value=get_contributor_signature())
                        if st.form_submit_button("Zapisz hipotezę"):
                            if h_stmt.strip():
                                ws.setdefault("hypotheses", []).append({
                                    "id": f"hyp-{int(time.time()*1000)}",
                                    "statement": h_stmt.strip(),
                                    "status": h_stat,
                                    "author": h_auth.strip() or "Gość",
                                    "approvalStatus": "approved" if can_auto_approve() else "pending",
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
                        n_auth = st.text_input("Autor", value=get_contributor_signature())
                        if st.form_submit_button("Zapisz notatkę"):
                            if n_title.strip() and n_content.strip():
                                ws.setdefault("notes", []).append({
                                    "id": f"note-{int(time.time()*1000)}",
                                    "title": n_title.strip(),
                                    "content": n_content.strip(),
                                    "author": n_auth.strip() or "Gość",
                                    "createdAt": datetime.utcnow().isoformat() + "Z",
                                    "approvalStatus": "approved" if can_auto_approve() else "pending",
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
                        b_auth = st.text_input("Dodał(a)", value=get_contributor_signature())
                        if st.form_submit_button("Dodaj źródło"):
                            if b_cit.strip():
                                ws.setdefault("bibliography", []).append({
                                    "id": f"bib-{int(time.time()*1000)}",
                                    "citation": b_cit.strip(),
                                    "url": b_url.strip(),
                                    "addedBy": b_auth.strip() or "Gość",
                                    "approvalStatus": "approved" if can_auto_approve() else "pending",
                                })
                                save_db(db)
                                st.rerun()

# ------------------------------------------------------------------------------
# ZAKŁADKA 4: REPOZYTORIUM MATERIAŁÓW BADAWCZYCH I UZUPEŁNIAJĄCYCH
# ------------------------------------------------------------------------------
with tab_mat:
    st.subheader("📚 Repozytorium Materiałów Badawczych i Biblioteka Projektu GOLEM 15")
    supp_lib_mat = db.get("supplementaryLibrary", DEFAULT_SEED["supplementaryLibrary"])
    with st.expander("📌 Zasady korzystania z biblioteki GOLEM 15 (1–6) oraz VI. Kolejność czytania", expanded=True):
        for r_idx, rule_txt in enumerate(supp_lib_mat.get("rules", []), start=1):
            st.markdown(f"**{r_idx}.** {rule_txt}")
        ro_mat = supp_lib_mat.get("readingOrder")
        if ro_mat:
            st.markdown(f"#### 🧭 {ro_mat.get('title', 'VI. KOLEJNOŚĆ CZYTANIA')}")
            ro_m_cols = st.columns(len(ro_mat.get("stages", [])))
            for s_idx, stage in enumerate(ro_mat.get("stages", [])):
                with ro_m_cols[s_idx]:
                    st.markdown(f"**{stage['stage']}**")
                    for b_item in stage.get("items", []):
                        st.markdown(f"- {b_item}")
            if ro_mat.get("principle"):
                st.info(f"**Zasada:** {ro_mat['principle']}")

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
            if m.get("links"):
                st.markdown("**🔗 Odnośniki i linki do źródeł:**")
                for lnk in m["links"]:
                    st.markdown(f"- [{lnk['label']}]({lnk['url']})")
            elif m.get("url"):
                st.markdown(f"[🔗 Otwórz źródło zewnętrzne / DOI]({m['url']})")
            st.caption(f"Zgłosił(a): **{m.get('author', 'Gość')}**")

# ------------------------------------------------------------------------------
# ZAKŁADKA 5: DODAWANIE PODPROJEKTÓW I MATERIAŁÓW + DELIKATNY ASYSTENT AI
# ------------------------------------------------------------------------------
with tab_new:
    st.subheader("🚀 Inicjowanie nowych podprojektów / środowisk oraz dodawanie materiałów")
    if can_auto_approve():
        st.success(f"✓ **Tryb Publikacji Natychmiastowej aktywny ({get_contributor_signature()})** — Twoje wpisy zostaną opublikowane od razu bez kolejki moderacji!")
    else:
        st.info("ℹ️ Jesteś w trybie Gościa (wpisy trafiają do kolejki). Możesz przejść do zakładki **🧑‍🔬 7. Badacze i Weryfikacja AI**, aby uzyskać **stałe konto Zweryfikowanego Badacza** i publikować od razu bez akceptacji!")

    with st.expander("🤖 Delikatny Asystent Metodologiczny AI — sprawdź klasyfikację epistemiczną i polską literaturę przed dodaniem wpisu", expanded=False):
        ai_c1, ai_c2 = st.columns([1, 2])
        with ai_c1:
            ai_target = st.selectbox(
                "Docelowa ścieżka / dziedzina:",
                options=[t["id"] for t in db["tracks"]] + [f["id"] for f in db["foundationDisciplines"]],
                format_func=lambda x: f"{tracks_by_id[x]['code']} — {tracks_by_id[x]['name']}" if x in tracks_by_id else f"Podstawy {foundations_by_id[x]['order']}: {foundations_by_id[x]['name']}",
                key="ai_helper_target",
            )
        with ai_c2:
            ai_draft_text = st.text_input("Wpisz roboczy tytuł lub temat swojego materiału / hipotezy:", key="ai_helper_draft")
        if ai_draft_text.strip():
            sug = ai_suggest_material_metadata(ai_draft_text, ai_draft_text, ai_target)
            st.markdown(
                f"- **Sugerowany status epistemiczny (Zasada 5):** `{sug['epistemicStatus']}`\n"
                f"- **Rekomendowany punkt wyjścia z Biblioteki Golem 15 (🇵🇱):** {sug['recommendedLiterature']}"
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
            sp_hyp = st.text_input("Hipoteza startowa")
            sp_phil = st.text_input("Nakładka interpretacyjna (Projekt E — Filozofia)")
            sp_author = st.text_input("Autor / Inicjator*", value=get_contributor_signature())

            if st.form_submit_button("🚀 Uruchom środowisko badawcze", use_container_width=True):
                if sp_title.strip() and sp_desc.strip():
                    final_branch = sp_custom_branch.strip() if sp_custom_branch.strip() else sp_branch
                    approval = "approved" if can_auto_approve() else "pending"
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
            mat_author = st.text_input("Autor zgłoszenia*", value=get_contributor_signature())

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
                        "status": "approved" if can_auto_approve() else "pending",
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
# ZAKŁADKA 7: STAŁE KONTA ZWERYFIKOWANYCH BADACZY I DELIKATNA WERYFIKACJA AI
# ------------------------------------------------------------------------------
with tab_researchers:
    st.subheader("🧑‍🔬 Zespół Stałych Badaczy & Autoryzacja z Delikatną Pomocą AI")
    st.markdown(
        "Aby właściciel projektu nie musiał ręcznie zatwierdzać każdej wrzutki, badacze mogą utworzyć **stałe konto Zweryfikowanego Badacza**. "
        "Po przejściu przyjaznej weryfikacji metodologiczno-epistemicznej wspieranej przez **Asystenta AI** (lub po dodaniu przez Administratora), "
        "wszystkie dodawane przez Ciebie materiały do nauki, artykuły, podprojekty i notatki są **publikowane natychmiastowo (`Zatwierdzone`)**."
    )

    col_res_left, col_res_right = st.columns([1.15, 1.35])

    with col_res_left:
        st.markdown(f"### 🏛️ Aktywni Stali Badacze ({len(active_researchers_list)})")
        for r in active_researchers_list:
            with st.container(border=True):
                st.markdown(f"#### 🧑‍🔬 {r['name']}  `{r.get('badge', '✓ Stały Badacz')}`")
                st.caption(f"**Rola:** {r.get('roleTitle', 'Badacz')} | **Obszar:** {r.get('specializationLabel', r.get('specialization', 'ALL'))}")
                if r.get("affiliation"):
                    st.caption(f"🏛️ Afiliacja / Zespół: {r['affiliation']}")
                st.write(r.get("bio", ""))
                if r.get("aiVerificationSummary"):
                    st.caption(f"🤖 *{r['aiVerificationSummary']}*")

        with st.container(border=True):
            st.markdown("#### 🔑 Szybkie logowanie na konto Stałego Badacza")
            if st.session_state.active_researcher:
                st.success(f"Jesteś zalogowany(a) jako: **{st.session_state.active_researcher['name']}** — masz aktywne uprawnienia do publikacji bez kolejki.")
            elif active_researchers_list:
                with st.form("tab_researcher_login_form", clear_on_submit=True):
                    login_res_id = st.selectbox(
                        "Wybierz swój profil Stałego Badacza",
                        options=[r["id"] for r in active_researchers_list],
                        format_func=lambda rid: next((f"{r['name']} — {r.get('roleTitle', '')}" for r in active_researchers_list if r["id"] == rid), rid),
                    )
                    login_res_pass = st.text_input("Twoje hasło Badacza", type="password", value="")
                    if st.form_submit_button("🧑‍🔬 Zaloguj na stałe konto Badacza", type="primary", use_container_width=True):
                        target_r = next((r for r in active_researchers_list if r["id"] == login_res_id), None)
                        if verify_researcher_password(login_res_pass, target_r):
                            st.session_state.active_researcher = target_r
                            st.success(f"Zalogowano jako {target_r['name']}!")
                            st.rerun()
                        else:
                            time.sleep(0.5)
                            st.error("Nieprawidłowe hasło dla wybranego profilu Badacza.")

    with col_res_right:
        with st.container(border=True):
            st.markdown("### 🤖 Dołącz na stałe jako Zweryfikowany Badacz (Delikatna Weryfikacja AI)")
            st.caption(
                "Wypełnij poniższą kartę badawczą. Asystent AI oceni spójność z metodologią projektu The Golem 15 "
                "(odróżnianie wiedzy potwierdzonej od hipotez i spekulacji oraz oparcie w literaturze). "
                "Po uzyskaniu min. **75/100 pkt** Twoje stałe konto zostaje od razu aktywowane!"
            )

            spec_options = (
                [t["id"] for t in db["tracks"]]
                + [f["id"] for f in db["foundationDisciplines"]]
            )

            def format_spec_option(code):
                if code in tracks_by_id:
                    return f"{tracks_by_id[code]['code']} — {tracks_by_id[code]['name']}"
                if code in foundations_by_id:
                    return f"Podstawy {foundations_by_id[code]['order']}: {foundations_by_id[code]['name']}"
                return code

            cand_name = st.text_input("Imię i nazwisko / Pseudonim naukowy*", key="cand_name")
            cand_spec = st.selectbox("Główna dziedzina lub ścieżka badawcza*", options=spec_options, format_func=format_spec_option, key="cand_spec")
            c_af1, c_af2 = st.columns(2)
            cand_role = c_af1.text_input("Tytuł / Rola w projekcie (np. Badacz Neuroinformatyki)", value="Stały Badacz The Golem 15", key="cand_role")
            cand_aff = c_af2.text_input("Afiliacja / Uczelnia / Koło / ORCID (opcjonalnie)", key="cand_aff")

            cand_sample = st.text_area(
                "1️⃣ Krótka próbka badawcza / opis zagadnienia, które chcesz rozwijać w Golemie 15 (2–4 zdania)*",
                placeholder="Np. Badam modele pobudliwości błony neuronalnej (Hodgkina-Huxleya oraz Izhikevicha) pod kątem estymacji kosztu obliczeniowego symulacji sieci korowych w Projekcie B...",
                key="cand_sample",
            )
            cand_cit = st.text_input(
                "2️⃣ Przywołane źródło bazowe (podręcznik z Biblioteki Golem 15, autor, PWN, OpenStax lub link DOI/URL)*",
                placeholder="Np. James W. Kalat — Biologiczne podstawy psychologii (PWN) / Dayan & Abbott — Theoretical Neuroscience",
                key="cand_cit",
            )

            if st.button("💡 Poproś Asystenta AI o delikatną podpowiedź do Twojej dziedziny", use_container_width=True):
                hint_meta = ai_suggest_material_metadata(cand_name, cand_sample, cand_spec)
                kw_hint = ", ".join(DOMAIN_KEYWORDS.get(cand_spec, ["model", "hipoteza", "pomiar"])[:6])
                st.info(
                    f"🤖 **Podpowiedź Asystenta AI dla obszaru {format_spec_option(cand_spec)}:**\n"
                    f"- **Warto przywołać literaturę podstawową:** {hint_meta['recommendedLiterature']}\n"
                    f"- **Przykładowe pojęcia kluczowe rozpoznawane w tym obszarze:** *{kw_hint}*\n"
                    f"- **Wskazówka metodologiczna:** Zaznacz w opisie, co jest modelem empirycznym/podręcznikowym, a co hipotezą badawczą."
                )

            q1_ans = st.selectbox(
                "3️⃣ Kalibracja epistemiczna (Zasada 5 Golema 15): Jaki status ma pełna emulacja ludzkiego mózgu (WBE) i przeniesienie umysłu?",
                options=[
                    "Hipoteza / długoterminowy cel badawczy i mapa drogowa wymagająca badań podstawowych (nie wiedza potwierdzona)",
                    "Wiedza w pełni potwierdzona i gotowa technologia wdrożeniowa",
                    "Zagadnienie niewymagające weryfikacji matematycznej ani biologicznej",
                ],
                key="cand_q1",
            )
            q2_ans = st.selectbox(
                "4️⃣ Kalibracja źródłowa (Zasady 1–4): Od jakich materiałów zaczynamy pracę nad nową dziedziną w Golemie 15?",
                options=[
                    "Od podręczników podstawowych (w pierwszej kolejności polskich 🇵🇱 i otwartych zasobów jak OpenStax/ZPE/NASA/ESA) oraz ćwiczeń",
                    "Od niezweryfikowanych spekulacji bez znajomości podstaw danej dziedziny",
                    "Wyłącznie od płatnych monografii bez sprawdzania wydania i przekładu",
                ],
                key="cand_q2",
            )

            c_pw1, c_pw2 = st.columns(2)
            cand_pass = c_pw1.text_input("Ustaw własne hasło Stałego Badacza (min. 6 znaków)*", type="password", value="", key="cand_pass")
            cand_pass2 = c_pw2.text_input("Powtórz hasło Badacza*", type="password", value="", key="cand_pass2")

            if st.button("🤖 Zweryfikuj przez Asystenta AI i aktywuj stałe konto Badacza", type="primary", use_container_width=True):
                if not cand_name.strip():
                    st.error("Podaj imię i nazwisko lub pseudonim naukowy.")
                elif len(cand_pass.strip()) < 6:
                    st.error("Hasło Badacza musi mieć co najmniej 6 znaków.")
                elif cand_pass != cand_pass2:
                    st.error("Wpisane hasła nie są identyczne.")
                else:
                    eval_res = evaluate_researcher_application_ai(
                        cand_name, cand_spec, cand_sample, cand_cit, q1_ans, q2_ans
                    )
                    st.markdown(f"#### 📊 Wynik Weryfikacji Metodologicznej AI: **{eval_res['score']} / 100 pkt**")
                    for fb in eval_res["feedback"]:
                        st.markdown(f"- {fb}")

                    if eval_res["passed"]:
                        new_researcher = {
                            "id": f"res-{int(time.time()*1000)}",
                            "name": cand_name.strip(),
                            "handle": "@" + cand_name.strip().lower().replace(" ", "-"),
                            "roleTitle": cand_role.strip() or "Stały Badacz The Golem 15",
                            "specialization": cand_spec,
                            "specializationLabel": format_spec_option(cand_spec),
                            "affiliation": cand_aff.strip(),
                            "orcid": "",
                            "bio": f"{cand_sample.strip()} (Źródło bazowe: {cand_cit.strip()})",
                            "aiVerificationScore": eval_res["score"],
                            "aiVerificationSummary": eval_res["summary"],
                            "badge": f"✓ Stały Badacz (AI {eval_res['score']}/100)",
                            "status": "active",
                            "joinedAt": datetime.utcnow().isoformat() + "Z",
                            "auth": create_admin_auth_record(cand_pass.strip(), iterations=260000),
                        }
                        db.setdefault("verifiedResearchers", []).append(new_researcher)
                        save_db(db)
                        st.session_state.active_researcher = new_researcher
                        st.success(
                            f"🎉 Gratulacje, **{new_researcher['name']}**! Twoje stałe konto Zweryfikowanego Badacza zostało utworzone i zaszyfrowane (PBKDF2-SHA256). "
                            "Od teraz wszystkie Twoje materiały i podprojekty publikują się automatycznie bez kolejki!"
                        )
                    else:
                        st.warning(eval_res["summary"])


# ------------------------------------------------------------------------------
# ZAKŁADKA 8: PANEL AUTORYZACJI ADMINISTRATORA (MODERACJA I ZARZĄDZANIE BADACZAMI)
# ------------------------------------------------------------------------------
with tab_admin:
    st.subheader("🛡️ Centrum Moderacji i Administracji")
    if not st.session_state.is_admin:
        st.info("🔒 Sekcja moderacji zgłoszeń jest przeznaczona wyłącznie dla właściciela projektu.")
        with st.expander("🔑 Autoryzacja właściciela projektu", expanded=False):
            with st.form("main_admin_login_form", clear_on_submit=True):
                admin_login_pass = st.text_input("Klucz dostępu Administratora", type="password", value="")
                if st.form_submit_button("Odblokuj panel", type="primary"):
                    if st.session_state.failed_admin_attempts >= 5:
                        time.sleep(2.0)
                    if verify_admin_password(admin_login_pass, db):
                        st.session_state.is_admin = True
                        st.session_state.failed_admin_attempts = 0
                        st.success("Autoryzacja zakończona pomyślnie.")
                        st.rerun()
                    else:
                        st.session_state.failed_admin_attempts += 1
                        time.sleep(0.6)
                        st.error("Odmowa dostępu — nieprawidłowe hasło.")
    else:
        with st.expander("🔑 Zmień / zaktualizuj hasło Administratora (PBKDF2-HMAC-SHA256)", expanded=False):
            st.caption(
                "Hasło nigdy nie jest zapisywane w postaci jawnej — w bazie danych przechowywany jest wyłącznie "
                "kryptograficzny skrót PBKDF2-HMAC-SHA256 (260 000 iteracji) z losową solą 128-bitową."
            )
            with st.form("change_admin_pass_form", clear_on_submit=True):
                current_pass = st.text_input("Aktualne hasło Administratora", type="password", value="")
                new_pass = st.text_input("Nowe hasło Administratora (min. 8 znaków)", type="password", value="")
                new_pass_confirm = st.text_input("Powtórz nowe hasło", type="password", value="")
                if st.form_submit_button("Zaktualizuj hasło kryptograficzne", type="primary"):
                    if not verify_admin_password(current_pass, db):
                        st.error("Aktualne hasło jest nieprawidłowe.")
                    elif len(new_pass.strip()) < 8:
                        st.error("Nowe hasło musi zawierać co najmniej 8 znaków.")
                    elif new_pass != new_pass_confirm:
                        st.error("Nowe hasła nie są identyczne.")
                    else:
                        new_auth = create_admin_auth_record(new_pass.strip(), iterations=260000)
                        db["projectMeta"]["adminAuth"] = new_auth
                        db["projectMeta"].pop("adminPassword", None)
                        save_db(db)
                        st.success("Hasło zostało zaszyfrowane (PBKDF2-HMAC-SHA256) i zapisane w bazie!")
                        st.code(json.dumps(new_auth, indent=2), language="json")

        with st.expander("🧑‍🔬 Zarządzaj Stałymi Badaczami (Dodaj badacza ręcznie na stałe lub zmień status)", expanded=False):
            st.caption("Badacze ze statusem **active** mogą publikować materiały i rozwijać podprojekty bez Twojej ręcznej akceptacji.")
            with st.form("admin_add_researcher_form", clear_on_submit=True):
                st.markdown("**➕ Dodaj nowego Stałego Badacza bezpośrednio (bez testu AI):**")
                ar_c1, ar_c2, ar_c3 = st.columns(3)
                ar_name = ar_c1.text_input("Imię i nazwisko Badacza*")
                ar_role = ar_c2.text_input("Rola / Specjalizacja", value="Stały Badacz The Golem 15")
                ar_pass = ar_c3.text_input("Hasło startowe dla Badacza (min. 6 znaków)*", type="password")
                ar_bio = st.text_input("Krótki opis / obszar badań")
                if st.form_submit_button("✓ Dodaj Badacza na stałe", type="primary"):
                    if ar_name.strip() and len(ar_pass.strip()) >= 6:
                        new_r = {
                            "id": f"res-{int(time.time()*1000)}",
                            "name": ar_name.strip(),
                            "handle": "@" + ar_name.strip().lower().replace(" ", "-"),
                            "roleTitle": ar_role.strip() or "Stały Badacz",
                            "specialization": "ALL",
                            "specializationLabel": ar_role.strip() or "Wszystkie ścieżki (A–G)",
                            "affiliation": "Zespół Badawczy The Golem 15",
                            "orcid": "",
                            "bio": ar_bio.strip() or "Stały członek zespołu badawczego autoryzowany przez Właściciela projektu.",
                            "aiVerificationScore": 100,
                            "aiVerificationSummary": "Autoryzacja bezpośrednia przez Właściciela projektu (Ireneusz).",
                            "badge": "✓ Stały Badacz (Autoryzacja Właściciela)",
                            "status": "active",
                            "joinedAt": datetime.utcnow().isoformat() + "Z",
                            "auth": create_admin_auth_record(ar_pass.strip(), iterations=260000),
                        }
                        db.setdefault("verifiedResearchers", []).append(new_r)
                        save_db(db)
                        st.success(f"Dodano stałego badacza: {new_r['name']}!")
                        st.rerun()
                    else:
                        st.error("Podaj imię i nazwisko oraz hasło (min. 6 znaków).")

            for r_idx, r_item in enumerate(db.get("verifiedResearchers", [])):
                rc1, rc2 = st.columns([4, 1])
                rc1.markdown(f"**{r_item['name']}** — *{r_item.get('roleTitle','')}* (`{r_item.get('status','active')}`)")
                if r_item["id"] != "res-founder":
                    if r_item.get("status") == "active":
                        if rc2.button("Zawieś", key=f"susp_res_{r_item['id']}"):
                            r_item["status"] = "suspended"
                            save_db(db)
                            st.rerun()
                    else:
                        if rc2.button("Aktywuj", key=f"act_res_{r_item['id']}"):
                            r_item["status"] = "active"
                            save_db(db)
                            st.rerun()

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
