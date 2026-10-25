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
            "topic": "Algebra liniowa, przestrzenie wektorowe, rachunek macierzowy i teoria operatorów.",
            "title": "I. Matematyka: Gilbert Strang („Introduction to Linear Algebra”), Penrose („Road to Reality”) i podręczniki matematyki",
            "level": "Podstawowy / Akademicki",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów (PL) oraz Gilbert Strang — „Introduction to Linear Algebra” (EN). Etap czytania: NAJPIERW (podstawy matematyki).",
            "url": "https://math.mit.edu/~gs/linearalgebra/",
            "links": [
                {"label": "🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT 18.06 + materiały)", "url": "https://math.mit.edu/~gs/linearalgebra/"},
                {"label": "🇬🇧 MIT OCW 18.06 — Wykłady wideo prof. Gilberta Stranga z algebry liniowej", "url": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"},
                {"label": "🇬🇧 OpenStax — Darmowe podręczniki matematyki i analizy (Calculus / Algebra)", "url": "https://openstax.org/subjects/math"},
                {"label": "🇵🇱 ZPE — Matematyka i algebra liniowa (po polsku)", "url": "https://zpe.gov.pl/"}
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
            "title": "I. Informatyka: Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” / „Code”",
            "level": "Podstawowy (Etap 1: Najpierw)",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Fundamentalna pozycja wyjaśniająca od podstaw, jak z bramek logicznych, przekaźników i tranzystorów powstaje komputer, pamięć i oprogramowanie. Pierwsza pozycja w kolejności czytania („Najpierw”).",
            "url": "https://codehiddenlanguage.com/",
            "links": [
                {"label": "🇬🇧 Charles Petzold — Code (Oficjalna strona książki z interaktywnymi układami)", "url": "https://codehiddenlanguage.com/"},
                {"label": "🇵🇱 Charles Petzold — Kod. Ukryty język komputerów. Wydanie II (Helion)", "url": "https://helion.pl/"},
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
            "title": "I. Programowanie: Eric Matthes — „Python. Instrukcje dla programisty” / „Python Crash Course”",
            "level": "Podstawowy (Etap 1: Najpierw)",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Praktyczny podręcznik programowania w języku Python z ćwiczeniami i projektami. Obowiązkowa pozycja pierwszego etapu czytania („Najpierw”) przed przejściem do symulacji naukowych.",
            "url": "https://ehmatthes.github.io/pcc_3e/",
            "links": [
                {"label": "🇬🇧 Eric Matthes — Python Crash Course (Oficjalne materiały, kod i ćwiczenia)", "url": "https://ehmatthes.github.io/pcc_3e/"},
                {"label": "🇵🇱 Eric Matthes — Python. Instrukcje dla programisty (Wydawnictwo Helion)", "url": "https://helion.pl/"},
                {"label": "🇬🇧 Scientific Python Lectures (NumPy, SciPy, Matplotlib)", "url": "https://lectures.scientific-python.org/"},
                {"label": "🇬🇧 Brian2 — Symulator sieci neuronowych w Pythonie", "url": "https://briansimulator.org/"}
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
            "title": "II. Fizyka i Komputery Kwantowe: Podręczniki fizyki ogólnej (PL), David J. Griffiths oraz Nielsen & Chuang (EN)",
            "level": "Podstawowy → Zaawansowany",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Polskojęzyczne: Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach. Anglojęzyczne (etap zaawansowany): David J. Griffiths — „Introduction to Quantum Mechanics” oraz Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”.",
            "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1",
            "links": [
                {"label": "🇵🇱 OpenStax — Fizyka dla szkół wyższych (Tom 1–3, darmowy podręcznik po polsku)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                {"label": "🇬🇧 David J. Griffiths — Introduction to Quantum Mechanics (Cambridge University Press)", "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"},
                {"label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — Quantum Computation and Quantum Information", "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"},
                {"label": "🇬🇧 The Feynman Lectures on Physics (Caltech — darmowy dostęp)", "url": "https://www.feynmanlectures.caltech.edu/"}
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
            "title": "II. Elektronika: Podręczniki podstaw elektroniki i układów cyfrowych (PL), Horowitz & Hill oraz ZPE",
            "level": "Podstawowy / Zaawansowany",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Podręczniki podstaw elektroniki i układów cyfrowych, wzmacniacze, oscylatory, filtry, przetworniki A/C i C/A oraz architektura bramek logicznych.",
            "url": "https://zpe.gov.pl/",
            "links": [
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i układy cyfrowe", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 OpenAGH — E-podręczniki z elektroniki", "url": "https://open.agh.edu.pl/"},
                {"label": "🇬🇧 All About Circuits — Darmowy podręcznik elektroniki analogowej i cyfrowej", "url": "https://www.allaboutcircuits.com/textbook/"},
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
            "title": "III. Chemia i Biochemia: OpenStax Chemistry 2e (EN) oraz akademickie podręczniki chemii ogólnej, organicznej i biochemii (PL/EN)",
            "level": "Podstawowy / Akademicki (Etap 2: Następnie)",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Polskojęzyczne: Akademickie podręczniki chemii ogólnej, organicznej i biochemii. Anglojęzyczne: OpenStax Chemistry 2e — podręcznik chemii ogólnej oraz akademickie podręczniki biochemii i biologii molekularnej.",
            "url": "https://openstax.org/details/books/chemistry-2e",
            "links": [
                {"label": "🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej online/PDF", "url": "https://openstax.org/details/books/chemistry-2e"},
                {"label": "🇬🇧 OpenStax Organic Chemistry — Darmowy podręcznik chemii organicznej", "url": "https://openstax.org/details/books/organic-chemistry"},
                {"label": "🇬🇧 NCBI Bookshelf — Biochemistry (Stryer / darmowe podręczniki biochemii)", "url": "https://www.ncbi.nlm.nih.gov/books/"},
                {"label": "🇵🇱 Księgarnia Naukowa PWN — Chemia ogólna, organiczna i biochemia", "url": "https://ksiegarnia.pwn.pl/"}
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
            "title": "III. Biologia i Genetyka: Terence A. Brown („Genomy”), „Biologia Campbella” (PL) oraz OpenStax Biology 2e (EN)",
            "level": "Podstawowy / Akademicki (Etap 2: Następnie)",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Polskojęzyczne: 1. Terence A. Brown — „Genomy”, 2. „Biologia Campbella” — polskie wydanie. Anglojęzyczne: OpenStax Biology 2e — podręcznik biologii oraz akademickie podręczniki biologii molekularnej.",
            "url": "https://openstax.org/details/books/biology-2e",
            "links": [
                {"label": "🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii online/PDF", "url": "https://openstax.org/details/books/biology-2e"},
                {"label": "🇬🇧 Terence A. Brown — Genomes (Darmowy dostęp w bazie NCBI Bookshelf)", "url": "https://www.ncbi.nlm.nih.gov/books/NBK21128/"},
                {"label": "🇵🇱 Terence A. Brown — Genomy & Biologia Campbella (Wydawnictwo Naukowe PWN / Rebis)", "url": "https://ksiegarnia.pwn.pl/"},
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
            "title": "IV & V. Sztuczna Inteligencja i Neuronauka Obliczeniowa: Aurélien Géron („Hands-On ML”) oraz Dayan & Abbott („Theoretical Neuroscience”)",
            "level": "Średniozaawansowany / Zaawansowany",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Praktyczne uczenie maszynowe i głębokie sieci neuronowe (Géron — Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow) oraz matematyczne modelowanie sieci neuronalnych (Dayan & Abbott — Theoretical Neuroscience).",
            "url": "https://github.com/ageron/handson-ml3",
            "links": [
                {"label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Oficjalne notebooki GitHub)", "url": "https://github.com/ageron/handson-ml3"},
                {"label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                {"label": "🇬🇧 Neuromatch Academy — Computational Neuroscience & Deep Learning", "url": "https://compneuro.neuromatch.io/"},
                {"label": "🇵🇱 Aurélien Géron — Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow (Helion)", "url": "https://helion.pl/"}
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
            "title": "IV. Projekt A (Człowiek biocyfrowo-robotyczny): Kalat („Biologiczne podstawy psychologii”), OpenStax Anatomy & Physiology 2e, Géron („Hands-On ML”), biofizyka, robotyka i BCI",
            "level": "Podstawowy → Zaawansowany",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Polskojęzyczne: 1. James W. Kalat — Biologiczne podstawy psychologii, 2. Akademickie podręczniki anatomii i fizjologii człowieka, 3. Podręczniki biofizyki, biomechaniki i biomateriałów, 4. Podręczniki robotyki, elektroniki i układów sterowania. Anglojęzyczne: 5. OpenStax Anatomy and Physiology 2e, 6. Géron — Hands-On Machine Learning, 7. Podręczniki inżynierii tkankowej, neuroprotetyki i BCI.",
            "url": "https://openstax.org/details/books/anatomy-and-physiology-2e",
            "links": [
                {"label": "🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik anatomii i fizjologii)", "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"},
                {"label": "🇵🇱 James W. Kalat — Biologiczne podstawy psychologii (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Scikit-Learn, Keras, TensorFlow)", "url": "https://github.com/ageron/handson-ml3"},
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
            "title": "V. Projekt B (Cyfrowy umysł): Kalat, Kandel, Squire, Dayan & Abbott, Izhikevich, Seung („Connectome”), Miller, Churchland & Sejnowski, Sandberg & Bostrom („Whole Brain Emulation”)",
            "level": "Podstawowy → Zaawansowany",
            "format": "Biblioteka Projektu (PL / EN)",
            "content": "Pełna bibliografia Projektu B: od „Biologicznych podstaw psychologii” (Kalat), przez „Theoretical Neuroscience” (Dayan, Abbott), „Dynamical Systems in Neuroscience” (Izhikevich), „Connectome” (Seung), „Whole Brain Emulation: A Roadmap” (Sandberg, Bostrom), po „Principles of Neural Science” (Kandel), „Fundamental Neuroscience” (Squire) i „The Computational Brain” (Churchland, Sejnowski).",
            "url": "https://www.izhikevich.org/publications/dsn.pdf",
            "links": [
                {"label": "🇬🇧 Eugene M. Izhikevich — Dynamical Systems in Neuroscience (Darmowy PDF książki)", "url": "https://www.izhikevich.org/publications/dsn.pdf"},
                {"label": "🇬🇧 Anders Sandberg, Nick Bostrom — Whole Brain Emulation: A Roadmap (Pełny raport PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                {"label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                {"label": "🇬🇧 Paul Miller — An Introductory Course in Computational Neuroscience (MIT Press)", "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"},
                {"label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — The Computational Brain (MIT Press)", "url": "https://mitpress.mit.edu/9780262531207/the-computational-brain/"},
                {"label": "🇬🇧 Eric R. Kandel et al. — Principles of Neural Science & Larry Squire — Fundamental Neuroscience", "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"},
                {"label": "🇬🇧 Sebastian Seung — Connectome (Seung Lab / MIT)", "url": "https://seunglab.org/"},
                {"label": "🇵🇱 James W. Kalat — Biologiczne podstawy psychologii (PWN)", "url": "https://ksiegarnia.pwn.pl/"}
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
            "title": "Projekt C (Po polsku i angielsku): Elektronika analogowa, przetworniki ADC/DAC, Analog & Neuromorphic Computing",
            "level": "Podstawowy / Akademicki",
            "format": "Biblioteka uzupełniająca GOLEM 15",
            "content": "Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne. Obejmuje wzmacniacze, oscylatory, filtry, sprzężenie zwrotne, przetworniki A/C i C/A oraz układy neuromorficzne.",
            "url": "https://zpe.gov.pl/",
            "links": [
                {"label": "Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika", "url": "https://zpe.gov.pl/"},
                {"label": "Frontiers in Neuroscience — Neuromorphic Engineering", "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"},
                {"label": "arXiv — Neural and Evolutionary Computing (Neuromorphic & Analog NN)", "url": "https://arxiv.org/list/cs.NE/recent"},
                {"label": "MIT OCW — Nonlinear Dynamics and Chaos", "url": "https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2014/"}
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
            "title": "Projekt D (Po polsku i angielsku): Biologia komórki, embriologia, komórki macierzyste, inżynieria tkankowa i National Academies",
            "level": "Zaawansowany / Badawczy",
            "format": "Biblioteka uzupełniająca GOLEM 15",
            "content": "Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka. Obejmuje podręczniki akademickie oraz raporty National Academies o odpowiedzialnym rozwoju biologii syntetycznej.",
            "url": "https://www.nationalacademies.org/",
            "links": [
                {"label": "National Academies — Odpowiedzialny rozwój biologii syntetycznej", "url": "https://www.nationalacademies.org/"},
                {"label": "NCBI Bookshelf — Developmental Biology & Cell Biology", "url": "https://www.ncbi.nlm.nih.gov/books/"},
                {"label": "ISSCR — International Society for Stem Cell Research", "url": "https://www.isscr.org/"},
                {"label": "Nature — Synthetic Biology & Tissue Engineering", "url": "https://www.nature.com/subjects/synthetic-biology"}
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
            "title": "Projekt E (Filozofia): Alan Chalmers, Thomas S. Kuhn, Michał Heller oraz filozofia starożytna, umysłu i bioetyka",
            "level": "Podstawowy / Akademicki",
            "format": "Biblioteka uzupełniająca GOLEM 15",
            "content": "Po polsku: Alan Chalmers („Czym jest to, co zwiemy nauką?”), Thomas S. Kuhn („Struktura rewolucji naukowych”), Michał Heller („Filozofia nauki. Wprowadzenie”). Zastosowanie: ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.",
            "url": "https://plato.stanford.edu/",
            "links": [
                {"label": "Copernicus Center Press — Książki prof. Michała Hellera i filozofia nauki", "url": "https://ccpress.pl/"},
                {"label": "Stanford Encyclopedia of Philosophy (Filozofia nauki, umysłu i bioetyka)", "url": "https://plato.stanford.edu/"},
                {"label": "Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, stoicy)", "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"},
                {"label": "Internet Encyclopedia of Philosophy (IEP)", "url": "https://iep.utm.edu/"}
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
            "title": "Projekt F (Człowiek w kosmosie): Darmowe źródła NASA i ESA oraz fizjologia kosmiczna i systemy podtrzymywania życia",
            "level": "Podstawowy / Zaawansowany",
            "format": "Biblioteka uzupełniająca GOLEM 15",
            "content": "Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty. Darmowe źródła NASA i ESA dotyczące zdrowia człowieka w kosmosie, promieniowania, napędów, ECLSS i psychologii izolacji.",
            "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/",
            "links": [
                {"label": "NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)", "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"},
                {"label": "ESA — Edukacja kosmiczna (Teach with Space)", "url": "https://education.esa.int/teach-with-space/"},
                {"label": "ESA — Eksploracja załogowa i robotyczna (Human and Robotic Exploration)", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"},
                {"label": "NASA Technical Reports Server (NTRS — publikacje inżynieryjne i medyczne)", "url": "https://ntrs.nasa.gov/"}
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
            "title": "Projekt G (Człowiek na Ziemi): Jan Krystek („Ochrona środowiska dla inżynierów”), Politechnika Śląska i ESA Education",
            "level": "Podstawowy / Inżynierski",
            "format": "Biblioteka uzupełniająca GOLEM 15",
            "content": "Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa. Obejmuje ochronę wód, powietrza i gleby, OZE, gospodarkę obiegu zamkniętego, LCA oraz satelitarny monitoring środowiska i AI.",
            "url": "https://www.polsl.pl/",
            "links": [
                {"label": "ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska", "url": "https://education.esa.int/teach-with-space/"},
                {"label": "Politechnika Śląska — Materiały dot. podstaw ochrony środowiska", "url": "https://www.polsl.pl/"},
                {"label": "Jan Krystek — Ochrona środowiska dla inżynierów (PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "Europejska Agencja Środowiska (EEA — raporty, klimat, GOZ, LCA)", "url": "https://www.eea.europa.eu/pl"}
            ],
            "author": "Administrator",
            "status": "approved",
            "createdAt": "2026-10-25T12:30:00Z",
        },
    ],
    "supplementaryLibrary": {
        "title": "BIBLIOTEKA PROJEKTU GOLEM 15 — Literatura podstawowa (I–VI) oraz uzupełniająca (Projekty C–G)",
        "description": "Kompletna bibliografia polsko- i anglojęzyczna: Wspólne podstawy (I. Matematyka i Informatyka, II. Fizyka i Komputery Kwantowe, III. Chemia, Biologia i Genetyka), IV. Projekt A, V. Projekt B, VI. Kolejność czytania oraz Biblioteka uzupełniająca do Projektów C, D, E, F i G wraz z bezpośrednimi odnośnikami.",
        "readingOrder": {
            "title": "VI. KOLEJNOŚĆ CZYTANIA — Plan lektur krok po kroku",
            "principle": "Zasada: najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja. Pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi.",
            "stages": [
                {
                    "stage": "1. Najpierw (Fundamenty obliczeń, programowania, matematyki i fizyki)",
                    "items": [
                        "Charles Petzold — *Kod. Ukryty język komputerów. Wydanie II* / *Code* — [Strona książki Code](https://codehiddenlanguage.com/) | [Helion](https://helion.pl/)",
                        "Eric Matthes — *Python. Instrukcje dla programisty* / *Python Crash Course* — [Materiały i ćwiczenia](https://ehmatthes.github.io/pcc_3e/) | [Helion](https://helion.pl/)",
                        "Podstawy matematyki (i algebry liniowej) — [OpenStax Math](https://openstax.org/subjects/math) | [Gilbert Strang MIT 18.06](https://math.mit.edu/~gs/linearalgebra/)",
                        "Podręcznik fizyki ogólnej — [OpenStax Fizyka dla szkół wyższych Tom 1–3 (PL)](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1)",
                    ],
                },
                {
                    "stage": "2. Następnie (Genomy, chemia, biologia i biologiczne podstawy psychologii)",
                    "items": [
                        "Terence A. Brown — *Genomy* — [NCBI Genomes](https://www.ncbi.nlm.nih.gov/books/NBK21128/) | [PWN](https://ksiegarnia.pwn.pl/)",
                        "Podstawy chemii, biologii i biochemii — [OpenStax Chemistry 2e](https://openstax.org/details/books/chemistry-2e) | [OpenStax Biology 2e](https://openstax.org/details/books/biology-2e) | [Biologia Campbella](https://ksiegarnia.pwn.pl/)",
                        "James W. Kalat — *Biologiczne podstawy psychologii* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                    ],
                },
                {
                    "stage": "3. Później (Neuronauka obliczeniowa, układy dynamiczne, konektomika i WBE)",
                    "items": [
                        "Peter Dayan, L. F. Abbott — *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems* — [MIT Press](https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/)",
                        "Eugene M. Izhikevich — *Dynamical Systems in Neuroscience* — [Pełny PDF autora](https://www.izhikevich.org/publications/dsn.pdf)",
                        "Sebastian Seung — *Connectome: How the Brain's Wiring Makes Us Who We Are* — [Seung Lab MIT](https://seunglab.org/)",
                        "Anders Sandberg, Nick Bostrom — *Whole Brain Emulation: A Roadmap* — [Pełny raport PDF (FHI Oxford)](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)",
                    ],
                },
                {
                    "stage": "4. Na zaawansowanym etapie (Neurobiologia kliniczna/akademicka i obliczenia kwantowe)",
                    "items": [
                        "Eric R. Kandel i współautorzy — *Principles of Neural Science* — [McGraw Hill](https://www.mheducation.com/)",
                        "Larry Squire i współautorzy — *Fundamental Neuroscience* — [ScienceDirect](https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience)",
                        "Patricia S. Churchland, Terrence J. Sejnowski — *The Computational Brain* — [MIT Press](https://mitpress.mit.edu/9780262531207/the-computational-brain/)",
                        "David J. Griffiths — *Introduction to Quantum Mechanics* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E)",
                        "Michael A. Nielsen, Isaac L. Chuang — *Quantum Computation and Quantum Information* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)",
                    ],
                },
            ],
        },
        "rules": [
            "Zasada czytania: najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja.",
            "Najpierw korzystać z materiałów bezpłatnych (np. OpenStax, ZPE, NCBI Bookshelf, NASA, ESA).",
            "Książki specjalistyczne kupować dopiero po poznaniu podstaw danego obszaru.",
            "Przed zakupem sprawdzać dokładny tytuł, autora, wydanie i dostępność polskiego przekładu.",
            "W szybko rozwijających się dziedzinach korzystać również z aktualnych przeglądów naukowych i dokumentacji instytucji badawczych.",
            "Rozróżniać wiedzę potwierdzoną, aktywne badania, hipotezy i spekulacje (pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi).",
            "Traktować bibliografię jako zasób długoterminowy, a nie listę lektur do przeczytania w całości od razu.",
        ],
        "projects": [
            {
                "trackId": "FND-1",
                "title": "I. MATEMATYKA I INFORMATYKA (Wspólne podstawy)",
                "sequenceLabel": "Etap czytania",
                "sequence": "Najpierw: Petzold (Kod) → Matthes (Python. Instrukcje dla programisty) → Podstawy matematyki i algebry liniowej (Strang).",
                "links": [
                    {"label": "🇬🇧 Charles Petzold — Code (Strona książki i symulacje)", "url": "https://codehiddenlanguage.com/"},
                    {"label": "🇬🇧 Eric Matthes — Python Crash Course (Zasoby i ćwiczenia)", "url": "https://ehmatthes.github.io/pcc_3e/"},
                    {"label": "🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT)", "url": "https://math.mit.edu/~gs/linearalgebra/"},
                    {"label": "🇵🇱 Wydawnictwo Helion (Polskie wydania Petzolda i Matthesa)", "url": "https://helion.pl/"},
                    {"label": "🇬🇧 OpenStax Mathematics (Darmowe podręczniki matematyki)", "url": "https://openstax.org/subjects/math"}
                ],
                "groups": [
                    {
                        "heading": "Polskojęzyczne",
                        "items": [
                            "1. Charles Petzold — *Kod. Ukryty język komputerów. Wydanie II.* — [Wydawnictwo Helion](https://helion.pl/)",
                            "2. Eric Matthes — *Python. Instrukcje dla programisty.* — [Wydawnictwo Helion](https://helion.pl/)",
                            "3. Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów — [ZPE Matematyka](https://zpe.gov.pl/) | [OpenAGH](https://open.agh.edu.pl/)",
                        ],
                    },
                    {
                        "heading": "Anglojęzyczne",
                        "items": [
                            "4. Gilbert Strang — *Introduction to Linear Algebra.* — [MIT Linear Algebra](https://math.mit.edu/~gs/linearalgebra/)",
                            "5. Charles Petzold — *Code.* — [codehiddenlanguage.com](https://codehiddenlanguage.com/)",
                            "6. Eric Matthes — *Python Crash Course.* — [ehmatthes.github.io/pcc_3e](https://ehmatthes.github.io/pcc_3e/)",
                        ],
                    },
                ],
            },
            {
                "trackId": "FND-4",
                "title": "II. FIZYKA I KOMPUTERY KWANTOWE (Wspólne podstawy)",
                "sequenceLabel": "Etap czytania",
                "sequence": "Najpierw: Podręcznik fizyki ogólnej i podstaw elektroniki → Na zaawansowanym etapie: Griffiths (Introduction to Quantum Mechanics) oraz Nielsen i Chuang (Quantum Computation and Quantum Information).",
                "links": [
                    {"label": "🇵🇱 OpenStax — Fizyka dla szkół wyższych (Tom 1–3 po polsku, darmowy)", "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"},
                    {"label": "🇬🇧 David J. Griffiths — Introduction to Quantum Mechanics (CUP)", "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"},
                    {"label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — Quantum Computation and Quantum Information", "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"},
                    {"label": "🇵🇱 ZPE / OpenAGH — Podstawy elektroniki i układów cyfrowych", "url": "https://zpe.gov.pl/"}
                ],
                "groups": [
                    {
                        "heading": "Polskojęzyczne",
                        "items": [
                            "1. Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach — [OpenStax Fizyka PL](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1) | [PWN](https://ksiegarnia.pwn.pl/)",
                            "2. Podręczniki podstaw elektroniki i układów cyfrowych — [ZPE Elektronika](https://zpe.gov.pl/) | [OpenAGH](https://open.agh.edu.pl/)",
                        ],
                    },
                    {
                        "heading": "Anglojęzyczne",
                        "items": [
                            "3. David J. Griffiths — *Introduction to Quantum Mechanics.* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E)",
                            "4. Michael A. Nielsen, Isaac L. Chuang — *Quantum Computation and Quantum Information.* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)",
                        ],
                    },
                ],
            },
            {
                "trackId": "FND-7",
                "title": "III. CHEMIA, BIOLOGIA I GENETYKA (Wspólne podstawy)",
                "sequenceLabel": "Etap czytania",
                "sequence": "Następnie (po podstawach matematyki, fizyki i informatyki): Brown (Genomy) → Podstawy chemii, biologii i biochemii (OpenStax Chemistry 2e, OpenStax Biology 2e, Biologia Campbella).",
                "links": [
                    {"label": "🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej", "url": "https://openstax.org/details/books/chemistry-2e"},
                    {"label": "🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii", "url": "https://openstax.org/details/books/biology-2e"},
                    {"label": "🇬🇧 Terence A. Brown — Genomes (NCBI Bookshelf)", "url": "https://www.ncbi.nlm.nih.gov/books/NBK21128/"},
                    {"label": "🇵🇱 Terence A. Brown „Genomy” & „Biologia Campbella” (PWN / Rebis)", "url": "https://ksiegarnia.pwn.pl/"}
                ],
                "groups": [
                    {
                        "heading": "Polskojęzyczne",
                        "items": [
                            "1. Terence A. Brown — *Genomy.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                            "2. *Biologia Campbella* — polskie wydanie — [Księgarnia PWN / Rebis](https://ksiegarnia.pwn.pl/)",
                            "3. Akademickie podręczniki chemii ogólnej, organicznej i biochemii — [PWN Naukowe](https://ksiegarnia.pwn.pl/) | [ZPE Chemia](https://zpe.gov.pl/)",
                        ],
                    },
                    {
                        "heading": "Anglojęzyczne",
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
                "title": "IV. PROJEKT A — CZŁOWIEK BIOCYFROWO-ROBOTYCZNY",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Anatomia, fizjologia i biologiczne podstawy psychologii (Kalat, OpenStax Anatomy & Physiology 2e) → Biofizyka, biomechanika i biomateriały → Robotyka, elektronika, sterowanie i uczenie maszynowe (Géron) → Inżynieria tkankowa, neuroprotetyka i interfejsy mózg–komputer (BCI).",
                "links": [
                    {"label": "🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik online/PDF)", "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"},
                    {"label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Scikit-Learn, Keras, TensorFlow)", "url": "https://github.com/ageron/handson-ml3"},
                    {"label": "🇵🇱 James W. Kalat — Biologiczne podstawy psychologii (PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇬🇧 MIT OCW — Introduction to Robotics & Biomechanics", "url": "https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/"}
                ],
                "groups": [
                    {
                        "heading": "Polskojęzyczne",
                        "items": [
                            "1. James W. Kalat — *Biologiczne podstawy psychologii.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                            "2. Akademickie podręczniki anatomii i fizjologii człowieka — [PWN / PZWL](https://ksiegarnia.pwn.pl/)",
                            "3. Akademickie podręczniki biofizyki, biomechaniki i biomateriałów — [OpenAGH](https://open.agh.edu.pl/) | [PWN](https://ksiegarnia.pwn.pl/)",
                            "4. Podręczniki robotyki, elektroniki i układów sterowania — [ZPE](https://zpe.gov.pl/) | [PWN](https://ksiegarnia.pwn.pl/)",
                        ],
                    },
                    {
                        "heading": "Anglojęzyczne",
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
                "title": "V. PROJEKT B — CYFROWY UMYSŁ",
                "sequenceLabel": "Kolejność czytania (Etapy 2 → 3 → 4)",
                "sequence": "Następnie: Kalat (Biologiczne podstawy psychologii) → Później: Dayan & Abbott (Theoretical Neuroscience), Izhikevich (Dynamical Systems in Neuroscience), Seung (Connectome), Sandberg & Bostrom (Whole Brain Emulation: A Roadmap) → Na zaawansowanym etapie: Kandel (Principles of Neural Science), Squire (Fundamental Neuroscience), Churchland & Sejnowski (The Computational Brain).",
                "links": [
                    {"label": "🇬🇧 Eugene M. Izhikevich — Dynamical Systems in Neuroscience (Darmowy PDF autora)", "url": "https://www.izhikevich.org/publications/dsn.pdf"},
                    {"label": "🇬🇧 Anders Sandberg, Nick Bostrom — Whole Brain Emulation: A Roadmap (PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                    {"label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                    {"label": "🇬🇧 Paul Miller — An Introductory Course in Computational Neuroscience", "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"},
                    {"label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — The Computational Brain", "url": "https://mitpress.mit.edu/9780262531207/the-computational-brain/"},
                    {"label": "🇬🇧 Sebastian Seung — Connectome (Seung Lab MIT)", "url": "https://seunglab.org/"},
                    {"label": "🇬🇧 Larry Squire et al. — Fundamental Neuroscience (ScienceDirect)", "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"}
                ],
                "groups": [
                    {
                        "heading": "Polskojęzyczne",
                        "items": [
                            "1. James W. Kalat — *Biologiczne podstawy psychologii.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
                            "2. Podręczniki neurobiologii i fizjologii układu nerwowego — [PWN Naukowe](https://ksiegarnia.pwn.pl/)",
                            "3. Podręczniki psychologii poznawczej — [PWN Naukowe](https://ksiegarnia.pwn.pl/)",
                            "4. Wprowadzenia do filozofii umysłu i problemu świadomości — [Centrum Kopernika / CCPress](https://ccpress.pl/)",
                        ],
                    },
                    {
                        "heading": "Anglojęzyczne",
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
                "title": "Projekt C — Maszyny analogowe i obliczenia fizyczne (Biblioteka uzupełniająca)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne.",
                "links": [
                    {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika", "url": "https://zpe.gov.pl/"},
                    {"label": "🇵🇱 OpenAGH — E-podręczniki z elektroniki i fizyki", "url": "https://open.agh.edu.pl/"},
                    {"label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering", "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"},
                    {"label": "🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks", "url": "https://arxiv.org/list/cs.NE/recent"},
                    {"label": "🇬🇧 MIT OCW — Circuits & Electronics", "url": "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"}
                ],
                "groups": [
                    {
                        "heading": "Po polsku",
                        "items": [
                            "Podręczniki akademickie z elektroniki analogowej: wzmacniacze, oscylatory, filtry, sprzężenie zwrotne i układy dynamiczne — [E-podręczniki OpenAGH](https://open.agh.edu.pl/)",
                            "Materiały dydaktyczne o przetwornikach analogowo-cyfrowych (ADC) i cyfrowo-analogowych (DAC) — [Materiały ZPE](https://zpe.gov.pl/)",
                            "Zintegrowana Platforma Edukacyjna — punkt wyjścia do szukania materiałów o elektronice: [https://zpe.gov.pl/](https://zpe.gov.pl/)",
                        ],
                    },
                    {
                        "heading": "Po angielsku",
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
                "title": "Projekt D — „Frankenstein”: biotechnologia i tworzenie organizmów (Biblioteka uzupełniająca)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka.",
                "links": [
                    {"label": "🇬🇧 National Academies — Responsible Development of Synthetic Biology", "url": "https://www.nationalacademies.org/"},
                    {"label": "🇬🇧 NCBI Bookshelf — Darmowe podręczniki biologii komórki, genetyki i embriologii", "url": "https://www.ncbi.nlm.nih.gov/books/"},
                    {"label": "🇬🇧 ISSCR — International Society for Stem Cell Research", "url": "https://www.isscr.org/"},
                    {"label": "🇬🇧 Nature Portfolio — Synthetic Biology & Tissue Engineering", "url": "https://www.nature.com/subjects/synthetic-biology"},
                    {"label": "🇵🇱 ZPE — Biologia komórki, genetyka i biotechnologia", "url": "https://zpe.gov.pl/"}
                ],
                "groups": [
                    {
                        "heading": "Po polsku",
                        "items": [
                            "Podręczniki akademickie z biologii komórki, genetyki i biologii rozwoju — [ZPE Biologia](https://zpe.gov.pl/) | [Katalog NUKAT](https://katalogi.bn.org.pl/)",
                            "Podręczniki z embriologii i komórek macierzystych — [PWN Naukowe — Biologia i Medycyna](https://ksiegarnia.pwn.pl/)",
                            "Literatura o inżynierii tkankowej, medycynie regeneracyjnej i bioetyce — [Komitet Bioetyki PAN](https://bioetyka.pan.pl/)",
                        ],
                    },
                    {
                        "heading": "Po angielsku",
                        "items": [
                            "National Academies — materiały o odpowiedzialnym rozwoju biologii syntetycznej: [https://www.nationalacademies.org/](https://www.nationalacademies.org/)",
                            "Publikacje akademickie o stem cells, developmental biology, tissue engineering i synthetic biology — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | [ISSCR](https://www.isscr.org/) | [Nature Synthetic Biology](https://www.nature.com/subjects/synthetic-biology)",
                        ],
                    },
                ],
            },
            {
                "trackId": "E",
                "title": "Projekt E — Filozofia (Biblioteka uzupełniająca)",
                "sequenceLabel": "Zastosowanie",
                "sequence": "Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.",
                "links": [
                    {"label": "🇵🇱 Copernicus Center Press (Michał Heller — Filozofia nauki)", "url": "https://ccpress.pl/"},
                    {"label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (Wykłady i kursy)", "url": "https://www.copernicuscenter.edu.pl/"},
                    {"label": "🇵🇱 Wolne Lektury — Filozofia starożytna (Platon, Arystoteles, stoicy)", "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"},
                    {"label": "🇬🇧 Stanford Encyclopedia of Philosophy (SEP)", "url": "https://plato.stanford.edu/"},
                    {"label": "🇬🇧 Internet Encyclopedia of Philosophy (IEP)", "url": "https://iep.utm.edu/"}
                ],
                "groups": [
                    {
                        "heading": "Po polsku",
                        "items": [
                            "Alan Chalmers — *Czym jest to, co zwiemy nauką?* — [Katalog Biblioteki Narodowej](https://katalogi.bn.org.pl/)",
                            "Thomas S. Kuhn — *Struktura rewolucji naukowych.* — [Wydawnictwo PWN / Aletheia](https://ksiegarnia.pwn.pl/)",
                            "Michał Heller — *Filozofia nauki. Wprowadzenie.* — [Copernicus Center Press](https://ccpress.pl/)",
                        ],
                    },
                    {
                        "heading": "Obszary do dalszego uzupełnienia",
                        "items": [
                            "Filozofia starożytna: Platon, Arystoteles i stoicy — [Wolne Lektury: Filozofia](https://wolnelektury.pl/katalog/gatunek/filozofia/) | [SEP Ancient Philosophy](https://plato.stanford.edu/)",
                            "Filozofia umysłu i problem świadomości — [SEP Philosophy of Mind](https://plato.stanford.edu/entries/mind-identity/) | [Centrum Kopernika](https://www.copernicuscenter.edu.pl/)",
                            "Filozofia techniki, bioetyka i etyka środowiskowa — [SEP Philosophy of Technology](https://plato.stanford.edu/entries/technology/) | [SEP Bioethics](https://plato.stanford.edu/entries/feminist-bioethics/)",
                        ],
                    },
                ],
            },
            {
                "trackId": "F",
                "title": "Projekt F — Człowiek w kosmosie (Biblioteka uzupełniająca)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.",
                "links": [
                    {"label": "🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)", "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"},
                    {"label": "🛰️ ESA — Edukacja kosmiczna (Teach with Space)", "url": "https://education.esa.int/teach-with-space/"},
                    {"label": "👩‍🚀 ESA — Eksploracja załogowa (Human and Robotic Exploration)", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"},
                    {"label": "📑 NASA Technical Reports Server (NTRS — napędy, ECLSS, habitaty)", "url": "https://ntrs.nasa.gov/"},
                    {"label": "🌱 MELiSSA Foundation — Systemy podtrzymywania życia (BLSS)", "url": "https://www.melissafoundation.org/"}
                ],
                "groups": [
                    {
                        "heading": "Darmowe źródła",
                        "items": [
                            "NASA — zdrowie człowieka w kosmosie: [https://www.nasa.gov/reference/fundamentals-of-human-health/](https://www.nasa.gov/reference/fundamentals-of-human-health/)",
                            "ESA — edukacja kosmiczna: [https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)",
                            "ESA — eksploracja załogowa: [https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)",
                        ],
                    },
                    {
                        "heading": "Tematy do dalszego studiowania",
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
                "title": "Projekt G — Człowiek na Ziemi i ochrona ekosystemu (Biblioteka uzupełniająca)",
                "sequenceLabel": "Kolejność nauki",
                "sequence": "Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa.",
                "links": [
                    {"label": "🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska", "url": "https://education.esa.int/teach-with-space/"},
                    {"label": "🇵🇱 Politechnika Śląska — Materiały dotyczące podstaw ochrony środowiska", "url": "https://www.polsl.pl/"},
                    {"label": "🇵🇱 Jan Krystek — Ochrona środowiska dla inżynierów (PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                    {"label": "🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ — Monitoring wód, powietrza i gleb)", "url": "https://www.gios.gov.pl/"},
                    {"label": "🇪🇺 Europejska Agencja Środowiska (EEA — Ekonomia ekologiczna, GOZ, LCA)", "url": "https://www.eea.europa.eu/pl"}
                ],
                "groups": [
                    {
                        "heading": "Po polsku",
                        "items": [
                            "Jan Krystek — *Ochrona środowiska dla inżynierów.* — [Księgarnia Naukowa PWN](https://ksiegarnia.pwn.pl/)",
                            "Podręczniki akademickie z ekologii, ochrony środowiska i gospodarki odpadami — [OpenAGH](https://open.agh.edu.pl/) | [ZPE Ekologia](https://zpe.gov.pl/)",
                            "Materiały polskich uczelni dotyczące ochrony wód, powietrza i gleby — [Politechnika Śląska](https://www.polsl.pl/) | [GIOŚ Monitoring Środowiska](https://www.gios.gov.pl/)",
                        ],
                    },
                    {
                        "heading": "Źródła bezpłatne",
                        "items": [
                            "ESA Education — edukacja o Ziemi, klimacie i obserwacji środowiska: [https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)",
                            "Politechnika Śląska — materiały dotyczące podstaw ochrony środowiska: [https://www.polsl.pl/](https://www.polsl.pl/)",
                        ],
                    },
                    {
                        "heading": "Tematy do dalszego studiowania",
                        "items": [
                            "Ekologia populacji i ekosystemów — [OpenStax Biology: Ecology](https://openstax.org/details/books/biology-2e)",
                            "Różnorodność biologiczna i ochrona siedlisk — [IPBES Global Assessment](https://www.ipbes.net/)",
                            "Obiegi biogeochemiczne i funkcjonowanie gleby — [FAO Soils Portal](https://www.fao.org/soils-portal/en/)",
                            "Zmiany klimatu oraz zanieczyszczenia — [Raporty IPCC](https://www.ipcc.ch/)",
                            "Ochrona przyrody, renaturyzacja i odbudowa ekosystemów — [EEA Nature & Biodiversity](https://www.eea.europa.eu/pl)",
                            "Odnawialne źródła energii i efektywność energetyczna — [IRENA / IEA Renewables](https://www.iea.org/)",
                            "Gospodarka obiegu zamkniętego — [EEA Circular Economy](https://www.eea.europa.eu/pl)",
                            "Ocena cyklu życia produktów (LCA) i ekonomia ekologiczna — [European Platform on LCA](https://eplca.jrc.ec.europa.eu/)",
                            "Monitoring środowiska z użyciem czujników, satelitów i AI — [ESA Copernicus & Earth Online](https://earth.esa.int/)",
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
            "url": "https://plato.stanford.edu/entries/models-science/",
            "links": [
                {"label": "Stanford Encyclopedia of Philosophy — Models in Science", "url": "https://plato.stanford.edu/entries/models-science/"},
                {"label": "SEP — The Chinese Room Argument & Syntax vs Semantics", "url": "https://plato.stanford.edu/entries/chinese-room/"}
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
            "url": "https://doi.org/10.1152/physrev.00027.2016",
            "links": [
                {"label": "Physiological Reviews — Brain-Machine Interfaces (Lebedev & Nicolelis)", "url": "https://doi.org/10.1152/physrev.00027.2016"}
            ],
            "status": "pending",
            "createdAt": "2026-10-25T13:10:00Z",
        },
        {
            "id": "mat-3",
            "trackId": "C",
            "branchTopic": "Elektronika analogowa i układy dynamiczne.",
            "subprojectId": "sub-2",
            "title": "GOLEM 15 — Projekt C: Maszyny analogowe i obliczenia fizyczne (Bibliografia i odnośniki PL/EN)",
            "type": "Biblioteka uzupełniająca GOLEM 15",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne.\n\n"
                "• Po polsku: Podręczniki akademickie z elektroniki analogowej (wzmacniacze, oscylatory, filtry, sprzężenie zwrotne, układy dynamiczne), "
                "materiały dydaktyczne o przetwornikach A/C i C/A oraz Zintegrowana Platforma Edukacyjna.\n"
                "• Po angielsku: Materiały techniczne dot. analog computing, badania dot. neuromorphic computing i analog neural networks, "
                "publikacje o fizycznych modelach neuronów oraz analogowych i hybrydowych procesorach."
            ),
            "url": "https://zpe.gov.pl/",
            "links": [
                {"label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika: https://zpe.gov.pl/", "url": "https://zpe.gov.pl/"},
                {"label": "🇵🇱 OpenAGH — E-podręczniki: Elektronika i układy dynamiczne", "url": "https://open.agh.edu.pl/"},
                {"label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering", "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"},
                {"label": "🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks", "url": "https://arxiv.org/list/cs.NE/recent"},
                {"label": "🇬🇧 MIT OCW — Circuits and Electronics (Analog Computing)", "url": "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:00:00Z",
        },
        {
            "id": "mat-4",
            "trackId": "D",
            "branchTopic": "Biologia syntetyczna i edycja genomu.",
            "subprojectId": None,
            "title": "GOLEM 15 — Projekt D: „Frankenstein” — biotechnologia i tworzenie organizmów (Bibliografia i odnośniki PL/EN)",
            "type": "Biblioteka uzupełniająca GOLEM 15",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka.\n\n"
                "• Po polsku: Podręczniki akademickie z biologii komórki, genetyki i biologii rozwoju; podręczniki z embriologii i komórek macierzystych; "
                "literatura o inżynierii tkankowej, medycynie regeneracyjnej i bioetyce.\n"
                "• Po angielsku: National Academies — materiały o odpowiedzialnym rozwoju biologii syntetycznej; publikacje akademickie o stem cells, "
                "developmental biology, tissue engineering i synthetic biology."
            ),
            "url": "https://www.nationalacademies.org/",
            "links": [
                {"label": "🇬🇧 National Academies — Biologia syntetyczna: https://www.nationalacademies.org/", "url": "https://www.nationalacademies.org/"},
                {"label": "🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell & Developmental Biology", "url": "https://www.ncbi.nlm.nih.gov/books/"},
                {"label": "🇬🇧 ISSCR — International Society for Stem Cell Research (Komórki macierzyste)", "url": "https://www.isscr.org/"},
                {"label": "🇬🇧 Nature Portfolio — Synthetic Biology & Tissue Engineering", "url": "https://www.nature.com/subjects/synthetic-biology"},
                {"label": "🇵🇱 Komitet Bioetyki PAN & ZPE Biologia", "url": "https://bioetyka.pan.pl/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:05:00Z",
        },
        {
            "id": "mat-5",
            "trackId": "E",
            "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "subprojectId": None,
            "title": "GOLEM 15 — Projekt E: Filozofia nauki, umysłu, techniki i bioetyka (Chalmers, Kuhn, Heller + odnośniki)",
            "type": "Biblioteka uzupełniająca GOLEM 15",
            "author": "Administrator",
            "content": (
                "Zastosowanie: Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.\n\n"
                "• Po polsku:\n"
                "  1. Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n"
                "  2. Thomas S. Kuhn — „Struktura rewolucji naukowych”\n"
                "  3. Michał Heller — „Filozofia nauki. Wprowadzenie”\n"
                "• Obszary do dalszego uzupełnienia: Filozofia starożytna (Platon, Arystoteles i stoicy), Filozofia umysłu i problem świadomości, "
                "Filozofia techniki, bioetyka i etyka środowiskowa."
            ),
            "url": "https://ccpress.pl/",
            "links": [
                {"label": "🇵🇱 Copernicus Center Press — Michał Heller „Filozofia nauki. Wprowadzenie”", "url": "https://ccpress.pl/"},
                {"label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych — Wykłady z filozofii nauki i umysłu", "url": "https://www.copernicuscenter.edu.pl/"},
                {"label": "🇵🇱 Wolne Lektury — Filozofia starożytna (Platon, Arystoteles, stoicy)", "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"},
                {"label": "🇬🇧 Stanford Encyclopedia of Philosophy (SEP — Nauka, Umysł, Technika, Bioetyka)", "url": "https://plato.stanford.edu/"},
                {"label": "🇬🇧 Internet Encyclopedia of Philosophy (IEP)", "url": "https://iep.utm.edu/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:10:00Z",
        },
        {
            "id": "mat-6",
            "trackId": "F",
            "branchTopic": "Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.",
            "subprojectId": "sub-3",
            "title": "GOLEM 15 — Projekt F: Człowiek w kosmosie (Darmowe źródła NASA i ESA + tematy badawcze)",
            "type": "Biblioteka uzupełniająca GOLEM 15",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.\n\n"
                "• Darmowe źródła: NASA (zdrowie człowieka w kosmosie), ESA (edukacja kosmiczna — Teach with Space), ESA (eksploracja załogowa i robotyczna).\n"
                "• Tematy do dalszego studiowania: Fizjologia człowieka w mikrograwitacji; Promieniowanie kosmiczne i ochrona biologiczna; "
                "Mechanika orbitalna i napędy; Systemy podtrzymywania życia; Projektowanie habitatów i statków kosmicznych; "
                "Uprawa żywności, odzysk wody i wykorzystanie zasobów lokalnych; Psychologia izolacji i medycyna długotrwałych misji."
            ),
            "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/",
            "links": [
                {"label": "🚀 NASA — Zdrowie człowieka w kosmosie: https://www.nasa.gov/reference/fundamentals-of-human-health/", "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"},
                {"label": "🛰️ ESA — Edukacja kosmiczna: https://education.esa.int/teach-with-space/", "url": "https://education.esa.int/teach-with-space/"},
                {"label": "👩‍🚀 ESA — Eksploracja załogowa: https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"},
                {"label": "📑 NASA Technical Reports Server (NTRS — napędy, ECLSS, habitaty)", "url": "https://ntrs.nasa.gov/"},
                {"label": "🌱 MELiSSA Foundation — Zamknięte systemy podtrzymywania życia", "url": "https://www.melissafoundation.org/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:15:00Z",
        },
        {
            "id": "mat-7",
            "trackId": "G",
            "branchTopic": "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.",
            "subprojectId": "sub-3",
            "title": "GOLEM 15 — Projekt G: Człowiek na Ziemi i ochrona ekosystemu (Krystek, Politechnika Śląska, ESA Education)",
            "type": "Biblioteka uzupełniająca GOLEM 15",
            "author": "Administrator",
            "content": (
                "Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa.\n\n"
                "• Po polsku: Jan Krystek — „Ochrona środowiska dla inżynierów”; podręczniki akademickie z ekologii, ochrony środowiska i gospodarki odpadami; "
                "materiały polskich uczelni dotyczące ochrony wód, powietrza i gleby.\n"
                "• Źródła bezpłatne: ESA Education (Ziemia, klimat, obserwacja środowiska), Politechnika Śląska (podstawy ochrony środowiska).\n"
                "• Tematy do dalszego studiowania: Ekologia populacji i ekosystemów; Różnorodność biologiczna i ochrona siedlisk; "
                "Obiegi biogeochemiczne i funkcjonowanie gleby; Zmiany klimatu oraz zanieczyszczenia; Ochrona przyrody, renaturyzacja i odbudowa ekosystemów; "
                "Odnawialne źródła energii i efektywność energetyczna; Gospodarka obiegu zamkniętego; Ocena cyklu życia produktów (LCA) i ekonomia ekologiczna; "
                "Monitoring środowiska z użyciem czujników, satelitów i AI."
            ),
            "url": "https://www.polsl.pl/",
            "links": [
                {"label": "🌍 ESA Education — Ziemia, klimat i obserwacja środowiska: https://education.esa.int/teach-with-space/", "url": "https://education.esa.int/teach-with-space/"},
                {"label": "🇵🇱 Politechnika Śląska — Podstawy ochrony środowiska: https://www.polsl.pl/", "url": "https://www.polsl.pl/"},
                {"label": "🇵🇱 Jan Krystek — „Ochrona środowiska dla inżynierów” (Księgarnia PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 GIOŚ — Państwowy Monitoring Środowiska (wody, powietrze, gleby)", "url": "https://www.gios.gov.pl/"},
                {"label": "🇪🇺 Europejska Agencja Środowiska (EEA) & Copernicus Earth Observation", "url": "https://www.eea.europa.eu/pl"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T14:20:00Z",
        },
        {
            "id": "mat-8",
            "trackId": "B",
            "branchTopic": "Modelowanie neuronów i sieci neuronalnych.",
            "subprojectId": "sub-1",
            "title": "BIBLIOTEKA PROJEKTU — I. Matematyka i Informatyka (Petzold, Matthes, Strang + podręczniki PL/EN)",
            "type": "Biblioteka Projektu GOLEM 15",
            "author": "Administrator",
            "content": (
                "Polskojęzyczne:\n"
                "1. Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II.”\n"
                "2. Eric Matthes — „Python. Instrukcje dla programisty.”\n"
                "3. Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów.\n\n"
                "Anglojęzyczne:\n"
                "4. Gilbert Strang — „Introduction to Linear Algebra.”\n"
                "5. Charles Petzold — „Code: The Hidden Language of Computer Hardware and Software.”\n"
                "6. Eric Matthes — „Python Crash Course.”"
            ),
            "url": "https://math.mit.edu/~gs/linearalgebra/",
            "links": [
                {"label": "🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 Eric Matthes — „Python. Instrukcje dla programisty” (Helion)", "url": "https://helion.pl/"},
                {"label": "🇵🇱 OpenAGH — E-podręczniki: Matematyka i Algebra Liniowa po polsku", "url": "https://open.agh.edu.pl/"},
                {"label": "🇬🇧 Gilbert Strang — „Introduction to Linear Algebra” & MIT 18.06", "url": "https://math.mit.edu/~gs/linearalgebra/"},
                {"label": "🇬🇧 Charles Petzold — „Code” (Oficjalna strona autora)", "url": "https://codehiddenlanguage.com/"},
                {"label": "🇬🇧 Eric Matthes — „Python Crash Course” (No Starch Press & GitHub)", "url": "https://nostarch.com/python-crash-course-3rd-edition"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:00:00Z",
        },
        {
            "id": "mat-9",
            "trackId": "C",
            "branchTopic": "Komputery analogowe i mechaniczne.",
            "subprojectId": "sub-2",
            "title": "BIBLIOTEKA PROJEKTU — II. Fizyka i Komputery Kwantowe (Griffiths, Nielsen & Chuang + elektronika)",
            "type": "Biblioteka Projektu GOLEM 15",
            "author": "Administrator",
            "content": (
                "Polskojęzyczne:\n"
                "1. Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach.\n"
                "2. Podręczniki podstaw elektroniki i układów cyfrowych.\n\n"
                "Anglojęzyczne:\n"
                "3. David J. Griffiths — „Introduction to Quantum Mechanics.”\n"
                "4. Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information.”"
            ),
            "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E",
            "links": [
                {"label": "🇵🇱 OpenStax Polska — Fizyka dla szkół wyższych (Tomy 1–3, darmowy podręcznik PL)", "url": "https://openstax.org/subjects/science"},
                {"label": "🇵🇱 Wydawnictwo Naukowe PWN — Fizyka ogólna, mechanika kwantowa i układy cyfrowe", "url": "https://ksiegarnia.pwn.pl/"},
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
            "title": "BIBLIOTEKA PROJEKTU — III. Chemia, Biologia i Genetyka (Brown „Genomy”, Biologia Campbella, OpenStax 2e)",
            "type": "Biblioteka Projektu GOLEM 15",
            "author": "Administrator",
            "content": (
                "Polskojęzyczne:\n"
                "1. Terence A. Brown — „Genomy.”\n"
                "2. „Biologia Campbella” — polskie wydanie.\n"
                "3. Akademickie podręczniki chemii ogólnej, organicznej i biochemii.\n\n"
                "Anglojęzyczne:\n"
                "4. OpenStax „Chemistry 2e” — podręcznik chemii ogólnej.\n"
                "5. OpenStax „Biology 2e” — podręcznik biologii.\n"
                "6. Akademickie podręczniki biochemii i biologii molekularnej."
            ),
            "url": "https://openstax.org/details/books/biology-2e",
            "links": [
                {"label": "🇵🇱 Terence A. Brown — „Genomy” (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)", "url": "https://www.rebis.com.pl/"},
                {"label": "🇬🇧 OpenStax „Chemistry 2e” — darmowy podręcznik chemii ogólnej online", "url": "https://openstax.org/details/books/chemistry-2e"},
                {"label": "🇬🇧 OpenStax „Biology 2e” — darmowy podręcznik biologii online", "url": "https://openstax.org/details/books/biology-2e"},
                {"label": "🇬🇧 NCBI Bookshelf — Genomes (T.A. Brown) & Molecular Biology of the Cell", "url": "https://www.ncbi.nlm.nih.gov/books/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:10:00Z",
        },
        {
            "id": "mat-11",
            "trackId": "A",
            "branchTopic": "Interfejsy mózg–komputer.",
            "subprojectId": "sub-1",
            "title": "BIBLIOTEKA PROJEKTU — IV. Projekt A: Człowiek biocyfrowo-robotyczny (Kalat, OpenStax Anatomy 2e, Géron)",
            "type": "Biblioteka Projektu GOLEM 15",
            "author": "Administrator",
            "content": (
                "Polskojęzyczne:\n"
                "1. James W. Kalat — „Biologiczne podstawy psychologii.”\n"
                "2. Akademickie podręczniki anatomii i fizjologii człowieka.\n"
                "3. Akademickie podręczniki biofizyki, biomechaniki i biomateriałów.\n"
                "4. Podręczniki robotyki, elektroniki i układów sterowania.\n\n"
                "Anglojęzyczne:\n"
                "5. OpenStax „Anatomy and Physiology 2e.”\n"
                "6. Aurélien Géron — „Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.”\n"
                "7. Akademickie podręczniki inżynierii tkankowej, neuroprotetyki i interfejsów mózg–komputer."
            ),
            "url": "https://openstax.org/details/books/anatomy-and-physiology-2e",
            "links": [
                {"label": "🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 OpenStax „Anatomy and Physiology 2e” — darmowy podręcznik online", "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"},
                {"label": "🇬🇧 Aurélien Géron — „Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow”", "url": "https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/"},
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
            "title": "BIBLIOTEKA PROJEKTU — V. Projekt B: Cyfrowy umysł (Kalat, Kandel, Squire, Dayan & Abbott, Izhikevich, Seung, Miller, Churchland & Sejnowski, Sandberg & Bostrom)",
            "type": "Biblioteka Projektu GOLEM 15",
            "author": "Administrator",
            "content": (
                "Polskojęzyczne:\n"
                "1. James W. Kalat — „Biologiczne podstawy psychologii.”\n"
                "2. Podręczniki neurobiologii i fizjologii układu nerwowego.\n"
                "3. Podręczniki psychologii poznawczej.\n"
                "4. Wprowadzenia do filozofii umysłu i problemu świadomości.\n\n"
                "Anglojęzyczne:\n"
                "5. Eric R. Kandel i współautorzy — „Principles of Neural Science.”\n"
                "6. Larry Squire i współautorzy — „Fundamental Neuroscience.”\n"
                "7. Peter Dayan, L. F. Abbott — „Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems.”\n"
                "8. Eugene M. Izhikevich — „Dynamical Systems in Neuroscience.”\n"
                "9. Sebastian Seung — „Connectome: How the Brain's Wiring Makes Us Who We Are.”\n"
                "10. Paul Miller — „An Introductory Course in Computational Neuroscience.”\n"
                "11. Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain.”\n"
                "12. Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap.”"
            ),
            "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/",
            "links": [
                {"label": "🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (PWN)", "url": "https://ksiegarnia.pwn.pl/"},
                {"label": "🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” (McGraw Hill)", "url": "https://www.mheducation.com/"},
                {"label": "🇬🇧 Larry Squire et al. — „Fundamental Neuroscience” (Academic Press)", "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"},
                {"label": "🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)", "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"},
                {"label": "🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (MIT Press / PDF autora)", "url": "https://www.izhikevich.org/publications/dsn.htm"},
                {"label": "🇬🇧 Paul Miller — „An Introductory Course in Computational Neuroscience” (MIT Press)", "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"},
                {"label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain” (MIT Press)", "url": "https://mitpress.mit.edu/9780262533393/the-computational-brain/"},
                {"label": "🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Technical Report PDF)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:20:00Z",
        },
        {
            "id": "mat-13",
            "trackId": "E",
            "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
            "subprojectId": None,
            "title": "BIBLIOTEKA PROJEKTU — VI. Kolejność czytania i zasady pracy z literaturą",
            "type": "Przewodnik metodologiczny GOLEM 15",
            "author": "Administrator",
            "content": (
                "1. Najpierw: Petzold — Kod; Matthes — Python. Instrukcje dla programisty; Podstawy matematyki; Podręcznik fizyki ogólnej.\n"
                "2. Następnie: Brown — Genomy; Podstawy chemii, biologii i biochemii; Kalat — Biologiczne podstawy psychologii.\n"
                "3. Później: Theoretical Neuroscience; Dynamical Systems in Neuroscience; Connectome; Whole Brain Emulation: A Roadmap.\n"
                "4. Na zaawansowanym etapie: Principles of Neural Science; Fundamental Neuroscience; The Computational Brain; "
                "Griffiths — Introduction to Quantum Mechanics; Nielsen i Chuang — Quantum Computation and Quantum Information.\n\n"
                "Zasada: Najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja. "
                "Pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi."
            ),
            "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf",
            "links": [
                {"label": "1️⃣ Etap I: Petzold — Code / Kod. Ukryty język komputerów", "url": "https://codehiddenlanguage.com/"},
                {"label": "2️⃣ Etap II: OpenStax — Chemistry 2e & Biology 2e + Brown (Genomy)", "url": "https://openstax.org/subjects/science"},
                {"label": "3️⃣ Etap III: Dayan & Abbott (Theoretical Neuroscience) + Sandberg & Bostrom (WBE Roadmap)", "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"},
                {"label": "4️⃣ Etap IV: Kandel (Principles of Neural Science) + Nielsen & Chuang (Quantum Computation)", "url": "https://mitpress.mit.edu/9780262533393/the-computational-brain/"}
            ],
            "status": "approved",
            "createdAt": "2026-10-25T15:25:00Z",
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
    """Upewnia się, że baza zawiera nową nazwę oraz sekcje foundationDisciplines, studyMaterials, supplementaryLibrary i materials."""
    data["projectMeta"]["title"] = "The Golem 15: A Human's Road to Reality"
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
    "🎓 1. Materiały do nauki (Dziedziny i Biblioteka)",
    "🗺️ 2. Mapa 7 Ścieżek (Projekty A–G)",
    f"🔬 3. Środowiska Badawcze ({len(db['subprojects'])})",
    f"📚 4. Repozytorium Badawcze ({len(db['materials'])})",
    "🚀 5. + Uruchom Środowisko / Dodaj Materiał",
    "🕸️ 6. Graf Powiązań (A–G)",
    f"🛡️ 7. Autoryzacja Administratora ({pending_count})",
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
                        sm_author = st.text_input("Dodał(a)", value="Administrator" if st.session_state.is_admin else "Gość / Obserwator")
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
                                    "status": "approved" if st.session_state.is_admin else "pending",
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
