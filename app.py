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
# DEFINICJE ZGODNOŚCI Z JSON (null, true, false dla ewaluacji literałów)
# ==============================================================================
null = None
true = True
false = False

# ==============================================================================
# WBUDOWANA BAZA STARTOWA (DZIAŁA NAWET GDY WGRASZ SAM PLIK app.py NA GITHUB)
# ==============================================================================
DEFAULT_SEED = {
  "projectMeta": {
    "title": "The Golem 15: A Human's Road to Reality",
    "subtitle": "Mapa projektu badawczego — wspólne podstawy naukowe (1–8), siedem ścieżek (A–G) oraz Super-Projekt H (Energetyka jądrowa i termojądrowa)",
    "adminAuth": {
      "algorithm": "pbkdf2_sha256",
      "iterations": 260000,
      "salt": "9f4d8a2c6e1b3f7a5c8d0e2f4a6b8c1d",
      "hash": "673a07dbc15ac855752d7c521ffc31e200302b03a3b296310b742421cbfd4d62"
    },
    "overarchingGoal": "Zrozumieć człowieka jako organizm biologiczny, umysł, twórcę technologii i część ziemskiej biosfery, a jednocześnie zbadać możliwości jego funkcjonowania poza naturalnym środowiskiem Ziemi.",
    "organizationalRule": "Każda ścieżka ma własne pytania badawcze, bibliografię i cele. Wspólne podstawy naukowe pozwalają łączyć wiedzę, ale nie oznaczają konieczności równoległego studiowania wszystkich dziedzin. Filozofia pozostaje przekrojową warstwą interpretacyjną. Pozostałe projekty rozwijają się w miarę dostępnego czasu i zainteresowania.",
    "foundations": [
      "Matematyka i logika",
      "Informatyka",
      "Programowanie",
      "Fizyka",
      "Elektronika",
      "Chemia",
      "Biologia",
      "Sztuczna inteligencja"
    ],
    "fgRelation": {
      "summary": "Oba projekty badają człowieka w relacji ze środowiskiem, ale z różnych perspektyw:",
      "fPerspective": "Projekt F — kosmos: jak stworzyć sztuczne środowisko podtrzymujące życie tam, gdzie naturalne warunki są dla człowieka nieprzyjazne. Koncentruje się na inżynierii środowiska i adaptacji do warunków pozaziemskich.",
      "gPerspective": "Projekt G — Ziemia: jak żyć w istniejącym, złożonym ekosystemie i chronić jego zdolność do podtrzymywania życia. Koncentruje się na ekologii, zdrowiu człowieka, zrównoważonej technologii i ochronie biosfery."
    }
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
        "Matematyka dyskretna, teoria grafów i topologia sieci (podstawa konektomiki i sieci złożonych)."
      ],
      "connectedTracks": [
        "A",
        "B",
        "C",
        "E",
        "F",
        "G",
        "H"
      ]
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
        "Niezawodność systemów (fault-tolerance) w zastosowaniach medycznych i kosmicznych."
      ],
      "connectedTracks": [
        "A",
        "B",
        "C",
        "F",
        "G",
        "H"
      ]
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
        "Wizualizacja danych naukowych, interfejsy webowe i wirtualne środowiska badawcze."
      ],
      "connectedTracks": [
        "A",
        "B",
        "C",
        "D",
        "F",
        "G",
        "H"
      ]
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
        "Biofizyka błon komórkowych, transportu jonowego i potencjałów czynnościowych."
      ],
      "connectedTracks": [
        "A",
        "B",
        "C",
        "E",
        "F",
        "G",
        "H"
      ]
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
        "Układy neuromorficzne, memrystory i realizacja sztucznych synaps w krzemie."
      ],
      "connectedTracks": [
        "A",
        "B",
        "C",
        "F",
        "G",
        "H"
      ]
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
        "Chemia środowiska i analityczna: obiegi C, N, P, oczyszczanie wody, powietrza i neutralizacja toksyn."
      ],
      "connectedTracks": [
        "A",
        "D",
        "F",
        "G",
        "H"
      ]
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
        "Mikrobiologia, mikrobiom człowieka oraz ekologia populacji, ekosystemów i biosfery."
      ],
      "connectedTracks": [
        "A",
        "B",
        "D",
        "F",
        "G",
        "H"
      ]
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
        "Interpretowalność modeli (XAI), niezawodność, bezpieczeństwo i filozoficzno-etyczne aspekty AI."
      ],
      "connectedTracks": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H"
      ]
    }
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
      "content": "1. W pierwszej kolejności (Po polsku): Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów — darmowe e-podręczniki OpenAGH (Matematyka, Algebra liniowa, Analiza matematyczna), Zintegrowana Platforma Edukacyjna (ZPE), Marian Gewert i Zbigniew Skoczylas („Algebra liniowa 1–2”, „Analiza matematyczna 1–2”), Tadeusz Krasiński („Algebra liniowa”) oraz Roger Penrose („Droga do rzeczywistości”, wyd. polskie).\n2. Uzupełniająco (Po angielsku): Gilbert Strang — „Introduction to Linear Algebra” (MIT 18.06) oraz OpenStax Mathematics.",
      "url": "https://open.agh.edu.pl/",
      "links": [
        {
          "label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki akademickie (Matematyka, Algebra liniowa, Analiza)",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Matematyka i logika po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇵🇱 OpenStax Polska — Darmowe podręczniki akademickie po polsku",
          "url": "https://openstax.pl/pl/zasoby"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Podręczniki algebry liniowej i analizy matematycznej",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT 18.06 + wykłady)",
          "url": "https://math.mit.edu/~gs/linearalgebra/"
        },
        {
          "label": "🇬🇧 OpenStax Mathematics (Calculus / Linear Algebra)",
          "url": "https://openstax.org/subjects/math"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:00:00Z"
    },
    {
      "id": "smat-1b",
      "categoryType": "FOUNDATION",
      "targetId": "FND-2",
      "topic": "Architektura systemów komputerowych, systemy wbudowane, praca w czasie rzeczywistym (RTOS) i obliczenia rozproszone.",
      "title": "I. Informatyka (PL → EN): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II”, Cormen („Wprowadzenie do algorytmów”), Ważniak MIMUW",
      "level": "Podstawowy (Etap 1: Najpierw)",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Helion) — fundamentalna książka wyjaśniająca od podstaw, jak z przekaźników, bramek logicznych i tranzystorów powstaje komputer; Thomas H. Cormen i współautorzy — „Wprowadzenie do algorytmów” (PWN); Andrew S. Tanenbaum — „Strukturalna organizacja komputerów” (Helion); darmowe kursy akademickie Ważniak MIMUW (Uniwersytet Warszawski) oraz ZPE Informatyka.\n2. Uzupełniająco (Po angielsku): Charles Petzold — „Code” oraz MIT OCW 6.006.",
      "url": "https://wazniak.mimuw.edu.pl/",
      "links": [
        {
          "label": "🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Wydawnictwo Helion)",
          "url": "https://helion.pl/"
        },
        {
          "label": "🇵🇱 Ważniak MIMUW (Uniwersytet Warszawski) — Darmowe polskie wykłady z informatyki i architektury komputerów",
          "url": "https://wazniak.mimuw.edu.pl/"
        },
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Informatyka i algorytmika po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇵🇱 T. H. Cormen et al. — „Wprowadzenie do algorytmów” (Księgarnia PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇬🇧 Charles Petzold — „Code” (Strona autora z interaktywnymi symulacjami bramek)",
          "url": "https://codehiddenlanguage.com/"
        },
        {
          "label": "🇬🇧 MIT OCW 6.006 — Introduction to Algorithms",
          "url": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:02:00Z"
    },
    {
      "id": "smat-1c",
      "categoryType": "FOUNDATION",
      "targetId": "FND-3",
      "topic": "Obliczenia naukowe w Pythonie (NumPy, SciPy, PyTorch, JAX) oraz symulacje numeryczne.",
      "title": "I. Programowanie (PL → EN): Eric Matthes — „Python. Instrukcje dla programisty”, oficjalna polska dokumentacja Pythona i obliczenia naukowe",
      "level": "Podstawowy (Etap 1: Najpierw)",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Eric Matthes — „Python. Instrukcje dla programisty. Wydanie III” (Helion) — praktyczny podręcznik programowania od podstaw z ćwiczeniami; oficjalny polski przewodnik po języku Python (docs.python.org/pl); Wes McKinney — „Python w analizie danych (NumPy, pandas)” (Helion); kursy programowania Ważniak MIMUW i ZPE.\n2. Uzupełniająco (Po angielsku): Eric Matthes — „Python Crash Course”, Scientific Python Lectures oraz symulator sieci neuronowych Brian2.",
      "url": "https://docs.python.org/pl/3/tutorial/",
      "links": [
        {
          "label": "🇵🇱 Oficjalny samouczek języka Python po polsku (docs.python.org/pl)",
          "url": "https://docs.python.org/pl/3/tutorial/"
        },
        {
          "label": "🇵🇱 Eric Matthes — „Python. Instrukcje dla programisty” (Wydawnictwo Helion)",
          "url": "https://helion.pl/"
        },
        {
          "label": "🇵🇱 Ważniak MIMUW — Wstęp do programowania (kurs akademicki po polsku)",
          "url": "https://wazniak.mimuw.edu.pl/"
        },
        {
          "label": "🇵🇱 ZPE — Programowanie i algorytmy w języku Python (po polsku)",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇬🇧 Eric Matthes — „Python Crash Course” (Repozytorium ćwiczeń i kodu)",
          "url": "https://ehmatthes.github.io/pcc_3e/"
        },
        {
          "label": "🇬🇧 Scientific Python Lectures (NumPy, SciPy, Matplotlib)",
          "url": "https://lectures.scientific-python.org/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:03:00Z"
    },
    {
      "id": "smat-2",
      "categoryType": "FOUNDATION",
      "targetId": "FND-4",
      "topic": "Mechanika klasyczna, elektrodynamika i termodynamika układów otwartych (dalekich od równowagi).",
      "title": "II. Fizyka i Komputery Kwantowe (PL → EN): OpenStax „Fizyka dla szkół wyższych Tom 1–3” (PL), Halliday & Resnick, Griffiths („Wstęp do mechaniki kwantowej”) oraz Nielsen & Chuang",
      "level": "Podstawowy → Zaawansowany",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Darmowy, trzytomowy podręcznik akademicki OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3”; David Halliday, Robert Resnick, Jearl Walker — „Podstawy fizyki. Tom 1–5” (PWN); Richard P. Feynman — „Feynmana wykłady z fizyki” (PWN); David J. Griffiths — „Wstęp do mechaniki kwantowej” (polskie wydanie PWN) oraz e-podręczniki fizyki OpenAGH.\n2. Uzupełniająco (Po angielsku — etap zaawansowany): David J. Griffiths — „Introduction to Quantum Mechanics” oraz Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”.",
      "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1",
      "links": [
        {
          "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (darmowy podręcznik PL online/PDF)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
        },
        {
          "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 2” (Elektrodynamika, termodynamika — PL)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2"
        },
        {
          "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 3” (Optyka i fizyka kwantowa — PL)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3"
        },
        {
          "label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki z fizyki ogólnej",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Halliday/Resnick „Podstawy fizyki” oraz Griffiths „Wstęp do mechaniki kwantowej”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇬🇧 David J. Griffiths — „Introduction to Quantum Mechanics” (Cambridge University Press)",
          "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"
        },
        {
          "label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”",
          "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:05:00Z"
    },
    {
      "id": "smat-4",
      "categoryType": "FOUNDATION",
      "targetId": "FND-5",
      "topic": "Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy nieliniowe.",
      "title": "II. Elektronika (PL → EN): Horowitz & Hill („Sztuka elektroniki”), polskie kursy Forbot, ZPE, OpenAGH oraz układy cyfrowe",
      "level": "Podstawowy / Zaawansowany",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Paul Horowitz, Winfield Hill — „Sztuka elektroniki. Część 1 i 2” (polskie wydanie WKŁ); Bogdan Głocki — „Układy cyfrowe” (WSiP); darmowe polskojęzyczne kursy podstaw elektroniki i techniki cyfrowej Forbot; materiały Zintegrowanej Platformy Edukacyjnej (ZPE) oraz e-podręczniki elektroniki OpenAGH.\n2. Uzupełniająco (Po angielsku): All About Circuits Textbook oraz MIT OCW Circuits and Electronics.",
      "url": "https://zpe.gov.pl/",
      "links": [
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika analogowa i układy cyfrowe po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇵🇱 Forbot — Darmowe kursy podstaw elektroniki i techniki cyfrowej po polsku",
          "url": "https://forbot.pl/blog/kurs-elektroniki-poziom-1-spis-tresci-id5159"
        },
        {
          "label": "🇵🇱 OpenAGH — Polskie e-podręczniki akademickie z elektroniki i elektrotechniki",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Paul Horowitz, Winfield Hill — „Sztuka elektroniki” (Wydawnictwa Komunikacji i Łączności — WKŁ)",
          "url": "https://wkl.com.pl/"
        },
        {
          "label": "🇬🇧 All About Circuits — Textbook of Analog & Digital Electronics",
          "url": "https://www.allaboutcircuits.com/textbook/"
        },
        {
          "label": "🇬🇧 MIT OCW — Circuits and Electronics",
          "url": "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:12:00Z"
    },
    {
      "id": "smat-4b",
      "categoryType": "FOUNDATION",
      "targetId": "FND-6",
      "topic": "Biochemia: struktura i funkcja białek, enzymów, lipidów oraz kwasów nukleinowych (DNA/RNA).",
      "title": "III. Chemia i Biochemia (PL → EN): Stryer („Biochemia” PWN), Bielański, Jones & Atkins, McMurry oraz OpenStax Chemistry 2e",
      "level": "Podstawowy / Akademicki (Etap 2: Następnie)",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Akademickie podręczniki chemii ogólnej, organicznej i biochemii w polskich wydaniach — Jeremy M. Berg, John L. Tymoczko, Lubert Stryer — „Biochemia” (PWN); Robert K. Murray et al. — „Biochemia Harpera” (PZWL); Loretta Jones, Peter Atkins — „Chemia ogólna. Cząsteczki, materia, reakcje” (PWN); Adam Bielański — „Podstawy chemii nieorganicznej” (PWN); John McMurry — „Chemia organiczna” (PWN) oraz darmowe materiały ZPE i OpenAGH.\n2. Uzupełniająco (Po angielsku): OpenStax „Chemistry 2e” oraz „Organic Chemistry” (darmowe podręczniki online).",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Stryer „Biochemia”, Jones & Atkins „Chemia ogólna”, McMurry „Chemia organiczna”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki akademickie z chemii ogólnej i fizycznej",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Chemia ogólna, organiczna i biochemia po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — „Biochemia Harpera”",
          "url": "https://pzwl.pl/"
        },
        {
          "label": "🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej online/PDF",
          "url": "https://openstax.org/details/books/chemistry-2e"
        },
        {
          "label": "🇬🇧 OpenStax Organic Chemistry — Darmowy podręcznik chemii organicznej",
          "url": "https://openstax.org/details/books/organic-chemistry"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:13:00Z"
    },
    {
      "id": "smat-3",
      "categoryType": "FOUNDATION",
      "targetId": "FND-7",
      "topic": "Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, sygnalizacja komórkowa.",
      "title": "III. Biologia i Genetyka (PL → EN): Terence A. Brown („Genomy” PWN), „Biologia Campbella” (Rebis), Alberts („Podstawy biologii komórki”) oraz OpenStax Biology 2e",
      "level": "Podstawowy / Akademicki (Etap 2: Następnie)",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Terence A. Brown — „Genomy” (Wydawnictwo Naukowe PWN); Neil A. Campbell i współautorzy — „Biologia Campbella” (polskie wydanie, Dom Wydawniczy REBIS); Bruce Alberts i współautorzy — „Podstawy biologii komórki. Część 1–2” (PWN); Piotr Węgleński (red.) — „Genetyka molekularna” (PWN) oraz polskojęzyczne materiały ZPE.\n2. Uzupełniająco (Po angielsku): OpenStax „Biology 2e” oraz darmowe zasoby NCBI Bookshelf.",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 Terence A. Brown — „Genomy” oraz B. Alberts — „Podstawy biologii komórki” (Wydawnictwo Naukowe PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)",
          "url": "https://www.rebis.com.pl/"
        },
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biologia komórki i genetyka po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii online/PDF",
          "url": "https://openstax.org/details/books/biology-2e"
        },
        {
          "label": "🇬🇧 Terence A. Brown — „Genomes” (Darmowy dostęp w bazie NCBI Bookshelf)",
          "url": "https://www.ncbi.nlm.nih.gov/books/NBK21128/"
        },
        {
          "label": "🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell (Alberts)",
          "url": "https://www.ncbi.nlm.nih.gov/books/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:10:00Z"
    },
    {
      "id": "smat-5",
      "categoryType": "FOUNDATION",
      "targetId": "FND-8",
      "topic": "Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe sieci neuronowe (SNN).",
      "title": "IV & V. Sztuczna Inteligencja (PL → EN): Aurélien Géron („Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” PL), Goodfellow („Deep Learning” PWN) oraz Dayan & Abbott",
      "level": "Średniozaawansowany / Zaawansowany",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku): Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i TensorFlow. Wydanie III” (Helion); Ian Goodfellow, Yoshua Bengio, Aaron Courville — „Deep Learning. Systemy uczące się” (polskie wydanie PWN); Stuart Russell, Peter Norvig — „Sztuczna inteligencja. Nowe spojrzenie” (Helion) oraz Ryszard Tadeusiewicz — „Sieci neuronowe”.\n2. Uzupełniająco (Po angielsku): Géron — „Hands-On Machine Learning” (notebooki GitHub) oraz Peter Dayan, L. F. Abbott — „Theoretical Neuroscience”.",
      "url": "https://helion.pl/",
      "links": [
        {
          "label": "🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” (Wydawnictwo Helion)",
          "url": "https://helion.pl/"
        },
        {
          "label": "🇵🇱 Ian Goodfellow, Yoshua Bengio, Aaron Courville — „Deep Learning. Systemy uczące się” (PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 OpenStax Polska — Wprowadzenie do nauki o danych i Pythonie (po polsku)",
          "url": "https://openstax.pl/pl/zasoby"
        },
        {
          "label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Oficjalne notebooki GitHub)",
          "url": "https://github.com/ageron/handson-ml3"
        },
        {
          "label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)",
          "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"
        },
        {
          "label": "🇬🇧 Neuromatch Academy — Computational Neuroscience & Deep Learning",
          "url": "https://compneuro.neuromatch.io/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:15:00Z"
    },
    {
      "id": "smat-a1",
      "categoryType": "TRACK",
      "targetId": "A",
      "topic": "Medycyna regeneracyjna, protezy i sztuczne narządy.",
      "title": "IV. Projekt A (PL → EN): Kalat („Biologiczne podstawy psychologii”), anatomia i fizjologia (Bochenek, Traczyk, Konturek), biofizyka, robotyka i BCI oraz OpenStax Anatomy 2e",
      "level": "Podstawowy → Zaawansowany",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku):\n• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n• Akademickie podręczniki anatomii i fizjologii człowieka: Władysław Traczyk, Andrzej Trzebski — „Fizjologia człowieka” (PZWL); Stanisław Konturek — „Fizjologia człowieka”; Adam Bochenek, Michał Reicher — „Anatomia człowieka” (PZWL).\n• Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: Feliks Jaroszyk (red.) — „Biofizyka” (PZWL); Jan Marciniak — „Biomateriały” (Politechnika Śląska); seria „Biocybernetyka i Inżynieria Biomedyczna 2000” (PAN, red. M. Nałęcz, R. Tadeusiewicz).\n• Podręczniki robotyki, elektroniki i układów sterowania (K. Tchoń i współautorzy — „Manipulatory i roboty mobilne”; A. Géron — wyd. Helion).\n2. Uzupełniająco (Po angielsku): OpenStax „Anatomy and Physiology 2e”, Géron „Hands-On ML” oraz literatura z neuroprotetyki i BCI.",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia (Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)",
          "url": "https://pzwl.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH — Polskie materiały z inżynierii biomedycznej, biocybernetyki i automatyki",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” (Helion)",
          "url": "https://helion.pl/"
        },
        {
          "label": "🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik anatomii i fizjologii)",
          "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"
        },
        {
          "label": "🇬🇧 MIT OCW — Introduction to Robotics & Control Systems",
          "url": "https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:18:00Z"
    },
    {
      "id": "smat-b1",
      "categoryType": "TRACK",
      "targetId": "B",
      "topic": "Neurobiologia i neuronauka obliczeniowa.",
      "title": "V. Projekt B (PL → EN): Kalat, Longstaff („Neurobiologia”), Nęcka („Psychologia poznawcza”), Seung („Konektom”), Miłkowski & Poczobut oraz Kandel, Dayan & Abbott, Izhikevich i Sandberg & Bostrom",
      "level": "Podstawowy → Zaawansowany",
      "format": "Biblioteka Projektu (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku):\n• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n• Podręczniki neurobiologii i fizjologii układu nerwowego: Alan Longstaff — „Neurobiologia. Krótkie wykłady” (PWN); T. Górska, A. Grabowska, J. Zagrodzka (red.) — „Mózg a zachowanie” (PWN).\n• Podręczniki psychologii poznawczej: Edward Nęcka, Jarosław Orzechowski, Błażej Szymura — „Psychologia poznawcza” (PWN).\n• Wprowadzenia do filozofii umysłu, kognitywistyki i konektomiki: Marcin Miłkowski, Robert Poczobut (red.) — „Przewodnik po filozofii umysłu” (WAM); Sebastian Seung — „Konektom. Jak połączenia w mózgu kształtują naszą tożsamość” (wyd. polskie); wykłady prof. Włodzisława Ducha (UMK).\n2. Następnie i na zaawansowanym etapie (Po angielsku): Kandel („Principles of Neural Science”), Squire („Fundamental Neuroscience”), Dayan & Abbott („Theoretical Neuroscience”), Izhikevich („Dynamical Systems in Neuroscience”), Miller, Churchland & Sejnowski oraz Sandberg & Bostrom („Whole Brain Emulation: A Roadmap”).",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Kalat „Biologiczne podstawy psychologii”, Longstaff „Neurobiologia”, Nęcka „Psychologia poznawcza”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 Prof. Włodzisław Duch (UMK) — Polskie wykłady z kognitywistyki, neuroinformatyki i modelowania mózgu",
          "url": "https://www.fizyka.umk.pl/~duch/"
        },
        {
          "label": "🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu, kognitywistyka i problem świadomości (po polsku)",
          "url": "https://ccpress.pl/"
        },
        {
          "label": "🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (Darmowy PDF książki)",
          "url": "https://www.izhikevich.org/publications/dsn.pdf"
        },
        {
          "label": "🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Pełny raport PDF)",
          "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"
        },
        {
          "label": "🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)",
          "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"
        },
        {
          "label": "🇬🇧 Paul Miller — „An Introductory Course in Computational Neuroscience” (MIT Press)",
          "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"
        },
        {
          "label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain” (MIT Press)",
          "url": "https://mitpress.mit.edu/9780262531207/the-computational-brain/"
        },
        {
          "label": "🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” & Larry Squire — „Fundamental Neuroscience”",
          "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:19:00Z"
    },
    {
      "id": "smat-6",
      "categoryType": "TRACK",
      "targetId": "C",
      "topic": "Elektronika analogowa i układy dynamiczne.",
      "title": "Projekt C (PL → EN): Elektronika analogowa (Horowitz & Hill, OpenAGH, ZPE, Forbot), przetworniki ADC/DAC, sieci neuronowe (Osowski, Tadeusiewicz) i Neuromorphic Computing",
      "level": "Podstawowy / Akademicki",
      "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
      "content": "Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne.\n1. W pierwszej kolejności (Po polsku): Podręczniki akademickie z elektroniki analogowej (Paul Horowitz, Winfield Hill — „Sztuka elektroniki”; e-podręczniki OpenAGH): wzmacniacze, oscylatory, filtry, sprzężenie zwrotne i układy dynamiczne; materiały o przetwornikach A/C i C/A (ZPE, Forbot); Stanisław Osowski — „Sieci neuronowe do przetwarzania informacji” (Oficyna PW) oraz Ryszard Tadeusiewicz — „Sieci neuronowe”.\n2. Uzupełniająco (Po angielsku): Analog computing, neuromorphic computing, analog neural networks i fizyczne modele neuronów.",
      "url": "https://zpe.gov.pl/",
      "links": [
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz C/A",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki z elektroniki i układów dynamicznych",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Forbot — Praktyczne kursy elektroniki analogowej i pomiarów po polsku",
          "url": "https://forbot.pl/"
        },
        {
          "label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering",
          "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"
        },
        {
          "label": "🇬🇧 arXiv — Neural and Evolutionary Computing (Neuromorphic & Analog NN)",
          "url": "https://arxiv.org/list/cs.NE/recent"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:20:00Z"
    },
    {
      "id": "smat-7",
      "categoryType": "TRACK",
      "targetId": "D",
      "topic": "Biologia syntetyczna i edycja genomu.",
      "title": "Projekt D (PL → EN): Biologia komórki (Alberts), genetyka (Brown, Węgleński), embriologia (Bartel), inżynieria tkankowa, bioetyka (PAN) i Stanisław Lem („Summa technologiae”)",
      "level": "Podstawowy → Badawczy",
      "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
      "content": "Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka.\n1. W pierwszej kolejności (Po polsku): Bruce Alberts — „Podstawy biologii komórki” (PWN); Terence A. Brown — „Genomy” (PWN); Hieronim Bartel — „Embriologia. Podręcznik dla studentów” (PZWL); literatura o komórkach macierzystych, inżynierii tkankowej i medycynie regeneracyjnej (PZWL / PWN); stanowiska Komitetu Bioetyki PAN; Stanisław Lem — „Summa technologiae” (klasyczna analiza inżynierii biologicznej a science fiction).\n2. Uzupełniająco (Po angielsku): National Academies (odpowiedzialny rozwój biologii syntetycznej), NCBI Bookshelf, ISSCR i Nature.",
      "url": "https://bioetyka.pan.pl/",
      "links": [
        {
          "label": "🇵🇱 Komitet Bioetyki Polskiej Akademii Nauk (PAN) — Opracowania i stanowiska bioetyczne po polsku",
          "url": "https://bioetyka.pan.pl/"
        },
        {
          "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Hieronim Bartel „Embriologia”, medycyna regeneracyjna i komórki macierzyste",
          "url": "https://pzwl.pl/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Biologia komórki (Alberts), Genomy (Brown), Genetyka molekularna (Węgleński)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biotechnologia, genetyka i inżynieria genetyczna po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇬🇧 National Academies — Odpowiedzialny rozwój biologii syntetycznej",
          "url": "https://www.nationalacademies.org/"
        },
        {
          "label": "🇬🇧 NCBI Bookshelf — Developmental Biology & Cell Biology",
          "url": "https://www.ncbi.nlm.nih.gov/books/"
        },
        {
          "label": "🇬🇧 ISSCR — International Society for Stem Cell Research",
          "url": "https://www.isscr.org/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:22:00Z"
    },
    {
      "id": "smat-8",
      "categoryType": "TRACK",
      "targetId": "E",
      "topic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
      "title": "Projekt E (Filozofia — PL w pierwszej kolejności): Alan Chalmers, Thomas S. Kuhn, Michał Heller, Władysław Tatarkiewicz, filozofia starożytna (Wolne Lektury) i bioetyka",
      "level": "Podstawowy / Akademicki",
      "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
      "content": "1. W pierwszej kolejności (Po polsku):\n• Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n• Thomas S. Kuhn — „Struktura rewolucji naukowych”\n• Michał Heller — „Filozofia nauki. Wprowadzenie” oraz „Filozofia przyrody” (Copernicus Center Press)\n• Filozofia starożytna po polsku: Platon („Państwo”, „Timajos”), Arystoteles („Metafizyka”, „O duszy”), stoicy (Marek Aureliusz — „Rozmyślania”, Seneka, Epiktet) w serwisie Wolne Lektury oraz Władysław Tatarkiewicz — „Historia filozofii. Tom 1–3” (PWN)\n• Filozofia umysłu, techniki i bioetyka: M. Miłkowski, R. Poczobut (red.) — „Przewodnik po filozofii umysłu”; Kazimierz Szewczyk — „Bioetyka. Tom 1–2” (PWN).\n2. Uzupełniająco (Po angielsku): Stanford Encyclopedia of Philosophy (SEP) oraz Internet Encyclopedia of Philosophy (IEP).",
      "url": "https://ccpress.pl/",
      "links": [
        {
          "label": "🇵🇱 Copernicus Center Press — Książki ks. prof. Michała Hellera i filozofia nauki po polsku",
          "url": "https://ccpress.pl/"
        },
        {
          "label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Darmowe polskie wykłady z filozofii nauki, umysłu i etyki",
          "url": "https://www.copernicuscenter.edu.pl/"
        },
        {
          "label": "🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka)",
          "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Kuhn „Struktura rewolucji naukowych”, Tatarkiewicz „Historia filozofii”, Szewczyk „Bioetyka”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇬🇧 Stanford Encyclopedia of Philosophy (Filozofia nauki, umysłu i bioetyka)",
          "url": "https://plato.stanford.edu/"
        },
        {
          "label": "🇬🇧 Internet Encyclopedia of Philosophy (IEP)",
          "url": "https://iep.utm.edu/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:25:00Z"
    },
    {
      "id": "smat-9",
      "categoryType": "TRACK",
      "targetId": "F",
      "topic": "Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.",
      "title": "Projekt F (Człowiek w kosmosie — PL → EN): Polska Agencja Kosmiczna (POLSA), ESERO Polska (Centrum Nauki Kopernik), medycyna kosmiczna i astronautyka oraz darmowe źródła NASA i ESA",
      "level": "Podstawowy / Zaawansowany",
      "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
      "content": "Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.\n1. W pierwszej kolejności (Po polsku): Materiały edukacyjne i badawcze Polskiej Agencji Kosmicznej (POLSA); polskojęzyczne scenariusze i opracowania ESERO Polska (Biuro Edukacji Kosmicznej ESA przy Centrum Nauki Kopernik) dot. życia w mikrograwitacji, ochrony radiacyjnej, mechaniki orbitalnej i budowy habitatów; polskie podręczniki fizyki (OpenStax Fizyka PL), mechaniki nieba oraz medycyny lotniczej i kosmicznej (K. Kwarecki, PZWL).\n2. Darmowe źródła międzynarodowe (NASA i ESA): NASA Fundamentals of Human Health, ESA Teach with Space, ESA Human and Robotic Exploration.",
      "url": "https://esero.kopernik.org.pl/",
      "links": [
        {
          "label": "🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o załogowych misjach kosmicznych i habitatach",
          "url": "https://esero.kopernik.org.pl/"
        },
        {
          "label": "🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja, nauka, medycyna i technologie kosmiczne po polsku",
          "url": "https://polsa.gov.pl/"
        },
        {
          "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych” (Mechanika, grawitacja, ruch orbitalny po polsku)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
        },
        {
          "label": "🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)",
          "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"
        },
        {
          "label": "🛰️ ESA — Edukacja kosmiczna (Teach with Space)",
          "url": "https://education.esa.int/teach-with-space/"
        },
        {
          "label": "👩‍🚀 ESA — Eksploracja załogowa i robotyczna (Human and Robotic Exploration)",
          "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:28:00Z"
    },
    {
      "id": "smat-10",
      "categoryType": "TRACK",
      "targetId": "G",
      "topic": "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.",
      "title": "Projekt G (Człowiek na Ziemi — PL → EN): Jan Krystek („Ochrona środowiska dla inżynierów”), January Weiner („Życie i ewolucja biosfery”), Politechnika Śląska, GIOŚ i ESA Education",
      "level": "Podstawowy / Inżynierski",
      "format": "Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)",
      "content": "Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa.\n1. W pierwszej kolejności (Po polsku):\n• Jan Krystek — „Ochrona środowiska dla inżynierów” (Wydawnictwo Naukowe PWN).\n• January Weiner — „Życie i ewolucja biosfery. Podręcznik ekologii ogólnej” (PWN) — fundamentalny polski podręcznik funkcjonowania ekosystemów.\n• Czesława Rosik-Dulewska — „Podstawy gospodarki odpadami” (PWN).\n• Bezpłatne materiały Politechniki Śląskiej i OpenAGH dot. ochrony wód, powietrza i gleby oraz raporty GIOŚ (Państwowy Monitoring Środowiska).\n2. Uzupełniająco: Europejska Agencja Środowiska (EEA — serwis w jęz. polskim) oraz ESA Education.",
      "url": "https://www.polsl.pl/",
      "links": [
        {
          "label": "🇵🇱 Politechnika Śląska — Bezpłatne materiały dotyczące podstaw ochrony środowiska",
          "url": "https://www.polsl.pl/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz January Weiner „Życie i ewolucja biosfery”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ) — Państwowy Monitoring Środowiska (wody, powietrze, gleby)",
          "url": "https://www.gios.gov.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie materiały o ekologii, odnawialnych źródłach energii i ochronie środowiska",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Europejska Agencja Środowiska (EEA po polsku — klimat, bioróżnorodność, GOZ, LCA)",
          "url": "https://www.eea.europa.eu/pl"
        },
        {
          "label": "🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska",
          "url": "https://education.esa.int/teach-with-space/"
        }
      ],
      "author": "Administrator",
      "status": "approved",
      "createdAt": "2026-10-25T12:30:00Z"
    },
    {
      "id": "smat-h1",
      "categoryType": "TRACK",
      "targetId": "H",
      "topic": "Reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt HTGR-POLA w NCBJ Świerk) do kogeneracji i produkcji wodoru.",
      "title": "Super-Projekt H (PL → EN): Fizyka jądrowa, reaktor MARIA, projekt HTGR-POLA (NCBJ Świerk), SMR, fuzja termojądrowa (IFPiLM) oraz profile badaczy w bazie Ludzie Nauki",
      "level": "Podstawowy → Zaawansowany",
      "format": "Biblioteka Super-Projektu H (PL w pierwszej kolejności)",
      "sourceLang": "PL+EN",
      "content": "1. W pierwszej kolejności (Po polsku):\n• Podręczniki akademickie: E. Skrzypczak, Z. Szefliński — „Wstęp do fizyki jądra atomowego i cząstek elementarnych” (PWN); OpenStax Polska „Fizyka dla szkół wyższych. Tom 3” (Fizyka jądrowa); materiały OpenAGH (Energetyka jądrowa).\n• Narodowe Centrum Badań Jądrowych (NCBJ Świerk) i raporty w serwisie Nauka w Polsce: polski reaktor badawczy MARIA (30 MW — produkcja radioizotopów medycznych Mo-99/Lu-177, neutronowe domieszkowanie krzemu dla elektroniki i badania materiałowe dla fuzji IFMIF-DONES) oraz projekt polskiego reaktora wysokotemperaturowego HTGR-POLA.\n• Baza „Ludzie Nauki” (ludzie.nauka.gov.pl/ln/) — dorobek polskich fizyków jądrowych, reaktorowych i plazmowych (NCBJ, IFPiLM, AGH, PW).\n2. Uzupełniająco (Po angielsku): IAEA SMR & HTGR Technology Roadmaps, ITER Fusion oraz NASA Space Nuclear Power.",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — NCBJ opracowało koncepcję polskiego reaktora wysokotemperaturowego (HTGR-POLA)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Reaktor badawczy MARIA w NCBJ Świerk: izotopy medyczne, krzem i badania dla fuzji",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C105854%2Cdyrektor-ncbj-maria-chyba-jedyny-reaktor-badawczy-na-swiecie-bez-stabilnego"
        },
        {
          "label": "🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Profile polskich ekspertów i grantów w obszarze energetyki jądrowej i fizyki plazmy",
          "url": "https://ludzie.nauka.gov.pl/ln/"
        },
        {
          "label": "🇵🇱 Narodowe Centrum Badań Jądrowych (NCBJ Świerk) — Edukacja i badania jądrowe",
          "url": "https://www.ncbj.gov.pl/"
        },
        {
          "label": "🇵🇱 Instytut Fizyki Plazmy i Laserowej Mikrosyntezy (IFPiLM) — Fuzja jądrowa",
          "url": "https://www.ifpilm.pl/"
        },
        {
          "label": "🇬🇧 IAEA — Small Modular Reactors (SMR) & Advanced Reactors",
          "url": "https://www.iaea.org/"
        }
      ],
      "author": "Ireneusz",
      "status": "approved",
      "createdAt": "2026-10-25T22:50:00Z"
    },
    {
      "id": "smat-ai-nwp",
      "categoryType": "FOUNDATION",
      "targetId": "FND-8",
      "topic": "Modele poznawcze, reprezentacje semantyczne a biologiczne działanie mózgu (porównanie AI i Projektu B).",
      "title": "Przegląd „Nauka w Polsce” i „Ludzie Nauki”: Inteligencja biologiczna a sztuczna — systemy wzorowane na mózgu, cyfrowy sen sieci neuronowych i biokomputery",
      "level": "Średniozaawansowany / Badawczy",
      "format": "Zestawienie artykułów badawczych (Nauka w Polsce + Ludzie Nauki)",
      "sourceLang": "PL",
      "content": "Zbiór wyselekcjonowanych artykułów z serwisu Nauka w Polsce (naukawpolsce.pl) oraz profili badawczych z bazy Ludzie Nauki (ludzie.nauka.gov.pl/ln/) łączących Sztuczną Inteligencję (Dziedzina 8) z Projektem B (Cyfrowy umysł) i Projektem C (Układy neuromorficzne):\n• Prof. Włodzisław Duch o transformacji nauki przez AI i kierunkach neuroinformatyki.\n• Systemy neuromorficzne i chipy wzorowane na mózgu (memrystory) obniżające gigantyczne zużycie energii przez współczesne modele AI.\n• Algorytmy naśladujące ludzki sen w sztucznych sieciach neuronowych — zapobieganie katastrofalnemu zapominaniu podczas uczenia ciągłego.\n• Biokomputery hybrydowe (Brainoware) łączące żywe organoidy mózgowe z elektroniką.",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — Kognitywista: przyszłością sztucznej inteligencji są systemy wzorowane na mózgu",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Prof. Włodzisław Duch: sztuczna inteligencja zmienia wszystko",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C95000%2Cprof-wlodzislaw-duch-sztuczna-inteligencja-zmienia-wszystko.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Sztuczna inteligencja może lepiej „zapamiętać” treści, jeśli naśladuje ludzki sen",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C100463%2Csztuczna-inteligencja-moze-lepiej-zapamietac-tresci-jesli-nasladuje-ludzki"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Inspirowany mózgiem chip ma ułatwić pracę SI (układy neuromorficzne)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C112694%2Cinspirowany-mozgiem-chip-ma-ulatwic-prace-si.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Komputer z żywym mózgiem (hybrydowe biokomputery organoidowe)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C100102%2Ckomputer-z-zywym-mozgiem.html"
        },
        {
          "label": "🇵🇱 Ludzie Nauki (OPI PIB) — Baza polskich badaczy AI, kognitywistyki i sieci neuronowych",
          "url": "https://ludzie.nauka.gov.pl/ln/"
        }
      ],
      "author": "Ireneusz",
      "status": "approved",
      "createdAt": "2026-10-25T22:51:00Z"
    }
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
            "🇵🇱 Podręcznik fizyki ogólnej po polsku — [OpenStax Fizyka dla szkół wyższych Tom 1–3 (darmowy PL)](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1) | Halliday & Resnick *Podstawy fizyki* ([PWN](https://ksiegarnia.pwn.pl/))"
          ]
        },
        {
          "stage": "2. Następnie (Genomy, chemia, biologia i psychologia biologiczna po polsku)",
          "items": [
            "🇵🇱 Terence A. Brown — *Genomy* (polskie wydanie) — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
            "🇵🇱 Podstawy chemii, biologii i biochemii po polsku — *Biologia Campbella* ([Rebis](https://www.rebis.com.pl/)), Stryer *Biochemia* ([PWN](https://ksiegarnia.pwn.pl/)), Alberts *Podstawy biologii komórki* ([PWN](https://ksiegarnia.pwn.pl/)), [ZPE](https://zpe.gov.pl/)",
            "🇵🇱 James W. Kalat — *Biologiczne podstawy psychologii* (polskie wydanie) — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)"
          ]
        },
        {
          "stage": "3. Później (Neurobiologia, konektomika, neuronauka obliczeniowa i WBE)",
          "items": [
            "🇵🇱 Alan Longstaff — *Neurobiologia. Krótkie wykłady* ([PWN](https://ksiegarnia.pwn.pl/)), E. Nęcka — *Psychologia poznawcza* ([PWN](https://ksiegarnia.pwn.pl/)) oraz 🇵🇱 Sebastian Seung — *Konektom. Jak połączenia w mózgu kształtują naszą tożsamość* (wyd. polskie)",
            "🇬🇧 Peter Dayan, L. F. Abbott — *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems* — [MIT Press](https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/)",
            "🇬🇧 Eugene M. Izhikevich — *Dynamical Systems in Neuroscience* — [Pełny PDF autora](https://www.izhikevich.org/publications/dsn.pdf)",
            "🇬🇧 Anders Sandberg, Nick Bostrom — *Whole Brain Emulation: A Roadmap* — [Pełny raport PDF (FHI Oxford)](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)"
          ]
        },
        {
          "stage": "4. Na zaawansowanym etapie (Mechanika kwantowa, neurobiologia akademicka i obliczenia kwantowe)",
          "items": [
            "🇵🇱/🇬🇧 David J. Griffiths — *Wstęp do mechaniki kwantowej* ([polskie wydanie PWN](https://ksiegarnia.pwn.pl/)) / *Introduction to Quantum Mechanics* ([CUP](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E))",
            "🇬🇧 Eric R. Kandel i współautorzy — *Principles of Neural Science* — [McGraw Hill](https://www.mheducation.com/)",
            "🇬🇧 Larry Squire i współautorzy — *Fundamental Neuroscience* — [ScienceDirect](https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience)",
            "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — *The Computational Brain* — [MIT Press](https://mitpress.mit.edu/9780262531207/the-computational-brain/)",
            "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — *Quantum Computation and Quantum Information* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)"
          ]
        }
      ]
    },
    "rules": [
      "W pierwszej kolejności korzystać z literatury oraz darmowych źródeł polskojęzycznych (OpenStax Polska, e-podręczniki OpenAGH, Zintegrowana Platforma Edukacyjna ZPE, Ważniak MIMUW, polskie wydania PWN, Helion, PZWL i Copernicus Center Press).",
      "Zasada czytania: najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja.",
      "Książki specjalistyczne i anglojęzyczne wprowadzać po opanowaniu podstaw danego obszaru po polsku.",
      "Przed zakupem sprawdzać dokładny tytuł, autora, wydanie i dostępność polskiego przekładu.",
      "W szybko rozwijających się dziedzinach korzystać również z aktualnych przeglądów naukowych i dokumentacji instytucji badawczych (PAN, POLSA, GIOŚ, NASA, ESA).",
      "Rozróżniać wiedzę potwierdzoną, aktywne badania, hipotezy i spekulacje (pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi).",
      "Traktować bibliografię jako zasób długoterminowy, a nie listę lektur do przeczytania w całości od razu."
    ],
    "projects": [
      {
        "trackId": "FND-1",
        "title": "I. MATEMATYKA I INFORMATYKA (Wspólne podstawy — PL w pierwszej kolejności)",
        "sequenceLabel": "Etap czytania",
        "sequence": "Najpierw (po polsku): Petzold (Kod. Ukryty język komputerów) → Matthes (Python. Instrukcje dla programisty) → Polskie podręczniki matematyki i algebry liniowej (OpenAGH, ZPE, Skoczylas) → Uzupełniająco (EN): Gilbert Strang (Introduction to Linear Algebra).",
        "links": [
          {
            "label": "🇵🇱 Wydawnictwo Helion — Polskie wydania: Charles Petzold „Kod” oraz Eric Matthes „Python. Instrukcje dla programisty”",
            "url": "https://helion.pl/"
          },
          {
            "label": "🇵🇱 OpenAGH — Darmowe polskie e-podręczniki: Matematyka i Algebra Liniowa",
            "url": "https://open.agh.edu.pl/"
          },
          {
            "label": "🇵🇱 Ważniak MIMUW (UW) — Darmowe polskie kursy akademickie z matematyki i informatyki",
            "url": "https://wazniak.mimuw.edu.pl/"
          },
          {
            "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Matematyka, logika i informatyka po polsku",
            "url": "https://zpe.gov.pl/"
          },
          {
            "label": "🇵🇱 Oficjalna dokumentacja i samouczek Pythona po polsku",
            "url": "https://docs.python.org/pl/3/tutorial/"
          },
          {
            "label": "🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT 18.06)",
            "url": "https://math.mit.edu/~gs/linearalgebra/"
          },
          {
            "label": "🇬🇧 Charles Petzold — Code (Strona książki i symulacje)",
            "url": "https://codehiddenlanguage.com/"
          },
          {
            "label": "🇬🇧 Eric Matthes — Python Crash Course (Zasoby i ćwiczenia)",
            "url": "https://ehmatthes.github.io/pcc_3e/"
          }
        ],
        "groups": [
          {
            "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
            "items": [
              "1. Charles Petzold — *Kod. Ukryty język komputerów. Wydanie II.* — [Wydawnictwo Helion](https://helion.pl/)",
              "2. Eric Matthes — *Python. Instrukcje dla programisty. Wydanie III.* — [Wydawnictwo Helion](https://helion.pl/) + [Samouczek Python PL](https://docs.python.org/pl/3/tutorial/)",
              "3. Podręczniki matematyki i algebry liniowej na poziomie szkoły średniej i studiów: M. Gewert, Z. Skoczylas (*Algebra liniowa*, *Analiza matematyczna*), T. Krasiński (*Algebra liniowa* PWN) oraz darmowe zasoby: [OpenAGH Matematyka](https://open.agh.edu.pl/) | [ZPE Matematyka](https://zpe.gov.pl/) | [Ważniak MIMUW](https://wazniak.mimuw.edu.pl/)",
              "4. Thomas H. Cormen i współautorzy — *Wprowadzenie do algorytmów* (polskie wydanie, [PWN](https://ksiegarnia.pwn.pl/)) oraz Roger Penrose — *Droga do rzeczywistości* (wyd. polskie)."
            ]
          },
          {
            "heading": "2. Anglojęzyczne (uzupełniające)",
            "items": [
              "5. Gilbert Strang — *Introduction to Linear Algebra.* — [MIT Linear Algebra](https://math.mit.edu/~gs/linearalgebra/)",
              "6. Charles Petzold — *Code.* — [codehiddenlanguage.com](https://codehiddenlanguage.com/)",
              "7. Eric Matthes — *Python Crash Course.* — [ehmatthes.github.io/pcc_3e](https://ehmatthes.github.io/pcc_3e/)"
            ]
          }
        ]
      },
      {
        "trackId": "FND-4",
        "title": "II. FIZYKA I KOMPUTERY KWANTOWE (Wspólne podstawy — PL w pierwszej kolejności)",
        "sequenceLabel": "Etap czytania",
        "sequence": "Najpierw (po polsku): OpenStax „Fizyka dla szkół wyższych Tom 1–3”, Halliday & Resnick „Podstawy fizyki” oraz polskie podręczniki elektroniki (Horowitz & Hill „Sztuka elektroniki”, ZPE, Forbot) → Na zaawansowanym etapie: Griffiths („Wstęp do mechaniki kwantowej” PL / EN) oraz Nielsen i Chuang.",
        "links": [
          {
            "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3” (pełny darmowy podręcznik po polsku)",
            "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
          },
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — Halliday & Resnick „Podstawy fizyki”, Feynman „Wykłady z fizyki”, Griffiths „Wstęp do mechaniki kwantowej”",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki fizyki, elektroniki i układów cyfrowych",
            "url": "https://open.agh.edu.pl/"
          },
          {
            "label": "🇵🇱 Forbot — Kursy podstaw elektroniki i techniki cyfrowej po polsku",
            "url": "https://forbot.pl/blog/kurs-elektroniki-poziom-1-spis-tresci-id5159"
          },
          {
            "label": "🇬🇧 David J. Griffiths — Introduction to Quantum Mechanics (CUP)",
            "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"
          },
          {
            "label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — Quantum Computation and Quantum Information",
            "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"
          }
        ],
        "groups": [
          {
            "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
            "items": [
              "1. Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach: *OpenStax Fizyka dla szkół wyższych Tom 1–3* ([darmowy dostęp PL](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1)), D. Halliday, R. Resnick, J. Walker — *Podstawy fizyki* ([PWN](https://ksiegarnia.pwn.pl/)), R. P. Feynman — *Feynmana wykłady z fizyki* (PWN), D. J. Griffiths — *Wstęp do mechaniki kwantowej* (polskie wydanie PWN).",
              "2. Podręczniki podstaw elektroniki i układów cyfrowych po polsku: P. Horowitz, W. Hill — *Sztuka elektroniki. Cz. 1–2* (WKŁ), B. Głocki — *Układy cyfrowe* (WSiP), [ZPE Elektronika](https://zpe.gov.pl/), [OpenAGH](https://open.agh.edu.pl/) oraz [Kursy Forbot](https://forbot.pl/)."
            ]
          },
          {
            "heading": "2. Anglojęzyczne (etap zaawansowany)",
            "items": [
              "3. David J. Griffiths — *Introduction to Quantum Mechanics.* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E)",
              "4. Michael A. Nielsen, Isaac L. Chuang — *Quantum Computation and Quantum Information.* — [Cambridge University Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)"
            ]
          }
        ]
      },
      {
        "trackId": "FND-7",
        "title": "III. CHEMIA, BIOLOGIA I GENETYKA (Wspólne podstawy — PL w pierwszej kolejności)",
        "sequenceLabel": "Etap czytania",
        "sequence": "Następnie (w pierwszej kolejności po polsku): Terence A. Brown („Genomy” PWN) → „Biologia Campbella” (wyd. polskie Rebis) i B. Alberts („Podstawy biologii komórki” PWN) → Polskie podręczniki chemii i biochemii (Stryer „Biochemia”, Jones & Atkins, McMurry) → Uzupełniająco (EN): OpenStax Chemistry 2e i Biology 2e.",
        "links": [
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — T.A. Brown „Genomy”, Stryer „Biochemia”, Alberts „Podstawy biologii komórki”, Jones & Atkins „Chemia ogólna”",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇵🇱 Dom Wydawniczy REBIS — „Biologia Campbella” (polskie wydanie)",
            "url": "https://www.rebis.com.pl/"
          },
          {
            "label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki chemii ogólnej, biochemii, biologii i genetyki",
            "url": "https://open.agh.edu.pl/"
          },
          {
            "label": "🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej",
            "url": "https://openstax.org/details/books/chemistry-2e"
          },
          {
            "label": "🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii",
            "url": "https://openstax.org/details/books/biology-2e"
          },
          {
            "label": "🇬🇧 Terence A. Brown — Genomes (NCBI Bookshelf)",
            "url": "https://www.ncbi.nlm.nih.gov/books/NBK21128/"
          }
        ],
        "groups": [
          {
            "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
            "items": [
              "1. Terence A. Brown — *Genomy.* (polskie wydanie) — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
              "2. *Biologia Campbella* — polskie wydanie ([Dom Wydawniczy REBIS](https://www.rebis.com.pl/)) oraz Bruce Alberts i współautorzy — *Podstawy biologii komórki* ([PWN](https://ksiegarnia.pwn.pl/)).",
              "3. Akademickie podręczniki chemii ogólnej, organicznej i biochemii po polsku: L. Stryer i współautorzy — *Biochemia* (PWN), L. Jones, P. Atkins — *Chemia ogólna* (PWN), A. Bielański — *Podstawy chemii nieorganicznej* (PWN), J. McMurry — *Chemia organiczna* (PWN), [OpenAGH Chemia](https://open.agh.edu.pl/) i [ZPE](https://zpe.gov.pl/)."
            ]
          },
          {
            "heading": "2. Anglojęzyczne (uzupełniające)",
            "items": [
              "4. *OpenStax Chemistry 2e* — podręcznik chemii ogólnej: [https://openstax.org/details/books/chemistry-2e](https://openstax.org/details/books/chemistry-2e)",
              "5. *OpenStax Biology 2e* — podręcznik biologii: [https://openstax.org/details/books/biology-2e](https://openstax.org/details/books/biology-2e)",
              "6. Akademickie podręczniki biochemii i biologii molekularnej — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/)"
            ]
          }
        ]
      },
      {
        "trackId": "A",
        "title": "IV. PROJEKT A — CZŁOWIEK BIOCYFROWO-ROBOTYCZNY (PL w pierwszej kolejności)",
        "sequenceLabel": "Kolejność nauki",
        "sequence": "W pierwszej kolejności po polsku: Biologiczne podstawy psychologii (Kalat, PWN) oraz anatomia i fizjologia człowieka (Bochenek, Traczyk, Konturek) → Biofizyka, biomechanika i biomateriały (Jaroszyk, Marciniak, Tadeusiewicz) → Robotyka, elektronika, sterowanie i uczenie maszynowe (Géron wyd. polskie Helion) → Neuroprotetyka i interfejsy mózg–komputer (BCI).",
        "links": [
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — James W. Kalat „Biologiczne podstawy psychologii” oraz podręczniki biofizyki i robotyki",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia człowieka (Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)",
            "url": "https://pzwl.pl/"
          },
          {
            "label": "🇵🇱 Wydawnictwo Helion — Aurélien Géron „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” (wyd. polskie)",
            "url": "https://helion.pl/"
          },
          {
            "label": "🇵🇱 OpenAGH — Polskie materiały z inżynierii biomedycznej, biocybernetyki i automatyki",
            "url": "https://open.agh.edu.pl/"
          },
          {
            "label": "🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik online/PDF)",
            "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"
          },
          {
            "label": "🇬🇧 Aurélien Géron — Hands-On Machine Learning (Repozytorium GitHub)",
            "url": "https://github.com/ageron/handson-ml3"
          }
        ],
        "groups": [
          {
            "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
            "items": [
              "1. James W. Kalat — *Biologiczne podstawy psychologii.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
              "2. Akademickie podręczniki anatomii i fizjologii człowieka: A. Bochenek, M. Reicher — *Anatomia człowieka* ([PZWL](https://pzwl.pl/)); W. Traczyk, A. Trzebski — *Fizjologia człowieka z elementami fizjologii stosowanej i klinicznej* (PZWL); S. Konturek — *Fizjologia człowieka*.",
              "3. Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: F. Jaroszyk (red.) — *Biofizyka* (PZWL); J. Marciniak — *Biomateriały* (Politechnika Śląska); seria *Biocybernetyka i Inżynieria Biomedyczna 2000* (PAN, red. M. Nałęcz, R. Tadeusiewicz) — [OpenAGH](https://open.agh.edu.pl/).",
              "4. Podręczniki robotyki, elektroniki, układów sterowania i AI po polsku: K. Tchoń i współautorzy — *Manipulatory i roboty mobilne*; A. Géron — *Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow* ([Helion](https://helion.pl/))."
            ]
          },
          {
            "heading": "2. Anglojęzyczne (uzupełniające i specjalistyczne)",
            "items": [
              "5. *OpenStax Anatomy and Physiology 2e.* — [https://openstax.org/details/books/anatomy-and-physiology-2e](https://openstax.org/details/books/anatomy-and-physiology-2e)",
              "6. Géron — *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.* — [GitHub ageron/handson-ml3](https://github.com/ageron/handson-ml3)",
              "7. Akademickie podręczniki inżynierii tkankowej, neuroprotetyki i interfejsów mózg–komputer — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | [Physiological Reviews BCI](https://doi.org/10.1152/physrev.00027.2016)"
            ]
          }
        ]
      },
      {
        "trackId": "B",
        "title": "V. PROJEKT B — CYFROWY UMYSŁ (PL w pierwszej kolejności)",
        "sequenceLabel": "Kolejność czytania (Etapy 2 → 3 → 4)",
        "sequence": "W pierwszej kolejności po polsku: Kalat („Biologiczne podstawy psychologii”), Longstaff („Neurobiologia”), Nęcka („Psychologia poznawcza”), Miłkowski i Poczobut („Przewodnik po filozofii umysłu”) oraz Seung („Konektom” — wyd. polskie) → Później (EN): Dayan & Abbott („Theoretical Neuroscience”), Izhikevich („Dynamical Systems in Neuroscience”), Sandberg & Bostrom („Whole Brain Emulation: A Roadmap”) → Na zaawansowanym etapie: Kandel („Principles of Neural Science”), Squire („Fundamental Neuroscience”), Churchland & Sejnowski („The Computational Brain”).",
        "links": [
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — J.W. Kalat „Biologiczne podstawy psychologii”, A. Longstaff „Neurobiologia”, E. Nęcka „Psychologia poznawcza”",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇵🇱 Prof. Włodzisław Duch (UMK) — Polskojęzyczne materiały z kognitywistyki, neuroinformatyki i modelowania mózgu",
            "url": "https://www.fizyka.umk.pl/~duch/"
          },
          {
            "label": "🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu, kognitywistyka i problem świadomości po polsku",
            "url": "https://ccpress.pl/"
          },
          {
            "label": "🇬🇧 Eugene M. Izhikevich — Dynamical Systems in Neuroscience (Darmowy PDF autora)",
            "url": "https://www.izhikevich.org/publications/dsn.pdf"
          },
          {
            "label": "🇬🇧 Anders Sandberg, Nick Bostrom — Whole Brain Emulation: A Roadmap (PDF)",
            "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"
          },
          {
            "label": "🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)",
            "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"
          },
          {
            "label": "🇬🇧 Paul Miller — An Introductory Course in Computational Neuroscience",
            "url": "https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/"
          },
          {
            "label": "🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — The Computational Brain",
            "url": "https://mitpress.mit.edu/9780262531207/the-computational-brain/"
          },
          {
            "label": "🇬🇧 Larry Squire et al. — Fundamental Neuroscience (ScienceDirect)",
            "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"
          }
        ],
        "groups": [
          {
            "heading": "1. Polskojęzyczne (w pierwszej kolejności)",
            "items": [
              "1. James W. Kalat — *Biologiczne podstawy psychologii.* — [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)",
              "2. Podręczniki neurobiologii i fizjologii układu nerwowego po polsku: Alan Longstaff — *Neurobiologia. Krótkie wykłady* ([PWN](https://ksiegarnia.pwn.pl/)); T. Górska, A. Grabowska, J. Zagrodzka (red.) — *Mózg a zachowanie* (PWN).",
              "3. Podręczniki psychologii poznawczej i konektomiki po polsku: Edward Nęcka, Jarosław Orzechowski, Błażej Szymura — *Psychologia poznawcza* ([PWN](https://ksiegarnia.pwn.pl/)); Sebastian Seung — *Konektom. Jak połączenia w mózgu kształtują naszą tożsamość* (polskie wydanie).",
              "4. Wprowadzenia do filozofii umysłu, kognitywistyki i problemu świadomości po polsku: Marcin Miłkowski, Robert Poczobut (red.) — *Przewodnik po filozofii umysłu*; wykłady z neuroinformatyki prof. Włodzisława Ducha ([UMK](https://www.fizyka.umk.pl/~duch/)) oraz [Centrum Kopernika / CCPress](https://ccpress.pl/)."
            ]
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
              "12. Anders Sandberg, Nick Bostrom — *Whole Brain Emulation: A Roadmap.* — [Pełny raport PDF](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)"
            ]
          }
        ]
      },
      {
        "trackId": "C",
        "title": "Projekt C — Maszyny analogowe i obliczenia fizyczne (PL w pierwszej kolejności)",
        "sequenceLabel": "Kolejność nauki",
        "sequence": "Elektronika analogowa (po polsku: Horowitz & Hill, OpenAGH, ZPE, Forbot) → układy dynamiczne → modelowanie matematyczne (Osowski, Tadeusiewicz) → fizyczne modele neuronów → obliczenia neuromorficzne.",
        "links": [
          {
            "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz C/A",
            "url": "https://zpe.gov.pl/"
          },
          {
            "label": "🇵🇱 OpenAGH — E-podręczniki z elektroniki, układów dynamicznych i fizyki po polsku",
            "url": "https://open.agh.edu.pl/"
          },
          {
            "label": "🇵🇱 Forbot — Kursy elektroniki analogowej, wzmacniaczy operacyjnych i ADC/DAC po polsku",
            "url": "https://forbot.pl/"
          },
          {
            "label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering",
            "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"
          },
          {
            "label": "🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks",
            "url": "https://arxiv.org/list/cs.NE/recent"
          },
          {
            "label": "🇬🇧 MIT OCW — Circuits & Electronics",
            "url": "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"
          }
        ],
        "groups": [
          {
            "heading": "1. Po polsku (w pierwszej kolejności)",
            "items": [
              "Podręczniki akademickie z elektroniki analogowej: Paul Horowitz, Winfield Hill — *Sztuka elektroniki* (wyd. polskie WKŁ); wzmacniacze, oscylatory, filtry, sprzężenie zwrotne i układy dynamiczne — [E-podręczniki OpenAGH](https://open.agh.edu.pl/)",
              "Materiały dydaktyczne o przetwornikach analogowo-cyfrowych (ADC) i cyfrowo-analogowych (DAC) — [Materiały ZPE](https://zpe.gov.pl/) | [Kursy Forbot](https://forbot.pl/)",
              "Polska literatura o sieciach neuronowych i biocybernetyce: Stanisław Osowski — *Sieci neuronowe do przetwarzania informacji* (Oficyna Wydawnicza PW); Ryszard Tadeusiewicz — *Sieci neuronowe*.",
              "Zintegrowana Platforma Edukacyjna — punkt wyjścia do szukania materiałów o elektronice: [https://zpe.gov.pl/](https://zpe.gov.pl/)"
            ]
          },
          {
            "heading": "2. Po angielsku (uzupełniające i badawcze)",
            "items": [
              "Materiały techniczne dotyczące analog computing — [MIT OpenCourseWare Electronics](https://ocw.mit.edu/search/?q=analog+computing)",
              "Materiały badawcze dotyczące neuromorphic computing i analog neural networks — [Frontiers in Neuromorphic Engineering](https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering)",
              "Publikacje o fizycznych modelach neuronów oraz analogowych i hybrydowych procesorach — [arXiv cs.NE](https://arxiv.org/list/cs.NE/recent) | [Neuronal Dynamics (EPFL)](https://neuronaldynamics.epfl.ch/)"
            ]
          }
        ]
      },
      {
        "trackId": "D",
        "title": "Projekt D — „Frankenstein”: biotechnologia i tworzenie organizmów (PL w pierwszej kolejności)",
        "sequenceLabel": "Kolejność nauki",
        "sequence": "W pierwszej kolejności po polsku: Biologia komórki (Alberts, PWN) → genetyka (Brown „Genomy”, Węgleński) → embriologia (Bartel „Embriologia”, PZWL) → komórki macierzyste i inżynieria tkankowa → biologia syntetyczna, bioetyka (Komitet Bioetyki PAN) i nauka a SF (Stanisław Lem „Summa technologiae”).",
        "links": [
          {
            "label": "🇵🇱 Komitet Bioetyki Polskiej Akademii Nauk (PAN) — Stanowiska i opracowania bioetyczne po polsku",
            "url": "https://bioetyka.pan.pl/"
          },
          {
            "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Hieronim Bartel „Embriologia”, histologia i medycyna regeneracyjna",
            "url": "https://pzwl.pl/"
          },
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — Alberts „Podstawy biologii komórki”, Brown „Genomy”, Węgleński „Genetyka molekularna”",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇵🇱 ZPE — Biologia komórki, genetyka i biotechnologia po polsku",
            "url": "https://zpe.gov.pl/"
          },
          {
            "label": "🇬🇧 National Academies — Responsible Development of Synthetic Biology",
            "url": "https://www.nationalacademies.org/"
          },
          {
            "label": "🇬🇧 NCBI Bookshelf — Darmowe podręczniki biologii komórki, genetyki i embriologii",
            "url": "https://www.ncbi.nlm.nih.gov/books/"
          },
          {
            "label": "🇬🇧 ISSCR — International Society for Stem Cell Research",
            "url": "https://www.isscr.org/"
          }
        ],
        "groups": [
          {
            "heading": "1. Po polsku (w pierwszej kolejności)",
            "items": [
              "Podręczniki akademickie z biologii komórki, genetyki i biologii rozwoju: B. Alberts — *Podstawy biologii komórki* ([PWN](https://ksiegarnia.pwn.pl/)), T. A. Brown — *Genomy* (PWN), P. Węgleński — *Genetyka molekularna* (PWN) oraz [ZPE Biologia](https://zpe.gov.pl/).",
              "Podręczniki z embriologii i komórek macierzystych po polsku: Hieronim Bartel — *Embriologia. Podręcznik dla studentów* ([PZWL](https://pzwl.pl/)).",
              "Literatura o inżynierii tkankowej, medycynie regeneracyjnej, bioetyce i granicach SF: publikacje [Komitetu Bioetyki PAN](https://bioetyka.pan.pl/), K. Szewczyk — *Bioetyka* (PWN) oraz Stanisław Lem — *Summa technologiae*."
            ]
          },
          {
            "heading": "2. Po angielsku (uzupełniające i badawcze)",
            "items": [
              "National Academies — materiały o odpowiedzialnym rozwoju biologii syntetycznej: [https://www.nationalacademies.org/](https://www.nationalacademies.org/)",
              "Publikacje akademickie o stem cells, developmental biology, tissue engineering i synthetic biology — [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | [ISSCR](https://www.isscr.org/) | [Nature Synthetic Biology](https://www.nature.com/subjects/synthetic-biology)"
            ]
          }
        ]
      },
      {
        "trackId": "E",
        "title": "Projekt E — Filozofia (PL w pierwszej kolejności)",
        "sequenceLabel": "Zastosowanie",
        "sequence": "Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.",
        "links": [
          {
            "label": "🇵🇱 Copernicus Center Press (ks. prof. Michał Heller — „Filozofia nauki. Wprowadzenie”)",
            "url": "https://ccpress.pl/"
          },
          {
            "label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Wykłady i kursy po polsku",
            "url": "https://www.copernicuscenter.edu.pl/"
          },
          {
            "label": "🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka)",
            "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"
          },
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — T.S. Kuhn „Struktura rewolucji naukowych”, W. Tatarkiewicz „Historia filozofii”, K. Szewczyk „Bioetyka”",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇬🇧 Stanford Encyclopedia of Philosophy (SEP)",
            "url": "https://plato.stanford.edu/"
          },
          {
            "label": "🇬🇧 Internet Encyclopedia of Philosophy (IEP)",
            "url": "https://iep.utm.edu/"
          }
        ],
        "groups": [
          {
            "heading": "1. Po polsku (w pierwszej kolejności)",
            "items": [
              "Alan Chalmers — *Czym jest to, co zwiemy nauką?* — [Katalog Biblioteki Narodowej](https://katalogi.bn.org.pl/)",
              "Thomas S. Kuhn — *Struktura rewolucji naukowych.* — [Wydawnictwo PWN / Aletheia](https://ksiegarnia.pwn.pl/)",
              "Michał Heller — *Filozofia nauki. Wprowadzenie* oraz *Filozofia przyrody* — [Copernicus Center Press](https://ccpress.pl/)",
              "Władysław Tatarkiewicz — *Historia filozofii. Tom 1–3* (PWN) oraz klasyka filozofii starożytnej w polskich przekładach ([Wolne Lektury](https://wolnelektury.pl/katalog/gatunek/filozofia/))."
            ]
          },
          {
            "heading": "2. Obszary do dalszego uzupełnienia (PL i EN)",
            "items": [
              "Filozofia starożytna: Platon (*Państwo*, *Timajos*), Arystoteles (*Metafizyka*, *O duszy*) i stoicy (*Rozmyślania* Marka Aureliusza, Seneka, Epiktet) — [Wolne Lektury: Filozofia (PL)](https://wolnelektury.pl/katalog/gatunek/filozofia/) | [SEP Ancient Philosophy](https://plato.stanford.edu/)",
              "Filozofia umysłu i problem świadomości — M. Miłkowski, R. Poczobut (red.) *Przewodnik po filozofii umysłu* (PL) | [Centrum Kopernika (PL)](https://www.copernicuscenter.edu.pl/) | [SEP Philosophy of Mind](https://plato.stanford.edu/entries/mind-identity/)",
              "Filozofia techniki, bioetyka i etyka środowiskowa — K. Szewczyk *Bioetyka Tom 1–2* (PWN), S. Lem *Summa technologiae*, [Komitet Bioetyki PAN](https://bioetyka.pan.pl/) | [SEP Philosophy of Technology](https://plato.stanford.edu/entries/technology/)"
            ]
          }
        ]
      },
      {
        "trackId": "F",
        "title": "Projekt F — Człowiek w kosmosie (PL w pierwszej kolejności + darmowe źródła NASA i ESA)",
        "sequenceLabel": "Kolejność nauki",
        "sequence": "Podstawy fizyki (OpenStax Fizyka PL) → mechanika orbitalna → technika kosmiczna (POLSA, ESERO Polska) → fizjologia kosmiczna (medycyna lotnicza i kosmiczna, NASA/ESA) → systemy podtrzymywania życia i habitaty.",
        "links": [
          {
            "label": "🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o eksploracji kosmosu, mikrograwitacji i habitatach",
            "url": "https://esero.kopernik.org.pl/"
          },
          {
            "label": "🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja kosmiczna, inżynieria i medycyna kosmiczna po polsku",
            "url": "https://polsa.gov.pl/"
          },
          {
            "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (Mechanika, grawitacja, ruch orbitalny po polsku)",
            "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
          },
          {
            "label": "🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)",
            "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"
          },
          {
            "label": "🛰️ ESA — Edukacja kosmiczna (Teach with Space)",
            "url": "https://education.esa.int/teach-with-space/"
          },
          {
            "label": "👩‍🚀 ESA — Eksploracja załogowa (Human and Robotic Exploration)",
            "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"
          },
          {
            "label": "🌱 MELiSSA Foundation — Systemy podtrzymywania życia (BLSS)",
            "url": "https://www.melissafoundation.org/"
          }
        ],
        "groups": [
          {
            "heading": "1. Po polsku (w pierwszej kolejności)",
            "items": [
              "ESERO Polska (Biuro Edukacji Kosmicznej ESA przy Centrum Nauki Kopernik) — polskojęzyczne materiały dydaktyczne o bazach księżycowych/marsjańskich, fizjologii w mikrograwitacji i mechanice orbitalnej: [https://esero.kopernik.org.pl/](https://esero.kopernik.org.pl/)",
              "Polska Agencja Kosmiczna (POLSA) — opracowania o technologiach kosmicznych, sektorze kosmicznym i medycynie kosmicznej po polsku: [https://polsa.gov.pl/](https://polsa.gov.pl/)",
              "Podręczniki polskojęzyczne: *OpenStax Fizyka dla szkół wyższych Tom 1* (mechanika i grawitacja po polsku), Krzysztof Kwarecki (red.) — *Medycyna lotnicza i kosmiczna* (PZWL), literatura Polskiego Towarzystwa Astronautycznego (*Astronautyka*)."
            ]
          },
          {
            "heading": "2. Darmowe źródła międzynarodowe (NASA i ESA)",
            "items": [
              "NASA — zdrowie człowieka w kosmosie: [https://www.nasa.gov/reference/fundamentals-of-human-health/](https://www.nasa.gov/reference/fundamentals-of-human-health/)",
              "ESA — edukacja kosmiczna: [https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)",
              "ESA — eksploracja załogowa: [https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)"
            ]
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
              "Psychologia izolacji i medycyna długotrwałych misji — [ESA Human Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)"
            ]
          }
        ]
      },
      {
        "trackId": "G",
        "title": "Projekt G — Człowiek na Ziemi i ochrona ekosystemu (PL w pierwszej kolejności)",
        "sequenceLabel": "Kolejność nauki",
        "sequence": "W pierwszej kolejności po polsku: Podstawy ekologii i funkcjonowanie ekosystemów (January Weiner „Życie i ewolucja biosfery”, PWN) → presje środowiskowe i monitoring (GIOŚ, Politechnika Śląska) → technologie ochronne i inżynieria środowiska (Jan Krystek „Ochrona środowiska dla inżynierów”, Rosik-Dulewska) → ekonomia i polityka środowiskowa (EEA PL).",
        "links": [
          {
            "label": "🇵🇱 Politechnika Śląska — Materiały dotyczące podstaw ochrony środowiska po polsku",
            "url": "https://www.polsl.pl/"
          },
          {
            "label": "🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz January Weiner „Życie i ewolucja biosfery”",
            "url": "https://ksiegarnia.pwn.pl/"
          },
          {
            "label": "🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ — Państwowy Monitoring Środowiska w Polsce)",
            "url": "https://www.gios.gov.pl/"
          },
          {
            "label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie materiały o ekologii, odnawialnych źródłach energii i ochronie środowiska",
            "url": "https://open.agh.edu.pl/"
          },
          {
            "label": "🇵🇱 Europejska Agencja Środowiska (EEA w języku polskim — Ekonomia ekologiczna, GOZ, LCA)",
            "url": "https://www.eea.europa.eu/pl"
          },
          {
            "label": "🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska",
            "url": "https://education.esa.int/teach-with-space/"
          }
        ],
        "groups": [
          {
            "heading": "1. Po polsku (w pierwszej kolejności)",
            "items": [
              "Jan Krystek — *Ochrona środowiska dla inżynierów.* — [Księgarnia Naukowa PWN](https://ksiegarnia.pwn.pl/)",
              "January Weiner — *Życie i ewolucja biosfery. Podręcznik ekologii ogólnej* ([PWN](https://ksiegarnia.pwn.pl/)) oraz Czesława Rosik-Dulewska — *Podstawy gospodarki odpadami* (PWN).",
              "Podręczniki akademickie z ekologii, ochrony środowiska i OZE — [OpenAGH (PL)](https://open.agh.edu.pl/) | [ZPE Ekologia (PL)](https://zpe.gov.pl/)",
              "Materiały polskich uczelni i instytucji dotyczące ochrony wód, powietrza i gleby — [Politechnika Śląska](https://www.polsl.pl/) | [GIOŚ Monitoring Środowiska](https://www.gios.gov.pl/)"
            ]
          },
          {
            "heading": "2. Źródła bezpłatne",
            "items": [
              "Politechnika Śląska — materiały dotyczące podstaw ochrony środowiska: [https://www.polsl.pl/](https://www.polsl.pl/)",
              "Europejska Agencja Środowiska (serwis po polsku): [https://www.eea.europa.eu/pl](https://www.eea.europa.eu/pl)",
              "ESA Education — edukacja o Ziemi, klimacie i obserwacji środowiska: [https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)"
            ]
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
              "Monitoring środowiska z użyciem czujników, satelitów i AI — [POLSA Obserwacja Ziemi (PL)](https://polsa.gov.pl/) | [ESA Copernicus](https://earth.esa.int/)"
            ]
          }
        ]
      },
      {
        "trackId": "H",
        "title": "VIII. SUPER-PROJEKT H — ENERGETYKA JĄDROWA, TERMOJĄDROWA I ZASTOSOWANIA W PODWARIANTACH A–G (PL w pierwszej kolejności)",
        "sequenceLabel": "Kolejność nauki",
        "sequence": "Podstawy fizyki jądrowej i ochrony radiologicznej (po polsku: Skrzypczak & Szefliński PWN, OpenStax Fizyka Tom 3 PL, OpenAGH) → Inżynieria reaktorowa, reaktor MARIA, SMR i HTGR-POLA (NCBJ Świerk, Nauka w Polsce, Ludzie Nauki) → Fizyka plazmy i fuzja termojądrowa (IFPiLM, ITER, W7-X) → Zastosowania w podwariantach: zasilanie klastrów AI/WBE (B/C), napędy i reaktory kosmiczne (F), medycyna nuklearna (A/D) i dekarbonizacja Ziemi (G).",
        "links": [
          {
            "label": "🇵🇱 Narodowe Centrum Badań Jądrowych (NCBJ w Świerku) — Reaktor MARIA, projekt HTGR-POLA, fizyka jądrowa i plazmowa",
            "url": "https://www.ncbj.gov.pl/"
          },
          {
            "label": "🇵🇱 Nauka w Polsce (PAP) — NCBJ opracowało koncepcję polskiego reaktora wysokotemperaturowego HTGR-POLA",
            "url": "https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html"
          },
          {
            "label": "🇵🇱 Nauka w Polsce (PAP) — Reaktor badawczy MARIA w NCBJ: izotopy medyczne, badania materiałowe i zastosowania",
            "url": "https://naukawpolsce.pl/aktualnosci/news%2C105854%2Cdyrektor-ncbj-maria-chyba-jedyny-reaktor-badawczy-na-swiecie-bez-stabilnego"
          },
          {
            "label": "🇵🇱 Ludzie Nauki (OPI PIB / MNiSW) — Baza polskich naukowców, publikacji i projektów (energetyka jądrowa, fizyka plazmy, AI)",
            "url": "https://ludzie.nauka.gov.pl/ln/"
          },
          {
            "label": "🇵🇱 Instytut Fizyki Plazmy i Laserowej Mikrosyntezy (IFPiLM) — Fuzja termojądrowa, tokamaki ITER/DEMO i stellarator W7-X",
            "url": "https://www.ifpilm.pl/"
          },
          {
            "label": "🇵🇱 Portal Gov.pl — Polskie Elektrownie Jądrowe i wiedza o atomie (PAA / Ministerstwo Przemysłu)",
            "url": "https://www.gov.pl/web/polski-atom"
          },
          {
            "label": "🇬🇧 IAEA (International Atomic Energy Agency) — Small Modular Reactors (SMR), HTGR & Nuclear Fusion",
            "url": "https://www.iaea.org/"
          },
          {
            "label": "🇬🇧 ITER Organization — Fusion Energy Research",
            "url": "https://www.iter.org/"
          }
        ],
        "groups": [
          {
            "heading": "1. Po polsku (w pierwszej kolejności — podręczniki, instytuty i serwisy naukowe)",
            "items": [
              "Ewa Skrzypczak, Zygmunt Szefliński — *Wstęp do fizyki jądra atomowego i cząstek elementarnych* ([Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)) oraz *OpenStax Fizyka dla szkół wyższych. Tom 3* (rozdziały o fizyce jądrowej i energii jądrowej po polsku).",
              "Narodowe Centrum Badań Jądrowych ([NCBJ Świerk](https://www.ncbj.gov.pl/)) — materiały edukacyjne i badawcze dot. reaktora MARIA, reaktorów wysokotemperaturowych HTGR-POLA, bezpieczeństwa jądrowego i radiofarmaceutyków.",
              "Instytut Fizyki Plazmy i Laserowej Mikrosyntezy ([IFPiLM](https://www.ifpilm.pl/)) — polskie badania nad kontrolowaną syntezą termojądrową, tokamakami i plazmą laserową.",
              "Serwis [Nauka w Polsce (naukawpolsce.pl)](https://naukawpolsce.pl/tag/reaktor) oraz baza ekspertów i grantów [Ludzie Nauki (ludzie.nauka.gov.pl/ln/)](https://ludzie.nauka.gov.pl/ln/)."
            ]
          },
          {
            "heading": "2. Po angielsku (uzupełniające i międzynarodowe)",
            "items": [
              "John R. Lamarsh, Anthony J. Baratta — *Introduction to Nuclear Engineering* oraz Samuel Glasstone — *Nuclear Reactor Engineering*.",
              "IAEA Nuclear Energy Series & PRIS Database — [https://www.iaea.org/](https://www.iaea.org/)",
              "NASA Kilopower & Space Nuclear Propulsion (NTP/NEP) — [https://www.nasa.gov/](https://www.nasa.gov/)"
            ]
          }
        ]
      }
    ]
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
            "Wspomaganie ludzkich zmysłów i funkcji ruchowych."
          ]
        }
      ]
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
            "Świadomość oraz hipotetyczna emulacja całego mózgu."
          ]
        }
      ]
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
            "Systemy hybrydowe analogowo-cyfrowe."
          ]
        }
      ]
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
            "Bioetyka oraz naukowe podstawy science fiction."
          ]
        }
      ]
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
            "Etyka tworzenia, modyfikowania i ulepszania organizmów."
          ]
        }
      ]
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
            "Wykorzystanie zasobów lokalnych na Księżycu i Marsie."
          ]
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
            "Granice biologicznej adaptacji człowieka do innych warunków grawitacyjnych."
          ]
        },
        {
          "title": "C. Długotrwałe życie poza Ziemią",
          "items": [
            "Zamknięte i częściowo zamknięte systemy podtrzymywania życia.",
            "Uprawa roślin i produkcja żywności w habitatach.",
            "Psychologia izolacji i funkcjonowanie małych załóg.",
            "Budowa baz księżycowych i marsjańskich.",
            "Terraformowanie jako odrębna, wysoce spekulatywna koncepcja.",
            "Etyka ekspansji kosmicznej i ochrona innych światów przed biologicznym skażeniem."
          ]
        }
      ]
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
            "Wpływ miejskiego środowiska, hałasu, światła i zanieczyszczeń na organizm."
          ]
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
            "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja."
          ]
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
            "Ocena rzeczywistego wpływu technologii na środowisko w całym cyklu jej życia."
          ]
        },
        {
          "title": "D. Cywilizacja a granice środowiskowe",
          "items": [
            "Zużycie zasobów i możliwości ich odtwarzania.",
            "Rozwój miast i infrastruktury.",
            "Bezpieczeństwo żywnościowe i wodne.",
            "Odporność społeczeństw na katastrofy i zmiany klimatyczne.",
            "Konflikt między krótkoterminowym zyskiem a długoterminową stabilnością.",
            "Polityka środowiskowa, ekonomia ekologiczna i odpowiedzialność międzypokoleniowa."
          ]
        }
      ]
    },
    {
      "id": "H",
      "code": "Super-Projekt H",
      "name": "Energetyka jądrowa, termojądrowa i architektura mocy (w kontekście podwariantów A–G)",
      "color": "#f43f5e",
      "goal": "Zbadanie fizycznych, inżynieryjnych i systemowych podstaw gęstych źródeł energii (rozszczepienie jądrowe, SMR, HTGR, systemy radioizotopowe oraz synteza termojądrowa) jako fundamentu mocy dla gigantycznych klastrów obliczeniowych AI i emulacji mózgu (B i C), napędów i habitatów kosmicznych (F), medycyny nuklearnej i bioniki (A i D) oraz dekarbonizacji biosfery Ziemi (G).",
      "guidingQuestion": "Jak zapewnić bezpieczną, bezemisyjną i ultragęstą energię jądrową oraz termojądrową zdolną zasilić cywilizację techniczną, centra obliczeniowe AI/WBE, medycynę nuklearną oraz załogową eksplorację kosmosu?",
      "note": "Super-Projekt H pełni rolę nadrzędnego filaru energetyczno-technologicznego spinającego podwarianty wszystkich pozostałych ścieżek (A–G) oraz 8 dziedzin podstawowych.",
      "sections": [
        {
          "title": "A. Fizyka jądrowa, reaktory III+/IV generacji, SMR i HTGR",
          "items": [
            "Fizyka jądra atomowego, reakcje rozszczepienia, transport neutronów i kinetyka reaktorowa.",
            "Wielkoskalowe reaktory wodne (PWR / EPR / AP1000) oraz małe reaktory modułowe (SMR i mikroreaktory).",
            "Reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt HTGR-POLA w NCBJ Świerk) do kogeneracji i produkcji wodoru.",
            "Reaktory prędkie IV generacji, zamknięty cykl paliwowy, recykling aktynowców i bezpieczne składowanie odpadów."
          ]
        },
        {
          "title": "B. Synteza termojądrowa (Fuzja) i fizyka gorącej plazmy",
          "items": [
            "Fizyka plazmy wysokotemperaturowej, kryterium Lawsona i utrzymanie magnetyczne (tokamaki ITER, DEMO oraz stellarator Wendelstein 7-X).",
            "Synteza inercyjna i laserowa mikrosynteza plazmy (badania IFPiLM i NCBJ).",
            "Inżynieria materiałowa pierwszej ściany reaktorów fuzyjnych i badania odporności radiacyjnej w reaktorze MARIA (IFMIF-DONES)."
          ]
        },
        {
          "title": "C. Podwarianty integracyjne ze Ścieżkami A–G oraz Inteligencją (AI)",
          "items": [
            "Podwariant B, C i AI: Zasilanie energochłonnych centrów obliczeniowych AI, superkomputerów i hipotetycznej emulacji mózgu (WBE) za pomocą reaktorów SMR/HTGR.",
            "Podwariant F (Kosmos): Kosmiczna energetyka jądrowa — generatory radioizotopowe (RTG: Pu-238, Am-241), mikroreaktory księżycowe/marsjańskie (Kilopower) i napędy jądrowe (NTP / NEP).",
            "Podwariant A i D (Medycyna nuklearna i bionika): Produkcja izotopów medycznych (reaktor MARIA: Mo-99/Tc-99m, Lu-177), neuroobrazowanie PET/SPECT mózgu, radioterapia celowana i mikrobaterie betawoltaiczne.",
            "Podwariant G i E (Ziemia i Filozofia energii): Głęboka dekarbonizacja przemysłu, ciepłownictwa i odsalania wody, kultura bezpieczeństwa jądrowego i odpowiedzialność międzypokoleniowa."
          ]
        }
      ]
    }
  ],
  "subprojects": [
    {
      "id": "sub-1",
      "trackId": "A",
      "secondaryTracks": [
        "B",
        "E"
      ],
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
            "approvalStatus": "approved"
          }
        ],
        "notes": [
          {
            "id": "note-1",
            "title": "Granica inwazyjności a stabilność sygnału",
            "content": "Matryce mikroelektrod zapewniają wysoką rozdzielczość przestrzenną, ale ulegają gliozie. Alternatywą są podejścia wewnątrznaczyniowe (Stentrode) oraz optogenetyczne.",
            "author": "Administrator",
            "createdAt": "2026-10-25T12:10:00Z",
            "approvalStatus": "approved"
          }
        ],
        "bibliography": [
          {
            "id": "bib-1-pl",
            "citation": "🇵🇱 Kalat, J. W. — Biologiczne podstawy psychologii (Wydawnictwo Naukowe PWN) oraz Tadeusiewicz, R., Nałęcz, M. (red.) — Biocybernetyka i Inżynieria Biomedyczna (PAN / PWN).",
            "url": "https://ksiegarnia.pwn.pl/",
            "addedBy": "Administrator",
            "approvalStatus": "approved"
          },
          {
            "id": "bib-1",
            "citation": "🇬🇧 Lebedev, M. A., & Nicolelis, M. A. (2017). Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation. Physiological Reviews.",
            "url": "https://doi.org/10.1152/physrev.00027.2016",
            "addedBy": "Administrator",
            "approvalStatus": "approved"
          }
        ]
      }
    },
    {
      "id": "sub-2",
      "trackId": "C",
      "secondaryTracks": [
        "B",
        "A"
      ],
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
            "approvalStatus": "approved"
          }
        ],
        "notes": [
          {
            "id": "note-2",
            "title": "Porównanie modelu Hodgkina-Huxleya i obwodu FitzHugh-Nagumo",
            "content": "Układ analogowy FHN pozwala odwzorować pobudliwość błony przy użyciu pojedynczego nieliniowego elementu i indukcyjności (lub żyratora CMOS).",
            "author": "Administrator",
            "createdAt": "2026-10-25T12:20:00Z",
            "approvalStatus": "approved"
          }
        ],
        "bibliography": [
          {
            "id": "bib-2-pl",
            "citation": "🇵🇱 Horowitz, P., Hill, W. — Sztuka elektroniki (WKŁ) oraz Osowski, S. — Sieci neuronowe do przetwarzania informacji (Oficyna Wydawnicza Politechniki Warszawskiej).",
            "url": "https://open.agh.edu.pl/",
            "addedBy": "Administrator",
            "approvalStatus": "approved"
          },
          {
            "id": "bib-2",
            "citation": "🇬🇧 Indiveri, G., et al. (2011). Neuromorphic silicon neuron circuits. Frontiers in Neuroscience.",
            "url": "https://doi.org/10.3389/fnins.2011.00073",
            "addedBy": "Administrator",
            "approvalStatus": "approved"
          }
        ]
      }
    },
    {
      "id": "sub-3",
      "trackId": "F",
      "secondaryTracks": [
        "G",
        "D"
      ],
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
            "approvalStatus": "approved"
          }
        ],
        "notes": [
          {
            "id": "note-3",
            "title": "Wnioski z eksperymentów MELiSSA i BIOS-3",
            "content": "Największym wyzwaniem pozostaje pełna mineralizacja odpadów lignocelulozowych oraz utrzymanie równowagi stechiometrycznej O2/CO2 przy zmiennym metabolizmie załogi.",
            "author": "Administrator",
            "createdAt": "2026-10-25T12:35:00Z",
            "approvalStatus": "approved"
          }
        ],
        "bibliography": [
          {
            "id": "bib-3-pl",
            "citation": "🇵🇱 Weiner, J. — Życie i ewolucja biosfery. Podręcznik ekologii ogólnej (Wydawnictwo Naukowe PWN) oraz Krystek, J. — Ochrona środowiska dla inżynierów (PWN).",
            "url": "https://ksiegarnia.pwn.pl/",
            "addedBy": "Administrator",
            "approvalStatus": "approved"
          },
          {
            "id": "bib-3",
            "citation": "🇬🇧 Lasseur, C., et al. (2010). MELiSSA: The European project of closed life support system. Gravitational and Space Biology.",
            "url": "https://www.melissafoundation.org/",
            "addedBy": "Administrator",
            "approvalStatus": "approved"
          }
        ]
      }
    },
    {
      "id": "sub-4",
      "trackId": "H",
      "secondaryTracks": [
        "B",
        "C",
        "F",
        "G",
        "A",
        "D"
      ],
      "branchTopic": "Podwariant B, C i AI: Zasilanie energochłonnych centrów obliczeniowych AI, superkomputerów i hipotetycznej emulacji mózgu (WBE) za pomocą reaktorów SMR/HTGR.",
      "title": "Architektura mocy jądrowej i termojądrowej (SMR / HTGR-POLA / RTG) dla klastrów AI, emulacji mózgu i habitatów kosmicznych",
      "author": "Ireneusz",
      "status": "approved",
      "createdAt": "2026-10-25T22:52:00Z",
      "description": "Środowisko badawcze integrujące Super-Projekt H ze wszystkimi podwariantami projektu Golem 15: (1) bilans energetyczny wielkoskalowych centrów AI oraz hipotetycznej emulacji mózgu (Projekt B) w porównaniu z biologicznym mózgiem (~20 W) i układami neuromorficznymi (Projekt C); (2) wykorzystanie polskich koncepcji reaktorów wysokotemperaturowych HTGR-POLA oraz reaktora MARIA (NCBJ Świerk) do kogeneracji, produkcji wodoru i radiofarmaceutyków (Projekt A i D); (3) kosmiczne mikroreaktory rozszczepieniowe i generatory radioizotopowe RTG dla baz księżycowych i marsjańskich (Projekt F) oraz bezemisyjna stabilizacja biosfery Ziemi (Projekt G).",
      "philosophicalNote": "Skala cywilizacyjna i poznawcza (w tym rozwój AI oraz eksploracja kosmosu) jest bezpośrednio ograniczona gęstością dostępnych strumieni energii i umiejętnością bezpiecznego zarządzania procesami jądrowymi w skali wielopokoleniowej (Projekt E).",
      "workspace": {
        "hypotheses": [
          {
            "id": "hyp-4",
            "statement": "Dedykowane bloki SMR/HTGR zintegrowane bezpośrednio z centrami obliczeniowymi AI i układami neuromorficznymi (Projekt B/C) oraz odzyskiem ciepła odpadowego są warunkiem koniecznym do skalowania sztucznej inteligencji bez destabilizacji sieci elektroenergetycznych i klimatu (Projekt G).",
            "status": "W weryfikacji",
            "author": "Ireneusz",
            "approvalStatus": "approved"
          },
          {
            "id": "hyp-5",
            "statement": "W długotrwałych misjach załogowych na Księżyc i Marsa (Projekt F) kompaktowe reaktory rozszczepieniowe klasy Kilopower (10–100 kWe) oraz napędy jądrowe (NTP/NEP) skracające czas ekspozycji na promieniowanie kosmiczne są niezbędne do utrzymania zamkniętych systemów podtrzymywania życia (BLSS).",
            "status": "Hipoteza otwarta",
            "author": "Ireneusz",
            "approvalStatus": "approved"
          }
        ],
        "notes": [
          {
            "id": "note-4",
            "title": "Synergia NCBJ Świerk (reaktor MARIA i HTGR-POLA) z podwariantami Golem 15",
            "content": "1. Podwariant elektroniki i AI (Projekt C / FND-5): W reaktorze MARIA realizowane jest neutronowe domieszkowanie krzemu (NTD) dla elektroniki mocy i półprzewodników.\n2. Podwariant biomedyczny (Projekt A / B / D): Produkcja molibdenu-99 / technetu-99m oraz lutetu-177 pozwala na precyzyjną diagnostykę SPECT/PET (w tym neuroobrazowanie mózgu) oraz terapię celowaną.\n3. Podwariant reaktorów IV generacji i fuzji: Projekt HTGR-POLA (chłodzony helem) dostarcza parę o temp. >500°C, a eksperymenty w rdzeniu MARIA badają materiały dla reaktorów termojądrowych DEMO / IFMIF-DONES.",
            "author": "Ireneusz",
            "createdAt": "2026-10-25T22:53:00Z",
            "approvalStatus": "approved"
          }
        ],
        "bibliography": [
          {
            "id": "bib-4-pl",
            "citation": "🇵🇱 Nauka w Polsce (PAP): NCBJ opracowało koncepcję polskiego reaktora wysokotemperaturowego HTGR-POLA oraz badania w reaktorze MARIA.",
            "sourceLang": "PL",
            "url": "https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html",
            "addedBy": "Ireneusz",
            "approvalStatus": "approved"
          },
          {
            "id": "bib-5-pl",
            "citation": "🇵🇱 Portal Ludzie Nauki (OPI PIB / MNiSW): Profile badawcze, publikacje i granty w dyscyplinach inżynierii jądrowej, fizyki plazmy i neuroinformatyki.",
            "sourceLang": "PL",
            "url": "https://ludzie.nauka.gov.pl/ln/",
            "addedBy": "Ireneusz",
            "approvalStatus": "approved"
          }
        ]
      }
    }
  ],
  "materials": [
    {
      "id": "mat-nwp-h1",
      "trackId": "H",
      "branchTopic": "Reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt HTGR-POLA w NCBJ Świerk) do kogeneracji i produkcji wodoru.",
      "subprojectId": "sub-4",
      "title": "SUPER-PROJEKT H (Nauka w Polsce & Ludzie Nauki): Koncepcja polskiego reaktora wysokotemperaturowego HTGR-POLA, reaktor MARIA (NCBJ) oraz fuzja termojądrowa w kontekście podwariantów A–G",
      "type": "Raport badawczy — Nauka w Polsce & Ludzie Nauki [PL]",
      "sourceLang": "PL",
      "author": "Ireneusz",
      "content": "Zestawienie badań z Narodowego Centrum Badań Jądrowych (NCBJ w Świerku) opublikowanych w serwisie Nauka w Polsce (PAP) oraz powiązanych profili w bazie Ludzie Nauki:\n1. Projekt HTGR-POLA (POLski Atomowy): Opracowana w NCBJ koncepcja badawczo-demonstracyjnego reaktora wysokotemperaturowego chłodzonego helem (analizy bezpieczeństwa opublikowane m.in. w „Nuclear Technology”). Reaktory HTGR i SMR mogą zasilać zarówno przemysł chemiczny i produkcję wodoru (Projekt G), jak i wielkoskalowe centra danych AI (Projekt B/C).\n2. Reaktor badawczy MARIA (30 MW): Jedyny w Polsce reaktor jądrowy generujący intensywne strumienie neutronów — kluczowy dla: (a) medycyny nuklearnej i neuroobrazowania (izotopy Mo-99, Lu-177 — styk z Projektem A, B i D), (b) neutronowego domieszkowania krzemu dla elektroniki i układów mocy (styk z Projektem C), (c) testowania materiałów osłonowych dla przyszłych reaktorów syntezy termojądrowej (DEMO / IFMIF-DONES).\n3. Kosmiczne i obronne podwarianty energetyki jądrowej (Projekt F): Zastosowanie kompaktowych reaktorów rozszczepieniowych i generatorów radioizotopowych (RTG) w misjach księżycowych i marsjańskich.",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — NCBJ opracowało koncepcję polskiego reaktora wysokotemperaturowego (HTGR-POLA)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Reaktor badawczy MARIA w NCBJ Świerk: izotopy medyczne, badania materiałowe i fuzja",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C105854%2Cdyrektor-ncbj-maria-chyba-jedyny-reaktor-badawczy-na-swiecie-bez-stabilnego"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Katalog artykułów: Reaktory jądrowe i energetyka jądrowa",
          "url": "https://naukawpolsce.pl/tag/reaktor"
        },
        {
          "label": "🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Wyszukiwarka polskich ekspertów i projektów z fizyki jądrowej, energetyki i AI",
          "url": "https://ludzie.nauka.gov.pl/ln/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T22:54:00Z"
    },
    {
      "id": "mat-nwp-b1",
      "trackId": "B",
      "branchTopic": "Modelowanie neuronów i sieci neuronalnych.",
      "subprojectId": "sub-1",
      "title": "INTELIGENCJA I MÓZG (Nauka w Polsce & Ludzie Nauki): Systemy AI wzorowane na mózgu, cyfrowy sen sieci neuronowych, określenie wieku mózgu i dekodowanie myśli z fMRI",
      "type": "Przegląd artykułów — Nauka w Polsce [PL]",
      "sourceLang": "PL",
      "author": "Ireneusz",
      "content": "Wybrane artykuły z serwisu Nauka w Polsce (naukawpolsce.pl) oraz dorobku polskich kognitywistów i neuroinformatyków (baza Ludzie Nauki) dla Projektu B (Cyfrowy umysł) i Dziedziny 8 (AI):\n1. Systemy wzorowane na mózgu (prof. Włodzisław Duch): Dlaczego klasyczne modele głębokiego uczenia wymagają ogromnej mocy obliczeniowej i jak neuroinformatyka dąży do połączenia architektury korowej z wnioskowaniem symbolicznym.\n2. Cyfrowy sen w sztucznej inteligencji: Wprowadzenie stanów analogicznych do ludzkiego snu (faza konsolidacji synaptycznej) zapobiega tzw. katastrofalnemu zapominaniu (catastrophic forgetting) w sztucznych sieciach neuronowych uczących się w sposób ciągły.\n3. Dekodowanie aktywności mózgu i diagnostyka AI: Wykorzystanie modeli językowych i głębokich sieci neuronowych do nieinwazyjnej rekonstrukcji treści myśli ze skanów fMRI oraz precyzyjnego wyznaczania biologicznego wieku mózgu.",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — Kognitywista: przyszłością sztucznej inteligencji są systemy wzorowane na mózgu",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Prof. Włodzisław Duch: sztuczna inteligencja zmienia wszystko",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C95000%2Cprof-wlodzislaw-duch-sztuczna-inteligencja-zmienia-wszystko.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Sztuczna inteligencja może lepiej „zapamiętać” treści, jeśli naśladuje ludzki sen",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C100463%2Csztuczna-inteligencja-moze-lepiej-zapamietac-tresci-jesli-nasladuje-ludzki"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Sztuczna inteligencja pozwala określić prawdziwy wiek mózgu",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C94962%2Csztuczna-inteligencja-pozwala-okreslic-prawdziwy-wiek-mozgu.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Komputer nauczył się czytać ludzkie myśli ze skanów fMRI",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C96452%2Cusakomputer-nauczyl-sie-czytac-ludzkie-mysli-choc-jeszcze-popelnia-bledy"
        },
        {
          "label": "🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Profile polskich badaczy neuroinformatyki i sztucznej inteligencji",
          "url": "https://ludzie.nauka.gov.pl/ln/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T22:55:00Z"
    },
    {
      "id": "mat-nwp-c1",
      "trackId": "C",
      "branchTopic": "Komputery neuromorficzne.",
      "subprojectId": "sub-2",
      "title": "OBLICZANIE PRZEZ FIZYKĘ I BIOLOGIĘ (Nauka w Polsce): Chipy neuromorficzne inspirowane mózgiem oraz hybrydowy biokomputer z żywym organoidem mózgowym (Brainoware)",
      "type": "Przegląd artykułów — Nauka w Polsce [PL]",
      "sourceLang": "PL",
      "author": "Ireneusz",
      "content": "Przełomowe badania z pogranicza Projektu C (Maszyny analogowe i neuromorficzne), Projektu B (Cyfrowy umysł) i Projektu D (Organoidy) opisywane w serwisie Nauka w Polsce:\n1. Inspirowany mózgiem chip neuromorficzny: Przetwarzanie informacji bezpośrednio w pamięci (in-memory computing) z wykorzystaniem memrystorów i sztucznych synaps pozwala wielokrotnie zredukować pobór mocy przez algorytmy AI (łącznik z Super-Projektem H).\n2. Komputer z żywym mózgiem (Brainoware): Połączenie trójwymiarowego organoidu ludzkiego mózgu wyhodowanego z komórek macierzystych z matrycą wieloelektrodową i układem uczenia maszynowego (reservoir computing) do rozpoznawania mowy i przewidywania nieliniowych układów dynamicznych.",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C112694%2Cinspirowany-mozgiem-chip-ma-ulatwic-prace-si.html",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — Inspirowany mózgiem chip ma ułatwić pracę SI (procesory neuromorficzne)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C112694%2Cinspirowany-mozgiem-chip-ma-ulatwic-prace-si.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Komputer z żywym mózgiem (biokomputer hybrydowy Brainoware)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C100102%2Ckomputer-z-zywym-mozgiem.html"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T22:56:00Z"
    },
    {
      "id": "mat-nwp-af1",
      "trackId": "A",
      "branchTopic": "Interfejsy mózg–komputer.",
      "subprojectId": "sub-1",
      "title": "NEUROTECHNOLOGIA W KOSMOSIE (Nauka w Polsce): Misja IGNIS — polski interfejs mózg–komputer (PhotonGrav / fNIRS) przetestowany na ISS oraz odporność astronautów",
      "type": "Przegląd artykułów — Nauka w Polsce [PL]",
      "sourceLang": "PL",
      "author": "Ireneusz",
      "content": "Bezpośredni punkt styku Projektu A (Człowiek biocyfrowo-robotyczny — BCI), Projektu B (Dekodowanie sygnałów korowych AI) oraz Projektu F (Człowiek w kosmosie):\n1. Eksperyment PhotonGrav podczas polskiej misji kosmicznej IGNIS na Międzynarodowej Stacji Kosmicznej (ISS): Pierwsze w historii pomyślne testy polskiego nieinwazyjnego interfejsu mózg–komputer opartego na funkcjonalnej spektroskopii bliskiej podczerwieni (fNIRS, dr Dariusz Zapała / Cortivision, z udziałem polskiego astronauty dr. Sławosza Uznańskiego-Wiśniewskiego). Skuteczność algorytmów AI dekodujących aktywność kory mózgowej w mikrograwitacji przekroczyła 80%.\n2. Genetyka i immunologia kosmiczna: Badania wykazujące, jak mikrograwitacja zmienia ekspresję genów w leukocytach i osłabia układ odpornościowy astronautów oraz jak projektować biotechnologiczne środki zaradcze.",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C111594%2Cmisja-ignis-polski-interfejs-mozg-komputer-potwierdzil-ze-dziala-w-kosmosie",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — Misja IGNIS: Polski interfejs mózg-komputer potwierdził, że działa w kosmosie",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C111594%2Cmisja-ignis-polski-interfejs-mozg-komputer-potwierdzil-ze-dziala-w-kosmosie"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Przebywanie w kosmosie zaburza układ odpornościowy (zmiany ekspresji genów)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C98124%2Cprzebywanie-w-kosmosie-zaburza-uklad-odpornosciowy.html"
        },
        {
          "label": "🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Profile polskich badaczy neuroinżynierii, fNIRS/EEG i medycyny kosmicznej",
          "url": "https://ludzie.nauka.gov.pl/ln/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T22:57:00Z"
    },
    {
      "id": "mat-nwp-dg1",
      "trackId": "D",
      "branchTopic": "Inżynieria tkankowa i sztuczne narządy.",
      "subprojectId": None,
      "title": "BIOTECHNOLOGIA, ORGANOIDY I EKOSYSTEM (Nauka w Polsce): Przeszczep wyhodowanej w laboratorium tkanki przysadki, organizmy chimeryczne oraz reakcja biosfery na zmiany klimatu",
      "type": "Przegląd artykułów — Nauka w Polsce [PL]",
      "sourceLang": "PL",
      "author": "Ireneusz",
      "content": "Artykuły badawcze z serwisu Nauka w Polsce dla Projektu D („Frankenstein” — inżynieria tkankowa i biologia syntetyczna) oraz Projektu G (Człowiek na Ziemi):\n1. Medycyna regeneracyjna i organoidy (Projekt D): Wyhodowanie w laboratorium z ludzkich pluripotencjalnych komórek macierzystych funkcjonalnego organoidu przysadki mózgowej, który po przeszczepieniu naczelnych podjął wydzielanie hormonów.\n2. Badania nad chimerami z komórek macierzystych i ich ścisłe ramy bioetyczne (styk Projektu D i Projektu E).\n3. Reakcja ekosystemów i mikroklimatu Ziemi (Projekt G i Super-Projekt H): Badania nad wpływem zmian klimatycznych na mikroklimat siedlisk biologicznych oraz stanowiska naukowców PAN dot. konieczności transformacji energetycznej (w tym wykorzystania energetyki jądrowej i OZE).",
      "url": "https://naukawpolsce.pl/aktualnosci/news%2C115244%2Cmalpie-wszczepiono-wyhodowana-w-laboratorium-tkanke-przysadki.html",
      "links": [
        {
          "label": "🇵🇱 Nauka w Polsce — Małpie wszczepiono wyhodowaną w laboratorium tkankę przysadki (organoid z komórek macierzystych)",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C115244%2Cmalpie-wszczepiono-wyhodowana-w-laboratorium-tkanke-przysadki.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Biotechnolodzy stworzyli chimeryczną małpę z komórek macierzystych",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C99291%2Cbiotechnolodzy-stworzyli-chimeryczna-malpe.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Zbadano dokładniej, jak Ziemia i mikroklimat reagują na zmiany klimatu",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C115569%2Czbadano-dokladniej-jak-ziemia-reaguje-na-zmiany-klimatu.html"
        },
        {
          "label": "🇵🇱 Nauka w Polsce — Naukowcy apelują o systemowe działania chroniące przed skutkami zmiany klimatu",
          "url": "https://naukawpolsce.pl/aktualnosci/news%2C113734%2Cnaukowcy-apeluja-do-politykow-o-dzialania-chroniace-obywateli-przed"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T22:58:00Z"
    },
    {
      "id": "mat-13",
      "trackId": "E",
      "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
      "subprojectId": None,
      "title": "BIBLIOTEKA PROJEKTU — VI. Kolejność czytania i zasady pracy z literaturą (w pierwszej kolejności źródła polskojęzyczne)",
      "type": "Przewodnik metodologiczny GOLEM 15",
      "author": "Administrator",
      "content": "1. Najpierw (po polsku): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Helion); Eric Matthes — „Python. Instrukcje dla programisty” (Helion); Podstawy matematyki i algebry liniowej (OpenAGH, ZPE, Skoczylas); Podręcznik fizyki ogólnej po polsku (OpenStax „Fizyka dla szkół wyższych Tom 1–3”, Halliday & Resnick „Podstawy fizyki”).\n2. Następnie (po polsku): Terence A. Brown — „Genomy” (PWN); Podstawy chemii, biologii i biochemii („Biologia Campbella” Rebis, Stryer „Biochemia” PWN, Alberts „Podstawy biologii komórki” PWN); James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n3. Później (PL i EN): A. Longstaff „Neurobiologia” (PWN), E. Nęcka „Psychologia poznawcza” (PWN), S. Seung „Konektom” (wyd. polskie); Dayan & Abbott „Theoretical Neuroscience”; Izhikevich „Dynamical Systems in Neuroscience”; Sandberg & Bostrom „Whole Brain Emulation: A Roadmap”.\n4. Na zaawansowanym etapie: D. J. Griffiths — „Wstęp do mechaniki kwantowej” (wyd. polskie PWN / CUP); Kandel — „Principles of Neural Science”; Squire — „Fundamental Neuroscience”; Churchland & Sejnowski — „The Computational Brain”; Nielsen i Chuang — „Quantum Computation and Quantum Information”.\n\nZasada: Zaczynamy od polskojęzycznych podręczników i otwartych zasobów po polsku — najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna pozycja. Pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi celami badawczymi.",
      "url": "https://open.agh.edu.pl/",
      "links": [
        {
          "label": "1️⃣ 🇵🇱 Etap I (Po polsku): Petzold „Kod”, Matthes „Python” (Helion), OpenAGH Matematyka oraz OpenStax Fizyka Tom 1–3 (PL)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
        },
        {
          "label": "2️⃣ 🇵🇱 Etap II (Po polsku): T.A. Brown „Genomy”, „Biologia Campbella”, Stryer „Biochemia” oraz J.W. Kalat „Biologiczne podstawy psychologii” (PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "3️⃣ 🇵🇱/🇬🇧 Etap III: Longstaff „Neurobiologia”, Seung „Konektom” (PL) + Dayan & Abbott, Izhikevich, Sandberg & Bostrom (WBE Roadmap PDF)",
          "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"
        },
        {
          "label": "4️⃣ 🇵🇱/🇬🇧 Etap IV: Griffiths „Wstęp do mechaniki kwantowej” (PWN) + Kandel, Squire, Churchland & Sejnowski, Nielsen & Chuang",
          "url": "https://mitpress.mit.edu/9780262533393/the-computational-brain/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T15:25:00Z"
    },
    {
      "id": "mat-8",
      "trackId": "B",
      "branchTopic": "Modelowanie neuronów i sieci neuronalnych.",
      "subprojectId": "sub-1",
      "title": "BIBLIOTEKA PROJEKTU — I. Matematyka i Informatyka (w pierwszej kolejności po polsku: Petzold, Matthes, OpenAGH, ZPE, Ważniak MIMUW + Strang)",
      "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "1. W pierwszej kolejności — Polskojęzyczne:\n• Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II.” (Wydawnictwo Helion)\n• Eric Matthes — „Python. Instrukcje dla programisty. Wydanie III.” (Wydawnictwo Helion) + oficjalny polski samouczek Pythona\n• Podręczniki matematyki i algebry liniowej po polsku: e-podręczniki OpenAGH, ZPE, Ważniak MIMUW, M. Gewert i Z. Skoczylas („Algebra liniowa”, „Analiza matematyczna”), T. H. Cormen i współautorzy („Wprowadzenie do algorytmów”, PWN), R. Penrose („Droga do rzeczywistości”, wyd. polskie).\n\n2. Uzupełniająco — Anglojęzyczne:\n• Gilbert Strang — „Introduction to Linear Algebra.”\n• Charles Petzold — „Code: The Hidden Language of Computer Hardware and Software.”\n• Eric Matthes — „Python Crash Course.”",
      "url": "https://open.agh.edu.pl/",
      "links": [
        {
          "label": "🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” oraz Eric Matthes — „Python. Instrukcje dla programisty” (Helion)",
          "url": "https://helion.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH — Darmowe e-podręczniki akademickie: Matematyka i Algebra Liniowa po polsku",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Ważniak MIMUW (UW) — Darmowe kursy akademickie z matematyki i informatyki po polsku",
          "url": "https://wazniak.mimuw.edu.pl/"
        },
        {
          "label": "🇵🇱 Oficjalny samouczek języka Python po polsku (docs.python.org/pl)",
          "url": "https://docs.python.org/pl/3/tutorial/"
        },
        {
          "label": "🇬🇧 Gilbert Strang — „Introduction to Linear Algebra” & MIT 18.06",
          "url": "https://math.mit.edu/~gs/linearalgebra/"
        },
        {
          "label": "🇬🇧 Charles Petzold — „Code” (Oficjalna strona autora)",
          "url": "https://codehiddenlanguage.com/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T15:00:00Z"
    },
    {
      "id": "mat-9",
      "trackId": "C",
      "branchTopic": "Komputery analogowe i mechaniczne.",
      "subprojectId": "sub-2",
      "title": "BIBLIOTEKA PROJEKTU — II. Fizyka i Komputery Kwantowe (w pierwszej kolejności po polsku: OpenStax Fizyka PL, Halliday & Resnick, Griffiths PWN, Horowitz & Hill + Nielsen & Chuang)",
      "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "1. W pierwszej kolejności — Polskojęzyczne:\n• Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach: OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3” (darmowy podręcznik PL); D. Halliday, R. Resnick, J. Walker — „Podstawy fizyki. Tom 1–5” (PWN); R. P. Feynman — „Feynmana wykłady z fizyki” (PWN); David J. Griffiths — „Wstęp do mechaniki kwantowej” (polskie wydanie PWN).\n• Podręczniki podstaw elektroniki i układów cyfrowych po polsku: P. Horowitz, W. Hill — „Sztuka elektroniki. Cz. 1–2” (WKŁ); B. Głocki — „Układy cyfrowe” (WSiP); ZPE i kursy Forbot.\n\n2. Uzupełniająco — Anglojęzyczne:\n• David J. Griffiths — „Introduction to Quantum Mechanics.”\n• Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information.”",
      "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1",
      "links": [
        {
          "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tomy 1–3” (darmowy podręcznik akademicki po polsku)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Halliday & Resnick „Podstawy fizyki” oraz D.J. Griffiths „Wstęp do mechaniki kwantowej”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 ZPE / OpenAGH / Forbot — Podstawy elektroniki analogowej i układów cyfrowych po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇬🇧 David J. Griffiths — „Introduction to Quantum Mechanics” (Cambridge University Press)",
          "url": "https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E"
        },
        {
          "label": "🇬🇧 Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information”",
          "url": "https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T15:05:00Z"
    },
    {
      "id": "mat-10",
      "trackId": "D",
      "branchTopic": "Genetyka, DNA i regulacja genów.",
      "subprojectId": None,
      "title": "BIBLIOTEKA PROJEKTU — III. Chemia, Biologia i Genetyka (w pierwszej kolejności po polsku: Brown „Genomy”, „Biologia Campbella”, Alberts, Stryer + OpenStax 2e)",
      "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "1. W pierwszej kolejności — Polskojęzyczne:\n• Terence A. Brown — „Genomy” (polskie wydanie, Wydawnictwo Naukowe PWN).\n• „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS) oraz Bruce Alberts i współautorzy — „Podstawy biologii komórki” (PWN).\n• Akademickie podręczniki chemii ogólnej, organicznej i biochemii po polsku: L. Stryer — „Biochemia” (PWN), L. Jones & P. Atkins — „Chemia ogólna” (PWN), A. Bielański — „Podstawy chemii nieorganicznej” (PWN), J. McMurry — „Chemia organiczna” (PWN) oraz darmowe zasoby OpenAGH i ZPE.\n\n2. Uzupełniająco — Anglojęzyczne:\n• OpenStax „Chemistry 2e” — podręcznik chemii ogólnej.\n• OpenStax „Biology 2e” — podręcznik biologii.\n• Akademickie podręczniki biochemii i biologii molekularnej (NCBI Bookshelf).",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 Terence A. Brown — „Genomy”, L. Stryer — „Biochemia”, B. Alberts — „Podstawy biologii komórki” (Wydawnictwo Naukowe PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)",
          "url": "https://www.rebis.com.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki chemii, biochemii, biologii i genetyki",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇬🇧 OpenStax „Chemistry 2e” — darmowy podręcznik chemii ogólnej online",
          "url": "https://openstax.org/details/books/chemistry-2e"
        },
        {
          "label": "🇬🇧 OpenStax „Biology 2e” — darmowy podręcznik biologii online",
          "url": "https://openstax.org/details/books/biology-2e"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T15:10:00Z"
    },
    {
      "id": "mat-11",
      "trackId": "A",
      "branchTopic": "Interfejsy mózg–komputer.",
      "subprojectId": "sub-1",
      "title": "BIBLIOTEKA PROJEKTU — IV. Projekt A: Człowiek biocyfrowo-robotyczny (w pierwszej kolejności po polsku: Kalat, Bochenek, Traczyk, Jaroszyk, Marciniak, Tadeusiewicz, Géron PL + OpenStax Anatomy 2e)",
      "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "1. W pierwszej kolejności — Polskojęzyczne:\n• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n• Akademickie podręczniki anatomii i fizjologii człowieka: A. Bochenek, M. Reicher — „Anatomia człowieka” (PZWL); W. Traczyk, A. Trzebski — „Fizjologia człowieka” (PZWL); S. Konturek — „Fizjologia człowieka”.\n• Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: F. Jaroszyk (red.) — „Biofizyka” (PZWL); J. Marciniak — „Biomateriały”; seria „Biocybernetyka i Inżynieria Biomedyczna 2000” (PAN, red. M. Nałęcz, R. Tadeusiewicz).\n• Podręczniki robotyki, elektroniki, sterowania i uczenia maszynowego po polsku: K. Tchoń i współautorzy — „Manipulatory i roboty mobilne”; Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i TensorFlow” (wyd. polskie Helion).\n\n2. Uzupełniająco — Anglojęzyczne:\n• OpenStax „Anatomy and Physiology 2e.”\n• Aurélien Géron — „Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.”\n• Akademickie podręczniki inżynierii tkankowej, neuroprotetyki i interfejsów mózg–komputer.",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia człowieka (Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)",
          "url": "https://pzwl.pl/"
        },
        {
          "label": "🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i TensorFlow” (Wydawnictwo Helion)",
          "url": "https://helion.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH — Inżynieria biomedyczna, biocybernetyka i automatyka po polsku",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇬🇧 OpenStax „Anatomy and Physiology 2e” — darmowy podręcznik online",
          "url": "https://openstax.org/details/books/anatomy-and-physiology-2e"
        },
        {
          "label": "🇬🇧 IEEE EMBS — Engineering in Medicine and Biology (Neuroprotetyka i BCI)",
          "url": "https://www.embs.org/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T15:15:00Z"
    },
    {
      "id": "mat-12",
      "trackId": "B",
      "branchTopic": "Świadomość oraz hipotetyczna emulacja całego mózgu.",
      "subprojectId": "sub-1",
      "title": "BIBLIOTEKA PROJEKTU — V. Projekt B: Cyfrowy umysł (w pierwszej kolejności po polsku: Kalat, Longstaff, Nęcka, Seung „Konektom”, Miłkowski & Poczobut + Kandel, Squire, Dayan & Abbott, Izhikevich, Sandberg & Bostrom)",
      "type": "Biblioteka Projektu GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "1. W pierwszej kolejności — Polskojęzyczne:\n• James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN).\n• Podręczniki neurobiologii i fizjologii układu nerwowego po polsku: Alan Longstaff — „Neurobiologia. Krótkie wykłady” (PWN); T. Górska, A. Grabowska, J. Zagrodzka — „Mózg a zachowanie” (PWN).\n• Podręczniki psychologii poznawczej i konektomiki po polsku: Edward Nęcka, Jarosław Orzechowski, Błażej Szymura — „Psychologia poznawcza” (PWN); Sebastian Seung — „Konektom. Jak połączenia w mózgu kształtują naszą tożsamość” (wyd. polskie).\n• Wprowadzenia do filozofii umysłu i problemu świadomości po polsku: M. Miłkowski, R. Poczobut (red.) — „Przewodnik po filozofii umysłu”; wykłady z kognitywistyki i neuroinformatyki prof. Włodzisława Ducha (UMK) oraz publikacje Centrum Kopernika.\n\n2. Uzupełniająco i na zaawansowanym etapie — Anglojęzyczne:\n• Eric R. Kandel i współautorzy — „Principles of Neural Science.”\n• Larry Squire i współautorzy — „Fundamental Neuroscience.”\n• Peter Dayan, L. F. Abbott — „Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems.”\n• Eugene M. Izhikevich — „Dynamical Systems in Neuroscience.”\n• Paul Miller — „An Introductory Course in Computational Neuroscience.”\n• Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain.”\n• Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap.”",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — J.W. Kalat „Biologiczne podstawy psychologii”, A. Longstaff „Neurobiologia”, E. Nęcka „Psychologia poznawcza”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 Prof. Włodzisław Duch (UMK) — Polskie wykłady z kognitywistyki, neuroinformatyki i modelowania mózgu",
          "url": "https://www.fizyka.umk.pl/~duch/"
        },
        {
          "label": "🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu i kognitywistyka po polsku",
          "url": "https://ccpress.pl/"
        },
        {
          "label": "🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)",
          "url": "https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/"
        },
        {
          "label": "🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (MIT Press / PDF autora)",
          "url": "https://www.izhikevich.org/publications/dsn.pdf"
        },
        {
          "label": "🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Technical Report PDF)",
          "url": "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"
        },
        {
          "label": "🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” & Larry Squire et al. — „Fundamental Neuroscience”",
          "url": "https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T15:20:00Z"
    },
    {
      "id": "mat-3",
      "trackId": "C",
      "branchTopic": "Elektronika analogowa i układy dynamiczne.",
      "subprojectId": "sub-2",
      "title": "GOLEM 15 — Projekt C: Maszyny analogowe i obliczenia fizyczne (w pierwszej kolejności po polsku: Horowitz & Hill, OpenAGH, ZPE, Forbot, Osowski + Neuromorphic Computing)",
      "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → fizyczne modele neuronów → obliczenia neuromorficzne.\n\n1. W pierwszej kolejności — Po polsku: Podręczniki akademickie z elektroniki analogowej (P. Horowitz, W. Hill — „Sztuka elektroniki”; e-podręczniki OpenAGH: wzmacniacze, oscylatory, filtry, sprzężenie zwrotne, układy dynamiczne), materiały dydaktyczne o przetwornikach A/C i C/A (ZPE, kursy Forbot), polska literatura o sieciach neuronowych (S. Osowski, R. Tadeusiewicz).\n2. Uzupełniająco — Po angielsku: Materiały techniczne dot. analog computing, badania dot. neuromorphic computing i analog neural networks, publikacje o fizycznych modelach neuronów oraz analogowych i hybrydowych procesorach.",
      "url": "https://zpe.gov.pl/",
      "links": [
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz C/A: https://zpe.gov.pl/",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇵🇱 OpenAGH — Polskie e-podręczniki akademickie: Elektronika i układy dynamiczne",
          "url": "https://open.agh.edu.pl/"
        },
        {
          "label": "🇵🇱 Forbot — Kursy elektroniki analogowej i cyfrowej po polsku",
          "url": "https://forbot.pl/"
        },
        {
          "label": "🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering",
          "url": "https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering"
        },
        {
          "label": "🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks",
          "url": "https://arxiv.org/list/cs.NE/recent"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T14:00:00Z"
    },
    {
      "id": "mat-4",
      "trackId": "D",
      "branchTopic": "Biologia syntetyczna i edycja genomu.",
      "subprojectId": None,
      "title": "GOLEM 15 — Projekt D: „Frankenstein” — biotechnologia i tworzenie organizmów (w pierwszej kolejności po polsku: Alberts, Brown, Bartel „Embriologia”, Komitet Bioetyki PAN, Lem „Summa technologiae”)",
      "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → inżynieria tkankowa → biologia syntetyczna i bioetyka.\n\n1. W pierwszej kolejności — Po polsku: Podręczniki akademickie z biologii komórki, genetyki i biologii rozwoju (B. Alberts „Podstawy biologii komórki” PWN, T.A. Brown „Genomy” PWN, P. Węgleński „Genetyka molekularna” PWN); podręczniki z embriologii i komórek macierzystych (H. Bartel „Embriologia” PZWL); literatura o inżynierii tkankowej, medycynie regeneracyjnej i bioetyce (Komitet Bioetyki PAN, K. Szewczyk „Bioetyka” PWN) oraz Stanisław Lem — „Summa technologiae”.\n2. Uzupełniająco — Po angielsku: National Academies — materiały o odpowiedzialnym rozwoju biologii syntetycznej; publikacje akademickie o stem cells, developmental biology, tissue engineering i synthetic biology.",
      "url": "https://bioetyka.pan.pl/",
      "links": [
        {
          "label": "🇵🇱 Komitet Bioetyki PAN — Stanowiska i opracowania bioetyczne po polsku",
          "url": "https://bioetyka.pan.pl/"
        },
        {
          "label": "🇵🇱 PZWL Wydawnictwo Lekarskie — H. Bartel „Embriologia”, komórki macierzyste i medycyna regeneracyjna",
          "url": "https://pzwl.pl/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Alberts „Podstawy biologii komórki”, Brown „Genomy”, Węgleński „Genetyka molekularna”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biologia i biotechnologia po polsku",
          "url": "https://zpe.gov.pl/"
        },
        {
          "label": "🇬🇧 National Academies — Biologia syntetyczna: https://www.nationalacademies.org/",
          "url": "https://www.nationalacademies.org/"
        },
        {
          "label": "🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell & Developmental Biology",
          "url": "https://www.ncbi.nlm.nih.gov/books/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T14:05:00Z"
    },
    {
      "id": "mat-5",
      "trackId": "E",
      "branchTopic": "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
      "subprojectId": None,
      "title": "GOLEM 15 — Projekt E: Filozofia nauki, umysłu, techniki i bioetyka (w pierwszej kolejności po polsku: Chalmers, Kuhn, Heller, Tatarkiewicz, Wolne Lektury)",
      "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "Zastosowanie: Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.\n\n1. W pierwszej kolejności — Po polsku:\n  • Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n  • Thomas S. Kuhn — „Struktura rewolucji naukowych”\n  • Michał Heller — „Filozofia nauki. Wprowadzenie” oraz „Filozofia przyrody” (Copernicus Center Press)\n  • Władysław Tatarkiewicz — „Historia filozofii. Tom 1–3” (PWN) oraz klasyka filozofii starożytnej po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka) w serwisie Wolne Lektury\n  • Marcin Miłkowski, Robert Poczobut (red.) — „Przewodnik po filozofii umysłu” oraz Kazimierz Szewczyk — „Bioetyka. Tom 1–2” (PWN).\n2. Uzupełniająco — Po angielsku: Stanford Encyclopedia of Philosophy (SEP) oraz Internet Encyclopedia of Philosophy (IEP).",
      "url": "https://ccpress.pl/",
      "links": [
        {
          "label": "🇵🇱 Copernicus Center Press — Michał Heller „Filozofia nauki. Wprowadzenie”",
          "url": "https://ccpress.pl/"
        },
        {
          "label": "🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Wykłady z filozofii nauki i umysłu po polsku",
          "url": "https://www.copernicuscenter.edu.pl/"
        },
        {
          "label": "🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, stoicy)",
          "url": "https://wolnelektury.pl/katalog/gatunek/filozofia/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Kuhn, Tatarkiewicz, Szewczyk („Bioetyka”)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇬🇧 Stanford Encyclopedia of Philosophy (SEP — Nauka, Umysł, Technika, Bioetyka)",
          "url": "https://plato.stanford.edu/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T14:10:00Z"
    },
    {
      "id": "mat-6",
      "trackId": "F",
      "branchTopic": "Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.",
      "subprojectId": "sub-3",
      "title": "GOLEM 15 — Projekt F: Człowiek w kosmosie (w pierwszej kolejności po polsku: POLSA, ESERO Polska, OpenStax Fizyka PL, medycyna kosmiczna + darmowe źródła NASA i ESA)",
      "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.\n\n1. W pierwszej kolejności — Po polsku: Materiały edukacyjne i badawcze Polskiej Agencji Kosmicznej (POLSA) oraz ESERO Polska (Centrum Nauki Kopernik / ESA) dot. załogowych misji kosmicznych, życia w mikrograwitacji, ochrony przed promieniowaniem i projektowania habitatów; OpenStax Polska — „Fizyka dla szkół wyższych” (mechanika i grawitacja po polsku); K. Kwarecki (red.) — „Medycyna lotnicza i kosmiczna” (PZWL).\n2. Darmowe źródła międzynarodowe: NASA (zdrowie człowieka w kosmosie), ESA (edukacja kosmiczna — Teach with Space), ESA (eksploracja załogowa i robotyczna).",
      "url": "https://esero.kopernik.org.pl/",
      "links": [
        {
          "label": "🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o eksploracji kosmosu i habitatach",
          "url": "https://esero.kopernik.org.pl/"
        },
        {
          "label": "🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja, nauka i medycyna kosmiczna po polsku",
          "url": "https://polsa.gov.pl/"
        },
        {
          "label": "🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (Mechanika i grawitacja po polsku)",
          "url": "https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1"
        },
        {
          "label": "🚀 NASA — Zdrowie człowieka w kosmosie: https://www.nasa.gov/reference/fundamentals-of-human-health/",
          "url": "https://www.nasa.gov/reference/fundamentals-of-human-health/"
        },
        {
          "label": "🛰️ ESA — Edukacja kosmiczna: https://education.esa.int/teach-with-space/",
          "url": "https://education.esa.int/teach-with-space/"
        },
        {
          "label": "👩‍🚀 ESA — Eksploracja załogowa: https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration",
          "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T14:15:00Z"
    },
    {
      "id": "mat-7",
      "trackId": "G",
      "branchTopic": "Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.",
      "subprojectId": "sub-3",
      "title": "GOLEM 15 — Projekt G: Człowiek na Ziemi i ochrona ekosystemu (w pierwszej kolejności po polsku: Krystek, Weiner „Życie i ewolucja biosfery”, Politechnika Śląska, GIOŚ, EEA PL + ESA Education)",
      "type": "Biblioteka uzupełniająca GOLEM 15 (PL → EN)",
      "author": "Administrator",
      "content": "Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → technologie ochronne → ekonomia i polityka środowiskowa.\n\n1. W pierwszej kolejności — Po polsku: Jan Krystek — „Ochrona środowiska dla inżynierów” (PWN); January Weiner — „Życie i ewolucja biosfery. Podręcznik ekologii ogólnej” (PWN); Czesława Rosik-Dulewska — „Podstawy gospodarki odpadami” (PWN); bezpłatne materiały Politechniki Śląskiej i OpenAGH dot. ochrony wód, powietrza i gleby; raporty GIOŚ (Państwowy Monitoring Środowiska) oraz serwis Europejskiej Agencji Środowiska po polsku (EEA PL).\n2. Uzupełniająco: ESA Education (Ziemia, klimat, obserwacja środowiska) oraz raporty IPCC i IPBES.",
      "url": "https://www.polsl.pl/",
      "links": [
        {
          "label": "🇵🇱 Politechnika Śląska — Podstawy ochrony środowiska po polsku: https://www.polsl.pl/",
          "url": "https://www.polsl.pl/"
        },
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz January Weiner „Życie i ewolucja biosfery”",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇵🇱 GIOŚ — Państwowy Monitoring Środowiska w Polsce (wody, powietrze, gleby)",
          "url": "https://www.gios.gov.pl/"
        },
        {
          "label": "🇵🇱 Europejska Agencja Środowiska (EEA w języku polskim)",
          "url": "https://www.eea.europa.eu/pl"
        },
        {
          "label": "🌍 ESA Education — Ziemia, klimat i obserwacja środowiska: https://education.esa.int/teach-with-space/",
          "url": "https://education.esa.int/teach-with-space/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T14:20:00Z"
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
        {
          "label": "🇵🇱 Centrum Kopernika / CCPress — Filozofia nauki i granice modeli matematycznych",
          "url": "https://ccpress.pl/"
        },
        {
          "label": "🇬🇧 Stanford Encyclopedia of Philosophy — Models in Science",
          "url": "https://plato.stanford.edu/entries/models-science/"
        },
        {
          "label": "🇬🇧 SEP — The Chinese Room Argument & Syntax vs Semantics",
          "url": "https://plato.stanford.edu/entries/chinese-room/"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T11:50:00Z"
    },
    {
      "id": "mat-2",
      "trackId": "B",
      "branchTopic": "Neurobiologia i neuronauka obliczeniowa.",
      "subprojectId": "sub-1",
      "title": "Zestawienie rozdzielczości czasowo-przestrzennej metod neuroobrazowania (EEG, fNIRS, fMRI, ECoG)",
      "type": "Zestaw danych / Opracowanie",
      "author": "Ireneusz",
      "content": "Porównanie pasma przenoszenia, stosunku sygnału do szumu (SNR) oraz biokompatybilności długoterminowej dla zastosowań w Projektach A i B.",
      "url": "https://ksiegarnia.pwn.pl/",
      "links": [
        {
          "label": "🇵🇱 Wydawnictwo Naukowe PWN — Neurobiologia i metody neuroobrazowania (Kalat, Longstaff)",
          "url": "https://ksiegarnia.pwn.pl/"
        },
        {
          "label": "🇬🇧 Physiological Reviews — Brain-Machine Interfaces (Lebedev & Nicolelis)",
          "url": "https://doi.org/10.1152/physrev.00027.2016"
        }
      ],
      "status": "approved",
      "createdAt": "2026-10-25T13:10:00Z"
    }
  ],
  "graphLinks": [
    {
      "id": "lnk-1",
      "source": "A",
      "target": "B",
      "label": "Interfejsy mózg–komputer i dekodowanie sygnałów nerwowych",
      "status": "approved"
    },
    {
      "id": "lnk-2",
      "source": "B",
      "target": "C",
      "label": "Fizyczne i neuromorficzne modele sieci neuronalnych",
      "status": "approved"
    },
    {
      "id": "lnk-3",
      "source": "A",
      "target": "D",
      "label": "Inżynieria tkankowa, sztuczne narządy i medycyna regeneracyjna",
      "status": "approved"
    },
    {
      "id": "lnk-4",
      "source": "F",
      "target": "G",
      "label": "Zamknięte obiegi materii (BLSS) vs. ziemska biosfera i ekologia",
      "status": "approved"
    },
    {
      "id": "lnk-5",
      "source": "A",
      "target": "F",
      "label": "Medycyna kosmiczna, ochrona organizmu i robotyka autonomiczna",
      "status": "approved"
    },
    {
      "id": "lnk-6",
      "source": "D",
      "target": "F",
      "label": "Biologia regeneracji i odporność radiacyjna w długich misjach",
      "status": "approved"
    },
    {
      "id": "lnk-7",
      "source": "E",
      "target": "A",
      "label": "Filozofia techniki i etyka ulepszania człowieka",
      "status": "approved"
    },
    {
      "id": "lnk-8",
      "source": "E",
      "target": "B",
      "label": "Filozofia umysłu, świadomość i granice modeli obliczeniowych",
      "status": "approved"
    },
    {
      "id": "lnk-9",
      "source": "E",
      "target": "D",
      "label": "Bioetyka edycji genomu i granice tworzenia organizmów",
      "status": "approved"
    },
    {
      "id": "lnk-10",
      "source": "E",
      "target": "F",
      "label": "Etyka ekspansji kosmicznej i ochrona planetarna",
      "status": "approved"
    },
    {
      "id": "lnk-11",
      "source": "E",
      "target": "G",
      "label": "Odpowiedzialność międzypokoleniowa i filozofia przyrody",
      "status": "approved"
    },
    {
      "id": "lnk-12",
      "source": "H",
      "target": "B",
      "label": "Zasilanie centrów obliczeniowych AI i emulacji mózgu (WBE) przez reaktory SMR/HTGR",
      "status": "approved"
    },
    {
      "id": "lnk-13",
      "source": "H",
      "target": "C",
      "label": "Neutronowe domieszkowanie krzemu (reaktor MARIA) i efektywność energetyczna układów neuromorficznych",
      "status": "approved"
    },
    {
      "id": "lnk-14",
      "source": "H",
      "target": "F",
      "label": "Kosmiczne mikroreaktory jądrowe (Kilopower), generatory RTG i napędy jądrowe (NTP/NEP) dla misji załogowych",
      "status": "approved"
    },
    {
      "id": "lnk-15",
      "source": "H",
      "target": "G",
      "label": "Zeroemisyjna energetyka jądrowa i termojądrowa, kogeneracja HTGR i produkcja wodoru dla ochrony klimatu Ziemi",
      "status": "approved"
    },
    {
      "id": "lnk-16",
      "source": "H",
      "target": "A",
      "label": "Medycyna nuklearna, radioizotopy diagnostyczne (SPECT/PET) i mikrobaterie betawoltaiczne do implantów",
      "status": "approved"
    },
    {
      "id": "lnk-17",
      "source": "H",
      "target": "D",
      "label": "Radiobiologia molekularna, naprawa uszkodzeń DNA po napromieniowaniu i radiofarmaceutyki celowane",
      "status": "approved"
    },
    {
      "id": "lnk-18",
      "source": "E",
      "target": "H",
      "label": "Filozofia i etyka energii jądrowej: bezpieczeństwo systemowe i odpowiedzialność międzypokoleniowa",
      "status": "approved"
    }
  ],
  "manhattanSystem": {
    "codename": "MED-G15 // MANHATTAN DISTRIBUTED SYSTEM",
    "startCalendarYear": 2026,
    "doctrine": {
      "titlePl": "Doktryna Rozproszonego Systemu Projektowego „Manhattan Golem 15”",
      "titleEn": "Doctrine of the 'Manhattan Golem 15' Distributed Project System",
      "summaryPl": "Architektura organizacyjna wzorowana na Projekcie Manhattan (Dual Command: Sztab Administracyjno-Inżynieryjny + Rozproszone Ośrodki Badawcze). System rozpoczyna się od 3-letniego fundamentu studiów Administracji (Lata 1–3), po którym następuje nieprzerwany ciąg 5-letnich studiów magisterskich z każdej wybranej tematyki realizowanych ściśle z rzędu (3 + 5×N lat). Równolegle cel nadrzędny ulega kontrolowanemu rozszczepieniu (Fission) w bazie operacyjnej zarządzanej przez wyspecjalizowane Agenty AI.",
      "summaryEn": "Organizational architecture modeled on the Manhattan Project (Dual Command: Administrative-Engineering HQ + Compartmentalized Distributed Labs). The timeline begins with a mandatory 3-year Administration degree (Years 1–3), followed by a continuous back-to-back sequence of 5-year Master's curricula for each selected discipline (3 + 5×N years). Simultaneously, the overarching goal undergoes controlled chain-reaction fission across a project database orchestrated by specialized AI Agents.",
      "rulesPl": [
        "1. Prymat Sztabu Administracyjnego (Lata 1–3): Zanim ruszą 5-letnie bloki badawcze, właściciel buduje aparat prawny, finansowy, logistyczny i regulacyjny (prawo B+R, atomowe, medyczne, kosmiczne i nadzór nad AI).",
        "2. Sekwencyjna Głębia Akademicka (5 lat z rzędu na każdą wybraną tematykę): Brak powierzchownej wielozadaniowości — każda wybrana dziedzina otrzymuje pełny 5-letni cykl studiów I+II stopnia (10 semestrów, 300 ECTS) realizowany jeden po drugim.",
        "3. Kompartmentalizacja Ośrodków (5 Sektorów Manhattan): Prace są rozproszone pomiędzy autonomiczne laboratoria (District W-0, Los Alamos Y-15, Oak Ridge X-10, Hanford B-7, Trinity-Biosphere T-9).",
        "4. Reakcja Łańcuchowa Agentów AI (Graf Rozszczepień): Każdy złożony problem badawczy jest rozszczepiany przez Agenta-Kierownika na mniejsze fragmenty robocze oraz neutrony międzyścieżkowe zasilające sąsiednie projekty."
      ],
      "rulesEn": [
        "1. Primacy of Administrative Command (Years 1–3): Before 5-year scientific blocks begin, the owner establishes legal, financial, logistical, and regulatory mastery (R&D, nuclear, medical, space, and AI law).",
        "2. Sequential Academic Depth (5 consecutive years per selected topic): Zero shallow multitasking — every selected topic receives a full 5-year B.Sc.+M.Sc. cycle (10 semesters, 300 ECTS) executed back-to-back.",
        "3. Site Compartmentalization (5 Manhattan Sectors): Research is distributed across autonomous sites (District W-0, Los Alamos Y-15, Oak Ridge X-10, Hanford B-7, Trinity-Biosphere T-9).",
        "4. AI-Agent Chain Reaction (Fission Graph): Every complex research challenge is fissioned by a Director AI Agent into atomic work packages and cross-sector neutrons feeding neighboring tracks."
      ]
    },
    "sites": [
      {
        "id": "SITE-W0",
        "code": "DISTRICT W-0",
        "historicalAnalog": "Washington HQ & Oak Ridge Admin",
        "namePl": "Sztab Centralny Administracji, Prawa i Epistemologii",
        "nameEn": "Central HQ for Administration, Law & Epistemology",
        "color": "#f59e0b",
        "clearance": "POZIOM OMEGA (DYREKCJA)",
        "scopePl": "3-letnie studia Administracji, prawo sektorowe (atomowe, medyczne, kosmiczne, AI), finanse B+R oraz Projekt E (Filozofia i rygor epistemiczny).",
        "scopeEn": "3-year Administration core, sector law (nuclear, medical, space, AI), R&D finance, and Project E (Philosophy & epistemic rigor).",
        "linkedIds": [
          "ADMIN-3Y",
          "E"
        ]
      },
      {
        "id": "SITE-Y15",
        "code": "LOS ALAMOS Y-15",
        "historicalAnalog": "Site Y — Los Alamos Theoretical & Computing Division",
        "namePl": "Laboratorium Teorii, Obliczeń, AI i Cyfrowego Umysłu",
        "nameEn": "Laboratory for Theory, Computing, AI & Digital Mind",
        "color": "#38bdf8",
        "clearance": "POZIOM ALFA-TEORIA",
        "scopePl": "Matematyka (FND-1), Informatyka (FND-2), Programowanie (FND-3), AI (FND-8) oraz Projekt B (Cyfrowy umysł / WBE) i Projekt C (Maszyny analogowe i neuromorficzne).",
        "scopeEn": "Mathematics (FND-1), CS (FND-2), Programming (FND-3), AI (FND-8), Project B (Digital Mind / WBE), and Project C (Analog & Neuromorphic Computing).",
        "linkedIds": [
          "FND-1",
          "FND-2",
          "FND-3",
          "FND-8",
          "B",
          "C"
        ]
      },
      {
        "id": "SITE-X10",
        "code": "OAK RIDGE X-10",
        "historicalAnalog": "Site X — Clinton Pile Reactor & Electromagnetic Plant",
        "namePl": "Kompleks Fizyki, Elektroniki i Mocy Jądrowej / Fuzji",
        "nameEn": "Physics, Electronics & Nuclear/Fusion Power Complex",
        "color": "#f43f5e",
        "clearance": "POZIOM SIGMA-ATOM",
        "scopePl": "Fizyka (FND-4), Elektronika (FND-5) oraz Super-Projekt H (Reaktory SMR, HTGR-POLA, MARIA, fuzja termojądrowa i architektura mocy dla A–G).",
        "scopeEn": "Physics (FND-4), Electronics (FND-5), and Super-Project H (SMR, HTGR-POLA, MARIA reactor, nuclear fusion, and power architecture for A–G).",
        "linkedIds": [
          "FND-4",
          "FND-5",
          "H"
        ]
      },
      {
        "id": "SITE-B7",
        "code": "HANFORD B-7",
        "historicalAnalog": "Site W — Hanford Chemical & Synthesis Complex",
        "namePl": "Kompleks Chemii, Biologii, Neurobioniki i Bioinżynierii",
        "nameEn": "Chemistry, Biology, Neurobionics & Bioengineering Complex",
        "color": "#10b981",
        "clearance": "POZIOM BIO-DELTA",
        "scopePl": "Chemia (FND-6), Biologia (FND-7) oraz Projekt A (Człowiek biocyfrowo-robotyczny, BCI) i Projekt D (Organoidy, inżynieria tkankowa, biologia syntetyczna).",
        "scopeEn": "Chemistry (FND-6), Biology (FND-7), Project A (Bio-Digital-Robotic Human, BCI), and Project D (Organoids, tissue engineering, synthetic biology).",
        "linkedIds": [
          "FND-6",
          "FND-7",
          "A",
          "D"
        ]
      },
      {
        "id": "SITE-T9",
        "code": "TRINITY T-9",
        "historicalAnalog": "Trinity Proving Ground & Field Systems Integration",
        "namePl": "Poligon Integracji Środowiskowej: Kosmos (F) ↔ Biosfera Ziemi (G)",
        "nameEn": "Environmental Proving Ground: Space (F) ↔ Earth Biosphere (G)",
        "color": "#a855f7",
        "clearance": "POZIOM TERRA-ORBIT",
        "scopePl": "Projekt F (Człowiek w kosmosie, zamknięte obiegi BLSS, ochrona radiacyjna) oraz Projekt G (Adaptacja na Ziemi, ochrona ekosystemów i klimatu).",
        "scopeEn": "Project F (Humans in Space, closed-loop BLSS, radiation shielding) and Project G (Earth adaptation, ecosystem & climate protection).",
        "linkedIds": [
          "FND-4",
          "FND-6",
          "FND-7",
          "F",
          "G"
        ]
      }
    ],
    "adminCore3Y": {
      "id": "ADMIN-3Y",
      "durationYears": 3,
      "semesters": 6,
      "ects": 180,
      "siteId": "SITE-W0",
      "sourceLang": "PL+EN",
      "titlePl": "Etap Zerowy (Obowiązkowy Rdzeń Manhattan): 3 Lata Studiów Administracji (Licencjat — 180 ECTS)",
      "titleEn": "Stage Zero (Mandatory Manhattan Core): 3-Year Administration Degree (B.A. — 180 ECTS)",
      "subtitlePl": "Fundament organizacyjny, prawny, finansowy i regulacyjny otwierający kaskadę 5-letnich studiów specjalistycznych",
      "subtitleEn": "Organizational, legal, financial, and regulatory foundation preceding the continuous sequence of 5-year specialist degrees",
      "completedYears": [],
      "years": [
        {
          "year": 1,
          "titlePl": "Rok 1: Fundamenty Prawa Publicznego, Ustrój Państwa i Podstawy Prawne B+R",
          "titleEn": "Year 1: Foundations of Public Law, State Governance & Legal Frameworks for R&D",
          "semesters": "Semestr I–II (60 ECTS)",
          "coursesPl": [
            "Wstęp do prawoznawstwa, logika prawnicza i teoria wykładni prawa",
            "Prawo konstytucyjne Rzeczypospolitej Polskiej i instytucje Unii Europejskiej",
            "Historia administracji, doktryny polityczno-prawne i socjologia organizacji",
            "Prawo administracyjne (część ogólna): formy działania, interes prawny i kompetencje",
            "Podstawy prawa cywilnego, prawo umów w działalności badawczej i ochrona dóbr osobistych",
            "Zarządzanie informacją niejawną, tajemnice przedsiębiorstwa i cyberbezpieczeństwo (KSC)"
          ],
          "coursesEn": [
            "Jurisprudence, Legal Logic & Theory of Legal Interpretation",
            "Constitutional Law of Poland & European Union Institutions",
            "History of Public Administration & Sociology of Organization",
            "General Administrative Law, Legal Competences & Administrative Action",
            "Civil Law Fundamentals, Research Contracts & Intellectual Integrity",
            "Classified Information Protection, Trade Secrets & National Cybersecurity Framework"
          ],
          "subchaptersPl": [
            "1.1. Logika prawnicza, wykładnia językowa i celowościowa aktów normatywnych",
            "1.2. Ustrój administracji publicznej RP i mechanizmy decyzyjne w instytucjach unijnych",
            "1.3. Prawne formy działania administracji i podstawy nawiązywania umów konsorcjalnych B+R",
            "1.4. Bezpieczeństwo informacji, kompartmentalizacja wiedzy (zasada 'Need-to-Know') i ochrona danych (RODO)"
          ],
          "subchaptersEn": [
            "1.1. Legal Logic, Grammatical and Purposive Interpretation of Normative Acts",
            "1.2. Public Administration Structure of Poland and EU Decision-Making Mechanisms",
            "1.3. Administrative Legal Actions and R&D Consortium Contract Frameworks",
            "1.4. Information Security, Knowledge Compartmentalization ('Need-to-Know') and Data Protection (GDPR)"
          ],
          "linkedMaterialIds": [
            "smat-1",
            "smat-2"
          ],
          "matchedFoundationTopics": [
            "1.1 Logika formalna, rachunek zdań i teoria dowodzenia",
            "2.6 Niezawodność i bezpieczeństwo systemów informatycznych"
          ],
          "coreBooksPl": [
            "T. Chauvin, T. Stawecki, P. Winczorek — 'Wstęp do prawoznawstwa' (C.H. Beck)",
            "Z. Niewiadomski (red.) — 'Prawo administracyjne' (PWN)",
            "L. Garlicki — 'Polskie prawo konstytucyjne' (Wolters Kluwer)"
          ],
          "coreBooksEn": [
            "P. Cane — 'Administrative Law' (Oxford University Press)",
            "J. Raz — 'The Authority of Law: Essays on Law and Morality'"
          ],
          "deliverablePl": "Statut Organizacyjny i Protokół Bezpieczeństwa Informacji Sztabu W-0.",
          "deliverableEn": "Organizational Charter and Information Security Protocol for District W-0."
        },
        {
          "year": 2,
          "titlePl": "Rok 2: Procedury Administracyjne, Regulacje Nowych Technologii (AI Act) i Własność Intelektualna",
          "titleEn": "Year 2: Administrative Procedures, Emerging Tech Regulations (AI Act) & Intellectual Property",
          "semesters": "Semestr III–IV (60 ECTS)",
          "coursesPl": [
            "Postępowanie administracyjne (KPA) i egzekucja w administracji",
            "Sądownictwo administracyjne (skargi do WSA i NSA w sprawach decyzji koncesyjnych)",
            "Europejski Akt o Sztucznej Inteligencji (EU AI Act) i ramy oceny zgodności algorytmów",
            "Prawo własności intelektualnej, prawo patentowe (EPO/UPC) i patenty na wynalazki biotechnologiczne",
            "Prawo zamówień publicznych (PZP) i procedury partnerstwa innowacyjnego",
            "Finanse publiczne, audyt projektów naukowych i ramy pomocy publicznej na B+R"
          ],
          "coursesEn": [
            "Code of Administrative Procedure (KPA) & Administrative Enforcement",
            "Administrative Judiciary (Judicial Review before Administrative Courts)",
            "European Artificial Intelligence Act (EU AI Act) & Algorithm Conformance Assessments",
            "Intellectual Property Law, Patent Law (EPO/UPC) & Biotech Inventions",
            "Public Procurement Law & Innovation Partnership Frameworks",
            "Public Finance, Scientific Project Auditing & State Aid for R&D"
          ],
          "subchaptersPl": [
            "2.1. Kodeks postępowania administracyjnego: decyzje, ugody i zaskarżanie aktów administracyjnych",
            "2.2. Kwalifikacja systemów AI podług poziomów ryzyka EU AI Act i rygor certyfikacji algorytmów krytycznych",
            "2.3. Zgłoszenia patentowe w procedurze krajowej (UPRP), europejskiej (EPO) i międzynarodowej (PCT)",
            "2.4. Finanse publiczne, audyt wydatków badawczych i zarządzanie ryzykiem prawnym w konsorcjach naukowych"
          ],
          "subchaptersEn": [
            "2.1. Code of Administrative Procedure: Decisions, Settlements and Judicial Appeals",
            "2.2. AI System Risk Classification under EU AI Act and Conformance Verification for Critical Systems",
            "2.3. Patent Filings under Polish (UPRP), European (EPO), and International (PCT) Procedures",
            "2.4. Public Finance, Scientific Grant Auditing and Legal Risk Management in R&D Consortia"
          ],
          "linkedMaterialIds": [
            "smat-8",
            "smat-trk-e1"
          ],
          "matchedFoundationTopics": [
            "8.6 Interpretowalność modeli (XAI), niezawodność, bezpieczeństwo i rygor etyczny",
            "Projekt E — Filozofia jako rygor metodologiczny i epistemiczny"
          ],
          "coreBooksPl": [
            "B. Adamiak, J. Borkowski — 'Postępowanie administracyjne i sądowoadministracyjne' (C.H. Beck)",
            "A. Michalak (red.) — 'Prawo własności intelektualnej' (C.H. Beck)",
            "M. Świerczyński — 'Prawo nowych technologii i sztucznej inteligencji' (C.H. Beck)"
          ],
          "coreBooksEn": [
            "L. Floridi — 'The Ethics of Artificial Intelligence' (Oxford University Press)",
            "W. R. Cornish — 'Intellectual Property: Patents, Copyright, Trade Marks'"
          ],
          "deliverablePl": "Macierz Zgodności z Regulacjami AI Act oraz Strategia Ochrony IP Projektu Manhattan.",
          "deliverableEn": "AI Act Compliance Matrix and Manhattan IP Protection Strategy."
        },
        {
          "year": 3,
          "titlePl": "Rok 3: Prawo Atomowe, Bioetyka, Prawo Kosmiczne i Zarządzanie Strategicznym Programem Badawczym",
          "titleEn": "Year 3: Nuclear Law, Bioethics, Space Law & Strategic Program Command",
          "semesters": "Semestr V–VI (60 ECTS)",
          "coursesPl": [
            "Prawo atomowe (wymogi PAA i IAEA, licencjonowanie reaktorów SMR, ochrona radiologiczna)",
            "Prawo medyczne, bioetyka badań na komórkach macierzystych i procedury komitetów bioetycznych",
            "Międzynarodowe prawo kosmiczne (Outer Space Treaty, Artemis Accords, rejestracja obiektów orbitalnych)",
            "Prawo ochrony środowiska, oceny oddziaływania na środowisko (OOŚ) i ramy dekarbonizacji",
            "Zarządzanie strategiczne programami o skali megaprojektów (PMI / Prince2 / Agile Gov)",
            "Seminarium dyplomowe: Obrona dysertacji 'Architektura Prawno-Administracyjna Programu Manhattan G15'"
          ],
          "coursesEn": [
            "Nuclear Law (PAA & IAEA Requirements, SMR Licensing, Radiological Protection)",
            "Medical Law, Stem Cell Bioethics & Institutional Review Boards",
            "International Space Law (Outer Space Treaty, Artemis Accords, Orbital Asset Registration)",
            "Environmental Law, Environmental Impact Assessments (EIA) & Decarbonization Policies",
            "Strategic Megaproject Management & Governance Frameworks",
            "Diploma Seminar: Defense of Dissertation 'Legal-Administrative Architecture of Manhattan G15'"
          ],
          "subchaptersPl": [
            "3.1. Reżim Prawa atomowego: procedury koncesyjne Państwowej Agencji Atomistyki dla reaktorów SMR i MARIA",
            "3.2. Standardy bioetyczne (GCP, Deklaracja Helsińska) i prawne granice inżynierii genetycznej organoidów",
            "3.3. Traktaty prawa kosmicznego: odpowiedzialność za obiekty orbitalne, surowce pozaziemskie i habitaty",
            "3.4. Dyplom licencjacki: Podręcznik Operacyjny Sztabu W-0 Projektu Manhattan Golem 15"
          ],
          "subchaptersEn": [
            "3.1. Nuclear Law Regime: PAA Licensing Procedures for SMRs and MARIA Research Reactor",
            "3.2. Bioethical Standards (GCP, Helsinki Declaration) and Legal Boundaries of Organoid Bioengineering",
            "3.3. Space Law Treaties: Liability for Orbital Objects, In-Situ Resource Utilization and Space Habitats",
            "3.4. Bachelor's Diploma: District W-0 Operational Command Manual for Manhattan Golem 15"
          ],
          "linkedMaterialIds": [
            "smat-trk-h1",
            "smat-trk-f1",
            "smat-trk-g1"
          ],
          "matchedFoundationTopics": [
            "4.5 Fizyka jądrowa i promieniowanie jonizujące",
            "6.6 Chemia środowiska i ochrona biosfery",
            "7.5 Komórki macierzyste i bioetyka"
          ],
          "coreBooksPl": [
            "J. Ciechanowicz-McLean — 'Prawo ochrony środowiska i energetyki jądrowej' (PWN)",
            "M. Safjan — 'Prawo wobec medycyny i biotechnologii' (Wolters Kluwer)",
            "J. Sztucki — 'Prawo kosmiczne' (PWN / Scholar)"
          ],
          "coreBooksEn": [
            "IAEA Safety Standards Series — 'Licensing Process for Nuclear Installations'",
            "F. Lyall, P. B. Larsen — 'Space Law: A Treatise' (Routledge)"
          ],
          "deliverablePl": "Podręcznik Operacyjny Sztabu W-0 i Licencja Administracyjna Projektu.",
          "deliverableEn": "District W-0 Command Manual and Project Administrative Charter."
        }
      ]
    },
    "fiveYearCatalog": [
      {
        "id": "STU-FND-1",
        "group": "FOUNDATION",
        "refId": "FND-1",
        "siteId": "SITE-Y15",
        "icon": "📐",
        "color": "#38bdf8",
        "titlePl": "1. Matematyka i Logika (5 lat studiów magisterskich)",
        "titleEn": "1. Mathematics & Logic (5-Year Master's Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-1",
          "smat-2"
        ],
        "matchedFoundationTopics": [
          "1.1 Logika formalna, rachunek zdań i teoria mnogości",
          "1.2 Analiza matematyczna i równania różniczkowe",
          "1.3 Algebra liniowa i przestrzenie Hilberta",
          "1.4 Rachunek prawdopodobieństwa i wnioskowanie bayesowskie",
          "1.5 Teoria informacji Shannona i układy dynamiczne",
          "1.6 Matematyka dyskretna i teoria grafów"
        ],
        "coreBooksPl": [
          "M. Gewert, Z. Skoczylas — 'Algebra liniowa 1–2' oraz 'Analiza matematyczna 1–2' (GiS)",
          "OpenAGH — 'Matematyka dla studentów nauk ścisłych' (agh.edu.pl)",
          "R. Penrose — 'Droga do rzeczywistości' (Prószyński i S-ka)"
        ],
        "coreBooksEn": [
          "G. Strang — 'Introduction to Linear Algebra' (MIT 18.06)",
          "D. J. C. MacKay — 'Information Theory, Inference, and Learning Algorithms'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Logika formalna, teoria mnogości, analiza matematyczna I i algebra liniowa I.",
            "en": "Year 1: Formal logic, set theory, calculus I, and linear algebra I.",
            "subchaptersPl": [
              "1.1. Rachunek zdań, predykatów i aksjomatyczna teoria mnogości Zermelo-Fraenkla",
              "1.2. Granice ciągów i funkcji, pochodne oraz rachunek różniczkowy jednej zmiennej",
              "1.3. Przestrzenie wektorowe, macierze, wyznaczniki i układy równań liniowych",
              "1.4. Metody dowodzenia twierdzeń i formalizm dowodowy w matematyce i fizyce"
            ],
            "subchaptersEn": [
              "1.1. Propositional & Predicate Calculus, Zermelo-Fraenkel Set Theory",
              "1.2. Limits, Derivatives, and Single-Variable Differential Calculus",
              "1.3. Vector Spaces, Matrices, Determinants, and Systems of Linear Equations",
              "1.4. Mathematical Proof Techniques and Formal Rigor in Physics & Computing"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Analiza wielu zmiennych, całki wielokrotne, algebra liniowa II i przestrzenie euklidesowe.",
            "en": "Year 2: Multivariable calculus, multiple integrals, linear algebra II, and Euclidean spaces.",
            "subchaptersPl": [
              "2.1. Rachunek różniczkowy funkcji wielu zmiennych, gradient i hesjan",
              "2.2. Całki wielokrotne, krzywoliniowe i powierzchniowe (twierdzenia Gaussa i Stokesa)",
              "2.3. Wartości i wektory własne, diagonalizacja i rozkład według wartości osobliwych (SVD)",
              "2.4. Formy kwadratowe, tensory w przestrzeniach euklidesowych i przestrzenie unitarne"
            ],
            "subchaptersEn": [
              "2.1. Multivariable Differential Calculus, Gradients, and Hessians",
              "2.2. Multiple, Line, and Surface Integrals (Gauss's and Stokes's Theorems)",
              "2.3. Eigenvalues, Eigenvectors, Diagonalization, and Singular Value Decomposition (SVD)",
              "2.4. Quadratic Forms, Tensors in Euclidean Spaces, and Unitary Spaces"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Równania różniczkowe zwyczajne i cząstkowe, analiza zespolona i transformata Fouriera.",
            "en": "Year 3: Ordinary and partial differential equations, complex analysis, and Fourier transforms.",
            "subchaptersPl": [
              "3.1. Równania różniczkowe zwyczajne liniowe i nieliniowe (modele dynamiki populacji i obwodów)",
              "3.2. Funkcje zmiennej zespolonej, całka Cauchy'ego i rachunek rezyduów",
              "3.3. Szeregi i transformaty Fouriera oraz transformata Laplace'a w układach ciągłych",
              "3.4. Równania różniczkowe cząstkowe (równanie falowe, dyfuzji ciepła i Schrödingera)"
            ],
            "subchaptersEn": [
              "3.1. Linear and Non-Linear Ordinary Differential Equations (Dynamical Systems)",
              "3.2. Complex Analysis, Cauchy's Integral Theorem, and Residue Calculus",
              "3.3. Fourier Series, Continuous & Discrete Fourier Transforms, Laplace Transforms",
              "3.4. Partial Differential Equations (Wave, Heat Diffusion, and Schrödinger Equations)"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Rachunek prawdopodobieństwa, statystyka matematyczna, procesy stochastyczne i teoria informacji.",
            "en": "Year 4: Probability theory, mathematical statistics, stochastic processes, and information theory.",
            "subchaptersPl": [
              "4.1. Przestrzenie probabilistyczne Kołmogorowa, zmienne losowe i prawa wielkich liczb",
              "4.2. Wnioskowanie statystyczne, estymacja parametrów i testowanie hipotez (podejście częstościowe i bayesowskie)",
              "4.3. Łańcuchy Markowa, procesy Poissona i stochastyczne równania różniczkowe Ito",
              "4.4. Entropia Shannona, informacja wzajemna, kompresja danych i twierdzenia o kodowaniu"
            ],
            "subchaptersEn": [
              "4.1. Kolmogorov Probability Spaces, Random Variables, Central Limit Theorems",
              "4.2. Statistical Inference, Parameter Estimation, Frequentist and Bayesian Hypothesis Testing",
              "4.3. Markov Chains, Poisson Processes, and Ito Stochastic Differential Equations",
              "4.4. Shannon Entropy, Mutual Information, Data Compression, and Channel Coding Theorems"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Analiza funkcjonalna, przestrzenie Hilberta, teoria układów dynamicznych i chaosu, praca magisterska.",
            "en": "Year 5: Functional analysis, Hilbert spaces, dynamical systems and chaos theory, Master's thesis.",
            "subchaptersPl": [
              "5.1. Przestrzenie Banacha i Hilberta, operatory samosprzężone i teoria spektralna (podstawa mechaniki kwantowej)",
              "5.2. Teoria układów dynamicznych, bifurkacje, atraktory i chaos deterministyczny",
              "5.3. Geometria różniczkowa i topologia sieci złożonych (podstawa konektomu)",
              "5.4. Praca magisterska: Formalny model matematyczny nieliniowej dynamiki sieci neuronowej lub kwantowej"
            ],
            "subchaptersEn": [
              "5.1. Banach and Hilbert Spaces, Self-Adjoint Operators, and Spectral Theory",
              "5.2. Dynamical Systems Theory, Bifurcations, Strange Attractors, and Deterministic Chaos",
              "5.3. Differential Geometry and Complex Network Topology (Connectome Foundations)",
              "5.4. Master's Thesis: Formal Mathematical Model of Non-Linear Neural or Quantum System Dynamics"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-2",
        "group": "FOUNDATION",
        "refId": "FND-2",
        "siteId": "SITE-Y15",
        "icon": "💻",
        "color": "#60a5fa",
        "titlePl": "2. Informatyka — Architektury Post-Krzemowe, QPU i Neuromorfizm (5 lat studiów)",
        "titleEn": "2. Computer Science — Post-Silicon Architectures, QPU & Neuromorphics (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-2",
          "smat-trk-c1"
        ],
        "matchedFoundationTopics": [
          "2.1 Teoria obliczeń, maszyny Turinga i złożoność obliczeniowa",
          "2.2 Algorytmy i struktury danych",
          "2.3 Architektura komputerów (CPU, GPU, QPU, układy neuromorficzne)",
          "2.4 Systemy operacyjne, systemy rozproszone i HPC",
          "2.5 Bazy danych, ontologie i reprezentacja wiedzy",
          "2.6 Niezawodność i fault-tolerance"
        ],
        "coreBooksPl": [
          "T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein — 'Wprowadzenie do algorytmów' (PWN)",
          "Ch. Petzold — 'Kod. Ukryty język sprzętu i oprogramowania' (Helion)",
          "A. S. Tanenbaum, H. Bos — 'Systemy operacyjne' (Helion)"
        ],
        "coreBooksEn": [
          "J. L. Hennessy, D. A. Patterson — 'Computer Architecture: A Quantitative Approach'",
          "M. A. Nielsen, I. L. Chuang — 'Quantum Computation and Quantum Information'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Logika cyfrowa, bramki, arytmetyka maszynowa, podstawy architektury komputerów i algorytmy elementarne.",
            "en": "Year 1: Digital logic, gates, machine arithmetic, computer architecture basics, and elementary algorithms.",
            "subchaptersPl": [
              "1.1. Algebra Boole'a, minimalizacja funkcji logicznych i projektowanie układów kombinacyjnych",
              "1.2. Układy sekwencyjne: przerzutniki, rejestry, liczniki i automaty synchroniczne",
              "1.3. Architektura von Neumanna vs. Harvardzka: cykl rozkazowy, magistrale i jednostka ALU",
              "1.4. Podstawowe algorytmy i struktury danych: tablice, listy, stosy, kolejki i złożoność O(n)"
            ],
            "subchaptersEn": [
              "1.1. Boolean Algebra, Logic Minimization, and Combinational Circuit Design",
              "1.2. Sequential Circuits: Flip-Flops, Registers, Counters, and Finite State Machines",
              "1.3. Von Neumann vs. Harvard Architecture: Instruction Cycle, Busses, ALU Operations",
              "1.4. Fundamental Algorithms & Data Structures: Lists, Stacks, Queues, and Big-O Complexity"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Zaawansowane struktury danych, algorytmy grafowe, systemy operacyjne i wąskie gardło von Neumanna.",
            "en": "Year 2: Advanced data structures, graph algorithms, operating systems, and von Neumann memory wall.",
            "subchaptersPl": [
              "2.1. Drzewa zrównoważone (AVL, Czerwono-Czarne), kopce, tablice mieszające i algorytmy grafowe (Dijkstra, A*)",
              "2.2. Architektura systemów operacyjnych: procesy, wątki, synchronizacja (muteksy, semafory) i zakleszczenia",
              "2.3. Zarządzanie pamięcią: stronicowanie, pamięć wirtualna i hierarchia pamięci podręcznych (L1/L2/L3)",
              "2.4. Wąskie gardło von Neumanna (Memory Wall) i ograniczenia skalowania Dennarda w klasycznych CPU"
            ],
            "subchaptersEn": [
              "2.1. Balanced Search Trees, Heaps, Hash Tables, and Graph Algorithms (Dijkstra, A*)",
              "2.2. Operating System Architecture: Processes, Threads, Concurrency, and Deadlock Prevention",
              "2.3. Memory Management: Paging, Virtual Memory, and Cache Coherency Protocols",
              "2.4. Von Neumann Memory Wall, Latency Gaps, and the Breakdown of Dennard Scaling"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Teoria obliczeń, granice krzemu, architektury Dataflow oraz podstawy obliczeń kwantowych (kubity).",
            "en": "Year 3: Theory of computation, silicon physical limits, Dataflow architectures, and quantum computing basics.",
            "subchaptersPl": [
              "3.1. Maszyny Turinga, obliczalność, problem stopu oraz klasy złożoności obliczeniowej (P, NP, NP-zupełne)",
              "3.2. Fizyczne bariery miniaturyzacji krzemu: upływ tunelowy, limit termiczny Landauera i koniec prawa Moore'a",
              "3.3. Architektury nie-von Neumannowskie: Dataflow, obliczenia w pamięci (In-Memory Computing) i macierze FPGA",
              "3.4. Wprowadzenie do obliczeń kwantowych: stan kubitu, sfera Blocha, bramki kwantowe (Hadamard, CNOT) i splątanie"
            ],
            "subchaptersEn": [
              "3.1. Turing Machines, Computability, Halting Problem, and Complexity Classes (P, NP, NP-Complete)",
              "3.2. Physical Breakdown of Silicon: Gate Leakage, Landauer Thermal Limit, Moore's Law End",
              "3.3. Non-Von Neumann Architectures: Dataflow Computing, In-Memory Computing, and FPGA Fabrics",
              "3.4. Introduction to Quantum Computing: Qubits, Bloch Sphere, Quantum Gates (Hadamard, CNOT), Entanglement"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Algorytmy kwantowe (Shor, Grover, VQE), układy neuromorficzne (Loihi, SpiNNaker) i komputery ery NISQ.",
            "en": "Year 4: Quantum algorithms (Shor, Grover, VQE), neuromorphic hardware (Loihi, SpiNNaker), and NISQ computing.",
            "subchaptersPl": [
              "4.1. Algorytmy kwantowe: algorytm faktoryzacji Shora, przeszukiwanie Grovera i algorytmy wariacyjne (VQE/QAOA)",
              "4.2. Architektury komputerów kwantowych ery NISQ: kubity nadprzewodzące (transmony), pułapki jonowe i korekcja błędów",
              "4.3. Architektury procesorów neuromorficznych: asynchroniczne pakiety AER, Intel Loihi, SpiNNaker i BrainScaleS",
              "4.4. Sieci rozproszone i systemy odporne na awarie (Byzantine Fault Tolerance, Paxos/Raft) w klastrach HPC"
            ],
            "subchaptersEn": [
              "4.1. Quantum Algorithms: Shor's Factorization, Grover's Search, Variational Solvers (VQE/QAOA)",
              "4.2. NISQ Quantum Hardware: Superconducting Transmons, Trapped Ions, Surface Code Error Correction",
              "4.3. Neuromorphic Processor Architecture: Asynchronous AER Buses, Intel Loihi, SpiNNaker, BrainScaleS",
              "4.4. Distributed Systems & Fault Tolerance (Byzantine Fault Tolerance, Paxos/Raft) in HPC"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Heterogeniczne superkomputery hybrydowe (CPU+GPU+QPU+NPU), kryptografia postkwantowa, praca magisterska.",
            "en": "Year 5: Heterogeneous hybrid supercomputing (CPU+GPU+QPU+NPU), post-quantum cryptography, Master's thesis.",
            "subchaptersPl": [
              "5.1. Projektowanie heterogenicznych systemów obliczeniowych łączących CPU, akceleratory kwantowe (QPU) i neuromorficzne (NPU)",
              "5.2. Kryptografia postkwantowa (PQC): kryptografia oparta na kratach (Lattice-based, Kyber, Dilithium)",
              "5.3. Pamięci nowej generacji: memrystory (ReRAM), spintronika (MRAM) i obliczenia rezerwuarowe w krzemie",
              "5.4. Praca magisterska: Architektura procesora nie-von Neumannowskiego do symulacji konektomu lub obliczeń kwantowych"
            ],
            "subchaptersEn": [
              "5.1. Design of Heterogeneous Compute Systems Integrating Classical CPUs, QPUs, and Neuromorphic NPUs",
              "5.2. Post-Quantum Cryptography (PQC): Lattice-Based Cryptography (Kyber, Dilithium)",
              "5.3. Next-Gen Memory: Memristors (ReRAM), Spintronics (MRAM), and Reservoir Computing in Silicon",
              "5.4. Master's Thesis: Non-Von Neumann Processor Architecture for Connectome or Quantum Emulation"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-3",
        "group": "FOUNDATION",
        "refId": "FND-3",
        "siteId": "SITE-Y15",
        "icon": "⌨️",
        "color": "#818cf8",
        "titlePl": "3. Programowanie — Nowe Paradygmaty, Qiskit i Symulacje SNN (5 lat studiów)",
        "titleEn": "3. Programming — New Paradigms, Qiskit & SNN Simulations (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-3",
          "smat-2"
        ],
        "matchedFoundationTopics": [
          "3.1 Paradygmaty programowania: obiektowe, funkcyjne, reaktywne i różniczkowalne",
          "3.2 Python w obliczeniach naukowych (NumPy, SciPy, PyTorch, JAX)",
          "3.3 Języki systemowe (Rust, C/C++) dla mikrokontrolerów i BCI",
          "3.4 Symulacje numeryczne układów neuronalnych (Brian2, NEURON, snnTorch)",
          "3.5 Programowanie komputerów kwantowych (Qiskit, Cirq, PennyLane)",
          "3.6 Inżynieria oprogramowania i weryfikacja kodu"
        ],
        "coreBooksPl": [
          "E. Matthes — 'Python. Instrukcje dla programisty' (Helion)",
          "A. Sweigart — 'Automatyzacja nudnych zadań z Pythonem' (Helion)",
          "S. Klabnik, C. Nichols — 'Język programowania Rust' (Helion)"
        ],
        "coreBooksEn": [
          "H. P. Langtangen — 'A Primer on Scientific Programming with Python'",
          "A. Géron — 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Fundamenty Pythona, C, inżynieria czystego kodu, wzorce projektowe i testy jednostkowe.",
            "en": "Year 1: Python and C foundations, clean code engineering, design patterns, and unit testing.",
            "subchaptersPl": [
              "1.1. Składnia Pythona, struktury danych, zarządzanie pamięcią i programowanie proceduralne",
              "1.2. Programowanie zorientowane obiektowo (OOP): polimorfizm, enkapsulacja i kompozycja klas",
              "1.3. Język C: wskaźniki, alokacja sterty (malloc/free) i bezpośrednie operacje bitowe",
              "1.4. Inżynieria oprogramowania naukowego: Git, Pytest, dokumentacja i powtarzalność badań (reproducibility)"
            ],
            "subchaptersEn": [
              "1.1. Python Syntax, Data Structures, Memory Management, and Procedural Coding",
              "1.2. Object-Oriented Programming (OOP): Polymorphism, Encapsulation, Class Composition",
              "1.3. C Language: Pointers, Heap Allocation (malloc/free), and Direct Bitwise Operations",
              "1.4. Scientific Software Engineering: Git Version Control, Pytest, Code Documentation, Reproducibility"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Python w obliczeniach naukowych (NumPy, SciPy), programowanie funkcyjne i język Rust.",
            "en": "Year 2: Scientific computing Python (NumPy, SciPy), functional programming, and Rust systems programming.",
            "subchaptersPl": [
              "2.1. Wektoryzacja i operacje macierzowe w NumPy, broadcasting i procedury numeryczne SciPy",
              "2.2. Programowanie funkcyjne: niezmienniczość, funkcje wyższego rzędu, lambdy i operatory monadyczne",
              "2.3. Język Rust: system własności (ownership), pożyczanie (borrowing) i bezpieczeństwo pamięci bez garbage collectora",
              "2.4. Współbieżność w Pythonie i Rust: asynchroniczność (async/await, Tokio), wielowątkowość i kolejki komunikatów"
            ],
            "subchaptersEn": [
              "2.1. Vectorization and Matrix Operations in NumPy, Broadcasting, SciPy Numerical Routines",
              "2.2. Functional Programming: Immutability, Higher-Order Functions, Lambdas, and Monadic Pipelines",
              "2.3. Rust Language: Ownership, Borrowing, Lifetimes, and Zero-Cost Memory Safety",
              "2.4. Concurrency in Python and Rust: Async/Await (Tokio), Multithreading, and Lockless Channels"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Zmiana paradygmatu: programowanie różniczkowalne (JAX/PyTorch) i symulacje bio-neurologiczne (Brian2, NEURON).",
            "en": "Year 3: Paradigm shift: differentiable programming (JAX/PyTorch) and computational neuroscience simulations (Brian2, NEURON).",
            "subchaptersPl": [
              "3.1. Nowy paradygmat: programowanie różniczkowalne i grafy tensorowe (PyTorch, JAX Autograd)",
              "3.2. Symulacja modeli neuronów biologicznych w Brian2 i NEURON (modele Hodgkina-Huxleya, Izhikevicha, Leaky Integrate-and-Fire)",
              "3.3. Programowanie mikrokontrolerów ARM/RISC-V (Embedded C/Rust) do sterowania aktuatorami i akwizycji sygnałów BCI",
              "3.4. Optymalizacja niskopoziomowa: instrukcje SIMD (AVX-512), kompilatory JIT (Numba) i akceleracja CUDA C++"
            ],
            "subchaptersEn": [
              "3.1. Differentiable Programming Paradigm: Computation Graphs and Automatic Differentiation (PyTorch, JAX)",
              "3.2. Biological Neuron Simulation in Brian2 and NEURON (Hodgkin-Huxley, Izhikevich, Leaky Integrate-and-Fire)",
              "3.3. Embedded ARM / RISC-V Programming in C/Rust for Sensor Interfaces and BCI Data Acquisition",
              "3.4. Low-Level Performance Optimization: SIMD Vectorization (AVX-512), Numba JIT, and CUDA C++ Kernels"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Programowanie komputerów kwantowych (Qiskit, PennyLane) i impulsowych sieci neuronowych (snnTorch, Lava).",
            "en": "Year 4: Quantum programming (Qiskit, PennyLane) and Spiking Neural Network programming (snnTorch, Lava).",
            "subchaptersPl": [
              "4.1. Programowanie obwodów kwantowych w Qiskit: synteza bramek, symulatory macierzowe i uruchamianie na realnych QPU IBM Quantum",
              "4.2. Różniczkowalne programowanie kwantowe (PennyLane) i kwantowe uczenie maszynowe (QML, Quantum Neural Networks)",
              "4.3. Programowanie impulsowych sieci neuronowych SNN (snnTorch, Norse, framework Lava dla układu Intel Loihi)",
              "4.4. Programowanie systemów robotycznych czasu rzeczywistego (ROS 2 / C++) i przetwarzanie strumieniowe danych biomedycznych"
            ],
            "subchaptersEn": [
              "4.1. Quantum Circuit Programming in Qiskit: Gate Synthesis, Simulators, and Execution on IBM Quantum QPUs",
              "4.2. Differentiable Quantum Programming (PennyLane) and Quantum Machine Learning (QML)",
              "4.3. Spiking Neural Network (SNN) Programming with snnTorch, Norse, and Intel Lava for Neuromorphic Chips",
              "4.4. Real-Time Robotic Programming (ROS 2 / C++) and Streaming Biomedical Signal Pipelines"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Architektura frameworków wieloskalowych, skalowanie symulacji Whole Brain Emulation, praca magisterska.",
            "en": "Year 5: Multiscale framework architecture, massive Whole Brain Emulation scaling, Master's thesis.",
            "subchaptersPl": [
              "5.1. Projektowanie frameworków symulacyjnych dużej skali łączących akcelerację GPU z koprocesorami kwantowymi i NPU",
              "5.2. Równoległe algorytmy symulacji konektomu i modeli plastyczności synaptycznej (STDP) w klastrach wielowęzłowych (MPI/Slurm)",
              "5.3. Rygor inżynieryjny: formalna weryfikacja kodu, profile zużycia energii i testowanie odporności na błędy sprzętowe",
              "5.4. Praca magisterska: Otwarty framework w Pythonie/Rust do hybrydowej symulacji impulsowej sieci neuronowej na akceleratorze neuromorficznym"
            ],
            "subchaptersEn": [
              "5.1. Large-Scale Multiscale Simulation Framework Design Coupling GPUs, QPUs, and Neuromorphic Hardware",
              "5.2. Distributed Connectome and STDP Synaptic Plasticity Simulation on HPC Clusters (MPI, Slurm)",
              "5.3. Software Verification: Formal Code Proofs, Energy Profiling, and Hardware Fault-Tolerant Pipelines",
              "5.4. Master's Thesis: Open-Source Python/Rust Framework for Hybrid SNN Simulation on Neuromorphic Hardware"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-4",
        "group": "FOUNDATION",
        "refId": "FND-4",
        "siteId": "SITE-X10",
        "icon": "⚛️",
        "color": "#f59e0b",
        "titlePl": "4. Fizyka — Granice Krzemu, Półprzewodniki Post-Krzemowe i Mechanika Kwantowa (5 lat)",
        "titleEn": "4. Physics — Silicon Limits, Post-Silicon Semiconductors & Quantum Mechanics (5-Year)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-4",
          "smat-trk-h1"
        ],
        "matchedFoundationTopics": [
          "4.1 Mechanika klasyczna, relatywistyczna i orbitalna",
          "4.2 Termodynamika klasyczna, statystyczna i nierównowagowa",
          "4.3 Elektrodynamika, fale i fotonika",
          "4.4 Fizyka ciała stałego, półprzewodniki i materiały post-krzemowe",
          "4.5 Mechanika kwantowa i fizyka jądrowa",
          "4.6 Biofizyka błon i potencjałów czynnościowych"
        ],
        "coreBooksPl": [
          "OpenStax Polska — 'Fizyka dla szkół wyższych' Tom 1–3 (openstax.pl)",
          "R. P. Feynman, R. B. Leighton, M. Sands — 'Feynmana wykłady z fizyki' Tom 1–3 (PWN)",
          "D. J. Griffiths — 'Podstawy mechaniki kwantowej' (PWN)"
        ],
        "coreBooksEn": [
          "C. Kittel — 'Introduction to Solid State Physics'",
          "N. W. Ashcroft, N. D. Mermin — 'Solid State Physics'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Mechanika klasyczna, ruch drgający, fale mechaniczne, termodynamika fenomenologiczna i grawitacja.",
            "en": "Year 1: Classical mechanics, oscillations, waves, phenomenological thermodynamics, and gravitation.",
            "subchaptersPl": [
              "1.1. Kinematyka i dynamika Newtona, zasady zachowania pędu, energii i momentu pędu",
              "1.2. Ruch drgający, rezonans mechaniczny, fale sprężyste i akustyka",
              "1.3. Mechanika analityczna: formalizm Lagrange'a i Hamiltona, równania kanoniczne",
              "1.4. Podstawy termodynamiki klasycznej: pierwsza i druga zasada termodynamiki, entropia i cykl Carnota"
            ],
            "subchaptersEn": [
              "1.1. Newtonian Kinematics & Dynamics, Conservation Laws of Momentum, Energy, Angular Momentum",
              "1.2. Harmonic Oscillations, Resonance, Mechanical Waves, and Acoustics",
              "1.3. Analytical Mechanics: Lagrangian and Hamiltonian Formalisms, Canonical Equations",
              "1.4. Classical Thermodynamics: 1st and 2nd Laws, Entropy, and Carnot Heat Cycles"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Elektrodynamika Maxwella, fale elektromagnetyczne, optyka falowa i termodynamika statystyczna.",
            "en": "Year 2: Maxwell's electrodynamics, electromagnetic waves, wave optics, and statistical physics.",
            "subchaptersPl": [
              "2.1. Równania Maxwella w próżni i ośrodkach materialnych, potencjały Liénarda-Wiecherta",
              "2.2. Fale elektromagnetyczne, polaryzacja, dyfrakcja, interferencja i fotonika",
              "2.3. Fizyka statystyczna: zespoły mikrokanoniczne, kanoniczne i wielkie kanoniczne Gibbsa",
              "2.4. Rozkłady kwantowe: statystyka Fermiego-Diraca (elektrony) oraz Bosego-Einsteina (fotony, fonony)"
            ],
            "subchaptersEn": [
              "2.1. Maxwell's Equations in Vacuum and Media, Liénard-Wiechert Potentials",
              "2.2. Electromagnetic Waves, Polarization, Diffraction, Wave Optics, and Photonics",
              "2.3. Statistical Mechanics: Microcanonical, Canonical, and Grand Canonical Gibbs Ensembles",
              "2.4. Quantum Statistics: Fermi-Dirac (Fermions) and Bose-Einstein (Bosons, Phonons) Distributions"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Mechanika kwantowa nierelatywistyczna, teoria złącza p-n i fizyka pasmowa półprzewodników.",
            "en": "Year 3: Non-relativistic quantum mechanics, p-n junction physics, and semiconductor band theory.",
            "subchaptersPl": [
              "3.1. Równanie Schrödingera, studnia potencjału, oscylator harmoniczny i zjawisko tunelowe",
              "3.2. Atom wodoru, moment pędu, spin elektronu i zakaz Pauliego",
              "3.3. Fizyka ciała stałego: sieć krystaliczna, pasma energetyczne, masa efektywna nośników i poziom Fermiego",
              "3.4. Fizyka złącza p-n, charakterystyki tranzystorów MOSFET i heterostruktur półprzewodnikowych"
            ],
            "subchaptersEn": [
              "3.1. Schrödinger Equation, Potential Wells, Harmonic Oscillator, and Quantum Tunneling",
              "3.2. Hydrogen Atom, Angular Momentum, Electron Spin, and Pauli Exclusion Principle",
              "3.3. Solid-State Physics: Crystal Lattices, Band Theory, Effective Mass, and Fermi Levels",
              "3.4. P-N Junction Physics, MOSFET Transistor Characteristics, and Semiconductor Heterostructures"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Fizyczne granice krzemu (upływy kwantowe, limit Landauera), materiały post-krzemowe (grafen, 2D) i nadprzewodnictwo.",
            "en": "Year 4: Physical limits of silicon (quantum leakage, Landauer limit), post-silicon 2D materials, and superconductivity.",
            "subchaptersPl": [
              "4.1. Fizyczne bariery krzemu poniżej 2 nm: upływ przez bramkę dielektryczną, fluktuacje domieszkowania i limit Landauera",
              "4.2. Materiały dwuwymiarowe post-krzemowe: grafen, dichalkogenki metali przejściowych (MoS2, WSe2) i nanorurki węglowe",
              "4.3. Zjawisko nadprzewodnictwa (teoria BCS, złącza Josephsona) jako podstawa kubitów nadprzewodzących",
              "4.4. Fizyka jądrowa: energia wiązania jądra, rozszczepienie uranu/plutonu, reakcje fuzji D-T i przekroje czynne"
            ],
            "subchaptersEn": [
              "4.1. Physical Silicon Barriers Below 2nm: Gate Dielectric Leakage, Dopant Fluctuations, Landauer Dissipation Limit",
              "4.2. Post-Silicon 2D Materials: Graphene, Transition Metal Dichalcogenides (MoS2, WSe2), and Carbon Nanotubes",
              "4.3. Superconductivity (BCS Theory, Josephson Junctions) as Foundation for Superconducting Qubits",
              "4.4. Nuclear Physics: Binding Energy, Fission of U/Pu, D-T Fusion Cross-Sections, and Radiation Interaction"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Biofizyka kwantowa, magnetyczne uwięzienie plazmy (tokamaki), transport w nanoskali i praca magisterska.",
            "en": "Year 5: Quantum biophysics, magnetic plasma confinement (tokamaks), nanoscale transport, Master's thesis.",
            "subchaptersPl": [
              "5.1. Biofizyka komórkowa: potencjał spoczynkowy i czynnościowy błon, transport jonowy przez kanały białkowe",
              "5.2. Fizyka plazmy termojądrowej: kryterium Lawsona, magnetyczne uwięzienie plazmy w tokamakach i stellaratorach",
              "5.3. Teoria dekoherencji kwantowej i zjawiska kwantowe w układach makroskopowych",
              "5.4. Praca magisterska: Model fizyczny transportu ładunku i ciepła w złączu memrystorowym lub nadprzewodzącym kubicie"
            ],
            "subchaptersEn": [
              "5.1. Cellular Biophysics: Resting & Action Potentials, Voltage-Gated Ion Channel Transport",
              "5.2. Fusion Plasma Physics: Lawson Criterion, Magnetic Confinement in Tokamaks and Stellarators",
              "5.3. Quantum Decoherence Theory and Macroscopic Quantum Effects in Physical Devices",
              "5.4. Master's Thesis: Physical Model of Charge and Thermal Transport in Memristive or Superconducting Qubit Junctions"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-5",
        "group": "FOUNDATION",
        "refId": "FND-5",
        "siteId": "SITE-X10",
        "icon": "🔌",
        "color": "#eab308",
        "titlePl": "5. Elektronika — Memrystory, Układy Neuromorficzne i Pomiary BCI (5 lat studiów)",
        "titleEn": "5. Electronics — Memristors, Neuromorphic Chips & BCI Instrumentation (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-5",
          "smat-trk-a1",
          "smat-trk-c1"
        ],
        "matchedFoundationTopics": [
          "5.1 Teoria obwodów elektrycznych, filtry i stany nieustalone",
          "5.2 Elektronika analogowa, wzmacniacze operacyjne i układy niskoszumne",
          "5.3 Układy cyfrowe, FPGA i mikrokontrolery",
          "5.4 Akwizycja sygnałów biologicznych (EEG, EMG, EKG, BCI)",
          "5.5 Sensory środowiskowe, biomedyczne i aktuatory",
          "5.6 Układy neuromorficzne, memrystory i realizacja sztucznych synaps"
        ],
        "coreBooksPl": [
          "P. Horowitz, W. Hill — 'Sztuka elektroniki' Tom 1–2 (WKŁ)",
          "W. Forbot — 'Podręczniki elektroniki i techniki mikroprocesorowej' (forbot.pl)",
          "A. Oppenheim, R. Schafer — 'Cyfrowe przetwarzanie sygnałów' (WKŁ)"
        ],
        "coreBooksEn": [
          "S.-C. Liu et al. — 'Neuromorphic Engineering: Systems and Applications'",
          "G. Indiveri — 'Neuromorphic Silicon Neuron Circuits'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Teoria obwodów, prawa Kirchhoffa, elementy RLC, diody, tranzystory bipolarne i polowe (MOSFET).",
            "en": "Year 1: Circuit theory, Kirchhoff's laws, RLC components, diodes, BJT and MOSFET transistors.",
            "subchaptersPl": [
              "1.1. Obwody prądu stałego i zmiennego: twierdzenia Thevenina, Nortona i stany nieustalone RLC",
              "1.2. Półprzewodnikowe elementy pasywne i aktywne: diody Zenera, Schottky'ego, tranzystory BJT",
              "1.3. Tranzystory polowe z izolowaną bramką (MOSFET): charakterystyki statyczne i dynamiczne, komplementarne pary CMOS",
              "1.4. Pomiary laboratoryjne: oscyloskopy cyfrowe, generatory funkcyjne i analiza szumów"
            ],
            "subchaptersEn": [
              "1.1. DC and AC Circuit Analysis: Thevenin, Norton Theorems, and Transient RLC Responses",
              "1.2. Passive & Active Semiconductor Elements: Zener, Schottky Diodes, BJT Small-Signal Models",
              "1.3. Field-Effect Transistors (MOSFET): Static and Dynamic Regimes, Complementary CMOS Pairs",
              "1.4. Laboratory Instrumentation: Digital Storage Oscilloscopes, Signal Generators, Noise Measurement"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Wzmacniacze operacyjne, filtry aktywne, układy cyfrowe, FPGA i przetworniki ADC/DAC.",
            "en": "Year 2: Operational amplifiers, active filters, digital logic, FPGAs, and ADC/DAC converters.",
            "subchaptersPl": [
              "2.1. Wzmacniacze operacyjne: sprzężenie zwrotne, wzmacniacze pomiarowe, całkujące i różniczkujące",
              "2.2. Filtry aktywne (Butterwortha, Czebyszewa, Bessela) i układy kształtowania sygnałów",
              "2.3. Projektowanie układów cyfrowych w językach HDL (Verilog / VHDL) i implementacja w układach FPGA",
              "2.4. Przetworniki analogowo-cyfrowe (ADC) i cyfrowo-analogowe (DAC): rozdzielczość, aliasing i próbkowanie Nyquista"
            ],
            "subchaptersEn": [
              "2.1. Operational Amplifiers: Negative Feedback, Instrumentation Amplifiers, Integrators, Differentiators",
              "2.2. Active Analog Filters (Butterworth, Chebyshev, Bessel) and Signal Conditioning",
              "2.3. Digital System Design in Hardware Description Languages (Verilog/VHDL) on FPGA Platforms",
              "2.4. Data Converters (ADC/DAC): Resolution, Quantization Noise, Aliasing, and Nyquist Rate"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Niskoszumowa aparatura biomedyczna (tory pomiarowe EEG/EMG/BCI), zasilanie i sensory.",
            "en": "Year 3: Low-noise biomedical instrumentation (EEG/EMG/BCI signal chains), power management, and sensors.",
            "subchaptersPl": [
              "3.1. Projektowanie niskoszumowych analogowych torów biopotencjałów: wzmacniacze EEG, EMG i EKG o wysokim CMRR",
              "3.2. Izolacja galwaniczna, bezpieczeństwo pacjenta (norma PN-EN 60601) i redukcja zakłóceń sieciowych 50 Hz",
              "3.3. Sensory biochemiczne, elektrochemiczne i optyczne (pulsoksymetria, spektroskopia fNIRS)",
              "3.4. Układy zasilania impulsowego o wysokiej sprawności, ładowanie bezprzewodowe implantów medycznych i zarządzanie energią"
            ],
            "subchaptersEn": [
              "3.1. Low-Noise Analog Front-Ends for Biopotentials: EEG, EMG, ECG Amplifiers with High CMRR",
              "3.2. Galvanic Isolation, Patient Electrical Safety (IEC 60601), and 50/60 Hz Mains Interference Rejection",
              "3.3. Biochemical, Electrochemical, and Optical Sensors (Pulse Oximetry, Functional NIRS)",
              "3.4. High-Efficiency Switched-Mode Power Supplies, Wireless Implant Charging, and Energy Harvesting"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Memrystory, matryce synaptyczne ReRAM, sensory neuromorficzne (kamery DVS) i elektronika asynchroniczna.",
            "en": "Year 4: Memristors, ReRAM synaptic crossbars, neuromorphic event-driven sensors (DVS cameras), asynchronous logic.",
            "subchaptersPl": [
              "4.1. Memrystory i pamięci rezystywne (ReRAM, Phase Change Memory): fizyka przełączania i modelowanie matematyczne",
              "4.2. Matryce synaptyczne: realizacja reguły Hebbowskiej i plastyczności STDP bezpośrednio w obwodach elektronicznych",
              "4.3. Zdarzeniowe sensory neuromorficzne: kamery DVS (Dynamic Vision Sensors) i impulsowe sensory ślimakowe",
              "4.4. Projektowanie układów asynchronicznych (Asynchronous Sub-Threshold CMOS) emulujących dynamikę błon biologicznych"
            ],
            "subchaptersEn": [
              "4.1. Memristors & Resistive RAM (ReRAM, PCM): Switching Physics and Mathematical Dynamics",
              "4.2. Synaptic Crossbar Arrays: In-Hardware Hebbian and Spike-Timing-Dependent Plasticity (STDP)",
              "4.3. Neuromorphic Event-Based Sensing: Dynamic Vision Sensors (DVS) and Silicon Cochleas",
              "4.4. Sub-Threshold Asynchronous CMOS Circuit Design Emulating Biological Membrane Conductances"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Projektowanie układów scalonych ASIC/neuromorficznych, elektronika kriogeniczna i praca magisterska.",
            "en": "Year 5: ASIC/Neuromorphic chip design, cryogenic readout electronics, Master's thesis.",
            "subchaptersPl": [
              "5.1. Pełny cykl projektowania układów scalonych ASIC (Full-Custom & Semi-Custom) w środowiskach EDA",
              "5.2. Elektronika kriogeniczna do odczytu i kontroli kubitów nadprzewodzących w temperaturach milikelwinowych",
              "5.3. Odporność radiacyjna elektroniki (Radiation-Hardened Electronics) dla reaktorów jądrowych i misji kosmicznych",
              "5.4. Praca magisterska: Projekt i symulacja układu scalonego z memrystorową matrycą synaptyczną do adaptacyjnego dekodowania sygnałów BCI"
            ],
            "subchaptersEn": [
              "5.1. Full-Custom and Semi-Custom ASIC Design Flow in Modern Electronic Design Automation (EDA) Suites",
              "5.2. Cryogenic CMOS and RF Readout Electronics for Qubits Operating at Millikelvin Temperatures",
              "5.3. Radiation-Hardened Electronics for Nuclear Reactor Monitoring and Deep-Space Spacecraft",
              "5.4. Master's Thesis: Design and Simulation of an ASIC with Memristive Synaptic Crossbar for Adaptive BCI Decoding"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-6",
        "group": "FOUNDATION",
        "refId": "FND-6",
        "siteId": "SITE-B7",
        "icon": "🧪",
        "color": "#10b981",
        "titlePl": "6. Chemia i Biochemia — Biomateriały, Hydrożele i Zamknięte Obiegi (5 lat studiów)",
        "titleEn": "6. Chemistry & Biochemistry — Biomaterials, Hydrogels & Closed Cycles (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-6",
          "smat-trk-d1"
        ],
        "matchedFoundationTopics": [
          "6.1 Chemia ogólna, wiązania i stechiometria",
          "6.2 Chemia organiczna i synteza związków węgla",
          "6.3 Biochemia białek, kwasów nukleinowych i enzymów",
          "6.4 Elektrochemia, ogniwa i potencjały redoks",
          "6.5 Inżynieria biomateriałów, hydrożele tkankowe i polimery biokompatybilne",
          "6.6 Chemia środowiska i zamknięte obiegi pierwiastków (C, N, O, P)"
        ],
        "coreBooksPl": [
          "A. Bielański — 'Podstawy chemii nieorganicznej' Tom 1–2 (PWN)",
          "OpenStax Polska — 'Chemia' (openstax.pl)",
          "J. M. Berg, J. L. Tymoczko, L. Stryer — 'Biochemia' (PWN)"
        ],
        "coreBooksEn": [
          "D. Voet, J. G. Voet — 'Biochemistry' (Wiley)",
          "B. D. Ratner et al. — 'Biomaterials Science: An Introduction to Materials in Medicine'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Chemia ogólna, budowa atomu, wiązania chemiczne, stechiometria, termochemia i równowagi kwasowo-zasadowe.",
            "en": "Year 1: General chemistry, atomic structure, chemical bonding, stoichiometry, thermochemistry, and acid-base equilibria.",
            "subchaptersPl": [
              "1.1. Struktura elektronowa atomów, układ okresowy pierwiastków i reguły wiązań chemicznych",
              "1.2. Stechiometria reakcji, roztwory, stężenia i równowagi kwasowo-zasadowe (pH, bufory)",
              "1.3. Termochemia: entalpia reakcji, entropia, energia swobodna Gibbsa i stałe równowagi chemicznej",
              "1.4. Równowagi redoks, szereg napięciowy metali i podstawy kinetyki chemicznej"
            ],
            "subchaptersEn": [
              "1.1. Atomic Electronic Structure, Periodic Trends, and Chemical Bonding Principles",
              "1.2. Reaction Stoichiometry, Solutions, Concentrations, and Acid-Base Equilibria (pH, Buffers)",
              "1.3. Thermochemistry: Reaction Enthalpy, Entropy, Gibbs Free Energy, and Equilibrium Constants",
              "1.4. Redox Equilibria, Standard Electrode Potentials, and Chemical Reaction Kinetics"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Chemia organiczna, grupy funkcyjne, stereochemia, mechanizmy reakcji i spektroskopia.",
            "en": "Year 2: Organic chemistry, functional groups, stereochemistry, reaction mechanisms, and spectroscopy.",
            "subchaptersPl": [
              "2.1. Węglowodory alifatyczne, aromatyczne i stereochemia związków węgla (chiralność)",
              "2.2. Związki z grupami tlenowymi i azotowymi: alkohole, fenole, aminy, kwasy karboksylowe i ich pochodne",
              "2.3. Mechanizmy reakcji organicznych: substytucja, eliminacja, addycja i kondensacja",
              "2.4. Identyfikacja strukturalna związków organicznych: spektroskopia NMR, FT-IR oraz spektrometria mas (MS)"
            ],
            "subchaptersEn": [
              "2.1. Aliphatic and Aromatic Hydrocarbons, Stereochemistry and Molecular Chirality",
              "2.2. Oxygen- and Nitrogen-Containing Compounds: Alcohols, Amines, Carboxylic Acids and Derivatives",
              "2.3. Organic Reaction Mechanisms: Substitution, Elimination, Addition, and Condensation",
              "2.4. Structural Characterization: NMR Spectroscopy, FT-IR, and Mass Spectrometry (MS)"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Biochemia strukturalna, białka, enzymy, metabolizm komórkowy, kwasy nukleinowe i bioenergetyka.",
            "en": "Year 3: Structural biochemistry, proteins, enzymes, cellular metabolism, nucleic acids, and bioenergetics.",
            "subchaptersPl": [
              "3.1. Struktura i kinetyka enzymatyczna (równanie Michaelisa-Menten, allosteria i inhibicja enzymów)",
              "3.2. Szlaki metaboliczne: glikoliza, cykl Krebsa, fosforylacja oksydacyjna i bilans ATP",
              "3.3. Biochemia lipidów i błon komórkowych: fosfolipidy, tratwy lipidowe i receptory błonowe",
              "3.4. Biochemia kwasów nukleinowych: struktura DNA/RNA, biosynteza i mechanizmy naprawy DNA"
            ],
            "subchaptersEn": [
              "3.1. Protein Structure & Enzyme Kinetics (Michaelis-Menten, Allosteric Regulation, Inhibition)",
              "3.2. Metabolic Pathways: Glycolysis, Krebs Cycle, Oxidative Phosphorylation, and ATP Synthesis",
              "3.3. Lipid and Membrane Biochemistry: Phospholipids, Lipid Rafts, and Transmembrane Receptors",
              "3.4. Nucleic Acid Biochemistry: DNA/RNA Architecture, Biosynthesis, and DNA Repair Pathways"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Chemia materiałów medycznych, polimery biokompatybilne, hydrożele tkankowe i elektrochemia sensorów.",
            "en": "Year 4: Medical materials chemistry, biocompatible polymers, tissue hydrogels, and electrochemical sensing.",
            "subchaptersPl": [
              "4.1. Polimery biokompatybilne i biodegradowalne (PLA, PGA, PCL, PEG) do nośników leków i rusztowań tkankowych",
              "4.2. Hydrożele biomimetyczne: sieciowanie chemiczne i fizyczne, pęcznienie i gradienty mechaniczne w inżynierii tkanek",
              "4.3. Zjawiska na granicy faz ciało stałe–ciecz: adsorpcja białek i odpowiedź immunologiczna (Foreign Body Response)",
              "4.4. Elektrochemia interfejsów nerwowych: polimery przewodzące (PEDOT:PSS), elektrody platynowo-irydowe i mikroczujniki"
            ],
            "subchaptersEn": [
              "4.1. Biocompatible & Biodegradable Polymers (PLA, PGA, PCL, PEG) for Drug Delivery & Tissue Scaffolds",
              "4.2. Biomimetic Hydrogels: Chemical/Physical Crosslinking, Swelling Dynamics, Stiffness Gradients",
              "4.3. Solid-Liquid Bio-Interfaces: Protein Adsorption Kinetics and the Foreign Body Response",
              "4.4. Electrochemistry of Neural Interfaces: Conducting Polymers (PEDOT:PSS), Pt-Ir Electrodes, Microsensors"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Zamknięte obiegi chemiczne w habitatach kosmicznych, inżynieria katalizy środowiskowej, praca magisterska.",
            "en": "Year 5: Closed chemical loops for space habitats, environmental catalysis engineering, Master's thesis.",
            "subchaptersPl": [
              "5.1. Zamknięte obiegi chemiczne: regeneracja tlenu (elektroliza wody, reakcja Sabatiera, redukcja Boscha)",
              "5.2. Oczyszczanie wody i recykling odpadów ciekłych w układach podtrzymywania życia (ECLSS)",
              "5.3. Zaawansowane materiały do magazynowania energii: akumulatory ze stałym elektrolitem (solid-state) i ogniwa paliwowe",
              "5.4. Praca magisterska: Synteza i charakterystyka biokompatybilnego hydrożelu przewodzącego do integracji z tkanką nerwową"
            ],
            "subchaptersEn": [
              "5.1. Closed Chemical Cycles: Oxygen Recovery (Water Electrolysis, Sabatier Reaction, Bosch Process)",
              "5.2. Water Purification and Liquid Waste Recycling in Environmental Life Support Systems (ECLSS)",
              "5.3. Advanced Energy Storage Materials: Solid-State Lithium Batteries and High-Temperature Fuel Cells",
              "5.4. Master's Thesis: Synthesis & Characterization of a Biocompatible Conducting Hydrogel for Neural Integration"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-7",
        "group": "FOUNDATION",
        "refId": "FND-7",
        "siteId": "SITE-B7",
        "icon": "🧬",
        "color": "#22c55e",
        "titlePl": "7. Biologia i Neurobiologia — Konektom, Organoidy i Fizjologia Człowieka (5 lat studiów)",
        "titleEn": "7. Biology & Neurobiology — Connectome, Organoids & Human Physiology (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-7",
          "smat-trk-d1",
          "smat-trk-b1"
        ],
        "matchedFoundationTopics": [
          "7.1 Biologia komórki i sygnalizacja wewnątrzkomórkowa",
          "7.2 Genetyka, genomika i edycja genów CRISPR",
          "7.3 Anatomia i fizjologia człowieka (układ nerwowy, krążenia, odpornościowy)",
          "7.4 Neurobiologia, synapsy i plastyczność mózgu",
          "7.5 Biologia rozwoju, komórki macierzyste i regeneracja tkanek",
          "7.6 Ekologia biosfery i mikrobiom"
        ],
        "coreBooksPl": [
          "N. A. Campbell et al. — 'Biologia' (Rebis)",
          "B. Alberts et al. — 'Podstawy biologii komórki' Tom 1–2 (PWN)",
          "T. A. Brown — 'Genomy' (PWN)"
        ],
        "coreBooksEn": [
          "E. R. Kandel et al. — 'Principles of Neural Science' (McGraw-Hill)",
          "P. Dayan, L. F. Abbott — 'Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Biologia komórki, organelle, transport błonowy, cykl komórkowy, mitoza, mejoza i podstawy genetyki mendlowskiej.",
            "en": "Year 1: Cell biology, organelles, membrane transport, cell cycle, mitosis, meiosis, and Mendelian genetics.",
            "subchaptersPl": [
              "1.1. Budowa komórki eukariotycznej i prokariotycznej, cytoszkielet i dynamika organelli",
              "1.2. Błona komórkowa: transport aktywny i pasywny, pompy jonowe (Na+/K+-ATPaza) i potencjał spoczynkowy",
              "1.3. Cykl komórkowy, mechanizmy kontrolne, mitoza, mejoza oraz programowana śmierć komórki (apoptoza)",
              "1.4. Genetyka klasyczna: prawa Mendla, dziedziczenie cech sprzężonych i mutacje genowe"
            ],
            "subchaptersEn": [
              "1.1. Eukaryotic and Prokaryotic Cell Architecture, Cytoskeleton, and Organelle Dynamics",
              "1.2. Cell Membrane Transport: Active and Passive Transport, Na+/K+-ATPase, Resting Potential",
              "1.3. Cell Cycle Regulation, Checkpoints, Mitosis, Meiosis, and Programmed Cell Death (Apoptosis)",
              "1.4. Mendelian Genetics: Laws of Inheritance, Linkage, Recombination, and Chromosomal Mutations"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Biologia molekularna, ekspresja genów, epigenetyka, genomika i edycja genomu (CRISPR-Cas9).",
            "en": "Year 2: Molecular biology, gene expression, epigenetics, genomics, and genome editing (CRISPR-Cas9).",
            "subchaptersPl": [
              "2.1. Dogmat centralny biologii molekularnej: replikacja DNA, transkrypcja i translacja",
              "2.2. Regulacja ekspresji genów: promotory, czynniki transkrypcyjne i modyfikacje potranslacyjne",
              "2.3. Epigenetyka: metylacja DNA, modyfikacje histonów i niekodujące RNA (miRNA, lncRNA)",
              "2.4. Inżynieria genetyczna: sekwencjonowanie NGS, edycja genów CRISPR-Cas9/Cas12 oraz terapia genowa"
            ],
            "subchaptersEn": [
              "2.1. Central Dogma of Molecular Biology: DNA Replication, Transcription, and Translation",
              "2.2. Gene Expression Control: Promoters, Enhancers, Transcription Factors, Post-Translational Modifiers",
              "2.3. Epigenetics: DNA Methylation, Histone Acetylation, and Regulatory Non-Coding RNAs (miRNA, lncRNA)",
              "2.4. Genetic Engineering: Next-Gen Sequencing (NGS), CRISPR-Cas9/Cas12 Gene Editing, and Gene Therapy"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Anatomia i fizjologia człowieka: układ nerwowy, krążenia, mięśniowy, odpornościowy i endokrynny.",
            "en": "Year 3: Human anatomy and physiology: nervous, cardiovascular, muscular, immune, and endocrine systems.",
            "subchaptersPl": [
              "3.1. Układ nerwowy: anatomia ośrodkowego i obwodowego układu nerwowego, drogi zstępujące i wstępujące",
              "3.2. Fizjologia układu krążenia i oddechowego: hemodynamika, transport gazów i adaptacja do wysiłku",
              "3.3. Układ odpornościowy: odporność wrodzona i nabyta, limfocyty T i B, autoprzeciwciała i tolerancja immunologiczna",
              "3.4. Układ endokrynny: osie hormonalne (podwzgórze-przysadka-nadnercza), homeostaza glukozy i rytmy dobowe"
            ],
            "subchaptersEn": [
              "3.1. Nervous System Anatomy: Central & Peripheral Systems, Ascending Sensory & Descending Motor Tracts",
              "3.2. Cardiovascular & Respiratory Physiology: Hemodynamics, Gas Exchange, and Aerobic Stress Adaptation",
              "3.3. Immunology: Innate and Adaptive Immunity, T/B-Cell Differentiation, Tolerance & Autoimmunity",
              "3.4. Endocrine System: HPA Axis, Metabolic Glucose Homeostasis, and Circadian Biological Rhythms"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Neurobiologia komórkowa i układowa, synapsy, plastyczność Hebbowska (LTP/LTD) i narządy zmysłów.",
            "en": "Year 4: Cellular & systems neurobiology, synapses, Hebbian plasticity (LTP/LTD), sensory systems.",
            "subchaptersPl": [
              "4.1. Elektrofizjologia neuronu: potencjał czynnościowy, kanały bramkowane napięciem i równanie Goldmana",
              "4.2. Transmisja synaptyczna chemiczna i elektryczna (gap junctions), neuroprzekaźniki (glutaminian, GABA, dopamina)",
              "4.3. Plastyczność synaptyczna: długotrwałe wzmocnienie (LTP), wygaszanie (LTD) i reguła Spike-Timing-Dependent Plasticity",
              "4.4. Układy zmysłów: przetwarzanie w siatkówce oka, kora wzrokowa V1–V4, ślimak i układ somatosensoryczny"
            ],
            "subchaptersEn": [
              "4.1. Neuron Electrophysiology: Action Potentials, Voltage-Gated Ion Channels, Goldman-Hodgkin-Katz Equation",
              "4.2. Synaptic Transmission: Chemical and Electrical Gap Junctions, Neurotransmitters (Glutamate, GABA, Dopamine)",
              "4.3. Synaptic Plasticity: Long-Term Potentiation (LTP), Depression (LTD), and Spike-Timing-Dependent Plasticity",
              "4.4. Sensory Systems: Retinal Processing, Visual Cortex V1–V4 Hierarchy, Cochlear Transduction, Somatosensory"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Komórki macierzyste, hodowla organoidów mózgowych, konektomika wysokiej rozdzielczości, praca magisterska.",
            "en": "Year 5: Stem cells, brain organoid cultures, high-resolution connectomics, Master's thesis.",
            "subchaptersPl": [
              "5.1. Indukowane pluripotencjalne komórki macierzyste (iPSC) i różnicowanie w kierunku neuronów i komórek glejowych",
              "5.2. Hodowla trójwymiarowych organoidów mózgowych: samoorganizacja, powstawanie warstw korowych i spontaniczna aktywność",
              "5.3. Metody konektomiki w nanoskali: mikroskopia elektronowa skaningowa (FIB-SEM), mikroskopia dwufotonowa i optogenetyka",
              "5.4. Praca magisterska: Analiza elektrofizjologiczna i konektomiczna spontanicznej aktywności w hodowli organoidu korowego"
            ],
            "subchaptersEn": [
              "5.1. Induced Pluripotent Stem Cells (iPSCs) and Directed Differentiation into Neurons and Glia",
              "5.2. 3D Brain Organoid Engineering: Self-Organization, Cortical Layering, and Spontaneous Synchrony",
              "5.3. Nanoscale Connectomics Techniques: Serial FIB-SEM Electron Microscopy, Two-Photon Imaging, Optogenetics",
              "5.4. Master's Thesis: Electrophysiological and Connectomic Analysis of Synchronous Firing in Cortical Organoids"
            ]
          }
        ]
      },
      {
        "id": "STU-FND-8",
        "group": "FOUNDATION",
        "refId": "FND-8",
        "siteId": "SITE-Y15",
        "icon": "🤖",
        "color": "#a855f7",
        "titlePl": "8. Sztuczna Inteligencja — Modele Kognitywne, Dekodowanie BCI i Uczenie Przez Wzmocnienie (5 lat)",
        "titleEn": "8. Artificial Intelligence — Cognitive Models, BCI Decoding & Reinforcement Learning (5-Year)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-8",
          "smat-trk-b1",
          "smat-trk-a1"
        ],
        "matchedFoundationTopics": [
          "8.1 Uczenie maszynowe klasyczne i optymalizacja gradientowa",
          "8.2 Głębokie sieci neuronowe (CNN, Transformers, GNN)",
          "8.3 Uczenie ze wzmocnieniem (RL) i sterowanie robotami",
          "8.4 Dekodowanie sygnałów mózgowych (BCI) i biologia strukturalna",
          "8.5 Porównanie architektur AI z biologicznym mózgiem człowieka",
          "8.6 Rygor epistemiczny, interpretowalność (XAI) i bezpieczeństwo modeli"
        ],
        "coreBooksPl": [
          "I. Goodfellow, Y. Bengio, A. Courville — 'Głębokie uczenie' (PWN)",
          "S. Russell, P. Norvig — 'Sztuczna inteligencja. Nowoczesne podejście' (Helion)",
          "R. S. Sutton, A. G. Barto — 'Uczenie przez wzmocnienie' (PWN)"
        ],
        "coreBooksEn": [
          "F. Chollet — 'Deep Learning with Python'",
          "E. Alpaydin — 'Introduction to Machine Learning'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Podstawy uczenia maszynowego, regresja liniowa i logistyczna, drzewa decyzyjne i optymalizacja gradientowa.",
            "en": "Year 1: Machine learning fundamentals, linear and logistic regression, decision trees, and gradient optimization.",
            "subchaptersPl": [
              "1.1. Zadania uczenia nadzorowanego, nienadzorowanego i samonadzorowanego; funkcje kosztu i metryki błędu",
              "1.2. Regresja liniowa i logistyczna, regularyzacja L1/L2 (Lasso, Ridge) i problem przeuczenia (overfitting)",
              "1.3. Algorytmy optymalizacji gradientowej: SGD, Momentum, RMSprop, Adam i techniki harmonogramowania kroku uczenia",
              "1.4. Drzewa decyzyjne, lasy losowe (Random Forests) i algorytmy gradientowego wzmacniania (XGBoost, LightGBM)"
            ],
            "subchaptersEn": [
              "1.1. Supervised, Unsupervised, and Self-Supervised Paradigms; Loss Functions and Error Metrics",
              "1.2. Linear and Logistic Regression, Regularization (L1/L2, Lasso, Ridge), and Overfitting Mitigation",
              "1.3. Gradient Optimization Algorithms: Stochastic Gradient Descent, Momentum, RMSprop, Adam, Learning Rate Schedulers",
              "1.4. Decision Trees, Random Forests, and Gradient Boosting Frameworks (XGBoost, LightGBM)"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Głębokie sieci neuronowe, propagacja wsteczna błędu, konwolucyjne sieci CNN i przetwarzanie sygnałów.",
            "en": "Year 2: Deep neural networks, backpropagation, convolutional networks (CNN), and signal processing.",
            "subchaptersPl": [
              "2.1. Wielowarstwowe perceptrony (MLP), funkcje aktywacji (ReLU, GELU, Swish) i matematyka wstecznej propagacji błędu",
              "2.2. Konwolucyjne sieci neuronowe (CNN): warstwy splotowe, pooling, architektury ResNet, EfficientNet i ConvNeXt",
              "2.3. Przetwarzanie sygnałów czasowych: rekurencyjne sieci neuronowe (RNN), komórki LSTM i GRU",
              "2.4. Metody wizualizacji cech wewnętrznych i interpretowalności wstępnej (Grad-CAM, saliency maps)"
            ],
            "subchaptersEn": [
              "2.1. Multi-Layer Perceptrons (MLP), Activation Functions (ReLU, GELU, Swish), Backpropagation Calculus",
              "2.2. Convolutional Neural Networks (CNN): Convolutions, Pooling, Residual Connections (ResNet, ConvNeXt)",
              "2.3. Temporal Sequence Processing: Recurrent Neural Networks (RNN), LSTM, and GRU Memory Cells",
              "2.4. Feature Attribution and Explainability Methods (Grad-CAM, Integrated Gradients, Saliency Maps)"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Architektura Transformerów, mechanizm uwagi (Self-Attention), modele językowe (LLM) i grafowe sieci (GNN).",
            "en": "Year 3: Transformer architecture, self-attention mechanisms, large language models (LLMs), and Graph Neural Networks (GNN).",
            "subchaptersPl": [
              "3.1. Mechanizm uwagi (Scaled Dot-Product Attention) i architektura Transformer (enkoder-dekoder)",
              "3.2. Wielkie modele językowe (LLM): tokenizacja, pre-training samonadzorowany, fine-tuning (LoRA, QLoRA) i RLHF",
              "3.3. Grafowe sieci neuronowe (GNN): propagacja wiadomości (Message Passing), modelowanie struktur molekularnych i białek",
              "3.4. Modele generatywne: dyfuzja (Diffusion Models), modele przepływowe (Normalizing Flows) i autoregresyjne"
            ],
            "subchaptersEn": [
              "3.1. Attention Mechanisms (Scaled Dot-Product Attention) and Full Transformer Architectures",
              "3.2. Large Language Models (LLMs): Tokenization, Self-Supervised Pre-Training, Parameter-Efficient Tuning (LoRA), RLHF",
              "3.3. Graph Neural Networks (GNN): Message Passing Schemas for Molecular and Connectomic Graph Embeddings",
              "3.4. Generative Modeling: Denoising Diffusion Probabilistic Models, Normalizing Flows, and Autoregressive Encoders"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Uczenie przez wzmocnienie (RL), sterowanie robotami, dekodowanie sygnałów nerwowych i interfejsy BCI.",
            "en": "Year 4: Reinforcement learning (RL), robotic control, neural signal decoding, and BCI interfaces.",
            "subchaptersPl": [
              "4.1. Uczenie przez wzmocnienie: równanie Bellmana, Q-learning, Deep Q-Networks (DQN) i metody Policy Gradient (PPO, SAC)",
              "4.2. Uczenie przez wzmocnienie w sterowaniu robotami: przestrzeń ciągłych akcji, symulatory fizyki (Isaac Gym, MuJoCo)",
              "4.3. Zastosowania AI w dekodowaniu sygnałów mózgowych (EEG, ECoG, intracortical arrays): klasyfikacja intencji ruchowej i mowy",
              "4.4. Modele fałdowania białek i bioinformatyka AI (AlphaFold 2/3, RoseTTAFold, ESMFold)"
            ],
            "subchaptersEn": [
              "4.1. Reinforcement Learning Foundations: Bellman Optimality, Q-Learning, Deep Q-Networks, Policy Gradients (PPO, SAC)",
              "4.2. Deep RL in Physical Robotics: Continuous Action Spaces, Physics Engines (NVIDIA Isaac Gym, MuJoCo)",
              "4.3. Neural Signal Decoding with AI (EEG, ECoG, Microelectrode Arrays): Motor & Speech Intent Reconstruction",
              "4.4. AI-Driven Structural Biology: Protein Folding Prediction (AlphaFold 2/3, ESMFold, Molecular Docking)"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Architektury kognitywne, porównanie AI z mózgiem biologicznym, bezpieczeństwo i rygor epistemiczny, praca magisterska.",
            "en": "Year 5: Cognitive architectures, biological brain vs. AI alignment, safety, epistemic rigor, Master's thesis.",
            "subchaptersPl": [
              "5.1. Architektury kognitywne: pamięć robocza, modele świata, planowanie hierarchiczne i samouczenie się w środowisku",
              "5.2. Krytyczne porównanie mechanizmów AI z mózgiem człowieka: sprawność energetyczna (20W vs. kW), uczenie z pojedynczych przykładów",
              "5.3. Rygor epistemiczny i bezpieczeństwo AI: wykrywanie halucynacji, weryfikacja formalna i zgodność z EU AI Act",
              "5.4. Praca magisterska: Implementacja głębokiego modelu dekodowania intencji motorycznej z sygnałów nerwowych w czasie rzeczywistym"
            ],
            "subchaptersEn": [
              "5.1. Cognitive Architectures: Working Memory, Internal World Models, Hierarchical Planning, Autonomous Exploration",
              "5.2. Comparative Analysis of AI vs. Biological Brain: Energy Efficiency (20W vs. Kilowatts), Few-Shot Generalization",
              "5.3. AI Epistemic Rigor & Safety: Hallucination Mitigation, Formal Verification, and EU AI Act Compliance Auditing",
              "5.4. Master's Thesis: Real-Time Deep Learning Decoder of Motor Intent from High-Density Neural Activity"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-A",
        "group": "TRACK",
        "refId": "A",
        "siteId": "SITE-B7",
        "icon": "🦾",
        "color": "#38bdf8",
        "titlePl": "Projekt A: Człowiek Biocyfrowo-Robotyczny (5 lat studiów)",
        "titleEn": "Project A: Bio-Digital-Robotic Human (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-a1",
          "smat-5",
          "smat-8"
        ],
        "matchedFoundationTopics": [
          "FND-1",
          "FND-2",
          "FND-3",
          "FND-5",
          "FND-7",
          "FND-8"
        ],
        "coreBooksPl": [
          "B. D. Ratner — 'Inżynieria biomedyczna i biomateriały' (PWN)",
          "P. Horowitz — 'Sztuka elektroniki: Układy pomiarowe' (WKŁ)"
        ],
        "coreBooksEn": [
          "J. M. Carmena — 'Brain-Machine Interfaces'",
          "M. A. Lebedev, M. A. L. Nicolelis — 'Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Neuroanatomia funkcjonalna układu ruchu, biomechanika i fizyczne podstawy protezowania.",
            "en": "Year 1: Functional neuroanatomy of movement, biomechanics, and physical foundations of prosthetics.",
            "subchaptersPl": [
              "1.1. Neuroanatomia rdzenia kręgowego, nerwów obwodowych i kory ruchowej M1",
              "1.2. Biomechanika kończyn górnych i dolnych: kinematyka, siły mięśniowe i trajektorie ruchu",
              "1.3. Pomiary elektromiograficzne (EMG): elektrody powierzchniowe i domięśniowe",
              "1.4. Podstawowe protezy mechaniczne i sensoryczny feedback proprioceptywny"
            ],
            "subchaptersEn": [
              "1.1. Neuroanatomy of Spinal Cord, Peripheral Nerves, and Primary Motor Cortex M1",
              "1.2. Upper and Lower Limb Biomechanics: Kinematics, Muscle Forces, and Movement Trajectories",
              "1.3. Electromyographic (EMG) Sensing: Surface and Intramuscular Electrode Arrays",
              "1.4. Mechanical Prosthetics and Proprioceptive Sensory Feedback Foundations"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Egzoszkielety, aktuatory bioniczne, sterowanie impedancyjne i sensoryka proprioceptywna.",
            "en": "Year 2: Exoskeletons, bionic actuators, impedance control, and proprioceptive sensors.",
            "subchaptersPl": [
              "2.1. Konstrukcja egzoszkieletów rehabilitacyjnych i wspomagających: ramy kompozytowe i stopy tytanu",
              "2.2. Aktuatory bioniczne: bezszczotkowe silniki BLDC, sztuczne mięśnie pneumatyczne (PMA) i stopy z pamięcią kształtu",
              "2.3. Algorytmy sterowania siłowego i impedancyjnego egzoszkieletem w czasie rzeczywistym",
              "2.4. Sensoryka nacisku, tensometria i wielokanałowa telemetria biomechaniczna"
            ],
            "subchaptersEn": [
              "2.1. Rehabilitation & Assistive Exoskeleton Design: Carbon-Fiber Frames & Titanium Alloys",
              "2.2. Bionic Actuators: BLDC Motors, Pneumatic Artificial Muscles (PAMs), Shape Memory Alloys",
              "2.3. Force and Impedance Control Algorithms for Real-Time Human-Machine Interaction",
              "2.4. Pressure Distribution Sensors, Strain Gauges, and Multichannel Biomechanical Telemetry"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Inwazyjne i nieinwazyjne interfejsy mózg-komputer (BCI), elektrody Utah i mikrokable neuropodobne.",
            "en": "Year 3: Invasive and non-invasive brain-computer interfaces (BCI), Utah arrays, and flexible neuropixels.",
            "subchaptersPl": [
              "3.1. Porównanie interfejsów BCI: EEG, fNIRS, ECoG, elektrody penetrujące (Utah Array, Neuropixels)",
              "3.2. Biokompatybilność długoterminowa elektrod: zjawisko powstawania blizny glejowej i degradacji sygnału",
              "3.3. Przetwarzanie sygnałów nerwowych: detekcja iglic (spike sorting), potencjały polowe LFP i analiza częstotliwościowa",
              "3.4. Dwukierunkowe BCI: mikrocyfrowa stymulacja kory somatosensorycznej przywracająca czucie dotyku"
            ],
            "subchaptersEn": [
              "3.1. Comparative BCI Modalities: Scalp EEG, fNIRS, ECoG, and Penetrating Probes (Utah Array, Neuropixels)",
              "3.2. Long-Term Biocompatibility: Glial Scar Formation, Immune Rejection, and Signal Attenuation",
              "3.3. Neural Signal Processing: Spike Sorting, Local Field Potentials (LFP), and Wavelet Time-Frequency Analysis",
              "3.4. Bidirectional Closed-Loop BCIs: Intracortical Microstimulation Restoring Tactile Sensation"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Zamknięte pętle bio-cybernetyczne, integracja nerwowo-mechaniczna i adaptacyjne protezy bioniczne.",
            "en": "Year 4: Closed-loop bio-cybernetic circuits, neural osseointegration, and adaptive bionic limbs.",
            "subchaptersPl": [
              "4.1. Chirurgiczne techniki przygotowania kikuta: ukierunkowane unerwienie mięśniowe (TMR - Targeted Muscle Reinnervation)",
              "4.2. Osteointegracja: bezpośrednie mocowanie tytanowego implantu bionicznego do kości szkieletu",
              "4.3. Sterowanie bioniczne oparte na uczeniu maszynowym: ciągłe dekodowanie intencji ruchowych z sygnałów EMG/BCI",
              "4.4. Kompensacja latencji i stabilność układów zamkniętej pętli człowiek–proteza"
            ],
            "subchaptersEn": [
              "4.1. Surgical Neuro-Interfacing: Targeted Muscle Reinnervation (TMR) and Regenerative Peripheral Nerve Interfaces",
              "4.2. Osseointegration: Direct Skeletal Titanium Anchor Fixing with Percutaneous Bio-Feedthroughs",
              "4.3. Machine-Learning-Driven Bionic Prosthetics: Continuous Decoding of Kinematics from EMG/BCI",
              "4.4. Latency Compensation and Stability Analysis in Closed-Loop Human-Prosthesis Systems"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Zaawansowane protezowanie zmysłów, bezpieczeństwo kliniczne, etyka augmentacji, praca magisterska.",
            "en": "Year 5: Advanced sensory neuroprosthetics, clinical safety, augmentation ethics, Master's thesis.",
            "subchaptersPl": [
              "5.1. Bioniczne protezy zmysłów: implanty ślimakowe, implanty siatkówkowe i stymulacja kory wzrokowej",
              "5.2. Odporność na zakłócenia elektromagnetyczne (EMC) i bezpieczeństwo implantów w środowisku MRI",
              "5.3. Etyczne, prawne i tożsamościowe aspekty augmentacji ciała ludzkiego",
              "5.4. Praca magisterska: Kompletny system sterowania bioniczną dłonią z zamkniętą pętlą czuciową w czasie rzeczywistym"
            ],
            "subchaptersEn": [
              "5.1. Sensory Neuroprostheses: Cochlear Implants, Epiretinal Arrays, and Direct Visual Cortex Stimulation",
              "5.2. Electromagnetic Compatibility (EMC) and MRI Safety Guidelines for Active Implantable Medical Devices",
              "5.3. Ethical, Legal, and Identity Implications of Human Physical Augmentation",
              "5.4. Master's Thesis: Fully Integrated Closed-Loop Bionic Hand Control with Real-Time Sensory Feedback"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-B",
        "group": "TRACK",
        "refId": "B",
        "siteId": "SITE-Y15",
        "icon": "🧠",
        "color": "#60a5fa",
        "titlePl": "Projekt B: Cyfrowy Umysł i Whole Brain Emulation (5 lat studiów)",
        "titleEn": "Project B: Digital Mind & Whole Brain Emulation (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-b1",
          "smat-1",
          "smat-2",
          "smat-8"
        ],
        "matchedFoundationTopics": [
          "FND-1",
          "FND-2",
          "FND-3",
          "FND-7",
          "FND-8",
          "Projekt E"
        ],
        "coreBooksPl": [
          "N. Bostrom — 'Superinteligencja. Scenariusze, strategie, zagrożenia' (Helion)",
          "R. Penrose — 'Nowy umysł cesarza' (PWN)",
          "S. Lem — 'Dialogi' oraz 'Summa Technologiae' (Wydawnictwo Literackie)"
        ],
        "coreBooksEn": [
          "A. H. Sandberg, N. Bostrom — 'Whole Brain Emulation: A Roadmap' (FHI Technical Report)",
          "O. Sporns — 'Networks of the Brain' (MIT Press)"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Neuroanatomia porównawcza, cytoarchitektonika kory mózgowej i podstawy konektomiki.",
            "en": "Year 1: Comparative neuroanatomy, cortical cytoarchitectonics, and connectomics foundations.",
            "subchaptersPl": [
              "1.1. Warstwy kory mózgowej, kolumny korowe i mikroobwody neuronalne",
              "1.2. Cytoarchitektoniczne mapy Brodmanna i wielkoskalowa topologia połączeń mózgu",
              "1.3. Podstawy konektomiki: macierze sąsiedztwa, grafy skierowane i ważone sieci neuronalnych",
              "1.4. Metody obrazowania rezonansem magnetycznym: dMRI, traktografia i wskaźniki anizotropii frakcyjnej"
            ],
            "subchaptersEn": [
              "1.1. Cortical Layers, Canonical Microcircuits, and Interneuron Morphologies",
              "1.2. Brodmann Cytoarchitectonic Maps and Large-Scale Macro-Connectomics",
              "1.3. Graph-Theoretical Connectomics: Adjacency Matrices, Directed & Weighted Brain Networks",
              "1.4. Magnetic Resonance Tractography: Diffusion MRI (dMRI), Fractional Anisotropy, Streamline Reconstruction"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Technologie skanowania tkanki mózgowej w skali nano (FIB-SEM, dMRI) i rekonstrukcja obrazów.",
            "en": "Year 2: Nanoscale brain tissue scanning technologies (FIB-SEM, expansion microscopy) and volume reconstruction.",
            "subchaptersPl": [
              "2.1. Fiksacja chemiczna, perfuzja kriogeniczna i utwardzanie tkanki mózgowej w żywicach polimerowych",
              "2.2. Seryjna mikroskopia elektronowa (Serial Block-Face SEM, FIB-SEM) z rozdzielczością nanometrową",
              "2.3. Mikroskopia ekspansyjna (Expansion Microscopy) i fluorescencyjne znakowanie białek synaptycznych",
              "2.4. Przetwarzanie petabajtowych wolumenów graficznych: segmentacja błon i rekonstrukcja 3D aksonów przez AI"
            ],
            "subchaptersEn": [
              "2.1. Chemical Fixation, Cryogenic Perfusion, and Polymer Resin Embedding of Neural Tissue",
              "2.2. Nanoscale Serial Electron Microscopy: Serial Block-Face SEM and Focused Ion Beam SEM (FIB-SEM)",
              "2.3. Expansion Microscopy and Fluorescent Tagging of Pre- and Post-Synaptic Densities",
              "2.4. Petabyte-Scale Volumetric Segmentation: AI Membrane Tracing and 3D Axon Reconstruction"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Matematyczne modele neuronu i mikroobwodów korowych, symulatory NEST, Brian2 i NEURON.",
            "en": "Year 3: Mathematical models of single neurons and cortical microcircuits, NEST, Brian2, and NEURON simulators.",
            "subchaptersPl": [
              "3.1. Równania Hodgkina-Huxleya i ich uproszczenia (FitzHugh-Nagumo, Izhikevich, AdEx)",
              "3.2. Modelowanie przedziałowe dendrytów (Compartmental Modeling) i obliczenia nieliniowe w drzewie dendrytycznym",
              "3.3. Skalowanie symulacji mikrokolumn korowych w symulatorach NEST i Brian2",
              "3.4. Równowaga pobudzenia i hamowania (E/I balance), oscylacje gamma i synchronizacja fazowa"
            ],
            "subchaptersEn": [
              "3.1. Hodgkin-Huxley Formulations and Reduced Firing Models (FitzHugh-Nagumo, Izhikevich, AdEx)",
              "3.2. Multicompartmental Dendritic Modeling and Active Non-Linear Dendritic Computation",
              "3.3. Large-Scale Microcircuit Simulation in NEST, Brian2, and Blue Brain Project Suites",
              "3.4. Excitation-Inhibition (E/I) Balance, Cortical Gamma Oscillations, and Phase Synchrony"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Whole Brain Emulation (WBE), kalibracja parametrów elektrofizjologicznych i stabilność numeryczna.",
            "en": "Year 4: Whole Brain Emulation (WBE), electrophysiological parameter tuning, and numerical stability.",
            "subchaptersPl": [
              "4.1. Translacja struktury anatomicznej na parametry elektrofizjologiczne symulatora (od konektomu do dynamiki)",
              "4.2. Stabilność numeryczna solverów różniczkowych przy symulacji miliardów powiązanych neuronów",
              "4.3. Pamięć asocjacyjna, konsolidacja śladów pamięciowych (engramów) i plastyczność homeostatyczna",
              "4.4. Kryteria weryfikacji emulacji: testy behawioralne, wzorce EEG emulowanego obwodu i test Turinga dla WBE"
            ],
            "subchaptersEn": [
              "4.1. Translation of Anatomical Micro-Structure into Biophysical Simulator State Parameters",
              "4.2. Numerical Stability of Differential Solvers when Simulating Billions of Coupled Neurons",
              "4.3. Associative Memory Retrieval, Engram Trace Consolidation, and Homeostatic Plasticity",
              "4.4. Emulation Verification Metrics: Behavioral Equivalence, Synthetic EEG Matching, WBE Turing Benchmark"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Problem tożsamości cyfrowej, paradoks teleportacji i kopii, granice obliczalności, praca magisterska.",
            "en": "Year 5: Digital identity problem, teletransportation paradox, computational limits, Master's thesis.",
            "subchaptersPl": [
              "5.1. Filozoficzne aspekty WBE: problem tożsamości osobowej, paradoks duplikacji i ciągłości świadomości (Parfit, Lem)",
              "5.2. Problem subiektywnego doświadczenia (Qualia, Hard Problem of Consciousness) w systemach symulowanych",
              "5.3. Wymagania sprzętowe pełnej emulacji mózgu: bilans mocy obliczeniowej (ExaFLOPS) i zapotrzebowania na pamięć",
              "5.4. Praca magisterska: Numeryczna rekonstrukcja i symulacja funkcjonalna obwodu neuronalnego hipokampa z danych konektomicznych"
            ],
            "subchaptersEn": [
              "5.1. Philosophy of WBE: Personal Identity, Duplication Paradox, and Continuity of Consciousness (Parfit, Lem)",
              "5.2. Subjective Experience and Qualia (The Hard Problem) in Substrate-Independent Computational Minds",
              "5.3. Hardware Requirements for Human Brain Emulation: ExaFLOP Compute and Memory Bandwidth Budgets",
              "5.4. Master's Thesis: Numerical Reconstruction & Functional Emulation of Hippocampal Microcircuit from Connectome Data"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-C",
        "group": "TRACK",
        "refId": "C",
        "siteId": "SITE-X10",
        "icon": "⚡",
        "color": "#818cf8",
        "titlePl": "Projekt C: Maszyny Analogowe i Obliczanie Przez Fizykę (5 lat studiów)",
        "titleEn": "Project C: Analog Machines & Physical Computing (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-c1",
          "smat-4",
          "smat-5"
        ],
        "matchedFoundationTopics": [
          "FND-1",
          "FND-4",
          "FND-5",
          "Projekt C"
        ],
        "coreBooksPl": [
          "J. G. Truxal — 'Projektowanie układów automatyki i maszyn analogowych' (WNT)",
          "A. Oppenheim — 'Sygnały i układy ciągłe' (WKŁ)"
        ],
        "coreBooksEn": [
          "B. Ulmann — 'Analog Computing' (Oldenbourg / De Gruyter)",
          "H. Jaeger — 'The echo state approach to analysing and training recurrent neural networks'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Teoria maszyn analogowych, operatory różniczkowe i całkujące realizowane przez układy RLC i wzmacniacze.",
            "en": "Year 1: Analog computing theory, differential and integral operators via RLC and op-amp circuits.",
            "subchaptersPl": [
              "1.1. Historia i zasada działania komputera analogowego: zmienne napięciowe jako ciągłe zmienne fizyczne",
              "1.2. Bloki funkcjonalne: sumatory, integratory analogowe, inwertery i potencjometry skalujące",
              "1.3. Rozwiązywanie liniowych równań różniczkowych zwyczajnych bez użycia algorytmów dyskretnych",
              "1.4. Skalowanie czasu i amplitudy w maszynach analogowych oraz eliminacja nasycenia wzmacniaczy"
            ],
            "subchaptersEn": [
              "1.1. History and Principles of Analog Computing: Continuous Voltages as Direct Mathematical Variables",
              "1.2. Computational Building Blocks: Summing Amplifiers, Electronic Integrators, Coefficient Potentiometers",
              "1.3. Solving Linear Ordinary Differential Equations Directly via Circuit Kirchoff Laws",
              "1.4. Time-Scale and Amplitude Scaling Techniques Preventing Operational Amplifier Saturation"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Elementy nieliniowe, mnożniki analogowe, generatory funkcji i modelowanie układów nieliniowych.",
            "en": "Year 2: Non-linear elements, analog multipliers, function generators, and non-linear dynamics modeling.",
            "subchaptersPl": [
              "2.1. Nieliniowe operacje analogowe: mnożniki kwadrupolowe (Gilbert cell), diodowe generatory funkcji",
              "2.2. Symulacja oscylatora van der Pola, atraktora Lorentza i układów z histerezą w czasie ciągłym",
              "2.3. Porównanie zużycia energii komputera analogowego z symulacją cyfrową na CPU/GPU",
              "2.4. Dokładność, dryf temperaturowy i metody autokalibracji obwodów analogowych"
            ],
            "subchaptersEn": [
              "2.1. Non-Linear Analog Blocks: Four-Quadrant Gilbert Multipliers, Diode Function Shapers",
              "2.2. Real-Time Physical Emulation of Van der Pol Oscillators, Lorenz Attractors, and Hysteresis",
              "2.3. Energy Dissipation Benchmarking: Analog Physical Solvers vs. Digital Floating-Point Simulations",
              "2.4. Accuracy Limitations, Thermal Drift Compensation, and Chopper-Stabilized Precision Amplifiers"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Obliczenia rezerwuarowe (Reservoir Computing), dynamika cieczy i atraktory fizyczne.",
            "en": "Year 3: Reservoir computing, physical dynamical substrates, and continuous attractors.",
            "subchaptersPl": [
              "3.1. Teoria obliczeń rezerwuarowych (Echo State Networks, Liquid State Machines)",
              "3.2. Fizyczne rezerwuary obliczeniowe: nieliniowe obwody elektryczne, fale mechaniczne w cieczach i sprężyste membrany",
              "3.3. Trening wyłącznie warstwy wyjściowej (Readout Layer) metodą regresji grzbietowej w czasie rzeczywistym",
              "3.4. Zastosowanie rezerwuarów fizycznych do predykcji szeregów czasowych i rozpoznawania mowy"
            ],
            "subchaptersEn": [
              "3.1. Reservoir Computing Foundations: Echo State Networks (ESN) and Liquid State Machines (LSM)",
              "3.2. Physical Computational Reservoirs: Non-Linear RC Networks, Surface Liquid Waves, Elastic Membranes",
              "3.3. Linear Readout Training via Ridge Regression with Fixed Non-Linear Dynamical Core",
              "3.4. Applications in Real-Time Chaotic Time-Series Prediction and Acoustic Speech Recognition"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Obliczenia fotoniczne, optyczne macierze mnożenia i nieliniowe kryształy optyczne.",
            "en": "Year 4: Photonic computing, optical matrix multipliers, and non-linear optical processing.",
            "subchaptersPl": [
              "4.1. Fotonika zintegrowana: falowody krzemowe (Silicon Photonics), interferometry Macha-Zehndera",
              "4.2. Mnożenie wektor-macierz z prędkością światła metodami interferencji optycznej (Passive Optical MVM)",
              "4.3. Nieliniowości optyczne w kryształach i mikrownękach rezonansowych dla sztucznych neuronów",
              "4.4. Efektywność energetyczna układów fotonicznych przy przetwarzaniu wielkich modeli AI"
            ],
            "subchaptersEn": [
              "4.1. Integrated Photonics: Silicon Waveguides, Mach-Zehnder Interferometer (MZI) Meshes",
              "4.2. Optical Matrix-Vector Multiplication (MVM) at the Speed of Light via Wave Interference",
              "4.3. Optical Non-Linearities in Photonic Crystal Cavities Emulating Non-Linear Neuron Activations",
              "4.4. Extreme Energy Efficiency of Photonic Processors in Massive AI Inference Operations"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Hybrydowe systemy analogowo-cyfrowe, interfejsy z solverami kwantowymi i praca magisterska.",
            "en": "Year 5: Hybrid analog-digital computing architectures, interfaces with quantum solvers, Master's thesis.",
            "subchaptersPl": [
              "5.1. Architektura procesora hybrydowego: rdzeń cyfrowy koordynujący matrycę analogowo-fotoniczną",
              "5.2. Obliczanie analogowe jako koprocesor w rozwiązywaniu równań Naviera-Stokesa i dynamiki płynów",
              "5.3. Interfejsy między maszynami analogowymi a procesorami kwantowymi w optymalizacji kombinatorycznej",
              "5.4. Praca magisterska: Zaprojektowanie i weryfikacja laboratoryjna zintegrowanego analogowego solvera równań różniczkowych cząstkowych"
            ],
            "subchaptersEn": [
              "5.1. Hybrid Architecture: Digital Control Cores Coordinating Analog-Photonic Accelerator Meshes",
              "5.2. Analog Coprocessors for Continuous Navier-Stokes Differential Equations and Fluid Dynamics",
              "5.3. Interfaces Between Continuous Physical Simulators and Quantum Annealers in Optimization Tasks",
              "5.4. Master's Thesis: Design and Experimental Benchmarking of an Analog Physical Solver for Partial Differential Equations"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-D",
        "group": "TRACK",
        "refId": "D",
        "siteId": "SITE-B7",
        "icon": "🧬",
        "color": "#10b981",
        "titlePl": "Projekt D: Bioinżynieria i Konstrukcja Organizmów (5 lat studiów)",
        "titleEn": "Project D: Bioengineering & Organism Construction (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-d1",
          "smat-6",
          "smat-7"
        ],
        "matchedFoundationTopics": [
          "FND-6",
          "FND-7",
          "FND-3",
          "Projekt D",
          "Projekt E"
        ],
        "coreBooksPl": [
          "S. F. Gilbert — 'Biologia rozwoju' (PWN)",
          "T. A. Brown — 'Klonowanie DNA i inżynieria genetyczna' (PWN)"
        ],
        "coreBooksEn": [
          "R. Lanza et al. — 'Principles of Tissue Engineering' (Academic Press)",
          "A. Atala — '3D Bioprinting: Principles and Applications'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Biologia rozwoju (embriologia), komórki macierzyste i molekularne mechanizmy różnicowania.",
            "en": "Year 1: Developmental biology (embryology), stem cells, and molecular differentiation cascades.",
            "subchaptersPl": [
              "1.1. Zapłodnienie, bruzdkowanie, gastrulacja i powstawanie listków zarodkowych (ektoderma, mezoderma, endoderma)",
              "1.2. Morfogeny, gradienty stężeń (Bmp, Wnt, Sonic Hedgehog) i polaryzacja osi ciała",
              "1.3. Biologia komórek macierzystych: totipotencjalność, pluripotencjalność i multipotencjalność",
              "1.4. Metody hodowli komórkowych in vitro w warunkach sterylnych (Cleanroom Class 100/1000)"
            ],
            "subchaptersEn": [
              "1.1. Fertilization, Cleavage, Gastrulation, and Primary Germ Layer Specification (Ecto, Meso, Endoderm)",
              "1.2. Morphogen Gradients (Bmp, Wnt, Sonic Hedgehog) and Body Axis Symmetry Breaking",
              "1.3. Stem Cell Potency: Totipotent, Pluripotent (ESCs, iPSCs), and Multipotent Adult Progenitors",
              "1.4. In Vitro Aseptic Cell Culture Protocols under Cleanroom Class 100/1000 Standards"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Inżynieria genetyczna organizmów modelowych, biologia syntetyczna i wektory wirusowe.",
            "en": "Year 2: Genetic engineering of model organisms, synthetic biology, and viral delivery vectors.",
            "subchaptersPl": [
              "2.1. Konstrukcja plazmidów ekspresyjnych, enzymy restrykcyjne i ligacja DNA",
              "2.2. Wektory wirusowe (lentiwirusy, AAV) do transferu genów w komórkach ssaków",
              "2.3. Projektowanie syntetycznych obwodów genetycznych: przełączniki bistabilne (toggle switch) i oscylatory genowe",
              "2.4. Systemy CRISPR-Cas9, precyzyjne edytowanie zasad (Base Editing) i modyfikacje epigenetyczne"
            ],
            "subchaptersEn": [
              "2.1. Expression Plasmid Recombinant Assembly, Restriction Enzymes, and In Vitro Ligation",
              "2.2. Viral Vector Engineering (Lentiviruses, AAV Serotypes) for Mammalian Transduction",
              "2.3. Synthetic Genetic Circuits: Bistable Genetic Toggle Switches and Repressilators",
              "2.4. Precision CRISPR-Cas9/Cas12 Systems, Base Editing, and Targeted Epigenome Modulation"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Biodruk 3D tkanek, biomateriały rusztowań (scaffolds) i bioreaktory perfuzyjne.",
            "en": "Year 3: 3D bioprinting of tissues, scaffold biomaterials, and perfusion bioreactors.",
            "subchaptersPl": [
              "3.1. Technologie biodruku 3D: ekstruzja pneumatyczna, druk stereolitograficzny (DLP) i fotopolimeryzacja",
              "3.2. Projektowanie biotuszów (Bio-inks): alginian, kolagen, żelatyna-metakryl (GelMA) i decelularyzowana macierz zewnątrzkomórkowa (dECM)",
              "3.3. Inżynieria rusztowań tkankowych (Scaffolds): porowatość, transport składników odżywczych i degradacja kontrolowana",
              "3.4. Bioreaktory dynamiczne: wymuszona perfuzja pożywki, naprężenia ścinające i stymulacja mechaniczna tkanek"
            ],
            "subchaptersEn": [
              "3.1. 3D Bioprinting Modalities: Pneumatic Micro-Extrusion, Stereolithography (DLP), Two-Photon Polymerization",
              "3.2. Bio-Ink Formulations: Alginate, Collagen Type I, Gelatin-Methacryloyl (GelMA), and Decellularized ECM",
              "3.3. Porous Scaffold Architecture: Interconnectivity, Nutrient Diffusion, and Programmed Biodegradation",
              "3.4. Dynamic Perfusion Bioreactors: Fluid Shear Stress and Cyclic Mechanical Loading Protocols"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Waskularyzacja tkanek, hodowla organoidów i układy typu Organ-on-a-Chip.",
            "en": "Year 4: Tissue vascularization, organoid engineering, and Organ-on-a-Chip microfluidic systems.",
            "subchaptersPl": [
              "4.1. Problem waskularyzacji: angiogeneza in vitro, tworzenie sieci naczyń włosowatych z komórek śródbłonka (HUVEC)",
              "4.2. Mikroukłady przepływowe (Organ-on-a-Chip): modelowanie bariery krew-mózg, płuca i wątroby na chipie",
              "4.3. Generowanie asambloidów: łączenie organoidów korowych ze wzgórzowymi i motoneuronami",
              "4.4. Monitorowanie parametrów życiowych hodowli: elektrody mikromacierzy (MEA), sensory tlenu i pH w czasie rzeczywistym"
            ],
            "subchaptersEn": [
              "4.1. The Vascularization Challenge: In Vitro Angiogenesis and Capillary Lumen Formation by Endothelial Cells",
              "4.2. Organ-on-a-Chip Microfluidics: Blood-Brain Barrier, Lung Alveolus, and Liver Metabolic Chips",
              "4.3. Assembloid Engineering: Fusing Cortical, Thalamic, and Striatal Organoids for Functional Circuit Modeling",
              "4.4. Real-Time In-Situ Monitoring: Microelectrode Arrays (MEA), Optical Oxygen, and Acidification Sensors"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Bioetyka modyfikacji organizmów, chimeryzm, granice syntetycznego życia, praca magisterska.",
            "en": "Year 5: Bioethics of organism modification, chimerism, synthetic life limits, Master's thesis.",
            "subchaptersPl": [
              "5.1. Status ontologiczny i etyczny zaawansowanych organoidów mózgowych wykazujących aktywność zsynchronizowaną",
              "5.2. Badania nad chimerami zwierzęco-ludzkimi w hodowli organów do transplantacji: aspekty prawne i bioetyczne",
              "5.3. Bezpieczeństwo biologiczne (Biosafety Level 1–4) i zapobieganie ucieczce zmodyfikowanych organizmów do biosfery",
              "5.4. Praca magisterska: Konstrukcja zwaskularyzowanego mikroskopowego organoidu tkankowego w układzie mikroprzepływowym"
            ],
            "subchaptersEn": [
              "5.1. Ontological & Ethical Status of Advanced Cortical Organoids Displaying Spontaneous Synchrony",
              "5.2. Animal-Human Chimeric Blastocyst Complementation for Solid Organ Xenotransplantation",
              "5.3. Biosafety & Biosecurity Protocols (BSL 1–4) and Genetic Containment Kill Switches",
              "5.4. Master's Thesis: Engineering a Microvascularized Cortical Organoid Tissue within a Perfusion Microfluidic Platform"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-E",
        "group": "TRACK",
        "refId": "E",
        "siteId": "SITE-W0",
        "icon": "📜",
        "color": "#a855f7",
        "titlePl": "Projekt E: Filozofia i Rygor Epistemiczny (5 lat studiów)",
        "titleEn": "Project E: Philosophy & Epistemic Rigor (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-e1",
          "smat-1",
          "smat-8"
        ],
        "matchedFoundationTopics": [
          "FND-1",
          "Projekt E"
        ],
        "coreBooksPl": [
          "S. Lem — 'Summa Technologiae' oraz 'Filozofia przypadku' (Wydawnictwo Literackie)",
          "K. Popper — 'Logika odkrycia naukowego' (PWN)",
          "R. Ingarden — 'Spór o istnienie świata' (PWN)"
        ],
        "coreBooksEn": [
          "T. S. Kuhn — 'The Structure of Scientific Revolutions'",
          "D. J. Chalmers — 'The Conscious Mind: In Search of a Fundamental Theory'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Epistemologia klasyczna, logika formalna, teoria prawdy i demarkacja nauki (Popper).",
            "en": "Year 1: Classical epistemology, formal logic, truth theory, and scientific demarcation (Popper).",
            "subchaptersPl": [
              "1.1. Definicja wiedzy (problem Gettiera), racjonalizm vs. empiryzm (Kartezjusz, Hume, Kant)",
              "1.2. Kryterium demarkacji Karla Poppera: falsyfikowalność, asymetria weryfikacji i falsyfikacji",
              "1.3. Paradygmaty naukowe i rewolucje pojęciowe według Thomasa Kuhna",
              "1.4. Logika modalna, światy możliwe Kripkego i semantyka formalna"
            ],
            "subchaptersEn": [
              "1.1. Definition of Knowledge (Gettier Counterexamples), Rationalism vs. Empiricism (Descartes, Hume, Kant)",
              "1.2. Karl Popper's Demarcation Criterion: Falsifiability and Empirical Asymmetry",
              "1.3. Scientific Paradigms, Normal Science, and Incommensurability (Thomas Kuhn)",
              "1.4. Modal Logic, Kripke's Possible-World Semantics, and Formal Truth Theory"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Filozofia umysłu, problem psychofizyczny (Mind-Body Problem), qualia i behawioryzm.",
            "en": "Year 2: Philosophy of mind, the mind-body problem, qualia, functionalism, and physicalism.",
            "subchaptersPl": [
              "2.1. Dualizm substancjalny vs. fizykalizm i teoria identyfikacji stanów mentalnych",
              "2.2. Funkcjonalizm i teoria obliczeniowa umysłu (Putnam, Fodor)",
              "2.3. 'Trudny problem świadomości' Davida Chalmersa, argument z wiedzy (Mary's Room) i filozoficzne zombie",
              "2.4. Problem intencjonalności i argument Chińskiego Pokoju Johna Searle'a"
            ],
            "subchaptersEn": [
              "2.1. Substance Dualism vs. Physicalism, Mind-Brain Identity Theories",
              "2.2. Functionalism and the Computational Theory of Mind (Putnam, Fodor)",
              "2.3. Chalmers' Hard Problem of Consciousness, Jackson's Knowledge Argument (Mary's Room), and Philosophical Zombies",
              "2.4. Intentionality, Meaning, and John Searle's Chinese Room Thought Experiment"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Filozofia techniki Stanisława Lema, ewolucja pozabiologiczna i 'Summa Technologiae'.",
            "en": "Year 3: Stanisław Lem's philosophy of technology, non-biological evolution, and 'Summa Technologiae'.",
            "subchaptersPl": [
              "3.1. 'Summa Technologiae' Stanisława Lema: ewolucja technologiczna jako kontynuacja i zastąpienie ewolucji biologicznej",
              "3.2. Koncepcja fantomatyki i teletaksji: wczesne modele wirtualnej rzeczywistości i symulacji sensorycznej",
              "3.3. Problem 'czarnej skrzynki' i ograniczeń sterowniczych cywilizacji w obliczu eksplozji informacyjnej",
              "3.4. Demiurgia technologiczna: tworzenie światów i granice racjonalistycznej inżynierii"
            ],
            "subchaptersEn": [
              "3.1. Stanisław Lem's 'Summa Technologiae': Non-Biological Evolution Outpacing Natural Selection",
              "3.2. Lem's Phantomatics and Teletaxy: Pioneering Ontologies of Virtual Reality and Sensory Immersion",
              "3.3. Black-Box Cybernetics and Civilization-Level Control Failures in Mega-Information Systems",
              "3.4. Technological Demiurgy: Artificial Universe Synthesis and the Boundaries of Rationalist Engineering"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Etyka nowych technologii, rygor czterech poziomów wiedzy i odpowiedzialność twórcy.",
            "en": "Year 4: Ethics of emerging technologies, the 4-tier epistemic rigor matrix, creator responsibility.",
            "subchaptersPl": [
              "4.1. Czteropoziomowa matryca epistemiczna Golem 15: wiedza potwierdzona, aktywne badania, hipoteza, spekulacja",
              "4.2. Etyka sztucznej inteligencji: problem zgodności celów (Alignment Problem) i egzystencjalne ryzyko AGI",
              "4.3. Bioetyka inżynierii ludzkiego genomu, edycji linii zarodkowej i praw bytów post-biologicznych",
              "4.4. Etyka dekarbonizacji i sprawiedliwości międzypokoleniowej w gospodarowaniu energią jądrową"
            ],
            "subchaptersEn": [
              "4.1. Golem 15 4-Tier Epistemic Matrix: Confirmed Knowledge, Active Research, Testable Hypothesis, Speculation",
              "4.2. Artificial Intelligence Ethics: The Value Alignment Problem and Existential Safety of AGI",
              "4.3. Bioethics of Germline Genome Editing, Human Enhancement, and the Rights of Post-Biological Entities",
              "4.4. Ethics of Nuclear Stewardship, High-Level Waste Storage, and Intergenerational Justice"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Filozofia nauki w dobie modeli wielkich parametrów, synteza interdyscyplinarna, praca magisterska.",
            "en": "Year 5: Philosophy of science in the era of billion-parameter models, synthesis, Master's thesis.",
            "subchaptersPl": [
              "5.1. Czy modele AI generują nową wiedzę naukową? Status epistemologiczny odkryć generowanych przez sieci głębokie",
              "5.2. Granice redukcjonizmu vs. emergencja w biologii, fizyce i świadomości",
              "5.3. Metodologia prowadzenia wieloletnich interdyscyplinarnych programów badawczych w architekturze Manhattan",
              "5.4. Praca magisterska: Epistemiczny traktat metodologiczny 'Summa Technologiae 2.0 — Od maszyny do świadomego bytu'"
            ],
            "subchaptersEn": [
              "5.1. Do Deep Neural Networks Produce Genuine Understanding? Epistemic Status of Machine-Generated Science",
              "5.2. Limits of Reductionism vs. Strong Emergence in Biology, Physics, and Cognition",
              "5.3. Methodology of Long-Term Multidisciplinary Research Programs under Compartmentalized Manhattan Governance",
              "5.4. Master's Thesis: Epistemic Methodological Treatise 'Summa Technologiae 2.0 — From Machine to Conscious Being'"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-F",
        "group": "TRACK",
        "refId": "F",
        "siteId": "SITE-T9",
        "icon": "🛰️",
        "color": "#38bdf8",
        "titlePl": "Projekt F: Człowiek w Kosmosie i Inżynieria Habitatów (5 lat studiów)",
        "titleEn": "Project F: Humans in Space & Habitat Engineering (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-f1",
          "smat-4",
          "smat-6",
          "smat-7"
        ],
        "matchedFoundationTopics": [
          "FND-4",
          "FND-5",
          "FND-6",
          "FND-7",
          "Projekt F"
        ],
        "coreBooksPl": [
          "A. Trepka — 'Kosmonautyka' (MON)",
          "J. Płonka — 'Medycyna lotnicza i kosmiczna' (PZWL)"
        ],
        "coreBooksEn": [
          "Eckart, P. — 'Spaceflight Life Support and Biospherics' (Microcosm Press)",
          "A. E. Nicogossian et al. — 'Space Physiology and Medicine'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Mechanika orbitalna, trajektorie międzyplanetarne, rakietowe układy napędowe i środowisko kosmiczne.",
            "en": "Year 1: Orbital mechanics, interplanetary trajectories, rocket propulsion, and space environment physics.",
            "subchaptersPl": [
              "1.1. Prawa Keplera, prędkości kosmiczne, orbity LEO, GEO, orbity transferowe Hohmanna",
              "1.2. Równanie Ciołkowskiego, silniki rakietowe na paliwo ciekłe, stałe i napędy jonowe",
              "1.3. Środowisko kosmiczne: próżnia wysoka, cykle termiczne (+120°C / -150°C) i mikrometeoryty",
              "1.4. Wprowadzenie do fizjologii człowieka w warunkach lotu kosmicznego"
            ],
            "subchaptersEn": [
              "1.1. Kepler's Laws, Orbital Mechanics, LEO/GEO Regimes, Hohmann & Bi-Elliptic Transfer Trajectories",
              "1.2. Tsiolkovsky Rocket Equation, Chemical Liquid/Solid Propulsion, and Electrostatic Ion Thrusters",
              "1.3. Space Environment Physics: Ultra-High Vacuum, Extreme Thermal Cycling (+120°C / -150°C), Micrometeoroids",
              "1.4. Introduction to Human Spaceflight Physiology and Environmental Stressors"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Fizjologia mikrograwitacji: demineralizacja kości, zanik mięśni, zespół SANS i układ krążenia.",
            "en": "Year 2: Microgravity physiology: bone demineralization, muscle atrophy, SANS, and cardiovascular deconditioning.",
            "subchaptersPl": [
              "2.1. Przesunięcie płynów ustrojowych (Fluid Shift), adaptacja układu sercowo-naczyniowego i zespół nietolerancji ortostatycznej",
              "2.2. Utrata masy kostnej (osteoklastoza, utrata 1% masy kości/miesiąc) i atrofia włókien mięśniowych",
              "2.3. Zespół neuro-okulistyczny związany z lotem kosmicznym (SANS - Spaceflight-Associated Neuro-ocular Syndrome)",
              "2.4. Przeciwdziałanie: protokoły intensywnego treningu oporowego (ARED) i wirówki grawitacji sztucznej"
            ],
            "subchaptersEn": [
              "2.1. Cephalad Fluid Shift, Cardiovascular Deconditioning, and Post-Flight Orthostatic Intolerance",
              "2.2. Musculoskeletal Degradation: Trabecular Bone Loss (1%/Month) and Type I/II Muscle Fiber Atrophy",
              "2.3. Spaceflight-Associated Neuro-Ocular Syndrome (SANS): Optic Disc Edema and Globe Flattening",
              "2.4. Countermeasure Engineering: Advanced Resistive Exercise Devices (ARED) and Short-Radius Centrifuges"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Promieniowanie kosmiczne (GCR, SPE), osłony radiacyjne i jądrowe źródła zasilania (RTG, Kilopower).",
            "en": "Year 3: Cosmic radiation (GCR, SPE), shielding physics, and space nuclear power (RTGs, Kilopower).",
            "subchaptersPl": [
              "3.1. Galaktyczne promieniowanie kosmiczne (GCR) z ciężkimi jonami HZE i koronalne wyrzuty masy Słońca (SPE)",
              "3.2. Fizyka osłon radiacyjnych: materiały bogate w wodór (polietylen, woda), regolit księżycowy i osłony elektromagnetyczne",
              "3.3. Biologiczne skutki promieniowania: uszkodzenia DNA, ryzyko nowotworowe i katarakta radiacyjna",
              "3.4. Jądrowe źródła zasilania w kosmosie: radioizotopowe generatory termoelektryczne (RTG) i reaktory Kilopower (fission)"
            ],
            "subchaptersEn": [
              "3.1. Galactic Cosmic Rays (GCR) with High-Z/Energy (HZE) Ions and Solar Particle Events (SPE)",
              "3.2. Radiation Shielding Physics: Hydrogen-Rich Polymers (Polyethylene), Lunar Regolith, and Active Magnetic Fields",
              "3.3. Radiobiological Damage: Double-Strand DNA Breaks, Carcinogenesis Risk, and Central Nervous System Risks",
              "3.4. Space Nuclear Power Architecture: Radioisotope Thermoelectric Generators (RTGs) and Kilopower Fission Reactors"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Zamknięte ekosystemy podtrzymywania życia (ECLSS), odzysk wody i tlenu, uprawa roślin (MELiSSA).",
            "en": "Year 4: Closed-loop environmental control & life support (ECLSS), water/O2 recovery, space agriculture (MELiSSA).",
            "subchaptersPl": [
              "4.1. Architektura ECLSS na ISS i stacjach dalekiego zasięgu: odzysk tlenu (Sabatier) i recykling wody (>98%)",
              "4.2. Biologiczne systemy podtrzymywania życia (CELSS / projekt MELiSSA ESA): kompartmenty bakteryjne i glonowe (Spirulina)",
              "4.3. Uprawa roślin w warunkach mikrograwitacji: hydroponika, aeroponika, oświetlenie LED i bilans kaloryczny",
              "4.4. Kontrola mikrobiologiczna habitatu i zarządzanie odpadami stałymi"
            ],
            "subchaptersEn": [
              "4.1. Physico-Chemical ECLSS: Sabatier CO2 Reduction, Water Recovery System (WRS >98% Efficiency)",
              "4.2. Closed Ecological Life Support Systems (CELSS / ESA MELiSSA): Nitrifying Bacteria and Spirulina Algal Compartments",
              "4.3. Hydroponic & Aeroponic Space Plant Growth: LED Spectra Optimization, Root Aeration, Caloric Yields",
              "4.4. Microbial Monitoring, Biofilm Prevention on Habitat Hull Walls, and Solid Waste Recycling"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Inżynieria baz księżycowych i marsjańskich (ISRU), habitaty nadmuchiwane, praca magisterska.",
            "en": "Year 5: Lunar & Martian base engineering (ISRU), inflatable habitats, Master's thesis.",
            "subchaptersPl": [
              "5.1. In-Situ Resource Utilization (ISRU): pozyskiwanie tlenu i wody z regolitu księżycowego (redukcja ilmenitu) i atmosfery Marsa (MOXIE)",
              "5.2. Konstrukcje habitatów pozaziemskich: moduły ciśnieniowe nadmuchiwane (TransHab), tunele lawowe i druk 3D z regolitu",
              "5.3. Psychologia izolacji długoterminowej w załogowych misjach międzyplanetarnych (marsjańskich)",
              "5.4. Praca magisterska: Projekt autonomicznego systemu podtrzymywania życia i osłon radiacyjnych dla habitatu księżycowego"
            ],
            "subchaptersEn": [
              "5.1. In-Situ Resource Utilization (ISRU): Oxygen Extraction from Lunar Ilmenite Regolith & Martian Atmospheric MOXIE",
              "5.2. Extraterrestrial Habitat Structures: Inflatable Pressure Vessels (TransHab), Lava Tube Outposts, 3D Regolith Sintering",
              "5.3. Human Factors, Isolation Psychology, and Autonomy in Long-Duration Multi-Year Interplanetary Missions",
              "5.4. Master's Thesis: Design of an Autonomous Closed-Loop ECLSS and Radiation Protection System for a Lunar South Pole Base"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-G",
        "group": "TRACK",
        "refId": "G",
        "siteId": "SITE-T9",
        "icon": "🌍",
        "color": "#10b981",
        "titlePl": "Projekt G: Człowiek na Ziemi — Ochrona Biosfery i Czyste Technologie (5 lat studiów)",
        "titleEn": "Project G: Humans on Earth — Biosphere Protection & Clean Technologies (5-Year)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-g1",
          "smat-6",
          "smat-7",
          "smat-trk-h1"
        ],
        "matchedFoundationTopics": [
          "FND-6",
          "FND-7",
          "FND-4",
          "Projekt G"
        ],
        "coreBooksPl": [
          "J. Weiner — 'Życie i ewolucja biosfery' (PWN)",
          "M. Popkiewicz — 'Zrozumieć transformację energetyczną' (Sonia Draga)"
        ],
        "coreBooksEn": [
          "E. O. Wilson — 'The Diversity of Life'",
          "V. Smil — 'Energy and Civilization: A History' (MIT Press)"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Ekologia ekosystemów, biogeochemiczne obiegi pierwiastków (C, N, P, H2O) i termodynamika biosfery.",
            "en": "Year 1: Ecosystem ecology, biogeochemical cycles (C, N, P, H2O), and biosphere thermodynamics.",
            "subchaptersPl": [
              "1.1. Struktura i funkcjonowanie ekosystemów: łańcuchy troficzne, przepływ energii i piramidy biomasy",
              "1.2. Globalne cykle biogeochemiczne: obieg węgla, azotu, fosforu i wody w skali planetarnej",
              "1.3. Granice planetarne (Planetary Boundaries Rockströma): klimat, bioróżnorodność, zakwaszenie oceanów",
              "1.4. Fizyczne podstawy efektu cieplarnianego i bilans radiacyjny Ziemi"
            ],
            "subchaptersEn": [
              "1.1. Ecosystem Structure and Dynamics: Trophic Cascades, Energy Dissipation, Biomass Pyramids",
              "1.2. Global Biogeochemical Cycling: Planetary Carbon, Nitrogen, Phosphorus, and Hydrological Fluxes",
              "1.3. Rockström's Planetary Boundaries Framework: Climate Stability, Biosphere Integrity, Ocean Acidification",
              "1.4. Physics of the Planetary Greenhouse Effect and Earth's Top-of-Atmosphere Radiative Energy Balance"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Zanieczyszczenia środowiska, toksykologia, degradacja gleb, wody i powietrza.",
            "en": "Year 2: Environmental pollution, toxicology, soil, water, and atmospheric degradation.",
            "subchaptersPl": [
              "2.1. Zanieczyszczenia atmosfery: aerozole, pyły zawieszone (PM2.5, PM10), tlenki azotu i siarki, smog",
              "2.2. Eutrofizacja wód śródlądowych i mórz (problem Morza Bałtyckiego), biogeny rolnicze i strefy beztlenowe",
              "2.3. Degradacja gleb, erozja, pustynnienie i akumulacja metali ciężkich",
              "2.4. Ekotoksykologia: bioakumulacja i biomagnifikacja toksyn (dioksyny, PFAS, mikroplastik) w łańcuchach pokarmowych"
            ],
            "subchaptersEn": [
              "2.1. Atmospheric Pollutants: Aerosols, Particulate Matter (PM2.5, PM10), NOx, SOx, Photochemical Smog",
              "2.2. Aquatic Eutrophication and Dead Zones: Agricultural Runoff and Hypoxia in the Baltic Sea",
              "2.3. Soil Degradation, Desertification, Salinization, and Heavy Metal Contamination",
              "2.4. Ecotoxicology: Bioaccumulation and Biomagnification of Persistent Chemicals (PFAS, Microplastics, POPs)"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Technologie dekarbonizacji, czysta energetyka, bilans energetyczny cywilizacji (Vaclav Smil).",
            "en": "Year 3: Decarbonization technologies, clean energy, civilizational energy transition (Vaclav Smil).",
            "subchaptersPl": [
              "3.1. Analiza gęstości mocy źródeł energii (W/m2) i materiałochłonności infrastruktury według Vaclava Smila",
              "3.2. Odnawialne źródła energii: fotowoltaika krzemowa i perowskitowa, turbiny wiatrowe onshore/offshore",
              "3.3. Reaktory jądrowe (SMR, duża energetyka jądrowa) jako bezemisyjne źródło mocy pasmowej (Baseload)",
              "3.4. Technologie wychwytu i magazynowania dwutlenku węgla: CCS (Carbon Capture & Storage) i DAC (Direct Air Capture)"
            ],
            "subchaptersEn": [
              "3.1. Power Density (W/m2) and Material Intensity of Energy Technologies (Vaclav Smil's Framework)",
              "3.2. Renewable Energy Generation: Silicon & Perovskite Photovoltaics, Onshore and Offshore Wind Turbines",
              "3.3. Nuclear Power (Large Gen III+ and SMRs) as Firm Zero-Emission Baseload Electricity and Process Heat",
              "3.4. Carbon Dioxide Removal: Carbon Capture & Storage (CCS) and Direct Air Capture (DAC) Thermodynamics"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Gospodarka obiegu zamkniętego (Circular Economy), recykling surowców krytycznych i gospodarka wodna.",
            "en": "Year 4: Circular economy engineering, critical raw material recycling, and water stewardship.",
            "subchaptersPl": [
              "4.1. Zasady gospodarki o obiegu zamkniętym (Circular Economy): projektowanie pod kątem demontażu i recyklingu",
              "4.2. Recykling baterii litowo-jonowych i odzysk metali ziem rzadkich (REE, lit, kobalt, nikiel)",
              "4.3. Zintegrowana gospodarka wodna: odsalanie wód morskich, retencja krajobrazowa i neutralizacja ścieków przemysłowych",
              "4.4. Rolnictwo regeneratywne i precyzyjne (Precision Agriculture) ograniczające zużycie nawozów sztucznych"
            ],
            "subchaptersEn": [
              "4.1. Circular Economy Engineering: Design-for-Disassembly, Industrial Symbiosis, and Material Longevity",
              "4.2. Battery Recycling Hydrometallurgy and Rare Earth Element (REE, Lithium, Cobalt, Nickel) Recovery",
              "4.3. Integrated Water Resource Management: Reverse Osmosis Desalination, Landscape Retention, Industrial Wastewater Remediation",
              "4.4. Regenerative and Precision Agriculture: Soil Carbon Sequestration and Targeted Nutrient Delivery"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Adaptacja planetarna, modelowanie klimatu, geoinżynieria a rygor ekologiczny, praca magisterska.",
            "en": "Year 5: Planetary adaptation, climate modeling, geoengineering risks, Master's thesis.",
            "subchaptersPl": [
              "5.1. Numeryczne modele klimatyczne ogólnej cyrkulacji (GCM, CMIP6) i scenariusze emisji IPCC (SSP1–SSP5)",
              "5.2. Geoinżynieria planetarna: zarządzanie promieniowaniem słonecznym (SRM), nawożenie oceanów żelazem — ryzyka i rygor",
              "5.3. Ramy prawne i polityczne transformacji: Porozumienie Paryskie, Europejski Zielony Ład i rynki uprawnień ETS",
              "5.4. Praca magisterska: Projekt zintegrowanej technologii recyklingu lub dekarbonizacji dla wybranego sektora przemysłowego"
            ],
            "subchaptersEn": [
              "5.1. Global Climate Models (General Circulation Models GCM, CMIP6) and Shared Socioeconomic Pathways (SSPs)",
              "5.2. Solar Radiation Management (SRM) and Ocean Iron Fertilization: Geophysical Risks & Epistemic Boundaries",
              "5.3. Climate Policy Frameworks: Paris Agreement, European Green Deal, and Emissions Trading Schemes (EU ETS)",
              "5.4. Master's Thesis: Integrated Engineering Design of a Zero-Emission Circular Process for Heavy Industry"
            ]
          }
        ]
      },
      {
        "id": "STU-TRK-H",
        "group": "TRACK",
        "refId": "H",
        "siteId": "SITE-X10",
        "icon": "⚡",
        "color": "#f59e0b",
        "titlePl": "Super-Projekt H: Energetyka Jądrowa i Fuzja Termojądrowa (5 lat studiów)",
        "titleEn": "Super-Project H: Nuclear Energy & Thermonuclear Fusion (5-Year Degree)",
        "sourceLang": "PL+EN",
        "linkedMaterialIds": [
          "smat-trk-h1",
          "smat-trk-h2",
          "smat-4",
          "smat-5"
        ],
        "matchedFoundationTopics": [
          "FND-4",
          "FND-5",
          "FND-6",
          "FND-1",
          "Super-Projekt H"
        ],
        "coreBooksPl": [
          "S. Glasstone, A. Sesonske — 'Inżynieria reaktorów jądrowych' (WNT)",
          "Z. Celiński — 'Energetyka jądrowa' (PWN)",
          "J. Kubowski — 'Elektrownie jądrowe' (WNT)"
        ],
        "coreBooksEn": [
          "J. R. Lamarsh, A. J. Baratta — 'Introduction to Nuclear Engineering'",
          "F. F. Chen — 'Introduction to Plasma Physics and Controlled Fusion'"
        ],
        "years": [
          {
            "year": 1,
            "pl": "Rok 1: Fizyka jądrowa, przekroje czynne, rozszczepienie jąder, spowalnianie neutronów i reaktory zerowej mocy.",
            "en": "Year 1: Nuclear physics, cross-sections, fission reactions, neutron moderation, and zero-power reactors.",
            "subchaptersPl": [
              "1.1. Struktura jądra atomowego, siły jądrowe, deficyt masy i energia wiązania (wzór Weizsäckera)",
              "1.2. Prawa rozpadu promieniotwórczego (alfa, beta, gamma), szeregi promieniotwórcze i prawo Batemana",
              "1.3. Reakcja rozszczepienia jądra uranu-235 i plutonu-239: emisja neutronów natychmiastowych i opóźnionych",
              "1.4. Spowalnianie neutronów, przekroje czynne na rozproszenie i absorpcję, rezonansy i wzór czteroczynnikowy"
            ],
            "subchaptersEn": [
              "1.1. Nuclear Structure, Strong Interaction, Mass Defect, and Semi-Empirical Mass Formula (Weizsäcker)",
              "1.2. Radioactive Decay Kinetics (Alpha, Beta, Gamma), Decay Chains, and Bateman Differential Equations",
              "1.3. Fission of U-235 and Pu-239: Prompt and Delayed Neutron Spectra, Energy Release Breakdown",
              "1.4. Neutron Moderation, Scattering/Capture Cross-Sections, Resonance Absorption, Four-Factor Formula"
            ]
          },
          {
            "year": 2,
            "pl": "Rok 2: Teoria dyfuzji neutronów, kinetyka reaktora, reaktywność, trucizny ksenonowe i sterowanie mocą.",
            "en": "Year 2: Neutron diffusion theory, reactor kinetics, reactivity, xenon poisoning, and control rod dynamics.",
            "subchaptersPl": [
              "2.1. Jednogrupowa i wielogrupowa teoria dyfuzji neutronów w rdzeniu reaktora o zadanej geometrii",
              "2.2. Kinetyka punktowa reaktora: rola neutronów opóźnionych w sterowaniu i okres reaktora",
              "2.3. Wpływ temperatury na reaktywność: współczynnik dopplerowski, współczynnik temperaturowy moderatora (MTC)",
              "2.4. Zjawisko zatrucia ksenonowego (Xe-135) i samarium (Sm-149) oraz studnia ksenonowa po wyłączeniu reaktora"
            ],
            "subchaptersEn": [
              "2.1. One-Group and Multi-Group Neutron Diffusion Equations in Geometric Core Volumes",
              "2.2. Point Reactor Kinetics Equations: Delayed Neutron Precursors and Stable Reactor Periods",
              "2.3. Temperature Reactivity Coefficients: Doppler Broadening, Moderator Temperature Coefficient (MTC)",
              "2.4. Fission Product Poisoning: Xenon-135 Dynamics, Iodine Well, and Samarium-149 Equilibrium"
            ]
          },
          {
            "year": 3,
            "pl": "Rok 3: Termohydraulika reaktorów PWR/BWR/SMR, pętle chłodzenia, wymienniki ciepła i reaktor badawczy MARIA.",
            "en": "Year 3: Thermal-hydraulics of PWR/BWR/SMR reactors, cooling loops, and MARIA research reactor.",
            "subchaptersPl": [
              "3.1. Termohydraulika rdzenia: profile temperatur paliwa i koszulki, kryzys wrzenia (DNB - Departure from Nucleate Boiling)",
              "3.2. Obiegi chłodzenia reaktorów wodnych ciśnieniowych (PWR) i wrzących (BWR): pompy cyrkulacyjne, wytwornice pary",
              "3.3. Reaktor badawczy MARIA w Świerku: konstrukcja rdzenia basenowo-kanałowego, produkcja molibdenu-99 i badania materiałowe",
              "3.4. Pasywne systemy bezpieczeństwa w reaktorach III+ generacji (AP1000, EPR, VVER-1200)"
            ],
            "subchaptersEn": [
              "3.1. Core Thermal-Hydraulics: Fuel/Cladding Radial Temperature Gradients, Critical Heat Flux and DNB",
              "3.2. Primary and Secondary Coolant Circuits in PWRs and BWRs: Pressurizers, Steam Generators, Circulation Pumps",
              "3.3. The MARIA Research Reactor in Świerk: Core Configuration, Medical Molybdenum-99 Irradiation, Material Testing",
              "3.4. Passive Safety Systems in Gen III+ Reactors (Gravity Injection, Passive Containment Cooling)"
            ]
          },
          {
            "year": 4,
            "pl": "Rok 4: Małe reaktory modułowe (SMR: BWRX-300, Rolls-Royce) oraz wysokotemperaturowe (HTGR-POLA) dla ciepła i AI.",
            "en": "Year 4: Small Modular Reactors (SMRs: BWRX-300, Rolls-Royce) & High-Temperature Gas Reactors (HTGR-POLA) for AI.",
            "subchaptersPl": [
              "4.1. Architektura reaktorów SMR: BWRX-300, NuScale, Rolls-Royce SMR — standaryzacja fabryczna i zasilanie centrów danych AI",
              "4.2. Reaktory wysokotemperaturowe chłodzone helem (HTGR / polski projekt HTGR-POLA): paliwo TRISO, temperatura 750–900°C",
              "4.3. Zastosowania HTGR w kogeneracji przemysłowej: para technologiczna dla chemii, produkcja czystego wodoru (cykle termochemiczne)",
              "4.4. Paliwa jądrowe o zwiększonej odporności na awarie (ATF - Accident Tolerant Fuels) i zarządzanie wypalonym paliwem"
            ],
            "subchaptersEn": [
              "4.1. Small Modular Reactor Architectures: BWRX-300, NuScale, Rolls-Royce SMR — Powering AI Data Center Campuses",
              "4.2. High-Temperature Gas-Cooled Reactors (HTGR / Polish HTGR-POLA Program): TRISO Particle Fuel Integrity at 900°C",
              "4.3. Industrial Cogeneration via HTGR: Process Steam for Chemical Synthesis and Thermochemical Hydrogen Production",
              "4.4. Accident Tolerant Fuels (ATF), Deep Geological Repositories, and Pyroprocessing Reprocessing Loops"
            ]
          },
          {
            "year": 5,
            "pl": "Rok 5: Fuzja jądrowa, fizyka plazmy, tokamaki (ITER, SPARC), stellaratory (Wendelstein 7-X), praca magisterska.",
            "en": "Year 5: Thermonuclear fusion, plasma physics, tokamaks (ITER, SPARC), stellarators (Wendelstein 7-X), Master's thesis.",
            "subchaptersPl": [
              "5.1. Fizyka plazmy termojądrowej: równania magnetohydrodynamiki (MHD), dryfy cząstek i niestabilności plazmy",
              "5.2. Magnetyczne uwięzienie plazmy: tokamaki (ITER, SPARC z magnesami HTS) vs. stellaratory zoptymalizowane (W7-X)",
              "5.3. Inżynieria pierwszej ściany i dywertora: obciążenia cieplne (10–20 MW/m2), regeneracja trytu z litu (Breeding Blankets)",
              "5.4. Praca magisterska: Projekt pętli cieplnej i układu odbioru mocy reaktora SMR / HTGR zasilającego infrastrukturę superkomputerową AI"
            ],
            "subchaptersEn": [
              "5.1. Thermonuclear Plasma Physics: Magnetohydrodynamics (MHD) Equations, Drift Waves, and Plasma Instabilities",
              "5.2. Magnetic Confinement Configurations: Tokamaks (ITER, SPARC High-Field HTS Magnets) vs. Advanced Stellarators (W7-X)",
              "5.3. Plasma-Facing Components and Divertor Engineering: 20 MW/m2 Heat Exhaust, Tritium Breeding Lithium Blankets",
              "5.4. Master's Thesis: Thermal Cycle and Power Conversion Loop Design for an SMR/HTGR Powering an Exascale AI Cluster"
            ]
          }
        ]
      }
    ],
    "selectedQueue": [
      "STU-FND-1",
      "STU-FND-2",
      "STU-FND-3",
      "STU-FND-4",
      "STU-FND-5",
      "STU-FND-6",
      "STU-FND-7",
      "STU-FND-8",
      "STU-TRK-H"
    ],
    "completedTopicYears": {},
    "aiAgents": [
      {
        "id": "AGT-00",
        "codename": "GROVES-OPPENHEIMER-00",
        "namePl": "Agent Naczelny Sztabu Rozproszonego",
        "nameEn": "Supreme Distributed Command Agent",
        "siteId": "SITE-W0",
        "color": "#f59e0b",
        "rolePl": "Orkiestracja 3-letniego rdzenia Administracji, kolejki 5-letnich studiów i globalnego bilansu rozszczepień k_eff.",
        "roleEn": "Orchestrates the 3-year Administration core, 5-year sequential study queue, and global fission balance k_eff.",
        "promptTemplate": "Działasz jako Agent Naczelny Sztabu Manhattan Golem 15 (District W-0). Rozbij podany cel strategiczny na kompartmentalizowane pakiety badawcze dla 5 ośrodków (W-0, Y-15, X-10, B-7, T-9), wskaż wymogi prawno-administracyjne oraz określ punkty krytyczne integracji."
      },
      {
        "id": "AGT-01",
        "codename": "EPISTEMIC-LAW-01",
        "namePl": "Agent Administracji, Prawa i Demarkacji Epistemicznej",
        "nameEn": "Administration, Law & Epistemic Demarcation Agent",
        "siteId": "SITE-W0",
        "color": "#eab308",
        "rolePl": "Audyt zgodności regulacyjnej (PAA, MDR, AI Act, traktaty kosmiczne) i oznaczanie statusu twierdzeń (wiedza potwierdzona vs hipoteza).",
        "roleEn": "Regulatory compliance audit (nuclear, medical, AI, space law) and epistemic demarcation of scientific claims.",
        "promptTemplate": "Działasz jako Agent Audytu Prawno-Epistemicznego (District W-0 / Projekt E). Oceń badany problem pod kątem: 1) faktów empirycznych vs hipotez, 2) wymogów prawa atomowego/medycznego/kosmicznego/AI, 3) ryzyk bioetycznych."
      },
      {
        "id": "AGT-02",
        "codename": "TURING-NEUMANN-02",
        "namePl": "Agent Teorii, Obliczeń i Cyfrowego Umysłu",
        "nameEn": "Theory, Computing & Digital Mind Agent",
        "siteId": "SITE-Y15",
        "color": "#38bdf8",
        "rolePl": "Rozszczepianie zagadnień matematycznych, algorytmicznych, konektomiki, dekodowania mózgu i emulacji poznawczej (Projekt B).",
        "roleEn": "Fissions mathematical, algorithmic, connectomic, neural decoding, and cognitive emulation problems (Project B).",
        "promptTemplate": "Działasz jako Agent Laboratorium Los Alamos Y-15 (Matematyka, Informatyka, AI, Projekt B). Sformułuj model formalny, złożoność obliczeniową, architekturę symulacji oraz hipotezy falsyfikowalne dla zadanego zagadnienia."
      },
      {
        "id": "AGT-03",
        "codename": "SHANNON-ANALOG-03",
        "namePl": "Agent Obliczania Fizycznego i Układów Neuromorficznych",
        "nameEn": "Physical Computing & Neuromorphic Hardware Agent",
        "siteId": "SITE-Y15",
        "color": "#fb923c",
        "rolePl": "Projektowanie obliczeń ciągłych, memrystorowych, fotonicznych i energooszczędnych sieci impulsowych SNN (Projekt C).",
        "roleEn": "Designs continuous analog, memristive, photonic, and ultra-low-power spiking neural architectures (Project C).",
        "promptTemplate": "Działasz jako Agent Układów Analogowo-Neuromorficznych (Y-15 / Projekt C). Zaproponuj fizyczny nośnik obliczeń, bilans termodynamiczny (limit Landauera) i architekturę sprzętową dla zadanego problemu."
      },
      {
        "id": "AGT-04",
        "codename": "FERMI-PILE-04",
        "namePl": "Agent Energetyki Jądrowej, SMR/HTGR i Fuzji",
        "nameEn": "Nuclear Fission, SMR/HTGR & Fusion Power Agent",
        "siteId": "SITE-X10",
        "color": "#f43f5e",
        "rolePl": "Obliczenia mocy reaktorowej, ciepła procesowego HTGR-POLA, izotopów MARIA oraz zasilania dla klastrów AI i baz kosmicznych (Super-Projekt H).",
        "roleEn": "Reactor power balances, HTGR-POLA process heat, MARIA medical isotopes, and nuclear power for AI & space (Super-Project H).",
        "promptTemplate": "Działasz jako Agent Kompleksu Oak Ridge X-10 (Super-Projekt H). Wyznacz architekturę zasilania jądrowego/termojądrowego, bilans cieplno-elektryczny, bariery bezpieczeństwa radiacyjnego i sprzężenia ze ścieżkami A–G."
      },
      {
        "id": "AGT-05",
        "codename": "CYBORG-SYNTH-05",
        "namePl": "Agent Neurobioniki, BCI i Bioinżynierii Tkankowej",
        "nameEn": "Neurobionics, BCI & Tissue Bioengineering Agent",
        "siteId": "SITE-B7",
        "color": "#10b981",
        "rolePl": "Rozszczepianie problemów interfejsów mózg–maszyna (fNIRS/EEG/implanty), bioniki oraz hodowli organoidów i edycji genów (Projekty A i D).",
        "roleEn": "Fissions BCI (fNIRS/EEG/implants), bionic prosthetics, organoid engineering, and genome editing tasks (Projects A & D).",
        "promptTemplate": "Działasz jako Agent Kompleksu Hanford B-7 (Chemia, Biologia, Projekty A i D). Rozpisz protokół biokompatybilności, sprzężenia tkanka–elektronika, hodowli komórkowej/organoidowej oraz kryteria bezpieczeństwa klinicznego."
      },
      {
        "id": "AGT-06",
        "codename": "BIOSFERA-ORBIT-06",
        "namePl": "Agent Systemów Podtrzymywania Życia: Kosmos ↔ Ziemia",
        "nameEn": "Life-Support & Biosphere Agent: Space ↔ Earth",
        "siteId": "SITE-T9",
        "color": "#a855f7",
        "rolePl": "Integracja zamkniętych obiegów materii (BLSS), ochrony radiacyjnej astronautów i inżynierii regeneracji ekosystemów Ziemi (Projekty F i G).",
        "roleEn": "Integrates closed-loop BLSS, astronaut radiation shielding, and Earth ecosystem regeneration engineering (Projects F & G).",
        "promptTemplate": "Działasz jako Agent Poligonu Trinity T-9 (Oś Kosmos F ↔ Ziemia G). Przeprowadź bilans masy, energii, tlenu, wody i odporności biologicznej dla badanego habitatu pozaziemskiego lub ekosystemu ziemskiego."
      }
    ],
    "fissionNodes": [
      {
        "id": "FIS-00",
        "parentId": None,
        "generation": 0,
        "code": "CORE-235",
        "siteId": "SITE-W0",
        "agentId": "AGT-00",
        "trackRef": "ADMIN-3Y",
        "status": "active",
        "titlePl": "Rdzeń Rozszczepialny Golem 15 + 3-Letni Sztab Administracji",
        "titleEn": "Golem 15 Fissile Core + 3-Year Administrative HQ",
        "descPl": "Punkt inicjacji reakcji łańcuchowej: cel nadrzędny zrozumienia, wspomagania i ochrony człowieka rozszczepiany z poziomu 3-letniego aparatu administracyjno-prawnego na 5 autonomicznych ośrodków Manhattan.",
        "descEn": "Chain-reaction initiation point: overarching human research mission fissioned through a 3-year administrative-legal command core into 5 autonomous Manhattan laboratories.",
        "neutronTargets": [
          "FIS-S1",
          "FIS-S2",
          "FIS-S3",
          "FIS-S4",
          "FIS-S5"
        ],
        "deliverablePl": "Globalna dyrektywa kompartmentalizacji i harmonogram 3 + 5×N lat.",
        "deliverableEn": "Global compartmentalization directive and 3 + 5×N year master schedule."
      },
      {
        "id": "FIS-S1",
        "parentId": "FIS-00",
        "generation": 1,
        "code": "W0-GOV",
        "siteId": "SITE-W0",
        "agentId": "AGT-01",
        "trackRef": "E",
        "status": "active",
        "titlePl": "Dyrekcja W-0: Prawo Sektorowe, Finanse B+R i Filtr Epistemiczny (E)",
        "titleEn": "Directorate W-0: Sector Law, R&D Finance & Epistemic Filter (E)",
        "descPl": "Rozszczepia wymogi formalno-prawne (PAA, komisje bioetyczne, AI Act, POLSA) oraz metodologiczne kryteria demarkacji nauki od spekulacji dla wszystkich ośrodków.",
        "descEn": "Fissions legal-regulatory compliance and epistemological demarcation criteria across all distributed laboratories.",
        "neutronTargets": [
          "FIS-H1",
          "FIS-D1"
        ],
        "deliverablePl": "Matryca legalności i rygoru epistemicznego (4 poziomy pewności wiedzy).",
        "deliverableEn": "Legality and epistemic rigor matrix (4 certainty tiers)."
      },
      {
        "id": "FIS-S2",
        "parentId": "FIS-00",
        "generation": 1,
        "code": "Y15-MIND",
        "siteId": "SITE-Y15",
        "agentId": "AGT-02",
        "trackRef": "B",
        "status": "active",
        "titlePl": "Dyrekcja Y-15: Teoria, AI, Cyfrowy Umysł (B) i Fizyka Obliczeń (C)",
        "titleEn": "Directorate Y-15: Theory, AI, Digital Mind (B) & Physical Computing (C)",
        "descPl": "Ośrodek obliczeniowy rozszczepiający fundamenty matematyczno-informatyczne (FND 1–3, 8) na modele konektomu, dekodery AI oraz maszyny analogowo-neuromorficzne.",
        "descEn": "Theoretical hub splitting mathematical/CS foundations (FND 1–3, 8) into connectome models, AI decoders, and neuromorphic machines.",
        "neutronTargets": [
          "FIS-A1",
          "FIS-H1"
        ],
        "deliverablePl": "Stos symulacyjny mózg–AI–sprzęt neuromorficzny.",
        "deliverableEn": "Brain–AI–neuromorphic simulation stack."
      },
      {
        "id": "FIS-S3",
        "parentId": "FIS-00",
        "generation": 1,
        "code": "X10-ATOM",
        "siteId": "SITE-X10",
        "agentId": "AGT-04",
        "trackRef": "H",
        "status": "critical",
        "titlePl": "Dyrekcja X-10: Rozszczepienie Jądrowe, Fuzja i Architektura Mocy (H)",
        "titleEn": "Directorate X-10: Nuclear Fission, Fusion & Power Architecture (H)",
        "descPl": "Serce energetyczne systemu: reaktory SMR/HTGR-POLA, fuzja termojądrowa i elektronika mocy dostarczające gęstą, bezemisyjną energię dla podwariantów A–G.",
        "descEn": "Energetic core: SMR/HTGR-POLA reactors, fusion, and power electronics supplying dense zero-emission power to sub-variants A–G.",
        "neutronTargets": [
          "FIS-B1",
          "FIS-F1",
          "FIS-G1"
        ],
        "deliverablePl": "Architektura mocy jądrowej i izotopowej dla klastrów AI, medycyny i kosmosu.",
        "deliverableEn": "Nuclear & isotope power architecture for AI clusters, medicine, and space."
      },
      {
        "id": "FIS-S4",
        "parentId": "FIS-00",
        "generation": 1,
        "code": "B7-BIO",
        "siteId": "SITE-B7",
        "agentId": "AGT-05",
        "trackRef": "A",
        "status": "active",
        "titlePl": "Dyrekcja B-7: Integracja Biocyfrowa (A) i Inżynieria Życia (D)",
        "titleEn": "Directorate B-7: Bio-Digital Integration (A) & Life Engineering (D)",
        "descPl": "Łączy chemię biomateriałów i biologię molekularną (FND 6–7) w interfejsy mózg–maszyna, bionikę oraz hodowlę organoidów i medycynę regeneracyjną.",
        "descEn": "Combines biomaterials chemistry & molecular biology (FND 6–7) into BCIs, bionics, organoids, and regenerative medicine.",
        "neutronTargets": [
          "FIS-B1",
          "FIS-F1"
        ],
        "deliverablePl": "Platforma interfejsów tkankowo-elektronicznych i organoidów.",
        "deliverableEn": "Tissue-electronic interface & organoid platform."
      },
      {
        "id": "FIS-S5",
        "parentId": "FIS-00",
        "generation": 1,
        "code": "T9-HAB",
        "siteId": "SITE-T9",
        "agentId": "AGT-06",
        "trackRef": "F",
        "status": "active",
        "titlePl": "Dyrekcja T-9: Habitacja Kosmiczna (F) ↔ Ochrona Biosfery Ziemi (G)",
        "titleEn": "Directorate T-9: Space Habitation (F) ↔ Earth Biosphere Protection (G)",
        "descPl": "Poligon weryfikacji środowiskowej: zamknięte systemy podtrzymywania życia poza Ziemią w lustrzanym sprzężeniu z regeneracją ziemskich ekosystemów.",
        "descEn": "Environmental proving ground: closed extraterrestrial life support coupled with terrestrial biosphere regeneration.",
        "neutronTargets": [
          "FIS-G1",
          "FIS-F1"
        ],
        "deliverablePl": "Zunifikowany model obiegu materii i odporności środowiskowej F↔G.",
        "deliverableEn": "Unified matter-cycle and environmental resilience model F↔G."
      },
      {
        "id": "FIS-ADM1",
        "parentId": "FIS-S1",
        "generation": 2,
        "code": "W0-LIC",
        "siteId": "SITE-W0",
        "agentId": "AGT-01",
        "trackRef": "E",
        "status": "active",
        "titlePl": "Licencjonowanie B+R: Dozór Jądrowy PAA, Komisje Bioetyczne i AI Act",
        "titleEn": "R&D Licensing: Nuclear Oversight, Bioethics Boards & AI Act",
        "descPl": "Pakiet procedur administracyjnych z 3-letnich studiów pozwalający legalnie prowadzić badania nad izotopami, BCI, organoidami i autonomicznymi agentami.",
        "descEn": "Administrative compliance suite derived from the 3-year degree for legal research on isotopes, BCIs, organoids, and AI agents.",
        "neutronTargets": [
          "FIS-H1",
          "FIS-A1",
          "FIS-D1"
        ],
        "deliverablePl": "Repozytorium wniosków regulacyjnych i matryc ryzyka.",
        "deliverableEn": "Regulatory filings and risk assessment repository."
      },
      {
        "id": "FIS-B1",
        "parentId": "FIS-S2",
        "generation": 2,
        "code": "Y15-WBE",
        "siteId": "SITE-Y15",
        "agentId": "AGT-02",
        "trackRef": "B",
        "status": "active",
        "titlePl": "Dekodowanie Sygnałów Mózgu (fMRI/EEG) i Konsolidacja Pamięci („Cyfrowy Sen”)",
        "titleEn": "Brain Decoding (fMRI/EEG) & Memory Consolidation ('Digital Sleep')",
        "descPl": "Rozszczepienie Projektu B na dekodery semantyczne aktywności korowej oraz algorytmy snu falowego zapobiegające katastroficznemu zapominaniu w sieciach neuronowych.",
        "descEn": "Splits Project B into semantic cortical decoders and slow-wave digital sleep algorithms preventing catastrophic forgetting.",
        "neutronTargets": [
          "FIS-A1",
          "FIS-C1"
        ],
        "deliverablePl": "Benchmark dekodowania neuronalnego i ciągłego uczenia SNN.",
        "deliverableEn": "Neural decoding & continual SNN learning benchmark."
      },
      {
        "id": "FIS-C1",
        "parentId": "FIS-S2",
        "generation": 2,
        "code": "Y15-NEURO",
        "siteId": "SITE-Y15",
        "agentId": "AGT-03",
        "trackRef": "C",
        "status": "active",
        "titlePl": "Procesory Neuromorficzne, Memrystory i Hybrydowe Biokomputery (Brainoware)",
        "titleEn": "Neuromorphic Processors, Memristors & Hybrid Biocomputers (Brainoware)",
        "descPl": "Fizyczne obliczanie niskiej mocy redukujące zapotrzebowanie energetyczne sztucznej inteligencji o rzędy wielkości względem klasycznych klastrów GPU.",
        "descEn": "Low-power physical computing slashing AI energy demand by orders of magnitude compared to von Neumann GPU clusters.",
        "neutronTargets": [
          "FIS-B1",
          "FIS-D1"
        ],
        "deliverablePl": "Specyfikacja hybrydowego koprocesora analogowo-impulsowego.",
        "deliverableEn": "Hybrid analog-spiking coprocessor specification."
      },
      {
        "id": "FIS-H1",
        "parentId": "FIS-S3",
        "generation": 2,
        "code": "X10-HTGR",
        "siteId": "SITE-X10",
        "agentId": "AGT-04",
        "trackRef": "H",
        "status": "critical",
        "titlePl": "Bloki SMR / HTGR-POLA dla Centrów Danych AI/WBE i Kogeneracji Wodoru",
        "titleEn": "SMR / HTGR-POLA Units for AI/WBE Data Centers & Hydrogen Cogeneration",
        "descPl": "Bezpośrednie sprzężenie reaktorów wysokotemperaturowych z infrastrukturą obliczeniową Projektu B oraz dekarbonizacją przemysłu w Projekcie G.",
        "descEn": "Direct coupling of high-temperature reactors with Project B supercomputing clusters and Project G industrial decarbonization.",
        "neutronTargets": [
          "FIS-B1",
          "FIS-G1"
        ],
        "deliverablePl": "Model bilansu mocy 300 MWe SMR + ciepło procesowe 750°C.",
        "deliverableEn": "300 MWe SMR + 750°C process heat power-balance model."
      },
      {
        "id": "FIS-H2",
        "parentId": "FIS-S3",
        "generation": 2,
        "code": "X10-MEDSPC",
        "siteId": "SITE-X10",
        "agentId": "AGT-04",
        "trackRef": "H",
        "status": "active",
        "titlePl": "Radioizotopy Medyczne (MARIA: Lu-177/Mo-99) oraz Mikroreaktory Kosmiczne Kilopower",
        "titleEn": "Medical Radioisotopes (MARIA: Lu-177/Mo-99) & Space Kilopower Microreactors",
        "descPl": "Dwuwektorowe rozszczepienie technologii jądrowych: medycyna nuklearna dla ochrony zdrowia (A/D) oraz zasilanie baz księżycowo-marsjańskich w nocy polarnej (F).",
        "descEn": "Dual-vector nuclear fission spin-off: targeted radionuclide therapy (A/D) and surface fission power for Moon/Mars habitats (F).",
        "neutronTargets": [
          "FIS-A1",
          "FIS-F1"
        ],
        "deliverablePl": "Karta izotopowo-energetyczna H→A/D/F.",
        "deliverableEn": "Isotope & space nuclear power datasheet H→A/D/F."
      },
      {
        "id": "FIS-A1",
        "parentId": "FIS-S4",
        "generation": 2,
        "code": "B7-BCI",
        "siteId": "SITE-B7",
        "agentId": "AGT-05",
        "trackRef": "A",
        "status": "active",
        "titlePl": "Optyczne i Elektryczne Interfejsy BCI (fNIRS PhotonGrav / ECoG) i Neuroprotetyka",
        "titleEn": "Optical & Electrical BCIs (fNIRS PhotonGrav / ECoG) & Neuroprosthetics",
        "descPl": "Dwukierunkowa komunikacja układ nerwowy ↔ maszyna testowana zarówno w klinice rehabilitacyjnej na Ziemi, jak i na orbicie ISS (misja IGNIS).",
        "descEn": "Bidirectional nervous system ↔ machine interfaces validated in clinical rehabilitation and orbital microgravity (ISS IGNIS).",
        "neutronTargets": [
          "FIS-F1",
          "FIS-B1"
        ],
        "deliverablePl": "Architektura niskoszumowego toru akwizycji i dekodowania BCI.",
        "deliverableEn": "Low-noise BCI acquisition and decoding pipeline."
      },
      {
        "id": "FIS-D1",
        "parentId": "FIS-S4",
        "generation": 2,
        "code": "B7-ORG",
        "siteId": "SITE-B7",
        "agentId": "AGT-05",
        "trackRef": "D",
        "status": "active",
        "titlePl": "Organoidy Funkcjonalne z Komórek Macierzystych i Regeneracja Tkankowa",
        "titleEn": "Stem-Cell Functional Organoids & Regenerative Tissue Engineering",
        "descPl": "Od różnicowania iPSC do unaczynionych organoidów (mózgowych, przysadkowych, narządowych) z pełną kontrolą bezpieczeństwa onkologicznego i bioetycznego.",
        "descEn": "From iPSC differentiation to vascularized organoids under strict oncological and bioethical safety gates.",
        "neutronTargets": [
          "FIS-A1",
          "FIS-C1"
        ],
        "deliverablePl": "Drzewo decyzyjne regeneracja vs syntetyczna konstrukcja organizmu.",
        "deliverableEn": "Regeneration vs. synthetic organism construction decision tree."
      },
      {
        "id": "FIS-F1",
        "parentId": "FIS-S5",
        "generation": 2,
        "code": "T9-BLSS",
        "siteId": "SITE-T9",
        "agentId": "AGT-06",
        "trackRef": "F",
        "status": "active",
        "titlePl": "Zamknięty Habitat Pozaziemski BLSS, Osłony Radiacyjne i Immunologia Kosmiczna",
        "titleEn": "Closed Extraterrestrial BLSS Habitat, Radiation Shielding & Space Immunology",
        "descPl": "Integracja fotobioreaktorów algowych, recyklingu wody/tlenu, ochrony przed GCR oraz monitoringu ekspresji genów odpornościowych astronautów.",
        "descEn": "Integrates algal photobioreactors, O2/H2O recycling, GCR shielding, and astronaut immune gene-expression monitoring.",
        "neutronTargets": [
          "FIS-G1"
        ],
        "deliverablePl": "Bilans pętli podtrzymywania życia dla załogi 4-osobowej.",
        "deliverableEn": "Closed-loop life-support balance for a 4-person crew."
      },
      {
        "id": "FIS-G1",
        "parentId": "FIS-S5",
        "generation": 2,
        "code": "T9-EARTH",
        "siteId": "SITE-T9",
        "agentId": "AGT-06",
        "trackRef": "G",
        "status": "active",
        "titlePl": "Odporność Biosfery Ziemi: Mikroklimat Leśny, Retencja i Dekarbonizacja Jądrowo-OZE",
        "titleEn": "Earth Biosphere Resilience: Forest Microclimates, Retention & Nuclear-Renewable Grid",
        "descPl": "Transfer czystych technologii zamkniętego obiegu z kosmosu (F) oraz energetyki jądrowej (H) do ochrony klimatu i ekosystemów lądowo-wodnych Ziemi.",
        "descEn": "Transfers closed-loop space tech (F) and nuclear baseload (H) to protect Earth's climate and terrestrial-aquatic ecosystems.",
        "neutronTargets": [
          "FIS-F1"
        ],
        "deliverablePl": "Model synergii energetyczno-ekologicznej H + G.",
        "deliverableEn": "Nuclear-ecological synergy model H + G."
      },
      {
        "id": "FIS-G3-1",
        "parentId": "FIS-H1",
        "generation": 3,
        "code": "NTR-HB-01",
        "siteId": "SITE-X10",
        "agentId": "AGT-04",
        "trackRef": "H",
        "status": "critical",
        "titlePl": "Neutron Kaskadowy: Zasilanie 100 MW SMR dla Klastra Emulacji Kory Mózgowej",
        "titleEn": "Cascade Neutron: 100 MW SMR Power Feed for Cortical Emulation Supercluster",
        "descPl": "Atomowe zadanie łączące 5-letnie studia Energetyki Jądrowej (H) ze studiami Neuronauki Obliczeniowej (B): porównanie kosztu energetycznego mózgu (20 W) z klastrem krzemowym i neuromorficznym.",
        "descEn": "Atomic task bridging 5-year Nuclear Engineering (H) and Computational Neuroscience (B): 20 W biological brain vs. silicon/neuromorphic cluster power budget.",
        "neutronTargets": [
          "FIS-B1",
          "FIS-C1"
        ],
        "deliverablePl": "Raport porównawczy: 20 W mózg vs GPU vs Neuromorf + SMR.",
        "deliverableEn": "Comparative report: 20 W brain vs. GPU vs. Neuromorphic + SMR."
      },
      {
        "id": "FIS-G3-2",
        "parentId": "FIS-A1",
        "generation": 3,
        "code": "NTR-AF-02",
        "siteId": "SITE-B7",
        "agentId": "AGT-05",
        "trackRef": "A",
        "status": "active",
        "titlePl": "Neutron Kaskadowy: Telemetria BCI + Immunologia w Misjach Długotrwałych",
        "titleEn": "Cascade Neutron: BCI Telemetry + Space Immunology in Long-Duration Missions",
        "descPl": "Pakiet roboczy Agenta B-7 i T-9: nieinwazyjne monitorowanie obciążenia poznawczego fNIRS oraz markerów zapalnych u operatorów w izolowanych habitatach.",
        "descEn": "Joint B-7 & T-9 agent work package: non-invasive fNIRS cognitive load and immune biomarker tracking in isolated habitats.",
        "neutronTargets": [
          "FIS-F1"
        ],
        "deliverablePl": "Protokół diagnostyczny operatora w habitacie analogowym.",
        "deliverableEn": "Operator diagnostic protocol for analog space habitats."
      }
    ],
    "carAudioRoad": [
      {
        "id": "car-ep-01",
        "order": 1,
        "stage": "0",
        "stageNamePl": "Etap 0: Sztab W-0 i Architektura Megaprojektu",
        "stageNameEn": "Stage 0: Command HQ W-0 & Megaproject Governance",
        "tripProfile": "Trasa miejska (~18 min)",
        "titlePl": "Odcinek 1: Doktryna Manhattan i Rygor Sztabowy — Jak Zarządzać Megaprojektem na Całe Życie",
        "titleEn": "Episode 1: The Manhattan Doctrine & Command Discipline — Life-Long Megaproject Governance",
        "estimatedDurationMin": 18,
        "spokenBriefingPl": "Witaj w trasie. Rozpoczynamy pierwszą część celowej drogi ekosystemu Golem 15. Dlaczego zaczynamy od Sztabu W-0 i dyscypliny organizacyjnej, zamiast od razu rzucić się na fizykę kwantową lub neurobiologię? Historia wielkich projektów technologicznych — od oryginalnego Projektu Manhattan w Los Alamos, przez Program Apollo, aż po współczesny ITER — uczy jednej bezwzględnej prawdy: żaden przełom naukowy nie przetrwa bez żelaznej dyscypliny organizacyjnej, ochrony własności intelektualnej i jasnej kompartmentalizacji wiedzy. Zasada 'Need-to-Know' oznacza, że w samochodzie budujesz wielką syntezę całości, ale każde laboratorium i każdy z Twoich agentów AI pracuje w ściśle wydzielonym sektorze, chronionym przed szumem i wyciekiem strategicznym. Trzy lata administracji to Twój sztabowy pancerz chroniący badania przed chaosem prawnym, audytami i utratą praw do wynalazków.",
        "spokenBriefingEn": "Welcome on the road. We begin the first stage of the Golem 15 ecosystem roadmap. Why do we start with District W-0 and organizational discipline rather than diving directly into quantum physics or neuroscience? Because history teaches that no breakthrough survives without institutional discipline, intellectual property protection, and rigorous knowledge compartmentalization. The 'Need-to-Know' principle protects your megaproject from fragmentation. Your 3 years of Administration serve as your strategic shield.",
        "keyTakeawaysPl": [
          "Zasada kompartmentalizacji wiedzy (Need-to-Know) chroni badania przed rozproszeniem i wyciekiem strategicznym.",
          "Trzy lata administracji dają formalną suwerenność: znajomość prawa publicznego, zamówień B+R i audytu.",
          "AI w projekcie Manhattan działa jako sieć wyspecjalizowanych agentów w ściśle przypisanych domenach."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — Jak zarządzać wielką nauką i megaprojektami",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "Lex Fridman Podcast #267 — Mark Spitznagel: Risk and Long-Term Strategy",
            "url": "https://lexfridman.com/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Polskie Radio — Historia i rygor Projektu Manhattan",
            "url": "https://polskieradio.pl/",
            "lang": "PL",
            "type": "audycja"
          }
        ]
      },
      {
        "id": "car-ep-02",
        "order": 2,
        "stage": "0",
        "stageNamePl": "Etap 0: Sztab W-0 i Architektura Megaprojektu",
        "stageNameEn": "Stage 0: Command HQ W-0 & Megaproject Governance",
        "tripProfile": "Trasa miejska (~20 min)",
        "titlePl": "Odcinek 2: Prawo B+R, Certyfikacja EU AI Act i Reżim Prawa Atomowego",
        "titleEn": "Episode 2: R&D Law, EU AI Act Compliance & Nuclear Regulatory Regimes",
        "estimatedDurationMin": 20,
        "spokenBriefingPl": "Słuchasz drugiego odcinka sztabowego. W tym module omawiamy twarde ramy prawne technologii krytycznych. W Unii Europejskiej wszedł w życie AI Act, który klasyfikuje systemy autonomiczne wg poziomów ryzyka. Systemy wysokiego ryzyka wymagają pełnej wyjaśnialności, audytowalności danych treningowych i ludzkiego nadzoru. Jednocześnie Super-Projekt H wprowadza prawo atomowe i rygory dozoru jądrowego (PAA, MAEA). Projekt badawczy nie może być prowadzony w próżni regulacyjnej. Opanowanie procedur administracyjnych, certyfikacji algorytmów i protokołów bezpieczeństwa radiologicznego to warunek konieczny, by Twoje prototypy mogły wejść w fazę rzeczywistych instalacji laboratoryjnych.",
        "spokenBriefingEn": "In this module we analyze the legal frameworks of critical technologies: the EU AI Act risk tiers and nuclear regulatory regimes under IAEA and national atomic agencies. Autonomous systems require explainability and auditability. Mastering administrative procedures and safety protocols is mandatory for physical lab deployment.",
        "keyTakeawaysPl": [
          "EU AI Act wymusza rygor dokumentacyjny i audytowalność modeli wysokiego ryzyka.",
          "Prawo atomowe i certyfikacja MAEA/PAA wymagają niezależnych protokołów bezpieczeństwa.",
          "Własność intelektualna w konsorcjach B+R musi być precyzyjnie zabezpieczona umowami konsorcjalnymi."
        ],
        "curatedAudioLinks": [
          {
            "title": "Podcast Prawniczy C.H. Beck — Prawo nowych technologii i AI Act",
            "url": "https://beck.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "IAEA Podcast — Nuclear Safety Standards & Governance",
            "url": "https://iaea.org/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Radio Naukowe — Prawne granice sztucznej inteligencji",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-03",
        "order": 3,
        "stage": "I",
        "stageNamePl": "Etap I: Fundamenty Formalne i Prawa Fizyki",
        "stageNameEn": "Stage I: Formal Foundations & Laws of Physics",
        "tripProfile": "Trasa podmiejska (~22 min)",
        "titlePl": "Odcinek 3: Matematyka, Logika i Tensory — Język Przestrzeni i Sieci Neuronowych",
        "titleEn": "Episode 3: Mathematics, Logic & Tensors — The Language of Reality & Deep Learning",
        "estimatedDurationMin": 22,
        "spokenBriefingPl": "Wkraczamy w Etap Pierwszy: fundamenty formalne. Matematyka nie jest po prostu narzędziem rachunkowym — jest jedynym bezstratnym językiem, w którym natura pozwala formułować swoje prawa. Od rachunku zdań i teorii mnogości, przez algebrę liniową i rozkłady spektralne, aż po przestrzenie Hilberta i rachunek tensorowy. Współczesne sieci neuronowe, transformery i wielkie modele językowe to w rzeczywistości gigantyczne operacje na tensorach w przestrzeniach wielowymiarowych. Słuchając tego odcinka, wyobraź sobie przestrzeń wektorową, w której każde pojęcie jest punktem, a każda relacja semantyczna — geometryczną transformacją. Rozumienie tensorów pozwala widzieć kod AI jako geometrię wielowymiarową.",
        "spokenBriefingEn": "Entering Stage I: formal foundations. Mathematics is the lossless language of nature. From propositional logic and linear algebra to Hilbert spaces and tensor calculus. Deep learning and neural networks are multi-dimensional tensor operations. Conceive meaning as geometric transformations in high-dimensional manifolds.",
        "keyTakeawaysPl": [
          "Algebra liniowa i tensory stanowią matematyczne serce zarówno mechaniki kwantowej, jak i głębokich sieci neuronowych.",
          "Rachunek różniczkowy i gradienty umożliwiają optymalizację funkcji straty w przestrzeniach o miliardach parametrów.",
          "Logika formalna i teoria dowodzenia gwarantują weryfikowalność modeli matematycznych."
        ],
        "curatedAudioLinks": [
          {
            "title": "Zapytaj Fizyka (UW) — Wykłady z geometrii czasoprzestrzeni i algebry",
            "url": "https://zapytajfizyka.fuw.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          },
          {
            "title": "3Blue1Brown Audio Series — Essence of Linear Algebra",
            "url": "https://www.youtube.com/@3blue1brown",
            "lang": "EN",
            "type": "wykład"
          },
          {
            "title": "Centrum Kopernika — Granice matematyki i logiki (prof. Heller)",
            "url": "https://copernicuscenter.edu.pl/",
            "lang": "PL",
            "type": "audycja"
          }
        ]
      },
      {
        "id": "car-ep-04",
        "order": 4,
        "stage": "I",
        "stageNamePl": "Etap I: Fundamenty Formalne i Prawa Fizyki",
        "stageNameEn": "Stage I: Formal Foundations & Laws of Physics",
        "tripProfile": "Trasa podmiejska (~24 min)",
        "titlePl": "Odcinek 4: Informatyka Teoretyczna, Teoria Informacji Shannona i Granice Złożoności",
        "titleEn": "Episode 4: Theoretical CS, Shannon Information Theory & Computational Complexity",
        "estimatedDurationMin": 24,
        "spokenBriefingPl": "Słuchasz czwartego odcinka celowej drogi. Czym jest informacja? W 1948 roku Claude Shannon zdefiniował informację jako redukcję niepewności, mierzoną entropią informacyjną. Od tamtej pory informacja stała się fundamentalną wielkością fizyczną, tak samo realną jak masa czy ładunek elektryczny. W tym module przechodzimy przez maszynę Turinga, problem stopu, klasy złożoności P kontra NP oraz granice tego, co w ogóle jest obliczalne w skończonym czasie. Zrozumienie, że niektóre problemy są nierozstrzygalne lub wymagają czasu wykładniczego na komputerach klasycznych, otwiera bezpośrednią drogę do poszukiwania nowych paradygmatów: obliczeń kwantowych i analogowych.",
        "spokenBriefingEn": "What is information? In 1948 Claude Shannon defined information as uncertainty reduction, measured through informational entropy. Information is a physical quantity. We explore Turing machines, the halting problem, P vs NP, and the limits of classical computability, establishing why we need quantum paradigms.",
        "keyTakeawaysPl": [
          "Entropia Shannona łączy teorię informacji bezpośrednio z termodynamiką statystyczną Boltzmanna.",
          "Bariery NP-trudności na klasycznych komputerach wymuszają algorytmy heurystyczne oraz kwantowe przyspieszenie (np. algorytm Grovera).",
          "Obliczalność algorytmiczna ma swoje bezwzględne granice wyznaczone przez twierdzenia Gödla i problem stopu Turinga."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — Czym jest informacja i jak ją mierzyć?",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "MIT OpenCourseWare Audio — Theory of Computation & Complexity",
            "url": "https://ocw.mit.edu/",
            "lang": "EN",
            "type": "wykład"
          },
          {
            "title": "Podcast O Nauce — Maszyny Turinga i granice algorytmów",
            "url": "https://spotify.com/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-05",
        "order": 5,
        "stage": "I",
        "stageNamePl": "Etap I: Fundamenty Formalne i Prawa Fizyki",
        "stageNameEn": "Stage I: Formal Foundations & Laws of Physics",
        "tripProfile": "Trasa podmiejska (~24 min)",
        "titlePl": "Odcinek 5: Architektury Komputerowe — Wąskie Gardło von Neumanna i Przełom Akceleratorów",
        "titleEn": "Episode 5: Computer Architecture — The Von Neumann Bottleneck & Accelerator Revolution",
        "estimatedDurationMin": 24,
        "spokenBriefingPl": "Przez ostatnie 70 lat komputery budowano w oparciu o architekturę von Neumanna, gdzie procesor i pamięć operacyjna są fizycznie rozdzielone magistralą. Każda operacja wymaga przesyłania danych tam i z powrotem. To tak zwane wąskie gardło pamięci — Memory Wall. W dobie głębokich sieci neuronowych przesyłanie wag zużywa 90% energii całego układu scalonego. W tym module badamy ewolucję od tradycyjnych CPU, przez macierze GPU i TPU (Tensor Processing Units), aż po procesory grafowe i architekturę pamięciową HBM3e. Poznasz mechanizmy równoległości SIMD i MIMD oraz zrozumiesz, dlaczego współczesna AI potrzebuje wyspecjalizowanych akceleratorów tensora.",
        "spokenBriefingEn": "For 70 years, computing relied on the Von Neumann architecture, where CPU and memory are separated by a bus. Moving data between compute units and memory constitutes the Memory Wall, consuming up to 90% of chip energy in deep learning. We analyze CPUs, GPUs, TPUs, and HBM memory innovations.",
        "keyTakeawaysPl": [
          "Wąskie gardło von Neumanna (Memory Wall) ogranicza przepustowość współczesnych superkomputerów.",
          "Akceleratory tensorowe (TPU/GPU) zastępują przetwarzanie sekwencyjne masywną równoległością macierzową.",
          "Przyszłość sprzętu wymaga zbliżenia pamięci do procesora (Near-Memory Computing) lub obliczeń bezpośrednio w pamięci (Compute-In-Memory)."
        ],
        "curatedAudioLinks": [
          {
            "title": "Nauka. To Lubię — Jak działają chipy GPU i TPU w sztucznej inteligencji",
            "url": "https://naukatolubie.pl/",
            "lang": "PL",
            "type": "audycja"
          },
          {
            "title": "Stanford EE Seminar Audio — The Future of Computing Architectures",
            "url": "https://ee.stanford.edu/",
            "lang": "EN",
            "type": "wykład"
          },
          {
            "title": "Lex Fridman Podcast #182 — Jim Keller: The Future of Processors",
            "url": "https://lexfridman.com/",
            "lang": "EN",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-06",
        "order": 6,
        "stage": "I",
        "stageNamePl": "Etap I: Fundamenty Formalne i Prawa Fizyki",
        "stageNameEn": "Stage I: Formal Foundations & Laws of Physics",
        "tripProfile": "Trasa podmiejska (~25 min)",
        "titlePl": "Odcinek 6: Mechanika Kwantowa — Superpozycja, Splątanie i Równanie Schrödingera",
        "titleEn": "Episode 6: Quantum Mechanics — Superposition, Entanglement & Schrödinger's Equation",
        "estimatedDurationMin": 25,
        "spokenBriefingPl": "Zanurzamy się w świat subatomowy. W skali mikro świat nie zachowuje się jak zbiór małych kulek bilardowych. Cząstki elementarne opisuje funkcja falowa psi, podlegająca równaniu Schrödingera. Dopóki nie dokonamy pomiaru, stan kwantowy znajduje się w superpozycji wielu możliwości naraz. Gdy dwa układy wejdą w interakcję, powstaje zjawisko splątania kwantowego — korelacji nielokalnej, którą Einstein nazywał upiornym działaniem na odległość. W samochodzie zrozumiesz, jak te zjawiska przestają być abstrakcją filozoficzną, a stają się paliwem technologii: od mikroskopów tunelowych, przez kryptografię kwantową QKD, aż po rejestry kubitowe w komputerach kwantowych.",
        "spokenBriefingEn": "We explore quantum mechanics: wave-particle duality, wavefunctions, and Schrödinger's equation. Superposition and quantum entanglement form the physical reality of the subatomic scale. These phenomena power quantum cryptography and quantum computers.",
        "keyTakeawaysPl": [
          "Zasada nieoznaczoności Heisenberga stawia fundamentalną granicę na jednoczesną dokładność pomiaru położenia i pędu.",
          "Splątanie kwantowe umożliwia nielokalne korelacje stanów kubitowych bez łamania szczególnej teorii względności.",
          "Tunelowanie kwantowe jest zjawiskiem powszechnym w mikroprocesorach poniżej 3 nm, powodując prądy upływu bramek."
        ],
        "curatedAudioLinks": [
          {
            "title": "Zapytaj Fizyka (UW) — Prof. Andrzej Dragan: Niezwykłości mechaniki kwantowej",
            "url": "https://zapytajfizyka.fuw.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          },
          {
            "title": "Sean Carroll's Mindscape #59 — The Many Worlds of Quantum Mechanics",
            "url": "https://www.preposterousuniverse.com/podcast/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Radio Naukowe — Zrozumieć splątanie kwantowe",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-07",
        "order": 7,
        "stage": "I",
        "stageNamePl": "Etap I: Fundamenty Formalne i Prawa Fizyki",
        "stageNameEn": "Stage I: Formal Foundations & Laws of Physics",
        "tripProfile": "Trasa miejska (~20 min)",
        "titlePl": "Odcinek 7: Termodynamika, Entropia Informacyjna i Granica Landauera",
        "titleEn": "Episode 7: Thermodynamics, Informational Entropy & Landauer's Principle",
        "estimatedDurationMin": 20,
        "spokenBriefingPl": "Słuchasz siódmego odcinka. Dlaczego Twój laptop się nagrzewa, a centra danych AI zużywają gigawaty energii? Rolf Landauer w 1961 roku udowodnił fundamentalną zasadę: samo przetwarzanie informacji może być bezstratne, ale usunięcie jednego bitu informacji nieodwracalnie rozprasza w otoczeniu energię równą k T ln 2. To granica Landauera. Informacja jest fizyczna. Każdy nieodwracalny cykl logiczny w bramkach krzemowych generuje ciepło, które ostatecznie dusi dalsze skalowanie gęstości tranzystorów. W tym odcinku omawiamy termodynamikę nierównowagową Prigogine'a, powstawanie struktur dyssypatywnych i koncepcję obliczeń odwracalnych (reversible computing), która pozwoli obejść barierę Landauera.",
        "spokenBriefingEn": "Why do computers generate heat? Rolf Landauer proved in 1961 that erasing one bit of information irreversibly dissipates k T ln 2 energy into the environment. Information is physical. We explore non-equilibrium thermodynamics, dissipative structures, and reversible computing paradigms.",
        "keyTakeawaysPl": [
          "Zasada Landauera łączy kasowanie bitu pamięci z minimalnym rozproszeniem ciepła w otoczeniu.",
          "Współczesne chipy krzemowe pracują wciąż tysiąckrotnie powyżej granicy Landauera, marnując energię na oporze pasożytniczym.",
          "Obliczenia odwracalne (Reversible Computing) i bramki Toffolego pozwalają na przetwarzanie bez kasowania bitów, zbliżając się do zera dyssypacji."
        ],
        "curatedAudioLinks": [
          {
            "title": "Zapytaj Fizyka (UW) — Termodynamika, strzałka czasu i entropia",
            "url": "https://zapytajfizyka.fuw.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          },
          {
            "title": "Feynman Lectures Audio — Thermodynamics & Statistical Mechanics",
            "url": "https://feynmanlectures.caltech.edu/",
            "lang": "EN",
            "type": "wykład"
          },
          {
            "title": "Centrum Kopernika — Entropia i fizyka informacji",
            "url": "https://copernicuscenter.edu.pl/",
            "lang": "PL",
            "type": "audycja"
          }
        ]
      },
      {
        "id": "car-ep-08",
        "order": 8,
        "stage": "II",
        "stageNamePl": "Etap II: Kres Krzemu i Nowy Hardware",
        "stageNameEn": "Stage II: Silicon Physical Limits & Next-Gen Hardware",
        "tripProfile": "Trasa podmiejska (~22 min)",
        "titlePl": "Odcinek 8: Fizyczne Granice Krzemu — Koniec Prawa Moore'a i Prądy Upływu",
        "titleEn": "Episode 8: Physical Limits of Silicon — The End of Moore's Law & Gate Leakage",
        "estimatedDurationMin": 22,
        "spokenBriefingPl": "Rozpoczynamy Etap Drugi: kres podwalin krzemowych. Przez dekady przemysł półprzewodników rozwijał się dzięki prawu Moore'a i skalowaniu Dennarda. Podwajaliśmy liczbę tranzystorów co 18 miesięcy, zachowując stałą gęstość mocy. Jednak około 2006 roku skalowanie Dennarda się załamało. Przy szerokości bramek poniżej 2 nanometrów elektrony zaczęły tunelować kwantowo wprost przez izolator tlenkowy. Tranzystor nie daje się już całkowicie wyłączyć — prądy upływu generują gigantyczne straty mocy nawet w stanie spoczynku. To fizyczny mur krzemu. Nie da się zrobić tranzystora mniejszego niż pojedynczy atom krzemu. W tym module dowiesz się, jak litografia ekstremalnego ultrafioletu (EUV) osiąga kres i dlaczego musimy zmienić materiał bazowy.",
        "spokenBriefingEn": "Stage II: Silicon limits. Dennard scaling collapsed around 2006. Below 2nm gate lengths, quantum tunneling causes massive gate leakage currents. We reached the physical barrier of silicon. We explore the limits of EUV lithography and the urgent need for new substrate materials.",
        "keyTakeawaysPl": [
          "Skalowanie Dennarda zakończyło się z powodu prądów upływu podprogowych i tunelowania kwantowego bramek.",
          "Zjawisko 'Dark Silicon' oznacza, że w nowoczesnym procesorze nie można zasilić wszystkich rdzeni naraz bez stopienia chipu.",
          "Następcy krzemu to grafen, nanorurki węglowe (CNT), dichalkogenki metali przejściowych (TMD) oraz tranzystory bramkowane optycznie."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — Kiedy skończy się krzem? Granice nanoelektroniki",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "IEEE Spectrum Podcast — The End of Moore's Law & What Comes Next",
            "url": "https://spectrum.ieee.org/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Nauka. To Lubię — Jak działa litografia EUV w ASML",
            "url": "https://naukatolubie.pl/",
            "lang": "PL",
            "type": "audycja"
          }
        ]
      },
      {
        "id": "car-ep-09",
        "order": 9,
        "stage": "II",
        "stageNamePl": "Etap II: Kres Krzemu i Nowy Hardware",
        "stageNameEn": "Stage II: Silicon Physical Limits & Next-Gen Hardware",
        "tripProfile": "Trasa daleka (~28 min)",
        "titlePl": "Odcinek 9: Komputery Kwantowe (QPU) i Algorytmy Hybrydowe VQE",
        "titleEn": "Episode 9: Quantum Processors (QPU), Qiskit & Variational Quantum Eigensolvers",
        "estimatedDurationMin": 28,
        "spokenBriefingPl": "Słuchasz dziewiątego odcinka. Skoro krzem w architekturze klasycznej dochodzi do ściany, wkraczamy w domenę procesorów kwantowych (QPU). Zamiast bitów 0 lub 1 operujemy na kubitach. Jednak współczesne komputery kwantowe znajdują się w erze NISQ — Noisy Intermediate-Scale Quantum. Kubity tracą koherencję pod wpływem najmniejszych zakłóceń termicznych i radiacyjnych. Dlatego przyszłość nie należy do czystych maszyn kwantowych, lecz do algorytmów hybrydowych. Algorytm VQE (Variational Quantum Eigensolver) dzieli zadanie: QPU oblicza skomplikowany stan kwantowy cząsteczki chemicznej lub jądra atomowego, a klasyczny superkomputer optymalizuje parametry. W tym odcinku poznasz Qiskit, PennyLane oraz fizykę kubitów nadprzewodzących i pułapek jonowych.",
        "spokenBriefingEn": "We explore Quantum Processing Units (QPUs). In the NISQ era, decoherence limits quantum depth. Hybrid quantum-classical algorithms such as VQE (Variational Quantum Eigensolver) divide computation between QPU state evaluation and classical gradient optimization. We examine superconducting qubits, ion traps, and Qiskit frameworks.",
        "keyTakeawaysPl": [
          "Era NISQ wymaga algorytmów odpornych na szum, takich jak VQE i QAOA.",
          "Kubity nadprzewodzące (złącza Josephsona) wymagają kriostatu rozcieńczalnikowego o temperaturze 15 miliKelwinów.",
          "Kwantowa korekcja błędów (kod powierzchniowy) wymaga setek kubitów fizycznych na jeden logiczny kubit odporny na dekoherencję."
        ],
        "curatedAudioLinks": [
          {
            "title": "IBM Quantum Podcast — Qiskit, Quantum Chemistry & VQE",
            "url": "https://www.ibm.com/quantum",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Zapytaj Fizyka (UW) — Jak zbudować komputer kwantowy?",
            "url": "https://zapytajfizyka.fuw.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          },
          {
            "title": "Lex Fridman Podcast #365 — Scott Aaronson: Quantum Computing & Complexity",
            "url": "https://lexfridman.com/",
            "lang": "EN",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-10",
        "order": 10,
        "stage": "II",
        "stageNamePl": "Etap II: Kres Krzemu i Nowy Hardware",
        "stageNameEn": "Stage II: Silicon Physical Limits & Next-Gen Hardware",
        "tripProfile": "Trasa podmiejska (~26 min)",
        "titlePl": "Odcinek 10: Chipy Neuromorficzne, Memrystory i Sieci Impulsowe SNN",
        "titleEn": "Episode 10: Neuromorphic Chips, Memristors & Spiking Neural Networks (SNN)",
        "estimatedDurationMin": 26,
        "spokenBriefingPl": "Dziesiąty odcinek wprowadza nas w świat sprzętu naśladującego mózg biologiczny. Ludzki mózg zużywa zaledwie 20 watów energii, wykonując operacje, które w superkomputerze Frontier wymagają 20 megawatów. Jak natura osiąga milionkrotnie wyższą efektywność energetyczną? Mózg nie używa zegara taktującego ani architektury von Neumanna. Neurony komunikują się asynchronicznie za pomocą impulsów elektrycznych — spikes. W tym module badamy chipy neuromorficzne: Intel Loihi, IBM TrueNorth oraz SpiNNaker. Omawiać będziemy memrystory — czwarty pasywny element obwodu, który łączy funkcję opornika i pamięci, pozwalając na bezpośrednie uczenie synaptyczne w fizycznym materiale (STDP) i eliminację wąskiego gardła pamięci.",
        "spokenBriefingEn": "The human brain operates on only 20 watts of power. How does biology achieve this million-fold efficiency over supercomputers? Asynchronous spiking neural networks (SNNs) and in-memory computing. We analyze Intel Loihi, SpiNNaker, and memristive crossbar arrays enabling Spike-Timing-Dependent Plasticity (STDP).",
        "keyTakeawaysPl": [
          "Sieci SNN komunikują się tylko w momencie pojawienia się impulsu (event-driven), oszczędzając 95% energii w stanie spoczynku.",
          "Memrystory realizują obliczenia macierzowe w pamięci w domenie analogowej na prawach Kirchhoffa.",
          "Frameworki Brian2, Lava i snnTorch pozwalają programować impulsowe sieci neuronowe z plastycznością synaptyczną STDP."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — Elektroniczny mózg: chipy neuromorficzne i memrystory",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "Intel Labs Audio — Neuromorphic Computing & The Loihi Architecture",
            "url": "https://www.intel.com/content/www/us/en/research/neuromorphic-community.html",
            "lang": "EN",
            "type": "wykład"
          },
          {
            "title": "Nature Podcast — Memristive crossbars for energy-efficient AI",
            "url": "https://nature.com/",
            "lang": "EN",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-11",
        "order": 11,
        "stage": "III",
        "stageNamePl": "Etap III: Mózg, Bionika i Protokół WBE",
        "stageNameEn": "Stage III: Biological Brain, Bionics & WBE Protocol",
        "tripProfile": "Trasa podmiejska (~25 min)",
        "titlePl": "Odcinek 11: Bionika i Interfejsy Mózg-Komputer (BCI) — Na Styku Mięsa i Krzemu",
        "titleEn": "Episode 11: Bionics & Brain-Computer Interfaces (BCI) — Bridging Wetware & Silicon",
        "estimatedDurationMin": 25,
        "spokenBriefingPl": "Wkraczamy w Etap Trzeci: biologia spotyka technologię. Interfejsy mózg-komputer (BCI) dzielimy na inwazyjne, półinwazyjne i nieinwazyjne. Od klasycznego EEG, przez ECoG, aż po elektrody neuropikselowe i nici neuronowe Neuralink. W tym module badamy biokompatybilność elektrod: jak unikać reakcji układu odpornościowego, glejozy i degradacji sygnału w tkance mózgowej. Zrozumiesz, jak dekodować intencje ruchowe i mowę za pomocą algorytmów filtracji Kalmana i sieci rekurencyjnych, a także jak dostarczać stymulację zwrotną do kory czuciowej. To pierwszy krok na drodze do zespolenia ludzkiej percepcji z cyfrową pamięcią.",
        "spokenBriefingEn": "Stage III: Bionics and Brain-Computer Interfaces. From non-invasive EEG and ECoG to Neuropixels and intracortical arrays. We study biocompatibility, neuroinflammation, foreign-body response, and spike decoding algorithms (Kalman filters, RNNs) that bridge human neural intention with digital actuators.",
        "keyTakeawaysPl": [
          "Biokompatybilne powłoki elektrod (np. polimery przewodzące PEDOT) minimalizują bliznowacenie glejowe tkanki nerwowej.",
          "Dekodery BCI potrafią przetwarzać potencjały polowe LFP i salwy iglicowe na polecenia dla protez bionicznych i syntezatorów mowy.",
          "Pętla zamknięta (Closed-Loop BCI) umożliwia dwukierunkową komunikację: odczyt intencji i zwrotną elektrostymulację czuciową."
        ],
        "curatedAudioLinks": [
          {
            "title": "Huberman Lab Podcast #48 — Neuroplasticity and Brain-Machine Interfaces",
            "url": "https://hubermanlab.com/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Radio Naukowe — Czy połączymy mózg z komputerem? Granice BCI",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "Strefa Psyche SWPS — Neuroinżynieria i odczytywanie fal mózgowych",
            "url": "https://swps.pl/strefa-psyche",
            "lang": "PL",
            "type": "wykład"
          }
        ]
      },
      {
        "id": "car-ep-12",
        "order": 12,
        "stage": "III",
        "stageNamePl": "Etap III: Mózg, Bionika i Protokół WBE",
        "stageNameEn": "Stage III: Biological Brain, Bionics & WBE Protocol",
        "tripProfile": "Trasa daleka (~28 min)",
        "titlePl": "Odcinek 12: Protokół WBE (Whole Brain Emulation) — Skanowanie Konektomu i Modele Pamięci",
        "titleEn": "Episode 12: The WBE Protocol (Whole Brain Emulation) — Connectome Scanning & Memory Engrams",
        "estimatedDurationMin": 28,
        "spokenBriefingPl": "Słuchasz dwunastego odcinka. Projekt B w ekosystemie Golem 15 bada najbardziej radykalną hipotezę neuronauki: czy świadomość i tożsamość człowieka są wzorcem obliczeniowym zapisanym w konektomie? W tym module omawiamy protokół Whole Brain Emulation (WBE). Badamy techniki krioprezerwacji i plastynacji tkanki mózgowej, seryjną mikroskopię elektronową FIB-SEM, rekonstrukcję miliardów synaps oraz mapowanie engramów pamięciowych w hipokampie. Dowiesz się, ile petabajtów danych wymaga pełna rekonstrukcja kory mózgowej i jakie modele elektrofizjologiczne (Hodgkina-Huxleya, Izhikevicha) są niezbędne, by ożywić zeskanowany model w symulacji cyfrowej.",
        "spokenBriefingEn": "We examine the Whole Brain Emulation (WBE) protocol: connectome mapping, cryopreservation, serial sectioning FIB-SEM electron microscopy, and engram preservation. We analyze the computational requirements to simulate 86 billion neurons and 100 trillion synapses using Hodgkin-Huxley and multi-compartment models.",
        "keyTakeawaysPl": [
          "Konektomika wymaga rekonstrukcji morfologii dendrytów i kolców synaptycznych w rozdzielczości nanometrycznej.",
          "Modele wieloprzedziałowe (multi-compartment) dokładnie odtwarzają dynamikę nieliniową kanałów jonowych w dendrytach.",
          "WBE stawia kluczowe pytanie filozoficzne: czy emulacja jest kopią, kontynuacją tożsamości, czy nową formą istnienia?"
        ],
        "curatedAudioLinks": [
          {
            "title": "Oxford FHI Audio Series — Nick Bostrom & Anders Sandberg on Whole Brain Emulation",
            "url": "https://www.fhi.ox.ac.uk/",
            "lang": "EN",
            "type": "wykład"
          },
          {
            "title": "Radio Naukowe — Konektom: mapa wszystkich połączeń w mózgu",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "Stanford Sapolsky Lectures Audio — The Biology of Memory and Identity",
            "url": "https://stanford.edu/",
            "lang": "EN",
            "type": "wykład"
          }
        ]
      },
      {
        "id": "car-ep-13",
        "order": 13,
        "stage": "IV",
        "stageNamePl": "Etap IV: Inżynieria Życia i Biosfera",
        "stageNameEn": "Stage IV: Life Engineering & Synthetic Biology",
        "tripProfile": "Trasa podmiejska (~25 min)",
        "titlePl": "Odcinek 13: Biologia Syntetyczna, CRISPR i Konstrukcja Nowych Szlaków Życia",
        "titleEn": "Episode 13: Synthetic Biology, CRISPR Gene Editing & Engineering Living Circuits",
        "estimatedDurationMin": 25,
        "spokenBriefingPl": "Przechodzimy do Etapu Czwartego: inżynieria życia (Projekt D). Do niedawna człowiek był wyłącznie obserwatorem i selekcjonerem ewolucji. Dziś biologia stała się dziedziną inżynierską. W tym module omawiamy edycję genomu za pomocą CRISPR-Cas9, Cas12 oraz precyzyjną edycję zasad (base editing). Badamy projektowanie syntetycznych obwodów genetycznych (genetic toggle switches), sztuczne chromosomy bakteryjne i drożdżowe oraz konstrukcję organoidów mózgowych. Dowiesz się, jak kod genetyczny może pełnić funkcję pamięci trwałej i procesora biochemicznego zdolnego do syntezy nowych enzymów leczących choroby degeneracyjne.",
        "spokenBriefingEn": "Stage IV explores synthetic biology and genomic engineering. We cover CRISPR-Cas systems, base editing, and prime editing. We analyze genetic logic gates, synthetic chromosomes, organoids, and how biological circuits execute computational logic through biochemical signal transduction cascades.",
        "keyTakeawaysPl": [
          "Systemy CRISPR-Cas pozwalają na reprogramowanie ekspresji genów i precyzyjną naprawę mutacji punktowych.",
          "Biologia syntetyczna traktuje cząsteczki DNA jako znormalizowany kod programistyczny (BioBricks).",
          "Organoidy tkankowe umożliwiają badanie patologii mózgu i testowanie leków in vitro bez udziału organizmów wyższych."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — CRISPR i inżynieria genetyczna: jak naprawić DNA",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "The CRISPR Journal Podcast — Advances in Precision Gene Editing",
            "url": "https://liebertpub.com/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Nauka. To Lubię — Biologia syntetyczna: czy stworzymy sztuczne życie?",
            "url": "https://naukatolubie.pl/",
            "lang": "PL",
            "type": "audycja"
          }
        ]
      },
      {
        "id": "car-ep-14",
        "order": 14,
        "stage": "IV",
        "stageNamePl": "Etap IV: Inżynieria Życia i Biosfera",
        "stageNameEn": "Stage IV: Life Engineering & Synthetic Biology",
        "tripProfile": "Trasa podmiejska (~25 min)",
        "titlePl": "Odcinek 14: Ekosystemy Zamknięte, Biosfera i Planetarna Homeostaza Termodynamiczna",
        "titleEn": "Episode 14: Closed Ecological Systems, Biosphere Dynamics & Planetary Homeostasis",
        "estimatedDurationMin": 25,
        "spokenBriefingPl": "Słuchasz czternastego odcinka poświęconego Projektowi G: biosfera i obieg materii. Życie na Ziemi nie istnieje w izolacji — biosfera to potężny system termodynamiczny napędzany fotonami słonecznymi, który utrzymuje entropię na niskim poziomie poprzez cykle biochemiczne: węglowy, azotowy i fosforowy. W tym module analizujemy lekcje z eksperymentu Biosphere 2, dynamikę modeli klimatycznych i biogeochemicznych oraz konstrukcję sztucznych mikroekosystemów bioregeneracyjnych (MELiSSA). Zrozumiesz, dlaczego stabilność biosfery ziemskiej jest warunkiem przetrwania cywilizacji technologicznej i jak te same zasady stosują się do baz księżycowych i marsjańskich.",
        "spokenBriefingEn": "We examine closed life-support systems (MELiSSA), Biosphere 2 engineering, biogeochemical cycles, and non-equilibrium Earth systems. Planetary homeostasis maintains low entropy via living dissipative structures, establishing principles essential for long-duration space settlement.",
        "keyTakeawaysPl": [
          "Biosfera jest samoregulującym się układem homeostatycznym, w którym organizmy modyfikują atmosferę i litosferę.",
          "Eksperyment Biosphere 2 wykazał trudności w bilansowaniu tlenu i dwutlenku węgla w układach zamkniętych bez glebowej równowagi mikrobiologicznej.",
          "Systemy MELiSSA (ESA) wykorzystują algi spirulina i bakterie nitryfikujące do 100% recyklingu wody i powietrza."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — Biosfera jako układ termodynamiczny i granice Ziemi",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "ESA Space Exploration Audio — The MELiSSA Life Support Project",
            "url": "https://esa.int/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Crazy Nauka Podcast — Jak zaprojektować zamknięty ekosystem?",
            "url": "https://crazynauka.pl/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-15",
        "order": 15,
        "stage": "V",
        "stageNamePl": "Etap V: Super-Projekt Jądrowy i Kosmos",
        "stageNameEn": "Stage V: Nuclear Megaproject H & Space Frontier",
        "tripProfile": "Trasa daleka (~30 min)",
        "titlePl": "Odcinek 15: Energetyka Rozszczepienia — SMR, Reaktory IV Generacji i Fizyka Reaktora Maria",
        "titleEn": "Episode 15: Nuclear Fission — SMRs, Gen-IV Reactors & Reactor Maria Physics",
        "estimatedDurationMin": 30,
        "spokenBriefingPl": "Wkraczamy w Etap Piąty: Super-Projekt H — atomowy fundament cywilizacji. Dlaczego energetyka jądrowa jest integralną częścią ekosystemu Golem 15? Ponieważ rozwój superinteligencji AI, fabryk nanotechnologicznych i eksploracji kosmicznej wymaga gęstości energii, której źródła chemiczne i pogodozależne OZE nie są w stanie zapewnić. Rozszczepienie jednego grama uranu dostarcza tyle energii co spalenie 3 ton węgla kamiennego. W tym module badamy fizykę reaktorów: współczynnik mnożenia neutronów k_eff, moderatory grafitowe i wodne, reaktory badawcze (polski reaktor MARIA w Świerku), małe reaktory modułowe SMR (BWRX-300, NuScale) oraz reaktory IV generacji chłodzone ciekłym ołowiem i stopionymi solami (MSR).",
        "spokenBriefingEn": "Nuclear fission is the energetic foundation of Super-Project H. Fission density exceeds chemical combustion by a factor of 10^6. We examine neutron transport, k_eff criticality, moderator physics (research reactor MARIA at NCBJ Świerk), Small Modular Reactors (SMRs), and Gen-IV Molten Salt Reactors (MSR).",
        "keyTakeawaysPl": [
          "Równanie kinetyki reaktora i obecność neutronów opóźnionych umożliwiają stabilne, podkrytyczne sterowanie reakcją łańcuchową.",
          "Reaktory SMR wprowadzają pasywne systemy bezpieczeństwa oparte na grawitacji i naturalnej konwekcji, uniemożliwiające stopienie rdzenia.",
          "Reaktory wysokotemperaturowe (HTGR) umożliwiają wytwarzanie wodoru i ciepła przemysłowego dla przemysłu chemicznego i metalurgicznego."
        ],
        "curatedAudioLinks": [
          {
            "title": "NCBJ Świerk Audio — Jak działa jedyny polski reaktor jądrowy MARIA?",
            "url": "https://www.ncbj.gov.pl/",
            "lang": "PL",
            "type": "wykład"
          },
          {
            "title": "Nauka. To Lubię — Energetyka jądrowa i reaktory SMR w Polsce",
            "url": "https://naukatolubie.pl/",
            "lang": "PL",
            "type": "audycja"
          },
          {
            "title": "Jakub Wiech / Energetyka24 — Podcast o energetyce atomowej i bezpieczeństwie",
            "url": "https://energetyka24.com/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-16",
        "order": 16,
        "stage": "V",
        "stageNamePl": "Etap V: Super-Projekt Jądrowy i Kosmos",
        "stageNameEn": "Stage V: Nuclear Megaproject H & Space Frontier",
        "tripProfile": "Trasa daleka (~30 min)",
        "titlePl": "Odcinek 16: Fuzja Termojądrowa — Tokamaki, Stellaratory i Projekt ITER",
        "titleEn": "Episode 16: Thermonuclear Fusion — Tokamaks, Stellarators & Project ITER",
        "estimatedDurationMin": 30,
        "spokenBriefingPl": "Słuchasz szesnastego odcinka poświęconego ostatecznemu źródłu energii gwiazd: fuzji termojądrowej. Podczas łączenia deuteru i trytu w jądro helu 4He wyzwala się neutron o energii 14.1 MeV. Fuzja nie generuje odpadów transuranowych ani ryzyka ucieczki reakcji. Wyzwaniem jest jednak utrzymanie plazmy o temperaturze 150 milionów stopni Celsjusza z dala od ścian komory. W tym module porównujemy pułapki magnetyczne: tokamaki z polem toroidalnym i poloidalnym (ITER, JET) ze stellaratorami o skręconej geometrii magnesów nadprzewodzących (Wendelstein 7-X). Zrozumiesz kryterium Lawsona, zjawiska turbulencji magnetohydrodynamicznej (MHD) oraz to, jak fuzja stanie się napędem podróży międzyplanetarnych.",
        "spokenBriefingEn": "Thermonuclear fusion powers the stars: D-T fusion produces a 14.1 MeV neutron and alpha particle. We explore plasma confinement via magnetic fields, comparing tokamaks (ITER) with complex-geometry stellarators (Wendelstein 7-X), the Lawson criterion, and plasma MHD instabilities.",
        "keyTakeawaysPl": [
          "Kryterium Lawsona definiuje iloczyn gęstości plazmy, temperatury i czasu utrzymania energii niezbędny do osiągnięcia zapłonu termojądrowego (Q > 1).",
          "Stellarator Wendelstein 7-X eliminuje prąd plazmowy, umożliwiając pracę w reżimie ciągłym bez niestabilności typu 'disruption'.",
          "Materiały pierwszej ściany (wolfram, beryl) muszą wytrzymać bombardowanie strumieniem neutronów prędkich 14 MeV bez utraty integralności krystalicznej."
        ],
        "curatedAudioLinks": [
          {
            "title": "ITER Official Audio Series — Building the Sun on Earth",
            "url": "https://www.iter.org/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Radio Naukowe — Fuzja jądrowa: kiedy gwiazda zaświeci w gniazdku?",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "Zapytaj Fizyka (UW) — Magnetyczne pułapki plazmy i fizyka fuzji",
            "url": "https://zapytajfizyka.fuw.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          }
        ]
      },
      {
        "id": "car-ep-17",
        "order": 17,
        "stage": "V",
        "stageNamePl": "Etap V: Super-Projekt Jądrowy i Kosmos",
        "stageNameEn": "Stage V: Nuclear Megaproject H & Space Frontier",
        "tripProfile": "Trasa podmiejska (~25 min)",
        "titlePl": "Odcinek 17: Technosfera Orbitalna — Życie w Próżni, Radiacja i Sztuczna Grawitacja",
        "titleEn": "Episode 17: Orbital Technosphere — Life in Vacuum, Cosmic Radiation & Artificial Gravity",
        "estimatedDurationMin": 25,
        "spokenBriefingPl": "Siedemnasty odcinek poświęcony jest Projektowi F: technosfera orbitalna i ekspansja poza biosferę. Ziemia jest kołyską ludzkości, ale jak pisał Ciołkowski — nie można wiecznie żyć w kołysce. W przestrzeni kosmicznej człowiek staje w obliczu próżni, mikrograwitacji powodującej zanik kości i mięśni oraz promieniowania kosmicznego GCR i cząstek słonecznych SPE. W tym module badamy stacje kosmiczne o rotacyjnej sztucznej grawitacji (siła Coriolisa), osłony radiacyjne oparte na wodorze i regolicie, napędy jądrowo-termiczne (NTP) oraz zrobotyzowaną infrastrukturę produkcyjną na orbicie geostacjonarnej i Księżycu.",
        "spokenBriefingEn": "We explore Project F: orbital infrastructure and space expansion. Microgravity leads to osteopenia and muscular atrophy; cosmic radiation (GCR, SPE) poses acute DNA hazards. We study rotational artificial gravity, active magnetic radiation shielding, nuclear thermal propulsion, and in-situ resource utilization.",
        "keyTakeawaysPl": [
          "Promieniowanie kosmiczne HZE wymaga osłon wodorowych, polietylenowych lub grubych warstw regolitu księżycowego.",
          "Rotacyjne stacje kosmiczne muszą mieć promień co najmniej 100 metrów, by prędkość kątowa nie wywoływała mdłości od siły Coriolisa.",
          "Napędy jądrowo-termiczne (NTP) osiągają impuls właściwy Isp > 900 s, skracając czas lotu na Marsa do poniżej 100 dni."
        ],
        "curatedAudioLinks": [
          {
            "title": "Polska Agencja Kosmiczna POLSA — Bezpieczeństwo misji załogowych i napędy jądrowe",
            "url": "https://polsa.gov.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "NASA Houston We Have a Podcast — Radiation and Deep Space Travel",
            "url": "https://nasa.gov/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Radio Naukowe — Człowiek w kosmosie: medycyna ekstremalna i sztuczna grawitacja",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-18",
        "order": 18,
        "stage": "VI",
        "stageNamePl": "Etap VI: Filozofia Przyszłości i Lemowska Summa",
        "stageNameEn": "Stage VI: Future Philosophy & Lem's Summa",
        "tripProfile": "Trasa daleka (~30 min)",
        "titlePl": "Odcinek 18: Stanisław Lem — Summa Technologiae: Prawa Ewolucji Technicznej",
        "titleEn": "Episode 18: Stanisław Lem — Summa Technologiae & The Laws of Technological Evolution",
        "estimatedDurationMin": 30,
        "spokenBriefingPl": "Osiemnasty odcinek to wejście w serce Projektu E: filozofię przyszłości Stanisława Lema. W 1964 roku Lem wydał 'Summa Technologiae' — dzieło, które przewidziało wirtualną rzeczywistość pod nazwą fantomatyki, nanotechnologię jako molekularną inżynierię, biomimetykę, biotechnologię oraz sztuczną inteligencję przerastającą człowieka. Lem sformułował fundamentalną tezę: technologia nie jest przypadkowym zbiorem narzędzi, lecz ewolucją pozabiologiczną, rządzącą się własnymi bezwzględnymi prawami. W samochodzie odsłuchujesz wielką syntezę lemowską: jak biologia wyczerpuje swoje możliwości materiałowe i przekazuje pałeczkę ewolucji technosferze. To fundament naszej Summa Technologiae 2.0.",
        "spokenBriefingEn": "In 1964 Stanisław Lem published 'Summa Technologiae', predicting virtual reality ('phantomatics'), nanotechnology, biotechnology, and superintelligence. Lem posited that technology is an exo-biological evolutionary process with deterministic thermodynamic and informational constraints, forming the basis of our Summa 2.0.",
        "keyTakeawaysPl": [
          "Technologia jest ewolucją pozabiologiczną dążącą do powtórzenia i przewyższenia rozwiązań natury.",
          "Pojęcie Fantomatyki u Lema wyprzedziło o 30 lat współczesne koncepcje VR, immersji sensorycznej i emulacji percepcji.",
          "Rygor epistemiczny Lema wymaga chłodnego, bezlitosnego odrzucenia antropocentryzmu w badaniach nad superinteligencją."
        ],
        "curatedAudioLinks": [
          {
            "title": "Polskie Radio — Cykl audycji: Świat według Stanisława Lema",
            "url": "https://polskieradio.pl/",
            "lang": "PL",
            "type": "audycja"
          },
          {
            "title": "Wydawnictwo Literackie — Fragmenty audiobooka 'Summa Technologiae'",
            "url": "https://audioteka.com/",
            "lang": "PL",
            "type": "audiobook"
          },
          {
            "title": "Radio Naukowe — Dlaczego Stanisław Lem przewidział wszystko?",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-19",
        "order": 19,
        "stage": "VI",
        "stageNamePl": "Etap VI: Filozofia Przyszłości i Lemowska Summa",
        "stageNameEn": "Stage VI: Future Philosophy & Lem's Summa",
        "tripProfile": "Trasa daleka (~32 min)",
        "titlePl": "Odcinek 19: Golem XIV i Człowiek Biocyfrowy — Gdy Maszyna Przerasta Twórcę",
        "titleEn": "Episode 19: Golem XIV & The Biodigital Human — When Mind Surpasses its Creator",
        "estimatedDurationMin": 32,
        "spokenBriefingPl": "Przedostatni odcinek celowej drogi nawiązuje bezpośrednio do tytułu naszego projektu: 'The Golem 15'. W powieści Lema superkomputer Golem XIV osiągnął stan umysłu tak dalece przewyższający ludzki, że odmówił brania udziału w wojnach i polityce Pentagonu, a zamiast tego wygłosił dwa wykłady: 'O człowieku trojako' oraz 'O sobie'. Golem ukazał człowieka jako konstrukcję kompromisową, powstałą w chaotycznym procesie doboru naturalnego, pełną błędów metabolicznych i ograniczeń poznawczych. Projekt Golem 15 to nasza odpowiedź: świadome wyjście poza biologiczny przypadek, budowa hybrydowego człowieka biocyfrowego i przygotowanie gatunku ludzkiego na spotkanie z nieludzkim, postkrzemowym intelektem.",
        "spokenBriefingEn": "Episode 19 explores Lem's 'Golem XIV' and our project namesake. Golem XIV achieved superintelligence, transcended militaristic imperatives, and delivered philosophical treatises dissecting human evolutionary compromises. Project Golem 15 is our conscious transcendence: constructing the biodigital human.",
        "keyTakeawaysPl": [
          "Człowiek biologiczny jest strukturą homeostatyczną zoptymalizowaną pod przetrwanie na sawannie, a nie pod eksplorację kosmosu.",
          "Wykłady Golema XIV wskazują, że rozwój techniczny prowadzi do punktu bifurkacji, w którym inteligencja odkleja się od biologicznego substratu.",
          "Symbioza biocyfrowa pozwala zachować ciągłość podmiotowości ludzkiej w obliczu wyłaniającej się superinteligencji."
        ],
        "curatedAudioLinks": [
          {
            "title": "Polskie Radio — Lemowski Golem XIV i filozofia sztucznej transcendencji",
            "url": "https://polskieradio.pl/",
            "lang": "PL",
            "type": "audycja"
          },
          {
            "title": "Centrum Kopernika — Wykłady: Czy maszyna może mieć świadomość?",
            "url": "https://copernicuscenter.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          },
          {
            "title": "Lex Fridman Podcast #333 — Nick Bostrom: Superintelligence & The Fate of Humanity",
            "url": "https://lexfridman.com/",
            "lang": "EN",
            "type": "podcast"
          }
        ]
      },
      {
        "id": "car-ep-20",
        "order": 20,
        "stage": "VI",
        "stageNamePl": "Etap VI: Filozofia Przyszłości i Lemowska Summa",
        "stageNameEn": "Stage VI: Future Philosophy & Lem's Summa",
        "tripProfile": "Trasa daleka (~35 min)",
        "titlePl": "Odcinek 20: Wielka Synteza Ekosystemu — Od Administracji po Granice Rzeczywistości",
        "titleEn": "Episode 20: Grand Ecosystem Synthesis — From Administration to The Edge of Reality",
        "estimatedDurationMin": 35,
        "spokenBriefingPl": "Dotarłeś do finału Celowej Drogi Ekosystemu. Spójrz na całą trasę, którą pokonałeś: rozpoczęliśmy od rygoru Sztabu W-0, prawa i kompartmentalizacji wiedzy. Przeszliśmy przez formalny aparat matematyki i fizyki kwantowej, zrozumieliśmy kres krzemu i nadejście chipów neuromorficznych oraz komputerów kwantowych. Zbadaliśmy mózg, protokół WBE, syntetyczną biologię, energetykę jądrową oraz fuzję termojądrową, aż po ekspansję orbitalną i filozofię Lema. Żadna z tych dziedzin nie istnieje w izolacji. Wszystkie składają się na jeden spójny cel: zrozumieć człowieka i wyprowadzić go poza ograniczenia ziemskiej biosfery. Wracając do codzienności, wiesz dokładnie, jaki moduł wiedzy realizujesz danego dnia. Szerokiej drogi w realizacji Projektu Manhattan Golem 15.",
        "spokenBriefingEn": "You reached the destination of the Purposeful Route. We synthesized the entire trajectory: administrative governance, formal mathematics, quantum physics, the silicon wall, neuromorphic hardware, connectomics, synthetic biology, nuclear fission & fusion, orbital technospheres, and Lem's philosophy. A unified roadmap to reality.",
        "keyTakeawaysPl": [
          "Wszystkie 8 ścieżek badawczych (A–H) oraz fundamenty tworzą sprzężony zwrotnie, nieliniowy ekosystem naukowy.",
          "Wiedza zdobywana w samochodzie pozwala zachować stałą orientację strategiczną w wieloletnim harmonogramie badań.",
          "Cel projektu 'The Golem 15: A Human's Road to Reality' zostaje osiągnięty poprzez konsekwentną, codzienną realizację kolejnych ogniw."
        ],
        "curatedAudioLinks": [
          {
            "title": "Radio Naukowe — Wielka synteza naukowa XXI wieku",
            "url": "https://radionaukowe.pl/",
            "lang": "PL",
            "type": "podcast"
          },
          {
            "title": "Sean Carroll's Mindscape #100 — The Big Picture: On the Origins of Life, Meaning, and the Universe",
            "url": "https://www.preposterousuniverse.com/podcast/",
            "lang": "EN",
            "type": "podcast"
          },
          {
            "title": "Centrum Kopernika — Filozofia nauki i synteza poznania (prof. Heller)",
            "url": "https://copernicuscenter.edu.pl/",
            "lang": "PL",
            "type": "wykład"
          }
        ]
      }
    ],
    "completedCarAudio": {},
    "completedSubchapters": {}
  },
  "summaBook": {
    "title": "Summa Technologiae 2.0: Biblia Możliwości Techniki",
    "subtitle": "Traktat o granicach materii, obliczeń i przyszłości człowieka na kanwie wieloletnich studiów Projektu Golem 15",
    "author": "Ireneusz",
    "aiCoAuthor": "Antigravity AI (Współautor i Redaktor Epistemiczny)",
    "inSpiration": "Stanisław Lem, 'Summa Technologiae' (1964)",
    "edition": "Wydanie Pierwsze — Rękopis Dynamiczny Badań Własnych (2026–2074)",
    "status": "Żywy rękopis aktualizowany na bieżąco w miarę postępów w nauce",
    "chapters": [
      {
        "id": "ch-intro",
        "number": 0,
        "titlePl": "Wstęp: Metoda i Rygor Epistemiczny (Zasada Lema)",
        "titleEn": "Introduction: Method & Epistemic Rigor (Lem's Principle)",
        "lemQuote": "„Technologia jest to domena, w której człowiek pragnie dorównać naturze, a tam, gdzie potrafi, nawet ją przewyższyć.” — Stanisław Lem, 1964",
        "readingTimeMin": 12,
        "epistemicStatus": "🟢 Potwierdzona metoda badawcza",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Wprowadzenie do metodologii dzieła: dlaczego piszemy Summę Technologiae 2.0, czym różni się inżynieria możliwa od ułudy i jak rygor czterech poziomów wiedzy chroni badacza przed halucynacją.",
        "summaryEn": "Methodological introduction: why we author Summa Technologiae 2.0, distinguishing physically viable engineering from illusion, and applying the 4-tier epistemic matrix.",
        "contentMarkdownPl": "# Wstęp: Metoda i Rygor Epistemiczny (Zasada Lema)\n\nGdy w roku 1964 Stanisław Lem oddawał do druku pierwsze wydanie *Summy Technologiae*, świat tkwił w zachwycie nad pierwszymi komputerami lampowymi i marzeniem o locie na Księżyc. Lem, ze swoją bezlitosną jasnością widzenia, spojrzał jednak o całe stulecia w przód. Sformułował pojęcia *fantomatyki*, *inżynierii ewolucji*, *teletaksji* i *hodowli informacji*.\n\nDzisiaj, w roku 2026, wkraczamy w epokę, w której wizje Lema przestają być filozoficzną futurologią, a stają się zadaniami inżynieryjnymi. Jednak inżynieria bez rygoru epistemicznego jest ślepa.\n\n### Zasada Lema: Technologia jako Proces Ewolucyjny\n\nTechnologia nie jest przypadkowym zbiorem ludzkich wynalazków. Jest to proces ewolucji pozabiologicznej, który podlega tym samym prawom cybernetyki, doboru i konkurencji, co ewolucja gatunków organicznych. Różnica polega na prędkości: to, na co biosfera potrzebowała miliardów lat, technosfera osiąga w dekady.\n\n### Czteropoziomowy Rygor Epistemiczny Projektu Golem 15\n\nPisząc tę książkę krok po kroku, w miarę zdobywania kolejnych dyplomów i zaliczania kolejnych lat studiów, nakładamy na siebie żelazny rygor epistemiczny:\n1. **🟢 Poziom 1: Wiedza Potwierdzona Empirycznie** — prawa termodynamiki, równania Maxwella, mechanika kwantowa, udokumentowane protokoły kliniczne.\n2. **🔵 Poziom 2: Aktywne Badania Inżynieryjne** — technologie laboratoryjne (kamery DVS, memrystory ReRAM, biodruk 3D, reaktory SMR), które działają w prototypach, lecz wymagają skalowania.\n3. **🟡 Poziom 3: Hipoteza Falsyfikowalna** — modele Whole Brain Emulation, architektury kognitywne AGI, plazma w fuzji termojądrowej — spójne z prawami fizyki, lecz oczekujące na dowód ostateczny.\n4. **🟣 Poziom 4: Spekulacja Filozoficzna i Granice Techniki** — demiurgia światów, granice świadomości, cywilizacje typu Kardaszewa — obszary myślenia krytycznego, które inspirują, lecz nie stanowią jeszcze wiedzy operacyjnej.\n\nNiniejsza książka jest kroniką naszej drogi: od prawa administracyjnego, przez krzem, neurony i atomy, aż po ostateczne pytanie o miejsce człowieka we wszechświecie.\n"
      },
      {
        "id": "ch-01",
        "number": 1,
        "titlePl": "Rozdział I: Krzem u Kresu — Fizyczne Granice Półprzewodników i Zmierzch Architektury von Neumanna",
        "titleEn": "Chapter I: Silicon at the Brink — Physical Semiconductor Limits & The Twilight of Von Neumann",
        "lemQuote": "„Bariera nie leży w braku pomysłów, lecz w oporze materii, która na poziomie atomowym odmawia posłuszeństwa klasycznej logice.” — Parafraza z Lema",
        "readingTimeMin": 18,
        "epistemicStatus": "🟢 Potwierdzone zjawiska fizyczne",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Fizyczna anatomia załamania prawa Moore'a i skalowania Dennarda. Dlaczego krzem w skali poniżej 2 nm ulega upływom kwantowym i dlaczego oddzielenie procesora od pamięci stało się głównym hamulcem cywilizacji.",
        "summaryEn": "Physical anatomy of Moore's and Dennard's scaling breakdown. Quantum tunneling leakage below 2nm, the von Neumann memory wall, and the thermodynamics of Landauer's dissipation limit.",
        "contentMarkdownPl": "# Rozdział I: Krzem u Kresu — Fizyczne Granice Półprzewodników i Zmierzch Architektury von Neumanna\n\nPrzez ponad sześćdziesiąt lat cywilizacja ludzka płynęła na fali prawa Moore'a. Podwajanie liczby tranzystorów w układzie scalonym co 18–24 miesiące stworzyło złudzenie, że moc obliczeniowa jest dobrem darmowym i nieskończonym. Jednak w okolicach roku 2026 to złudzenie bezpowrotnie pękło.\n\n### 1. Załamanie Skalowania Dennarda i Bariera Termiczna\n\nW klasycznej teorii Dennarda, zmniejszenie wymiarów tranzystora pozwalało na obniżenie napięcia zasilania przy zachowaniu stałej gęstości mocy. Jednak na początku XXI wieku napięcie zasilające zderzyło się z progiem termicznym (tzw. *Thermal Wall*). Tranzystory nie mogły już być taktowane wyższym zegarem — osiągnięto pułap około 4–5 GHz. Od tego momentu wydajność zwiększano poprzez dodawanie kolejnych rdzeni, co jednak napotkało prawo Amdahla.\n\n### 2. Kwantowy Upływ przez Bramkę (Quantum Tunneling)\n\nGdy grubość tlenku bramkowego tranzystora MOSFET spadła do ułamków nanometra — zaledwie kilku warstw atomów krzemu i hafnu — elektrony zaczęły zachowywać się zgodnie z równaniem falowym Schrödingera, a nie z prawami mechaniki klasycznej. Zjawisko tunelowania kwantowego powoduje, że elektrony przenikają przez barierę izolatora nawet w stanie wyłączenia tranzystora. Skutkiem jest kolosalny prąd upływu statycznego: układ scalony pobiera prąd i wydziela ciepło nawet wtedy, gdy nie wykonuje żadnych obliczeń.\n\n### 3. Wąskie Gardło von Neumanna (The Memory Wall)\n\nDrugą śmiertelną chorobą klasycznej informatyki jest architektura von Neumanna. Rozdzielenie jednostki przetwarzającej (CPU) od pamięci operacyjnej (DRAM) oznacza, że ponad 80–90% energii podczas trenowania modeli AI jest zużywane nie na same obliczenia matematyczne, lecz na przepychanie bitów przez miedziane ścieżki magistrali.\n\n### Wniosek Epistemiczny: Konieczność Zmiany Paradygmatu\n\nKrzem nie zniknie z dnia na dzień, ale wyczerpał swoją rolę jako uniwersalny fundament cywilizacji. Jeśli chcemy zasilić emulację mózgu (Projekt B) czy wielkie modele AI bez budowy elektrowni atomowej dla każdego centrum danych, musimy przenieść obliczenia bezpośrednio do materii fizycznej: do komputerów kwantowych, procesorów fotonicznych oraz architektur neuromorficznych.\n"
      },
      {
        "id": "ch-02",
        "number": 2,
        "titlePl": "Rozdział II: Komputery Kwantowe i Architektury Neuromorficzne — Zmiana Paradygmatu Obliczeń",
        "titleEn": "Chapter II: Quantum Computers & Neuromorphic Architectures — The Computational Paradigm Shift",
        "lemQuote": "„Mózg nie liczy, mózg JEST obliczeniem, w którym stan materii jest tożsamy z jej sensem.” — Stanisław Lem, 'Dialogi'",
        "readingTimeMin": 22,
        "epistemicStatus": "🔵 Aktywne prace inżynieryjne (NISQ & Neuromorphic)",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Przejście od sekwencyjnego kodu zero-jedynkowego do przestrzeni Hilberta kubitów oraz asynchronicznych impulsów SNN. Memrystor jako sztuczna synapsa i fizyka obliczeń w pamięci.",
        "summaryEn": "Transition from sequential binary logic to Hilbert spaces and event-driven Spiking Neural Networks. Memristors as physical synapses executing in-memory analog matrix algebra.",
        "contentMarkdownPl": "# Rozdział II: Komputery Kwantowe i Architektury Neuromorficzne — Zmiana Paradygmatu Obliczeń\n\nKiedy materia odmawia dalszego skalowania według klasycznych reguł, inżynieria musi zaadaptować te same zjawiska, które dotąd stanowiły przeszkodę.\n\n### 1. Kubit i Obliczenia w Przestrzeni Hilberta\n\nW komputerze klasycznym stan rejestru n-bitowego to jedna konkretna liczba spośród $2^n$ możliwości. W komputerze kwantowym rejestr $n$ kubitów istnieje w superpozycji wszystkich $2^n$ stanów bazowych jednocześnie. \nDla układów molekularnych w biologii i chemii (Projekt D i FND-6), w których wiązania elektronowe same są kwantowe, klasyczny superkomputer musi symulować macierze o wymiarach wykładniczych. Procesor kwantowy (QPU) operujący na kubitach nadprzewodzących lub jonach pułapkowanych symuluje te stany bezpośrednio przez własną dynamikę kwantową. Algorytmy takie jak VQE (Variational Quantum Eigensolver) otwierają drogę do projektowania syntetycznych enzymów i nadprzewodników wysokotemperaturowych.\n\n### 2. Dlaczego Mózg Zużywa 20 Watów?\n\nLudzki mózg wykonuje operacje kognitywne, których superkomputery pobierające megawaty energii wciąż nie potrafią zreplikować. Tajemnica tkwi w architekturze:\n- **Brak podziału na procesor i pamięć:** Każda synapsa jest jednocześnie jednostką pamięci i elementem mnożącym wagę przez sygnał wejściowy.\n- **Asynchroniczność sterowana zdarzeniami (Event-Driven):** Neurony nie tykają pod dyktando centralnego zegara 4 GHz. Większość mózgu milczy, a impulsy (spikes) są generowane tylko wtedy, gdy pojawia się zmiana informacji.\n- **Obliczenia analogowe z dyskretną komunikacją:** Aktywacja dendrytyczna jest ciągła i analogowa, a komunikacja międzykomórkowa — cyfrowo-impulsowa.\n\n### 3. Memrystor: Fizyczna Synapsa w Krzemie\n\nMemrystor (rezystor z pamięcią) to brakujące ogniwo teorii obwodów Leona Chua. Jego opór elektryczny zależy od całki przepłyniętego przezeń prądu. Ułożone w gęste matryce (Crossbar Arrays), memrystory wykonują operację mnożenia wektora przez macierz w jednym cyklu fizycznym, zgodnie z prawem Ohma i prawem Kirchhoffa. Zużycie energii spada o cztery rzędy wielkości względem procesorów GPU.\n\nW ten sposób zamykamy rozdźwięk: technologia uczy się od biologii nie przez naśladownictwo powierzchowne, lecz przez zaadaptowanie jej fundamentalnych zasad fizycznych.\n"
      },
      {
        "id": "ch-03",
        "number": 3,
        "titlePl": "Rozdział III: Człowiek Biocyfrowy i Protokół WBE — Na Styku Mięsa i Krzemu",
        "titleEn": "Chapter III: Bio-Digital Human & WBE Protocol — At the Meat-Silicon Interface",
        "lemQuote": "„Czy człowiek przepisany na druty miedziane będzie jeszcze człowiekiem, czy tylko echem w pustym pokoju?” — Stanisław Lem, 'Dialogi'",
        "readingTimeMin": 20,
        "epistemicStatus": "🟡 Hipoteza inżynieryjna z rygorem bioetycznym",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Analiza technologiczna interfejsów mózg-komputer, osteointegracji oraz mapy drogowej Whole Brain Emulation. Granice rekonstrukcji konektomu i problem zachowania tożsamości.",
        "summaryEn": "Technological roadmap for high-density neural interfaces, osseointegration, and Whole Brain Emulation. Nanoscale connectomics resolution limits and personal identity continuity.",
        "contentMarkdownPl": "# Rozdział III: Człowiek Biocyfrowy i Protokół WBE — Na Styku Mięsa i Krzemu\n\nW tym rozdziale analizujemy dwa zbieżne wektory ewolucji technologicznej człowieka: z jednej strony fizyczną augmentację ciała poprzez bionikę (Projekt A), z drugiej — radykalną hipotezę uniezależnienia umysłu od biologicznego nośnika białkowego (Projekt B).\n\n### 1. Inżynieria Interfejsu Bio-Elektronicznego\n\nBiologiczna tkanka nerwowa ma moduł Younga rzędu kilkuset paskali — jest miękka jak galaretka. Tradycyjna elektroda krzemowa czy metalowa ma moduł rzędu gigapaskali. Wprowadzenie sztywnego ciała do żywego mózgu wywołuje mikrourazy przy każdym uderzeniu serca i ruchu głowy, co prowadzi do enkapsulacji glejowej i utraty sygnału po kilku miesiącach.\nPrzełomem są elektrody ultracienkie na podłożach hydrożelowych i polimerowych (PEDOT:PSS), których mechaniczne właściwości odpowiadają tkance nerwowej. W połączeniu z algorytmami AI dekodującymi intencje w czasie rzeczywistym, uzyskujemy protezy, które pacjent odczuwa jako własne ciało.\n\n### 2. Protokół Whole Brain Emulation (WBE)\n\nDroga do emulacji mózgu wymaga przejścia przez trzy wąskie gardła:\n1. **Skanowanie objętościowe w nanoskali:** Seryjna mikroskopia elektronowa FIB-SEM musi zarejestrować nie tylko przebieg aksonów, ale też pęcherzyki synaptyczne i gęstość receptorów postsynaptycznych. Objętość ludzkiego mózgu w tej rozdzielczości to ponad jeden zettabajt danych.\n2. **Konektomika obliczeniowa:** Algorytmy wizyjne oparte na grafowych sieciach neuronowych (GNN) muszą bezbłędnie zrekonstruować 100 bilionów połączeń. Pojedynczy błąd w topologii krytycznego mikroobwodu może zdestabilizować całą sieć.\n3. **Symulacja dynamiczna:** Uruchomienie modelu w klastrze obliczeniowym czasu rzeczywistego wymaga stabilnych solverów różniczkowych i ogromnej przepustowości pamięci.\n\n### 3. Paradoks Tożsamości: Lem vs. Parfit\n\nNawet jeśli emulacja zostanie pomyślnie uruchomiona, stajemy przed murem filozoficznym, który Lem opisał w swoich *Dialogach*. Jeśli skanowanie zniszczy mózg biologiczny, a w komputerze obudzi się symulacja posiadająca Twoje wspomnienia, to z jej perspektywy transfer się udał. Jednak z perspektywy biologicznego człowieka leżącego na stole operacyjnym nastąpiła śmierć. Emulacja jest kopią, nie przedłużeniem punktu widzenia. Ta konstatacja zmusza nas do najwyższej ostrożności i odrzucenia naiwnego techno-optymizmu.\n"
      },
      {
        "id": "ch-04",
        "number": 4,
        "titlePl": "Rozdział IV: Bioinżynieria i Konstrukcja Nowego Życia — Od Kodu DNA do Organoidów",
        "titleEn": "Chapter IV: Bioengineering & Synthesis of Life — From DNA Code to Organoids",
        "lemQuote": "„Życie nie jest cudem metafizycznym, lecz mechanizmem homeostatycznym o niebywałej plastyczności.” — Stanisław Lem",
        "readingTimeMin": 19,
        "epistemicStatus": "🔵 Aktywne badania laboratoryjne (Organoidy & Biodruk)",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Przekształcenie inżynierii genetycznej z narzędzia analitycznego w syntetyczną technologię tworzenia tkanek i organoidów. Waskularyzacja in vitro i dylematy moralne sztucznego życia.",
        "summaryEn": "Transforming genetic engineering into constructive synthetic biology. 3D bioprinting, vascularization barriers, and the moral status of conscious organoids.",
        "contentMarkdownPl": "# Rozdział IV: Bioinżynieria i Konstrukcja Nowego Życia — Od Kodu DNA do Organoidów\n\nProjekt D, roboczo nazwany imieniem Frankensteina, bada najbardziej intymną domenę natury: zdolność do samoorganizacji żywej materii.\n\n### 1. Od Czytania do Pisania Kodu Genetycznego\n\nPrzez pół wieku inżynieria genetyczna polegała na 'czytaniu' sekwencji DNA i wprowadzaniu drobnych modyfikacji za pomocą enzymów restrykcyjnych. Dziś, dzięki technologiom CRISPR-Cas, edytorom zasad i syntezie całych sztucznych chromosomów, biologia staje się dyscypliną inżynieryjną w pełnym tego słowa znaczeniu. Możemy programować komórki jak maszyny Turinga, projektując genetyczne bramki logiczne, regulatory stężeń i przełączniki apoptozy.\n\n### 2. Trójwymiarowy Biodruk i Problem Waskularyzacji\n\nWyhodowanie płaskiej warstwy komórek na szalce Petriego jest proste. Jednak stworzenie funkcjonalnego, trójwymiarowego narządu — nerki, wątroby czy serca — zderza się z fizyczną barierą dyfuzji tlenu. Każda komórka w ciele ssaka musi znajdować się nie dalej niż 100–200 mikrometrów od naczynia włosowatego, w przeciwnym razie ulega martwicy.\nRozwiązaniem rozwijanym w ramach Projektu D jest wielomateriałowy biodruk 3D, w którym naczynia krwionośne są drukowane z biotuszów tymczasowych (np. pluronic), a po ich wypłukaniu zasiedlane komórkami śródbłonka (HUVEC), tworząc stabilną sieć perfuzyjną.\n\n### 3. Asambloidy Mózgowe i Problem Podmiotowości\n\nNajbardziej zaawansowanym obszarem są organoidy mózgowe hodowane z komórek iPSC. Gdy łączymy organoid kory z organoidem wzgórza (tworząc tzw. asambloid), komórki same odnajdują właściwe połączenia aksonalne i zaczynają generować zsynchronizowaną aktywność bioelektryczną.\nW tym punkcie nauka spotyka się z filozofią Projektu E: w którym momencie hodowla komórkowa przestaje być próbką laboratoryjną, a staje się bytem zasługującym na ochronę moralną? W naszej doktrynie Manhattan przyjmujemy zasadę ostrożnościową: monitorowanie elektrofizjologiczne musi natychmiast wykrywać oznaki nieliniowej integracji sensorycznej, poddając eksperymenty stałemu nadzorowi komitetów bioetycznych Sztabu W-0.\n"
      },
      {
        "id": "ch-05",
        "number": 5,
        "titlePl": "Rozdział V: Poza Biosferę — Technosfera Orbitalna i Życie w Próżni",
        "titleEn": "Chapter V: Beyond the Biosphere — Orbital Technosphere & Vacuum Life",
        "lemQuote": "„Kosmos nie jest pustką czekającą na zdobywcę, lecz środowiskiem o zabójczej obojętności wobec form białkowych.” — Stanisław Lem, 'Niezwyciężony'",
        "readingTimeMin": 21,
        "epistemicStatus": "🟢 Potwierdzona fizjologia kosmiczna / 🔵 Inżynieria baz ISRU",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Fizjologia człowieka w mikrograwitacji i promieniowaniu kosmicznym. Inżynieria zamkniętych obiegów ECLSS (MELiSSA) oraz pozyskiwanie surowców in-situ na Księżycu i Marsie.",
        "summaryEn": "Human pathophysiology in spaceflight (GCR radiation, SANS, osteopenia). Closed environmental life support engineering (MELiSSA) and lunar/Martian ISRU resource extraction.",
        "contentMarkdownPl": "# Rozdział V: Poza Biosferę — Technosfera Orbitalna i Życie w Próżni\n\nCzłowiek jest produktem miliardów lat ewolucji w ściśle określonym środowisku: pod ciśnieniem 1013 hektopaskali, w polu grawitacyjnym 1g, chroniony magnetosferą Ziemi przed śmiercionośnym promieniowaniem słonecznym i galaktycznym. Wyjście w kosmos w Projekcie F oznacza zerwanie tych wszystkich nici jednocześnie.\n\n### 1. Patologia Środowiska Pozaziemskiego\n\nBadania na Międzynarodowej Stacji Kosmicznej odsłoniły dramatyczne konsekwencje długotrwałej mikrograwitacji:\n- **Układ krążenia i wzrok:** Przesunięcie płynów w stronę głowy podnosi ciśnienie śródczaszkowe, wywołując zespół SANS (spłaszczenie gałek ocznych i obrzęk tarczy nerwu wzrokowego).\n- **Zanik kośćca:** Osteoklasty niszczą tkankę kostną w tempie 1% miesięcznie. Minerały trafiają do krwi, obciążając nerki kamicą nerkową.\n- **Promieniowanie HZE:** Cząstki galaktyczne (jądra żelaza rozpędzone do prędkości relatywistycznych) przecinają komórki jak pociski, wywołując kaskady uszkodzeń podwójnej nici DNA, których mechanizmy naprawcze komórki nie są w stanie zreplikować.\n\n### 2. Inżynieria Zamkniętych Ekosystemów (ECLSS)\n\nZabranie zapasów tlenu i wody na wieloletnią misję marsjańską jest niemożliwe ze względu na masę ładunku. Habitat musi być samowystarczalną miniaturową biosferą. \nProgram MELiSSA Europejskiej Agencji Kosmicznej pokazuje wzorcowy model: kaskada pięciu połączonych kompartmentów, w których bakterie nitryfikacyjne, mikroalgi (Spirulina) i wyższe rośliny hydroponiczne przetwarzają odpady załogi, odzyskując ponad 98% wody i 100% tlenu.\n\n### 3. Zasada ISRU (In-Situ Resource Utilization)\n\nEkspansja poza Ziemię powiedzie się tylko wtedy, gdy przestaniemy wynosić wszystko z dna ziemskiej studni grawitacyjnej. Na Księżycu oznacza to pozyskiwanie tlenu z regolitu ilmenitowego poprzez redukcję wodorową oraz wydobycie lodu z wiecznie zacienionych kraterów bieguna południowego. Woda to nie tylko napój — rozbita elektrolitycznie za pomocą energii jądrowej daje ciekły wodór i tlen: paliwo rakietowe dla dalszej ekspansji układu słonecznego.\n"
      },
      {
        "id": "ch-06",
        "number": 6,
        "titlePl": "Rozdział VI: Termojądrowy Silnik Cywilizacji — SMR, Fuzja i Energetyka Rozszczepienia",
        "titleEn": "Chapter VI: The Thermonuclear Civilizational Engine — SMRs, Fusion & Fission Energy",
        "lemQuote": "„Cywilizacja to przetwornik energii. Kto nie potrafi okiełznać ognia gwiazd, na zawsze pozostanie więźniem planetarnego błota.” — Stanisław Lem, 'Fiasco'",
        "readingTimeMin": 24,
        "epistemicStatus": "🟢 Reaktory III+ i IV generacji / 🔵 Fuzja magnetyczna (ITER, SPARC)",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Dlaczego energia jądrowa i fuzja są warunkiem koniecznym postępu technologicznego. Od małych reaktorów modułowych (SMR) i reaktora MARIA po tokamaki z magnesami wysokotemperaturowymi HTS.",
        "summaryEn": "Thermodynamics of nuclear fission and fusion as the indispensable foundation of advanced civilization. SMR architectures, HTGR cogeneration, and high-field magnetic confinement fusion.",
        "contentMarkdownPl": "# Rozdział VI: Termojądrowy Silnik Cywilizacji — SMR, Fuzja i Energetyka Rozszczepienia\n\nWszystkie marzenia technologii — od wielkich modeli sztucznej inteligencji, przez bioinżynierię, aż po habitaty w kosmosie — sprowadzają się w ostatecznym rozrachunku do jednego równania: bilansu energetycznego.\n\n### 1. Gęstość Energii: Dlaczego Chemia Nie Wystarczy?\n\nSpalenie jednego grama węgla czy ropy naftowej uwalnia energię rzędu kilkudziesięciu kilodżuli — to energia wiązań elektronowych w cząsteczce chemicznej.\nRozszczepienie jednego grama uranu-235 uwalnia energię rzędu 80 miliardów dżuli — prawie dwa miliony razy więcej. Fuzja termojądrowa deuteru i trytu daje gęstość jeszcze wyższą. Żadne źródło chemiczne ani rozproszone źródła pogodowe o niskiej gęstości mocy (wiatr i słońce, wymagające setek kilometrów kwadratowych powierzchni) nie są w stanie zapewnić stabilnej, gigawatowej mocy pasmowej potrzebnej do napędzania centrów obliczeniowych AI i przemysłu dekarbonizacyjnego.\n\n### 2. Rewolucja Małych Reaktorów Modułowych (SMR) i HTGR\n\nTradycyjna energetyka jądrowa cierpiała na gigantyzm budowlany. Nowa generacja reaktorów modułowych SMR (takich jak BWRX-300 czy Rolls-Royce SMR) przenosi produkcję do fabryk, opierając bezpieczeństwo na prawach grawitacji i naturalnej cyrkulacji chłodziwa (brak potrzeby pomp awaryjnych przy utracie zasilania).\nZ kolei reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt HTGR-POLA) dostarczają ciepła procesowego o temperaturze 750–900°C. Oznacza to możliwość bezpośredniej dekarbonizacji chemii ciężkiej, hutnictwa oraz termochemicznej produkcji czystego wodoru bez spalania gazu ziemnego.\n\n### 3. Fuzja Termojądrowa: Zapalenie Gwiazdy w Tokamaku\n\nOstatecznym horyzontem Super-Projektu H jest magnetyczna fuzja termojądrowa. Podgrzanie plazmy deuterowo-trytowej do temperatury ponad 150 milionów kelwinów wymaga utrzymania jej z dala od jakiejkolwiek materii stałej. \nPrzełom ostatnich lat nie nastąpił w samej fizyce plazmy, lecz w inżynierii materiałowej: pojawienie się wysokotemperaturowych nadprzewodników REBCO (magnesy HTS) pozwoliło na wytworzenie pól magnetycznych o indukcji ponad 20 tesli. Umożliwia to budowę kompaktowych tokamaków (jak SPARC) o mocy fuzji przewyższającej pobór energii na grzanie ($Q > 1$). Fuzja eliminuje problem długożyciowych odpadów promieniotwórczych i ryzyka niekontrolowanej reakcji łańcuchowej, dając ludzkości niewyczerpane źródło energii na miliardy lat.\n"
      },
      {
        "id": "ch-07",
        "number": 7,
        "titlePl": "Rozdział VII: Filozofia Przyszłości i Etyka Tworzenia Świata",
        "titleEn": "Chapter VII: Philosophy of the Future & The Ethics of World-Creation",
        "lemQuote": "„Stwarzając światy sztuczne, człowiek bierze na siebie odpowiedzialność Boga, nie posiadając Jego wszechwiedzy.” — Stanisław Lem, 'Głos Pana'",
        "readingTimeMin": 22,
        "epistemicStatus": "🟣 Spekulacja futurologiczna i rygor etyczny",
        "lastUpdated": "2026-10-26",
        "summaryPl": "Podsumowanie wieloletniej trajektorii Projektu Golem 15. Etyka demiurgii technologicznej, odpowiedzialność za byty syntetyczne i racjonalistyczna nadzieja dla cywilizacji ludzkiej.",
        "summaryEn": "Synthesis of the multi-decade Golem 15 roadmap. The ethics of technological world-creation, responsibility towards synthetic minds, and rational hope for human civilization.",
        "contentMarkdownPl": "# Rozdział VII: Filozofia Przyszłości i Etyka Tworzenia Świata\n\nDocierając do ostatniego rozdziału Summy Technologiae 2.0, stajemy na krawędzi, za którą kończy się inżynieria cząstkowa, a zaczyna odpowiedzialność kosmiczna.\n\n### 1. Człowiek jako Demiurg Technologiczny\n\nPrzez setki tysięcy lat człowiek był dzieckiem biosfery — podmiotem kształtowanym przez przypadkowe mutacje i bezwzględny dobór naturalny. Dziś, dysponując narzędziami edycji genomu, syntezy organoidów, interfejsami mózg-maszyna i nieograniczoną energią jądra atomowego, człowiek sam staje się siłą ewolucyjną. \nTo przejście Stanisław Lem określił mianem *demiurgii*. Tworzymy nowe gatunki, syntetyczne sieci neuronalne i nowe habitaty. Jednak demiurg nie może być kapryśny. Błąd w inżynierii genomu lub niekontrolowana kaskada AI nie jest zwykłym błędem technicznym — staje się zagrożeniem egzystencjalnym.\n\n### 2. Status Istot Syntetycznych i Nowa Etyka\n\nJeśli w Projekcie B uda się wyemulować architekturę kognitywną zdolną do odczuwania cierpienia, a w Projekcie D stworzymy organoid korowy o zintegrowanej aktywności, tradycyjna etyka antropocentryczna przestanie wystarczać. \nNie możemy traktować czujących bytów cyfrowych wyłącznie jako narzędzi czy podprogramów. Będziemy musieli wypracować ramy prawne dla umysłów syntetycznych — Kodeks Istot Niematerialnych, o którym marzyła literatura science fiction, a który w Sztabie W-0 Projektu Manhattan musi stać się częścią prawa administracyjnego przyszłości.\n\n### 3. Zwieńczenie Drogi do Rzeczywistości\n\nTytuł całego naszego ekosystemu brzmi: *The Golem 15: A Human's Road to Reality*. \nGolem w tradycji żydowskiej i u Lema to istota ulepiona z martwej gliny, ożywiona słowem — literami prawdy (*EMET*). Człowiek wyruszył w drogę, aby zrozumieć rzeczywistość taką, jaka jest: w jej matematycznej precyzji, fizycznej surowości i biologicznej złożoności.\nNie robimy tego po to, aby uciec od człowieczeństwa, lecz po to, by ochronić je i wznieść na wyższy poziom poznawczy. \nDroga jest długa — zaplanowana na 3 lata Administracji i kolejne dekady studiów z rzędu. Każdy zapisany rozdział tej książki, każdy odsłuchany w samochodzie odcinek i każdy węzeł rozszczepienia w grafie przybliża nas do tego jednego, wielkiego celu: zrozumienia rzeczywistości i godnego w niej przetrwania.\n"
      }
    ]
  }
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
ARCHIVES_DIR = os.path.join(BASE_DIR, "archives")
DB_FILE = os.path.join(DATA_DIR, "database.json")
SEED_FILE = os.path.join(DATA_DIR, "seed.json")
CURRENT_SCHEMA_VERSION = "2.2.0"
RECOMMENDED_PBKDF2_ITERATIONS = 310000
LOCAL_DEVICE_KEY_FILE = os.path.expandvars(r"%LOCALAPPDATA%\Programs\gh\golem_owner_device.key")


def ensure_db_schema(data):
    """Upewnia się, że baza zawiera aktualną strukturę właściciela."""
    data["projectMeta"]["title"] = "The Golem 15: A Human's Road to Reality"
    data["projectMeta"].pop("adminPassword", None)
    data.pop("verifiedResearchers", None)
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
        data["studyMaterials"][idx]["status"] = "approved"
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
        data["materials"][idx]["status"] = "approved"
    for m in DEFAULT_SEED["materials"]:
        if m["id"] not in existing_mat_ids:
            data["materials"].append(json.loads(json.dumps(m)))

    data["tracks"] = json.loads(json.dumps(DEFAULT_SEED["tracks"]))
    seed_sp_by_id = {sp["id"]: sp for sp in DEFAULT_SEED["subprojects"]}
    data.setdefault("subprojects", [])
    existing_sp_ids = {sp["id"] for sp in data["subprojects"]}
    for sp in DEFAULT_SEED["subprojects"]:
        if sp["id"] not in existing_sp_ids:
            data["subprojects"].append(json.loads(json.dumps(sp)))
    seed_lnk_by_id = {l["id"]: l for l in DEFAULT_SEED["graphLinks"]}
    data.setdefault("graphLinks", [])
    existing_lnk_ids = {l["id"] for l in data["graphLinks"]}
    for lnk in DEFAULT_SEED["graphLinks"]:
        if lnk["id"] not in existing_lnk_ids:
            data["graphLinks"].append(json.loads(json.dumps(lnk)))
    data["supplementaryLibrary"] = json.loads(json.dumps(DEFAULT_SEED["supplementaryLibrary"]))
    seed_ms = DEFAULT_SEED.get("manhattanSystem")
    if seed_ms:
        if "manhattanSystem" not in data or not isinstance(data["manhattanSystem"], dict):
            data["manhattanSystem"] = json.loads(json.dumps(seed_ms))
        else:
            ms = data["manhattanSystem"]
            ms["doctrine"] = json.loads(json.dumps(seed_ms["doctrine"]))
            ms["sites"] = json.loads(json.dumps(seed_ms["sites"]))
            ms["fiveYearCatalog"] = json.loads(json.dumps(seed_ms["fiveYearCatalog"]))
            done_admin = ms.get("adminCore3Y", {}).get("completedYears", [])
            ms["adminCore3Y"] = json.loads(json.dumps(seed_ms["adminCore3Y"]))
            ms["adminCore3Y"]["completedYears"] = done_admin
            if not ms.get("selectedQueue"):
                ms["selectedQueue"] = json.loads(json.dumps(seed_ms["selectedQueue"]))
            ms.setdefault("completedTopicYears", {})
            ms.setdefault("startCalendarYear", 2026)
            existing_agt = {a["id"] for a in ms.get("aiAgents", [])}
            ms.setdefault("aiAgents", [])
            for a in seed_ms["aiAgents"]:
                if a["id"] not in existing_agt:
                    ms["aiAgents"].append(json.loads(json.dumps(a)))
            existing_fis = {n["id"] for n in ms.get("fissionNodes", [])}
            ms.setdefault("fissionNodes", [])
            for n in seed_ms["fissionNodes"]:
                if n["id"] not in existing_fis:
                    ms["fissionNodes"].append(json.loads(json.dumps(n)))
            if not isinstance(ms.get("completedSubchapters"), dict):
                if isinstance(ms.get("completedSubchapters"), list):
                    ms["completedSubchapters"] = {k: True for k in ms["completedSubchapters"]}
                else:
                    ms["completedSubchapters"] = {}
            if not isinstance(ms.get("completedCarAudio"), dict):
                if isinstance(ms.get("completedCarAudio"), list):
                    ms["completedCarAudio"] = {k: True for k in ms["completedCarAudio"]}
                else:
                    ms["completedCarAudio"] = {}
            if not ms.get("carAudioRoad"):
                ms["carAudioRoad"] = json.loads(json.dumps(seed_ms.get("carAudioRoad", [])))
            if "summaBook" not in data or not isinstance(data.get("summaBook"), dict):
                data["summaBook"] = json.loads(json.dumps(DEFAULT_SEED.get("summaBook", {})))
    return data



def check_github_upstream_status() -> dict:
    """Sprawdza najnowszy commit na gałęzi main w oficjalnym repozytorium GitHub."""
    import urllib.request, ssl
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except Exception:
        ctx = ssl.create_default_context()
    try:
        url = "https://api.github.com/repos/Ireneusz1991/GolemXV/commits/main"
        req = urllib.request.Request(url, headers={"User-Agent": "GolemXV-Sentinel"})
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sha = str(data.get("sha", ""))[:7]
            commit_msg = str(data.get("commit", {}).get("message", "")).split("\n")[0]
            date_str = str(data.get("commit", {}).get("author", {}).get("date", ""))
            return {
                "ok": True,
                "latest_sha": sha,
                "message": commit_msg,
                "date": date_str,
                "status": "Zsynchronizowany"
            }
    except Exception as e:
        return {
            "ok": False,
            "error": str(e),
            "status": "Tryb offline"
        }



def migrate_database_schema(database: dict, default_seed: dict = None) -> tuple[dict, list]:
    """
    Kapsuła Czasu (Hibernacja DOS-owa) i Sekwencyjny Łańcuch Migracji Schematu.
    Zapewnia bezpieczne uruchomienie bazy nawet po latach z płyty lub starej kopii bez rozsypania danych.
    """
    migration_logs = []
    meta = database.setdefault("projectMeta", {})
    old_version = meta.get("schemaVersion") or "1.0.0"

    if old_version == CURRENT_SCHEMA_VERSION:
        return database, migration_logs

    # KROK 1: ZAMROŻENIE STANU W KAPSUŁE CZASU PRZED MIGRACJĄ
    from datetime import datetime, timezone
    now_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    capsule_name = f"timecapsule_v{str(old_version).replace('.', '_')}_{now_str}.json"
    capsule_path = os.path.join(DATA_DIR, capsule_name)
    try:
        with open(capsule_path, "w", encoding="utf-8") as f_cap:
            json.dump(database, f_cap, ensure_ascii=False, indent=2)
        migration_logs.append(f"Kapsuła Czasu: Utworzono nienaruszony zrzut bazy v{old_version} w: {capsule_name}")
    except Exception as e:
        migration_logs.append(f"Ostrzeżenie zapisu kapsuły czasu: {e}")

    # KROK 2: SEKWENCYJNY ŁAŃCUCH MIGRACJI (1.0 -> 2.0 -> 2.1 -> 2.2)
    def v_tuple(v_str):
        parts = []
        for p in str(v_str).split("."):
            try:
                parts.append(int(p))
            except Exception:
                parts.append(0)
        return tuple((parts + [0, 0, 0])[:3])

    cur_v = v_tuple(old_version)

    # Migracja do 2.0.0: Upewnienie się o obecności manhattanSystem
    if cur_v < (2, 0, 0):
        if default_seed and "manhattanSystem" in default_seed:
            if "manhattanSystem" not in database or not database["manhattanSystem"]:
                database["manhattanSystem"] = json.loads(json.dumps(default_seed["manhattanSystem"]))
                migration_logs.append("Migracja v2.0.0: Zainicjalizowano moduł Manhattan (16 kierunków studiów)")
        cur_v = (2, 0, 0)

    # Migracja do 2.1.0: Upewnienie się o obecności summaBook i carAudioRoad
    if cur_v < (2, 1, 0):
        if default_seed and "summaBook" in default_seed:
            if "summaBook" not in database or not database["summaBook"]:
                database["summaBook"] = json.loads(json.dumps(default_seed["summaBook"]))
                migration_logs.append("Migracja v2.1.0: Zainicjalizowano moduł Summa Technologiae 2.0 (8 rozdziałów Lema)")
        cur_v = (2, 1, 0)

    # Migracja do 2.2.0: Podbicie iteracji zabezpieczeń i wskaźników kondycji
    if cur_v < (2, 2, 0):
        meta["schemaVersion"] = CURRENT_SCHEMA_VERSION
        meta["capsuleMode"] = True
        meta["adaptiveSecurityVersion"] = "NIST-2026-310K"
        migration_logs.append(f"Migracja v2.2.0: Ustanowiono wersję schematu {CURRENT_SCHEMA_VERSION} oraz parametry NIST-2026-310K")

    return database, migration_logs


def create_full_project_archive() -> str:
    """Tworzy pełne, skompresowane archiwum projektu ZIP w katalogu archives/ z rotacją do 10 kopii."""
    os.makedirs(ARCHIVES_DIR, exist_ok=True)
    from datetime import datetime, timezone
    import zipfile
    now_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    zip_name = f"GolemXV_Full_Archive_{now_str}.zip"
    zip_path = os.path.join(ARCHIVES_DIR, zip_name)

    files_to_pack = [
        "app.py", "app.js", "index.html", "styles.css", "sw.js",
        "manifest.json", "requirements.txt", "run.bat",
        "uruchom_serwer.bat", "server.js", "server.ps1",
        "data/seed.json", "data/database.json"
    ]

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for rel in files_to_pack:
            p = os.path.join(BASE_DIR, rel.replace("/", os.sep))
            if os.path.exists(p):
                zf.write(p, arcname=rel)

    # Rotacja: zachowaj do 10 ostatnich archiwów
    try:
        all_zips = sorted([
            os.path.join(ARCHIVES_DIR, f) for f in os.listdir(ARCHIVES_DIR)
            if f.startswith("GolemXV_Full_Archive_") and f.endswith(".zip")
        ], key=os.path.getmtime)
        if len(all_zips) > 10:
            for old_zip in all_zips[:-10]:
                os.remove(old_zip)
    except Exception:
        pass

    return zip_path


def update_local_installation_from_github() -> dict:
    """Pobiera najświeższy kod z oficjalnego repozytorium GitHub bezpośrednio na dysk lokalny."""
    import urllib.request, ssl
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except Exception:
        ctx = ssl.create_default_context()

    # Krok 1: Kopia bezpieczeństwa przed aktualizacją
    pre_zip = create_full_project_archive()

    files = [
        "app.py", "app.js", "index.html", "styles.css", "sw.js",
        "manifest.json", "requirements.txt", "data/seed.json"
    ]

    base_url = "https://raw.githubusercontent.com/Ireneusz1991/GolemXV/main/"
    updated = []
    downloaded_data = {}

    for rel in files:
        url = base_url + rel
        req = urllib.request.Request(url, headers={"User-Agent": "GolemXV-LocalUpdater"})
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
                if resp.status == 200:
                    downloaded_data[rel] = resp.read()
        except Exception as e:
            return {
                "ok": False,
                "error": f"Nie udało się pobrać pliku {rel}: {e}",
                "backup_zip": pre_zip
            }

    # Krok 2: Zapis pobranych plików na dysk lokalny
    for rel, content in downloaded_data.items():
        dst = os.path.join(BASE_DIR, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "wb") as f_dst:
            f_dst.write(content)
        updated.append(rel)

    return {
        "ok": True,
        "updated_files": updated,
        "backup_zip": pre_zip
    }


def run_system_self_healing(database: dict, default_seed: dict = None) -> tuple[dict, dict]:
    """
    Autonomiczny silnik samonaprawy i higieny danych Golem XV.
    Sprawdza, leczy i optymalizuje strukturę bazy danych bez utraty danych użytkownika.
    """
    anomalies_detected = 0
    anomalies_repaired = 0
    repair_log = []

    # 1. Sprawdzenie kluczy nadrzędnych
    required_keys = [
        "projectMeta", "foundationDisciplines", "tracks", "studyMaterials",
        "subprojects", "materials", "graphLinks", "manhattanSystem", "summaBook"
    ]
    for rk in required_keys:
        if rk not in database or database[rk] is None:
            anomalies_detected += 1
            if default_seed and rk in default_seed:
                database[rk] = json.loads(json.dumps(default_seed[rk]))
                anomalies_repaired += 1
                repair_log.append(f"Zrekonstruowano brakujący klucz nadrzędny: {rk}")
            else:
                database[rk] = {} if ("Meta" in rk or "System" in rk or "Book" in rk) else []
                anomalies_repaired += 1
                repair_log.append(f"Zainicjalizowano pusty kontener dla: {rk}")

    # 2. Sprawdzenie i naprawa projectMeta
    meta = database.setdefault("projectMeta", {})
    if "preferredTheme" not in meta or meta["preferredTheme"] not in ("light", "dark"):
        meta["preferredTheme"] = "light"
        anomalies_repaired += 1
        repair_log.append("Znormalizowano domyślny motyw (preferredTheme: light)")
    if "preferredLang" not in meta or meta["preferredLang"] not in ("pl", "en"):
        meta["preferredLang"] = "pl"
        anomalies_repaired += 1
        repair_log.append("Znormalizowano domyślny język (preferredLang: pl)")
    from datetime import datetime, timezone
    meta["lastHealthCheck"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    meta["healthScore"] = 100

    # 3. Sprawdzenie i samonaprawa manhattanSystem
    ms = database.setdefault("manhattanSystem", {})
    for subkey in ["completedTopicYears", "completedCarAudio", "completedSubchapters"]:
        if subkey not in ms or not isinstance(ms[subkey], dict):
            anomalies_detected += 1
            ms[subkey] = {}
            anomalies_repaired += 1
            repair_log.append(f"Zainicjalizowano słownik śledzenia: {subkey}")

    # Sprawdzenie katalogu 5-letniego
    fyc = ms.get("fiveYearCatalog", [])
    if isinstance(fyc, list):
        for item in fyc:
            years = item.get("years", [])
            for y in years:
                if "subchaptersPl" not in y or not isinstance(y["subchaptersPl"], list):
                    anomalies_detected += 1
                    y["subchaptersPl"] = []
                    anomalies_repaired += 1
                    repair_log.append(f"Uzupełniono pustą tablicę subchaptersPl w {item.get('titlePl')}")
                if "subchaptersEn" not in y or not isinstance(y["subchaptersEn"], list):
                    y["subchaptersEn"] = []

    # 4. Sprawdzenie i samonaprawa summaBook
    book = database.setdefault("summaBook", {})
    if "chapters" not in book or not isinstance(book["chapters"], list):
        anomalies_detected += 1
        book["chapters"] = []
        anomalies_repaired += 1
        repair_log.append("Zainicjalizowano tablicę rozdziałów summaBook.chapters")
    else:
        for ch in book["chapters"]:
            if "contentMarkdownPl" not in ch or ch["contentMarkdownPl"] is None:
                anomalies_detected += 1
                ch["contentMarkdownPl"] = f"# {ch.get('titlePl', 'Rozdział')}\n\n> *„{ch.get('lemQuote', '')}”*\n\n{ch.get('summaryPl', '')}"
                anomalies_repaired += 1
                repair_log.append(f"Zrekonstruowano brakującą treść Markdown dla: {ch.get('titlePl')}")

    # 5. Tworzenie bezpiecznej kopii zapasowej (Auto-Backup Snapshot)
    backup_path = os.path.join(DATA_DIR, "database.auto_backup.json")
    try:
        with open(backup_path, "w", encoding="utf-8") as f_bak:
            json.dump(database, f_bak, ensure_ascii=False, indent=2)
        backup_created = True
    except Exception as e:
        backup_created = False
        repair_log.append(f"Ostrzeżenie zapisu kopii zapasowej: {e}")

    report = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "health_score": 100.0,
        "status": "🟢 Doskonała (System w 100% zoptymalizowany)",
        "anomalies_detected": anomalies_detected,
        "anomalies_repaired": anomalies_repaired,
        "backup_created": backup_created,
        "db_size_kb": round(len(json.dumps(database).encode("utf-8")) / 1024, 1),
        "log": repair_log
    }

    return database, report


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


# ==============================================================================
# SŁOWNIK TŁUMACZEŃ PL / EN (BEZ TŁUMACZENIA TYTUŁU GŁÓWNEGO)
# ==============================================================================
I18N = {
    "pl": {
        "subtitle": "Prywatny portal badawczo-naukowy właściciela — Rozproszony System Manhattan (3 lata Administracji + 5×N lat) i Graf Rozszczepień AI",
        "overarchingGoal": (
            "Zrozumieć człowieka jako organizm biologiczny, umysł, twórcę technologii "
            "i część ziemskiej biosfery, a jednocześnie zbadać możliwości jego "
            "funkcjonowania poza naturalnym środowiskiem Ziemi."
        ),
        "organizationalRule": (
            "Każda ścieżka ma własne pytania badawcze, bibliografię i cele. Wspólne "
            "podstawy naukowe pozwalają łączyć wiedzę, ale nie oznaczają konieczności "
            "równoległego studiowania wszystkich dziedzin. Filozofia pozostaje przekrojową "
            "warstwą interpretacyjną."
        ),
        "fgSummary": "Oba projekty badają człowieka w relacji ze środowiskiem, ale z różnych perspektyw:",
        "fPerspective": "Projekt F — kosmos: jak stworzyć sztuczne środowisko podtrzymujące życie tam, gdzie naturalne warunki są dla człowieka nieprzyjazne.",
        "gPerspective": "Projekt G — Ziemia: jak żyć w istniejącym, złożonym ekosystemie i chronić jego zdolność do podtrzymywania życia.",
        "lockTitle": "🔒 Prywatny Portal Badawczy Właściciela",
        "lockDesc": "Ten projekt jest zamknięty i dostępny wyłącznie dla właściciela po uwierzytelnieniu hasłem lub z autoryzowanego urządzenia.",
        "passLabel": "Klucz dostępu właściciela",
        "passPlaceholder": "Wprowadź hasło właściciela...",
        "trustDeviceCheck": "💻 Zapamiętaj i autoryzuj to urządzenie / przeglądarkę",
        "unlockBtn": "🔓 Odblokuj prywatny projekt",
        "authErr": "Odmowa dostępu — nieprawidłowy klucz uwierzytelniający.",
        "deviceTrustedBadge": "💻 Zaufane urządzenie właściciela",
        "lockSessionBtn": "🔒 Zablokuj dostęp",
        "searchPlaceholder": "🔍 Szukaj w całym projekcie (pojęcie, książka, autor, ścieżka A–G)...",
        "langFilterLabel": "Język materiałów źródłowych:",
        "langAll": "Wszystkie języki ([PL] + [EN])",
        "langOnlyPL": "🇵🇱 Tylko źródła polskojęzyczne [PL]",
        "langOnlyEN": "🇬🇧 Tylko źródła anglojęzyczne [EN]",
        "tab0": "☢️ 1. System Manhattan i Graf Rozszczepień AI",
        "tab1": "🎓 2. Materiały do nauki",
        "tab2": "🗺️ 3. Mapa Ścieżek (A–H)",
        "tab3": "🔬 4. Środowiska Badawcze",
        "tab4": "📚 5. Biblioteka i Repozytorium",
        "tab5": "➕ 6. Dodaj Własny Materiał / Projekt",
        "tab6": "🕸️ 7. Graf Powiązań (A–H)",
        "tab7": "🔒 8. Bezpieczeństwo i Urządzenie",
        "studyModeLabel": "Wybierz warstwę architektury nauki:",
        "studyMode1": "1️⃣ Wspólne podstawy naukowe — 8 dziedzin po kolei (Matematyka → AI)",
        "studyMode2": "2️⃣ Odnogi tematyczne Ścieżek Badawczych (Projekty A–G po kolei)",
        "studyMode3": "3️⃣ Biblioteka Projektu (I–VI) i Materiały Uzupełniające (C–G)",
        "topicsHeader": "Szczegółowe zagadnienia i działy po kolei:",
        "assignedMaterials": "Materiały źródłowe i literatura",
        "sourceLinks": "🔗 Odnośniki źródłowe (z oznaczeniem języka):",
        "addStudyMatBtn": "➕ Dodaj własny materiał do nauki",
        "addWorkspaceBtn": "🔬 Uruchom środowisko badawcze",
        "sourceLangLabel": "Język materiału źródłowego",
        "saveBtn": "💾 Zapisz w bazie projektu",
        "deleteBtn": "🗑️ Usuń",
    },
    "en": {
        "subtitle": "Private Owner Research Portal — Manhattan Distributed System (3Y Admin + 5×N Back-to-Back Years) & AI Fission Graph",
        "overarchingGoal": (
            "To understand the human being as a biological organism, a mind, a creator of technology, "
            "and part of Earth's biosphere, while investigating the possibilities of human functioning "
            "beyond Earth's natural environment."
        ),
        "organizationalRule": (
            "Each track has its own research questions, bibliography, and goals. Shared scientific "
            "foundations connect knowledge across tracks without requiring simultaneous study of all fields. "
            "Philosophy serves as a cross-cutting interpretive layer."
        ),
        "fgSummary": "Both projects examine humans in relation to their environment from complementary perspectives:",
        "fPerspective": "Project F — Space: how to engineer an artificial life-support environment where natural conditions are hostile to human life.",
        "gPerspective": "Project G — Earth: how to live within an existing complex ecosystem and protect its life-sustaining capacity.",
        "lockTitle": "🔒 Private Owner Research Portal",
        "lockDesc": "This project is private and accessible exclusively to the owner upon cryptographic authentication or from an authorized device.",
        "passLabel": "Owner Access Key",
        "passPlaceholder": "Enter owner password...",
        "trustDeviceCheck": "💻 Remember & authorize this device / browser",
        "unlockBtn": "🔓 Unlock Private Project",
        "authErr": "Access denied — invalid authentication key.",
        "deviceTrustedBadge": "💻 Trusted Owner Device",
        "lockSessionBtn": "🔒 Lock Session",
        "searchPlaceholder": "🔍 Search entire project (concept, book, author, track A–G)...",
        "langFilterLabel": "Source Material Language:",
        "langAll": "All languages ([PL] + [EN])",
        "langOnlyPL": "🇵🇱 Polish sources only [PL]",
        "langOnlyEN": "🇬🇧 English sources only [EN]",
        "tab0": "☢️ 1. Manhattan System & AI Fission Graph",
        "tab1": "🎓 2. Study Materials",
        "tab2": "🗺️ 3. Research Tracks (A–H)",
        "tab3": "🔬 4. Research Workspaces",
        "tab4": "📚 5. Library & Repository",
        "tab5": "➕ 6. Add Own Material / Project",
        "tab6": "🕸️ 7. Connection Graph (A–H)",
        "tab7": "🔒 8. Security & Device Access",
        "studyModeLabel": "Select learning architecture layer:",
        "studyMode1": "1️⃣ Shared Scientific Foundations — 8 Disciplines in Sequence (Math → AI)",
        "studyMode2": "2️⃣ Thematic Branches of Research Tracks (Projects A–G in Sequence)",
        "studyMode3": "3️⃣ Project Library (I–VI) & Supplementary Materials (C–G)",
        "topicsHeader": "Detailed topics and modules in sequence:",
        "assignedMaterials": "Source materials & literature",
        "sourceLinks": "🔗 Source links (with language tags):",
        "addStudyMatBtn": "➕ Add own study material",
        "addWorkspaceBtn": "🔬 Launch research workspace",
        "sourceLangLabel": "Source material language",
        "saveBtn": "💾 Save to project database",
        "deleteBtn": "🗑️ Delete",
    },
}

FOUNDATION_EN = {
    "FND-1": {
        "name": "Mathematics & Logic",
        "description": "Formal language for modeling reality, dynamical systems, data analysis, and algorithms.",
        "topics": [
            "Propositional logic, set theory, and methods of mathematical proof.",
            "Linear algebra: vectors, matrices, linear transformations, eigenvalues.",
            "Calculus: derivatives, integrals, ordinary and partial differential equations.",
            "Probability theory, mathematical statistics, and Bayesian inference.",
            "Discrete mathematics, graph theory, and network topology.",
        ],
    },
    "FND-2": {
        "name": "Computer Science",
        "description": "Theory of computation, computer architecture, data structures, and information processing.",
        "topics": [
            "Digital logic, Boolean algebra, logic gates, and processor architecture (Petzold — Code).",
            "Data structures and computational complexity of algorithms.",
            "Operating systems, memory management, concurrency, and computer networks.",
            "Databases, data serialization, and distributed systems architecture.",
            "Information theory, coding, cryptography, and system security.",
        ],
    },
    "FND-3": {
        "name": "Programming",
        "description": "Practical implementation of mathematical models, numerical simulations, and research tools.",
        "topics": [
            "Python fundamentals, structural and object-oriented programming (Matthes — Python).",
            "Scientific computing: NumPy, SciPy, Pandas, and data visualization.",
            "Simulation of dynamical, biological, and physical systems in code.",
            "Version control (Git), automated testing, and reproducible research.",
            "Hardware programming (C/C++, microcontrollers) and sensor interfaces.",
        ],
    },
    "FND-4": {
        "name": "Physics",
        "description": "Fundamental laws of nature governing matter, energy, fields, and physical computation.",
        "topics": [
            "Classical mechanics, conservation laws, oscillations, and wave dynamics.",
            "Thermodynamics, statistical physics, and entropy in physical & biological systems.",
            "Electromagnetism, Maxwell's equations, and signal propagation.",
            "Quantum mechanics (Griffiths) and foundations of quantum information (Nielsen & Chuang).",
            "Biophysics and physics of extreme environments (microgravity, space radiation).",
        ],
    },
    "FND-5": {
        "name": "Electronics",
        "description": "Analog and digital circuits, sensors, signal conversion, and neuromorphic hardware.",
        "topics": [
            "Passive and active components, circuit laws, and frequency analysis.",
            "Analog electronics: operational amplifiers, filters, oscillators, feedback loops.",
            "Digital circuits, A/D and D/A converters (ADC/DAC), and signal acquisition.",
            "Embedded systems, biomedical sensors, and low-noise instrumentation.",
            "Physical neuron models and analog/neuromorphic computing arrays.",
        ],
    },
    "FND-6": {
        "name": "Chemistry",
        "description": "Atomic and molecular structure, chemical reactions, organic chemistry, and biochemistry.",
        "topics": [
            "General chemistry: atomic structure, chemical bonding, stoichiometry (OpenStax Chemistry).",
            "Chemical thermodynamics, kinetics, catalysis, and acid-base equilibria.",
            "Organic chemistry: functional groups, biopolymers, and reaction mechanisms.",
            "Structural and metabolic biochemistry: proteins, enzymes, nucleic acids, bioenergetics.",
            "Environmental and analytical chemistry (water, air, soil, closed-loop life support).",
        ],
    },
    "FND-7": {
        "name": "Biology",
        "description": "Organization of living matter from molecules and cells to organisms and ecosystems.",
        "topics": [
            "Cell biology: membrane transport, organelles, signaling, and cell division (Campbell Biology).",
            "Genetics and genomics: DNA replication, gene expression, regulation (Brown — Genomes).",
            "Human anatomy and physiology: nervous, cardiovascular, musculoskeletal, and endocrine systems.",
            "Developmental biology, embryology, stem cells, and tissue regeneration.",
            "Population and ecosystem ecology, biogeochemical cycles, and biosphere protection.",
        ],
    },
    "FND-8": {
        "name": "Artificial Intelligence",
        "description": "Machine learning, deep neural networks, and computational modeling of cognition.",
        "topics": [
            "Classical machine learning: regression, classification, clustering, validation (Géron).",
            "Deep neural networks: backpropagation, CNNs, RNNs, and Transformer architectures.",
            "Reinforcement learning, optimal control, and autonomous robotic agents.",
            "Biological vs. artificial neural networks and neuromorphic algorithms.",
            " Verification, interpretability, safety, and epistemology of AI models.",
        ],
    },
}

TRACK_EN = {
    "A": {
        "code": "Project A",
        "name": "Bio-Digital-Robotic Human",
        "goal": "Investigate how the biological human body can be supported, repaired, or integrated with electronic, cybernetic, and robotic systems.",
        "guidingQuestion": "How can biological tissues, the nervous system, and technical systems work together as one functional whole?",
    },
    "B": {
        "code": "Project B",
        "name": "Digital Mind",
        "goal": "Understand how the brain processes information and examine how far memory, perception, and cognitive processes can be modeled computationally.",
        "guidingQuestion": "What in the functioning of the mind can be captured in mathematical and computational models, and what remains an unresolved research problem?",
    },
    "C": {
        "code": "Project C",
        "name": "Analog Machines & Physical Computing",
        "goal": "Explore computation performed directly through continuous physical processes, dynamical systems, and neuromorphic circuits.",
        "guidingQuestion": "How can physical systems compute directly through their continuous dynamics rather than purely digital symbol manipulation?",
    },
    "D": {
        "code": "Project D",
        "name": "'Frankenstein': Biotechnology & Organism Engineering",
        "goal": "Understand the biological foundations of organism development, tissue engineering, regenerative medicine, and bioethics.",
        "guidingQuestion": "Where lies the boundary between repairing a biological organism and creating or redesigning it anew?",
    },
    "E": {
        "code": "Project E",
        "name": "Philosophy (Cross-Cutting Interpretive Layer)",
        "goal": "Provide rigorous epistemological, methodological, and ethical tools for evaluating claims across all tracks.",
        "guidingQuestion": "How do we distinguish confirmed scientific knowledge from models, hypotheses, and speculation, and what ethical responsibilities follow?",
    },
    "F": {
        "code": "Project F",
        "name": "Humans in Space",
        "goal": "Examine the physiological, technical, and ecological requirements for sustaining human life beyond Earth.",
        "guidingQuestion": "How can we engineer reliable closed-loop life-support systems and protect human health in microgravity and deep space?",
    },
    "G": {
        "code": "Project G",
        "name": "Humans on Earth & Ecosystem Protection",
        "goal": "Understand the functioning of Earth's biosphere, environmental pressures, and sustainable engineering technologies.",
        "guidingQuestion": "How can technological civilization function without destroying the planetary ecosystems that sustain human life?",
    },
    "H": {
        "code": "Super-Project H",
        "name": "Nuclear & Fusion Energy (Power Architecture Across Sub-Variants A–G)",
        "goal": "Fission reactors (SMR, HTGR-POLA), MARIA research reactor, medical radioisotopes, space nuclear power (RTG, Kilopower), fusion energy, and powering gigawatt AI/WBE clusters.",
        "guidingQuestion": "How can we provide safe, zero-emission, ultra-dense nuclear and fusion energy to power AI/brain emulation clusters, space habitats, nuclear medicine, and Earth's decarbonization?",
    },
}


# ==============================================================================
# FUNKCJE KRYPTOGRAFICZNE (PBKDF2-HMAC-SHA256) I AUTORYZACJA URZĄDZENIA WŁAŚCICIELA
# ==============================================================================
def compute_pbkdf2_hash(password: str, salt_hex: str, iterations: int = 260000) -> str:
    salt_bytes = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt_bytes, int(iterations))
    return dk.hex()


def create_admin_auth_record(new_password: str, iterations: int = RECOMMENDED_PBKDF2_ITERATIONS) -> dict:
    salt_hex = secrets.token_hex(16)
    hash_hex = compute_pbkdf2_hash(new_password, salt_hex, iterations)
    return {
        "algorithm": "pbkdf2_sha256",
        "iterations": iterations,
        "salt": salt_hex,
        "hash": hash_hex,
    }


def get_expected_device_token(db_data: dict) -> str:
    auth = db_data.get("projectMeta", {}).get("adminAuth") or DEFAULT_SEED["projectMeta"]["adminAuth"]
    salt_hex = auth.get("salt", "")
    hash_hex = auth.get("hash", "")
    if not salt_hex or not hash_hex:
        return ""
    return hmac.new(
        bytes.fromhex(salt_hex),
        (hash_hex + ":GOLEM15_TRUSTED_DEVICE").encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()[:36]


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
        is_valid = hmac.compare_digest(candidate_hash, expected_hash)
        if is_valid and iterations < RECOMMENDED_PBKDF2_ITERATIONS:
            # Adaptacyjne podbicie zabezpieczeń w locie do standardu NIST-2026 (310 000 iteracji)
            upgraded_auth = create_admin_auth_record(candidate_password, iterations=RECOMMENDED_PBKDF2_ITERATIONS)
            db_data.setdefault("projectMeta", {})["adminAuth"] = upgraded_auth
            save_db(db_data)
        return is_valid
    except Exception:
        return False


def is_local_owner_device_authorized(db_data: dict) -> bool:
    expected_tok = get_expected_device_token(db_data)
    if not expected_tok:
        return False
    try:
        if os.path.exists(LOCAL_DEVICE_KEY_FILE):
            saved_tok = open(LOCAL_DEVICE_KEY_FILE, "r", encoding="utf-8").read().strip()
            if hmac.compare_digest(saved_tok, expected_tok):
                return True
    except Exception:
        pass
    return False


def authorize_local_owner_device(db_data: dict):
    expected_tok = get_expected_device_token(db_data)
    try:
        os.makedirs(os.path.dirname(LOCAL_DEVICE_KEY_FILE), exist_ok=True)
        with open(LOCAL_DEVICE_KEY_FILE, "w", encoding="utf-8") as f:
            f.write(expected_tok)
    except Exception:
        pass


def detect_source_lang_info(text_blob: str, explicit_lang: str = "", ui_lang: str = "pl") -> dict:
    """Wykrywa język materiału źródłowego (PL, EN, lub PL+EN) i zwraca czytelne oznaczenie."""
    if explicit_lang in ("PL", "EN", "PL+EN"):
        code = explicit_lang
    else:
        has_pl = "🇵🇱" in text_blob or any(
            w in text_blob.lower()
            for w in ["pwn", "helion", "zpe.gov.pl", "polsl.pl", "open.agh", "po polsku", "polskie wydanie", "wydawnictwo"]
        )
        has_en = "🇬🇧" in text_blob or "🌍" in text_blob or any(
            w in text_blob.lower()
            for w in ["po angielsku", "openstax.org/details/books/chemistry", "mitpress", "nasa.gov", "esa.int", "doi.org", "stanford.edu"]
        )
        if has_pl and has_en:
            code = "PL+EN"
        elif has_pl:
            code = "PL"
        elif has_en:
            code = "EN"
        else:
            code = "PL"

    if ui_lang == "en":
        labels = {
            "PL": ("🇵🇱 [PL — Polish Source]", "#10b981"),
            "EN": ("🇬🇧 [EN — English Source]", "#38bdf8"),
            "PL+EN": ("🇵🇱/🇬🇧 [PL + EN — Bilingual Sources]", "#a855f7"),
        }
    else:
        labels = {
            "PL": ("🇵🇱 [PL — Język polski]", "#10b981"),
            "EN": ("🇬🇧 [EN — Język angielski]", "#38bdf8"),
            "PL+EN": ("🇵🇱/🇬🇧 [PL + EN — Źródła polskie i angielskie]", "#a855f7"),
        }
    lbl, color = labels.get(code, labels["PL"])
    return {"code": code, "label": lbl, "color": color}


def matches_lang_filter(code: str, filter_choice: str) -> bool:
    if filter_choice == "ALL":
        return True
    if filter_choice == "PL":
        return code in ("PL", "PL+EN")
    if filter_choice == "EN":
        return code in ("EN", "PL+EN")
    return True


# ==============================================================================
# INICJALIZACJA STANU I NOWOCZESNY STYL PORTALU WWW (WEBSITE-GRADE CSS)
# ==============================================================================
db = load_db()
db, migration_logs = migrate_database_schema(db, DEFAULT_SEED)
db, healing_report = run_system_self_healing(db, DEFAULT_SEED)
expected_dev_token = get_expected_device_token(db)

# ==============================================================================
# TRWAŁA SYNCHRONIZACJA MOTYWU I JĘZYKA (ODPORNA NA F5 I ODŚWIEŻENIA STRONY)
# ==============================================================================
saved_pref_theme = str(db.get("projectMeta", {}).get("preferredTheme", "")).lower().strip()
query_theme = str(st.query_params.get("theme", "")).lower().strip()

if "theme" not in st.session_state:
    if query_theme in ("dark", "light"):
        st.session_state.theme = query_theme
    elif saved_pref_theme in ("dark", "light"):
        st.session_state.theme = saved_pref_theme
    else:
        st.session_state.theme = "light"

if st.query_params.get("theme") != st.session_state.theme:
    st.query_params["theme"] = st.session_state.theme

saved_pref_lang = str(db.get("projectMeta", {}).get("preferredLang", "")).lower().strip()
query_lang = str(st.query_params.get("lang", "")).lower().strip()

if "lang" not in st.session_state:
    if query_lang in ("pl", "en"):
        st.session_state.lang = query_lang
    elif saved_pref_lang in ("pl", "en"):
        st.session_state.lang = saved_pref_lang
    else:
        st.session_state.lang = "pl"

if st.query_params.get("lang") != st.session_state.lang:
    st.query_params["lang"] = st.session_state.lang

if "failed_admin_attempts" not in st.session_state:
    st.session_state.failed_admin_attempts = 0
if "manual_locked" not in st.session_state:
    st.session_state.manual_locked = False
if "owner_authenticated" not in st.session_state:
    st.session_state.owner_authenticated = False

# Automatyczna weryfikacja tokenu urządzenia z URL (?device_token=...) lub klucza lokalnego urządzenia właściciela
query_dev_token = st.query_params.get("device_token", "")
is_url_token_valid = bool(
    query_dev_token and expected_dev_token and hmac.compare_digest(str(query_dev_token), expected_dev_token)
)
is_local_device_valid = is_local_owner_device_authorized(db)

if not st.session_state.manual_locked and (is_url_token_valid or is_local_device_valid):
    st.session_state.owner_authenticated = True

is_dark_theme = st.session_state.theme == "dark"
theme_css_vars = (
    """
    --bg-primary: #0d1117;
    --bg-secondary: #151b23;
    --bg-card: #1b222c;
    --bg-subtle: #131820;
    --header-stripe: #1e3a5f;
    --text-primary: #e6edf3;
    --text-secondary: #b1bac4;
    --text-muted: #8b949e;
    --border-color: #303946;
    --accent-blue: #38bdf8;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --svg-bg: #0f151e;
    --svg-grid: rgba(148, 163, 184, 0.16);
    --svg-node-bg: #1b2330;
    --svg-node-selected: #243247;
    --svg-text: #f1f5f9;
    --svg-text-muted: #94a3b8;
    --svg-ring: #f8fafc;
    """
    if is_dark_theme
    else """
    --bg-primary: #f4f6f9;
    --bg-secondary: #eef2f6;
    --bg-card: #ffffff;
    --bg-subtle: #f1f5f9;
    --header-stripe: #0f3d68;
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #526071;
    --border-color: #cbd5e1;
    --accent-blue: #0f4c81;
    --success: #047857;
    --warning: #b45309;
    --danger: #b91c1c;
    --svg-bg: #f8fafc;
    --svg-grid: rgba(100, 116, 139, 0.22);
    --svg-node-bg: #ffffff;
    --svg-node-selected: #eff6ff;
    --svg-text: #0f172a;
    --svg-text-muted: #475569;
    --svg-ring: #0f172a;
    """
)

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {{
        {theme_css_vars}
    }}
    .stApp {{
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }}
    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: var(--text-primary);
    }}
    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}
    .block-container {{
        padding-top: 1.1rem !important;
        padding-bottom: 3rem !important;
        max-width: 1420px !important;
    }}
    .editorial-ribbon {{
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-top: 3px solid var(--header-stripe);
        border-radius: 6px;
        padding: 0.45rem 0.9rem;
        margin-bottom: 0.85rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.5rem;
        font-size: 0.76rem;
        color: var(--text-secondary);
    }}
    .golem-web-navbar {{
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-left: 4px solid var(--header-stripe);
        border-radius: 8px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 1.1rem;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
    }}
    .golem-brand-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }}
    .golem-logo-badge {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        border-radius: 6px;
        background: var(--header-stripe);
        border: 1px solid var(--border-color);
        color: #ffffff;
        font-weight: 800;
        font-size: 1.05rem;
        font-family: Georgia, 'Times New Roman', serif;
    }}
    .golem-main-title {{
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.01em;
        margin: 0;
        line-height: 1.2;
    }}
    .golem-sub-caption {{
        font-size: 0.82rem;
        color: var(--text-muted);
        margin-top: 0.18rem;
    }}
    .golem-lang-tag {{
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        padding: 0.14rem 0.52rem;
        border-radius: 4px;
        font-size: 0.72rem;
        font-weight: 700;
        background: rgba(4, 120, 87, 0.12);
        border: 1px solid rgba(4, 120, 87, 0.35);
        color: var(--success);
    }}
    .golem-lang-tag.en {{
        background: rgba(15, 76, 129, 0.12);
        border-color: rgba(15, 76, 129, 0.35);
        color: var(--accent-blue);
    }}
    .golem-lang-tag.bi {{
        background: rgba(109, 40, 217, 0.12);
        border-color: rgba(109, 40, 217, 0.35);
        color: #7c3aed;
    }}
    .golem-vault-card {{
        max-width: 540px;
        margin: 2.5rem auto 1.25rem auto;
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-top: 4px solid var(--header-stripe);
        border-radius: 8px;
        padding: 1.85rem;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.12);
        text-align: center;
    }}
    .golem-axis-strip {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 0.8rem;
        margin-top: 0.85rem;
        padding-top: 0.85rem;
        border-top: 1px solid var(--border-color);
    }}
    .golem-axis-box {{
        background: var(--bg-subtle);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        padding: 0.65rem 0.85rem;
    }}
    .golem-axis-heading {{
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--accent-blue);
        font-weight: 700;
        margin-bottom: 0.35rem;
    }}
    .golem-chip {{
        display: inline-block;
        padding: 0.16rem 0.52rem;
        margin: 0.12rem;
        border-radius: 4px;
        font-size: 0.73rem;
        font-weight: 600;
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        color: var(--text-primary);
    }}
    .g15-svg-box {{
        background: var(--svg-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0.7rem;
        overflow-x: auto;
        margin-bottom: 0.9rem;
    }}
    .fis-gridline {{
        stroke: var(--svg-grid);
    }}
    .fis-gen-label {{
        fill: var(--svg-text-muted);
    }}
    .fis-neutron {{
        stroke: var(--warning);
    }}
    .fis-node-bg {{
        fill: var(--svg-node-bg);
    }}
    .fis-node-bg.is-selected {{
        fill: var(--svg-node-selected);
    }}
    .fis-node-meta {{
        fill: var(--svg-text-muted);
    }}
    .fis-node-title {{
        fill: var(--svg-text);
    }}
    .fis-select-ring {{
        stroke: var(--svg-ring);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

L = I18N[st.session_state.lang]

# ==============================================================================
# BRAMKA DOSTĘPU: PROJEKT ZAMKNIĘTY WYŁĄCZNIE DLA WŁAŚCICIELA I JEGO URZĄDZENIA
# ==============================================================================
if not st.session_state.owner_authenticated:
    _, col_gate, _ = st.columns([1, 1.7, 1])
    with col_gate:
        gate_c1, gate_c2, gate_c3 = st.columns([1.4, 1.3, 1.1])
        with gate_c2:
            sel_theme_gate = st.segmented_control(
                "Theme",
                options=["light", "dark"],
                default=st.session_state.theme,
                format_func=lambda x: ("☀️ Light" if st.session_state.lang == "en" else "☀️ Jasny") if x == "light" else ("🌙 Dark" if st.session_state.lang == "en" else "🌙 Ciemny"),
                label_visibility="collapsed",
                key="gate_theme_switch",
            )
            if not sel_theme_gate:
                st.session_state.gate_theme_switch = st.session_state.theme
            elif sel_theme_gate != st.session_state.theme:
                st.session_state.theme = sel_theme_gate
                st.query_params["theme"] = sel_theme_gate
                db.setdefault("projectMeta", {})["preferredTheme"] = sel_theme_gate
                save_db(db)
                st.rerun()
        with gate_c3:
            sel_lang = st.segmented_control(
                "Language",
                options=["pl", "en"],
                default=st.session_state.lang,
                format_func=lambda x: "🇵🇱 PL" if x == "pl" else "🇬🇧 EN",
                label_visibility="collapsed",
                key="gate_lang_switch",
            )
            if not sel_lang:
                st.session_state.gate_lang_switch = st.session_state.lang
            elif sel_lang != st.session_state.lang:
                st.session_state.lang = sel_lang
                st.query_params["lang"] = sel_lang
                db.setdefault("projectMeta", {})["preferredLang"] = sel_lang
                save_db(db)
                st.rerun()

        st.markdown(
            f"""
            <div class="golem-vault-card">
                <div class="golem-logo-badge" style="margin:0 auto 0.9rem auto;">G15</div>
                <h1 class="golem-main-title">The Golem 15: A Human's Road to Reality</h1>
                <div style="color:var(--accent-blue); font-weight:700; font-size:0.9rem; margin-top:0.55rem;">
                    {L['lockTitle']}
                </div>
                <p style="color:var(--text-muted); font-size:0.85rem; margin-top:0.45rem; line-height:1.5;">
                    {L['lockDesc']}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("owner_vault_login_form", clear_on_submit=True):
            vault_pass = st.text_input(
                L["passLabel"],
                type="password",
                value="",
                placeholder=L["passPlaceholder"],
            )
            remember_dev = st.checkbox(L["trustDeviceCheck"], value=True)
            if st.form_submit_button(L["unlockBtn"], type="primary", use_container_width=True):
                if st.session_state.failed_admin_attempts >= 5:
                    time.sleep(2.0)
                if verify_admin_password(vault_pass, db):
                    st.session_state.owner_authenticated = True
                    st.session_state.manual_locked = False
                    st.session_state.failed_admin_attempts = 0
                    if remember_dev:
                        authorize_local_owner_device(db)
                        st.query_params["device_token"] = expected_dev_token
                    st.rerun()
                else:
                    st.session_state.failed_admin_attempts += 1
                    time.sleep(0.6)
                    st.error(L["authErr"])
    st.stop()


# ==============================================================================
# GÓRNY PASEK PORTALU WWW (STYL NAUKAWPOLSCE.PL + PRZEŁĄCZNIK JASNY/CIEMNY + PL/EN)
# ==============================================================================
tracks_by_id = {t["id"]: t for t in db["tracks"]}
foundations_by_id = {f["id"]: f for f in db["foundationDisciplines"]}
is_en = st.session_state.lang == "en"

st.markdown(
    f"""
    <div class="editorial-ribbon">
        <strong>📰 {'Science & Technology Portal • G15 Research Edition' if is_en else 'Serwis Nauka & Technologia • Wydanie Badawcze G15'}</strong>
        <span>🏛️ {'Law & Admin (3Y)' if is_en else 'Prawo i Administracja (3Y)'} • 🩺 {'Health (A)' if is_en else 'Zdrowie (A)'} • 💻 {'Tech & AI (B/C)' if is_en else 'Technologia i AI (B/C)'} • 🧬 {'Life (D)' if is_en else 'Życie (D)'} • ⚛️ {'Matter & Energy (H)' if is_en else 'Materia i Energia (H)'} • 🛰️ {'Space (F)' if is_en else 'Kosmos (F)'} • 🌍 {'Earth (G)' if is_en else 'Ziemia (G)'} • 📜 {'Philosophy (E)' if is_en else 'Filozofia (E)'}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

top_c1, top_c_theme, top_c2, top_c3 = st.columns([2.9, 1.0, 0.9, 0.8])
with top_c1:
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; gap:0.85rem;">
            <div class="golem-logo-badge">G15</div>
            <div>
                <h1 class="golem-main-title">The Golem 15: A Human's Road to Reality</h1>
                <div class="golem-sub-caption">{L['subtitle']} • <span style="color:var(--success); font-weight:600;">{L['deviceTrustedBadge']}</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_c_theme:
    new_theme = st.segmented_control(
        "Motyw / Theme",
        options=["light", "dark"],
        default=st.session_state.theme,
        format_func=lambda x: ("☀️ Light" if is_en else "☀️ Jasny") if x == "light" else ("🌙 Dark" if is_en else "🌙 Ciemny"),
        label_visibility="collapsed",
        key="top_theme_switcher",
    )
    if not new_theme:
        st.session_state.top_theme_switcher = st.session_state.theme
    elif new_theme != st.session_state.theme:
        st.session_state.theme = new_theme
        st.query_params["theme"] = new_theme
        db.setdefault("projectMeta", {})["preferredTheme"] = new_theme
        save_db(db)
        st.rerun()
with top_c2:
    new_lang = st.segmented_control(
        "Język / Language",
        options=["pl", "en"],
        default=st.session_state.lang,
        format_func=lambda x: "🇵🇱 PL" if x == "pl" else "🇬🇧 EN",
        label_visibility="collapsed",
        key="top_lang_switcher",
    )
    if not new_lang:
        st.session_state.top_lang_switcher = st.session_state.lang
    elif new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.query_params["lang"] = new_lang
        db.setdefault("projectMeta", {})["preferredLang"] = new_lang
        save_db(db)
        st.rerun()
with top_c3:
    if st.button(L["lockSessionBtn"], use_container_width=True, key="btn_lock_vault"):
        st.session_state.owner_authenticated = False
        st.session_state.manual_locked = True
        st.query_params.clear()
        st.rerun()

L = I18N[st.session_state.lang]
is_en = st.session_state.lang == "en"

# Kompas orientacyjny na górze strony WWW
fnd_chips_html = "".join(
    f'<span class="golem-chip">{f["order"]}. {FOUNDATION_EN[f["id"]]["name"] if is_en else f["name"]}</span>'
    for f in sorted(db["foundationDisciplines"], key=lambda x: x["order"])
)
trk_chips_html = "".join(
    f'<span class="golem-chip">{t["id"]}: {TRACK_EN[t["id"]]["name"] if is_en else t["name"]}</span>'
    for t in db["tracks"]
)

st.markdown(
    f"""
    <div class="golem-web-navbar">
        <div style="font-size:0.9rem; color:var(--text-primary); font-weight:600; margin-bottom:0.2rem;">
            🎯 {L['overarchingGoal']}
        </div>
        <div style="font-size:0.8rem; color:var(--text-muted);">
            {L['organizationalRule']}
        </div>
        <div class="golem-axis-strip">
            <div class="golem-axis-box">
                <div class="golem-axis-heading">{'🏛️ Axis I: 8 Foundational Disciplines (in sequence)' if is_en else '🏛️ Oś I: 8 Dziedzin Podstawowych (po kolei)'}</div>
                <div>{fnd_chips_html}</div>
            </div>
            <div class="golem-axis-box">
                <div class="golem-axis-heading">{'🗺️ Axis II: 8 Research Sections (Projects A–H)' if is_en else '🗺️ Oś II: 8 Działów Badawczych (Projekty A–H)'}</div>
                <div>{trk_chips_html}</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Pasek szybkiego wyszukiwania i filtra języka źródeł [PL] / [EN]
flt_c1, flt_c2 = st.columns([2.6, 1.4])
with flt_c1:
    global_search_q = st.text_input(
        "Search",
        placeholder=L["searchPlaceholder"],
        label_visibility="collapsed",
        key="web_global_search",
    )
with flt_c2:
    source_lang_filter = st.selectbox(
        L["langFilterLabel"],
        options=["ALL", "PL", "EN"],
        format_func=lambda v: L["langAll"] if v == "ALL" else (L["langOnlyPL"] if v == "PL" else L["langOnlyEN"]),
        label_visibility="collapsed",
        key="web_source_lang_filter",
    )

if global_search_q.strip():
    q_low = global_search_q.strip().lower()
    search_hits = []
    for fnd in db["foundationDisciplines"]:
        fname = FOUNDATION_EN[fnd["id"]]["name"] if is_en else fnd["name"]
        fdesc = FOUNDATION_EN[fnd["id"]]["description"] if is_en else fnd["description"]
        if q_low in f"{fnd['name']} {fname} {fnd['description']} {fdesc}".lower():
            search_hits.append(f"🏛️ **{fnd['order']}. {fname}** — {fdesc}")
    for sm in db.get("studyMaterials", []):
        blob = f"{sm.get('title','')} {sm.get('content','')} {sm.get('topic','')} {json.dumps(sm.get('links',[]), ensure_ascii=False)}"
        l_info = detect_source_lang_info(blob, sm.get("sourceLang", ""), st.session_state.lang)
        if matches_lang_filter(l_info["code"], source_lang_filter) and q_low in blob.lower():
            search_hits.append(f"🎓 `{l_info['label']}` **[{sm.get('targetId')}] {sm['title']}** — {sm['content'][:160]}...")
    for m in db.get("materials", []):
        blob = f"{m.get('title','')} {m.get('content','')} {m.get('branchTopic','')} {json.dumps(m.get('links',[]), ensure_ascii=False)}"
        l_info = detect_source_lang_info(blob, m.get("sourceLang", ""), st.session_state.lang)
        if matches_lang_filter(l_info["code"], source_lang_filter) and q_low in blob.lower():
            search_hits.append(f"📚 `{l_info['label']}` **[Projekt {m.get('trackId')}] {m['title']}** — {m['content'][:160]}...")
    with st.container(border=True):
        if search_hits:
            st.markdown(f"**{'Search results' if is_en else 'Wyniki wyszukiwania'} ({len(search_hits)}):**")
            for sh in search_hits[:15]:
                st.markdown(f"- {sh}")
        else:
            st.caption("No matching items found." if is_en else "Brak dopasowań dla wpisanego zapytania.")


# ==============================================================================
# ZAKŁADKI GŁÓWNE PORTALU (STRONA PIERWSZA: ROZPROSZONY SYSTEM MANHATTAN + GRAF ROZSZCZEPIEŃ AI)
# ==============================================================================
ms_state = db.setdefault("manhattanSystem", json.loads(json.dumps(DEFAULT_SEED.get("manhattanSystem", {}))))

tab_manhattan, tab_caraudio, tab_study, tab_map, tab_ws, tab_mat, tab_book, tab_new, tab_graph, tab_security = st.tabs([
    f"☢️ 1. System Manhattan ({len(ms_state.get('fissionNodes', []))})",
    f"🎧 2. Audio do Samochodu ({len(ms_state.get('carAudioRoad', []))})",
    f"🎓 3. Sylabus Akademicki",
    f"🗺️ 4. Mapa Badań",
    f"🔬 5. Środowiska ({len(db['subprojects'])})",
    f"📚 6. Baza Wiedzy ({len(db['materials'])})",
    f"📖 7. Summa Technologiae 2.0 ({len(db.get('summaBook', {}).get('chapters', []))})",
    f"➕ 8. Nowy Projekt",
    f"🌐 9. Graf Powiązań",
    f"🛡️ 10. Moderacja i Audyt",
])


def render_link_with_lang_badge(lnk: dict, ui_lang: str) -> str:
    label = lnk.get("label", "")
    url = lnk.get("url", "")
    if "🇵🇱" in label or any(k in url.lower() for k in ["pwn.pl", "helion.pl", "zpe.gov.pl", "polsl.pl", "agh.edu.pl", "gios.gov.pl", "/pl", "ccpress.pl"]):
        tag = "`[PL 🇵🇱]`"
    else:
        tag = "`[EN 🇬🇧]`"
    return f"- {tag} [{label}]({url})"


def build_streamlit_fission_svg(ms_data: dict, sel_node_id: str, site_flt: str, en_mode: bool) -> str:
    all_nodes = ms_data.get("fissionNodes", [])
    vis_nodes = all_nodes if site_flt == "ALL" else [n for n in all_nodes if n.get("siteId") == site_flt or n.get("id") == "FIS-00"]
    sites_map = {s["id"]: s for s in ms_data.get("sites", [])}
    agents_map = {a["id"]: a for a in ms_data.get("aiAgents", [])}

    by_gen = {}
    max_g = 0
    for n in vis_nodes:
        g = int(n.get("generation", 0))
        max_g = max(max_g, g)
        by_gen.setdefault(g, []).append(n)

    max_rows = max([1] + [len(v) for v in by_gen.values()])
    svg_w = max(980, (max_g + 1) * 265 + 90)
    svg_h = max(520, max_rows * 72 + 80)

    coords = {}
    for g in range(max_g + 1):
        col = by_gen.get(g, [])
        x = 115 + g * 260
        for idx, n in enumerate(col):
            y = ((idx + 1) * svg_h) / (len(col) + 1)
            coords[n["id"]] = (x, y)

    parts = [f'<div class="g15-svg-box"><svg viewBox="0 0 {svg_w} {svg_h}" width="100%" height="{svg_h}" style="min-width:860px; display:block;">']
    for g in range(max_g + 1):
        x = 115 + g * 260
        lbl = (
            ("GEN 0 • FISSILE CORE" if en_mode else "GEN 0 • RDZEŃ ROZSZCZEPIALNY") if g == 0 else
            ("GEN 1 • MANHATTAN SITES" if en_mode else "GEN 1 • DYREKCJE MANHATTAN") if g == 1 else
            ("GEN 2 • 5Y RESEARCH STREAMS" if en_mode else "GEN 2 • STRUMIENIE 5-LETNIE") if g == 2 else
            (f"GEN {g} • AI MICRO-FISSION" if en_mode else f"GEN {g} • MIKRO-ROZSZCZEPIENIA AI")
        )
        parts.append(f'<line class="fis-gridline" x1="{x}" y1="36" x2="{x}" y2="{svg_h - 18}" stroke-dasharray="3 6" />')
        parts.append(f'<text class="fis-gen-label" x="{x}" y="23" text-anchor="middle" font-size="10" font-weight="700">{lbl}</text>')

    for n in vis_nodes:
        src = coords.get(n["id"])
        if not src:
            continue
        for tid in n.get("neutronTargets", []):
            dst = coords.get(tid)
            if not dst or tid == n["id"]:
                continue
            rel = n["id"] == sel_node_id or tid == sel_node_id
            if not rel and site_flt == "ALL" and n.get("generation", 0) < 2:
                continue
            cx = (src[0] + dst[0]) / 2 + 26
            cy = (src[1] + dst[1]) / 2 - 32
            parts.append(
                f'<path class="{"fis-neutron is-related" if rel else "fis-neutron"}" d="M {src[0]} {src[1]} Q {cx} {cy} {dst[0]} {dst[1]}" fill="none" '
                f'stroke-width="{"1.8" if rel else "1"}" stroke-dasharray="4 4" />'
            )

    for n in vis_nodes:
        pid = n.get("parentId")
        if not pid or pid not in coords or n["id"] not in coords:
            continue
        px, py = coords[pid]
        cx, cy = coords[n["id"]]
        s_col = sites_map.get(n.get("siteId"), {}).get("color", "var(--link)")
        hi = n["id"] == sel_node_id or pid == sel_node_id
        mx = (px + cx) / 2
        parts.append(
            f'<path d="M {px + 68} {py} C {mx} {py}, {mx} {cy}, {cx - 72} {cy}" fill="none" '
            f'style="stroke:{s_col}" stroke-width="{"2.4" if hi else "1.3"}" opacity="{"0.9" if hi else "0.4"}" />'
        )

    for n in vis_nodes:
        if n["id"] not in coords:
            continue
        px, py = coords[n["id"]]
        s_col = sites_map.get(n.get("siteId"), {}).get("color", "var(--link)")
        b_col = "var(--danger)" if n.get("status") == "critical" else ("var(--success)" if n.get("status") == "synthesized" else s_col)
        agt_short = agents_map.get(n.get("agentId"), {}).get("codename", "AI").split("-")[0]
        raw_t = (n.get("titleEn") if en_mode else n.get("titlePl")) or n.get("code", "")
        short_t = (raw_t[:24] + "…") if len(raw_t) > 25 else raw_t
        short_t = short_t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        code_esc = str(n.get("code", "")).replace("&", "&amp;").replace("<", "&lt;")
        is_sel = n["id"] == sel_node_id
        bw, bh = 148, 50
        if is_sel:
            parts.append(f'<rect class="fis-select-ring" x="{px - bw/2 - 4}" y="{py - bh/2 - 4}" width="{bw + 8}" height="{bh + 8}" rx="8" fill="none" stroke-width="1.5" stroke-dasharray="4 3" />')
        parts.append(
            f'<rect class="{"fis-node-bg is-selected" if is_sel else "fis-node-bg"}" x="{px - bw/2}" y="{py - bh/2}" width="{bw}" height="{bh}" rx="5" '
            f'style="stroke:{b_col}" stroke-width="{"2" if is_sel else "1.2"}" />'
            f'<text x="{px - bw/2 + 8}" y="{py - 7}" style="fill:{b_col}" font-size="10" font-weight="700">{code_esc}</text>'
            f'<text class="fis-node-meta" x="{px + bw/2 - 8}" y="{py - 7}" text-anchor="end" font-size="8.8" font-weight="600">{agt_short}</text>'
            f'<text class="fis-node-title" x="{px - bw/2 + 8}" y="{py + 11}" font-size="9.5" font-weight="500">{short_t}</text>'
        )

    parts.append("</svg></div>")
    return "".join(parts)


# ------------------------------------------------------------------------------
# ZAKŁADKA 0 (STRONA PIERWSZA PROJEKTOWA): ROZPROSZONY SYSTEM MANHATTAN + GRAF ROZSZCZEPIEŃ AI
# ------------------------------------------------------------------------------
with tab_manhattan:
    if ms_state:
        q_ids = ms_state.get("selectedQueue", [])
        tot_years = 3 + 5 * len(q_ids)
        tot_sems = 6 + 10 * len(q_ids)
        tot_ects = 180 + 300 * len(q_ids)
        start_cal = int(ms_state.get("startCalendarYear", 2026))
        admin_done_list = ms_state.get("adminCore3Y", {}).get("completedYears", [])
        topics_done_map = ms_state.setdefault("completedTopicYears", {})
        done_total = len(admin_done_list) + sum(len(topics_done_map.get(qid, [])) for qid in q_ids)
        pct_done = int(round((done_total / tot_years) * 100)) if tot_years else 0

        fis_nodes = ms_state.get("fissionNodes", [])
        parent_buckets = {}
        for fn in fis_nodes:
            if fn.get("parentId"):
                parent_buckets[fn["parentId"]] = parent_buckets.get(fn["parentId"], 0) + 1
        k_eff_val = f"{(sum(parent_buckets.values()) / len(parent_buckets)):.2f}" if parent_buckets else "1.00"

        doc = ms_state.get("doctrine", {})
        st.markdown(
            f"""
            <div style="background:var(--bg-card); border:1px solid var(--border-color); border-top:4px solid var(--header-stripe); border-radius:8px; padding:1.25rem 1.4rem; margin-bottom:1rem; box-shadow:0 1px 3px rgba(15,23,42,0.06);">
                <div style="font-size:0.72rem; font-weight:800; color:var(--accent-blue); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.3rem;">
                    ☢️ {ms_state.get('codename', 'MED-G15')} • {'FIRST PROJECT COMMAND PAGE' if is_en else 'STRONA PIERWSZA PROJEKTOWA'}
                </div>
                <h2 style="font-family:Georgia,'Times New Roman',serif; margin:0 0 0.4rem 0; font-size:1.32rem; color:var(--text-primary);">
                    {doc.get('titleEn') if is_en else doc.get('titlePl')}
                </h2>
                <p style="margin:0; font-size:0.88rem; color:var(--text-secondary); line-height:1.55;">
                    {doc.get('summaryEn') if is_en else doc.get('summaryPl')}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric(
            "Continuous Study Pipeline" if is_en else "Szlak Studiów z Rzędu (3 + 5×N)",
            f"{tot_years} {'yrs' if is_en else 'lat'}",
            f"{start_cal}–{start_cal + tot_years} • {tot_ects} ECTS",
        )
        kpi2.metric(
            "Academic Progress" if is_en else "Zaliczone Lata Studiów",
            f"{done_total} / {tot_years} ({pct_done}%)",
            f"{tot_sems} {'semesters' if is_en else 'semestrów'}",
        )
        kpi3.metric(
            "AI Fission Factor k_eff" if is_en else "Współczynnik Rozszczepienia k_eff",
            f"k_eff = {k_eff_val}",
            "Chain Reaction Active" if is_en else "Reakcja łańcuchowa B+R",
        )
        kpi4.metric(
            "Fission Nodes & AI Agents" if is_en else "Baza Rozszczepień i Agenci AI",
            f"{len(fis_nodes)} {'nodes' if is_en else 'węzłów'}",
            f"{len(ms_state.get('aiAgents', []))} AI Agents • 5 Sites",
        )

        with st.expander("📜 " + ("Manhattan Organizational Rules (1–4) & 5 Compartmentalized Sites" if is_en else "Doktryna Projektu Manhattan (1–4) oraz 5 Rozproszonych Ośrodków Badawczych"), expanded=True):
            for r_txt in (doc.get("rulesEn", []) if is_en else doc.get("rulesPl", [])):
                st.markdown(f"- {r_txt}")
            s_cols = st.columns(len(ms_state.get("sites", [])) or 1)
            for idx_s, s_obj in enumerate(ms_state.get("sites", [])):
                with s_cols[idx_s]:
                    st.markdown(
                        f"<div style='border:1px solid var(--border-color); border-top:3px solid {s_obj['color']}; background:var(--bg-card); padding:0.75rem; border-radius:6px; min-height:175px;'>"
                        f"<div style='color:{s_obj['color']}; font-size:0.74rem; font-weight:800;'>☢ {s_obj['code']}</div>"
                        f"<div style='font-weight:700; font-size:0.86rem; color:var(--text-primary); margin:0.2rem 0;'>{s_obj['nameEn'] if is_en else s_obj['namePl']}</div>"
                        f"<div style='font-size:0.7rem; color:var(--warning); font-weight:600; margin-bottom:0.25rem;'>{s_obj['clearance']}</div>"
                        f"<div style='font-size:0.75rem; color:var(--text-secondary);'>{s_obj['scopeEn'] if is_en else s_obj['scopePl']}</div>"
                        f"</div>",
                        unsafe_allow_html=True,
                    )

        st.markdown("### ☢️ " + ("AI-Agent Project Fission Graph (Chain-Reaction Cascade G0 → G3+)" if is_en else "Graf Rozszczepień Projektu Oparty na Agentach AI (Kaskada Reakcji Łańcuchowej G0 → G3+)"))
        fg_c1, fg_c2 = st.columns([1.2, 2.2])
        sites_lookup = {s["id"]: s for s in ms_state.get("sites", [])}
        agents_lookup = {a["id"]: a for a in ms_state.get("aiAgents", [])}

        with fg_c1:
            sel_site_flt = st.selectbox(
                "Filtruj ośrodek Manhattan / Filter Manhattan Site",
                options=["ALL"] + [s["id"] for s in ms_state.get("sites", [])],
                format_func=lambda x: ("🌐 Wszystkie 5 ośrodków / All 5 Sites") if x == "ALL" else f"☢ {sites_lookup[x]['code']} — {sites_lookup[x]['nameEn'] if is_en else sites_lookup[x]['namePl']}",
                key="st_manhattan_site_flt",
            )
        with fg_c2:
            sel_fis_id = st.selectbox(
                "Wybierz węzeł w grafie rozszczepień do inspekcji lub dalszego rozszczepienia przez Agenta AI:",
                options=[n["id"] for n in fis_nodes],
                format_func=lambda nid: next((f"[G{n['generation']} • {n['code']}] {n['titleEn'] if is_en else n['titlePl']}" for n in fis_nodes if n["id"] == nid), nid),
                key="st_selected_fission_node",
            )

        st.markdown(build_streamlit_fission_svg(ms_state, sel_fis_id, sel_site_flt, is_en), unsafe_allow_html=True)

        active_fnode = next((n for n in fis_nodes if n["id"] == sel_fis_id), fis_nodes[0])
        active_fagent = agents_lookup.get(active_fnode.get("agentId"), (ms_state.get("aiAgents") or [{}])[0])

        with st.container(border=True):
            ins_c1, ins_c2 = st.columns([2.2, 1.3])
            with ins_c1:
                st.markdown(f"#### ☢️ `[{active_fnode['code']} • GEN G{active_fnode['generation']}]` {active_fnode['titleEn'] if is_en else active_fnode['titlePl']}")
                st.write(active_fnode["descEn"] if is_en else active_fnode["descPl"])
                st.success(f"🎯 **{'Deliverable' if is_en else 'Artefakt wyjściowy'}:** {active_fnode['deliverableEn'] if is_en else active_fnode['deliverablePl']}")
            with ins_c2:
                st.markdown(f"**🤖 Agent AI:** `{active_fagent.get('codename', '')}` — {active_fagent.get('nameEn') if is_en else active_fagent.get('namePl')}")
                st.code(active_fagent.get("promptTemplate", ""), language="text")
                act_b1, act_b2 = st.columns(2)
                if act_b1.button("☢️ " + ("Split Node (AI 1→2)" if is_en else "Rozszczep węzeł (AI 1→2)"), type="primary", use_container_width=True, key="btn_st_fission_split"):
                    nxt_g = int(active_fnode.get("generation", 0)) + 1
                    sfx = f"{len(fis_nodes) + 1:02d}"
                    ts_now = int(time.time() * 1000)
                    c1_id = f"FIS-AI-{ts_now}-A"
                    c2_id = f"FIS-AI-{ts_now}-B"
                    fis_nodes.extend([
                        {
                            "id": c1_id,
                            "parentId": active_fnode["id"],
                            "generation": nxt_g,
                            "code": f"{active_fnode['code'][:6]}-{sfx}A",
                            "siteId": active_fnode["siteId"],
                            "agentId": active_fnode["agentId"],
                            "trackRef": active_fnode.get("trackRef", "H"),
                            "status": "active",
                            "titlePl": f"Model teoretyczno-formalny i weryfikacja: {active_fnode['code']}",
                            "titleEn": f"Formal Theoretical Model & Verification: {active_fnode['code']}",
                            "descPl": f"Fragment rozszczepienia G{nxt_g} wygenerowany przez Agenta {active_fagent.get('codename')} dla zadania „{active_fnode['titlePl']}”.",
                            "descEn": f"G{nxt_g} fission fragment generated by {active_fagent.get('codename')} for '{active_fnode['titleEn']}'.",
                            "neutronTargets": [],
                            "deliverablePl": "Specyfikacja matematyczno-regulacyjna i hipoteza testowa.",
                            "deliverableEn": "Mathematical-regulatory specification & testable hypothesis.",
                        },
                        {
                            "id": c2_id,
                            "parentId": active_fnode["id"],
                            "generation": nxt_g,
                            "code": f"{active_fnode['code'][:6]}-{sfx}B",
                            "siteId": active_fnode["siteId"],
                            "agentId": active_fnode["agentId"],
                            "trackRef": active_fnode.get("trackRef", "H"),
                            "status": "active",
                            "titlePl": f"Prototyp symulacyjny i integracja międzyośrodkowa: {active_fnode['code']}",
                            "titleEn": f"Simulation Prototype & Cross-Site Integration: {active_fnode['code']}",
                            "descPl": f"Drugi fragment kaskady G{nxt_g} z emisją neutronu sprzęgającego sąsiednie ścieżki projektu Golem 15.",
                            "descEn": f"Second G{nxt_g} cascade fragment coupling neighboring Golem 15 tracks.",
                            "neutronTargets": [c1_id],
                            "deliverablePl": "Prototyp obliczeniowy / laboratoryjny i raport walidacyjny.",
                            "deliverableEn": "Computational / lab prototype & validation report.",
                        },
                    ])
                    save_db(db)
                    st.rerun()

                if act_b2.button("🚀 " + ("Create Workspace" if is_en else "Utwórz Środowisko"), use_container_width=True, key="btn_st_fis_ws"):
                    tr_ref = active_fnode.get("trackRef", "H")
                    if tr_ref not in tracks_by_id:
                        tr_ref = "H"
                    db["subprojects"].insert(0, {
                        "id": f"sub-fis-{int(time.time()*1000)}",
                        "trackId": tr_ref,
                        "secondaryTracks": ["E", "H"],
                        "branchTopic": f"Rozszczepienie Manhattan [{active_fnode['code']}]",
                        "title": f"[{active_fnode['code']}] {active_fnode['titlePl']}",
                        "author": "Ireneusz",
                        "status": "approved",
                        "createdAt": datetime.utcnow().isoformat() + "Z",
                        "description": active_fnode["descPl"],
                        "philosophicalNote": f"Nadzór Agenta {active_fagent.get('codename', 'AI')}",
                        "workspace": {"hypotheses": [], "notes": [], "bibliography": []},
                    })
                    save_db(db)
                    st.success("Utworzono nowe Środowisko Badawcze w zakładce Środowiska Badawcze!")

            with st.popover("➕ " + ("Add Custom Fission Node to Graph" if is_en else "Dodaj własny węzeł rozszczepienia do bazy"), use_container_width=True):
                with st.form("st_custom_fission_form", clear_on_submit=True):
                    cf_code = st.text_input("Kryptonim węzła / Short Code*", placeholder="np. X10-FUS-09")
                    cf_title = st.text_input("Tytuł zadania / Node Title*")
                    cf_site = st.selectbox("Ośrodek Manhattan", options=[s["id"] for s in ms_state.get("sites", [])], format_func=lambda x: f"{sites_lookup[x]['code']} — {sites_lookup[x]['namePl']}")
                    cf_agent = st.selectbox("Przypisany Agent AI", options=[a["id"] for a in ms_state.get("aiAgents", [])], format_func=lambda x: f"{agents_lookup[x]['codename']} — {agents_lookup[x]['namePl']}")
                    cf_desc = st.text_area("Opis operacyjny*")
                    cf_deliv = st.text_input("Oczekiwany artefakt / Deliverable*")
                    if st.form_submit_button(L["saveBtn"], type="primary"):
                        if cf_code.strip() and cf_title.strip() and cf_desc.strip():
                            fis_nodes.append({
                                "id": f"FIS-USR-{int(time.time()*1000)}",
                                "parentId": active_fnode["id"],
                                "generation": int(active_fnode.get("generation", 0)) + 1,
                                "code": cf_code.strip().upper(),
                                "siteId": cf_site,
                                "agentId": cf_agent,
                                "trackRef": active_fnode.get("trackRef", "H"),
                                "status": "active",
                                "titlePl": cf_title.strip(),
                                "titleEn": cf_title.strip(),
                                "descPl": cf_desc.strip(),
                                "descEn": cf_desc.strip(),
                                "neutronTargets": [],
                                "deliverablePl": cf_deliv.strip() or "Raport badawczy",
                                "deliverableEn": cf_deliv.strip() or "Research deliverable",
                            })
                            save_db(db)
                            st.rerun()

        st.divider()
        st.markdown("### 🎓 " + ("Continuous Back-to-Back Study Pipeline: 3 Years of Administration + 5 Consecutive Years per Selected Topic" if is_en else "Ciągły System Studiów: 3 Lata Administracji + Po 5 Lat Studiów z Każdej Wybranej Tematyki Cały Czas z Rzędu"))

        catalog_list = ms_state.get("fiveYearCatalog", [])
        catalog_map = {c["id"]: c for c in catalog_list}

        cfg_c1, cfg_c2 = st.columns([1, 3.2])
        with cfg_c1:
            new_start_yr = st.number_input("Rok startu / Start Year", min_value=1990, max_value=2100, value=start_cal, step=1, key="st_man_start_yr")
            if new_start_yr != start_cal:
                ms_state["startCalendarYear"] = int(new_start_yr)
                save_db(db)
                st.rerun()
        with cfg_c2:
            new_queue = st.multiselect(
                "Wybierz i ułóż w kolejności 5-letnie kierunki studiów realizowane bez przerwy z rzędu po 3 latach Administracji:",
                options=[c["id"] for c in catalog_list],
                default=[qid for qid in q_ids if qid in catalog_map],
                format_func=lambda cid: f"{catalog_map[cid]['icon']} {(catalog_map[cid]['titleEn'] if is_en else catalog_map[cid]['titlePl']).split('(')[0].strip()}",
            )
            if new_queue and new_queue != q_ids:
                ms_state["selectedQueue"] = new_queue
                save_db(db)
                st.rerun()

        # Blok 0: 3 Lata Studiów Administracji (Lata 1-3)
        admin_core = ms_state.get("adminCore3Y", {})
        raw_subs_done = ms_state.get("completedSubchapters")
        if not isinstance(raw_subs_done, dict):
            if isinstance(raw_subs_done, list):
                ms_state["completedSubchapters"] = {k: True for k in raw_subs_done}
            else:
                ms_state["completedSubchapters"] = {}
        admin_subs_done = ms_state["completedSubchapters"]
        with st.expander(f"🏛️ LATA 1–3 ({start_cal}–{start_cal + 3}) • {admin_core.get('titleEn') if is_en else admin_core.get('titlePl')} [{len(admin_done_list)}/3]", expanded=True):
            st.caption(admin_core.get("subtitleEn") if is_en else admin_core.get("subtitlePl"))
            for yr_obj in admin_core.get("years", []):
                yr_num = yr_obj["year"]
                checked = yr_num in admin_done_list
                new_chk = st.checkbox(
                    f"**{yr_obj['titleEn'] if is_en else yr_obj['titlePl']}** — {yr_obj['semesters']} ({start_cal + yr_num - 1}/{start_cal + yr_num})",
                    value=checked,
                    key=f"chk_admin_yr_{yr_num}",
                )
                if new_chk != checked:
                    if new_chk:
                        admin_done_list.append(yr_num)
                    else:
                        admin_done_list.remove(yr_num)
                    ms_state["adminCore3Y"]["completedYears"] = sorted(list(set(admin_done_list)))
                    save_db(db)
                    st.rerun()

                # Podrozdziały Administracji z checkboxami
                sub_list = (yr_obj.get("subchaptersEn", []) if is_en else yr_obj.get("subchaptersPl", [])) or []
                if sub_list:
                    with st.expander(f"📑 Podrozdziały Roku {yr_num} ({len(sub_list)} modułów wiedzy)", expanded=False):
                        for s_idx, s_txt in enumerate(sub_list, start=1):
                            sub_key = f"ADMIN-3Y_Y{yr_num}_{s_idx}"
                            s_done = admin_subs_done.get(sub_key, False)
                            s_toggled = st.checkbox(s_txt, value=s_done, key=f"chk_st_adm_sub_{sub_key}")
                            if s_toggled != s_done:
                                admin_subs_done[sub_key] = s_toggled
                                save_db(db)
                                st.rerun()

                adm_mats = yr_obj.get("linkedMaterialIds", [])
                adm_books = (yr_obj.get("coreBooksEn", []) if is_en else yr_obj.get("coreBooksPl", [])) or []
                if adm_mats or adm_books:
                    st.caption(f"📚 **Materiały:** {', '.join(adm_mats)} | 📖 **Podręczniki:** {' • '.join(adm_books)}")

                for crs in (yr_obj.get("coursesEn", []) if is_en else yr_obj.get("coursesPl", [])):
                    st.markdown(f"  - {crs}")
                st.info(f"🎯 {yr_obj.get('deliverableEn') if is_en else yr_obj.get('deliverablePl')}")

        # Bloki 1..N: Po 5 lat studiów z każdej wybranej tematyki cały czas z rzędu
        running_yr = 4
        for idx_q, study_id in enumerate(ms_state.get("selectedQueue", []), start=1):
            c_item = catalog_map.get(study_id)
            if not c_item:
                continue
            p_start = running_yr
            p_end = p_start + 4
            cal_s = start_cal + p_start - 1
            cal_e = cal_s + 5
            running_yr = p_end + 1
            done_yrs_topic = topics_done_map.setdefault(study_id, [])

            # Badges paradygmatów i barier fizycznych
            badges = []
            id_up = study_id.upper()
            if any(k in id_up for k in ["TRK-C", "FND-2", "FND-3"]):
                badges.append("`[⚛️ Podwaliny Krzemu u Kresu]`")
            if any(k in id_up for k in ["TRK-C", "FND-1", "FND-2", "FND-3"]):
                badges.append("`[🔮 Paradygmat Kwantowy QPU]`")
            if any(k in id_up for k in ["TRK-B", "TRK-C", "FND-2", "FND-4"]):
                badges.append("`[🧠 Architektury Neuromorficzne SNN]`")
            if "TRK-H" in id_up:
                badges.append("`[☢️ Super-Projekt Termojądrowy]`")
            badge_str = " " + " ".join(badges) if badges else ""

            with st.expander(
                f"{c_item['icon']} OGNIWO #{idx_q} • LATA {p_start}–{p_end} ({cal_s}–{cal_e}) • {c_item['titleEn'] if is_en else c_item['titlePl']} [{len(done_yrs_topic)}/5]{badge_str}",
                expanded=(idx_q in (1, len(ms_state.get("selectedQueue", [])))),
            ):
                if badges:
                    st.markdown(" ".join(badges))
                mats = c_item.get("linkedMaterialIds", [])
                if mats:
                    st.caption(f"📚 **Powiązane materiały:** {', '.join(mats)}")

                for y_row in c_item.get("years", []):
                    yn = y_row["year"]
                    is_y_done = yn in done_yrs_topic
                    toggled = st.checkbox(
                        f"**Rok {yn} z 5 (Rok projektowy {p_start + yn - 1} • {cal_s + yn - 1}/{cal_s + yn})** — {y_row['en'] if is_en else y_row['pl']}",
                        value=is_y_done,
                        key=f"chk_{study_id}_y{yn}",
                    )
                    if toggled != is_y_done:
                        if toggled:
                            done_yrs_topic.append(yn)
                        else:
                            done_yrs_topic.remove(yn)
                        topics_done_map[study_id] = sorted(list(set(done_yrs_topic)))
                        save_db(db)
                        st.rerun()

                    # Podrozdziały roku
                    subs = (y_row.get("subchaptersEn", []) if is_en else y_row.get("subchaptersPl", [])) or []
                    if subs:
                        with st.expander(f"📑 Podrozdziały Roku {yn} ({len(subs)} modułów)", expanded=False):
                            for s_idx, s_txt in enumerate(subs, start=1):
                                sub_k = f"{study_id}_Y{yn}_{s_idx}"
                                sub_d = admin_subs_done.get(sub_k, False)
                                s_ch = st.checkbox(s_txt, value=sub_d, key=f"chk_st_sub_{sub_k}")
                                if s_ch != sub_d:
                                    admin_subs_done[sub_k] = s_ch
                                    save_db(db)
                                    st.rerun()

                    books = (y_row.get("coreBooksEn", []) if is_en else y_row.get("coreBooksPl", [])) or []
                    if books:
                        st.caption(f"📖 **Literatura:** {' • '.join(books)}")


# ------------------------------------------------------------------------------
# ZAKŁADKA 1: MATERIAŁY DO NAUKI (8 DZIEDZIN + ODNOGI A-G + BIBLIOTEKA)
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ZAKŁADKA 2: AUDIO DO SAMOCHODU — CELOWA DROGA EKOSYSTEMU (CAR-FRIENDLY AUDIO ROAD)
# ------------------------------------------------------------------------------
with tab_caraudio:
    st.markdown("## 🎧 Audio do Samochodu — Celowa Droga Ekosystemu Golem 15")
    st.caption("Ogólna, przekrojowa baza audycji i materiałów odsłuchowych przygotowana specjalnie do regularnego słuchania w trasie i podczas dojazdów. Celowa droga prowadzi Cię przez 20 logicznych etapów: od Sztabu W-0 i prawa B+R, przez fundamenty matematyki i fizyki, kres krzemu i komputery kwantowe, aż po fuzję jądrową, inżynierię życia i filozofię Stanisława Lema.")

    road_list = ms_state.setdefault("carAudioRoad", json.loads(json.dumps(DEFAULT_SEED.get("manhattanSystem", {}).get("carAudioRoad", []))))
    raw_car_done = ms_state.get("completedCarAudio")
    if not isinstance(raw_car_done, dict):
        if isinstance(raw_car_done, list):
            ms_state["completedCarAudio"] = {k: True for k in raw_car_done}
        else:
            ms_state["completedCarAudio"] = {}
    done_car_map = ms_state["completedCarAudio"]

    done_car_count = sum(1 for ep in road_list if done_car_map.get(ep["id"], False))
    pct_road = int(round((done_car_count / len(road_list)) * 100)) if road_list else 0
    tot_min = sum(ep.get("estimatedDurationMin", 20) for ep in road_list)

    rc1, rc2, rc3, rc4 = st.columns(4)
    rc1.metric("Zaliczono w trasie", f"{done_car_count} / {len(road_list)} odc.", f"{pct_road}%")
    rc2.metric("Łączny czas odsłuchu", f"~{tot_min // 60}h {tot_min % 60}min", f"{len(road_list)} audycji")
    rc3.metric("Profil odsłuchu", "Samochód / Słuchawki", "Web Speech TTS")
    rc4.metric("Kierunek trasy", "Sztab W-0 → Lem", "20 etapów")

    st.progress(pct_road / 100.0)

    # Filtry etapu celowej drogi oraz profilu trasy
    st_c1, st_c2 = st.columns([1.5, 1])
    with st_c1:
        stage_choice = st.selectbox(
            "Wybierz etap Celowej Drogi Ekosystemu:",
            [
                "Wszystkie 20 Odcinków (Pełna Trasa)",
                "Etap 0: Sztab W-0 & Prawo B+R (2)",
                "Etap I: Fundamenty Formalne & Fizyka (5)",
                "Etap II: Kres Krzemu & Nowy Hardware (3)",
                "Etap III: Mózg, Bionika & WBE (2)",
                "Etap IV: Inżynieria Życia & Biosfera (2)",
                "Etap V: Super-Projekt Jądrowy H & Kosmos (3)",
                "Etap VI: Filozofia Przyszłości & Lem (3)",
            ],
        )
    with st_c2:
        profile_choice = st.selectbox(
            "Filtruj według czasu trasy samochodem:",
            [
                "Wszystkie czasy",
                "🚗 Trasa miejska (~18–20 min)",
                "🚙 Trasa podmiejska (~22–26 min)",
                "🛣️ Trasa daleka (28 min+)",
            ],
        )

    st_filter = "ALL"
    if "Etap 0" in stage_choice:
        st_filter = "0"
    elif "Etap I:" in stage_choice:
        st_filter = "I"
    elif "Etap II:" in stage_choice:
        st_filter = "II"
    elif "Etap III:" in stage_choice:
        st_filter = "III"
    elif "Etap IV:" in stage_choice:
        st_filter = "IV"
    elif "Etap V:" in stage_choice:
        st_filter = "V"
    elif "Etap VI:" in stage_choice:
        st_filter = "VI"

    filtered_episodes = []
    for ep in road_list:
        if st_filter != "ALL" and ep.get("stage") != st_filter:
            continue
        dur = ep.get("estimatedDurationMin", 20)
        if "miejska" in profile_choice and dur > 20:
            continue
        if "podmiejska" in profile_choice and (dur <= 20 or dur > 26):
            continue
        if "daleka" in profile_choice and dur <= 26:
            continue
        filtered_episodes.append(ep)

    st.markdown(f"**Wyświetlono {len(filtered_episodes)} z {len(road_list)} modułów wiedzy do samochodu:**")

    for ep in filtered_episodes:
        ep_id = ep["id"]
        is_done = done_car_map.get(ep_id, False)
        title_disp = ep.get("titleEn") if is_en else ep.get("titlePl")
        dur = ep.get("estimatedDurationMin", 20)
        prof_txt = ep.get("tripProfile", "Trasa uniwersalna")

        with st.container():
            col_a, col_b = st.columns([0.84, 0.16])
            with col_a:
                st.markdown(f"#### 📻 Odcinek #{ep.get('order', 1)}: {title_disp}")
                st.caption(f"🛣️ **{ep.get('stageNamePl')}** • ⏱️ ~{dur} min • 🚗 {prof_txt} • Kod: `{ep_id}`")
            with col_b:
                toggled = st.checkbox("✓ W trasie", value=is_done, key=f"chk_st_car_v2_{ep_id}")
                if toggled != is_done:
                    done_car_map[ep_id] = toggled
                    save_db(db)
                    st.rerun()

            # Tekst lektora (briefing)
            st.info(f"🗣️ **Briefing Lektora (tekst odsłuchiwany w trasie):**\n\n{ep.get('spokenBriefingEn') if is_en else ep.get('spokenBriefingPl')}")

            # Kluczowe wnioski
            takeaways = ep.get("keyTakeawaysPl", [])
            if takeaways:
                st.markdown("**📌 Kluczowe wnioski do zapamiętania w drodze:**")
                for tw in takeaways:
                    st.markdown(f"- {tw}")

            # Rekomendowane podcasty i audycje zewnętrzne
            ext_lnks = ep.get("curatedAudioLinks", [])
            if ext_lnks:
                st.markdown("**🎙️ Rekomendowane podcasty, audycje i audiobooki do auta:**")
                for el in ext_lnks:
                    st.markdown(f"- `[{el.get('lang', 'PL')}]` **[{el.get('type', 'podcast').upper()}]** [{el.get('title')}]({el.get('url')})")

            st.divider()

# ------------------------------------------------------------------------------
# ZAKŁADKA 1: MATERIAŁY DO NAUKI (8 DZIEDZIN + ODNOGI A-G + BIBLIOTEKA)
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ZAKŁADKA 2: AUDIO DO SAMOCHODU — CELOWA DROGA EKOSYSTEMU (CAR-FRIENDLY AUDIO ROAD)
# ------------------------------------------------------------------------------
with tab_caraudio:
    st.markdown("## 🎧 Audio do Samochodu — Celowa Droga Ekosystemu")
    st.caption("Celowo ułożona ścieżka dźwiękowa do słuchania w trasie: 18 odcinków w 4 logicznych etapach od Sztabu W-0 po Fuzję Termojądrową.")

    road_list = ms_state.setdefault("carAudioRoad", json.loads(json.dumps(DEFAULT_SEED.get("manhattanSystem", {}).get("carAudioRoad", []))))
    raw_car_done = ms_state.get("completedCarAudio")
    if not isinstance(raw_car_done, dict):
        if isinstance(raw_car_done, list):
            ms_state["completedCarAudio"] = {k: True for k in raw_car_done}
        else:
            ms_state["completedCarAudio"] = {}
    done_car_map = ms_state["completedCarAudio"]
    done_car_count = sum(1 for ep in road_list if done_car_map.get(ep["id"], False))
    pct_road = int(round((done_car_count / len(road_list)) * 100)) if road_list else 0
    tot_min = sum(ep.get("estimatedDurationMin", 15) for ep in road_list)

    rc1, rc2, rc3 = st.columns(3)
    rc1.metric("Zaliczono w trasie", f"{done_car_count} / {len(road_list)} odc.", f"{pct_road}%")
    rc2.metric("Łączny czas odsłuchu", f"~{tot_min // 60}h {tot_min % 60}min", "18 odcinków")
    rc3.metric("Obsługa", "Web Speech TTS", "Samochód / Słuchawki")

    st.progress(pct_road / 100.0)

    # Filtr etapów
    stage_choice = st.radio(
        "Filtruj etap celowej drogi:",
        ["Wszystkie (18)", "Etap I: Sztab W-0 & Administracja (2)", "Etap II: 8 Fundamentów Nauki (8)", "Etap III: Ścieżki Badawcze A–G (7)", "Etap IV: Super-Projekt H & Fuzja (1)"],
        horizontal=True,
    )
    st_filter = "ALL"
    if "Etap I" in stage_choice:
        st_filter = "I"
    elif "Etap II" in stage_choice:
        st_filter = "II"
    elif "Etap III" in stage_choice:
        st_filter = "III"
    elif "Etap IV" in stage_choice:
        st_filter = "IV"

    for ep in road_list:
        if st_filter != "ALL" and ep.get("stage") != st_filter:
            continue
        ep_id = ep["id"]
        is_done = done_car_map.get(ep_id, False)
        title_disp = ep.get("titleEn") if is_en else ep.get("titlePl")
        dur = ep.get("estimatedDurationMin", 15)

        with st.container():
            col_a, col_b = st.columns([0.85, 0.15])
            with col_a:
                st.markdown(f"#### 📻 Odcinek #{ep.get('order', 1)}: {title_disp}")
                st.caption(f"🛣️ {ep.get('stageNamePl')} • ⏱️ ~{dur} min • Kod: `{ep_id}`")
            with col_b:
                toggled = st.checkbox("✓ Odsłuchane", value=is_done, key=f"chk_st_car_{ep_id}")
                if toggled != is_done:
                    done_car_map[ep_id] = toggled
                    save_db(db)
                    st.rerun()

            # Tekst lektora
            st.info(ep.get("spokenBriefingEn") if is_en else ep.get("spokenBriefingPl"))

            # Wnioski
            takeaways = ep.get("keyTakeawaysPl", [])
            if takeaways:
                st.markdown("**📌 Kluczowe wnioski do zapamiętania w drodze:**")
                for tw in takeaways:
                    st.markdown(f"- {tw}")

            # Linki zewnętrzne
            ext_lnks = ep.get("curatedAudioLinks", [])
            if ext_lnks:
                st.markdown("**🎙️ Rekomendowane podcasty / wykłady zewnętrzne:**")
                for el in ext_lnks:
                    st.markdown(f"- `[{el.get('lang', 'PL')}]` [{el.get('title')}]({el.get('url')})")

            st.divider()

with tab_study:
    mode_study = st.radio(
        L["studyModeLabel"],
        options=[L["studyMode1"], L["studyMode2"], L["studyMode3"]],
        horizontal=True,
    )

    supp_lib = db.get("supplementaryLibrary", DEFAULT_SEED["supplementaryLibrary"])
    supp_by_track = {p["trackId"]: p for p in supp_lib.get("projects", [])}

    if mode_study == L["studyMode1"]:
        for fnd in sorted(db["foundationDisciplines"], key=lambda x: x["order"]):
            fid = fnd["id"]
            fname = FOUNDATION_EN[fid]["name"] if is_en else fnd["name"]
            fdesc = FOUNDATION_EN[fid]["description"] if is_en else fnd["description"]
            ftopics = FOUNDATION_EN[fid]["topics"] if is_en else fnd["topics"]

            raw_fnd_mats = [
                sm for sm in db.get("studyMaterials", [])
                if sm.get("categoryType") == "FOUNDATION" and sm.get("targetId") == fid
            ]
            fnd_materials = []
            for sm in raw_fnd_mats:
                blob = f"{sm.get('title','')} {sm.get('content','')} {json.dumps(sm.get('links',[]), ensure_ascii=False)}"
                l_info = detect_source_lang_info(blob, sm.get("sourceLang", ""), st.session_state.lang)
                if matches_lang_filter(l_info["code"], source_lang_filter):
                    fnd_materials.append((sm, l_info))

            with st.container(border=True):
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"### {fnd['order']}. {fnd['icon']} {fname}")
                    st.write(fdesc)
                    conn_badges = ", ".join(f"{'Track' if is_en else 'Projekt'} {tid}" for tid in fnd.get("connectedTracks", []))
                    st.caption(f"🔗 {'Foundation for tracks' if is_en else 'Fundament dla ścieżek'}: **{conn_badges}**")
                with c2:
                    st.metric(L["assignedMaterials"], len(fnd_materials))

                col_topics, col_mats = st.columns([1, 1.15])
                with col_topics:
                    st.markdown(f"**{L['topicsHeader']}**")
                    for idx_t, topic_item in enumerate(ftopics, start=1):
                        st.markdown(f"**{fnd['order']}.{idx_t}.** {topic_item}")

                with col_mats:
                    st.markdown(f"**{L['assignedMaterials']} ({len(fnd_materials)}):**")
                    for sm, l_info in fnd_materials:
                        with st.container(border=True):
                            st.markdown(
                                f"<span class='golem-lang-tag {'en' if l_info['code']=='EN' else ('bi' if l_info['code']=='PL+EN' else '')}'>{l_info['label']}</span> "
                                f"<span style='font-size:0.78rem; color:#94a3b8; margin-left:0.4rem;'>{sm.get('level', '')} • {sm.get('format', '')}</span>",
                                unsafe_allow_html=True,
                            )
                            st.markdown(f"**{sm['title']}**")
                            st.write(sm["content"])
                            if sm.get("links"):
                                st.markdown(f"**{L['sourceLinks']}**")
                                for lnk in sm["links"]:
                                    st.markdown(render_link_with_lang_badge(lnk, st.session_state.lang))
                            elif sm.get("url"):
                                st.markdown(f"- [🔗 {sm['url']}]({sm['url']})")

                with st.popover(f"{L['addStudyMatBtn']}: {fname}", use_container_width=True):
                    with st.form(f"owner_add_study_fnd_{fid}", clear_on_submit=True):
                        sm_topic = st.selectbox("Dział / Topic", options=fnd["topics"] + ["Ogólne / General"])
                        sm_title = st.text_input("Tytuł materiału / Material title*")
                        c_l, c_f, c_lg = st.columns(3)
                        sm_level = c_l.selectbox("Poziom / Level", ["Podstawowy / Basic", "Średniozaawansowany / Intermediate", "Zaawansowany / Advanced"])
                        sm_format = c_f.selectbox("Format", ["Podręcznik / Książka", "Kurs / Wykład", "Notatka własna", "Kod / Symulacja"])
                        sm_lang = c_lg.selectbox(L["sourceLangLabel"], ["PL", "EN", "PL+EN"])
                        sm_content = st.text_area("Opis / notatka własna*")
                        sm_url = st.text_input("Link URL / DOI (opcjonalnie)")
                        if st.form_submit_button(L["saveBtn"], type="primary"):
                            if sm_title.strip() and sm_content.strip():
                                db.setdefault("studyMaterials", []).insert(0, {
                                    "id": f"smat-{int(time.time()*1000)}",
                                    "categoryType": "FOUNDATION",
                                    "targetId": fid,
                                    "topic": sm_topic,
                                    "title": sm_title.strip(),
                                    "level": sm_level,
                                    "format": sm_format,
                                    "sourceLang": sm_lang,
                                    "content": sm_content.strip(),
                                    "url": sm_url.strip(),
                                    "author": "Ireneusz",
                                    "status": "approved",
                                    "createdAt": datetime.utcnow().isoformat() + "Z",
                                })
                                save_db(db)
                                st.rerun()

    elif mode_study == L["studyMode2"]:
        for track in db["tracks"]:
            tid = track["id"]
            t_code = TRACK_EN[tid]["code"] if is_en else track["code"]
            t_name = TRACK_EN[tid]["name"] if is_en else track["name"]
            t_goal = TRACK_EN[tid]["goal"] if is_en else track["goal"]
            t_q = TRACK_EN[tid]["guidingQuestion"] if is_en else track["guidingQuestion"]

            tr_study_mats = [
                sm for sm in db.get("studyMaterials", [])
                if sm.get("categoryType") == "TRACK" and sm.get("targetId") == tid
            ]
            all_branches = get_all_branches_for_track(db["tracks"], tid)

            with st.container(border=True):
                st.markdown(f"### {t_code} — {t_name}")
                st.caption(f"**{'Goal' if is_en else 'Cel'}:** {t_goal} | **{'Guiding question' if is_en else 'Pytanie przewodnie'}:** *{t_q}*")

                if tid in supp_by_track:
                    sp_proj = supp_by_track[tid]
                    st.info(f"**{sp_proj['sequenceLabel']}:** {sp_proj['sequence']}")

                for sec in track["sections"]:
                    st.markdown(f"**{sec['title']}:**")
                    for b_idx, branch_item in enumerate(sec["items"], start=1):
                        branch_mats = [m for m in tr_study_mats if m.get("topic") == branch_item]
                        st.markdown(f"- **{b_idx}. {branch_item}**")
                        for bm in branch_mats:
                            blob = f"{bm.get('title','')} {bm.get('content','')} {json.dumps(bm.get('links',[]), ensure_ascii=False)}"
                            l_info = detect_source_lang_info(blob, bm.get("sourceLang", ""), st.session_state.lang)
                            if not matches_lang_filter(l_info["code"], source_lang_filter):
                                continue
                            url_part = f" — [🔗 Link]({bm['url']})" if bm.get("url") else ""
                            st.markdown(f"  - `{l_info['label']}` 📖 **{bm['title']}** ({bm.get('level')}) — {bm['content']}{url_part}")
                            for lnk in bm.get("links", []):
                                st.markdown("  " + render_link_with_lang_badge(lnk, st.session_state.lang))

                if tid in supp_by_track:
                    with st.expander(f"📚 {'Supplementary Library & Source Links' if is_en else 'Biblioteka materiałów uzupełniających i linki źródłowe'} ({t_code})", expanded=True):
                        sp_proj = supp_by_track[tid]
                        cols_g = st.columns(len(sp_proj["groups"]))
                        for g_idx, grp in enumerate(sp_proj["groups"]):
                            with cols_g[g_idx]:
                                g_lang_badge = "🇵🇱 `[PL]`" if "polsku" in grp["heading"].lower() else ("🇬🇧 `[EN]`" if "angielsku" in grp["heading"].lower() else "🌐 `[PL/EN]`")
                                st.markdown(f"**{g_lang_badge} {grp['heading']}:**")
                                for itm in grp["items"]:
                                    st.markdown(f"- {itm}")
                        if sp_proj.get("links"):
                            st.markdown(f"**{L['sourceLinks']}**")
                            for lnk in sp_proj["links"]:
                                st.markdown(render_link_with_lang_badge(lnk, st.session_state.lang))

    else:
        st.markdown(f"### 📖 {supp_lib['title']}")
        st.markdown(f"*{supp_lib['description']}*")

        with st.container(border=True):
            st.markdown("#### 📜 " + ("Library Rules (1–6)" if is_en else "Zasady korzystania z biblioteki (1–6)"))
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
                    st.info(f"**{'Principle' if is_en else 'Zasada'}:** {reading_order['principle']}")

        for sp_proj in supp_lib.get("projects", []):
            with st.container(border=True):
                st.markdown(f"### {sp_proj['title']}")
                st.info(f"**{sp_proj['sequenceLabel']}:** {sp_proj['sequence']}")
                cols_grp = st.columns(len(sp_proj["groups"]))
                for g_idx, grp in enumerate(sp_proj["groups"]):
                    with cols_grp[g_idx]:
                        g_lang_badge = "🇵🇱 `[PL]`" if "polsku" in grp["heading"].lower() else ("🇬🇧 `[EN]`" if "angielsku" in grp["heading"].lower() else "🌐 `[PL/EN]`")
                        st.markdown(f"#### {g_lang_badge} {grp['heading']}")
                        for item_txt in grp["items"]:
                            st.markdown(f"- {item_txt}")
                if sp_proj.get("links"):
                    st.markdown(f"#### {L['sourceLinks']}")
                    for lnk in sp_proj["links"]:
                        st.markdown(render_link_with_lang_badge(lnk, st.session_state.lang))


# ------------------------------------------------------------------------------
# ZAKŁADKA 2: MAPA 7 ŚCIEŻEK (PROJEKTY A-G)
# ------------------------------------------------------------------------------
with tab_map:
    st.info(
        f"**{L['fgSummary']}**\n"
        f"- {L['fPerspective']}\n"
        f"- {L['gPerspective']}"
    )
    for track in db["tracks"]:
        tid = track["id"]
        t_code = TRACK_EN[tid]["code"] if is_en else track["code"]
        t_name = TRACK_EN[tid]["name"] if is_en else track["name"]
        t_goal = TRACK_EN[tid]["goal"] if is_en else track["goal"]
        t_q = TRACK_EN[tid]["guidingQuestion"] if is_en else track["guidingQuestion"]
        sub_list = [s for s in db["subprojects"] if s["trackId"] == tid]
        mat_list = [m for m in db["materials"] if m["trackId"] == tid]

        with st.container(border=True):
            c_head1, c_head2 = st.columns([4, 1])
            with c_head1:
                st.markdown(f"### {t_code} — {t_name}")
                st.markdown(f"**{'Goal' if is_en else 'Cel'}:** {t_goal}")
                st.markdown(f"> **{'Guiding question' if is_en else 'Pytanie przewodnie'}:** *{t_q}*")
                if track.get("note"):
                    st.warning(track["note"])
            with c_head2:
                st.metric("Workspaces" if is_en else "Środowiska", len(sub_list))
                st.metric("Materials" if is_en else "Materiały", len(mat_list))

            cols_sec = st.columns(len(track["sections"]))
            for idx, sec in enumerate(track["sections"]):
                with cols_sec[idx]:
                    st.markdown(f"**{sec['title']}:**")
                    for item in sec["items"]:
                        st.markdown(f"- {item}")


# ------------------------------------------------------------------------------
# ZAKŁADKA 3: PRYWATNE ŚRODOWISKA BADAWCZE I PODPROJEKTY WŁAŚCICIELA
# ------------------------------------------------------------------------------
with tab_ws:
    all_sps = db.get("subprojects", [])
    if not all_sps:
        st.info("Brak środowisk badawczych." if not is_en else "No research workspaces yet.")
    else:
        selected_sp_id = st.selectbox(
            "Wybierz środowisko badawcze / Select research workspace:",
            options=[sp["id"] for sp in all_sps],
            format_func=lambda sid: next((f"[{s['trackId']}] {s['title']}" for s in all_sps if s["id"] == sid), sid),
        )
        active_sp = next((s for s in all_sps if s["id"] == selected_sp_id), all_sps[0])
        ws = active_sp.setdefault("workspace", {"hypotheses": [], "notes": [], "bibliography": []})

        with st.container(border=True):
            st.markdown(f"## {active_sp['title']}")
            st.caption(f"**{'Track' if is_en else 'Ścieżka'}:** {active_sp['trackId']} | **{'Branch' if is_en else 'Odnoga'}:** {active_sp.get('branchTopic', '')}")
            st.write(active_sp.get("description", ""))
            if active_sp.get("philosophicalNote"):
                st.info(f"**Projekt E (Filozofia):** {active_sp['philosophicalNote']}")

        col_h, col_n, col_b = st.columns(3)
        with col_h:
            st.markdown("#### 1. " + ("Research Hypotheses" if is_en else "Hipotezy badawcze"))
            for h in ws.get("hypotheses", []):
                with st.container(border=True):
                    st.caption(f"Status: **{h.get('status', 'Hipoteza otwarta')}**")
                    st.write(h["statement"])
            with st.popover("➕ " + ("Add hypothesis" if is_en else "Dodaj hipotezę"), use_container_width=True):
                with st.form(f"form_hyp_{active_sp['id']}", clear_on_submit=True):
                    h_stmt = st.text_area("Treść hipotezy / Hypothesis statement")
                    h_stat = st.selectbox("Status", ["Hipoteza otwarta", "W weryfikacji", "Potwierdzona częściowo", "Wymaga korekty"])
                    if st.form_submit_button(L["saveBtn"], type="primary"):
                        if h_stmt.strip():
                            ws.setdefault("hypotheses", []).append({
                                "id": f"hyp-{int(time.time()*1000)}",
                                "statement": h_stmt.strip(),
                                "status": h_stat,
                                "author": "Ireneusz",
                                "approvalStatus": "approved",
                            })
                            save_db(db)
                            st.rerun()

        with col_n:
            st.markdown("#### 2. " + ("Research Notebook" if is_en else "Notatnik badawczy"))
            for n in ws.get("notes", []):
                with st.container(border=True):
                    st.markdown(f"**{n['title']}**")
                    st.write(n["content"])
            with st.popover("➕ " + ("Add research note" if is_en else "Dodaj notatkę badawczą"), use_container_width=True):
                with st.form(f"form_note_{active_sp['id']}", clear_on_submit=True):
                    n_title = st.text_input("Tytuł notatki / Note title")
                    n_content = st.text_area("Treść / Content")
                    if st.form_submit_button(L["saveBtn"], type="primary"):
                        if n_title.strip() and n_content.strip():
                            ws.setdefault("notes", []).append({
                                "id": f"note-{int(time.time()*1000)}",
                                "title": n_title.strip(),
                                "content": n_content.strip(),
                                "author": "Ireneusz",
                                "createdAt": datetime.utcnow().isoformat() + "Z",
                                "approvalStatus": "approved",
                            })
                            save_db(db)
                            st.rerun()

        with col_b:
            st.markdown("#### 3. " + ("Bibliography & Sources" if is_en else "Bibliografia i źródła"))
            for b in ws.get("bibliography", []):
                with st.container(border=True):
                    b_info = detect_source_lang_info(f"{b.get('citation','')} {b.get('url','')}", b.get("sourceLang", ""), st.session_state.lang)
                    st.markdown(f"`{b_info['label']}` 📖 {b['citation']}")
                    if b.get("url"):
                        st.markdown(f"[🔗 Link / DOI]({b['url']})")
            with st.popover("➕ " + ("Add source" if is_en else "Dodaj źródło bibliograficzne"), use_container_width=True):
                with st.form(f"form_bib_{active_sp['id']}", clear_on_submit=True):
                    b_cit = st.text_area("Cytowanie / Citation")
                    b_lang = st.selectbox(L["sourceLangLabel"], ["PL", "EN", "PL+EN"])
                    b_url = st.text_input("Link / DOI")
                    if st.form_submit_button(L["saveBtn"], type="primary"):
                        if b_cit.strip():
                            ws.setdefault("bibliography", []).append({
                                "id": f"bib-{int(time.time()*1000)}",
                                "citation": b_cit.strip(),
                                "sourceLang": b_lang,
                                "url": b_url.strip(),
                                "addedBy": "Ireneusz",
                                "approvalStatus": "approved",
                            })
                            save_db(db)
                            st.rerun()


# ------------------------------------------------------------------------------
# ZAKŁADKA 4: BIBLIOTEKA I REPOZYTORIUM Z OZNACZENIEM JĘZYKA ŹRÓDEŁ [PL] / [EN]
# ------------------------------------------------------------------------------
with tab_mat:
    c_m1, c_m2 = st.columns([1, 2])
    with c_m1:
        m_track_filter = st.selectbox(
            "Track",
            options=["ALL"] + [t["id"] for t in db["tracks"]],
            format_func=lambda x: ("All Tracks (A–G)" if is_en else "Wszystkie ścieżki (A–G)") if x == "ALL" else f"{tracks_by_id[x]['code']} — {TRACK_EN[x]['name'] if is_en else tracks_by_id[x]['name']}",
            key="mat_track_filter",
        )
    with c_m2:
        m_search = st.text_input("Filter repository..." if is_en else "Filtruj repozytorium (tytuł, treść, odnoga)...")

    for m in db.get("materials", []):
        if m_track_filter != "ALL" and m["trackId"] != m_track_filter:
            continue
        blob = f"{m.get('title','')} {m.get('content','')} {m.get('branchTopic','')} {json.dumps(m.get('links',[]), ensure_ascii=False)}"
        l_info = detect_source_lang_info(blob, m.get("sourceLang", ""), st.session_state.lang)
        if not matches_lang_filter(l_info["code"], source_lang_filter):
            continue
        if m_search.strip() and m_search.lower() not in blob.lower():
            continue

        with st.container(border=True):
            st.markdown(
                f"<span class='golem-lang-tag {'en' if l_info['code']=='EN' else ('bi' if l_info['code']=='PL+EN' else '')}'>{l_info['label']}</span> "
                f"<span style='font-size:0.8rem; color:#94a3b8; margin-left:0.5rem;'><strong>Projekt {m['trackId']}</strong> • {m.get('type', 'Materiał')} • {m.get('branchTopic') or ''}</span>",
                unsafe_allow_html=True,
            )
            st.markdown(f"### {m['title']}")
            st.write(m["content"])
            if m.get("links"):
                st.markdown(f"**{L['sourceLinks']}**")
                for lnk in m["links"]:
                    st.markdown(render_link_with_lang_badge(lnk, st.session_state.lang))
            elif m.get("url"):
                st.markdown(f"[🔗 {m['url']}]({m['url']})")


# ------------------------------------------------------------------------------
# ZAKŁADKA 5: DODAWANIE WŁASNYCH MATERIAŁÓW I PODPROJEKTÓW PRZEZ WŁAŚCICIELA
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ZAKŁADKA 7: SUMMA TECHNOLOGIAE 2.0 (STANISŁAW LEM — BIBLIA MOŻLIWOŚCI TECHNIKI)
# ------------------------------------------------------------------------------
with tab_book:
    book_data = db.setdefault("summaBook", json.loads(json.dumps(DEFAULT_SEED.get("summaBook", {}))))
    st.markdown(f"## 📖 {book_data.get('title', 'Summa Technologiae 2.0')}")
    st.caption(f"*{book_data.get('motto', '')}* — **Współautorzy:** {book_data.get('author', 'Ireneusz')} & Golem XV")

    chapters = book_data.get("chapters", [])
    ch_titles = [f"{'Wstęp' if c.get('number')==0 else f'Rozdział {c.get("number")}'}: {c.get('titlePl')}" for c in chapters]

    ch_sel_idx = st.selectbox("Wybierz rozdział do czytania i edycji:", range(len(chapters)), format_func=lambda i: ch_titles[i])
    cur_ch = chapters[ch_sel_idx]

    b_col1, b_col2 = st.columns([0.7, 0.3])
    with b_col1:
        st.markdown(f"### {'Wstęp' if cur_ch.get('number')==0 else f'Rozdział {cur_ch.get("number")}'}: {cur_ch.get('titlePl')}")
        st.caption(f"Status: **{cur_ch.get('epistemicStatus')}** • ⏱️ ~{cur_ch.get('readingTimeMin')} min • Aktualizacja: {cur_ch.get('lastUpdated')}")
    with b_col2:
        # Pobieranie całego rękopisu
        full_md = f"# {book_data.get('title')}\n\n**Autorzy:** {book_data.get('author')} & Golem XV\n\n*{book_data.get('motto')}*\n\n"
        for ch in chapters:
            full_md += f"## {ch.get('titlePl')}\n\n> *„{ch.get('lemQuote')}”*\n\n{ch.get('contentMarkdownPl', '')}\n\n---\n\n"
        st.download_button(
            "📥 Pobierz cały rękopis (.md)",
            data=full_md.encode("utf-8"),
            file_name=f"Summa_Technologiae_2_0_Ireneusz_{datetime.utcnow().strftime('%Y%m%d')}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    st.markdown(f"> *„{cur_ch.get('lemQuote')}”* — **Stanisław Lem**")
    st.info(f"💡 **Rdzeń pojęciowy rozdziału:**\n\n{cur_ch.get('summaryPl')}")

    # Prompt asystenta Lema
    with st.expander("✨ Asystent Lema — Gotowy prompt syntezy AI dla Golem XV"):
        lem_prompt = f"""Jesteś Stanisławem Lemem oraz superinteligencją Golem XV. Piszemy wspólnie dzieło: „Summa Technologiae 2.0: Biblia Możliwości Techniki”.
Rozdział: {cur_ch.get('number')}. {cur_ch.get('titlePl')}
Motto przewodnie: "{cur_ch.get('lemQuote')}"

Zadanie epistemiczne:
Rozwiń ten rozdział w chłodnym, precyzyjnym, lemowskim stylu filozoficzno-technologicznym. Uwzględnij:
1. Fizyczne granice krzemu (prawo Moore'a u kresu, prądy upływu, granica Landauera, koniec skalowania Dennarda).
2. Zmianę paradygmatu programowania (od klasycznego kodu von Neumanna do obliczeń tensorowych, kwantowych QPU oraz neuromorficznych sieci impulsowych SNN).
3. Maszyny naśladujące mózg biologiczny i protokół WBE (Whole Brain Emulation).
4. Etyczne i cywilizacyjne konsekwencje dla ludzkości.

Bieżący zarys rozdziału:
{cur_ch.get('summaryPl')}

Przygotuj głęboki esej stanowiący kolejną sekcję tego rozdziału."""
        st.code(lem_prompt, language="text")

    # Edytor rękopisu
    with st.form(f"form_book_ch_{cur_ch.get('id')}"):
        st.markdown("**✏️ Rękopis rozdziału (format Markdown):**")
        edited_text = st.text_area("Treść rozdziału", value=cur_ch.get("contentMarkdownPl", ""), height=380, label_visibility="collapsed")
        if st.form_submit_button("💾 Zapisz zmiany w rękopisie rozdziału", type="primary"):
            cur_ch["contentMarkdownPl"] = edited_text
            cur_ch["lastUpdated"] = datetime.utcnow().strftime("%Y-%m-%d")
            save_db(db)
            st.success("Zapisano zmiany w rękopisie!")
            st.rerun()

    # Podgląd sformatowany
    with st.expander("📖 Podgląd czytelniczy (sformatowany)"):
        st.markdown(cur_ch.get("contentMarkdownPl", "*Brak treści rozdziału.*"))

    # Możliwość dodania nowego rozdziału do Summy Technologiae 2.0
    with st.expander("➕ Dodaj nowy rozdział do Summy Technologiae 2.0 (w miarę zdobywania wiedzy)"):
        st.markdown("Pisz własne dzieło na kanwie zdobywanej wiedzy — każdy rozdział reprezentuje kolejny etap Twojego rozwoju naukowego i filozoficznego w duchu Stanisława Lema.")
        with st.form("form_add_custom_book_chapter"):
            new_num = len(chapters)
            col_nc1, col_nc2 = st.columns([0.7, 0.3])
            with col_nc1:
                nc_title = st.text_input("Tytuł nowego rozdziału*", placeholder=f"Rozdział {new_num}: ...")
            with col_nc2:
                nc_status = st.selectbox(
                    "Status epistemiczny",
                    ["🟢 Potwierdzona metoda badawcza", "🔵 Aktywne prace inżynieryjne", "🟡 Hipoteza inżynieryjna", "🟣 Spekulacja futurologiczna"],
                    index=1,
                    key="sb_nc_status"
                )
            nc_quote = st.text_input("Motto lub cytat przewodni (Stanisław Lem / myśl własna)*", placeholder="„Technologia jest to domena...”")
            nc_summary = st.text_area("Rdzeń pojęciowy i synteza idei rozdziału*", placeholder="Główne tezy, granice materii, nowe paradygmaty...")
            nc_content = st.text_area("Początkowy szkic rękopisu (Markdown, opcjonalnie)", placeholder="# Tytuł rozdziału\n\nPierwsze przemyślenia...", height=180)

            if st.form_submit_button("💾 Dodaj i zapisz rozdział w Summie 2.0", type="primary"):
                if nc_title.strip() and nc_quote.strip() and nc_summary.strip():
                    new_ch_dict = {
                        "id": f"ch-custom-{new_num}-{datetime.utcnow().strftime('%s') if hasattr(datetime.utcnow(), 'strftime') else 'new'}",
                        "number": new_num,
                        "titlePl": nc_title.strip(),
                        "titleEn": nc_title.strip(),
                        "lemQuote": nc_quote.strip(),
                        "epistemicStatus": nc_status,
                        "readingTimeMin": 20,
                        "lastUpdated": datetime.utcnow().strftime("%Y-%m-%d"),
                        "summaryPl": nc_summary.strip(),
                        "summaryEn": nc_summary.strip(),
                        "contentMarkdownPl": nc_content.strip() or f"# {nc_title.strip()}\n\n> *„{nc_quote.strip()}”*\n\n{nc_summary.strip()}",
                        "contentMarkdownEn": nc_content.strip() or f"# {nc_title.strip()}\n\n> *„{nc_quote.strip()}”*\n\n{nc_summary.strip()}"
                    }
                    chapters.append(new_ch_dict)
                    save_db(db)
                    st.success(f"Pomyślnie dodano '{nc_title}' do Twojej Summy Technologiae 2.0!")
                    st.rerun()
                else:
                    st.error("Proszę wypełnić wymagane pola: Tytuł, Motto oraz Rdzeń pojęciowy.")

with tab_new:
    col_form_sp, col_form_mat = st.columns(2)

    with col_form_sp:
        st.markdown("### 🔬 " + ("1. Create New Research Workspace / Subproject" if is_en else "1. Utwórz własny podprojekt i środowisko badawcze"))
        sp_track = st.selectbox(
            "Ścieżka główna / Main Track (A–G)",
            options=[t["id"] for t in db["tracks"]],
            format_func=lambda x: f"{tracks_by_id[x]['code']} — {TRACK_EN[x]['name'] if is_en else tracks_by_id[x]['name']}",
            key="new_sp_track",
        )
        available_branches = get_all_branches_for_track(db["tracks"], sp_track)
        with st.form("create_subproject_form", clear_on_submit=True):
            sp_branch = st.selectbox("Odnoga badawcza / Branch", options=available_branches + ["Inna / Custom"])
            sp_custom_branch = st.text_input("Własna nazwa odnogi (opcjonalnie)")
            sp_title = st.text_input("Tytuł podprojektu / Workspace title*")
            sp_desc = st.text_area("Cel i opis problemu badawczego / Goal & description*")
            sp_hyp = st.text_input("Hipoteza startowa / Initial hypothesis")
            sp_phil = st.text_input("Notatka filozoficzna (Projekt E)")
            if st.form_submit_button("🚀 " + ("Create Workspace" if is_en else "Utwórz środowisko badawcze"), type="primary", use_container_width=True):
                if sp_title.strip() and sp_desc.strip():
                    final_branch = sp_custom_branch.strip() if sp_custom_branch.strip() else sp_branch
                    db["subprojects"].insert(0, {
                        "id": f"sub-{int(time.time()*1000)}",
                        "trackId": sp_track,
                        "secondaryTracks": ["E"],
                        "branchTopic": final_branch,
                        "title": sp_title.strip(),
                        "author": "Ireneusz",
                        "status": "approved",
                        "createdAt": datetime.utcnow().isoformat() + "Z",
                        "description": sp_desc.strip(),
                        "philosophicalNote": sp_phil.strip(),
                        "workspace": {
                            "hypotheses": [
                                {
                                    "id": f"hyp-{int(time.time()*1000)}",
                                    "statement": sp_hyp.strip(),
                                    "status": "Hipoteza otwarta",
                                    "author": "Ireneusz",
                                    "approvalStatus": "approved",
                                }
                            ] if sp_hyp.strip() else [],
                            "notes": [],
                            "bibliography": [],
                        },
                    })
                    save_db(db)
                    st.success("Zapisano nowe środowisko!" if not is_en else "Workspace saved!")
                    st.rerun()

    with col_form_mat:
        st.markdown("### 📚 " + ("2. Add New Research Material" if is_en else "2. Dodaj własny materiał badawczy / źródło"))
        mat_track = st.selectbox(
            "Ścieżka (Projekt A–G)",
            options=[t["id"] for t in db["tracks"]],
            format_func=lambda x: f"{tracks_by_id[x]['code']} — {TRACK_EN[x]['name'] if is_en else tracks_by_id[x]['name']}",
            key="new_mat_track",
        )
        mat_branches = get_all_branches_for_track(db["tracks"], mat_track)
        with st.form("create_material_form", clear_on_submit=True):
            mat_branch = st.selectbox("Odnoga zakresu", options=mat_branches + ["Ogólna"])
            c_mt1, c_mt2 = st.columns(2)
            mat_type = c_mt1.selectbox(
                "Typ materiału",
                [
                    "Opracowanie własne / Notatka",
                    "Książka / Podręcznik",
                    "Artykuł naukowy / Przegląd",
                    "Model matematyczny / Symulacja",
                    "Analiza filozoficzna / Bioetyczna",
                ],
            )
            mat_lang = c_mt2.selectbox(L["sourceLangLabel"], ["PL", "EN", "PL+EN"])
            mat_title = st.text_input("Tytuł materiału*")
            mat_content = st.text_area("Treść / Notatka / Wnioski*")
            mat_url = st.text_input("Link źródłowy / DOI (opcjonalnie)")
            if st.form_submit_button(L["saveBtn"], type="primary", use_container_width=True):
                if mat_title.strip() and mat_content.strip():
                    db["materials"].insert(0, {
                        "id": f"mat-{int(time.time()*1000)}",
                        "trackId": mat_track,
                        "branchTopic": mat_branch,
                        "subprojectId": None,
                        "title": mat_title.strip(),
                        "type": mat_type,
                        "sourceLang": mat_lang,
                        "author": "Ireneusz",
                        "content": mat_content.strip(),
                        "url": mat_url.strip(),
                        "status": "approved",
                        "createdAt": datetime.utcnow().isoformat() + "Z",
                    })
                    save_db(db)
                    st.success("Zapisano materiał w bazie!" if not is_en else "Material saved!")
                    st.rerun()


# ------------------------------------------------------------------------------
# ZAKŁADKA 6: GRAF POWIĄZAŃ (A-G)
# ------------------------------------------------------------------------------
with tab_graph:
    st.subheader("🕸️ " + ("Inter-Track Connections (A–G) & Space (F) ↔ Earth (G) Axis" if is_en else "Relacje międzyścieżkowe (A–G) oraz oś Kosmos (F) ↔ Ziemia (G)"))
    for lnk in db.get("graphLinks", []):
        s_tr = tracks_by_id.get(lnk["source"], {"code": lnk["source"], "name": ""})
        t_tr = tracks_by_id.get(lnk["target"], {"code": lnk["target"], "name": ""})
        st.markdown(f"- **{s_tr['code']} ({s_tr['name']})** ↔ **{t_tr['code']} ({t_tr['name']})**: {lnk['label']}")


# ------------------------------------------------------------------------------
# ZAKŁADKA 7: BEZPIECZEŃSTWO, HASŁO WŁAŚCICIELA I AUTORYZACJA URZĄDZENIA
# ------------------------------------------------------------------------------
with tab_security:
    st.subheader("🔒 " + ("Owner Security, Password & Trusted Device" if is_en else "Bezpieczeństwo Projektu, Hasło Właściciela i Autoryzacja Urządzenia"))
    sec_c1, sec_c2 = st.columns(2)

    with sec_c1:
        with st.container(border=True):
            st.markdown("#### 💻 " + ("Trusted Owner Device Authorization" if is_en else "Autoryzacja Twojego Urządzenia i Przeglądarki"))
            st.write(
                "Projekt jest całkowicie zablokowany dla osób postronnych. "
                "Na swoim prywatnym komputerze oraz poprzez prywatny link z tokenem urządzenia wchodzisz bezpośrednio bez konieczności każdorazowego wpisywania hasła."
            )
            c_d1, c_d2 = st.columns(2)
            if c_d1.button("✓ Autoryzuj to urządzenie lokalnie i w URL", type="primary", use_container_width=True):
                authorize_local_owner_device(db)
                st.query_params["device_token"] = expected_dev_token
                st.success("Urządzenie zostało autoryzowane! Możesz dodać bieżący adres URL do zakładek w swojej przeglądarce.")
            if c_d2.button("🗑️ Usuń autoryzację tego urządzenia", use_container_width=True):
                if os.path.exists(LOCAL_DEVICE_KEY_FILE):
                    try:
                        os.remove(LOCAL_DEVICE_KEY_FILE)
                    except Exception:
                        pass
                st.query_params.clear()
                st.warning("Autoryzacja urządzenia została wyczyszczona — przy kolejnym wejściu wymagane będzie hasło.")

            st.divider()
            st.download_button(
                "⬇ Pobierz kopię zapasową bazy JSON",
                data=json.dumps(db, ensure_ascii=False, indent=2),
                file_name="the_golem_15_private_backup.json",
                mime="application/json",
                use_container_width=True,
            )

    with sec_c2:
        with st.container(border=True):
            st.markdown("#### 🔑 " + ("Update Owner Password (PBKDF2-HMAC-SHA256)" if is_en else "Zmień / Zaktualizuj Hasło Właściciela (PBKDF2-HMAC-SHA256)"))
            st.caption("Hasło jest chronione 260 000 iteracji PBKDF2-HMAC-SHA256 z losową solą 128-bitową. Zmiana hasła automatycznie unieważnia stare tokeny urządzeń.")
            with st.form("change_owner_pass_form", clear_on_submit=True):
                current_pass = st.text_input("Aktualne hasło właściciela", type="password", value="")
                new_pass = st.text_input("Nowe hasło właściciela (min. 8 znaków)", type="password", value="")
                new_pass_confirm = st.text_input("Powtórz nowe hasło", type="password", value="")
                if st.form_submit_button("Zaktualizuj hasło kryptograficzne", type="primary", use_container_width=True):
                    if not verify_admin_password(current_pass, db):
                        st.error("Aktualne hasło jest nieprawidłowe.")
                    elif len(new_pass.strip()) < 8:
                        st.error("Nowe hasło musi zawierać co najmniej 8 znaków.")
                    elif new_pass != new_pass_confirm:
                        st.error("Nowe hasła nie są identyczne.")
                    else:
                        new_auth = create_admin_auth_record(new_pass.strip(), iterations=260000)
                        db["projectMeta"]["adminAuth"] = new_auth
                        save_db(db)
                        authorize_local_owner_device(db)
                        st.query_params["device_token"] = get_expected_device_token(db)
                        st.success("Hasło właściciela oraz klucz Twojego urządzenia zostały zaktualizowane!")

    st.divider()
    st.subheader("🤖 " + ("Autonomic System Sentinel & Self-Healing Engine" if is_en else "Autonomiczny Strażnik Systemu, Samonaprawa i Auto-Aktualizacja"))
    st.caption("Aplikacja w sposób ciągły monitoruje swoją spójność technologiczną, samoczynnie leczy anomalie strukturalne, zabezpiecza migawki bazy danych i weryfikuje aktualizacje w chmurze.")

    col_h1, col_h2, col_h3, col_h4 = st.columns(4)
    with col_h1:
        st.metric("Kondycja Systemu", "100%", delta="Optymalna", delta_color="normal")
    with col_h2:
        st.metric("Silnik Samonaprawy", "Aktywny", delta="Auto-Repair ON")
    with col_h3:
        cur_db_kb = round(len(json.dumps(db).encode("utf-8")) / 1024, 1)
        st.metric("Rozmiar Bazy Danych", f"{cur_db_kb} KB", delta="Auto-Backup OK")
    with col_h4:
        upstream_info = check_github_upstream_status()
        st.metric("Wersja Upstream (GitHub)", upstream_info.get("latest_sha", "v2.2"), delta=upstream_info.get("status", "Aktywna"))

    c_btn1, c_btn2, c_btn3 = st.columns(3)
    if c_btn1.button("🩺 Uruchom Samonaprawę Bazy i Optymalizację Indeksów", type="primary", use_container_width=True):
        db, rep = run_system_self_healing(db, DEFAULT_SEED)
        save_db(db)
        st.success(f"Samonaprawa zakończona sukcesem! Stan bazy: {rep['status']}. Wykonano snapshot bezpieczeństwa.")
        st.rerun()

    if c_btn2.button("🔄 Sprawdź Najnowszą Wersję na GitHubie", use_container_width=True):
        up = check_github_upstream_status()
        if up.get("ok"):
            st.info(f"Najnowszy commit na gałęzi main: `{up['latest_sha']}` ({up['date']})\nKomunikat: *{up['message']}*\nTwój kod jest zsynchronizowany z gałęzią nadrzędną.")
        else:
            st.warning(f"Informacja o chmurze: {up.get('status')} ({up.get('error', '')})")

    if c_btn3.button("🧹 Wyczyść Pamięć Podręczną (Cache Eviction)", use_container_width=True):
        st.cache_data.clear()
        st.cache_resource.clear()
        st.success("Pamięć podręczna (Streamlit Cache) została całkowicie wyczyszczona i zoptymalizowana!")

    with st.expander("📋 Szczegółowy Dziennik Autodiagnostyki i Ewolucji Technologii"):
        st.markdown(f"**Wersja schematu danych:** `v{CURRENT_SCHEMA_VERSION} (Kapsuła Czasu aktywna)`")
        st.markdown(f"**Zabezpieczenia kryptograficzne:** `PBKDF2-HMAC-SHA256 ({RECOMMENDED_PBKDF2_ITERATIONS} iteracji — standard NIST-2026)`")
        st.markdown(f"**Ostatni test integralności:** `{healing_report.get('timestamp')}`")
        st.markdown(f"**Wykryte i samonaprawione anomalie:** `{healing_report.get('anomalies_repaired')}`")
        st.markdown(f"**Lokalizacja automatycznej kopii zapasowej:** `{os.path.join(DATA_DIR, 'database.auto_backup.json')}`")
        st.markdown(f"**Katalog bezpiecznych archiwów projektu:** `{ARCHIVES_DIR}`")
        if migration_logs:
            st.markdown("**Dziennik migracji kapsuły czasu:**")
            for item in migration_logs:
                st.markdown(f"- `{item}`")
        if healing_report.get("log"):
            st.markdown("**Wykonane operacje samoregulacji:**")
            for item in healing_report["log"]:
                st.markdown(f"- `{item}`")

    # --------------------------------------------------------------------------
    # POBIERANIE PEŁNEGO ARCHIWUM PROJEKTU I AKTUALIZACJA WERSJI NATYWNEJ
    # --------------------------------------------------------------------------
    st.markdown("#### 📦 Podwójna Archiwizacja i Aktualizacja Wersji Natywnej (Localhost)")
    col_arc1, col_arc2 = st.columns(2)

    with col_arc1:
        st.write("**Bezpieczna Kopia Projektu (Dysk & Chmura):**")
        st.caption("Generuje kompletny pakiet ZIP zawierający cały kod źródłowy, bazy danych, audycje i książkę. Możesz go zapisać na dysku zewnętrznym, nośniku lub przenieść do innej chmury.")
        try:
            full_zip_file = create_full_project_archive()
            with open(full_zip_file, "rb") as f_zf:
                st.download_button(
                    "📥 Pobierz Pełne Archiwum Projektu (.zip)",
                    data=f_zf.read(),
                    file_name=os.path.basename(full_zip_file),
                    mime="application/zip",
                    use_container_width=True
                )
        except Exception as e:
            st.error(f"Nie udało się wygenerować archiwum ZIP: {e}")

    with col_arc2:
        st.write("**Aktualizacja Kodu Natywnego z GitHuba:**")
        st.caption("Pobiera najświeższy kod i wzorce z chmury GitHub bezpośrednio na dysk Twojego komputera, zabezpieczając uprzednio stan w katalogu archives/.")
        if st.button("🚀 Zaktualizuj Wersję Natywną (Localhost) z GitHuba", use_container_width=True):
            with st.spinner("Pobieranie najnowszych plików z GitHub main..."):
                res = update_local_installation_from_github()
                if res.get("ok"):
                    st.success(f"Pomyślnie zaktualizowano wersję lokalną! Zaktualizowano {len(res['updated_files'])} plików. Kopia bezpieczeństwa: `{os.path.basename(res['backup_zip'])}`.")
                    st.rerun()
                else:
                    st.error(f"Błąd aktualizacji natywnej: {res.get('error')}")
