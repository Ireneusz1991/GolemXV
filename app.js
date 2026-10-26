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
        "parentId": null,
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
};

const STORAGE_KEY = "the_golem_15_state_v8_private";
const ADMIN_AUTH_KEY = "golem_xv_admin_auth_pbkdf2";
const TRUSTED_DEVICE_KEY = "golem_15_trusted_device_token";
const LANG_STORAGE_KEY = "golem_15_ui_lang";
const THEME_STORAGE_KEY = "golem_15_ui_theme";

const appState = {
  data: null,
  isAdmin: false,
  deviceTrusted: false,
  lang: localStorage.getItem(LANG_STORAGE_KEY) === "en" ? "en" : "pl",
  theme: localStorage.getItem(THEME_STORAGE_KEY) === "dark" ? "dark" : "light",
  sourceLangFilter: "ALL",
  serverOnline: false,
  activeTab: "manhattan",
  manhattanSiteFilter: "ALL",
  selectedFissionNodeId: "FIS-00",
  fissionDbSearch: "",
  expandedStudyIds: { "ADMIN-3Y": true, "STU-FND-1": true, "STU-TRK-H": true },
  selectedTrackFilter: "ALL",
  selectedSubprojectId: "sub-1",
  materialFilterTrack: "ALL",
  materialSearch: "",
  selectedGraphNode: null,
  carAudioPlayingId: null,
  carAudioRate: 1.15,
  carAudioStageFilter: "ALL",
  carAudioAutoPlay: false,
  bookActiveChapterId: "ch-intro",
  bookIsEditing: false
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

function setTheme(theme) {
  appState.theme = theme === "dark" ? "dark" : "light";
  localStorage.setItem(THEME_STORAGE_KEY, appState.theme);
  document.documentElement.setAttribute("data-theme", appState.theme);
  const metaColor = document.getElementById("metaThemeColor");
  if (metaColor) {
    metaColor.setAttribute("content", appState.theme === "dark" ? "#0d1117" : "#f4f6f9");
  }
  document.querySelectorAll(".theme-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.themeBtn === appState.theme);
  });
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
  document.querySelectorAll(".theme-lbl-light").forEach((el) => {
    el.textContent = isEn ? "Light" : "Jasny";
  });
  document.querySelectorAll(".theme-lbl-dark").forEach((el) => {
    el.textContent = isEn ? "Dark" : "Ciemny";
  });
  setTxt(
    "editorialEditionLabel",
    "📰 Serwis Nauka & Technologia • Wydanie Badawcze G15",
    "📰 Science & Technology Portal • G15 Research Edition"
  );
  setTxt("edCatAdmin", "🏛️ Prawo i Administracja (3Y)", "🏛️ Law & Administration (3Y)");
  setTxt("edCatHealth", "🩺 Zdrowie i Bionika (A)", "🩺 Health & Bionics (A)");
  setTxt("edCatTech", "💻 Technologia i AI (B/C)", "💻 Technology & AI (B/C)");
  setTxt("edCatLife", "🧬 Życie i Biotechnologia (D)", "🧬 Life & Biotech (D)");
  setTxt("edCatEnergy", "⚛️ Materia i Energia (H)", "⚛️ Matter & Nuclear Energy (H)");
  setTxt("edCatSpace", "🛰️ Kosmos (F)", "🛰️ Space (F)");
  setTxt("edCatEarth", "🌍 Ziemia i Klimat (G)", "🌍 Earth & Climate (G)");
  setTxt("edCatHumanities", "📜 Człowiek i Filozofia (E)", "📜 Humanities & Philosophy (E)");
  setTxt(
    "lockBadgeText",
    "🔒 SERWIS NAUKOWO-BADAWCZY — DOSTĘP AUTORYZOWANY",
    "🔒 SCIENTIFIC RESEARCH PORTAL — AUTHORIZED ACCESS"
  );
  setTxt(
    "lockSubText",
    "Portal naukowo-badawczy zamknięty dla osób postronnych. Podgląd i edycja wymagają uwierzytelnienia właściciela (PBKDF2-SHA256) lub autoryzowanego urządzenia.",
    "Scientific research portal closed to outsiders. Viewing and editing require Owner Authentication (PBKDF2-SHA256) or an Authorized Owner Device."
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
  setTxt("gatekeeperSubmitBtn", "🔓 Odblokuj portal naukowy", "🔓 Unlock Research Portal");
  setTxt(
    "headerSubtitleText",
    "Portal Naukowo-Badawczy • Rozproszony System Manhattan (3 lata Administracji + 5×N lat z rzędu) • Graf Rozszczepień AI",
    "Scientific Research Portal • Manhattan Distributed System (3Y Admin + 5×N Back-to-Back Years) • AI Fission Graph"
  );
  setTxt("authToggleBtn", "🔒 Zablokuj", "🔒 Lock");
  setTxt(
    "navTabManhattanLabel",
    "☢️ 1. System Manhattan i Graf Rozszczepień AI",
    "☢️ 1. Manhattan System & AI Fission Graph"
  );
  setTxt(
    "navTabCarAudioLabel",
    "🎧 2. Audio do Samochodu (Celowa Droga)",
    "🎧 2. Car Audio Road (Purposeful Route)"
  );
  setTxt("navTabStudyLabel", "🎓 3. Materiały do nauki i Biblioteka", "🎓 3. Study Materials & Library");
  setTxt("navTabMapLabel", "🗺️ 4. Mapa Ścieżek (A–H)", "🗺️ 4. Research Tracks Map (A–H)");
  setTxt("navTabWsLabel", "🔬 5. Środowiska Badawcze", "🔬 5. Research Workspaces");
  setTxt("navTabMatLabel", "📚 6. Repozytorium Badawcze", "📚 6. Research Repository");
  setTxt(
    "navTabBookLabel",
    "📖 7. Summa Technologiae 2.0 (Książka Lema)",
    "📖 7. Summa Technologiae 2.0 (Lem's Opus)"
  );
  setTxt("navTabGraphLabel", "🕸️ 8. Graf Powiązań (A–H)", "🕸️ 8. Connections Graph (A–H)");
  setTxt("navTabSecurityLabel", "🛡️ 9. Bezpieczeństwo i Urządzenie", "🛡️ 9. Security & Device");

  setTxt(
    "compassHeaderBadge",
    "🧭 Katalog Działów i Architektura Projektu (Nauka w Polsce • Most Wiedzy • OSF)",
    "🧭 Editorial Sections & Project Architecture (Nauka w Polsce • Most Wiedzy • OSF)"
  );
  setTxt(
    "compassSubText",
    "Kliknij wybraną warstwę fundamentów (1–8) lub dział badawczy (A–H), albo użyj wyszukiwarki poniżej. Wszystkie źródła posiadają oznaczenie języka [PL] / [EN].",
    "Click any foundation layer (1–8) or research section (A–H), or use the search bar below. Every source includes a language badge [PL] / [EN]."
  );
  setTxt("axis1Title", "🏛️ Oś I: 8 Dziedzin Podstawowych (po kolei)", "🏛️ Axis I: 8 Core Foundations (Sequential)");
  setTxt("axis2Title", "🗺️ Oś II: 8 Działów Badawczych (A–H)", "🗺️ Axis II: 8 Research Sections (A–H)");
  setTxt("axis3Title", "🔒 Oś III: Oznaczenia Języka i Rygor Epistemiczny", "🔒 Axis III: Source Language & Epistemic Status");
  setTxt(
    "studyHeaderTitle",
    "🎓 Materiały do nauki — 8 dziedzin ze Wspólnych podstaw po kolei oraz odnogi Projektów A–H",
    "🎓 Study Materials — 8 Core Foundations in Sequence & Tracks A–H Branches"
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
    "🧭 Materiały do nauki i Biblioteka według Działów A–H",
    "🧭 Study Materials & Library by Research Sections A–H"
  );
  setTxt(
    "mapHeaderTitle",
    "Osiem powiązanych działów badawczych (Projekty A–H)",
    "Eight Interconnected Research Sections (Projects A–H)"
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
  if (!d.manhattanSystem) {
    d.manhattanSystem = JSON.parse(JSON.stringify(DEFAULT_SEED.manhattanSystem));
  } else {
    const seedMs = DEFAULT_SEED.manhattanSystem;
    d.manhattanSystem.doctrine = JSON.parse(JSON.stringify(seedMs.doctrine));
    d.manhattanSystem.sites = JSON.parse(JSON.stringify(seedMs.sites));
    d.manhattanSystem.fiveYearCatalog = JSON.parse(JSON.stringify(seedMs.fiveYearCatalog));
    if (!d.manhattanSystem.adminCore3Y) {
      d.manhattanSystem.adminCore3Y = JSON.parse(JSON.stringify(seedMs.adminCore3Y));
    } else {
      const doneAdmin = d.manhattanSystem.adminCore3Y.completedYears || [];
      d.manhattanSystem.adminCore3Y = JSON.parse(JSON.stringify(seedMs.adminCore3Y));
      d.manhattanSystem.adminCore3Y.completedYears = doneAdmin;
    }
    if (!Array.isArray(d.manhattanSystem.selectedQueue) || !d.manhattanSystem.selectedQueue.length) {
      d.manhattanSystem.selectedQueue = JSON.parse(JSON.stringify(seedMs.selectedQueue));
    }
    if (!d.manhattanSystem.completedTopicYears) {
      d.manhattanSystem.completedTopicYears = {};
    }
    if (Array.isArray(d.manhattanSystem.completedSubchapters)) {
      const smap = {};
      d.manhattanSystem.completedSubchapters.forEach((k) => { smap[k] = true; });
      d.manhattanSystem.completedSubchapters = smap;
    } else if (!d.manhattanSystem.completedSubchapters || typeof d.manhattanSystem.completedSubchapters !== "object") {
      d.manhattanSystem.completedSubchapters = {};
    }
    if (Array.isArray(d.manhattanSystem.completedCarAudio)) {
      const cmap = {};
      d.manhattanSystem.completedCarAudio.forEach((k) => { cmap[k] = true; });
      d.manhattanSystem.completedCarAudio = cmap;
    } else if (!d.manhattanSystem.completedCarAudio || typeof d.manhattanSystem.completedCarAudio !== "object") {
      d.manhattanSystem.completedCarAudio = {};
    }
    if (!Array.isArray(d.manhattanSystem.carAudioRoad) || !d.manhattanSystem.carAudioRoad.length) {
      d.manhattanSystem.carAudioRoad = JSON.parse(JSON.stringify(seedMs.carAudioRoad || []));
    }
    if (!d.summaBook) {
      d.summaBook = JSON.parse(JSON.stringify(DEFAULT_SEED.summaBook));
    }
    if (!Array.isArray(d.manhattanSystem.aiAgents) || !d.manhattanSystem.aiAgents.length) {
      d.manhattanSystem.aiAgents = JSON.parse(JSON.stringify(seedMs.aiAgents));
    } else {
      const existingAgt = new Set(d.manhattanSystem.aiAgents.map((a) => a.id));
      seedMs.aiAgents.forEach((a) => {
        if (!existingAgt.has(a.id)) d.manhattanSystem.aiAgents.push(JSON.parse(JSON.stringify(a)));
      });
    }
    if (!Array.isArray(d.manhattanSystem.fissionNodes) || !d.manhattanSystem.fissionNodes.length) {
      d.manhattanSystem.fissionNodes = JSON.parse(JSON.stringify(seedMs.fissionNodes));
    } else {
      const existingFis = new Set(d.manhattanSystem.fissionNodes.map((n) => n.id));
      seedMs.fissionNodes.forEach((n) => {
        if (!existingFis.has(n.id)) d.manhattanSystem.fissionNodes.push(JSON.parse(JSON.stringify(n)));
      });
    }
  }
  return d;
}

async function initApp() {
  // Zastosuj zapisany motyw natychmiast bez oczekiwania na asynchroniczne zapytania sieciowe
  setTheme(appState.theme);
  setLanguage(appState.lang);
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

  setTheme(appState.theme);
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
    '<a href="$2" target="_blank" rel="noopener noreferrer" style="color:var(--accent-blue); text-decoration:underline; font-weight:600;">🔗 $1</a>'
  );
  escaped = escaped.replace(
    /(^|[^"'>])(https?:\/\/[^\s<)]+)/g,
    '$1<a href="$2" target="_blank" rel="noopener noreferrer" style="color:var(--accent-blue); text-decoration:underline;">$2</a>'
  );
  return escaped;
}

function renderLinksBlock(item) {
  const links = item.links || [];
  const isEn = appState.lang === "en";
  if (links.length > 0) {
    return `
      <div style="margin-top:0.5rem; padding-top:0.4rem; border-top:1px dashed var(--border-color);">
        <div style="font-size:0.75rem; font-weight:700; color:var(--accent-blue); margin-bottom:0.25rem;">🔗 ${isEn ? "Source Links & Language:" : "Odnośniki źródłowe i język materiału:"}</div>
        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.25rem;">
          ${links
            .map((l) => {
              const lCode = detectSourceLang(`${l.label || ""} ${l.url || ""}`);
              const tag = lCode === "PL" ? `<span class="lang-tag lang-pl" style="font-size:0.65rem; padding:0.05rem 0.4rem;">[PL 🇵🇱]</span>` : `<span class="lang-tag lang-en" style="font-size:0.65rem; padding:0.05rem 0.4rem;">[EN 🇬🇧]</span>`;
              return `<li style="font-size:0.8rem; display:flex; align-items:center; gap:0.35rem; flex-wrap:wrap;">${tag} <a href="${escapeHtml(l.url)}" target="_blank" rel="noopener noreferrer" style="color:var(--accent-blue); text-decoration:underline;">${escapeHtml(l.label)}</a></li>`;
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
        <a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer" style="color:var(--accent-blue); font-size:0.82rem; font-weight:600; text-decoration:underline;">🔗 ${isEn ? "Open source material" : "Otwórz materiał źródłowy"}</a>
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

  if (appState.activeTab === "manhattan") renderManhattanView();
  if (appState.activeTab === "caraudio") renderCarAudioView();
  if (appState.activeTab === "study") renderStudyView();
  if (appState.activeTab === "map") renderMapView();
  if (appState.activeTab === "workspaces") renderWorkspacesView();
  if (appState.activeTab === "materials") renderMaterialsView();
  if (appState.activeTab === "book") renderBookView();
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
  const fisCountEl = document.getElementById("navFissionCount");
  const studyCountEl = document.getElementById("navStudyCount");
  const subCountEl = document.getElementById("navSubprojectsCount");
  const matCountEl = document.getElementById("navMaterialsCount");

  if (fisCountEl) fisCountEl.textContent = ((appState.data.manhattanSystem || {}).fissionNodes || []).length;
  if (studyCountEl) studyCountEl.textContent = (appState.data.studyMaterials || []).length;
  if (subCountEl) subCountEl.textContent = (appState.data.subprojects || []).length;
  if (matCountEl) matCountEl.textContent = (appState.data.materials || []).length;

  const navCarEl = document.getElementById("navCarAudioCount");
  const navBookEl = document.getElementById("navBookCount");
  const carRoad = ((appState.data.manhattanSystem || {}).carAudioRoad || []);
  const carDoneMap = ((appState.data.manhattanSystem || {}).completedCarAudio || {});
  const carDoneCount = Object.values(carDoneMap).filter(Boolean).length;
  if (navCarEl) navCarEl.textContent = `${carDoneCount}/${carRoad.length}`;
  const bookChapters = ((appState.data.summaBook || {}).chapters || []);
  if (navBookEl) navBookEl.textContent = bookChapters.length;
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
              <div style="background:var(--bg-subtle); padding:0.55rem 0.7rem; border-radius:var(--radius-sm); border:1px solid var(--border-subtle);">
                <strong style="font-size:0.82rem; color:var(--accent-blue);">${escapeHtml(st.stage)}</strong>
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
                <div class="track-section-block" style="border: 1px solid var(--border-color); background: var(--bg-subtle); padding: 0.75rem; border-radius: var(--radius-sm);">
                  <h4 style="color:var(--accent-blue);">📚 ${escapeHtml(suppProj.title)}</h4>
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
      return `<line class="g-edge" x1="${s.x}" y1="${s.y}" x2="${t.x}" y2="${t.y}" stroke-width="1.5" />`;
    })
    .join("");

  const nodesSvg = appState.data.tracks
    .map((tr) => {
      const tObj = getTrackOrFoundationById(tr.id);
      const c = coords[tr.id] || { x: 100, y: 100 };
      const r = tr.id === "E" ? 44 : 36;
      return `
      <g style="cursor:pointer;" onclick="selectGraphNode('${tr.id}')">
        <circle class="g-node" cx="${c.x}" cy="${c.y}" r="${r}" style="stroke:${tr.color}" stroke-width="2" />
        <text class="g-label-strong" x="${c.x}" y="${c.y + 4}" text-anchor="middle" font-size="12.5" font-weight="700">${escapeHtml(tObj.code)}</text>
        <text class="g-label" x="${c.x}" y="${c.y + r + 18}" text-anchor="middle" font-size="11.5" font-weight="500">${escapeHtml(tObj.name)}</text>
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

// =============================================================================
// STRONA PIERWSZA PROJEKTOWA: ROZPROSZONY SYSTEM MANHATTAN (3 LATA ADMINISTRACJI
// + 5×N LAT Z RZĘDU) ORAZ BAZA I GRAF ROZSZCZEPIEŃ AGENTÓW AI
// =============================================================================

function computeManhattanMetrics(ms) {
  const queueIds = ms.selectedQueue || [];
  const totalStudyYears = 3 + queueIds.length * 5;
  const totalSemesters = 6 + queueIds.length * 10;
  const totalEcts = 180 + queueIds.length * 300;

  const adminDone = ((ms.adminCore3Y || {}).completedYears || []).length;
  let topicsDone = 0;
  queueIds.forEach((qid) => {
    const arr = (ms.completedTopicYears || {})[qid] || [];
    topicsDone += arr.length;
  });
  const completedYearsTotal = adminDone + topicsDone;
  const progressPct = totalStudyYears > 0 ? Math.round((completedYearsTotal / totalStudyYears) * 100) : 0;

  const nodes = ms.fissionNodes || [];
  const parentCounts = {};
  nodes.forEach((n) => {
    if (n.parentId) {
      parentCounts[n.parentId] = (parentCounts[n.parentId] || 0) + 1;
    }
  });
  const activeParents = Object.keys(parentCounts).length;
  const totalChildren = Object.values(parentCounts).reduce((acc, v) => acc + v, 0);
  const kEff = activeParents > 0 ? (totalChildren / activeParents).toFixed(2) : "1.00";

  return {
    totalStudyYears,
    totalSemesters,
    totalEcts,
    completedYearsTotal,
    progressPct,
    kEff
  };
}

function selectManhattanSiteFilter(siteId) {
  appState.manhattanSiteFilter = appState.manhattanSiteFilter === siteId ? "ALL" : siteId;
  renderManhattanView();
}

function setManhattanStartYear(val) {
  const yr = parseInt(val, 10);
  if (!isNaN(yr) && yr >= 1990 && yr <= 2100) {
    appState.data.manhattanSystem.startCalendarYear = yr;
    saveState();
  }
}

function applyStudyQueuePreset(preset) {
  const ms = appState.data.manhattanSystem;
  const catalog = ms.fiveYearCatalog || [];
  if (preset === "FOUNDATIONS") {
    ms.selectedQueue = catalog.filter((c) => c.group === "FOUNDATION").map((c) => c.id);
  } else if (preset === "TRACKS") {
    ms.selectedQueue = catalog.filter((c) => c.group === "TRACK").map((c) => c.id);
  } else if (preset === "ALL16") {
    ms.selectedQueue = catalog.map((c) => c.id);
  } else {
    ms.selectedQueue = [
      "STU-FND-1",
      "STU-FND-2",
      "STU-FND-3",
      "STU-FND-4",
      "STU-FND-5",
      "STU-FND-6",
      "STU-FND-7",
      "STU-FND-8",
      "STU-TRK-H"
    ];
  }
  saveState(
    appState.lang === "en"
      ? "Sequential 5-year study queue updated!"
      : "Zaktualizowano kolejkę ciągłych 5-letnich studiów!"
  );
}

function toggleQueueTopic(studyId) {
  const ms = appState.data.manhattanSystem;
  const idx = ms.selectedQueue.indexOf(studyId);
  if (idx >= 0) {
    if (ms.selectedQueue.length <= 1) {
      showToast(
        appState.lang === "en"
          ? "At least 1 five-year specialization must remain in the sequence."
          : "W kolejce musi pozostać co najmniej 1 pięcioletnia tematyka."
      );
      return;
    }
    ms.selectedQueue.splice(idx, 1);
  } else {
    ms.selectedQueue.push(studyId);
    appState.expandedStudyIds[studyId] = true;
  }
  saveState();
}

function moveQueueTopic(studyId, delta) {
  const q = appState.data.manhattanSystem.selectedQueue;
  const idx = q.indexOf(studyId);
  if (idx < 0) return;
  const nextIdx = idx + delta;
  if (nextIdx < 0 || nextIdx >= q.length) return;
  const tmp = q[idx];
  q[idx] = q[nextIdx];
  q[nextIdx] = tmp;
  saveState();
}

function toggleStudyBlockExpand(blockId) {
  appState.expandedStudyIds[blockId] = !appState.expandedStudyIds[blockId];
  renderManhattanView();
}

function toggleSubchapterDone(subKey) {
  if (!appState.data || !appState.data.manhattanSystem) return;
  const ms = appState.data.manhattanSystem;
  ms.completedSubchapters = ms.completedSubchapters || {};
  ms.completedSubchapters[subKey] = !ms.completedSubchapters[subKey];
  saveState();
  renderManhattanView();
}

function toggleAdminYearDone(yr) {
  const admin = appState.data.manhattanSystem.adminCore3Y;
  admin.completedYears = admin.completedYears || [];
  const idx = admin.completedYears.indexOf(yr);
  if (idx >= 0) admin.completedYears.splice(idx, 1);
  else admin.completedYears.push(yr);
  saveState();
}

function toggleTopicYearDone(studyId, yr) {
  const map = appState.data.manhattanSystem.completedTopicYears;
  map[studyId] = map[studyId] || [];
  const idx = map[studyId].indexOf(yr);
  if (idx >= 0) map[studyId].splice(idx, 1);
  else map[studyId].push(yr);
  saveState();
}

function selectFissionNode(nodeId) {
  appState.selectedFissionNodeId = nodeId;
  renderManhattanView();
}

function setFissionNodeStatus(nodeId, newStatus) {
  const node = (appState.data.manhattanSystem.fissionNodes || []).find((n) => n.id === nodeId);
  if (!node) return;
  node.status = newStatus;
  saveState(appState.lang === "en" ? "Fission node status updated." : "Zaktualizowano status węzła rozszczepienia.");
}

function deleteFissionNode(nodeId) {
  if (nodeId === "FIS-00") {
    showToast("Rdzeń główny CORE-235 nie może zostać usunięty.");
    return;
  }
  const ms = appState.data.manhattanSystem;
  const target = (ms.fissionNodes || []).find((n) => n.id === nodeId);
  if (!target) return;
  const fallbackParent = target.parentId || "FIS-00";
  ms.fissionNodes.forEach((n) => {
    if (n.parentId === nodeId) n.parentId = fallbackParent;
    if (Array.isArray(n.neutronTargets)) {
      n.neutronTargets = n.neutronTargets.filter((tid) => tid !== nodeId);
    }
  });
  ms.fissionNodes = ms.fissionNodes.filter((n) => n.id !== nodeId);
  appState.selectedFissionNodeId = fallbackParent;
  saveState(appState.lang === "en" ? "Fission node removed." : "Węzeł rozszczepienia został usunięty.");
}

function generateAiFissionSuggestions(parentNode, ms) {
  const nextGen = (parentNode.generation || 0) + 1;
  const siteId = parentNode.siteId || "SITE-Y15";
  const agentId = parentNode.agentId || "AGT-02";
  const baseCode = (parentNode.code || "FIS").split("-")[0];
  const suffix = String((ms.fissionNodes || []).length + 1).padStart(2, "0");

  const domainTemplates = {
    "SITE-W0": [
      {
        code: `${baseCode}-REG-${suffix}A`,
        titlePl: `Audyt Prawno-Regulacyjny i Kompartmentalizacja: ${parentNode.code}`,
        titleEn: `Legal-Regulatory Audit & Compartmentalization: ${parentNode.code}`,
        descPl: `Weryfikacja zgodności pakietu „${parentNode.titlePl}” z prawem administracyjnym, bioetycznym, atomowym i AI Act oraz wyznaczenie barier dostępu.`,
        descEn: `Compliance verification of '${parentNode.titleEn}' against administrative, bioethical, nuclear, and AI regulations.`,
        deliverablePl: "Raport zgodności formalnej i rygoru epistemicznego (Poziom 1–4)."
      },
      {
        code: `${baseCode}-LOG-${suffix}B`,
        titlePl: `Budżetowanie Zadaniowe, Granty B+R i Ochrona Patentowa: ${parentNode.code}`,
        titleEn: `Mission Budgeting, R&D Grants & Patent IP Shield: ${parentNode.code}`,
        descPl: `Harmonogram finansowo-organizacyjny i strategia własności intelektualnej wyprowadzona z 3-letniego rdzenia Administracji.`,
        descEn: `Financial-logistical schedule and IP protection strategy derived from the 3-year Administration core.`,
        deliverablePl: "Matryca alokacji zasobów i zgłoszeń IP."
      }
    ],
    "SITE-X10": [
      {
        code: `X10-PWR-${suffix}A`,
        titlePl: `Bilans Mocy Reaktorowej i Termodynamiki Procesowej (${parentNode.code})`,
        titleEn: `Reactor Power & Process Thermodynamics Balance (${parentNode.code})`,
        descPl: `Obliczenia gęstości mocy, odbioru ciepła (SMR/HTGR/Fuzja) oraz niezawodności zasilania dla sprzężonych układów z węzła „${parentNode.titlePl}”.`,
        descEn: `Power density, heat rejection (SMR/HTGR/Fusion), and reliability modeling for systems coupled to '${parentNode.titleEn}'.`,
        deliverablePl: "Specyfikacja pętli cieplno-elektrycznej i osłon radiacyjnych."
      },
      {
        code: `X10-ELEC-${suffix}B`,
        titlePl: `Architektura Elektroniki Pomiarowej i Sterowania Bezpieczeństwem (${parentNode.code})`,
        titleEn: `Instrumentation Electronics & Safety Control Architecture (${parentNode.code})`,
        descPl: `Projekt niskoszumowej aparatury kontrolno-pomiarowej, detektorów promieniowania i układów FPGA odpornych na błędy.`,
        descEn: `Low-noise instrumentation, radiation sensors, and fault-tolerant FPGA control loops.`,
        deliverablePl: "Schemat blokowy toru pomiarowo-zabezpieczającego."
      }
    ],
    "SITE-B7": [
      {
        code: `B7-MOL-${suffix}A`,
        titlePl: `Protokół Biokompatybilności i Syntezy Biomateriałowej (${parentNode.code})`,
        titleEn: `Biocompatibility & Biomaterial Synthesis Protocol (${parentNode.code})`,
        descPl: `Analiza oddziaływań na styku tkanka żywa – hydrożel/elektroda oraz kontrola odpowiedzi immunologicznej dla „${parentNode.titlePl}”.`,
        descEn: `Living tissue–electrode/hydrogel interface analysis and immune response control for '${parentNode.titleEn}'.`,
        deliverablePl: "Karta walidacji biologiczno-materiałowej in vitro."
      },
      {
        code: `B7-NEU-${suffix}B`,
        titlePl: `Sprzężenie Zwrotne Neuro-Cybernetyczne i Bezpieczeństwo Kliniczne (${parentNode.code})`,
        titleEn: `Closed-Loop Neuro-Cybernetic Feedback & Clinical Safety (${parentNode.code})`,
        descPl: `Dekodowanie sygnałów fizjologicznych w czasie rzeczywistym i wyznaczenie granic regeneracji względem modyfikacji syntetycznej.`,
        descEn: `Real-time physiological signal decoding and clinical safety thresholds.`,
        deliverablePl: "Protokół testowy pętli zamkniętej bio-maszyna."
      }
    ],
    "SITE-T9": [
      {
        code: `T9-ORB-${suffix}A`,
        titlePl: `Wariant Pozaziemski (Projekt F): Zamknięty Obieg i Radiacja (${parentNode.code})`,
        titleEn: `Extraterrestrial Variant (Project F): Closed Loop & Radiation (${parentNode.code})`,
        descPl: `Adaptacja rozwiązań z węzła „${parentNode.titlePl}” do warunków mikrograwitacji, próżni i promieniowania kosmicznego.`,
        descEn: `Adapting '${parentNode.titleEn}' to microgravity, vacuum, and deep-space radiation constraints.`,
        deliverablePl: "Bilans masy, energii i niezawodności habitatu."
      },
      {
        code: `T9-BIO-${suffix}B`,
        titlePl: `Wariant Ziemski (Projekt G): Wdrożenie Ekologiczne i Dekarbonizacja (${parentNode.code})`,
        titleEn: `Earth Biosphere Variant (Project G): Ecological Resilience (${parentNode.code})`,
        descPl: `Transfer czystych technologii recyklingu i monitoringu środowiskowego do ochrony ekosystemów Ziemi.`,
        descEn: `Transferring closed-loop and clean-tech engineering to Earth biosphere protection.`,
        deliverablePl: "Raport wpływu środowiskowego i odporności ekosystemowej."
      }
    ]
  };

  const fallbackY15 = [
    {
      code: `Y15-MOD-${suffix}A`,
      titlePl: `Formalny Model Matematyczno-Algorytmiczny (${parentNode.code})`,
      titleEn: `Formal Mathematical & Algorithmic Model (${parentNode.code})`,
      descPl: `Wyprowadzenie równań dynamiki, złożoności obliczeniowej i reprezentacji grafowej dla zagadnienia „${parentNode.titlePl}”.`,
      descEn: `Derivation of dynamical equations, computational complexity, and graph representations for '${parentNode.titleEn}'.`,
      deliverablePl: "Specyfikacja matematyczna i hipoteza falsyfikowalna."
    },
    {
      code: `Y15-SIM-${suffix}B`,
      titlePl: `Symulacja Numeryczna AI / SNN i Walidacja Empiryczna (${parentNode.code})`,
      titleEn: `AI / SNN Numerical Simulation & Empirical Benchmark (${parentNode.code})`,
      descPl: `Implementacja prototypu symulacyjnego w Pythonie/PyTorch/Brian2 oraz porównanie z danymi biologicznymi i fizycznymi.`,
      descEn: `Simulation prototype in Python/PyTorch/Brian2 benchmarked against empirical biological/physical data.`,
      deliverablePl: "Kod symulacji i metryki błędu rekonstrukcji."
    }
  ];

  const pair = domainTemplates[siteId] || fallbackY15;
  return pair.map((item) => ({
    ...item,
    generation: nextGen,
    siteId,
    agentId,
    trackRef: parentNode.trackRef || "B"
  }));
}

function openAiFissionModal(parentId) {
  const ms = appState.data.manhattanSystem;
  const parentNode = (ms.fissionNodes || []).find((n) => n.id === parentId) || ms.fissionNodes[0];
  if (!parentNode) return;
  const isEn = appState.lang === "en";
  const proposals = generateAiFissionSuggestions(parentNode, ms);

  const siteOptions = (ms.sites || [])
    .map((s) => `<option value="${s.id}" ${s.id === parentNode.siteId ? "selected" : ""}>${escapeHtml(s.code)} — ${escapeHtml(isEn ? s.nameEn : s.namePl)}</option>`)
    .join("");
  const agentOptions = (ms.aiAgents || [])
    .map((a) => `<option value="${a.id}" ${a.id === parentNode.agentId ? "selected" : ""}>${escapeHtml(a.codename)} — ${escapeHtml(isEn ? a.nameEn : a.namePl)}</option>`)
    .join("");

  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>☢️ ${isEn ? `AI Chain-Reaction Fission: ${parentNode.code}` : `Rozszczepienie Łańcuchowe Węzła przez Agenta AI: ${parentNode.code}`}</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <p style="font-size:0.84rem; color:var(--text-secondary); margin-bottom:0.9rem;">
      ${
        isEn
          ? `Parent node <strong>${escapeHtml(parentNode.titleEn)}</strong> (Generation G${parentNode.generation}) will fission into 2 specialized Generation G${parentNode.generation + 1} child work packages:`
          : `Węzeł macierzysty <strong>${escapeHtml(parentNode.titlePl)}</strong> (Generacja G${parentNode.generation}) ulegnie rozszczepieniu na 2 wyspecjalizowane fragmenty potomne Generacji G${parentNode.generation + 1}:`
      }
    </p>
    <form onsubmit="submitAiFissionSplit(event, '${parentNode.id}')">
      <div class="ws-card" style="margin-bottom:0.85rem; border-left:3px solid var(--warning);">
        <strong style="color:var(--warning); font-size:0.84rem;">⚡ Fragment Rozszczepienia #1 (G${parentNode.generation + 1})</strong>
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:0.6rem; margin-top:0.45rem;">
          <input type="text" id="fis1Code" class="input-field" value="${escapeHtml(proposals[0].code)}" required />
          <input type="text" id="fis1Title" class="input-field" value="${escapeHtml(isEn ? proposals[0].titleEn : proposals[0].titlePl)}" required />
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.6rem; margin-top:0.45rem;">
          <select id="fis1Site" class="select-field">${siteOptions}</select>
          <select id="fis1Agent" class="select-field">${agentOptions}</select>
        </div>
        <textarea id="fis1Desc" class="textarea-field" rows="2" style="margin-top:0.45rem;" required>${escapeHtml(isEn ? proposals[0].descEn : proposals[0].descPl)}</textarea>
        <input type="text" id="fis1Deliv" class="input-field" style="margin-top:0.4rem;" value="${escapeHtml(proposals[0].deliverablePl)}" required />
      </div>

      <div class="ws-card" style="margin-bottom:0.85rem; border-left:3px solid var(--accent-blue);">
        <strong style="color:var(--accent-blue); font-size:0.84rem;">⚡ Fragment Rozszczepienia #2 (G${parentNode.generation + 1})</strong>
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:0.6rem; margin-top:0.45rem;">
          <input type="text" id="fis2Code" class="input-field" value="${escapeHtml(proposals[1].code)}" required />
          <input type="text" id="fis2Title" class="input-field" value="${escapeHtml(isEn ? proposals[1].titleEn : proposals[1].titlePl)}" required />
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.6rem; margin-top:0.45rem;">
          <select id="fis2Site" class="select-field">${siteOptions}</select>
          <select id="fis2Agent" class="select-field">${agentOptions}</select>
        </div>
        <textarea id="fis2Desc" class="textarea-field" rows="2" style="margin-top:0.45rem;" required>${escapeHtml(isEn ? proposals[1].descEn : proposals[1].descPl)}</textarea>
        <input type="text" id="fis2Deliv" class="input-field" style="margin-top:0.4rem;" value="${escapeHtml(proposals[1].deliverablePl)}" required />
      </div>

      <div style="display:flex; justify-content:flex-end; gap:0.5rem;">
        <button type="button" class="btn" onclick="closeModal()">${isEn ? "Cancel" : "Anuluj"}</button>
        <button type="submit" class="btn btn-primary">☢️ ${isEn ? "Execute AI Chain Fission (1 → 2)" : "Wykonaj rozszczepienie łańcuchowe (1 → 2)"}</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitAiFissionSplit(e, parentId) {
  e.preventDefault();
  const ms = appState.data.manhattanSystem;
  const parentNode = (ms.fissionNodes || []).find((n) => n.id === parentId);
  if (!parentNode) return;
  const nextGen = (parentNode.generation || 0) + 1;
  const nowTs = Date.now();

  const n1 = {
    id: `FIS-C-${nowTs}-1`,
    parentId: parentNode.id,
    generation: nextGen,
    code: document.getElementById("fis1Code").value.trim(),
    siteId: document.getElementById("fis1Site").value,
    agentId: document.getElementById("fis1Agent").value,
    trackRef: parentNode.trackRef || "B",
    status: "active",
    titlePl: document.getElementById("fis1Title").value.trim(),
    titleEn: document.getElementById("fis1Title").value.trim(),
    descPl: document.getElementById("fis1Desc").value.trim(),
    descEn: document.getElementById("fis1Desc").value.trim(),
    neutronTargets: [],
    deliverablePl: document.getElementById("fis1Deliv").value.trim(),
    deliverableEn: document.getElementById("fis1Deliv").value.trim()
  };

  const n2 = {
    id: `FIS-C-${nowTs}-2`,
    parentId: parentNode.id,
    generation: nextGen,
    code: document.getElementById("fis2Code").value.trim(),
    siteId: document.getElementById("fis2Site").value,
    agentId: document.getElementById("fis2Agent").value,
    trackRef: parentNode.trackRef || "B",
    status: "active",
    titlePl: document.getElementById("fis2Title").value.trim(),
    titleEn: document.getElementById("fis2Title").value.trim(),
    descPl: document.getElementById("fis2Desc").value.trim(),
    descEn: document.getElementById("fis2Desc").value.trim(),
    neutronTargets: [n1.id],
    deliverablePl: document.getElementById("fis2Deliv").value.trim(),
    deliverableEn: document.getElementById("fis2Deliv").value.trim()
  };

  ms.fissionNodes.push(n1, n2);
  appState.selectedFissionNodeId = n1.id;
  closeModal();
  saveState(
    appState.lang === "en"
      ? `Chain fission complete! Added ${n1.code} & ${n2.code}.`
      : `Rozszczepienie zakończone! Dodano węzły ${n1.code} oraz ${n2.code}.`
  );
}

function openCustomFissionNodeModal() {
  const ms = appState.data.manhattanSystem;
  const isEn = appState.lang === "en";
  const parentOptions = (ms.fissionNodes || [])
    .map((n) => `<option value="${n.id}" ${n.id === appState.selectedFissionNodeId ? "selected" : ""}>[G${n.generation} • ${escapeHtml(n.code)}] ${escapeHtml(isEn ? n.titleEn : n.titlePl)}</option>`)
    .join("");
  const siteOptions = (ms.sites || [])
    .map((s) => `<option value="${s.id}">${escapeHtml(s.code)} — ${escapeHtml(isEn ? s.nameEn : s.namePl)}</option>`)
    .join("");
  const agentOptions = (ms.aiAgents || [])
    .map((a) => `<option value="${a.id}">${escapeHtml(a.codename)} — ${escapeHtml(isEn ? a.nameEn : a.namePl)}</option>`)
    .join("");
  const targetOptions = (ms.fissionNodes || [])
    .map((n) => `<option value="${n.id}">[${escapeHtml(n.code)}] ${escapeHtml(isEn ? n.titleEn : n.titlePl)}</option>`)
    .join("");

  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>➕ ${isEn ? "Add Custom Fission Node to Database" : "Dodaj własny węzeł rozszczepienia do bazy projektu"}</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitCustomFissionNode(event)">
      <div class="form-group">
        <label>${isEn ? "Parent Fission Node" : "Węzeł macierzysty (z którego następuje rozszczepienie)"}</label>
        <select id="cFisParent" class="select-field" required>${parentOptions}</select>
      </div>
      <div style="display:grid; grid-template-columns:1fr 2fr; gap:0.6rem;">
        <div class="form-group">
          <label>${isEn ? "Short Code" : "Kryptonim węzła"}</label>
          <input type="text" id="cFisCode" class="input-field" placeholder="np. X10-SMR-09" required />
        </div>
        <div class="form-group">
          <label>${isEn ? "Node Title" : "Tytuł zadania / fragmentu rozszczepienia"}</label>
          <input type="text" id="cFisTitle" class="input-field" required />
        </div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.6rem;">
        <div class="form-group">
          <label>${isEn ? "Manhattan Site" : "Ośrodek rozproszony Manhattan"}</label>
          <select id="cFisSite" class="select-field">${siteOptions}</select>
        </div>
        <div class="form-group">
          <label>${isEn ? "Assigned AI Agent" : "Przypisany Agent AI"}</label>
          <select id="cFisAgent" class="select-field">${agentOptions}</select>
        </div>
      </div>
      <div class="form-group">
        <label>${isEn ? "Secondary Neutron Target (Cross-Track Trigger)" : "Wtórny cel neutronu (powiązany węzeł międzyośrodkowy — opcjonalnie)"}</label>
        <select id="cFisNeutron" class="select-field">
          <option value="">${isEn ? "— None —" : "— Brak wtórnego neutronu —"}</option>
          ${targetOptions}
        </select>
      </div>
      <div class="form-group">
        <label>${isEn ? "Operational Scope & Hypothesis" : "Opis operacyjny i zakres badawczy"}</label>
        <textarea id="cFisDesc" class="textarea-field" rows="3" required></textarea>
      </div>
      <div class="form-group">
        <label>${isEn ? "Expected Deliverable" : "Oczekiwany rezultat / artefakt"}</label>
        <input type="text" id="cFisDeliv" class="input-field" required />
      </div>
      <div style="display:flex; justify-content:flex-end;">
        <button type="submit" class="btn btn-primary">💾 ${isEn ? "Save Fission Node" : "Zapisz węzeł rozszczepienia"}</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitCustomFissionNode(e) {
  e.preventDefault();
  const ms = appState.data.manhattanSystem;
  const parentId = document.getElementById("cFisParent").value;
  const parentNode = (ms.fissionNodes || []).find((n) => n.id === parentId);
  const nextGen = parentNode ? (parentNode.generation || 0) + 1 : 1;
  const neutronVal = document.getElementById("cFisNeutron").value;
  const title = document.getElementById("cFisTitle").value.trim();
  const desc = document.getElementById("cFisDesc").value.trim();
  const deliv = document.getElementById("cFisDeliv").value.trim();
  const newId = "FIS-USR-" + Date.now();

  ms.fissionNodes.push({
    id: newId,
    parentId,
    generation: nextGen,
    code: document.getElementById("cFisCode").value.trim(),
    siteId: document.getElementById("cFisSite").value,
    agentId: document.getElementById("cFisAgent").value,
    trackRef: parentNode ? parentNode.trackRef : "H",
    status: "active",
    titlePl: title,
    titleEn: title,
    descPl: desc,
    descEn: desc,
    neutronTargets: neutronVal ? [neutronVal] : [],
    deliverablePl: deliv,
    deliverableEn: deliv
  });
  appState.selectedFissionNodeId = newId;
  closeModal();
  saveState(appState.lang === "en" ? "Custom fission node added!" : "Dodano własny węzeł rozszczepienia!");
}

function openNewAiAgentModal() {
  const ms = appState.data.manhattanSystem;
  const isEn = appState.lang === "en";
  const siteOptions = (ms.sites || [])
    .map((s) => `<option value="${s.id}">${escapeHtml(s.code)} — ${escapeHtml(isEn ? s.nameEn : s.namePl)}</option>`)
    .join("");
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🤖 ${isEn ? "Register New Specialized AI Agent" : "Zarejestruj nowego wyspecjalizowanego Agenta AI"}</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewAiAgent(event)">
      <div style="display:grid; grid-template-columns:1fr 1.6fr; gap:0.6rem;">
        <div class="form-group">
          <label>${isEn ? "Agent Codename" : "Kryptonim Agenta AI"}</label>
          <input type="text" id="agtCodeInput" class="input-field" placeholder="np. SKLODOWSKA-RAD-07" required />
        </div>
        <div class="form-group">
          <label>${isEn ? "Agent Name / Title" : "Nazwa i funkcja Agenta AI"}</label>
          <input type="text" id="agtNameInput" class="input-field" required />
        </div>
      </div>
      <div class="form-group">
        <label>${isEn ? "Assigned Manhattan Site" : "Macierzysty ośrodek Manhattan"}</label>
        <select id="agtSiteInput" class="select-field">${siteOptions}</select>
      </div>
      <div class="form-group">
        <label>${isEn ? "Specialization Scope" : "Zakres specjalizacji badawczej"}</label>
        <input type="text" id="agtRoleInput" class="input-field" required />
      </div>
      <div class="form-group">
        <label>${isEn ? "System Prompt / Operational Directive" : "Szablon rozkazu systemowego (System Prompt)"}</label>
        <textarea id="agtPromptInput" class="textarea-field" rows="3" required></textarea>
      </div>
      <div style="display:flex; justify-content:flex-end;">
        <button type="submit" class="btn btn-primary">🤖 ${isEn ? "Save AI Agent" : "Zapisz Agenta AI w bazie"}</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitNewAiAgent(e) {
  e.preventDefault();
  const ms = appState.data.manhattanSystem;
  const siteId = document.getElementById("agtSiteInput").value;
  const siteObj = (ms.sites || []).find((s) => s.id === siteId);
  const name = document.getElementById("agtNameInput").value.trim();
  const role = document.getElementById("agtRoleInput").value.trim();

  ms.aiAgents.push({
    id: "AGT-" + Date.now(),
    codename: document.getElementById("agtCodeInput").value.trim().toUpperCase(),
    namePl: name,
    nameEn: name,
    siteId,
    color: siteObj ? siteObj.color : "#38bdf8",
    rolePl: role,
    roleEn: role,
    promptTemplate: document.getElementById("agtPromptInput").value.trim()
  });
  closeModal();
  saveState(appState.lang === "en" ? "New AI Agent registered!" : "Nowy Agent AI został dodany do floty!");
}

async function copyAgentDirectiveToClipboard(nodeId) {
  const ms = appState.data.manhattanSystem;
  const node = (ms.fissionNodes || []).find((n) => n.id === nodeId);
  if (!node) return;
  const agt = (ms.aiAgents || []).find((a) => a.id === node.agentId) || ms.aiAgents[0];
  const site = (ms.sites || []).find((s) => s.id === node.siteId);
  const directive = [
    `=== ROZKAZ OPERACYJNY SZTABU MANHATTAN GOLEM 15 [${node.code}] ===`,
    `Ośrodek: ${site ? site.code + " — " + site.namePl : node.siteId}`,
    `Agent AI: ${agt ? agt.codename + " (" + agt.namePl + ")" : node.agentId}`,
    `Generacja rozszczepienia: G${node.generation}`,
    `Zadanie węzła: ${node.titlePl}`,
    `Kontekst i cel: ${node.descPl}`,
    `Wymagany artefakt końcowy: ${node.deliverablePl}`,
    ``,
    `Instrukcja systemowa Agenta:`,
    `${agt ? agt.promptTemplate : ""}`,
    `Uwzględnij rygor epistemiczny Projektu E (oddziel fakty potwierdzone od hipotez i spekulacji) oraz wymogi prawno-administracyjne Sztabu W-0.`
  ].join("\n");

  try {
    await navigator.clipboard.writeText(directive);
    showToast(
      appState.lang === "en"
        ? `Copied AI Agent directive [${node.code}] to clipboard!`
        : `Skopiowano rozkaz operacyjny Agenta AI [${node.code}] do schowka!`
    );
  } catch {
    showToast("Nie udało się skopiować automatycznie — zaznacz tekst ręcznie w inspektorze.");
  }
}

function spawnWorkspaceFromFissionNode(nodeId) {
  const ms = appState.data.manhattanSystem;
  const node = (ms.fissionNodes || []).find((n) => n.id === nodeId);
  if (!node) return;
  const agt = (ms.aiAgents || []).find((a) => a.id === node.agentId);
  const validTrackIds = new Set([
    ...appState.data.tracks.map((t) => t.id),
    ...(appState.data.foundationDisciplines || []).map((f) => f.id)
  ]);
  const mappedTrack = validTrackIds.has(node.trackRef) ? node.trackRef : "H";
  const newSpId = "sub-fis-" + Date.now();

  appState.data.subprojects.unshift({
    id: newSpId,
    trackId: mappedTrack,
    secondaryTracks: ["E", "H"],
    branchTopic: `Rozszczepienie Manhattan [${node.code}] (G${node.generation})`,
    title: `[${node.code}] ${node.titlePl}`,
    author: "Ireneusz",
    status: "approved",
    createdAt: new Date().toISOString(),
    description: `${node.descPl}\n\nOczekiwany rezultat węzła: ${node.deliverablePl}`,
    philosophicalNote: `Nadzór Agenta ${agt ? agt.codename : "AI"} w architekturze kompartmentalizacji Manhattan Golem 15.`,
    workspace: {
      hypotheses: [
        {
          id: "hyp-" + Date.now(),
          statement: `Hipoteza operacyjna węzła ${node.code}: ${node.deliverablePl}`,
          status: "Hipoteza otwarta",
          author: "Ireneusz",
          approvalStatus: "approved"
        }
      ],
      notes: [
        {
          id: "note-" + Date.now(),
          title: `Rozkaz startowy Agenta ${agt ? agt.codename : "AI"}`,
          content: agt ? agt.promptTemplate : node.descPl,
          author: "Ireneusz",
          approvalStatus: "approved"
        }
      ],
      bibliography: []
    }
  });

  appState.selectedTrackFilter = "ALL";
  appState.selectedSubprojectId = newSpId;
  switchTab("workspaces");
  saveState(
    appState.lang === "en"
      ? `Workspace created from fission node ${node.code}!`
      : `Utworzono Środowisko Badawcze z węzła rozszczepienia ${node.code}!`
  );
}

function buildFissionSvgMarkup(ms, isEn) {
  const allNodes = ms.fissionNodes || [];
  const siteFilter = appState.manhattanSiteFilter;
  const visibleNodes =
    siteFilter === "ALL"
      ? allNodes
      : allNodes.filter((n) => n.siteId === siteFilter || n.id === "FIS-00");

  const sitesById = {};
  (ms.sites || []).forEach((s) => {
    sitesById[s.id] = s;
  });
  const agentsById = {};
  (ms.aiAgents || []).forEach((a) => {
    agentsById[a.id] = a;
  });

  const byGen = {};
  let maxGen = 0;
  visibleNodes.forEach((n) => {
    const g = n.generation || 0;
    if (g > maxGen) maxGen = g;
    if (!byGen[g]) byGen[g] = [];
    byGen[g].push(n);
  });

  const maxRowsInAnyGen = Math.max(
    1,
    ...Object.values(byGen).map((arr) => arr.length)
  );
  const svgWidth = Math.max(980, (maxGen + 1) * 265 + 90);
  const svgHeight = Math.max(540, maxRowsInAnyGen * 74 + 90);

  const coords = {};
  for (let g = 0; g <= maxGen; g++) {
    const col = byGen[g] || [];
    const x = 115 + g * 260;
    col.forEach((node, idx) => {
      const y = ((idx + 1) * svgHeight) / (col.length + 1);
      coords[node.id] = { x, y };
    });
  }

  const selId = appState.selectedFissionNodeId;

  // Nagłówki kolumn generacji rozszczepienia
  let genHeadersSvg = "";
  for (let g = 0; g <= maxGen; g++) {
    const x = 115 + g * 260;
    const lbl =
      g === 0
        ? isEn
          ? "GEN 0 • FISSILE CORE"
          : "GEN 0 • RDZEŃ ROZSZCZEPIALNY"
        : g === 1
        ? isEn
          ? "GEN 1 • MANHATTAN SITES"
          : "GEN 1 • DYREKCJE MANHATTAN"
        : g === 2
        ? isEn
          ? "GEN 2 • 5Y RESEARCH STREAMS"
          : "GEN 2 • STRUMIENIE 5-LETNIE"
        : isEn
        ? `GEN ${g} • AI MICRO-FISSION`
        : `GEN ${g} • MIKRO-ROZSZCZEPIENIA AI`;
    genHeadersSvg += `
      <line class="fis-gridline" x1="${x}" y1="36" x2="${x}" y2="${svgHeight - 20}" stroke-dasharray="3 6" />
      <text class="fis-gen-label" x="${x}" y="24" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.08em">${lbl}</text>
    `;
  }

  // Krawędzie rozszczepienia macierzystego (Parent -> Child)
  let primaryEdgesSvg = "";
  visibleNodes.forEach((n) => {
    if (!n.parentId || !coords[n.parentId] || !coords[n.id]) return;
    const p = coords[n.parentId];
    const c = coords[n.id];
    const site = sitesById[n.siteId] || { color: "var(--link)" };
    const isHighlighted = n.id === selId || n.parentId === selId;
    const midX = (p.x + c.x) / 2;
    const strokeW = isHighlighted ? 2.4 : 1.3;
    const opacity = isHighlighted ? 0.9 : 0.4;
    primaryEdgesSvg += `
      <path d="M ${p.x + 68} ${p.y} C ${midX} ${p.y}, ${midX} ${c.y}, ${c.x - 72} ${c.y}"
            fill="none" style="stroke:${site.color}" stroke-width="${strokeW}" opacity="${opacity}" />
    `;
  });

  // Wtórne neutrony międzyośrodkowe (Cross-Track Neutrons)
  let neutronArcsSvg = "";
  visibleNodes.forEach((n) => {
    const src = coords[n.id];
    if (!src || !Array.isArray(n.neutronTargets)) return;
    n.neutronTargets.forEach((tid) => {
      const dst = coords[tid];
      if (!dst || tid === n.id) return;
      const isRelated = n.id === selId || tid === selId;
      if (!isRelated && siteFilter === "ALL" && n.generation < 2) return;
      const ctrlX = (src.x + dst.x) / 2 + 28;
      const ctrlY = (src.y + dst.y) / 2 - 34;
      neutronArcsSvg += `
        <path class="${isRelated ? "fis-neutron is-related" : "fis-neutron"}" d="M ${src.x} ${src.y} Q ${ctrlX} ${ctrlY} ${dst.x} ${dst.y}"
              fill="none"
              stroke-width="${isRelated ? 1.8 : 1}"
              stroke-dasharray="4 4" />
      `;
    });
  });

  // Węzły rozszczepienia
  const nodesSvg = visibleNodes
    .map((n) => {
      const pt = coords[n.id];
      if (!pt) return "";
      const site = sitesById[n.siteId] || { color: "var(--link)", code: n.siteId };
      const agt = agentsById[n.agentId] || { codename: "AI-AGENT" };
      const isSelected = n.id === selId;
      const borderCol =
        n.status === "critical"
          ? "var(--danger)"
          : n.status === "synthesized"
          ? "var(--success)"
          : site.color;
      const titleRaw = isEn ? n.titleEn : n.titlePl;
      const shortTitle = titleRaw.length > 26 ? titleRaw.slice(0, 25) + "…" : titleRaw;
      const boxW = 148;
      const boxH = 50;

      return `
        <g style="cursor:pointer;" onclick="selectFissionNode('${n.id}')">
          ${
            isSelected
              ? `<rect class="fis-select-ring" x="${pt.x - boxW / 2 - 4}" y="${pt.y - boxH / 2 - 4}" width="${boxW + 8}" height="${boxH + 8}" rx="8" fill="none" stroke-width="1.5" stroke-dasharray="4 3" />`
              : ""
          }
          <rect class="${isSelected ? "fis-node-bg is-selected" : "fis-node-bg"}" x="${pt.x - boxW / 2}" y="${pt.y - boxH / 2}" width="${boxW}" height="${boxH}" rx="5"
                style="stroke:${borderCol}"
                stroke-width="${isSelected ? 2 : 1.2}" />
          <text x="${pt.x - boxW / 2 + 8}" y="${pt.y - 7}" style="fill:${borderCol}" font-size="10" font-weight="700">${escapeHtml(n.code)}</text>
          <text class="fis-node-meta" x="${pt.x + boxW / 2 - 8}" y="${pt.y - 7}" text-anchor="end" font-size="8.8" font-weight="600">${escapeHtml(agt.codename.split("-")[0])}</text>
          <text class="fis-node-title" x="${pt.x - boxW / 2 + 8}" y="${pt.y + 11}" font-size="9.6" font-weight="500">${escapeHtml(shortTitle)}</text>
        </g>
      `;
    })
    .join("");

  return `<svg viewBox="0 0 ${svgWidth} ${svgHeight}" width="100%" height="${svgHeight}" style="min-width:860px; display:block;">
    ${genHeadersSvg}
    ${neutronArcsSvg}
    ${primaryEdgesSvg}
    ${nodesSvg}
  </svg>`;
}

function renderManhattanView() {
  const root = document.getElementById("manhattanRootContainer");
  if (!root || !appState.data || !appState.data.manhattanSystem) return;

  const isEn = appState.lang === "en";
  const ms = appState.data.manhattanSystem;
  const metrics = computeManhattanMetrics(ms);
  const startYr = ms.startCalendarYear || 2026;
  const adminEndYr = startYr + 3;
  const totalEndYr = startYr + metrics.totalStudyYears;

  const sitesById = {};
  (ms.sites || []).forEach((s) => {
    sitesById[s.id] = s;
  });
  const catalogById = {};
  (ms.fiveYearCatalog || []).forEach((c) => {
    catalogById[c.id] = c;
  });
  const agentsById = {};
  (ms.aiAgents || []).forEach((a) => {
    agentsById[a.id] = a;
  });

  // Wybrany węzeł w inspektorze
  const allFisNodes = ms.fissionNodes || [];
  let activeNode = allFisNodes.find((n) => n.id === appState.selectedFissionNodeId) || allFisNodes[0];
  const activeAgent = activeNode ? agentsById[activeNode.agentId] || ms.aiAgents[0] : null;
  const activeSite = activeNode ? sitesById[activeNode.siteId] : null;

  // Budowa wstęgi ciągłych studiów z rzędu (3 lata Administracji + po 5 lat każda wybrana tematyka)
  let currentProjStart = 1;
  const adminDoneCount = ((ms.adminCore3Y || {}).completedYears || []).length;
  const ribbonStepsHtml = [];

  ribbonStepsHtml.push(`
    <div class="seq-ribbon-step" style="--step-color:var(--warning);">
      <div style="font-size:0.68rem; color:var(--warning); font-weight:800;">${isEn ? "YEARS 1–3" : "LATA 1–3"} (${startYr}–${adminEndYr})</div>
      <div style="font-weight:700; color:var(--text-primary); margin:0.15rem 0;">🏛️ ${isEn ? "Administration (3Y Core)" : "Administracja (3 lata)"}</div>
      <div style="font-size:0.7rem; color:var(--text-muted);">180 ECTS • ${adminDoneCount}/3 ${isEn ? "yrs done" : "lat ukończ."}</div>
    </div>
  `);
  currentProjStart = 4;

  const completedSubs = ms.completedSubchapters || {};

  const queueBlocksHtml = (ms.selectedQueue || [])
    .map((studyId, qIdx) => {
      const item = catalogById[studyId];
      if (!item) return "";
      const pStart = currentProjStart;
      const pEnd = pStart + 4;
      const calS = startYr + pStart - 1;
      const calE = calS + 5;
      currentProjStart = pEnd + 1;

      const doneArr = (ms.completedTopicYears || {})[studyId] || [];
      const site = sitesById[item.siteId] || { code: item.siteId, color: item.color };
      const expanded = Boolean(appState.expandedStudyIds[studyId]);

      ribbonStepsHtml.push(`
        <div class="seq-ribbon-step" style="--step-color:${item.color}; cursor:pointer;" onclick="toggleStudyBlockExpand('${item.id}')">
          <div style="font-size:0.68rem; color:${item.color}; font-weight:800;">${isEn ? `YEARS ${pStart}–${pEnd}` : `LATA ${pStart}–${pEnd}`} (${calS}–${calE})</div>
          <div style="font-weight:700; color:var(--text-primary); margin:0.15rem 0;">${item.icon} #${qIdx + 1}: ${escapeHtml((isEn ? item.titleEn : item.titlePl).split("(")[0].trim())}</div>
          <div style="font-size:0.7rem; color:var(--text-muted);">5 ${isEn ? "yrs in a row" : "lat z rzędu"} • ${doneArr.length}/5</div>
        </div>
      `);

      // Wykrywanie paradygmatów i barier materiałowych
      const idUpper = item.id.toUpperCase();
      const hasSiliconLimits = idUpper.includes("TRK-C") || idUpper.includes("FND-2") || idUpper.includes("FND-3");
      const hasQuantum = idUpper.includes("TRK-C") || idUpper.includes("FND-1") || idUpper.includes("FND-2") || idUpper.includes("FND-3");
      const hasNeuromorphic = idUpper.includes("TRK-B") || idUpper.includes("TRK-C") || idUpper.includes("FND-2") || idUpper.includes("FND-4");
      const hasNuclear = idUpper.includes("TRK-H");

      return `
        <div class="ws-card" style="border-left:4px solid ${item.color}; margin-bottom:0.85rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.6rem;">
            <div style="cursor:pointer;" onclick="toggleStudyBlockExpand('${item.id}')">
              <div style="display:flex; align-items:center; gap:0.45rem; flex-wrap:wrap; margin-bottom:0.2rem;">
                <span class="foundation-pill" style="font-size:0.7rem; font-weight:800; border-color:${item.color}; color:var(--text-primary);">
                  ${isEn ? `BLOCK #${qIdx + 1} • YEARS ${pStart}–${pEnd} (${calS}–${calE})` : `OGNIWO #${qIdx + 1} • LATA ${pStart}–${pEnd} (${calS}–${calE})`}
                </span>
                <span class="foundation-pill" style="font-size:0.69rem; color:${site.color}; border-color:${site.color};">
                  ☢ ${escapeHtml(site.code)}
                </span>
                ${renderLangBadgeHtml(item.sourceLang || "PL+EN")}
                <span style="font-size:0.74rem; color:var(--success); font-weight:700;">${doneArr.length}/5 ${isEn ? "years completed" : "lat zaliczonych"} (300 ECTS)</span>
              </div>
              <h4 style="font-size:1rem; color:var(--text-primary); margin-bottom:0.25rem;">${item.icon} ${escapeHtml(isEn ? item.titleEn : item.titlePl)}</h4>
              
              <!-- Badges paradygmatów i barier fizycznych -->
              <div style="display:flex; gap:0.35rem; flex-wrap:wrap; margin-top:0.35rem;">
                ${hasSiliconLimits ? `<span class="alignment-badge" style="background:rgba(239,68,68,0.12); color:var(--danger); border-color:rgba(239,68,68,0.3);">⚛️ ${isEn ? "Physical Silicon Limits & Dennard Scaling" : "Podwaliny Krzemu u Kresu & Bariera Termiczna"}</span>` : ""}
                ${hasQuantum ? `<span class="alignment-badge" style="background:rgba(168,85,247,0.12); color:var(--accent-purple); border-color:rgba(168,85,247,0.3);">🔮 ${isEn ? "Quantum Paradigm (QPU / PennyLane / VQE)" : "Paradygmat Kwantowy (QPU / PennyLane / VQE)"}</span>` : ""}
                ${hasNeuromorphic ? `<span class="alignment-badge" style="background:rgba(59,130,246,0.12); color:var(--accent-blue); border-color:rgba(59,130,246,0.3);">🧠 ${isEn ? "Neuromorphic Chips & Spiking Neural Nets (SNN)" : "Architektury Neuromorficzne & Sieci Impulsowe SNN"}</span>` : ""}
                ${hasNuclear ? `<span class="alignment-badge" style="background:rgba(245,158,11,0.12); color:var(--warning); border-color:rgba(245,158,11,0.3);">☢️ ${isEn ? "Fission & Fusion Megaproject H" : "Super-Projekt Jądrowy & Synteza Termojądrowa"}</span>` : ""}
                ${(item.linkedMaterialIds || []).map(mid => `<span class="alignment-badge" style="cursor:pointer;" onclick="event.stopPropagation(); switchTab('materials');">📚 ${mid}</span>`).join("")}
              </div>
            </div>
            <div style="display:flex; gap:0.35rem; align-items:center;">
              <button class="btn btn-sm" title="${isEn ? "Move earlier" : "Przesuń wcześniej w kolejce"}" onclick="moveQueueTopic('${item.id}', -1)">↑</button>
              <button class="btn btn-sm" title="${isEn ? "Move later" : "Przesuń później w kolejce"}" onclick="moveQueueTopic('${item.id}', 1)">↓</button>
              <button class="btn btn-sm" onclick="toggleStudyBlockExpand('${item.id}')">${expanded ? (isEn ? "Collapse ▲" : "Zwiń ▲") : (isEn ? "5-Year Syllabus ▼" : "Sylabus 5 lat z podrozdziałami ▼")}</button>
              <button class="btn btn-sm btn-danger" title="${isEn ? "Remove from queue" : "Usuń z kolejki ciągłej"}" onclick="toggleQueueTopic('${item.id}')">✕</button>
            </div>
          </div>

          ${
            expanded
              ? `
            <div style="margin-top:0.8rem; padding-top:0.75rem; border-top:1px solid var(--border-subtle);">
              ${(item.years || [])
                .map((yrObj) => {
                  const isDone = doneArr.includes(yrObj.year);
                  const absProjectYr = pStart + yrObj.year - 1;
                  const absCalYr = calS + yrObj.year - 1;
                  const subList = (isEn && yrObj.subchaptersEn ? yrObj.subchaptersEn : yrObj.subchaptersPl) || [];
                  const booksList = (isEn && yrObj.coreBooksEn ? yrObj.coreBooksEn : yrObj.coreBooksPl) || (isEn ? item.coreBooksEn : item.coreBooksPl) || [];

                  return `
                  <div class="seq-year-row ${isDone ? "done" : ""}" style="margin-bottom:0.65rem;">
                    <div style="display:flex; align-items:flex-start; gap:0.6rem;">
                      <input type="checkbox" ${isDone ? "checked" : ""} onchange="toggleTopicYearDone('${item.id}', ${yrObj.year})" style="margin-top:0.25rem; width:17px; height:17px; accent-color:var(--success); cursor:pointer;" />
                      <div style="flex:1;">
                        <div style="font-size:0.85rem; font-weight:700; color:${isDone ? "var(--success)" : "var(--text-primary)"};">
                          ${isEn ? `Year ${yrObj.year} of 5 (Project Year ${absProjectYr} • ${absCalYr}/${absCalYr + 1})` : `Rok ${yrObj.year} z 5 (Rok projektowy ${absProjectYr} • ${absCalYr}/${absCalYr + 1})`}
                        </div>
                        <div style="font-size:0.83rem; color:var(--text-secondary); margin-top:0.12rem;">
                          ${escapeHtml(isEn ? yrObj.en : yrObj.pl)}
                        </div>

                        <!-- Szczegółowe podrozdziały roku z checkboxami zaliczenia -->
                        ${
                          subList.length
                            ? `
                          <div style="margin-top:0.5rem; background:var(--bg-card); border:1px solid var(--border-subtle); border-radius:var(--radius-sm); padding:0.45rem 0.65rem;">
                            <div style="font-size:0.71rem; font-weight:700; color:var(--accent-blue); text-transform:uppercase; margin-bottom:0.3rem;">
                              📑 ${isEn ? "Subchapters & Core Knowledge Modules (Check off as you study):" : "Podrozdziały i moduły wiedzy (zaznaczaj w toku nauki):"}
                            </div>
                            ${subList
                              .map((sub, sIdx) => {
                                const subKey = `${item.id}_Y${yrObj.year}_${sIdx + 1}`;
                                const isSubDone = Boolean(completedSubs[subKey]);
                                return `
                                <div class="subchapter-row ${isSubDone ? "done" : ""}">
                                  <input type="checkbox" ${isSubDone ? "checked" : ""} onchange="toggleSubchapterDone('${subKey}')" style="margin-top:0.2rem; width:14px; height:14px; accent-color:var(--success); cursor:pointer;" />
                                  <span style="flex:1;">${escapeHtml(sub)}</span>
                                </div>
                              `;
                              })
                              .join("")}
                          </div>
                        `
                            : ""
                        }

                        <!-- Literatura i powiązane materiały -->
                        ${
                          booksList.length
                            ? `
                          <div style="font-size:0.75rem; color:var(--text-muted); margin-top:0.4rem;">
                            <strong>📖 ${isEn ? "Core Reading:" : "Rekomendowana literatura bazowa:"}</strong> ${booksList.map(b => escapeHtml(b)).join(" • ")}
                          </div>
                        `
                            : ""
                        }
                      </div>
                    </div>
                  </div>
                `;
                })
                .join("")}
            </div>
          `
              : ""
          }
        </div>
      `;
    })
    .join("");

  // Filtrowana baza rozszczepień
  const qSearch = (appState.fissionDbSearch || "").trim().toLowerCase();
  const dbFilteredNodes = allFisNodes.filter((n) => {
    if (appState.manhattanSiteFilter !== "ALL" && n.siteId !== appState.manhattanSiteFilter) return false;
    if (!qSearch) return true;
    const blob = `${n.code} ${n.titlePl} ${n.titleEn} ${n.descPl} ${n.deliverablePl} ${n.siteId} ${n.agentId}`.toLowerCase();
    return blob.includes(qSearch);
  });

  const adminExpanded = Boolean(appState.expandedStudyIds["ADMIN-3Y"]);
  const adminCore = ms.adminCore3Y;

  root.innerHTML = `
    <!-- 1. HERO SZTABU MANHATTAN GOLEM 15 -->
    <div class="manhattan-hero">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
        <div style="max-width:920px;">
          <span class="manhattan-codename-badge">☢️ ${escapeHtml(ms.codename)} • ${isEn ? "FIRST PROJECT COMMAND PAGE" : "STRONA PIERWSZA PROJEKTOWA"}</span>
          <h2 style="font-family:Georgia,'Times New Roman',serif; font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:0.45rem;">
            ${escapeHtml(isEn ? ms.doctrine.titleEn : ms.doctrine.titlePl)}
          </h2>
          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.58;">
            ${escapeHtml(isEn ? ms.doctrine.summaryEn : ms.doctrine.summaryPl)}
          </p>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button class="btn btn-primary" onclick="switchTab('caraudio')">
            🎧 ${isEn ? "Go to Car Audio Road" : "Przejdź do Celowej Drogi (Audio do Samochodu)"}
          </button>
          <button class="btn" onclick="openAiFissionModal('${activeNode ? activeNode.id : "FIS-00"}')">
            ☢️ ${isEn ? "Fission Selected Node (AI)" : "Rozszczep węzeł (AI)"}
          </button>
          <button class="btn" onclick="openCustomFissionNodeModal()">
            ➕ ${isEn ? "New Fission Node" : "Dodaj węzeł"}
          </button>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:0.65rem; margin-top:0.95rem;">
        ${(isEn ? ms.doctrine.rulesEn : ms.doctrine.rulesPl)
          .map(
            (r) => `
          <div style="background:var(--bg-subtle); border:1px solid var(--border-color); border-left:3px solid var(--header-stripe); border-radius:var(--radius-sm); padding:0.6rem 0.8rem; font-size:0.79rem; color:var(--text-primary);">
            ${escapeHtml(r)}
          </div>
        `
          )
          .join("")}
      </div>

      <div class="manhattan-kpi-grid">
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Continuous Study Pipeline" : "Ciągły Szlak Studiów z Rzędu"}</div>
          <div class="manhattan-kpi-val" style="color:var(--warning);">${metrics.totalStudyYears} ${isEn ? "yrs" : "lat"} <span style="font-size:0.82rem; font-weight:600; color:var(--text-muted);">(3 + ${ms.selectedQueue.length}×5)</span></div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${startYr}–${totalEndYr} • ${metrics.totalSemesters} sem. • ${metrics.totalEcts} ECTS</div>
        </div>
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Academic Completion" : "Zaliczony Postęp Studiów"}</div>
          <div class="manhattan-kpi-val" style="color:var(--success);">${metrics.completedYearsTotal} / ${metrics.totalStudyYears} ${isEn ? "yrs" : "lat"} (${metrics.progressPct}%)</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${isEn ? "Admin 3Y + sequential 5Y blocks" : "Administracja (3 l.) + bloki 5-letnie"}</div>
        </div>
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "AI Fission Factor (k_eff)" : "Współczynnik Rozszczepienia k_eff"}</div>
          <div class="manhattan-kpi-val" style="color:var(--danger);">k_eff = ${metrics.kEff}</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${isEn ? "Controlled supercritical chain reaction" : "Kontrolowana reakcja łańcuchowa B+R"}</div>
        </div>
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Fission Graph Database" : "Baza Węzłów Rozszczepień"}</div>
          <div class="manhattan-kpi-val" style="color:var(--accent-blue);">${allFisNodes.length} ${isEn ? "nodes" : "węzłów"}</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${(ms.sites || []).length} ${isEn ? "Manhattan sites" : "ośrodków"} • ${(ms.aiAgents || []).length} ${isEn ? "AI Agents" : "Agentów AI"}</div>
        </div>
      </div>
    </div>

    <!-- 2. PIĘĆ ROZPROSZONYCH OŚRODKÓW PROJEKTU MANHATTAN -->
    <div style="margin-bottom:0.55rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
      <h3 style="font-size:1.05rem;">🏛️ ${isEn ? "I. Five Compartmentalized Manhattan Sites (Click to Filter Fission Graph)" : "I. Pięć Rozproszonych Ośrodków Projektu Manhattan (Kliknij ośrodek, aby filtrować graf)"}</h3>
      ${
        appState.manhattanSiteFilter !== "ALL"
          ? `<button class="btn btn-sm" onclick="selectManhattanSiteFilter('ALL')">🌐 ${isEn ? "Show All 5 Sites" : "Pokaż wszystkie 5 ośrodków"}</button>`
          : ""
      }
    </div>
    <div class="manhattan-sites-grid">
      ${(ms.sites || [])
        .map((s) => {
          const isAct = appState.manhattanSiteFilter === s.id;
          const cnt = allFisNodes.filter((n) => n.siteId === s.id).length;
          return `
          <div class="manhattan-site-card ${isAct ? "active" : ""}" style="--site-color:${s.color};" onclick="selectManhattanSiteFilter('${s.id}')">
            <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.3rem;">
              <span style="font-size:0.74rem; font-weight:800; color:${s.color};">☢ ${escapeHtml(s.code)}</span>
              <span class="foundation-pill" style="font-size:0.68rem;">${cnt} ${isEn ? "nodes" : "węzłów"}</span>
            </div>
            <div style="font-weight:700; font-size:0.92rem; color:var(--text-primary); margin-bottom:0.25rem;">${escapeHtml(isEn ? s.nameEn : s.namePl)}</div>
            <div style="font-size:0.75rem; color:var(--warning); font-weight:600; margin-bottom:0.35rem;">🛡️ ${escapeHtml(s.clearance)}</div>
            <div style="font-size:0.77rem; color:var(--text-secondary); line-height:1.45;">${escapeHtml(isEn ? s.scopeEn : s.scopePl)}</div>
          </div>
        `;
        })
        .join("")}
    </div>

    <!-- 3. GRAF ROZSZCZEPIEŃ OPARTY NA AGENTACH AI -->
    <div class="ws-card" style="padding:1.25rem; margin-bottom:1.5rem;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.6rem; margin-bottom:0.85rem;">
        <div>
          <h3 style="font-size:1.12rem; color:var(--text-primary);">
            ☢️ ${isEn ? "II. AI-Agent Fission Cascade Graph (G0 → G3+)" : "II. Graf Rozszczepień Projektu Oparty na Agentach AI (Kaskada Reakcji G0 → G3+)"}
          </h3>
          <p style="font-size:0.8rem; color:var(--text-muted);">
            ${isEn ? "Visual representation of controlled technological fission. Dashed curves represent cross-track neutron emissions coupling distant fields." : "Wizualizacja reakcji rozszczepienia. Przerywane łuki to emisje neutronów sprzęgające odległe gałęzie wiedzy (np. kwanty z neurobiologią i energetyką jądrową)."}
          </p>
        </div>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
          <button class="btn btn-sm btn-primary" onclick="openAiFissionModal('${activeNode ? activeNode.id : "FIS-00"}')">
            ☢️ ${isEn ? "Split Selected Node via AI" : "Rozszczep zaznaczony węzeł (AI)"}
          </button>
          <button class="btn btn-sm" onclick="openCustomFissionNodeModal()">
            ➕ ${isEn ? "Add Node" : "Własny węzeł"}
          </button>
          <button class="btn btn-sm" onclick="openNewAiAgentModal()">
            🤖 ${isEn ? "Add AI Agent" : "Nowy Agent AI"}
          </button>
        </div>
      </div>

      <div class="fission-split-layout">
        <div class="fission-svg-box">
          ${buildFissionSvgMarkup(ms, isEn)}
        </div>

        <div class="fission-inspector-box">
          ${
            activeNode
              ? `
            <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.4rem;">
              <span class="track-code" style="margin:0; color:${activeSite ? activeSite.color : "var(--accent-blue)"};">
                ☢ ${escapeHtml(activeNode.code)} • GEN G${activeNode.generation}
              </span>
              <select class="select-field" style="width:auto; padding:0.2rem 0.5rem; font-size:0.75rem;" onchange="setFissionNodeStatus('${activeNode.id}', this.value)">
                <option value="active" ${activeNode.status === "active" ? "selected" : ""}>🟢 ${isEn ? "Active Fission" : "Aktywna reakcja"}</option>
                <option value="critical" ${activeNode.status === "critical" ? "selected" : ""}>🔴 ${isEn ? "Critical Priority" : "Stan krytyczny (Priorytet)"}</option>
                <option value="synthesized" ${activeNode.status === "synthesized" ? "selected" : ""}>✅ ${isEn ? "Synthesized" : "Zsyntetyzowano"}</option>
              </select>
            </div>
            <h4 style="font-size:1.02rem; color:var(--text-primary); margin-bottom:0.35rem;">
              ${escapeHtml(isEn ? activeNode.titleEn : activeNode.titlePl)}
            </h4>
            <p style="font-size:0.83rem; color:var(--text-secondary); margin-bottom:0.65rem;">
              ${escapeHtml(isEn ? activeNode.descEn : activeNode.descPl)}
            </p>
            <div style="background:var(--bg-subtle); border:1px solid var(--border-color); border-left:3px solid var(--success); border-radius:var(--radius-sm); padding:0.55rem 0.7rem; font-size:0.79rem; margin-bottom:0.7rem;">
              <strong style="color:var(--success);">🎯 ${isEn ? "Deliverable:" : "Artefakt wyjściowy:"}</strong>
              <div style="color:var(--text-primary); margin-top:0.15rem;">${escapeHtml(isEn ? activeNode.deliverableEn : activeNode.deliverablePl)}</div>
            </div>

            ${
              activeAgent
                ? `
              <div style="background:var(--bg-subtle); border:1px solid var(--border-color); border-radius:var(--radius-sm); padding:0.65rem 0.75rem; margin-bottom:0.75rem;">
                <div style="font-size:0.72rem; text-transform:uppercase; color:${activeAgent.color}; font-weight:800;">
                  🤖 ${escapeHtml(activeAgent.codename)}
                </div>
                <div style="font-size:0.85rem; font-weight:700; color:var(--text-primary); margin:0.1rem 0 0.25rem;">
                  ${escapeHtml(isEn ? activeAgent.nameEn : activeAgent.namePl)}
                </div>
                <div style="font-size:0.76rem; color:var(--text-muted); font-style:italic;">
                  "${escapeHtml(activeAgent.promptTemplate)}"
                </div>
              </div>
            `
                : ""
            }

            <div style="display:flex; flex-direction:column; gap:0.45rem;">
              <button class="btn btn-primary btn-sm" style="width:100%;" onclick="openAiFissionModal('${activeNode.id}')">
                ☢️ ${isEn ? `Fission into Generation G${activeNode.generation + 1} (AI)` : `Rozszczep dalej na Generację G${activeNode.generation + 1} (Agent AI)`}
              </button>
              <button class="btn btn-sm" style="width:100%;" onclick="copyAgentDirectiveToClipboard('${activeNode.id}')">
                📋 ${isEn ? "Copy AI Agent Operational Order" : "Kopiuj rozkaz operacyjny dla Agenta AI"}
              </button>
              <button class="btn btn-success btn-sm" style="width:100%;" onclick="spawnWorkspaceFromFissionNode('${activeNode.id}')">
                🚀 ${isEn ? "Launch Research Workspace from Node" : "Utwórz Środowisko Badawcze z tego rozszczepienia"}
              </button>
              ${
                activeNode.id !== "FIS-00"
                  ? `<button class="btn btn-danger btn-sm" style="width:100%;" onclick="deleteFissionNode('${activeNode.id}')">🗑️ ${isEn ? "Remove Node" : "Usuń ten węzeł z grafu"}</button>`
                  : ""
              }
            </div>
          `
              : ""
          }
        </div>
      </div>
    </div>

    <!-- 4. NIEPRZERWANY SZLAK AKADEMICKI: 3 LATA ADMINISTRACJI + PO 5 LAT Z KAŻDEJ WYBRANEJ TEMATYKI CAŁY CZAS Z RZĘDU -->
    <div class="ws-card" style="padding:1.25rem; margin-bottom:1.5rem;">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.85rem; margin-bottom:0.85rem;">
        <div>
          <h3 style="font-size:1.12rem; color:var(--text-primary);">
            🎓 ${isEn ? "III. Continuous Study Pipeline: 3 Years of Administration + 5 Consecutive Years per Selected Discipline" : "III. Ciągły System Studiów: 3 Lata Administracji + Po 5 Lat Studiów z Każdej Wybranej Tematyki Cały Czas z Rzędu"}
          </h3>
          <p style="font-size:0.82rem; color:var(--text-muted);">
            ${
              isEn
                ? "Select and order your disciplines below. Years 1–3 are permanently anchored in Administration (Manhattan Command Core), followed back-to-back without breaks by 5-year full Master's cycles for each chosen topic."
                : "Wybierz poniżej interesujące Cię tematyki i ustaw ich kolejność. Lata 1–3 to zawsze studia Administracji (rdzeń zarządczy Projektu Manhattan), a zaraz po nich biegną nieprzerwanie z rzędu pełne 5-letnie studia z każdej wybranej dziedziny."
            }
          </p>
        </div>
        <div style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">
          <label style="font-size:0.78rem; color:var(--text-secondary); font-weight:600;">${isEn ? "Start Year:" : "Rok startu:"}</label>
          <input type="number" class="input-field" style="width:92px; padding:0.3rem 0.5rem;" value="${startYr}" min="1990" max="2100" onchange="setManhattanStartYear(this.value)" />
          <button class="btn btn-sm" onclick="applyStudyQueuePreset('DEFAULT')">⭐ ${isEn ? "Core 1–8 + Atom H (48Y)" : "Fundamenty 1–8 + Atom H (48 lat)"}</button>
          <button class="btn btn-sm" onclick="applyStudyQueuePreset('FOUNDATIONS')">🏛️ ${isEn ? "8 Foundations (43Y)" : "8 Dziedzin Podstawowych (43 lata)"}</button>
          <button class="btn btn-sm" onclick="applyStudyQueuePreset('TRACKS')">🗺️ ${isEn ? "Tracks A–H (43Y)" : "Ścieżki A–H (43 lata)"}</button>
          <button class="btn btn-sm" onclick="applyStudyQueuePreset('ALL16')">⚡ ${isEn ? "All 16 Topics (83Y)" : "Pełne 16 kierunków (83 lata)"}</button>
        </div>
      </div>

      <!-- Selektor wybieranych 5-letnich tematyk -->
      <div style="background:var(--bg-subtle); border:1px solid var(--border-color); border-radius:var(--radius-sm); padding:0.8rem; margin-bottom:1rem;">
        <div style="font-size:0.75rem; font-weight:700; color:var(--accent-blue); text-transform:uppercase; margin-bottom:0.45rem;">
          ✓ ${isEn ? "Click to toggle 5-year specializations in your sequential back-to-back queue:" : "Kliknij, aby włączyć lub wyłączyć 5-letnie kierunki studiów w Twoim ciągu realizowanym z rzędu:"}
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
          ${(ms.fiveYearCatalog || [])
            .map((cat) => {
              const selIdx = (ms.selectedQueue || []).indexOf(cat.id);
              const isSelected = selIdx >= 0;
              return `
                <button type="button" class="topic-selector-chip ${isSelected ? "selected" : ""}" onclick="toggleQueueTopic('${cat.id}')">
                  <span>${isSelected ? `#${selIdx + 1} ✓` : "+"}</span>
                  <span>${cat.icon} ${escapeHtml((isEn ? cat.titleEn : cat.titlePl).split("(")[0].trim())}</span>
                </button>
              `;
            })
            .join("")}
        </div>
      </div>

      <!-- Wizualna wstęga ciągła 3 + 5×N lat -->
      <div class="seq-ribbon">
        ${ribbonStepsHtml.join("")}
      </div>

      <!-- BLOK 0: 3 LATA STUDIÓW ADMINISTRACJI (OBOWIĄZKOWY RDZEŃ MANHATTAN) -->
      <div class="ws-card" style="border-left:4px solid var(--warning); background:var(--bg-subtle); margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.6rem;">
          <div style="cursor:pointer;" onclick="toggleStudyBlockExpand('ADMIN-3Y')">
            <div style="display:flex; align-items:center; gap:0.45rem; flex-wrap:wrap; margin-bottom:0.2rem;">
              <span class="foundation-pill" style="font-size:0.7rem; font-weight:800; border-color:var(--warning); color:var(--warning);">
                ${isEn ? `FOUNDATIONAL COMMAND • YEARS 1–3 (${startYr}–${adminEndYr})` : `OGNIWO ZEROWE (SZTAB) • LATA 1–3 (${startYr}–${adminEndYr})`}
              </span>
              <span class="foundation-pill" style="font-size:0.69rem; color:var(--warning); border-color:var(--warning);">☢ DISTRICT W-0</span>
              ${renderLangBadgeHtml("PL+EN")}
              <span style="font-size:0.75rem; color:var(--success); font-weight:700;">${adminDoneCount}/3 ${isEn ? "years completed" : "lata zaliczone"} (180 ECTS)</span>
            </div>
            <h4 style="font-size:1.05rem; color:var(--text-primary);">🏛️ ${escapeHtml(isEn ? adminCore.titleEn : adminCore.titlePl)}</h4>
            <p style="font-size:0.8rem; color:var(--text-secondary);">${escapeHtml(isEn ? adminCore.subtitleEn : adminCore.subtitlePl)}</p>
          </div>
          <button class="btn btn-sm" onclick="toggleStudyBlockExpand('ADMIN-3Y')">
            ${adminExpanded ? (isEn ? "Collapse ▲" : "Zwiń ▲") : (isEn ? "3-Year Syllabus ▼" : "Program 3 lat z podrozdziałami ▼")}
          </button>
        </div>

        ${
          adminExpanded
            ? `
          <div style="margin-top:0.85rem; padding-top:0.8rem; border-top:1px solid var(--border-color);">
            ${(adminCore.years || [])
              .map((yrObj) => {
                const isDone = (adminCore.completedYears || []).includes(yrObj.year);
                const calYr = startYr + yrObj.year - 1;
                const subList = (isEn && yrObj.subchaptersEn ? yrObj.subchaptersEn : yrObj.subchaptersPl) || [];
                const booksList = (isEn && yrObj.coreBooksEn ? yrObj.coreBooksEn : yrObj.coreBooksPl) || [];

                return `
                <div class="seq-year-row ${isDone ? "done" : ""}" style="background:var(--bg-card); margin-bottom:0.65rem;">
                  <div style="display:flex; align-items:flex-start; gap:0.6rem;">
                    <input type="checkbox" ${isDone ? "checked" : ""} onchange="toggleAdminYearDone(${yrObj.year})" style="margin-top:0.25rem; width:17px; height:17px; accent-color:var(--success); cursor:pointer;" />
                    <div style="flex:1;">
                      <div style="font-size:0.86rem; font-weight:700; color:${isDone ? "var(--success)" : "var(--text-primary)"};">
                        ${escapeHtml(isEn ? yrObj.titleEn : yrObj.titlePl)} • ${escapeHtml(yrObj.semesters)} (${calYr}/${calYr + 1})
                      </div>
                      <ul style="margin:0.3rem 0 0.35rem; padding-left:1.15rem; font-size:0.8rem; color:var(--text-secondary);">
                        ${(isEn ? yrObj.coursesEn : yrObj.coursesPl).map((c) => `<li>${escapeHtml(c)}</li>`).join("")}
                      </ul>

                      <!-- Podrozdziały Administracji z checkboxami -->
                      ${
                        subList.length
                          ? `
                        <div style="margin-top:0.45rem; background:var(--bg-subtle); border:1px solid var(--border-subtle); border-radius:var(--radius-sm); padding:0.45rem 0.65rem;">
                          <div style="font-size:0.71rem; font-weight:700; color:var(--warning); text-transform:uppercase; margin-bottom:0.25rem;">
                            📑 ${isEn ? "Administration Subchapters (Check off as you study):" : "Podrozdziały Administracji (zaznaczaj zaliczone partie materiału):"}
                          </div>
                          ${subList
                            .map((sub, sIdx) => {
                              const subKey = `ADMIN-3Y_Y${yrObj.year}_${sIdx + 1}`;
                              const isSubDone = Boolean(completedSubs[subKey]);
                              return `
                              <div class="subchapter-row ${isSubDone ? "done" : ""}">
                                <input type="checkbox" ${isSubDone ? "checked" : ""} onchange="toggleSubchapterDone('${subKey}')" style="margin-top:0.2rem; width:14px; height:14px; accent-color:var(--success); cursor:pointer;" />
                                <span style="flex:1;">${escapeHtml(sub)}</span>
                              </div>
                            `;
                            })
                            .join("")}
                        </div>
                      `
                          : ""
                      }

                      <!-- Powiązane materiały i literatura sztabowa -->
                      <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-top:0.4rem; align-items:center;">
                        ${(yrObj.linkedMaterialIds || []).map(mid => `<span class="alignment-badge" style="cursor:pointer;" onclick="switchTab('materials');">📚 ${mid}</span>`).join("")}
                        ${booksList.length ? `<span style="font-size:0.75rem; color:var(--text-muted);"><strong>📖 Podręczniki:</strong> ${booksList.map(b => escapeHtml(b)).join(" • ")}</span>` : ""}
                      </div>

                      <div style="font-size:0.77rem; color:var(--accent-blue); margin-top:0.35rem;">
                        <strong>🎯 ${isEn ? "Administrative Milestone:" : "Kamień milowy Sztabu W-0:"}</strong> ${escapeHtml(isEn ? yrObj.deliverableEn : yrObj.deliverablePl)}
                      </div>
                    </div>
                  </div>
                </div>
              `;
              })
              .join("")}
          </div>
        `
            : ""
        }
      </div>

      <!-- BLOKI 1..N: PO 5 LAT Z KAŻDEJ WYBRANEJ TEMATYKI CAŁY CZAS Z RZĘDU -->
      ${queueBlocksHtml}
    </div>

    <!-- 5. BAZA ROZSZCZEPIEŃ PROJEKTU I REJESTR FLOTY AGENTÓW AI -->
    <div class="ws-card" style="padding:1.25rem;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem; margin-bottom:1rem;">
        <div>
          <h3 style="font-size:1.08rem; color:var(--text-primary);">
            🗄️ ${isEn ? "IV. Project Fission Database & Specialized AI Agent Fleet" : "IV. Baza Rozszczepień Projektu oraz Rejestr Floty Agentów AI"}
          </h3>
          <p style="font-size:0.8rem; color:var(--text-muted);">
            ${isEn ? "Complete persistent registry of fission work packages and autonomous AI Agent personas." : "Pełny rejestr wszystkich rozszczepionych pakietów badawczych oraz person operacyjnych Agentów AI."}
          </p>
        </div>
        <input
          type="search"
          class="input-field"
          style="max-width:320px;"
          placeholder="${isEn ? "Search fission nodes, codes, agents..." : "Szukaj w bazie rozszczepień (kod, tytuł, agent)..."}"
          value="${escapeHtml(appState.fissionDbSearch)}"
          oninput="appState.fissionDbSearch = this.value; renderManhattanView();"
        />
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(310px, 1fr)); gap:0.75rem; margin-bottom:1.5rem;">
        ${dbFilteredNodes
          .map((n) => {
            const s = sitesById[n.siteId] || { color: "var(--accent-blue)", code: n.siteId };
            const a = agentsById[n.agentId] || { codename: n.agentId };
            return `
            <div class="ws-card" style="border-left:3px solid ${s.color}; cursor:pointer;" onclick="selectFissionNode('${n.id}')">
              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.73rem; margin-bottom:0.25rem;">
                <strong style="color:${s.color};">☢ ${escapeHtml(n.code)} • G${n.generation}</strong>
                <span style="color:var(--text-muted);">🤖 ${escapeHtml(a.codename)}</span>
              </div>
              <div style="font-weight:700; font-size:0.88rem; color:var(--text-primary); margin-bottom:0.2rem;">${escapeHtml(isEn ? n.titleEn : n.titlePl)}</div>
              <div style="font-size:0.77rem; color:var(--text-secondary); margin-bottom:0.35rem;">${escapeHtml(isEn ? n.descEn : n.descPl)}</div>
              <div style="font-size:0.73rem; color:var(--success); font-weight:600;">🎯 ${escapeHtml(isEn ? n.deliverableEn : n.deliverablePl)}</div>
            </div>
          `;
          })
          .join("")}
      </div>

      <h4 style="font-size:0.96rem; color:var(--accent-blue); margin-bottom:0.7rem;">
        🤖 ${isEn ? "Specialized Manhattan AI Agents (System Prompts)" : "Flota Wyspecjalizowanych Agentów AI (Gotowe Rozkazy Systemowe)"}
      </h4>
      <div class="agent-card-grid">
        ${(ms.aiAgents || [])
          .map((agt) => {
            const s = sitesById[agt.siteId] || { code: agt.siteId };
            return `
            <div class="ws-card" style="border-top:3px solid ${agt.color};">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.25rem;">
                <span style="font-size:0.74rem; font-weight:800; color:${agt.color};">🤖 ${escapeHtml(agt.codename)}</span>
                <span class="foundation-pill" style="font-size:0.66rem;">${escapeHtml(s.code)}</span>
              </div>
              <div style="font-weight:700; font-size:0.9rem; color:var(--text-primary); margin-bottom:0.25rem;">${escapeHtml(isEn ? agt.nameEn : agt.namePl)}</div>
              <p style="font-size:0.78rem; color:var(--text-secondary); margin-bottom:0.45rem;">${escapeHtml(isEn ? agt.roleEn : agt.rolePl)}</p>
              <div style="background:var(--bg-subtle); border:1px solid var(--border-subtle); padding:0.45rem 0.6rem; border-radius:var(--radius-sm); font-size:0.73rem; color:var(--text-muted); font-style:italic;">
                "${escapeHtml(agt.promptTemplate)}"
              </div>
            </div>
          `;
          })
          .join("")}
      </div>
    </div>
  `;
}

/* ============================================================================
   MODUŁ: AUDIO DO SAMOCHODU — CELOWA DROGA EKOSYSTEMU (CAR-FRIENDLY AUDIO PLAYER)
   Web Speech API TTS, duże przyciski dotykowe w trasie, 18 odcinków w 4 etapach
   ============================================================================ */

let carAudioSpeechUtterance = null;

function playCarAudioEpisode(epId) {
  if (!appState.data || !appState.data.manhattanSystem) return;
  const ep = (appState.data.manhattanSystem.carAudioRoad || []).find((e) => e.id === epId);
  if (!ep) return;

  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }

  appState.carAudioPlayingId = epId;
  const isEn = appState.lang === "en";
  const spokenText = (isEn && ep.spokenBriefingEn ? ep.spokenBriefingEn : ep.spokenBriefingPl) || "";

  if (!window.speechSynthesis) {
    showToast(isEn ? "SpeechSynthesis API not supported in this browser." : "Twoja przeglądarka nie obsługuje syntezy mowy Web Speech API.");
    renderCarAudioView();
    return;
  }

  const u = new SpeechSynthesisUtterance(spokenText);
  u.lang = isEn ? "en-US" : "pl-PL";
  u.rate = appState.carAudioRate || 1.15;
  u.pitch = 1.0;

  const voices = window.speechSynthesis.getVoices() || [];
  const matchingVoice = voices.find((v) => isEn ? v.lang.startsWith("en") : v.lang.startsWith("pl"));
  if (matchingVoice) u.voice = matchingVoice;

  u.onend = () => {
    const ms = appState.data.manhattanSystem;
    ms.completedCarAudio = ms.completedCarAudio || {};
    ms.completedCarAudio[epId] = true;
    saveState();

    if (appState.carAudioAutoPlay) {
      const road = ms.carAudioRoad || [];
      const currIdx = road.findIndex((e) => e.id === epId);
      if (currIdx >= 0 && currIdx + 1 < road.length) {
        const nextEp = road[currIdx + 1];
        setTimeout(() => {
          playCarAudioEpisode(nextEp.id);
        }, 1200);
        return;
      }
    }
    appState.carAudioPlayingId = null;
    renderCarAudioView();
    renderNavCounts();
  };

  u.onerror = (err) => {
    console.warn("TTS Error:", err);
    appState.carAudioPlayingId = null;
    renderCarAudioView();
  };

  carAudioSpeechUtterance = u;
  window.speechSynthesis.speak(u);
  showToast(isEn ? `Now playing: ${ep.titleEn}` : `Odtwarzanie: ${ep.titlePl}`);
  renderCarAudioView();
}

function pauseCarAudio() {
  if (window.speechSynthesis) {
    if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {
      window.speechSynthesis.pause();
    } else if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }
  }
  renderCarAudioView();
}

function stopCarAudio() {
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
  appState.carAudioPlayingId = null;
  renderCarAudioView();
}

function setCarAudioRate(newRate) {
  appState.carAudioRate = parseFloat(newRate);
  if (appState.carAudioPlayingId) {
    playCarAudioEpisode(appState.carAudioPlayingId);
  } else {
    renderCarAudioView();
  }
}

function toggleCarAudioAutoPlay() {
  appState.carAudioAutoPlay = !appState.carAudioAutoPlay;
  showToast(appState.carAudioAutoPlay ? "Auto-Play w trasie: WŁĄCZONE (ciągłe odtwarzanie)" : "Auto-Play w trasie: WYŁĄCZONE");
  renderCarAudioView();
}

function toggleCarAudioDone(epId) {
  if (!appState.data || !appState.data.manhattanSystem) return;
  const ms = appState.data.manhattanSystem;
  ms.completedCarAudio = ms.completedCarAudio || {};
  ms.completedCarAudio[epId] = !ms.completedCarAudio[epId];
  saveState();
  renderCarAudioView();
  renderNavCounts();
}

function selectCarAudioStageFilter(stage) {
  appState.carAudioStageFilter = stage;
  renderCarAudioView();
}

function openNewCarAudioModal() {
  const isEn = appState.lang === "en";
  const modalHtml = `
    <div id="newCarAudioModal" class="modal-backdrop" onclick="if(event.target===this) this.remove();">
      <div class="modal-card" style="max-width:540px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
          <h3 style="margin:0;">➕ ${isEn ? "Add Custom Car Audio Episode" : "Dodaj Własny Odcinek do Trasy Samochodowej"}</h3>
          <button class="btn btn-sm" onclick="document.getElementById('newCarAudioModal').remove();">✕</button>
        </div>
        <form onsubmit="saveCustomCarAudioEpisode(event)">
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Episode Title (PL)*" : "Tytuł odcinka (PL)*"}</label>
            <input type="text" id="custCarTitlePl" class="input-field" required placeholder="np. Odcinek 19: Moje podsumowanie..." />
          </div>
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Stage" : "Etap Drogi"}</label>
            <select id="custCarStage" class="select-field">
              <option value="I">Etap I: Sztab W-0 & Administracja</option>
              <option value="II">Etap II: 8 Fundamentów Naukowych</option>
              <option value="III">Etap III: Ścieżki Badawcze A–G</option>
              <option value="IV" selected>Etap IV: Super-Projekt H & Synteza</option>
            </select>
          </div>
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Duration (minutes)" : "Szacowany czas słuchania (minuty)"}</label>
            <input type="number" id="custCarDuration" class="input-field" value="20" min="1" max="180" />
          </div>
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Spoken Briefing Text (Read aloud by TTS)*" : "Treść do odczytania w trasie przez Lektora TTS*"}</label>
            <textarea id="custCarBriefing" class="input-field" rows="4" required placeholder="Tekst, który ma czytać syntezator mowy w samochodzie..."></textarea>
          </div>
          <div style="margin-bottom:1rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "External Audio / Podcast Link (optional)" : "Zewnętrzny link do wykładu/podcastu (opcjonalnie)"}</label>
            <input type="url" id="custCarLink" class="input-field" placeholder="https://..." />
          </div>
          <div style="display:flex; justify-content:flex-end; gap:0.5rem;">
            <button type="button" class="btn" onclick="document.getElementById('newCarAudioModal').remove();">${isEn ? "Cancel" : "Anuluj"}</button>
            <button type="submit" class="btn btn-primary">${isEn ? "Save Episode" : "Zapisz odcinek"}</button>
          </div>
        </form>
      </div>
    </div>
  `;
  const existing = document.getElementById("newCarAudioModal");
  if (existing) existing.remove();
  document.body.insertAdjacentHTML("beforeend", modalHtml);
}

function saveCustomCarAudioEpisode(e) {
  e.preventDefault();
  const title = document.getElementById("custCarTitlePl").value.trim();
  const stage = document.getElementById("custCarStage").value;
  const duration = parseInt(document.getElementById("custCarDuration").value, 10) || 15;
  const briefing = document.getElementById("custCarBriefing").value.trim();
  const extLink = document.getElementById("custCarLink").value.trim();

  if (!title || !briefing) return;
  const ms = appState.data.manhattanSystem;
  ms.carAudioRoad = ms.carAudioRoad || [];
  const epNum = ms.carAudioRoad.length + 1;
  const newEp = {
    id: `car-ep-${String(epNum).padStart(2, "0")}`,
    order: epNum,
    stage: stage,
    stageNamePl: `Etap ${stage}`,
    stageNameEn: `Stage ${stage}`,
    titlePl: title,
    titleEn: title,
    estimatedDurationMin: duration,
    spokenBriefingPl: briefing,
    spokenBriefingEn: briefing,
    keyTakeawaysPl: ["Własny odcinek dodany przez użytkownika."],
    curatedAudioLinks: extLink ? [{ title: "Materiały zewnętrzne", url: extLink, lang: "PL", type: "podcast" }] : []
  };

  ms.carAudioRoad.push(newEp);
  saveState(appState.lang === "en" ? "Car audio episode added." : "Dodano nowy odcinek do trasy samochodowej.");
  const m = document.getElementById("newCarAudioModal");
  if (m) m.remove();
  renderCarAudioView();
  renderNavCounts();
}

function renderCarAudioView() {
  const root = document.getElementById("carAudioRootContainer");
  if (!root || !appState.data || !appState.data.manhattanSystem) return;

  const isEn = appState.lang === "en";
  const ms = appState.data.manhattanSystem;
  const road = ms.carAudioRoad || [];
  const doneMap = ms.completedCarAudio || {};
  const doneCount = road.filter((e) => Boolean(doneMap[e.id])).length;
  const pct = road.length ? Math.round((doneCount / road.length) * 100) : 0;
  const totalMin = road.reduce((acc, e) => acc + (e.estimatedDurationMin || 20), 0);
  const totalHrs = Math.floor(totalMin / 60);
  const remMin = totalMin % 60;

  const isSpeaking = window.speechSynthesis && window.speechSynthesis.speaking && !window.speechSynthesis.paused;
  const isPaused = window.speechSynthesis && window.speechSynthesis.paused;
  const currentPlayingEp = road.find((e) => e.id === appState.carAudioPlayingId) || null;

  // Filtrowanie etapów i profili jazdy
  const stageFlt = appState.carAudioStageFilter || "ALL";
  const profileFlt = appState.carAudioProfileFilter || "ALL";

  const filteredRoad = road.filter((e) => {
    if (stageFlt !== "ALL" && e.stage !== stageFlt) return false;
    if (profileFlt !== "ALL") {
      const dur = e.estimatedDurationMin || 20;
      if (profileFlt === "URBAN" && dur > 20) return false;
      if (profileFlt === "SUBURBAN" && (dur <= 20 || dur > 26)) return false;
      if (profileFlt === "HIGHWAY" && dur <= 26) return false;
    }
    return true;
  });

  const stageColors = {
    "0": "var(--warning)",
    "I": "var(--accent-blue)",
    "II": "var(--danger)",
    "III": "var(--success)",
    "IV": "var(--accent-purple)",
    "V": "var(--warning)",
    "VI": "var(--header-stripe)"
  };

  root.innerHTML = `
    <!-- NAGŁÓWEK BAZY AUDIO DO SAMOCHODU -->
    <div style="background:var(--bg-card); border:1px solid var(--border-color); border-top:4px solid var(--accent-blue); border-radius:var(--radius-md); padding:1.25rem 1.4rem; margin-bottom:1.15rem; box-shadow:var(--shadow-sm);">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.85rem;">
        <div>
          <span class="manhattan-codename-badge" style="background:rgba(15,76,129,0.12); color:var(--accent-blue); border-color:rgba(15,76,129,0.3);">
            🎧 ${isEn ? "CAR AUDIO HUB • PURPOSEFUL ROUTE" : "BAZA AUDIO DO SAMOCHODU • CELOWA DROGA EKOSYSTEMU"}
          </span>
          <h2 style="font-family:Georgia,'Times New Roman',serif; font-size:1.35rem; font-weight:800; color:var(--text-primary); margin:0.35rem 0 0.25rem;">
            ${isEn ? "The Golem 15 Purposeful Commute & Driving Knowledge Route" : "Celowa Droga Odsłuchowa Ekosystemu Golem 15 — Baza Wiedzy do Samochodu"}
          </h2>
          <p style="font-size:0.88rem; color:var(--text-secondary); margin:0; line-height:1.55; max-width:980px;">
            ${
              isEn
                ? "A comprehensive car-friendly audio hub designed for purposeful listening during commutes and long road trips. The sequential road leads you from Administrative Governance and Formal Mathematics, through the Silicon Wall, Quantum Computing, and Neuroscience, to Nuclear Energy, Biospheres, and Stanisław Lem's philosophy."
                : "Ogólna, przekrojowa baza audycji i materiałów odsłuchowych przygotowana specjalnie do regularnego słuchania w trasie i podczas dojazdów. Celowa droga prowadzi Cię sekwencyjnie od podstaw prawa sztabowego i matematyki, przez kres krzemu, komputery kwantowe i neurobiologię, aż po energetykę jądrową, inżynierię biosfery i filozofię Stanisława Lema."
            }
          </p>
        </div>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
          <button class="btn btn-sm btn-primary" onclick="openNewCarAudioModal()">
            ➕ ${isEn ? "Add Custom Episode" : "Dodaj własną audycję"}
          </button>
          <button class="btn btn-sm" onclick="switchTab('manhattan')">
            ☢️ ${isEn ? "Back to Manhattan" : "Powrót do Manhattanu"}
          </button>
        </div>
      </div>

      <!-- KARTY WSKAŹNIKÓW TRASY -->
      <div class="manhattan-kpi-grid" style="margin-top:1rem;">
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Roadtrip Completion" : "Zaliczono w Trasie"}</div>
          <div class="manhattan-kpi-val" style="color:var(--success);">${doneCount} / ${road.length} ${isEn ? "episodes" : "odc."} (${pct}%)</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${road.length - doneCount} ${isEn ? "episodes remaining" : "odcinków do ukończenia"}</div>
        </div>
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Total Ecosystem Journey" : "Łączny Czas Celowej Drogi"}</div>
          <div class="manhattan-kpi-val" style="color:var(--warning);">~${totalHrs}h ${remMin}min</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${road.length} ${isEn ? "sequential chapters" : "ogniw w łańcuchu trasy"}</div>
        </div>
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Hands-Free Lector" : "Wbudowany Lektor TTS"}</div>
          <div class="manhattan-kpi-val" style="color:var(--accent-blue);">${appState.carAudioRate}x ${isEn ? "speed" : "tempo"}</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${isSpeaking ? "🟢 " + (isEn ? "Active on road" : "Czyta w trasie") : (isPaused ? "⏸️ " + (isEn ? "Paused" : "Wstrzymano") : "⚪ " + (isEn ? "Standing by" : "Gotowy do jazdy"))}</div>
        </div>
        <div class="manhattan-kpi-card">
          <div class="manhattan-kpi-label">${isEn ? "Continuous Driving Mode" : "Tryb Ciągłej Jazdy"}</div>
          <div class="manhattan-kpi-val" style="color:${appState.carAudioAutoPlay ? "var(--success)" : "var(--text-muted);"}">${appState.carAudioAutoPlay ? "AUTO-PLAY ON" : "AUTO-PLAY OFF"}</div>
          <div style="font-size:0.74rem; color:var(--text-muted);">${isEn ? "Plays next episode seamlessly" : "Automatyczny start kolejnego odcinka"}</div>
        </div>
      </div>
    </div>

    <!-- TACTILE CAR PLAYER DECK (Pulpit dotykowy do samochodu z dużymi przyciskami) -->
    <div class="car-player-deck">
      <div class="car-player-hero">
        <div>
          <div style="font-size:0.74rem; font-weight:800; color:var(--accent-blue); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.25rem;">
            🚘 ${isEn ? "HANDS-FREE VEHICLE DECK • ACTIVE EPISODE" : "SAMOCHODOWY ODTWARZACZ DOTYKOWY • AKTYWNY ODCINEK"}
          </div>
          <h3 style="font-size:1.18rem; font-weight:800; color:var(--text-primary); margin:0 0 0.25rem 0;">
            ${
              currentPlayingEp
                ? `▶ Odcinek ${currentPlayingEp.order}: ${escapeHtml(isEn ? currentPlayingEp.titleEn : currentPlayingEp.titlePl)}`
                : (isEn ? "Ready to drive. Select an episode or press START ROAD." : "Gotowy do drogi. Wybierz odcinek z listy lub naciśnij START TRASY.")
            }
          </h3>
          <div style="font-size:0.79rem; color:var(--text-muted);">
            ${
              currentPlayingEp
                ? `⏱️ ~${currentPlayingEp.estimatedDurationMin || 20} min • ${escapeHtml(currentPlayingEp.stageNamePl)} • ${currentPlayingEp.tripProfile || "Trasa uniwersalna"}`
                : (isEn ? "Audio roadtrip standing by • Web Speech API TTS ready" : "Celowa droga w gotowości • Wbudowany syntezator mowy TTS gotowy")
            }
          </div>
        </div>

        <!-- Duże dotykowe przyciski samochodowe -->
        <div class="car-btn-group">
          ${
            isSpeaking
              ? `<button class="car-btn-tactile car-btn-play" onclick="pauseCarAudio()">⏸️ ${isEn ? "PAUSE" : "PAUZA"}</button>`
              : isPaused
              ? `<button class="car-btn-tactile car-btn-play" onclick="pauseCarAudio()">▶️ ${isEn ? "RESUME" : "WZNÓW"}</button>`
              : `<button class="car-btn-tactile car-btn-play" onclick="playCarAudioEpisode('${currentPlayingEp ? currentPlayingEp.id : (road[0] ? road[0].id : '')}')">▶️ ${isEn ? "START ROAD" : "START TRASY"}</button>`
          }
          <button class="car-btn-tactile btn" style="border:1px solid var(--border-color);" onclick="stopCarAudio()">⏹️ ${isEn ? "STOP" : "ZATRZYMAJ"}</button>
          
          <!-- Przełącznik tempa lektora -->
          <div style="display:inline-flex; border:1px solid var(--border-color); border-radius:var(--radius-sm); overflow:hidden;">
            <button class="btn btn-sm ${appState.carAudioRate === 1.0 ? "btn-primary" : ""}" style="border-radius:0; padding:0.5rem 0.7rem; font-weight:700;" onclick="setCarAudioRate(1.0)">1.0x</button>
            <button class="btn btn-sm ${appState.carAudioRate === 1.15 ? "btn-primary" : ""}" style="border-radius:0; padding:0.5rem 0.7rem; font-weight:700;" onclick="setCarAudioRate(1.15)">1.15x</button>
            <button class="btn btn-sm ${appState.carAudioRate === 1.25 ? "btn-primary" : ""}" style="border-radius:0; padding:0.5rem 0.7rem; font-weight:700;" onclick="setCarAudioRate(1.25)">1.25x</button>
            <button class="btn btn-sm ${appState.carAudioRate === 1.5 ? "btn-primary" : ""}" style="border-radius:0; padding:0.5rem 0.7rem; font-weight:700;" onclick="setCarAudioRate(1.5)">1.5x</button>
          </div>

          <!-- Przełącznik Auto-Play -->
          <button class="car-btn-tactile btn ${appState.carAudioAutoPlay ? "btn-success" : ""}" style="font-size:0.85rem;" onclick="toggleCarAudioAutoPlay()" title="${isEn ? "Continuous playback on road" : "Ciągłe odtwarzanie kolejnych odcinków w trasie"}">
            🚘 ${appState.carAudioAutoPlay ? (isEn ? "Auto-Play: ON" : "Auto-Play: WŁ") : (isEn ? "Auto-Play: OFF" : "Auto-Play: WYŁ")}
          </button>
        </div>
      </div>

      <!-- Wizualny pasek postępu całej drogi -->
      <div class="car-road-progress">
        <div class="car-road-progress-fill" style="width:${pct}%;"></div>
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem; color:var(--text-muted); margin-top:0.35rem;">
        <span>🎯 ${isEn ? "Roadtrip Progress:" : "Zaliczono w trasie:"} <strong>${doneCount} / ${road.length} ${isEn ? "episodes" : "odcinków"} (${pct}%)</strong></span>
        <span>⏱️ ${isEn ? "Total Journey:" : "Całkowity czas drogi:"} <strong>~${totalHrs}h ${remMin}min</strong></span>
      </div>
    </div>

    <!-- FILTRACJA ETAPÓW CELOWEJ DROGI ORAZ CZASU JAZDY -->
    <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-sm); padding:0.8rem 1rem; margin-bottom:1.15rem;">
      <div style="font-size:0.75rem; font-weight:700; color:var(--accent-blue); text-transform:uppercase; margin-bottom:0.45rem;">
        🛣️ ${isEn ? "Select Ecosystem Stage along Purposeful Route:" : "Wybierz Etap Celowej Drogi Ekosystemu:"}
      </div>
      <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:0.75rem;">
        <button class="topic-selector-chip ${stageFlt === "ALL" ? "selected" : ""}" onclick="selectCarAudioStageFilter('ALL')">
          ${isEn ? "All 20 Episodes" : "Wszystkie 20 Odcinków"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "0" ? "selected" : ""}" onclick="selectCarAudioStageFilter('0')">
          🏛️ ${isEn ? "Stage 0: HQ & Law (2)" : "Etap 0: Sztab W-0 & Prawo B+R (2)"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "I" ? "selected" : ""}" onclick="selectCarAudioStageFilter('I')">
          📐 ${isEn ? "Stage I: Foundations & Physics (5)" : "Etap I: Fundamenty Formalne & Fizyka (5)"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "II" ? "selected" : ""}" onclick="selectCarAudioStageFilter('II')">
          ⚡ ${isEn ? "Stage II: Silicon Wall & QPU (3)" : "Etap II: Kres Krzemu & Nowy Hardware (3)"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "III" ? "selected" : ""}" onclick="selectCarAudioStageFilter('III')">
          🧠 ${isEn ? "Stage III: Brain & WBE (2)" : "Etap III: Mózg, Bionika & WBE (2)"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "IV" ? "selected" : ""}" onclick="selectCarAudioStageFilter('IV')">
          🧬 ${isEn ? "Stage IV: Life & Biosphere (2)" : "Etap IV: Inżynieria Życia & Biosfera (2)"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "V" ? "selected" : ""}" onclick="selectCarAudioStageFilter('V')">
          ☢️ ${isEn ? "Stage V: Nuclear & Space (3)" : "Etap V: Super-Projekt Jądrowy H & Kosmos (3)"}
        </button>
        <button class="topic-selector-chip ${stageFlt === "VI" ? "selected" : ""}" onclick="selectCarAudioStageFilter('VI')">
          📜 ${isEn ? "Stage VI: Lem's Philosophy (3)" : "Etap VI: Filozofia Przyszłości & Lem (3)"}
        </button>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; padding-top:0.45rem; border-top:1px dashed var(--border-subtle);">
        <div style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">
          🚗 ${isEn ? "Filter by Driving Commute Profile:" : "Filtruj według czasu trasy samochodem:"}
        </div>
        <div style="display:flex; gap:0.35rem; flex-wrap:wrap;">
          <button class="btn btn-sm ${profileFlt === "ALL" ? "btn-primary" : ""}" onclick="appState.carAudioProfileFilter = 'ALL'; renderCarAudioView();">${isEn ? "All Durations" : "Wszystkie czasy"}</button>
          <button class="btn btn-sm ${profileFlt === "URBAN" ? "btn-primary" : ""}" onclick="appState.carAudioProfileFilter = 'URBAN'; renderCarAudioView();">${isEn ? "Urban (~18–20m)" : "🚗 Trasa miejska (~18–20 min)"}</button>
          <button class="btn btn-sm ${profileFlt === "SUBURBAN" ? "btn-primary" : ""}" onclick="appState.carAudioProfileFilter = 'SUBURBAN'; renderCarAudioView();">${isEn ? "Suburban (~22–26m)" : "🚙 Trasa podmiejska (~22–26 min)"}</button>
          <button class="btn btn-sm ${profileFlt === "HIGHWAY" ? "btn-primary" : ""}" onclick="appState.carAudioProfileFilter = 'HIGHWAY'; renderCarAudioView();">${isEn ? "Highway (28m+)" : "🛣️ Trasa daleka (28 min+)"}</button>
        </div>
      </div>
    </div>

    <!-- LISTA ODCINKÓW CELOWEJ DROGI (20 MODUŁÓW) -->
    <div style="display:flex; flex-direction:column; gap:0.95rem;">
      ${filteredRoad
        .map((ep) => {
          const isDone = Boolean(doneMap[ep.id]);
          const isPlayingThis = appState.carAudioPlayingId === ep.id;
          const stageCol = stageColors[ep.stage] || "var(--accent-blue)";
          const extLinks = ep.curatedAudioLinks || [];
          const takeaways = (isEn && ep.keyTakeawaysEn ? ep.keyTakeawaysEn : ep.keyTakeawaysPl) || ep.keyTakeawaysPl || [];

          return `
          <div class="car-episode-card ${isPlayingThis ? "is-playing" : ""} ${isDone ? "is-done" : ""}" style="--stage-color:${stageCol};">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.6rem; margin-bottom:0.45rem;">
              <div>
                <div style="display:flex; align-items:center; gap:0.45rem; flex-wrap:wrap; margin-bottom:0.25rem;">
                  <span class="foundation-pill" style="font-size:0.69rem; font-weight:800; color:${stageCol}; border-color:${stageCol};">
                    ${escapeHtml(isEn ? ep.stageNameEn : ep.stageNamePl)}
                  </span>
                  <span class="foundation-pill" style="font-size:0.68rem; font-weight:700;">
                    DROGA #${ep.order}
                  </span>
                  <span style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">
                    ⏱️ ~${ep.estimatedDurationMin || 20} min
                  </span>
                  ${ep.tripProfile ? `<span class="foundation-pill" style="font-size:0.68rem; color:var(--text-secondary);">${escapeHtml(ep.tripProfile)}</span>` : ""}
                  ${isPlayingThis ? `<span class="badge-count" style="background:var(--success); color:#fff; animation:pulse 1.5s infinite;">🔊 ODTWARZANIE</span>` : ""}
                </div>
                <h3 style="font-size:1.08rem; font-weight:800; color:var(--text-primary); margin:0;">
                  ${escapeHtml(isEn ? ep.titleEn : ep.titlePl)}
                </h3>
              </div>

              <!-- Checkbox i przyciski akcji -->
              <div style="display:flex; align-items:center; gap:0.6rem;">
                <label style="display:inline-flex; align-items:center; gap:0.4rem; font-size:0.82rem; font-weight:700; color:${isDone ? "var(--success)" : "var(--text-secondary)"}; cursor:pointer; background:var(--bg-subtle); padding:0.35rem 0.65rem; border-radius:var(--radius-sm); border:1px solid var(--border-subtle);">
                  <input type="checkbox" ${isDone ? "checked" : ""} onchange="toggleCarAudioDone('${ep.id}')" style="width:16px; height:16px; accent-color:var(--success); cursor:pointer;" />
                  <span>${isDone ? (isEn ? "✓ Listened on road" : "✓ Odsłuchane w trasie") : (isEn ? "Mark as listened" : "Oznacz jako odsłuchane")}</span>
                </label>
                
                ${
                  isPlayingThis && isSpeaking
                    ? `<button class="btn btn-sm btn-primary" onclick="pauseCarAudio()">⏸️ ${isEn ? "Pause" : "Pauza"}</button>`
                    : `<button class="btn btn-sm btn-primary" onclick="playCarAudioEpisode('${ep.id}')">▶️ ${isEn ? "Listen (TTS)" : "Słuchaj lektorem AI"}</button>`
                }
              </div>
            </div>

            <!-- Tekst przemówienia lektora (odsłuchiwany w trasie) -->
            <div style="background:var(--bg-subtle); border-left:3px solid ${stageCol}; padding:0.75rem 0.95rem; border-radius:0 var(--radius-sm) var(--radius-sm) 0; font-size:0.85rem; color:var(--text-primary); line-height:1.62; margin:0.65rem 0;">
              ${escapeHtml(isEn && ep.spokenBriefingEn ? ep.spokenBriefingEn : ep.spokenBriefingPl)}
            </div>

            <!-- Kluczowe wnioski -->
            ${
              takeaways.length
                ? `
              <div style="margin:0.55rem 0 0.45rem;">
                <div style="font-size:0.72rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.25rem;">
                  📌 ${isEn ? "Key Takeaways to Memorize on Road:" : "Kluczowe wnioski do zapamiętania w drodze:"}
                </div>
                <ul style="margin:0; padding-left:1.2rem; font-size:0.8rem; color:var(--text-secondary); line-height:1.48;">
                  ${takeaways.map((t) => `<li>${escapeHtml(t)}</li>`).join("")}
                </ul>
              </div>
            `
                : ""
            }

            <!-- Zewnętrzne rekomendowane audycje, podcasty i audiobooki -->
            ${
              extLinks.length
                ? `
              <div style="display:flex; gap:0.4rem; flex-wrap:wrap; align-items:center; margin-top:0.6rem; padding-top:0.5rem; border-top:1px dashed var(--border-subtle);">
                <span style="font-size:0.73rem; color:var(--text-muted); font-weight:700;">🎙️ ${isEn ? "Curated Audio & Podcasts to Stream in Vehicle:" : "Rekomendowane podcasty, audycje i audiobooki do auta:"}</span>
                ${extLinks
                  .map(
                    (lnk) => `
                  <a href="${escapeHtml(lnk.url)}" target="_blank" rel="noopener noreferrer" class="alignment-badge" style="text-decoration:none; color:var(--link); border-color:var(--border-subtle); padding:0.22rem 0.55rem;">
                    ${renderLangBadgeHtml(lnk.lang || "PL")} <strong>[${escapeHtml(lnk.type || "podcast")}]</strong> ${escapeHtml(lnk.title)} ↗
                  </a>
                `
                  )
                  .join("")}
              </div>
            `
                : ""
            }
          </div>
        `;
        })
        .join("")}
    </div>
  `;
}
function renderBookView() {
  const root = document.getElementById("bookRootContainer");
  if (!root || !appState.data || !appState.data.summaBook) return;

  const isEn = appState.lang === "en";
  const book = appState.data.summaBook;
  const chapters = book.chapters || [];
  const activeCh = chapters.find((c) => c.id === appState.bookActiveChapterId) || chapters[0];

  const totalWords = chapters.reduce((acc, c) => acc + (c.contentMarkdownPl ? c.contentMarkdownPl.split(/\s+/).filter(Boolean).length : 0), 0);
  const isSpeaking = Boolean(bookSpeechUtterance);

  root.innerHTML = `
    <!-- NAGŁÓWEK MODUŁU KSIĄŻKOWEGO -->
    <div style="background:var(--bg-card); border:1px solid var(--border-color); border-top:4px solid var(--accent-purple); border-radius:var(--radius-md); padding:1.25rem 1.4rem; margin-bottom:1.25rem;">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.75rem;">
        <div>
          <span class="manhattan-codename-badge" style="background:rgba(168,85,247,0.12); color:var(--accent-purple); border-color:rgba(168,85,247,0.3);">
            📖 ${isEn ? "STANISŁAW LEM • SUMMA TECHNOLOGIAE 2.0" : "STANISŁAW LEM • SUMMA TECHNOLOGIAE 2.0"}
          </span>
          <h2 style="font-family:Georgia,'Times New Roman',serif; font-size:1.35rem; font-weight:800; color:var(--text-primary); margin:0.35rem 0 0.25rem;">
            ${escapeHtml(book.title)}
          </h2>
          <p style="font-size:0.86rem; color:var(--text-secondary); margin:0; line-height:1.5;">
            <em>"${escapeHtml(book.motto)}"</em> • <strong>${isEn ? "Authors:" : "Autorzy:"}</strong> ${escapeHtml(book.author)} & Golem XV • <strong>${chapters.length} ${isEn ? "chapters" : "rozdziałów"}</strong> (~${totalWords} ${isEn ? "words" : "słów"})
          </p>
        </div>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
          <button class="btn btn-sm" onclick="exportBookManuscript()">📥 ${isEn ? "Export Manuscript (.md)" : "Pobierz rękopis (.md)"}</button>
          <button class="btn btn-sm" onclick="window.print()">📄 ${isEn ? "Print / PDF" : "Drukuj / PDF"}</button>
        </div>
      </div>
    </div>

    <!-- DWUKOLUMNOWY UKŁAD: SPIS TREŚCI (TOC) + CZYTNIK I EDYTOR RĘKOPISU -->
    <div class="book-layout">
      <!-- LEWY PANEL: SPIS ROZDZIAŁÓW -->
      <div class="book-toc">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.65rem;">
          <h4 style="font-size:0.88rem; font-weight:800; color:var(--text-primary); margin:0; text-transform:uppercase; letter-spacing:0.04em;">
            📑 ${isEn ? "Table of Contents" : "Spis Rozdziałów"}
          </h4>
          <button class="btn btn-sm btn-primary" onclick="openNewBookChapterModal()" title="${isEn ? "Add new chapter" : "Dodaj nowy rozdział"}">
            ➕ ${isEn ? "Add Chapter" : "Nowy rozdział"}
          </button>
        </div>
        <div>
          ${chapters
            .map((ch) => {
              const isActive = ch.id === activeCh.id;
              const words = ch.contentMarkdownPl ? ch.contentMarkdownPl.split(/\s+/).filter(Boolean).length : 0;
              return `
              <div class="book-toc-item ${isActive ? "active" : ""}" onclick="selectBookChapter('${ch.id}')">
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.71rem; margin-bottom:0.15rem;">
                  <strong style="color:${isActive ? "var(--accent-purple)" : "var(--text-muted)"};">
                    ${ch.number === 0 ? "WSTĘP" : `ROZDZIAŁ ${ch.number}`}
                  </strong>
                  <span style="font-size:0.68rem; color:var(--text-muted);">~${ch.readingTimeMin} min</span>
                </div>
                <div style="font-size:0.82rem; font-weight:${isActive ? "700" : "500"}; color:var(--text-primary); line-height:1.35;">
                  ${escapeHtml(isEn ? ch.titleEn : ch.titlePl)}
                </div>
                <div style="display:flex; justify-content:space-between; font-size:0.68rem; color:var(--text-muted); margin-top:0.25rem;">
                  <span>${escapeHtml(ch.epistemicStatus || "W toku")}</span>
                  <span>${words} słów</span>
                </div>
              </div>
            `;
            })
            .join("")}
        </div>
      </div>

      <!-- PRAWY PANEL: CZYTNIK / EDYTOR RĘKOPISU -->
      <div class="book-manuscript-reader">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.6rem; margin-bottom:0.75rem;">
          <div>
            <div style="font-size:0.75rem; font-weight:800; color:var(--accent-purple); text-transform:uppercase; margin-bottom:0.2rem;">
              ${activeCh.number === 0 ? "WSTĘP EPISTEMOLOGICZNY" : `ROZDZIAŁ ${activeCh.number}`} • ${escapeHtml(activeCh.epistemicStatus)}
            </div>
            <h2 style="font-family:Georgia,'Times New Roman',serif; font-size:1.38rem; font-weight:800; color:var(--text-primary); margin:0;">
              ${escapeHtml(isEn ? activeCh.titleEn : activeCh.titlePl)}
            </h2>
            <div style="font-size:0.76rem; color:var(--text-muted); margin-top:0.2rem;">
              ⏱️ ~${activeCh.readingTimeMin} min lektury • 📅 Aktualizacja: ${activeCh.lastUpdated || "2026-10-26"}
            </div>
          </div>

          <!-- Przyciski trybu i syntezy -->
          <div style="display:flex; gap:0.35rem; align-items:center; flex-wrap:wrap;">
            ${
              appState.bookIsEditing
                ? `
                <button class="btn btn-sm btn-primary" onclick="saveBookChapterContent()">💾 ${isEn ? "Save Manuscript" : "Zapisz rękopis"}</button>
                <button class="btn btn-sm" onclick="toggleBookEditMode(false)">${isEn ? "Cancel" : "Anuluj"}</button>
              `
                : `
                <button class="btn btn-sm" onclick="toggleBookEditMode(true)">✏️ ${isEn ? "Edit Chapter" : "Edytuj treść"}</button>
              `
            }
            ${
              isSpeaking
                ? `<button class="btn btn-sm btn-danger" onclick="stopBookSpeech()">⏹️ ${isEn ? "Stop Audio" : "Zatrzymaj lektora"}</button>`
                : `<button class="btn btn-sm btn-primary" onclick="speakBookChapter('${activeCh.id}')">🔊 ${isEn ? "Read Chapter (TTS)" : "Odsłuchaj rozdział"}</button>`
            }
            <button class="btn btn-sm" onclick="openLemAiPromptModal('${activeCh.id}')">✨ ${isEn ? "Lem AI Prompt" : "Asystent Lema (AI)"}</button>
          </div>
        </div>

        <!-- MOTTO LEMOWSKIE ROZDZIAŁU -->
        <div class="book-lem-quote">
          „${escapeHtml(activeCh.lemQuote)}”
        </div>

        <!-- STRESZCZENIE IDEI -->
        <div style="background:var(--bg-subtle); border:1px solid var(--border-color); border-radius:var(--radius-sm); padding:0.8rem 1rem; margin-bottom:1.25rem;">
          <div style="font-size:0.74rem; font-weight:800; color:var(--accent-blue); text-transform:uppercase; margin-bottom:0.3rem;">
            💡 ${isEn ? "Epistemic Core & Conceptual Summary:" : "Rdzeń pojęciowy i synteza rozdziału:"}
          </div>
          <div style="font-size:0.85rem; color:var(--text-primary); line-height:1.6;">
            ${escapeHtml(isEn && activeCh.summaryEn ? activeCh.summaryEn : activeCh.summaryPl)}
          </div>
        </div>

        <!-- WŁAŚCIWA TREŚĆ RĘKOPISU -->
        ${
          appState.bookIsEditing
            ? `
          <div>
            <label style="display:block; font-size:0.78rem; font-weight:700; color:var(--text-secondary); margin-bottom:0.35rem;">
              ${isEn ? "Edit Markdown Manuscript for this chapter:" : "Edycja rękopisu rozdziału w formacie Markdown:"}
            </label>
            <textarea id="bookChapterEditor" class="input-field" rows="18" style="font-family:monospace; font-size:0.88rem; line-height:1.6; width:100%;">${escapeHtml(activeCh.contentMarkdownPl || "")}</textarea>
            <div style="display:flex; justify-content:flex-end; gap:0.5rem; margin-top:0.75rem;">
              <button class="btn" onclick="toggleBookEditMode(false)">${isEn ? "Cancel" : "Anuluj"}</button>
              <button class="btn btn-primary" onclick="saveBookChapterContent()">💾 ${isEn ? "Save Chapter Changes" : "Zapisz zmiany w rozdziale"}</button>
            </div>
          </div>
        `
            : `
          <div class="book-body-prose">
            ${
              activeCh.contentMarkdownPl
                ? activeCh.contentMarkdownPl
                    .split("\n\n")
                    .map((para) => {
                      const trimmed = para.trim();
                      if (!trimmed) return "";
                      if (trimmed.startsWith("### ")) {
                        return `<h3>${escapeHtml(trimmed.slice(4))}</h3>`;
                      } else if (trimmed.startsWith("## ")) {
                        return `<h2>${escapeHtml(trimmed.slice(3))}</h2>`;
                      } else if (trimmed.startsWith("> ")) {
                        return `<blockquote style="border-left:3px solid var(--accent-purple); padding-left:0.75rem; margin:0.75rem 0; font-style:italic;">${escapeHtml(trimmed.slice(2))}</blockquote>`;
                      } else if (trimmed.startsWith("- ")) {
                        const items = trimmed.split("\n- ").map(i => i.replace(/^- /, "")).filter(Boolean);
                        return `<ul>${items.map(it => `<li>${escapeHtml(it)}</li>`).join("")}</ul>`;
                      } else {
                        return `<p>${escapeHtml(trimmed)}</p>`;
                      }
                    })
                    .join("")
                : `<p style="color:var(--text-muted); font-style:italic;">${isEn ? "No text written yet. Click 'Edit Chapter' or use 'Lem AI Prompt' to generate initial manuscript." : "Rozdział oczekuje na rękopis. Kliknij 'Edytuj treść' lub użyj 'Asystent Lema (AI)', aby wygenerować pierwszy szkic."}</p>`
            }
          </div>
        `
        }
      </div>
    </div>
  `;
}


// ==============================================================================
// MODUŁ KSIĄŻKOWY: SUMMA TECHNOLOGIAE 2.0 (BIBLIA MOŻLIWOŚCI TECHNIKI)
// ==============================================================================
let bookSpeechUtterance = null;

function selectBookChapter(chId) {
  appState.bookActiveChapterId = chId;
  appState.bookIsEditing = false;
  stopBookSpeech();
  renderBookView();
}

function toggleBookEditMode(isEditing) {
  appState.bookIsEditing = Boolean(isEditing);
  renderBookView();
}

async function saveBookChapterContent() {
  const editor = document.getElementById("bookChapterEditor");
  if (!editor) return;
  const val = editor.value;
  const book = appState.data.summaBook;
  if (!book || !book.chapters) return;

  const activeCh = book.chapters.find((c) => c.id === appState.bookActiveChapterId) || book.chapters[0];
  if (!activeCh) return;

  activeCh.contentMarkdownPl = val;
  activeCh.lastUpdated = new Date().toISOString().split("T")[0];
  appState.bookIsEditing = false;

  await saveState();
  showNotification(appState.lang === "en" ? "Chapter manuscript saved successfully!" : "Rękopis rozdziału został pomyślnie zapisany!");
  renderBookView();
}

function exportBookManuscript() {
  const book = appState.data.summaBook;
  if (!book) return;
  const isEn = appState.lang === "en";
  let md = `# ${book.title}\n\n*${book.subtitle || ""}*\n\n**${isEn ? "Authors:" : "Autorzy:"}** ${book.author} & ${book.aiCoAuthor || "Golem XV"}\n\n*„${book.motto || ""}”*\n\n---\n\n`;
  for (const ch of book.chapters || []) {
    const chNum = ch.number === 0 ? (isEn ? "INTRODUCTION" : "WSTĘP") : `${isEn ? "CHAPTER" : "ROZDZIAŁ"} ${ch.number}`;
    md += `## ${chNum}: ${isEn && ch.titleEn ? ch.titleEn : ch.titlePl}\n\n`;
    if (ch.lemQuote) md += `> *„${ch.lemQuote}”* — Stanisław Lem\n\n`;
    if (ch.epistemicStatus) md += `**Status:** ${ch.epistemicStatus} • ⏱️ ~${ch.readingTimeMin || 15} min\n\n`;
    if (ch.summaryPl) md += `**${isEn ? "Epistemic Core:" : "Rdzeń pojęciowy:"}** ${isEn && ch.summaryEn ? ch.summaryEn : ch.summaryPl}\n\n`;
    md += `${ch.contentMarkdownPl || ""}\n\n---\n\n`;
  }
  const blob = new Blob([md], { type: "text/markdown;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `Summa_Technologiae_2_0_${book.author || "Ireneusz"}_${new Date().toISOString().split("T")[0]}.md`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

function speakBookChapter(chId) {
  if (!("speechSynthesis" in window)) {
    showNotification(appState.lang === "en" ? "Speech synthesis is not supported in this browser." : "Twoja przeglądarka nie obsługuje syntezy mowy (Web Speech API).");
    return;
  }
  stopBookSpeech();
  const book = appState.data.summaBook;
  if (!book) return;
  const ch = (book.chapters || []).find((c) => c.id === chId) || (book.chapters || [])[0];
  if (!ch) return;

  const title = ch.titlePl;
  const quote = ch.lemQuote ? "Motto Stanisława Lema: " + ch.lemQuote + ". " : "";
  const rawText = ch.contentMarkdownPl || ch.summaryPl || "";
  const cleanBody = rawText.replace(/[#*`_>-]/g, " ").replace(/\s+/g, " ");

  const fullSpoken = `${title}. ${quote} ${cleanBody}`;

  bookSpeechUtterance = new SpeechSynthesisUtterance(fullSpoken);
  bookSpeechUtterance.lang = appState.lang === "en" ? "en-US" : "pl-PL";
  bookSpeechUtterance.rate = 1.0;
  bookSpeechUtterance.pitch = 0.95;

  bookSpeechUtterance.onend = function() {
    bookSpeechUtterance = null;
    renderBookView();
  };
  bookSpeechUtterance.onerror = function() {
    bookSpeechUtterance = null;
    renderBookView();
  };

  window.speechSynthesis.speak(bookSpeechUtterance);
  renderBookView();
}

function stopBookSpeech() {
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
  bookSpeechUtterance = null;
  renderBookView();
}

function openLemAiPromptModal(chId) {
  const isEn = appState.lang === "en";
  const book = appState.data.summaBook;
  if (!book) return;
  const ch = (book.chapters || []).find((c) => c.id === chId) || (book.chapters || [])[0];
  if (!ch) return;

  const lemPrompt = `Jesteś Stanisławem Lemem oraz superinteligencją Golem XV. Piszemy wspólnie dzieło: „Summa Technologiae 2.0: Biblia Możliwości Techniki”.\n` +
`Rozdział: ${ch.number === 0 ? "Wstęp" : "Rozdział " + ch.number}. ${ch.titlePl}\n` +
`Motto przewodnie: "${ch.lemQuote}"\n\n` +
`Zadanie epistemiczne:\n` +
`Rozwiń ten rozdział w chłodnym, precyzyjnym, lemowskim stylu filozoficzno-technologicznym. Uwzględnij:\n` +
`1. Fizyczne granice krzemu (prawo Moore'a u kresu, prądy upływu, granica Landauera, koniec skalowania Dennarda).\n` +
`2. Zmianę paradygmatu programowania (od klasycznego kodu von Neumanna do obliczeń tensorowych, kwantowych QPU oraz neuromorficznych sieci impulsowych SNN).\n` +
`3. Maszyny naśladujące mózg biologiczny i protokół WBE (Whole Brain Emulation).\n` +
`4. Etyczne i cywilizacyjne konsekwencje dla ludzkości.\n\n` +
`Bieżący zarys rozdziału:\n` +
`${ch.summaryPl}\n\n` +
`Przygotuj głęboki esej stanowiący kolejną sekcję tego rozdziału.`;

  const modalHtml = `
    <div id="lemAiModal" class="modal-backdrop" onclick="if(event.target===this) this.remove();">
      <div class="modal-card" style="max-width:680px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
          <h3 style="margin:0; font-family:Georgia,serif; color:var(--text-primary);">
            ✨ ${isEn ? "Lem AI Co-Author Prompt" : "Asystent Lema — Gotowy Prompt do Współpracy z AI"}
          </h3>
          <button class="btn btn-sm" onclick="document.getElementById('lemAiModal').remove();">✕</button>
        </div>
        <p style="font-size:0.83rem; color:var(--text-secondary); margin-bottom:0.75rem;">
          ${isEn ? "Copy this prompt to chat with Antigravity / Golem XV to generate the next philosophical and technical section of your manuscript:" : "Skopiuj poniższy prompt do okna rozmowy ze mną (Antigravity / Golem XV), aby wspólnie napisać kolejną lemowską sekcję Twojego rękopisu:"}
        </p>
        <div style="position:relative; margin-bottom:1rem;">
          <textarea id="lemPromptText" class="input-field" rows="11" readonly style="font-family:monospace; font-size:0.82rem; line-height:1.5; width:100%; background:var(--bg-subtle);">${escapeHtml(lemPrompt)}</textarea>
        </div>
        <div style="display:flex; justify-content:flex-end; gap:0.5rem;">
          <button class="btn" onclick="document.getElementById('lemAiModal').remove();">${isEn ? "Close" : "Zamknij"}</button>
          <button class="btn btn-primary" onclick="copyLemPromptToClipboard()">📋 ${isEn ? "Copy Prompt to Clipboard" : "Skopiuj prompt do schowka"}</button>
        </div>
      </div>
    </div>
  `;
  const existing = document.getElementById("lemAiModal");
  if (existing) existing.remove();
  document.body.insertAdjacentHTML("beforeend", modalHtml);
}

function copyLemPromptToClipboard() {
  const ta = document.getElementById("lemPromptText");
  if (!ta) return;
  ta.select();
  navigator.clipboard.writeText(ta.value).then(() => {
    showNotification(appState.lang === "en" ? "Prompt copied to clipboard!" : "Skopiowano prompt do schowka! Wklej go do czatu.");
  }).catch(() => {
    document.execCommand("copy");
    showNotification(appState.lang === "en" ? "Prompt copied to clipboard!" : "Skopiowano prompt do schowka! Wklej go do czatu.");
  });
}

function openNewBookChapterModal() {
  const isEn = appState.lang === "en";
  const modalHtml = `
    <div id="newChapterModal" class="modal-backdrop" onclick="if(event.target===this) this.remove();">
      <div class="modal-card" style="max-width:600px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
          <h3 style="margin:0; font-family:Georgia,serif;">
            ➕ ${isEn ? "Add New Chapter to Summa Technologiae 2.0" : "Dodaj Nowy Rozdział do Summy Technologiae 2.0"}
          </h3>
          <button class="btn btn-sm" onclick="document.getElementById('newChapterModal').remove();">✕</button>
        </div>
        <form onsubmit="saveCustomBookChapter(event)">
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Chapter Title (PL)*" : "Tytuł Rozdziału (PL)*"}</label>
            <input type="text" id="custChTitlePl" class="input-field" required placeholder="np. Rozdział VIII: ..." />
          </div>
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Motto / Lem Quote*" : "Motto lub Cytat Przewodni*"}</label>
            <input type="text" id="custChQuote" class="input-field" required placeholder="Cytat Stanisława Lema lub sentencja..." />
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:0.75rem;">
            <div>
              <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Epistemic Status" : "Status Epistemiczny"}</label>
              <select id="custChStatus" class="select-field">
                <option value="🟢 Potwierdzona metoda badawcza">🟢 Potwierdzona metoda</option>
                <option value="🔵 Aktywne prace inżynieryjne" selected>🔵 Aktywne prace inżynieryjne</option>
                <option value="🟡 Hipoteza inżynieryjna">🟡 Hipoteza inżynieryjna</option>
                <option value="🟣 Spekulacja futurologiczna">🟣 Spekulacja futurologiczna</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Est. Reading Time (min)" : "Szacowany czas czytania (min)"}</label>
              <input type="number" id="custChReadTime" class="input-field" value="20" min="5" max="180" />
            </div>
          </div>
          <div style="margin-bottom:0.75rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Epistemic Core & Conceptual Summary*" : "Rdzeń pojęciowy i synteza idei*"}</label>
            <textarea id="custChSummary" class="input-field" rows="3" required placeholder="O czym traktuje ten rozdział, jakie granice technologii eksploruje..."></textarea>
          </div>
          <div style="margin-bottom:1rem;">
            <label style="display:block; font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">${isEn ? "Initial Manuscript Draft (Markdown, optional)" : "Początkowy szkic rękopisu (opcjonalnie)"}</label>
            <textarea id="custChContent" class="input-field" rows="4" placeholder="# Rozdział...&#10;&#10;Pierwsze akapity..."></textarea>
          </div>
          <div style="display:flex; justify-content:flex-end; gap:0.5rem;">
            <button type="button" class="btn" onclick="document.getElementById('newChapterModal').remove();">${isEn ? "Cancel" : "Anuluj"}</button>
            <button type="submit" class="btn btn-primary">💾 ${isEn ? "Save Chapter" : "Zapisz Rozdział"}</button>
          </div>
        </form>
      </div>
    </div>
  `;
  const existing = document.getElementById("newChapterModal");
  if (existing) existing.remove();
  document.body.insertAdjacentHTML("beforeend", modalHtml);
}

async function saveCustomBookChapter(e) {
  e.preventDefault();
  const book = appState.data.summaBook;
  if (!book) return;
  const num = (book.chapters || []).length;
  const id = `ch-custom-${Date.now().toString(36)}`;
  const title = document.getElementById("custChTitlePl").value.trim();
  const quote = document.getElementById("custChQuote").value.trim();
  const status = document.getElementById("custChStatus").value;
  const readTime = parseInt(document.getElementById("custChReadTime").value, 10) || 20;
  const summary = document.getElementById("custChSummary").value.trim();
  const content = document.getElementById("custChContent").value.trim() || `# ${title}\n\n> *„${quote}”*\n\n${summary}`;

  const newCh = {
    id: id,
    number: num,
    titlePl: title,
    titleEn: title,
    lemQuote: quote,
    epistemicStatus: status,
    readingTimeMin: readTime,
    lastUpdated: new Date().toISOString().split("T")[0],
    summaryPl: summary,
    summaryEn: summary,
    contentMarkdownPl: content,
    contentMarkdownEn: content
  };

  book.chapters.push(newCh);
  appState.bookActiveChapterId = id;
  const modal = document.getElementById("newChapterModal");
  if (modal) modal.remove();

  await saveState();
  showNotification(appState.lang === "en" ? "New chapter added to Summa Technologiae 2.0!" : "Dodano nowy rozdział do Summy Technologiae 2.0!");
  renderBookView();
}

window.addEventListener("DOMContentLoaded", initApp);
