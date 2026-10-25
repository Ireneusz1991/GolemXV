// The Golem 15: A Human's Road to Reality
// Główny moduł aplikacji (obsługa API serwera + automatyczny fallback localStorage)

const DEFAULT_SEED = {
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
      "subprojectId": null,
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
      "subprojectId": null,
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
      "subprojectId": null,
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
      "subprojectId": null,
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
      "subprojectId": null,
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
      "subprojectId": null,
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
  ]
};

const STORAGE_KEY = "the_golem_15_state_v8_private";
const ADMIN_AUTH_KEY = "golem_xv_admin_auth_pbkdf2";
const TRUSTED_DEVICE_KEY = "golem_15_trusted_device_token";
const LANG_STORAGE_KEY = "golem_15_ui_lang";

const appState = {
  data: null,
  isAdmin: false,
  deviceTrusted: false,
  lang: localStorage.getItem(LANG_STORAGE_KEY) === "en" ? "en" : "pl",
  sourceLangFilter: "ALL",
  serverOnline: false,
  activeTab: "study",
  selectedTrackFilter: "ALL",
  selectedSubprojectId: "sub-1",
  materialFilterTrack: "ALL",
  materialSearch: "",
  selectedGraphNode: null
};

const FOUNDATION_EN = {
  "FND-1": {
    name: "Mathematics & Logic",
    description: "Formal apparatus essential for physical modeling, computational neuroscience, data analysis, and AI algorithms.",
    topics: [
      "Propositional calculus, predicate logic, and set theory",
      "Linear algebra (vectors, matrices, eigenvalues, tensor spaces)",
      "Mathematical analysis and differential & integral calculus",
      "Ordinary and partial differential equations (dynamical systems)",
      "Probability theory and mathematical statistics",
      "Information theory (Shannon entropy, mutual information) and graph theory"
    ]
  },
  "FND-2": {
    name: "Computer Science",
    description: "Foundations of information processing, computer architecture, operating systems, networks, and computational complexity.",
    topics: [
      "Models of computation, Turing machine, and computational complexity",
      "Data structures and graph, search, and optimization algorithms",
      "Computer architecture (CPU, GPU, TPU, memory hierarchy, buses)",
      "Operating systems, concurrency, and real-time systems (RTOS)",
      "Databases, distributed storage, and knowledge graphs",
      "Cybersecurity, cryptography, and medical/research data integrity"
    ]
  },
  "FND-3": {
    name: "Programming & Software Engineering",
    description: "Practical creation of simulations, control software, embedded firmware, and data processing pipelines.",
    topics: [
      "Scientific and numerical programming (Python, Julia, C++, Rust)",
      "Low-level and embedded programming (C, microcontrollers, FPGA/VHDL)",
      "Physical, biological, and neural simulation tools",
      "Critical systems software engineering, testing, and formal verification",
      "Version control (Git), containerization, and reproducible research",
      "Communication interfaces, hardware APIs, and biomedical signal acquisition"
    ]
  },
  "FND-4": {
    name: "Physics",
    description: "Fundamental laws governing matter, energy, fields, and physical carriers of computation.",
    topics: [
      "Classical mechanics, continuum mechanics, and biomechanics",
      "Thermodynamics, statistical physics, and non-equilibrium physics (life & brain)",
      "Electromagnetism, Maxwell's equations, and wave propagation in media",
      "Optics, photonics, and laser spectroscopy",
      "Quantum mechanics, solid-state physics, and semiconductors",
      "Radiation physics, dosimetry, and orbital mechanics (for Track F)"
    ]
  },
  "FND-5": {
    name: "Electronics & Dynamical Systems",
    description: "Bridge between physics and computer science: sensors, actuators, analog circuits, neuromorphic chips, and control theory.",
    topics: [
      "Analog circuit theory, operational amplifiers, and filters",
      "Digital electronics, combinational/sequential logic, and microprocessors",
      "Signal processing (DSP), A/D and D/A converters, and biological signal filtering",
      "Control theory, feedback loops, PID, and state-space control",
      "Measurement sensors, biosensors, and mechatronic actuators",
      "Neuromorphic circuits, memristors, and analog physical computers (Track C)"
    ]
  },
  "FND-6": {
    name: "Chemistry & Biochemistry",
    description: "Molecular foundation of matter, metabolism, biomaterials, and closed life-support cycles.",
    topics: [
      "General and inorganic chemistry (chemical bonds, kinetics, thermochemistry)",
      "Organic chemistry and polymer chemistry (biomaterials and scaffolds)",
      "Structural and metabolic biochemistry (proteins, enzymes, nucleic acids)",
      "Electrochemistry (membrane potentials, electrochemical sensors, batteries)",
      "Analytical and environmental chemistry (water, air, and soil monitoring)",
      "Supramolecular chemistry and drug/gene delivery systems"
    ]
  },
  "FND-7": {
    name: "Biology, Neurobiology & Physiology",
    description: "Study of living organisms, nervous systems, genetics, tissue regeneration, and ecology.",
    topics: [
      "Molecular and cell biology (organelles, cell cycle, signaling)",
      "Genetics, genomics, epigenetics, and gene expression regulation",
      "Human anatomy and systems physiology (nervous, circulatory, muscular)",
      "Neurobiology and electrophysiology (neurons, synapses, plasticity, connectome)",
      "Developmental biology, stem cells, and tissue engineering",
      "Systems ecology, microbiology, and biosphere cycles (Tracks F & G)"
    ]
  },
  "FND-8": {
    name: "Artificial Intelligence & Machine Learning",
    description: "Statistical learning, deep neural networks, neuro-decoding, and intelligent control.",
    topics: [
      "Statistical learning, regression, classification, and probabilistic models",
      "Deep neural networks (MLP, CNN, RNN, Transformers, Graph Neural Networks)",
      "Reinforcement Learning and autonomous robotics control",
      "Biomedical signal decoding (EEG/ECoG/EMG) for Brain-Computer Interfaces (BCI)",
      "Spiking Neural Networks (SNN) and biologically plausible learning rules",
      "AI interpretability, safety, alignment, and formal model limits"
    ]
  }
};

const TRACK_EN = {
  A: {
    code: "Project A",
    name: "Bio-Digital & Robotic Human",
    goal: "Integration of the human organism with technology, medicine, neuroengineering, and robotics.",
    guidingQuestion: "How far can the human body be repaired, replaced, or augmented without losing health, identity, and agency?"
  },
  B: {
    code: "Project B",
    name: "Digital Mind",
    goal: "Computational neuroscience, brain modeling, cognitive architectures, and long-term Whole Brain Emulation (WBE) research.",
    guidingQuestion: "Which aspects of mental processes can be faithfully modeled or emulated in computational systems?"
  },
  C: {
    code: "Project C",
    name: "Analog Machines & Physical Computing",
    goal: "Computing through continuous physical dynamics, neuromorphic electronics, photonics, and quantum systems.",
    guidingQuestion: "How can physical dynamics directly perform computation beyond standard digital architectures?"
  },
  D: {
    code: "Project D",
    name: "'Frankenstein': Bioengineering & Synthetic Biology",
    goal: "Genetics, stem cells, organoids, tissue engineering, and synthetic biology alongside cultural analysis of creating life.",
    guidingQuestion: "Where lies the boundary between tissue regeneration and creating a new synthetic organism?"
  },
  E: {
    code: "Project E",
    name: "Philosophy as a Cross-Cutting Layer",
    goal: "Philosophy of science, philosophy of mind, philosophy of technology, and bioethics across all tracks.",
    guidingQuestion: "How do we distinguish proven empirical knowledge from hypotheses and speculation while preserving human dignity?"
  },
  F: {
    code: "Project F",
    name: "Human in Space",
    goal: "Space physiology, radiation protection, closed-loop life support systems (BLSS), and extraterrestrial habitats.",
    guidingQuestion: "What biological and technological conditions are required for long-term human survival beyond Earth?"
  },
  G: {
    code: "Project G",
    name: "Human on Earth: Adaptation & Biosphere Protection",
    goal: "Systems ecology, climate adaptation, environmental engineering, and biosphere regeneration.",
    guidingQuestion: "How can technology and ecological science protect Earth's biosphere as humanity's primary habitat?"
  },
  H: {
    code: "Super-Project H",
    name: "Nuclear & Fusion Energy (Power Architecture Across Sub-Variants A–G)",
    goal: "Fission reactors (SMR, HTGR-POLA), MARIA research reactor, nuclear medicine isotopes, space nuclear power (RTG, Kilopower), fusion energy, and powering gigawatt AI/WBE clusters.",
    guidingQuestion: "How can we provide safe, zero-emission, ultra-dense nuclear and fusion energy to power AI/brain emulation clusters, space habitats, nuclear medicine, and Earth's decarbonization?"
  }
};

function detectSourceLang(textBlob, explicitCode = "") {
  const code = (explicitCode || "").toUpperCase().trim();
  if (code === "PL" || code === "EN" || code === "PL+EN") return code;
  const raw = String(textBlob || "");
  const hasPl =
    raw.includes("🇵🇱") ||
    /pwn|helion|zpe\.gov|openagh|ważniak|polsku|wydanie polskie|pzwl|forbot|polsa|gios\.gov|polsl\.pl|ccpress/i.test(raw);
  const hasEn =
    raw.includes("🇬🇧") ||
    /mit press|cambridge|oxford|arxiv|ncbi|stanford|openstax\.org\/details\/books\/chemistry-2e|openstax\.org\/details\/books\/biology-2e|nature|ieee|roadmap-report/i.test(raw);
  if (hasPl && hasEn) return "PL+EN";
  if (hasPl) return "PL";
  return "EN";
}

function renderLangBadgeHtml(langCode) {
  const isEn = appState.lang === "en";
  if (langCode === "PL") {
    return `<span class="lang-tag lang-pl">🇵🇱 ${isEn ? "[PL — Polish]" : "[PL — Język polski]"}</span>`;
  }
  if (langCode === "PL+EN") {
    return `<span class="lang-tag lang-plen">🇵🇱/🇬🇧 ${isEn ? "[PL + EN — Bilingual]" : "[PL + EN — Dwujęzyczne]"}</span>`;
  }
  return `<span class="lang-tag lang-en">🇬🇧 ${isEn ? "[EN — English]" : "[EN — Język angielski]"}</span>`;
}

function matchesSourceLangFilter(itemLangCode) {
  if (!appState.sourceLangFilter || appState.sourceLangFilter === "ALL") return true;
  if (appState.sourceLangFilter === "PL") return itemLangCode === "PL" || itemLangCode === "PL+EN";
  if (appState.sourceLangFilter === "EN") return itemLangCode === "EN" || itemLangCode === "PL+EN";
  return true;
}

function onGlobalSourceLangFilterChange(val) {
  appState.sourceLangFilter = val || "ALL";
  renderAll();
}

function setLanguage(lang) {
  appState.lang = lang === "en" ? "en" : "pl";
  localStorage.setItem(LANG_STORAGE_KEY, appState.lang);
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === appState.lang);
  });
  applyStaticTranslations();
  renderAll();
}

function applyStaticTranslations() {
  const isEn = appState.lang === "en";
  const setTxt = (id, pl, en) => {
    const el = document.getElementById(id);
    if (el) el.textContent = isEn ? en : pl;
  };
  setTxt(
    "lockBadgeText",
    "🔒 PRYWATNY PROJEKT BADAWCZY — DOSTĘP WYŁĄCZNIE DLA WŁAŚCICIELA",
    "🔒 PRIVATE RESEARCH PROJECT — OWNER ACCESS ONLY"
  );
  setTxt(
    "lockSubText",
    "Projekt zamknięty dla osób postronnych. Podgląd i edycja wymagają uwierzytelnienia właściciela (PBKDF2-SHA256) lub autoryzowanego urządzenia.",
    "Project closed to outsiders. Viewing and editing require Owner Authentication (PBKDF2-SHA256) or an Authorized Owner Device."
  );
  setTxt(
    "lockPassLabel",
    "Klucz dostępu właściciela (PBKDF2-HMAC-SHA256)",
    "Owner Access Key (PBKDF2-HMAC-SHA256)"
  );
  setTxt(
    "trustDeviceLabel",
    "💻 Autoryzuj wyłącznie to urządzenie (pomiń hasło przy kolejnych wizytach w tej przeglądarce)",
    "💻 Authorize this device exclusively (skip password on future visits in this browser)"
  );
  setTxt("gatekeeperSubmitBtn", "🔓 Odblokuj prywatny portal", "🔓 Unlock Private Portal");
  setTxt(
    "headerSubtitleText",
    "Prywatny Portal Badawczy Właściciela • 8 Dziedzin Podstawowych (1–8) • 7 Ścieżek (A–G)",
    "Private Owner Research Portal • 8 Core Foundations (1–8) • 7 Research Tracks (A–G)"
  );
  setTxt("authToggleBtn", "🔒 Zablokuj", "🔒 Lock");
  setTxt("navTabStudyLabel", "🎓 1. Materiały do nauki i Biblioteka", "🎓 1. Study Materials & Library");
  setTxt("navTabMapLabel", "🗺️ 2. Mapa 7 Ścieżek (A–G)", "🗺️ 2. 7 Research Tracks Map (A–G)");
  setTxt("navTabWsLabel", "🔬 3. Środowiska Badawcze", "🔬 3. Research Workspaces");
  setTxt("navTabMatLabel", "📚 4. Repozytorium Badawcze", "📚 4. Research Repository");
  setTxt("navTabGraphLabel", "🕸️ 5. Graf Powiązań (A–G)", "🕸️ 5. Connections Graph (A–G)");
  setTxt("navTabSecurityLabel", "🛡️ 6. Bezpieczeństwo i Urządzenie", "🛡️ 6. Security & Device");

  setTxt(
    "compassHeaderBadge",
    "🧭 Architektura Orientacyjna Projektu (OSF • ResearchHub • Most Wiedzy • Heptabase)",
    "🧭 Project Wayfinding Architecture (OSF • ResearchHub • Most Wiedzy • Heptabase)"
  );
  setTxt(
    "compassSubText",
    "Kliknij wybraną warstwę fundamentów (1–8) lub ścieżkę (A–G), albo użyj wyszukiwarki poniżej. Wszystkie źródła posiadają oznaczenie języka [PL] / [EN].",
    "Click any foundation layer (1–8) or research track (A–G), or use the search bar below. Every source includes a language badge [PL] / [EN]."
  );
  setTxt("axis1Title", "🏛️ Oś I: 8 Dziedzin Podstawowych (po kolei)", "🏛️ Axis I: 8 Core Foundations (Sequential)");
  setTxt("axis2Title", "🗺️ Oś II: 7 Ścieżek Badawczych (A–G)", "🗺️ Axis II: 7 Research Tracks (A–G)");
  setTxt("axis3Title", "🔒 Oś III: Oznaczenia Języka i Rygor Epistemiczny", "🔒 Axis III: Source Language & Epistemic Status");
  setTxt(
    "studyHeaderTitle",
    "🎓 Materiały do nauki — 8 dziedzin ze Wspólnych podstaw po kolei oraz odnogi Projektów A–G",
    "🎓 Study Materials — 8 Core Foundations in Sequence & Tracks A–G Branches"
  );
  setTxt(
    "studyHeaderDesc",
    "Przeglądaj kolejne dziedziny fundamentalne (1–8), dodawaj własne materiały do nauki i uruchamiaj środowiska. Każdy materiał posiada oznaczenie języka źródła ([PL], [EN], [PL+EN]).",
    "Explore the 8 core scientific foundations (1–8), add your own study materials, and launch workspaces. Each source is tagged with its language ([PL], [EN], [PL+EN])."
  );
  setTxt("btnAddStudyMatTop", "+ Dodaj materiał do nauki", "+ Add Study Material");
  setTxt("btnAddStudyWsTop", "🚀 Uruchom środowisko dla dziedziny", "🚀 Launch Foundation Workspace");
  setTxt(
    "studyTracksHeaderTitle",
    "🧭 Materiały do nauki i Biblioteka według Ścieżek A–G",
    "🧭 Study Materials & Library by Research Tracks A–G"
  );
  setTxt(
    "mapHeaderTitle",
    "Siedem powiązanych ścieżek badawczych (Projekty A–G)",
    "Seven Interconnected Research Tracks (Projects A–G)"
  );
}

function getExpectedDeviceToken() {
  const auth = getActiveAdminAuth();
  if (!auth || !auth.hash || !auth.salt) return "";
  return `${auth.salt.slice(0, 12)}_${auth.hash.slice(0, 28)}_g15_trusted`;
}

function updateLockScreenVisibility() {
  const lockEl = document.getElementById("ownerLockScreen");
  const mainEl = document.getElementById("appMainRoot");
  const unlocked = Boolean(appState.isAdmin || appState.deviceTrusted);
  if (lockEl) lockEl.style.display = unlocked ? "none" : "flex";
  if (mainEl) mainEl.style.display = unlocked ? "flex" : "none";
}

function lockOwnerPortal() {
  appState.isAdmin = false;
  appState.deviceTrusted = false;
  sessionStorage.removeItem("golem_xv_is_admin");
  updateLockScreenVisibility();
  showToast(appState.lang === "en" ? "Portal locked." : "Portal został zablokowany.");
}

function revokeDeviceTrust() {
  localStorage.removeItem(TRUSTED_DEVICE_KEY);
  appState.deviceTrusted = false;
  showToast(
    appState.lang === "en"
      ? "Device authorization revoked. Password will be required on next visit."
      : "Autoryzacja tego urządzenia została cofnięta."
  );
  renderAll();
}

function authorizeCurrentBrowserDevice() {
  const tok = getExpectedDeviceToken();
  if (tok) {
    localStorage.setItem(TRUSTED_DEVICE_KEY, tok);
    appState.deviceTrusted = true;
    showToast(
      appState.lang === "en"
        ? "This browser/device is now authorized for direct owner access!"
        : "To urządzenie zostało autoryzowane jako zaufane urządzenie właściciela!"
    );
    renderAll();
  }
}

async function submitOwnerGatekeeper(e) {
  e.preventDefault();
  const passInput = document.getElementById("gatekeeperPassInput");
  const trustCheck = document.getElementById("trustDeviceCheckbox");
  const errBox = document.getElementById("gatekeeperErrorBox");
  const candidate = passInput ? passInput.value : "";

  const ok = await verifyAdminPasswordCrypto(candidate);
  if (ok) {
    appState.isAdmin = true;
    sessionStorage.setItem("golem_xv_is_admin", "true");
    if (trustCheck && trustCheck.checked) {
      const tok = getExpectedDeviceToken();
      if (tok) {
        localStorage.setItem(TRUSTED_DEVICE_KEY, tok);
        appState.deviceTrusted = true;
      }
    }
    if (passInput) passInput.value = "";
    if (errBox) errBox.style.display = "none";
    updateLockScreenVisibility();
    renderAll();
    showToast(
      appState.lang === "en"
        ? "Welcome, Ireneusz! Owner portal unlocked."
        : "Witaj, Ireneusz! Prywatny portal został odblokowany."
    );
  } else {
    if (errBox) {
      errBox.style.display = "block";
      errBox.textContent =
        appState.lang === "en"
          ? "Access denied — invalid owner password."
          : "Odmowa dostępu — nieprawidłowe hasło właściciela.";
    }
  }
}

function ensureSchema(d) {
  if (!d.projectMeta) d.projectMeta = JSON.parse(JSON.stringify(DEFAULT_SEED.projectMeta));
  d.projectMeta.title = "The Golem 15: A Human's Road to Reality";
  delete d.projectMeta.adminPassword;
  delete d.verifiedResearchers;
  if (!d.projectMeta.adminAuth || !d.projectMeta.adminAuth.hash) {
    d.projectMeta.adminAuth = JSON.parse(JSON.stringify(DEFAULT_SEED.projectMeta.adminAuth));
  }
  if (!d.foundationDisciplines || !d.foundationDisciplines.length) {
    d.foundationDisciplines = JSON.parse(JSON.stringify(DEFAULT_SEED.foundationDisciplines));
  }
  const seedSmatMap = new Map((DEFAULT_SEED.studyMaterials || []).map((m) => [m.id, m]));
  if (!d.studyMaterials) {
    d.studyMaterials = JSON.parse(JSON.stringify(DEFAULT_SEED.studyMaterials));
  } else {
    d.studyMaterials = d.studyMaterials.map((m) =>
      seedSmatMap.has(m.id) ? JSON.parse(JSON.stringify(seedSmatMap.get(m.id))) : m
    );
    const existingIds = new Set(d.studyMaterials.map((m) => m.id));
    (DEFAULT_SEED.studyMaterials || []).forEach((m) => {
      if (!existingIds.has(m.id)) d.studyMaterials.push(JSON.parse(JSON.stringify(m)));
    });
  }
  const seedMatMap = new Map((DEFAULT_SEED.materials || []).map((m) => [m.id, m]));
  if (!d.materials) {
    d.materials = JSON.parse(JSON.stringify(DEFAULT_SEED.materials));
  } else {
    d.materials = d.materials.map((m) =>
      seedMatMap.has(m.id) ? JSON.parse(JSON.stringify(seedMatMap.get(m.id))) : m
    );
    const existingMatIds = new Set(d.materials.map((m) => m.id));
    (DEFAULT_SEED.materials || []).forEach((m) => {
      if (!existingMatIds.has(m.id)) d.materials.push(JSON.parse(JSON.stringify(m)));
    });
  }
  d.tracks = JSON.parse(JSON.stringify(DEFAULT_SEED.tracks));
  const existingSpIds = new Set((d.subprojects || []).map((s) => s.id));
  (DEFAULT_SEED.subprojects || []).forEach((s) => {
    if (!existingSpIds.has(s.id)) d.subprojects.push(JSON.parse(JSON.stringify(s)));
  });
  const existingLnkIds = new Set((d.graphLinks || []).map((l) => l.id));
  (DEFAULT_SEED.graphLinks || []).forEach((l) => {
    if (!existingLnkIds.has(l.id)) d.graphLinks.push(JSON.parse(JSON.stringify(l)));
  });
  d.supplementaryLibrary = JSON.parse(JSON.stringify(DEFAULT_SEED.supplementaryLibrary));
  return d;
}

async function initApp() {
  localStorage.removeItem("golem_xv_admin_pass");
  await loadState();

  const expectedTok = getExpectedDeviceToken();
  const urlParams = new URLSearchParams(window.location.search);
  const urlDeviceTok = urlParams.get("device_token");

  if (expectedTok && urlDeviceTok && constantTimeEqual(urlDeviceTok, expectedTok)) {
    localStorage.setItem(TRUSTED_DEVICE_KEY, expectedTok);
    appState.deviceTrusted = true;
    appState.isAdmin = true;
  } else if (expectedTok && localStorage.getItem(TRUSTED_DEVICE_KEY) === expectedTok) {
    appState.deviceTrusted = true;
    appState.isAdmin = true;
  } else if (sessionStorage.getItem("golem_xv_is_admin") === "true") {
    appState.isAdmin = true;
  }

  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === appState.lang);
  });
  applyStaticTranslations();
  updateLockScreenVisibility();
  if (appState.isAdmin || appState.deviceTrusted) {
    renderAll();
  }
}

async function loadState() {
  try {
    const res = await fetch("/api/state", { cache: "no-store" });
    if (res.ok) {
      appState.data = ensureSchema(await res.json());
      appState.serverOnline = true;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(appState.data));
      updateServerBadge();
      return;
    }
  } catch (e) {
    // Brak serwera HTTP -> localStorage
  }

  appState.serverOnline = false;
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    try {
      appState.data = ensureSchema(JSON.parse(saved));
    } catch {
      appState.data = JSON.parse(JSON.stringify(DEFAULT_SEED));
    }
  } else {
    appState.data = JSON.parse(JSON.stringify(DEFAULT_SEED));
    localStorage.setItem(STORAGE_KEY, JSON.stringify(appState.data));
  }
  updateServerBadge();
}

async function saveState(toastMsg) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(appState.data));
  if (appState.serverOnline) {
    try {
      const res = await fetch("/api/state", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(appState.data)
      });
      if (!res.ok) throw new Error("Save error");
    } catch {
      appState.serverOnline = false;
      updateServerBadge();
    }
  }
  if (toastMsg) showToast(toastMsg);
  renderAll();
}

function updateServerBadge() {
  const el = document.getElementById("serverStatusBadge");
  if (!el) return;
  const isEn = appState.lang === "en";
  if (appState.serverOnline) {
    el.innerHTML = `<span class="status-dot" style="background:#10b981"></span> ${isEn ? "Server DB Active" : "Baza serwerowa aktywna"}`;
  } else {
    el.innerHTML = `<span class="status-dot" style="background:#38bdf8"></span> ${isEn ? "Private Browser Storage" : "Baza lokalna właściciela"}`;
  }
}

function showToast(message) {
  const container = document.getElementById("toastContainer");
  if (!container) return;
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function formatTextWithLinks(str) {
  if (!str) return "";
  let escaped = escapeHtml(str);
  escaped = escaped.replace(
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; text-decoration:underline; font-weight:600;">🔗 $1</a>'
  );
  escaped = escaped.replace(
    /(^|[^"'>])(https?:\/\/[^\s<)]+)/g,
    '$1<a href="$2" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; text-decoration:underline;">$2</a>'
  );
  return escaped;
}

function renderLinksBlock(item) {
  const links = item.links || [];
  const isEn = appState.lang === "en";
  if (links.length > 0) {
    return `
      <div style="margin-top:0.5rem; padding-top:0.4rem; border-top:1px dashed rgba(148,163,184,0.2);">
        <div style="font-size:0.75rem; font-weight:700; color:#38bdf8; margin-bottom:0.25rem;">🔗 ${isEn ? "Source Links & Language:" : "Odnośniki źródłowe i język materiału:"}</div>
        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.25rem;">
          ${links
            .map((l) => {
              const lCode = detectSourceLang(`${l.label || ""} ${l.url || ""}`);
              const tag = lCode === "PL" ? `<span class="lang-tag lang-pl" style="font-size:0.65rem; padding:0.05rem 0.4rem;">[PL 🇵🇱]</span>` : `<span class="lang-tag lang-en" style="font-size:0.65rem; padding:0.05rem 0.4rem;">[EN 🇬🇧]</span>`;
              return `<li style="font-size:0.8rem; display:flex; align-items:center; gap:0.35rem; flex-wrap:wrap;">${tag} <a href="${escapeHtml(l.url)}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; text-decoration:underline;">${escapeHtml(l.label)}</a></li>`;
            })
            .join("")}
        </ul>
      </div>
    `;
  }
  if (item.url) {
    const lCode = detectSourceLang(item.url, item.sourceLang);
    return `
      <div style="margin-top:0.45rem; display:flex; align-items:center; gap:0.4rem;">
        ${renderLangBadgeHtml(lCode)}
        <a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-size:0.82rem; font-weight:600; text-decoration:underline;">🔗 ${isEn ? "Open source material" : "Otwórz materiał źródłowy"}</a>
      </div>
    `;
  }
  return "";
}

function getTrackOrFoundationById(id) {
  const isEn = appState.lang === "en";
  const tr = appState.data.tracks.find((t) => t.id === id);
  if (tr) {
    return {
      ...tr,
      code: isEn && TRACK_EN[id] ? TRACK_EN[id].code : tr.code,
      name: isEn && TRACK_EN[id] ? TRACK_EN[id].name : tr.name,
      goal: isEn && TRACK_EN[id] ? TRACK_EN[id].goal : tr.goal,
      guidingQuestion: isEn && TRACK_EN[id] ? TRACK_EN[id].guidingQuestion : tr.guidingQuestion
    };
  }
  const fnd = (appState.data.foundationDisciplines || []).find((f) => f.id === id);
  if (fnd) {
    const fEn = FOUNDATION_EN[id];
    return {
      id: fnd.id,
      code: isEn ? `Foundation ${fnd.order}` : `Podstawy ${fnd.order}`,
      name: isEn && fEn ? fEn.name : fnd.name,
      color: fnd.color,
      sections: [{ title: isEn ? "Study Topics" : "Działy do nauki", items: isEn && fEn ? fEn.topics : fnd.topics }]
    };
  }
  return { id, code: id, name: id, color: "#38bdf8", sections: [] };
}

function switchTab(tabName) {
  appState.activeTab = tabName;
  renderAll();
}

function openTrackWorkspaceFilter(trackId) {
  appState.selectedTrackFilter = trackId;
  const matching = appState.data.subprojects.find((s) => s.trackId === trackId);
  if (matching) {
    appState.selectedSubprojectId = matching.id;
  }
  switchTab("workspaces");
}

function renderAll() {
  if (!appState.data) return;
  updateLockScreenVisibility();
  if (!appState.isAdmin && !appState.deviceTrusted) return;

  updateServerBadge();
  renderHeaderRole();
  renderNavCounts();

  document.querySelectorAll(".nav-tab").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.tab === appState.activeTab);
  });

  document.querySelectorAll(".tab-view").forEach((view) => {
    view.style.display = view.id === `view-${appState.activeTab}` ? "block" : "none";
  });

  if (appState.activeTab === "study") renderStudyView();
  if (appState.activeTab === "map") renderMapView();
  if (appState.activeTab === "workspaces") renderWorkspacesView();
  if (appState.activeTab === "materials") renderMaterialsView();
  if (appState.activeTab === "graph") renderGraphView();
  if (appState.activeTab === "moderation") renderModerationView();
}

function renderHeaderRole() {
  const roleBadge = document.getElementById("roleBadge");
  if (!roleBadge) return;
  const isEn = appState.lang === "en";
  roleBadge.className = "role-badge admin";
  roleBadge.innerHTML = appState.deviceTrusted
    ? `<span>💻</span> ${isEn ? "Owner: Ireneusz (Authorized Device)" : "Właściciel: Ireneusz (Zaufane Urządzenie)"}`
    : `<span>🛡️</span> ${isEn ? "Owner: Ireneusz (Authenticated)" : "Właściciel: Ireneusz (Zalogowany)"}`;
}

function renderNavCounts() {
  const studyCountEl = document.getElementById("navStudyCount");
  const subCountEl = document.getElementById("navSubprojectsCount");
  const matCountEl = document.getElementById("navMaterialsCount");

  if (studyCountEl) studyCountEl.textContent = (appState.data.studyMaterials || []).length;
  if (subCountEl) subCountEl.textContent = (appState.data.subprojects || []).length;
  if (matCountEl) matCountEl.textContent = (appState.data.materials || []).length;
}

function renderGlobalWayfindingResults(query) {
  const box = document.getElementById("globalWayfindingResults");
  if (!box) return;
  const q = (query || "").trim().toLowerCase();
  if (!q) {
    box.style.display = "none";
    box.innerHTML = "";
    return;
  }
  const hits = [];
  (appState.data.foundationDisciplines || []).forEach((f) => {
    const fEn = FOUNDATION_EN[f.id] || {};
    if (`${f.name} ${fEn.name || ""} ${f.description} ${(f.topics || []).join(" ")}`.toLowerCase().includes(q)) {
      hits.push(`<div>🏛️ <strong>${f.order}. ${escapeHtml(appState.lang === "en" && fEn.name ? fEn.name : f.name)}</strong> — <a href="javascript:void(0)" onclick="switchTab('study')" style="color:#38bdf8;">Otwórz</a></div>`);
    }
  });
  (appState.data.studyMaterials || []).forEach((sm) => {
    const blob = `${sm.title} ${sm.content} ${sm.topic} ${JSON.stringify(sm.links || [])}`;
    const lCode = detectSourceLang(blob, sm.sourceLang);
    if (matchesSourceLangFilter(lCode) && blob.toLowerCase().includes(q)) {
      hits.push(`<div>🎓 ${renderLangBadgeHtml(lCode)} <strong>[${escapeHtml(sm.targetId)}] ${escapeHtml(sm.title)}</strong> — <a href="javascript:void(0)" onclick="switchTab('study')" style="color:#38bdf8;">Materiały do nauki</a></div>`);
    }
  });
  (appState.data.materials || []).forEach((m) => {
    const blob = `${m.title} ${m.content} ${m.branchTopic} ${JSON.stringify(m.links || [])}`;
    const lCode = detectSourceLang(blob, m.sourceLang);
    if (matchesSourceLangFilter(lCode) && blob.toLowerCase().includes(q)) {
      hits.push(`<div>📚 ${renderLangBadgeHtml(lCode)} <strong>[Projekt ${escapeHtml(m.trackId)}] ${escapeHtml(m.title)}</strong> — <a href="javascript:void(0)" onclick="switchTab('materials')" style="color:#38bdf8;">Repozytorium</a></div>`);
    }
  });

  box.style.display = "block";
  box.innerHTML = hits.length
    ? `<div style="display:flex; flex-direction:column; gap:0.35rem; font-size:0.82rem;">${hits.slice(0, 12).join("")}</div>`
    : `<div style="font-size:0.82rem; color:var(--text-muted);">Brak dopasowań dla „${escapeHtml(query)}”.</div>`;
}

// --- WIDOK 0: MATERIAŁY DO NAUKI ---
function renderStudyView() {
  const fndGrid = document.getElementById("foundationsGrid");
  const tracksTree = document.getElementById("tracksStudyTree");
  if (!fndGrid) return;
  const isEn = appState.lang === "en";

  const foundations = (appState.data.foundationDisciplines || []).slice().sort((a, b) => a.order - b.order);

  fndGrid.innerHTML = foundations
    .map((fnd) => {
      const fEn = FOUNDATION_EN[fnd.id] || {};
      const fName = isEn && fEn.name ? fEn.name : fnd.name;
      const fDesc = isEn && fEn.description ? fEn.description : fnd.description;
      const fTopics = isEn && fEn.topics ? fEn.topics : fnd.topics;

      const mats = (appState.data.studyMaterials || []).filter((sm) => {
        if (sm.categoryType !== "FOUNDATION" || sm.targetId !== fnd.id) return false;
        const lCode = detectSourceLang(`${sm.title} ${sm.content} ${JSON.stringify(sm.links || [])}`, sm.sourceLang);
        return matchesSourceLangFilter(lCode);
      });
      const subCount = appState.data.subprojects.filter((s) => s.trackId === fnd.id).length;

      return `
      <div class="track-card" style="--track-color: ${fnd.color}">
        <div>
          <div class="track-header">
            <div>
              <span class="track-code">${isEn ? `CORE FOUNDATION • ${fnd.order} OF 8` : `WSPÓLNE PODSTAWY • DZIEDZINA ${fnd.order} z 8`}</span>
              <h3 class="track-title">${fnd.icon} ${escapeHtml(fName)}</h3>
            </div>
            <button class="btn btn-sm btn-primary" onclick="openNewStudyMaterialModal('FOUNDATION', '${fnd.id}', '')">
              + ${isEn ? "Add Material" : "Materiał do nauki"}
            </button>
          </div>
          <p class="track-goal">${escapeHtml(fDesc)}</p>

          <div class="track-sections">
            <div class="track-section-block">
              <h4>${isEn ? "Sequential Study Topics" : "Program nauki po kolei (zagadnienia i działy)"}</h4>
              <ul class="branch-list">
                ${fTopics
                  .map(
                    (topic, idx) => `
                  <li class="branch-item">
                    <span><strong>${fnd.order}.${idx + 1}.</strong> ${escapeHtml(topic)}</span>
                    <div style="display:flex; gap:0.35rem;">
                      <button class="btn btn-sm branch-launch-btn" onclick="openNewStudyMaterialModal('FOUNDATION', '${fnd.id}', '${escapeHtml(topic).replace(/'/g, "\\'")}')">
                        + ${isEn ? "Material" : "Materiał"}
                      </button>
                      <button class="btn btn-sm branch-launch-btn" onclick="openNewSubprojectModal('${fnd.id}', '${escapeHtml(topic).replace(/'/g, "\\'")}')">
                        🚀 ${isEn ? "Workspace" : "Środowisko"}
                      </button>
                    </div>
                  </li>
                `
                  )
                  .join("")}
              </ul>
            </div>

            <div class="track-section-block">
              <h4>${isEn ? `Assigned Study Materials (${mats.length})` : `Przypisane materiały do nauki (${mats.length})`}</h4>
              ${
                mats.length === 0
                  ? `<p style="font-size:0.8rem; color:var(--text-muted);">${isEn ? "No study materials for the active filter." : "Brak materiałów dla wybranego filtru."}</p>`
                  : mats
                      .map((m) => {
                        const lCode = detectSourceLang(`${m.title} ${m.content} ${JSON.stringify(m.links || [])}`, m.sourceLang);
                        return `
                    <div class="ws-card" style="margin-bottom:0.5rem;">
                      <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.3rem; flex-wrap:wrap;">
                        ${renderLangBadgeHtml(lCode)}
                        <span class="foundation-pill" style="font-size:0.7rem;">${escapeHtml(m.format)} • ${escapeHtml(m.level)}</span>
                      </div>
                      <strong style="font-size:0.9rem;">📖 ${escapeHtml(m.title)}</strong>
                      <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:0.25rem;">${isEn ? "Topic" : "Dział"}: ${escapeHtml(m.topic)}</div>
                      <p style="font-size:0.82rem; color:var(--text-secondary); white-space:pre-line;">${formatTextWithLinks(m.content)}</p>
                      ${renderLinksBlock(m)}
                    </div>
                  `;
                      })
                      .join("")
              }
            </div>
          </div>
        </div>

        <div class="track-footer">
          <div class="track-stats">
            <span>📖 ${isEn ? "Materials" : "Materiały"}: <strong>${mats.length}</strong></span>
            <span>🔬 ${isEn ? "Workspaces" : "Środowiska"}: <strong>${subCount}</strong></span>
          </div>
          <button class="btn btn-sm" onclick="openNewSubprojectModal('${fnd.id}', '')">
            🚀 ${isEn ? "New Workspace" : "Nowe środowisko"} (${escapeHtml(fName)})
          </button>
        </div>
      </div>
    `;
    })
    .join("");

  if (tracksTree) {
    const suppLib = appState.data.supplementaryLibrary || {};
    const suppProjects = suppLib.projects || [];
    const suppRules = suppLib.rules || [];
    const readingOrder = suppLib.readingOrder || null;

    const readingOrderHtml = readingOrder
      ? `
        <div class="ws-card" style="margin-top:0.75rem; border-left:3px solid #10b981;">
          <h4 style="margin-bottom:0.45rem; color:#10b981;">🧭 ${escapeHtml(readingOrder.title || "VI. KOLEJNOŚĆ CZYTANIA")}</h4>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:0.75rem; margin-bottom:0.55rem;">
            ${(readingOrder.stages || [])
              .map(
                (st) => `
              <div style="background:rgba(15,23,42,0.65); padding:0.55rem 0.7rem; border-radius:8px; border:1px solid rgba(148,163,184,0.18);">
                <strong style="font-size:0.82rem; color:#38bdf8;">${escapeHtml(st.stage)}</strong>
                <ul style="margin:0.35rem 0 0; padding-left:1.1rem; font-size:0.8rem; color:var(--text-secondary);">
                  ${(st.items || []).map((it) => `<li>${formatTextWithLinks(it)}</li>`).join("")}
                </ul>
              </div>
            `
              )
              .join("")}
          </div>
        </div>
      `
      : "";

    const suppBannerHtml =
      suppProjects.length > 0
        ? `
      <div class="overview-banner" style="grid-column: 1 / -1; margin-bottom: 1rem; border-color: rgba(16, 185, 129, 0.45);">
        <div class="overarching-goal">
          <h2>📚 ${escapeHtml(suppLib.title || "BIBLIOTEKA PROJEKTU GOLEM 15")}</h2>
          <p>${escapeHtml(suppLib.description || "")}</p>
        </div>
        <div class="ws-card" style="margin-top:0.75rem;">
          <h4 style="margin-bottom:0.45rem; color:#38bdf8;">📌 ${isEn ? "Library Principles (1–6)" : "Zasady korzystania z biblioteki (1–6)"}</h4>
          <ol style="padding-left:1.3rem; margin:0; font-size:0.86rem; color:var(--text-secondary); line-height:1.6;">
            ${suppRules.map((r) => `<li>${escapeHtml(r)}</li>`).join("")}
          </ol>
        </div>
        ${readingOrderHtml}
      </div>
    `
        : "";

    tracksTree.innerHTML =
      suppBannerHtml +
      appState.data.tracks
        .map((tr) => {
          const tObj = getTrackOrFoundationById(tr.id);
          const mats = (appState.data.studyMaterials || []).filter((sm) => {
            if (sm.categoryType !== "TRACK" || sm.targetId !== tr.id) return false;
            const lCode = detectSourceLang(`${sm.title} ${sm.content} ${JSON.stringify(sm.links || [])}`, sm.sourceLang);
            return matchesSourceLangFilter(lCode);
          });
          const suppProj = suppProjects.find((sp) => sp.trackId === tr.id);

          return `
        <div class="track-card" style="--track-color: ${tr.color}">
          <div>
            <div class="track-header">
              <div>
                <span class="track-code">${escapeHtml(tObj.code)}</span>
                <h3 class="track-title">${escapeHtml(tObj.name)}</h3>
              </div>
              <button class="btn btn-sm btn-primary" onclick="openNewStudyMaterialModal('TRACK', '${tr.id}', '')">
                + ${isEn ? "Study Material" : "Materiał do nauki"}
              </button>
            </div>
            <div class="track-sections">
              ${
                suppProj
                  ? `
                <div class="track-section-block" style="border: 1px solid rgba(56, 189, 248, 0.35); background: rgba(15, 23, 42, 0.78); padding: 0.75rem; border-radius: 8px;">
                  <h4 style="color:#38bdf8;">📚 ${escapeHtml(suppProj.title)}</h4>
                  ${
                    suppProj.sequence
                      ? `<div style="margin:0.4rem 0 0.65rem; padding:0.45rem 0.65rem; border-radius:8px; background:rgba(16,185,129,0.12); border-left:3px solid #10b981; font-size:0.82rem;">
                          <strong>🧭 ${escapeHtml(suppProj.sequenceLabel || "Kolejność nauki")}:</strong> ${escapeHtml(suppProj.sequence)}
                        </div>`
                      : ""
                  }
                  ${(suppProj.groups || [])
                    .map((ssec) => {
                      const gLang = ssec.heading.toLowerCase().includes("polsku") ? "PL" : ssec.heading.toLowerCase().includes("angielsku") ? "EN" : "PL+EN";
                      return `
                    <div style="margin-top:0.5rem;">
                      <div style="display:flex; align-items:center; gap:0.4rem; margin-bottom:0.25rem;">
                        ${renderLangBadgeHtml(gLang)}
                        <strong style="font-size:0.78rem; text-transform:uppercase; color:var(--text-secondary);">${escapeHtml(ssec.heading)}</strong>
                      </div>
                      <ul class="branch-list">
                        ${(ssec.items || [])
                          .map((it) => `<li class="branch-item" style="font-size:0.82rem;"><span>• ${formatTextWithLinks(it)}</span></li>`)
                          .join("")}
                      </ul>
                    </div>
                  `;
                    })
                    .join("")}
                  ${renderLinksBlock(suppProj)}
                </div>
              `
                  : ""
              }
              ${
                mats.length > 0
                  ? `<div class="track-section-block">
                      <h4>${isEn ? `Study Materials (${mats.length})` : `Materiały do nauki (${mats.length})`}</h4>
                      ${mats
                        .map((m) => {
                          const lCode = detectSourceLang(`${m.title} ${m.content} ${JSON.stringify(m.links || [])}`, m.sourceLang);
                          return `
                        <div class="ws-card" style="margin-bottom:0.45rem;">
                          <div style="margin-bottom:0.25rem;">${renderLangBadgeHtml(lCode)}</div>
                          <strong>📖 ${escapeHtml(m.title)}</strong> (${escapeHtml(m.level)})
                          <div style="font-size:0.75rem; color:var(--text-muted);">${escapeHtml(m.topic)}</div>
                          <p style="font-size:0.82rem; color:var(--text-secondary); white-space:pre-line;">${formatTextWithLinks(m.content)}</p>
                          ${renderLinksBlock(m)}
                        </div>
                      `;
                        })
                        .join("")}
                    </div>`
                  : ""
              }
            </div>
          </div>
        </div>
      `;
        })
        .join("");
  }
}

// --- WIDOK 1: MAPA PROJEKTU (ŚCIEŻKI A-G) ---
function renderMapView() {
  const meta = appState.data.projectMeta;
  const isEn = appState.lang === "en";
  const bannerEl = document.getElementById("overviewBanner");
  bannerEl.innerHTML = `
    <div class="overarching-goal">
      <h2>${isEn ? "Overarching Goal" : "Cel nadrzędny przedsięwzięcia"}</h2>
      <p><strong>${escapeHtml(isEn ? "To examine and advance the scientific, engineering, biological, computational, and philosophical foundations of understanding, augmenting, and protecting the human being across 7 research tracks (A–G)." : meta.overarchingGoal)}</strong></p>
      <p style="font-size:0.86rem; color:var(--text-muted)">${escapeHtml(meta.organizationalRule)}</p>
    </div>
    <div class="fg-relation-box">
      <h3>${isEn ? "Track F ↔ Track G Relation (Space ↔ Earth)" : "Relacja między projektami F i G (Kosmos ↔ Ziemia)"}</h3>
      <p>${escapeHtml(meta.fgRelation.summary)}</p>
      <p>• <strong>Kosmos (F):</strong> ${escapeHtml(meta.fgRelation.fPerspective)}</p>
      <p>• <strong>Ziemia (G):</strong> ${escapeHtml(meta.fgRelation.gPerspective)}</p>
    </div>
  `;

  const gridEl = document.getElementById("tracksGrid");
  gridEl.innerHTML = appState.data.tracks
    .map((track) => {
      const tObj = getTrackOrFoundationById(track.id);
      const subCount = appState.data.subprojects.filter((s) => s.trackId === track.id).length;
      const matCount = appState.data.materials.filter((m) => m.trackId === track.id).length;
      const isCrossCutting = track.id === "E";

      return `
      <div class="track-card ${isCrossCutting ? "cross-cutting" : ""}" style="--track-color: ${track.color}">
        <div>
          <div class="track-header">
            <div>
              <span class="track-code">${escapeHtml(tObj.code)}</span>
              <h3 class="track-title">${escapeHtml(tObj.name)}</h3>
            </div>
            <button class="btn btn-sm" onclick="openNewSubprojectModal('${track.id}', '')">
              + ${isEn ? "Workspace" : "Środowisko"}
            </button>
          </div>
          <p class="track-goal"><strong>${isEn ? "Goal" : "Cel"}:</strong> ${escapeHtml(tObj.goal)}</p>
          <div class="guiding-question">
            <strong>${isEn ? "Guiding Question" : "Pytanie przewodnie"}:</strong> ${escapeHtml(tObj.guidingQuestion)}
          </div>
          <div class="track-sections">
            ${track.sections
              .map(
                (sec) => `
              <div class="track-section-block">
                <h4>${escapeHtml(sec.title)}</h4>
                <ul class="branch-list">
                  ${sec.items
                    .map(
                      (item) => `
                    <li class="branch-item">
                      <span>• ${escapeHtml(item)}</span>
                      <div style="display:flex; gap:0.35rem;">
                        <button class="btn btn-sm branch-launch-btn" onclick="openNewSubprojectModal('${track.id}', '${escapeHtml(item).replace(/'/g, "\\'")}')">
                          🚀 ${isEn ? "Workspace" : "Środowisko"}
                        </button>
                        <button class="btn btn-sm branch-launch-btn" onclick="openNewMaterialModal('${track.id}', '${escapeHtml(item).replace(/'/g, "\\'")}')">
                          + ${isEn ? "Material" : "Materiał"}
                        </button>
                      </div>
                    </li>
                  `
                    )
                    .join("")}
                </ul>
              </div>
            `
              )
              .join("")}
          </div>
        </div>
        <div class="track-footer">
          <div class="track-stats">
            <span>🔬 ${isEn ? "Workspaces" : "Środowiska"}: <strong>${subCount}</strong></span>
            <span>📚 ${isEn ? "Materials" : "Materiały"}: <strong>${matCount}</strong></span>
          </div>
          <div style="display:flex; gap:0.45rem;">
            <button class="btn btn-sm" onclick="openTrackWorkspaceFilter('${track.id}')">${isEn ? "Open Workspaces" : "Otwórz środowiska"} (${subCount})</button>
          </div>
        </div>
      </div>
    `;
    })
    .join("");
}

// --- WIDOK 2: ŚRODOWISKA BADAWCZE I PODPROJEKTY ---
function renderWorkspacesView() {
  const isEn = appState.lang === "en";
  const filterSelect = document.getElementById("wsTrackFilter");
  if (filterSelect) {
    filterSelect.value = appState.selectedTrackFilter;
  }

  const visibleSubprojects = appState.data.subprojects.filter((sp) => {
    return (
      appState.selectedTrackFilter === "ALL" ||
      sp.trackId === appState.selectedTrackFilter ||
      (sp.secondaryTracks && sp.secondaryTracks.includes(appState.selectedTrackFilter))
    );
  });

  if (
    visibleSubprojects.length > 0 &&
    !visibleSubprojects.some((s) => s.id === appState.selectedSubprojectId)
  ) {
    appState.selectedSubprojectId = visibleSubprojects[0].id;
  }

  const listEl = document.getElementById("subprojectsList");
  if (visibleSubprojects.length === 0) {
    listEl.innerHTML = `<p style="color:var(--text-muted); font-size:0.86rem;">${isEn ? "No workspaces for this filter." : "Brak podprojektów dla wybranego filtru."}</p>`;
  } else {
    listEl.innerHTML = visibleSubprojects
      .map((sp) => {
        const track = getTrackOrFoundationById(sp.trackId);
        const activeClass = sp.id === appState.selectedSubprojectId ? "active" : "";
        return `
        <div class="subproject-item ${activeClass}" onclick="selectSubproject('${sp.id}')">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.3rem;">
            <span style="font-size:0.74rem; font-weight:700; color:${track.color};">${escapeHtml(track.code)} — ${escapeHtml(track.name)}</span>
          </div>
          <div style="font-weight:600; font-size:0.92rem; margin-bottom:0.25rem;">${escapeHtml(sp.title)}</div>
          <div style="font-size:0.78rem; color:var(--text-muted);">${escapeHtml(sp.branchTopic || "")}</div>
        </div>
      `;
      })
      .join("");
  }

  const activeSp = appState.data.subprojects.find((s) => s.id === appState.selectedSubprojectId);
  const panelEl = document.getElementById("activeWorkspacePanel");
  if (!activeSp) {
    panelEl.innerHTML = `<div style="text-align:center; padding:3rem 1rem; color:var(--text-muted);"><h3>${isEn ? "Select a workspace on the left" : "Wybierz środowisko z listy po lewej stronie"}</h3></div>`;
    return;
  }

  const primaryTrack = getTrackOrFoundationById(activeSp.trackId);
  const ws = activeSp.workspace || { hypotheses: [], notes: [], bibliography: [] };

  panelEl.innerHTML = `
    <div style="border-bottom:1px solid var(--border-color); padding-bottom:1.1rem;">
      <span class="track-code" style="color:${primaryTrack.color};">${escapeHtml(primaryTrack.code)} — ${escapeHtml(primaryTrack.name)}</span>
      <h2 style="font-size:1.35rem; margin-bottom:0.3rem;">${escapeHtml(activeSp.title)}</h2>
      <p style="font-size:0.84rem; color:var(--text-muted);"><strong>${isEn ? "Branch" : "Odnoga"}:</strong> ${escapeHtml(activeSp.branchTopic || "")}</p>
      <p style="margin-top:0.75rem; color:var(--text-secondary); font-size:0.92rem;">${escapeHtml(activeSp.description)}</p>
      ${
        activeSp.philosophicalNote
          ? `<div class="track-note" style="margin-top:0.75rem; margin-bottom:0;">
              <strong>Projekt E (Filozofia):</strong> ${escapeHtml(activeSp.philosophicalNote)}
            </div>`
          : ""
      }
    </div>

    <div class="workspace-grid">
      <div class="ws-section">
        <h4>
          <span>1. ${isEn ? "Hypotheses" : "Hipotezy badawcze"} (${(ws.hypotheses || []).length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('hypothesis', '${activeSp.id}')">+ ${isEn ? "Add" : "Hipoteza"}</button>
        </h4>
        ${(ws.hypotheses || [])
          .map(
            (h) => `
          <div class="ws-card">
            <span class="foundation-pill" style="font-size:0.7rem;">${escapeHtml(h.status || "Hipoteza otwarta")}</span>
            <p style="margin:0.4rem 0;">${escapeHtml(h.statement)}</p>
          </div>
        `
          )
          .join("")}
      </div>

      <div class="ws-section">
        <h4>
          <span>2. ${isEn ? "Research Notes" : "Notatnik badawczy"} (${(ws.notes || []).length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('note', '${activeSp.id}')">+ ${isEn ? "Add" : "Notatka"}</button>
        </h4>
        ${(ws.notes || [])
          .map(
            (n) => `
          <div class="ws-card">
            <strong>${escapeHtml(n.title)}</strong>
            <p style="color:var(--text-secondary); margin:0.35rem 0;">${escapeHtml(n.content)}</p>
          </div>
        `
          )
          .join("")}
      </div>

      <div class="ws-section">
        <h4>
          <span>3. ${isEn ? "Bibliography & Sources" : "Bibliografia i źródła"} (${(ws.bibliography || []).length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('bibliography', '${activeSp.id}')">+ ${isEn ? "Add" : "Źródło"}</button>
        </h4>
        ${(ws.bibliography || [])
          .map((b) => {
            const lCode = detectSourceLang(`${b.citation} ${b.url || ""}`, b.sourceLang);
            return `
          <div class="ws-card">
            <div style="margin-bottom:0.25rem;">${renderLangBadgeHtml(lCode)}</div>
            <p>📖 ${escapeHtml(b.citation)}</p>
            ${b.url ? `<div style="margin-top:0.25rem;"><a href="${escapeHtml(b.url)}" target="_blank" style="color:#38bdf8; font-size:0.78rem;">🔗 ${escapeHtml(b.url)}</a></div>` : ""}
          </div>
        `;
          })
          .join("")}
      </div>
    </div>
  `;
}

function selectSubproject(id) {
  appState.selectedSubprojectId = id;
  renderWorkspacesView();
}

function onWorkspaceTrackFilterChange(val) {
  appState.selectedTrackFilter = val;
  renderWorkspacesView();
}

// --- WIDOK 3: REPOZYTORIUM MATERIAŁÓW ---
function renderMaterialsView() {
  const listEl = document.getElementById("materialsListContainer");
  const searchVal = (appState.materialSearch || "").toLowerCase();
  const trackFilter = appState.materialFilterTrack;

  const filtered = appState.data.materials.filter((m) => {
    if (trackFilter !== "ALL" && m.trackId !== trackFilter) return false;
    const blob = `${m.title} ${m.content} ${m.branchTopic || ""} ${JSON.stringify(m.links || [])}`;
    const lCode = detectSourceLang(blob, m.sourceLang);
    if (!matchesSourceLangFilter(lCode)) return false;
    if (searchVal && !blob.toLowerCase().includes(searchVal)) return false;
    return true;
  });

  if (filtered.length === 0) {
    listEl.innerHTML = `<div class="ws-card" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak materiałów spełniających kryteria.</div>`;
    return;
  }

  listEl.innerHTML = filtered
    .map((m) => {
      const track = getTrackOrFoundationById(m.trackId);
      const lCode = detectSourceLang(`${m.title} ${m.content} ${JSON.stringify(m.links || [])}`, m.sourceLang);
      return `
      <div class="ws-card" style="padding:1.15rem; border-left:4px solid ${track.color};">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.45rem;">
          <span class="track-code" style="color:${track.color}; margin:0;">${escapeHtml(track.code)}: ${escapeHtml(track.name)} • ${escapeHtml(m.type || "Materiał")}</span>
          ${renderLangBadgeHtml(lCode)}
        </div>
        <h3 style="font-size:1.08rem; margin-bottom:0.35rem;">${escapeHtml(m.title)}</h3>
        <p style="color:var(--text-secondary); margin-bottom:0.65rem; white-space:pre-line;">${formatTextWithLinks(m.content)}</p>
        ${renderLinksBlock(m)}
      </div>
    `;
    })
    .join("");
}

// --- WIDOK 4: INTERAKTYWNY GRAF POWIĄZAŃ (A-G) ---
function renderGraphView() {
  const svgWrapper = document.getElementById("graphSvgWrapper");
  const linksListEl = document.getElementById("graphLinksList");
  if (!svgWrapper) return;

  const coords = {
    E: { x: 360, y: 265 },
    H: { x: 560, y: 265 },
    A: { x: 190, y: 110 },
    B: { x: 450, y: 70 },
    C: { x: 710, y: 110 },
    D: { x: 190, y: 425 },
    F: { x: 450, y: 460 },
    G: { x: 710, y: 425 }
  };

  const visibleLinks = appState.data.graphLinks || [];

  const linesSvg = visibleLinks
    .map((lnk) => {
      const s = coords[lnk.source];
      const t = coords[lnk.target];
      if (!s || !t) return "";
      return `<line x1="${s.x}" y1="${s.y}" x2="${t.x}" y2="${t.y}" stroke="#475569" stroke-width="2" opacity="0.75" />`;
    })
    .join("");

  const nodesSvg = appState.data.tracks
    .map((tr) => {
      const tObj = getTrackOrFoundationById(tr.id);
      const c = coords[tr.id] || { x: 100, y: 100 };
      const r = tr.id === "E" ? 44 : 36;
      return `
      <g style="cursor:pointer;" onclick="selectGraphNode('${tr.id}')">
        <circle cx="${c.x}" cy="${c.y}" r="${r}" fill="#111827" stroke="${tr.color}" stroke-width="3" />
        <text x="${c.x}" y="${c.y + 4}" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="700">${escapeHtml(tObj.code)}</text>
        <text x="${c.x}" y="${c.y + r + 18}" text-anchor="middle" fill="#e2e8f0" font-size="11.5" font-weight="600">${escapeHtml(tObj.name)}</text>
      </g>
    `;
    })
    .join("");

  svgWrapper.innerHTML = `<svg viewBox="0 0 900 520" width="100%" height="100%">${linesSvg}${nodesSvg}</svg>`;
  linksListEl.innerHTML = `<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(290px, 1fr)); gap:0.75rem;">
    ${visibleLinks.map((l) => `<div class="ws-card"><strong>Projekt ${escapeHtml(l.source)} ↔ Projekt ${escapeHtml(l.target)}</strong><p style="font-size:0.84rem; color:var(--text-secondary);">${escapeHtml(l.label)}</p></div>`).join("")}
  </div>`;
}

function selectGraphNode(trackId) {
  appState.selectedGraphNode = trackId;
  renderGraphView();
}

// --- WIDOK 5: BEZPIECZEŃSTWO I AUTORYZACJA URZĄDZENIA WŁAŚCICIELA ---
function renderModerationView() {
  const container = document.getElementById("moderationContainer");
  if (!container) return;
  const isEn = appState.lang === "en";

  container.innerHTML = `
    <div class="filter-bar">
      <div>
        <h3 style="font-size:1.1rem;">🛡️ ${isEn ? "Owner Security, Password & Trusted Device Authorization" : "Bezpieczeństwo Projektu, Hasło Właściciela i Autoryzacja Urządzenia"}</h3>
        <p style="font-size:0.83rem; color:var(--text-muted);">
          ${isEn ? "This project is locked exclusively for you (Ireneusz). Manage your trusted device token and PBKDF2-HMAC-SHA256 cryptographic password below." : "Projekt jest zamknięty wyłącznie dla Ciebie (Ireneusz). Zarządzaj autoryzacją swojego urządzenia oraz hasłem kryptograficznym PBKDF2-HMAC-SHA256."}
        </p>
      </div>
      <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
        <button class="btn btn-primary" onclick="openChangeAdminPassModal()">🔑 ${isEn ? "Change Owner Password" : "Zmień hasło właściciela"}</button>
        <button class="btn" onclick="exportDatabaseJson()">⬇ ${isEn ? "Export JSON Backup" : "Eksportuj kopię JSON"}</button>
        <button class="btn btn-danger" onclick="lockOwnerPortal()">🔒 ${isEn ? "Lock Portal Now" : "Zablokuj portal teraz"}</button>
      </div>
    </div>

    <div class="workspace-grid">
      <div class="ws-section">
        <h4>💻 ${isEn ? "Exclusive Device Authorization" : "Autoryzacja Twojego Urządzenia"}</h4>
        <div class="ws-card">
          <p style="margin-bottom:0.75rem; color:var(--text-secondary);">
            ${
              appState.deviceTrusted
                ? isEn
                  ? "🟢 This browser/device is currently authorized as your trusted owner device. You can open the project directly without re-typing the password."
                  : "🟢 Ta przeglądarka i to urządzenie posiadają aktywną autoryzację właściciela. Możesz otwierać projekt bezpośrednio bez każdorazowego wpisywania hasła."
                : isEn
                ? "🟡 This browser is unlocked for the current session only."
                : "🟡 Ta przeglądarka jest odblokowana tylko na czas bieżącej sesji."
            }
          </p>
          <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
            <button class="btn btn-success" onclick="authorizeCurrentBrowserDevice()">✓ ${isEn ? "Authorize This Device" : "Autoryzuj to urządzenie na stałe"}</button>
            <button class="btn btn-danger" onclick="revokeDeviceTrust()">🚫 ${isEn ? "Revoke Device Authorization" : "Cofnij autoryzację tego urządzenia"}</button>
          </div>
        </div>
      </div>

      <div class="ws-section">
        <h4>🔐 ${isEn ? "Cryptographic Protection Status" : "Status Ochrony Kryptograficznej"}</h4>
        <div class="ws-card">
          <p>• <strong>Algorytm:</strong> PBKDF2-HMAC-SHA256 (260 000 iteracji)</p>
          <p>• <strong>Tryb dostępu:</strong> Prywatny (Single-Owner Gatekeeper — brak dostępu dla osób postronnych)</p>
          <p>• <strong>Właściciel i jedyny autor:</strong> Ireneusz</p>
        </div>
      </div>
    </div>
  `;
}

function closeModal() {
  document.getElementById("modalBackdrop").classList.remove("open");
}

function openNewStudyMaterialModal(categoryType = "FOUNDATION", targetId = "FND-1", defaultTopic = "") {
  const modalBody = document.getElementById("modalContentBox");
  const targetObj = getTrackOrFoundationById(targetId);

  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🎓 Dodaj materiał do nauki (${escapeHtml(targetObj.name)})</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewStudyMaterial(event, '${categoryType}', '${targetId}')">
      <div class="form-group">
        <label>Konkretny dział / zagadnienie</label>
        <input type="text" id="smTopicInput" class="input-field" value="${escapeHtml(defaultTopic)}" required />
      </div>
      <div class="form-group">
        <label>Tytuł materiału do nauki</label>
        <input type="text" id="smTitleInput" class="input-field" required />
      </div>
      <div class="form-group">
        <label>Język materiału źródłowego</label>
        <select id="smLangSelect" class="select-field">
          <option value="PL">🇵🇱 [PL — Język polski]</option>
          <option value="EN">🇬🇧 [EN — Język angielski]</option>
          <option value="PL+EN">🇵🇱/🇬🇧 [PL + EN — Dwujęzyczne]</option>
        </select>
      </div>
      <div class="form-group">
        <label>Poziom zaawansowania</label>
        <select id="smLevelSelect" class="select-field">
          <option value="Podstawowy">Podstawowy</option>
          <option value="Średniozaawansowany">Średniozaawansowany</option>
          <option value="Zaawansowany / Akademicki">Zaawansowany / Akademicki</option>
        </select>
      </div>
      <div class="form-group">
        <label>Format materiału</label>
        <select id="smFormatSelect" class="select-field">
          <option value="Podręcznik / Książka">Podręcznik / Książka</option>
          <option value="Kurs / Wykład">Kurs / Wykład</option>
          <option value="Notatka własna">Notatka własna</option>
          <option value="Kod / Symulacja">Kod / Symulacja</option>
        </select>
      </div>
      <div class="form-group">
        <label>Opis i wskazówki do nauki</label>
        <textarea id="smContentInput" class="textarea-field" rows="3" required></textarea>
      </div>
      <div class="form-group">
        <label>Link zewnętrzny (opcjonalnie)</label>
        <input type="url" id="smUrlInput" class="input-field" placeholder="https://..." />
      </div>
      <div style="display:flex; justify-content:flex-end; margin-top:1rem;">
        <button type="submit" class="btn btn-primary">Zapisz materiał do nauki</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitNewStudyMaterial(e, categoryType, targetId) {
  e.preventDefault();
  appState.data.studyMaterials.unshift({
    id: "smat-" + Date.now(),
    categoryType,
    targetId,
    topic: document.getElementById("smTopicInput").value.trim(),
    title: document.getElementById("smTitleInput").value.trim(),
    sourceLang: document.getElementById("smLangSelect").value,
    level: document.getElementById("smLevelSelect").value,
    format: document.getElementById("smFormatSelect").value,
    content: document.getElementById("smContentInput").value.trim(),
    url: document.getElementById("smUrlInput").value.trim(),
    author: "Ireneusz",
    status: "approved",
    createdAt: new Date().toISOString()
  });
  closeModal();
  saveState("Materiał do nauki został zapisany!");
}

function openNewSubprojectModal(defaultTrackId = "A", defaultBranch = "") {
  const modalBody = document.getElementById("modalContentBox");
  const allTargets = [
    ...(appState.data.foundationDisciplines || []).map((f) => ({
      id: f.id,
      label: `Podstawy ${f.order}: ${f.name}`
    })),
    ...appState.data.tracks.map((t) => ({
      id: t.id,
      label: `${t.code} — ${t.name}`
    }))
  ];

  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🚀 Nowy podprojekt i środowisko badawcze</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewSubproject(event)">
      <div class="form-group">
        <label>Dziedzina podstawowa (1–8) lub Ścieżka projektu (A–G)</label>
        <select id="spTrackSelect" class="select-field" required>
          ${allTargets
            .map(
              (t) =>
                `<option value="${t.id}" ${t.id === defaultTrackId ? "selected" : ""}>${escapeHtml(t.label)}</option>`
            )
            .join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Odnoga zakresu badawczego / dział</label>
        <input type="text" id="spBranchInput" class="input-field" value="${escapeHtml(defaultBranch)}" required />
      </div>
      <div class="form-group">
        <label>Tytuł podprojektu / środowiska badawczego</label>
        <input type="text" id="spTitleInput" class="input-field" required />
      </div>
      <div class="form-group">
        <label>Cel i opis problemu badawczego</label>
        <textarea id="spDescInput" class="textarea-field" rows="3" required></textarea>
      </div>
      <div class="form-group">
        <label>Hipoteza startowa (opcjonalnie)</label>
        <input type="text" id="spInitialHypothesis" class="input-field" />
      </div>
      <div style="display:flex; justify-content:flex-end; margin-top:1rem;">
        <button type="submit" class="btn btn-primary">Utwórz środowisko badawcze</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitNewSubproject(e) {
  e.preventDefault();
  const trackId = document.getElementById("spTrackSelect").value;
  const branchTopic = document.getElementById("spBranchInput").value.trim();
  const title = document.getElementById("spTitleInput").value.trim();
  const description = document.getElementById("spDescInput").value.trim();
  const initialHyp = document.getElementById("spInitialHypothesis").value.trim();
  const newId = "sub-" + Date.now();

  appState.data.subprojects.unshift({
    id: newId,
    trackId,
    secondaryTracks: ["E"],
    branchTopic,
    title,
    author: "Ireneusz",
    status: "approved",
    createdAt: new Date().toISOString(),
    description,
    philosophicalNote: "",
    workspace: {
      hypotheses: initialHyp
        ? [
            {
              id: "hyp-" + Date.now(),
              statement: initialHyp,
              status: "Hipoteza otwarta",
              author: "Ireneusz",
              approvalStatus: "approved"
            }
          ]
        : [],
      notes: [],
      bibliography: []
    }
  });

  appState.selectedTrackFilter = "ALL";
  appState.selectedSubprojectId = newId;
  closeModal();
  switchTab("workspaces");
  saveState("Środowisko badawcze zostało utworzone!");
}

function openNewMaterialModal(defaultTrackId = "A", defaultBranch = "") {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>📚 Dodaj materiał badawczy</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewMaterial(event)">
      <div class="form-group">
        <label>Ścieżka projektu (A–G)</label>
        <select id="matTrackSelect" class="select-field" required>
          ${appState.data.tracks.map((t) => `<option value="${t.id}" ${t.id === defaultTrackId ? "selected" : ""}>${escapeHtml(t.code)} — ${escapeHtml(t.name)}</option>`).join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Odnoga badawcza</label>
        <input type="text" id="matBranchInput" class="input-field" value="${escapeHtml(defaultBranch)}" />
      </div>
      <div class="form-group">
        <label>Język materiału źródłowego</label>
        <select id="matLangSelect" class="select-field">
          <option value="PL">🇵🇱 [PL — Język polski]</option>
          <option value="EN">🇬🇧 [EN — Język angielski]</option>
          <option value="PL+EN">🇵🇱/🇬🇧 [PL + EN — Dwujęzyczne]</option>
        </select>
      </div>
      <div class="form-group">
        <label>Tytuł materiału</label>
        <input type="text" id="matTitleInput" class="input-field" required />
      </div>
      <div class="form-group">
        <label>Treść / Notatka</label>
        <textarea id="matContentInput" class="textarea-field" rows="4" required></textarea>
      </div>
      <div class="form-group">
        <label>Link zewnętrzny / DOI (opcjonalnie)</label>
        <input type="url" id="matUrlInput" class="input-field" placeholder="https://..." />
      </div>
      <div style="display:flex; justify-content:flex-end; margin-top:1rem;">
        <button type="submit" class="btn btn-primary">Zapisz materiał</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitNewMaterial(e) {
  e.preventDefault();
  appState.data.materials.unshift({
    id: "mat-" + Date.now(),
    trackId: document.getElementById("matTrackSelect").value,
    branchTopic: document.getElementById("matBranchInput").value.trim(),
    subprojectId: null,
    title: document.getElementById("matTitleInput").value.trim(),
    sourceLang: document.getElementById("matLangSelect").value,
    type: "Opracowanie własne",
    author: "Ireneusz",
    content: document.getElementById("matContentInput").value.trim(),
    url: document.getElementById("matUrlInput").value.trim(),
    status: "approved",
    createdAt: new Date().toISOString()
  });
  closeModal();
  saveState("Materiał został zapisany.");
}

function openWorkspaceEntryModal(entryType, spId) {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>Dodaj wpis do środowiska</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitWorkspaceEntry(event, '${entryType}', '${spId}')">
      ${entryType === "note" ? `<div class="form-group"><label>Tytuł</label><input type="text" id="wsEntryTitle" class="input-field" required /></div>` : ""}
      ${entryType === "bibliography" ? `<div class="form-group"><label>Język źródła</label><select id="wsEntryLang" class="select-field"><option value="PL">🇵🇱 [PL]</option><option value="EN">🇬🇧 [EN]</option><option value="PL+EN">🇵🇱/🇬🇧 [PL+EN]</option></select></div>` : ""}
      <div class="form-group">
        <label>Treść</label>
        <textarea id="wsEntryText" class="textarea-field" rows="3" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Zapisz</button>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitWorkspaceEntry(e, entryType, spId) {
  e.preventDefault();
  const sp = appState.data.subprojects.find((s) => s.id === spId);
  if (!sp) return;
  if (entryType === "hypothesis") {
    sp.workspace.hypotheses.push({
      id: "hyp-" + Date.now(),
      statement: document.getElementById("wsEntryText").value.trim(),
      status: "Hipoteza otwarta",
      author: "Ireneusz",
      approvalStatus: "approved"
    });
  } else if (entryType === "note") {
    sp.workspace.notes.push({
      id: "note-" + Date.now(),
      title: document.getElementById("wsEntryTitle").value.trim(),
      content: document.getElementById("wsEntryText").value.trim(),
      author: "Ireneusz",
      approvalStatus: "approved"
    });
  } else {
    sp.workspace.bibliography.push({
      id: "bib-" + Date.now(),
      citation: document.getElementById("wsEntryText").value.trim(),
      sourceLang: document.getElementById("wsEntryLang") ? document.getElementById("wsEntryLang").value : "PL",
      url: "",
      addedBy: "Ireneusz",
      approvalStatus: "approved"
    });
  }
  closeModal();
  saveState("Dodano wpis do środowiska.");
}

function hexToBytes(hex) {
  const bytes = new Uint8Array(hex.length / 2);
  for (let i = 0; i < bytes.length; i++) {
    bytes[i] = parseInt(hex.substr(i * 2, 2), 16);
  }
  return bytes;
}

function bytesToHex(bytes) {
  return Array.from(bytes)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

function constantTimeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return diff === 0;
}

async function derivePbkdf2Hex(password, saltHex, iterations = 260000) {
  const enc = new TextEncoder();
  const keyMaterial = await window.crypto.subtle.importKey(
    "raw",
    enc.encode(password),
    { name: "PBKDF2" },
    false,
    ["deriveBits"]
  );
  const derivedBits = await window.crypto.subtle.deriveBits(
    {
      name: "PBKDF2",
      salt: hexToBytes(saltHex),
      iterations: Number(iterations),
      hash: "SHA-256"
    },
    keyMaterial,
    256
  );
  return bytesToHex(new Uint8Array(derivedBits));
}

function getActiveAdminAuth() {
  const savedAuth = localStorage.getItem(ADMIN_AUTH_KEY);
  if (savedAuth) {
    try {
      const parsed = JSON.parse(savedAuth);
      if (parsed && parsed.salt && parsed.hash) return parsed;
    } catch {
      // ignore invalid JSON
    }
  }
  if (appState.data && appState.data.projectMeta && appState.data.projectMeta.adminAuth) {
    return appState.data.projectMeta.adminAuth;
  }
  return DEFAULT_SEED.projectMeta.adminAuth;
}

async function verifyAdminPasswordCrypto(candidatePassword) {
  if (!candidatePassword) return false;
  const auth = getActiveAdminAuth();
  if (!auth || !auth.salt || !auth.hash) return false;
  try {
    const derived = await derivePbkdf2Hex(candidatePassword, auth.salt, auth.iterations || 260000);
    return constantTimeEqual(derived, auth.hash);
  } catch {
    return false;
  }
}

function openChangeAdminPassModal() {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🔑 Zmień hasło właściciela (PBKDF2-SHA256)</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitChangeAdminPass(event)">
      <div class="form-group">
        <label>Aktualne hasło właściciela</label>
        <input type="password" id="currentAdminPassInput" class="input-field" value="" required />
      </div>
      <div class="form-group">
        <label>Nowe hasło właściciela (min. 8 znaków)</label>
        <input type="password" id="newAdminPassInput" class="input-field" value="" minlength="8" required />
      </div>
      <div class="form-group">
        <label>Powtórz nowe hasło</label>
        <input type="password" id="confirmAdminPassInput" class="input-field" value="" minlength="8" required />
      </div>
      <button type="submit" class="btn btn-primary">Zaszyfruj i zapisz nowe hasło</button>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

async function submitChangeAdminPass(e) {
  e.preventDefault();
  const currentPass = document.getElementById("currentAdminPassInput").value;
  const newPass = document.getElementById("newAdminPassInput").value.trim();
  const confirmPass = document.getElementById("confirmAdminPassInput").value.trim();
  if (!(await verifyAdminPasswordCrypto(currentPass))) {
    showToast("Aktualne hasło jest nieprawidłowe.");
    return;
  }
  if (newPass.length < 8) {
    showToast("Nowe hasło musi mieć co najmniej 8 znaków.");
    return;
  }
  if (newPass !== confirmPass) {
    showToast("Nowe hasła nie są identyczne.");
    return;
  }
  const saltBytes = new Uint8Array(16);
  window.crypto.getRandomValues(saltBytes);
  const saltHex = bytesToHex(saltBytes);
  const iterations = 260000;
  const hashHex = await derivePbkdf2Hex(newPass, saltHex, iterations);
  const newAuth = {
    algorithm: "pbkdf2_sha256",
    iterations,
    salt: saltHex,
    hash: hashHex
  };
  localStorage.setItem(ADMIN_AUTH_KEY, JSON.stringify(newAuth));
  if (appState.data && appState.data.projectMeta) {
    appState.data.projectMeta.adminAuth = newAuth;
    delete appState.data.projectMeta.adminPassword;
  }
  if (appState.deviceTrusted) {
    localStorage.setItem(TRUSTED_DEVICE_KEY, getExpectedDeviceToken());
  }
  closeModal();
  await saveState("Hasło właściciela zostało zaszyfrowane (PBKDF2-SHA256) i zaktualizowane!");
}

function exportDatabaseJson() {
  const blob = new Blob([JSON.stringify(appState.data, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "the_golem_15_private_backup.json";
  a.click();
  URL.revokeObjectURL(url);
}

window.addEventListener("DOMContentLoaded", initApp);
