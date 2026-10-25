// The Golem 15: A Human's Road to Reality
// Główny moduł aplikacji (obsługa API serwera + automatyczny fallback localStorage)

const DEFAULT_SEED = {
  "projectMeta": {
    "title": "The Golem 15: A Human's Road to Reality",
    "subtitle": "Mapa projektu badawczego — wspólne podstawy naukowe oraz siedem powiązanych ścieżek (A–G)",
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
        "G"
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
        "G"
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
        "G"
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
        "G"
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
        "G"
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
        "G"
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
        "G"
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
        "G"
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
    }
  ],
  "materials": [
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
      "author": "Dr Janina Kowalska (Gość)",
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
      "status": "pending",
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
    }
  ]
};

const STORAGE_KEY = "the_golem_15_state_v5";
const ADMIN_PASS_KEY = "golem_xv_admin_pass";

const appState = {
  data: null,
  isAdmin: false,
  serverOnline: false,
  activeTab: "study", // Domyślnie pierwsza zakładka: 'study' (Materiały do nauki)
  selectedTrackFilter: "ALL",
  selectedSubprojectId: "sub-1",
  materialFilterTrack: "ALL",
  materialSearch: "",
  selectedGraphNode: null
};

function ensureSchema(d) {
  if (!d.projectMeta) d.projectMeta = JSON.parse(JSON.stringify(DEFAULT_SEED.projectMeta));
  d.projectMeta.title = "The Golem 15: A Human's Road to Reality";
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
  d.supplementaryLibrary = JSON.parse(JSON.stringify(DEFAULT_SEED.supplementaryLibrary));
  return d;
}

async function initApp() {
  if (sessionStorage.getItem("golem_xv_is_admin") === "true") {
    appState.isAdmin = true;
  }
  await loadState();
  renderAll();
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
  if (appState.serverOnline) {
    el.innerHTML = `<span class="status-dot" style="background:#10b981"></span> Baza serwerowa (JSON API aktywne)`;
  } else {
    el.innerHTML = `<span class="status-dot" style="background:#38bdf8"></span> Baza lokalna przeglądarki`;
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
  if (links.length > 0) {
    return `
      <div style="margin-top:0.45rem; padding-top:0.35rem; border-top:1px dashed rgba(148,163,184,0.2);">
        <div style="font-size:0.75rem; font-weight:700; color:#38bdf8; margin-bottom:0.2rem;">🔗 Odnośniki i linki źródłowe:</div>
        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.2rem;">
          ${links
            .map(
              (l) =>
                `<li style="font-size:0.8rem;"><a href="${escapeHtml(l.url)}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; text-decoration:underline;">🔗 ${escapeHtml(l.label)}</a></li>`
            )
            .join("")}
        </ul>
      </div>
    `;
  }
  if (item.url) {
    return `
      <div style="margin-top:0.4rem;">
        <a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-size:0.82rem; font-weight:600; text-decoration:underline;">🔗 Otwórz materiał / źródło zewnętrzne</a>
      </div>
    `;
  }
  return "";
}

function getTrackOrFoundationById(id) {
  const tr = appState.data.tracks.find((t) => t.id === id);
  if (tr) return tr;
  const fnd = (appState.data.foundationDisciplines || []).find((f) => f.id === id);
  if (fnd) {
    return {
      id: fnd.id,
      code: `Podstawy ${fnd.order}`,
      name: fnd.name,
      color: fnd.color,
      sections: [{ title: "Działy do nauki", items: fnd.topics }]
    };
  }
  return { id, code: id, name: id, color: "#38bdf8", sections: [] };
}

function countPendingItems() {
  if (!appState.data) return 0;
  let count = 0;
  (appState.data.studyMaterials || []).forEach((sm) => {
    if (sm.status === "pending") count++;
  });
  appState.data.materials.forEach((m) => {
    if (m.status === "pending") count++;
  });
  appState.data.subprojects.forEach((sp) => {
    if (sp.status === "pending") count++;
    if (sp.workspace) {
      (sp.workspace.hypotheses || []).forEach((h) => {
        if (h.approvalStatus === "pending") count++;
      });
      (sp.workspace.notes || []).forEach((n) => {
        if (n.approvalStatus === "pending") count++;
      });
      (sp.workspace.bibliography || []).forEach((b) => {
        if (b.approvalStatus === "pending") count++;
      });
    }
  });
  (appState.data.graphLinks || []).forEach((l) => {
    if (l.status === "pending") count++;
  });
  return count;
}

function switchTab(tabName) {
  appState.activeTab = tabName;
  renderAll();
}

function openTrackWorkspaceFilter(trackId) {
  appState.selectedTrackFilter = trackId;
  const matching = appState.data.subprojects.find(
    (s) => (s.status === "approved" || appState.isAdmin) && s.trackId === trackId
  );
  if (matching) {
    appState.selectedSubprojectId = matching.id;
  }
  switchTab("workspaces");
}

function renderAll() {
  if (!appState.data) return;
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
  const authBtn = document.getElementById("authToggleBtn");
  if (appState.isAdmin) {
    roleBadge.className = "role-badge admin";
    roleBadge.innerHTML = `<span>★</span> Tryb Administratora (Pełna kontrola)`;
    authBtn.textContent = "Wyloguj do trybu Gościa";
    authBtn.className = "btn btn-sm";
  } else {
    roleBadge.className = "role-badge guest";
    roleBadge.innerHTML = `<span>👁</span> Tryb Gościa / Obserwatora`;
    authBtn.textContent = "Zaloguj jako Administrator";
    authBtn.className = "btn btn-sm btn-primary";
  }
}

function renderNavCounts() {
  const approvedStudy = (appState.data.studyMaterials || []).filter(
    (s) => s.status === "approved" || appState.isAdmin
  ).length;
  const approvedSubprojects = appState.data.subprojects.filter(
    (s) => s.status === "approved" || appState.isAdmin
  ).length;
  const approvedMaterials = appState.data.materials.filter(
    (m) => m.status === "approved" || appState.isAdmin
  ).length;
  const pendingTotal = countPendingItems();

  const studyCountEl = document.getElementById("navStudyCount");
  const subCountEl = document.getElementById("navSubprojectsCount");
  const matCountEl = document.getElementById("navMaterialsCount");
  const modCountEl = document.getElementById("navModerationCount");

  if (studyCountEl) studyCountEl.textContent = approvedStudy;
  if (subCountEl) subCountEl.textContent = approvedSubprojects;
  if (matCountEl) matCountEl.textContent = approvedMaterials;
  if (modCountEl) {
    modCountEl.textContent = pendingTotal;
    modCountEl.className = pendingTotal > 0 ? "badge-count pending-alert" : "badge-count";
  }
}

// --- WIDOK 0 (PIERWSZA OPCJA): MATERIAŁY DO NAUKI (8 DZIEDZIN PODSTAWOWYCH PO KOLEI + ODNOGI A-G + BIBLIOTEKA UZUPEŁNIAJĄCA) ---
function renderStudyView() {
  const fndGrid = document.getElementById("foundationsGrid");
  const tracksTree = document.getElementById("tracksStudyTree");
  if (!fndGrid) return;

  const foundations = (appState.data.foundationDisciplines || []).slice().sort((a, b) => a.order - b.order);

  fndGrid.innerHTML = foundations
    .map((fnd) => {
      const mats = (appState.data.studyMaterials || []).filter(
        (sm) =>
          sm.categoryType === "FOUNDATION" &&
          sm.targetId === fnd.id &&
          (sm.status === "approved" || appState.isAdmin || sm.isSessionCreated)
      );
      const subCount = appState.data.subprojects.filter(
        (s) => s.trackId === fnd.id && (s.status === "approved" || appState.isAdmin)
      ).length;

      return `
      <div class="track-card" style="--track-color: ${fnd.color}">
        <div>
          <div class="track-header">
            <div>
              <span class="track-code">WSPÓLNE PODSTAWY • DZIEDZINA ${fnd.order} z 8</span>
              <h3 class="track-title">${fnd.icon} ${escapeHtml(fnd.name)}</h3>
            </div>
            <button class="btn btn-sm btn-primary" onclick="openNewStudyMaterialModal('FOUNDATION', '${fnd.id}', '')">
              + Materiał do nauki
            </button>
          </div>
          <p class="track-goal">${escapeHtml(fnd.description)}</p>

          <div class="track-sections">
            <div class="track-section-block">
              <h4>Program nauki po kolei (zagadnienia i działy)</h4>
              <ul class="branch-list">
                ${fnd.topics
                  .map(
                    (topic, idx) => `
                  <li class="branch-item">
                    <span><strong>${fnd.order}.${idx + 1}.</strong> ${escapeHtml(topic)}</span>
                    <div style="display:flex; gap:0.35rem;">
                      <button class="btn btn-sm branch-launch-btn" onclick="openNewStudyMaterialModal('FOUNDATION', '${fnd.id}', '${escapeHtml(topic).replace(/'/g, "\\'")}')" title="Dodaj materiał do nauki dla tego działu">
                        + Materiał
                      </button>
                      <button class="btn btn-sm branch-launch-btn" onclick="openNewSubprojectModal('${fnd.id}', '${escapeHtml(topic).replace(/'/g, "\\'")}')" title="Uruchom środowisko dla tego działu">
                        🚀 Środowisko
                      </button>
                    </div>
                  </li>
                `
                  )
                  .join("")}
              </ul>
            </div>

            <div class="track-section-block">
              <h4>Przypisane materiały do nauki (${mats.length})</h4>
              ${
                mats.length === 0
                  ? `<p style="font-size:0.8rem; color:var(--text-muted);">Brak przypisanych materiałów. Kliknij „+ Materiał do nauki”, aby dodać podręcznik, kurs lub notatkę.</p>`
                  : mats
                      .map(
                        (m) => `
                    <div class="ws-card" style="margin-bottom:0.45rem;">
                      <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.2rem;">
                        <span class="foundation-pill" style="font-size:0.7rem;">${escapeHtml(m.format)} • ${escapeHtml(m.level)}</span>
                        ${
                          m.status === "pending"
                            ? `<span class="status-tag status-pending">Do akceptacji Admina</span>`
                            : `<span class="status-tag status-approved">Zatwierdzony</span>`
                        }
                      </div>
                      <strong style="font-size:0.9rem;">📖 ${escapeHtml(m.title)}</strong>
                      <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:0.25rem;">Dział: ${escapeHtml(m.topic)}</div>
                      <p style="font-size:0.82rem; color:var(--text-secondary);">${formatTextWithLinks(m.content)}</p>
                      ${renderLinksBlock(m)}
                      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.35rem; font-size:0.74rem; color:var(--text-muted);">
                        <span>Dodał(a): ${escapeHtml(m.author)}</span>
                        ${
                          appState.isAdmin
                            ? `<div style="display:flex; gap:0.3rem;">
                                ${
                                  m.status === "pending"
                                    ? `<button class="btn btn-sm btn-success" onclick="moderateItem('studyMaterial', '${m.id}', 'approve')">✓</button>`
                                    : ""
                                }
                                <button class="btn btn-sm btn-danger" onclick="moderateItem('studyMaterial', '${m.id}', 'delete')">✕</button>
                              </div>`
                            : ""
                        }
                      </div>
                    </div>
                  `
                      )
                      .join("")
              }
            </div>
          </div>
        </div>

        <div class="track-footer">
          <div class="track-stats">
            <span>📖 Materiały do nauki: <strong>${mats.length}</strong></span>
            <span>🔬 Środowiska: <strong>${subCount}</strong></span>
          </div>
          <button class="btn btn-sm" onclick="openNewSubprojectModal('${fnd.id}', '')">
            🚀 Nowe środowisko (${escapeHtml(fnd.name)})
          </button>
        </div>
      </div>
    `;
    })
    .join("");

  if (tracksTree) {
    const suppLib = appState.data.supplementaryLibrary || {};
    const suppProjects = suppLib.projects || [];
    const suppRules = suppLib.rules || suppLib.usageRules || [];

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
          ${
            readingOrder.principle
              ? `<div style="font-size:0.82rem; color:#e2e8f0; background:rgba(56,189,248,0.1); padding:0.45rem 0.65rem; border-radius:6px;">
                  <strong>Zasada:</strong> ${escapeHtml(readingOrder.principle)}
                </div>`
              : ""
          }
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
          <h4 style="margin-bottom:0.45rem; color:#38bdf8;">📌 Zasady korzystania z biblioteki (1–6)</h4>
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
          const mats = (appState.data.studyMaterials || []).filter(
            (sm) =>
              sm.categoryType === "TRACK" &&
              sm.targetId === tr.id &&
              (sm.status === "approved" || appState.isAdmin || sm.isSessionCreated)
          );
          const suppProj = suppProjects.find((sp) => sp.trackId === tr.id);

          return `
        <div class="track-card" style="--track-color: ${tr.color}">
          <div>
            <div class="track-header">
              <div>
                <span class="track-code">${escapeHtml(tr.code)} • MATERIAŁY DO NAUKI</span>
                <h3 class="track-title">${escapeHtml(tr.name)}</h3>
              </div>
              <button class="btn btn-sm btn-primary" onclick="openNewStudyMaterialModal('TRACK', '${tr.id}', '')">
                + Materiał do nauki
              </button>
            </div>
            <div class="track-sections">
              ${
                suppProj
                  ? `
                <div class="track-section-block" style="border: 1px solid rgba(56, 189, 248, 0.35); background: rgba(15, 23, 42, 0.78);">
                  <h4 style="color:#38bdf8;">📚 Biblioteka uzupełniająca — ${escapeHtml(suppProj.title)}</h4>
                  ${
                    suppProj.sequence
                      ? `<div style="margin:0.4rem 0 0.65rem; padding:0.45rem 0.65rem; border-radius:8px; background:rgba(16,185,129,0.12); border-left:3px solid #10b981; font-size:0.82rem;">
                          <strong>🧭 ${escapeHtml(suppProj.sequenceLabel || "Kolejność nauki")}:</strong> ${escapeHtml(suppProj.sequence)}
                        </div>`
                      : ""
                  }
                  ${(suppProj.groups || suppProj.sections || [])
                    .map(
                      (ssec) => `
                    <div style="margin-top:0.45rem;">
                      <strong style="font-size:0.78rem; text-transform:uppercase; color:var(--text-secondary);">${escapeHtml(ssec.heading)}:</strong>
                      <ul class="branch-list" style="margin-top:0.25rem;">
                        ${(ssec.items || [])
                          .map(
                            (it) => `
                          <li class="branch-item" style="font-size:0.82rem;">
                            <span>• ${formatTextWithLinks(it)}</span>
                          </li>
                        `
                          )
                          .join("")}
                      </ul>
                    </div>
                  `
                    )
                    .join("")}
                  ${renderLinksBlock(suppProj)}
                </div>
              `
                  : ""
              }
              ${tr.sections
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
                        <button class="btn btn-sm branch-launch-btn" onclick="openNewStudyMaterialModal('TRACK', '${tr.id}', '${escapeHtml(item).replace(/'/g, "\\'")}')">
                          + Materiał do nauki
                        </button>
                      </li>
                    `
                      )
                      .join("")}
                  </ul>
                </div>
              `
                )
                .join("")}
              ${
                mats.length > 0
                  ? `<div class="track-section-block">
                      <h4>Dodane materiały do nauki (${mats.length})</h4>
                      ${mats
                        .map(
                          (m) => `
                        <div class="ws-card" style="margin-bottom:0.4rem;">
                          <strong>📖 ${escapeHtml(m.title)}</strong> (${escapeHtml(m.level)})
                          <div style="font-size:0.75rem; color:var(--text-muted);">Odnoga: ${escapeHtml(m.topic)}</div>
                          <p style="font-size:0.82rem; color:var(--text-secondary);">${formatTextWithLinks(m.content)}</p>
                          ${renderLinksBlock(m)}
                        </div>
                      `
                        )
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
  const bannerEl = document.getElementById("overviewBanner");
  bannerEl.innerHTML = `
    <div class="overarching-goal">
      <h2>Cel nadrzędny przedsięwzięcia</h2>
      <p><strong>${escapeHtml(meta.overarchingGoal)}</strong></p>
      <p style="font-size:0.86rem; color:var(--text-muted)">${escapeHtml(meta.organizationalRule)}</p>
      <div style="margin-top:0.85rem;">
        <span style="font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--text-muted); font-weight:700;">Wspólne podstawy naukowe (kliknij zakładkę „1. Materiały do nauki”, aby studiować po kolei):</span>
        <div class="foundations-list">
          ${meta.foundations.map((f) => `<span class="foundation-pill" style="cursor:pointer;" onclick="switchTab('study')">${escapeHtml(f)}</span>`).join("")}
        </div>
      </div>
    </div>
    <div class="fg-relation-box">
      <h3>Relacja między projektami F i G (Kosmos ↔ Ziemia)</h3>
      <p>${escapeHtml(meta.fgRelation.summary)}</p>
      <p>• <strong>Kosmos (F):</strong> ${escapeHtml(meta.fgRelation.fPerspective)}</p>
      <p>• <strong>Ziemia (G):</strong> ${escapeHtml(meta.fgRelation.gPerspective)}</p>
    </div>
  `;

  const gridEl = document.getElementById("tracksGrid");
  gridEl.innerHTML = appState.data.tracks
    .map((track) => {
      const subCount = appState.data.subprojects.filter(
        (s) => s.trackId === track.id && (s.status === "approved" || appState.isAdmin)
      ).length;
      const matCount = appState.data.materials.filter(
        (m) => m.trackId === track.id && (m.status === "approved" || appState.isAdmin)
      ).length;
      const isCrossCutting = track.id === "E";

      return `
      <div class="track-card ${isCrossCutting ? "cross-cutting" : ""}" style="--track-color: ${track.color}">
        <div>
          <div class="track-header">
            <div>
              <span class="track-code">${escapeHtml(track.code)}${isCrossCutting ? " • WARSTWA PRZEKROJOWA" : ""}</span>
              <h3 class="track-title">${escapeHtml(track.name)}</h3>
            </div>
            <button class="btn btn-sm" onclick="openNewSubprojectModal('${track.id}', '')">
              + Podprojekt / Środowisko
            </button>
          </div>
          <p class="track-goal"><strong>Cel:</strong> ${escapeHtml(track.goal)}</p>
          <div class="guiding-question">
            <strong>Pytanie przewodnie:</strong> ${escapeHtml(track.guidingQuestion)}
          </div>
          ${track.note ? `<div class="track-note">ℹ️ ${escapeHtml(track.note)}</div>` : ""}
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
                          🚀 Środowisko
                        </button>
                        <button class="btn btn-sm branch-launch-btn" onclick="openNewMaterialModal('${track.id}', '${escapeHtml(item).replace(/'/g, "\\'")}')">
                          + Materiał
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
            <span>🔬 Środowiska: <strong>${subCount}</strong></span>
            <span>📚 Materiały: <strong>${matCount}</strong></span>
          </div>
          <div style="display:flex; gap:0.45rem;">
            <button class="btn btn-sm" onclick="openTrackWorkspaceFilter('${track.id}')">Otwórz środowiska (${subCount})</button>
            <button class="btn btn-sm" onclick="openNewMaterialModal('${track.id}', '')">+ Dodaj materiał</button>
          </div>
        </div>
      </div>
    `;
    })
    .join("");
}

// --- WIDOK 2: ŚRODOWISKA BADAWCZE I PODPROJEKTY ---
function renderWorkspacesView() {
  const filterSelect = document.getElementById("wsTrackFilter");
  if (filterSelect) {
    filterSelect.value = appState.selectedTrackFilter;
  }

  const visibleSubprojects = appState.data.subprojects.filter((sp) => {
    const statusOk = sp.status === "approved" || appState.isAdmin || sp.isSessionCreated;
    const trackOk =
      appState.selectedTrackFilter === "ALL" ||
      sp.trackId === appState.selectedTrackFilter ||
      (sp.secondaryTracks && sp.secondaryTracks.includes(appState.selectedTrackFilter));
    return statusOk && trackOk;
  });

  if (
    visibleSubprojects.length > 0 &&
    !visibleSubprojects.some((s) => s.id === appState.selectedSubprojectId)
  ) {
    appState.selectedSubprojectId = visibleSubprojects[0].id;
  }

  const listEl = document.getElementById("subprojectsList");
  if (visibleSubprojects.length === 0) {
    listEl.innerHTML = `<p style="color:var(--text-muted); font-size:0.86rem;">Brak podprojektów dla wybranego filtru.</p>`;
  } else {
    listEl.innerHTML = visibleSubprojects
      .map((sp) => {
        const track = getTrackOrFoundationById(sp.trackId);
        const activeClass = sp.id === appState.selectedSubprojectId ? "active" : "";
        const statusBadge =
          sp.status === "pending"
            ? `<span class="status-tag status-pending">Do akceptacji</span>`
            : `<span class="status-tag status-approved">Aktywne</span>`;
        return `
        <div class="subproject-item ${activeClass}" onclick="selectSubproject('${sp.id}')">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.3rem;">
            <span style="font-size:0.74rem; font-weight:700; color:${track.color};">${escapeHtml(track.code)} — ${escapeHtml(track.name)}</span>
            ${statusBadge}
          </div>
          <div style="font-weight:600; font-size:0.92rem; margin-bottom:0.25rem;">${escapeHtml(sp.title)}</div>
          <div style="font-size:0.78rem; color:var(--text-muted);">Odnoga: ${escapeHtml(sp.branchTopic || "Ogólna")}</div>
        </div>
      `;
      })
      .join("");
  }

  const activeSp = appState.data.subprojects.find((s) => s.id === appState.selectedSubprojectId);
  const panelEl = document.getElementById("activeWorkspacePanel");
  if (!activeSp) {
    panelEl.innerHTML = `
      <div style="text-align:center; padding:3rem 1rem; color:var(--text-muted);">
        <h3>Wybierz podprojekt z listy po lewej stronie lub uruchom nowe środowisko badawcze</h3>
        <button class="btn btn-primary" style="margin-top:1rem;" onclick="openNewSubprojectModal('A', '')">+ Uruchom nowe środowisko badawcze</button>
      </div>
    `;
    return;
  }

  const primaryTrack = getTrackOrFoundationById(activeSp.trackId);
  const ws = activeSp.workspace || { hypotheses: [], notes: [], bibliography: [] };
  const hypotheses = (ws.hypotheses || []).filter(
    (h) => h.approvalStatus !== "pending" || appState.isAdmin || h.isSessionCreated
  );
  const notes = (ws.notes || []).filter(
    (n) => n.approvalStatus !== "pending" || appState.isAdmin || n.isSessionCreated
  );
  const bibliography = (ws.bibliography || []).filter(
    (b) => b.approvalStatus !== "pending" || appState.isAdmin || b.isSessionCreated
  );

  panelEl.innerHTML = `
    <div style="border-bottom:1px solid var(--border-color); padding-bottom:1.1rem;">
      <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-start; gap:0.75rem;">
        <div>
          <span class="track-code" style="color:${primaryTrack.color};">${escapeHtml(primaryTrack.code)} — ${escapeHtml(primaryTrack.name)}</span>
          <h2 style="font-size:1.35rem; margin-bottom:0.3rem;">${escapeHtml(activeSp.title)}</h2>
          <p style="font-size:0.84rem; color:var(--text-muted);">
            <strong>Odnoga badawcza:</strong> ${escapeHtml(activeSp.branchTopic || "Ogólna")} •
            <strong>Inicjator:</strong> ${escapeHtml(activeSp.author)}
          </p>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          ${
            appState.isAdmin && activeSp.status === "pending"
              ? `<button class="btn btn-sm btn-success" onclick="moderateItem('subproject', '${activeSp.id}', 'approve')">✓ Zatwierdź podprojekt</button>`
              : ""
          }
          ${
            appState.isAdmin
              ? `<button class="btn btn-sm btn-danger" onclick="moderateItem('subproject', '${activeSp.id}', 'delete')">Usuń</button>`
              : ""
          }
        </div>
      </div>
      <p style="margin-top:0.75rem; color:var(--text-secondary); font-size:0.92rem;">${escapeHtml(activeSp.description)}</p>
      ${
        activeSp.philosophicalNote
          ? `<div class="track-note" style="margin-top:0.75rem; margin-bottom:0;">
              <strong>Nakładka interpretacyjna (Projekt E — Filozofia):</strong> ${escapeHtml(activeSp.philosophicalNote)}
            </div>`
          : ""
      }
    </div>

    <div class="workspace-grid">
      <div class="ws-section">
        <h4>
          <span>1. Hipotezy badawcze (${hypotheses.length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('hypothesis', '${activeSp.id}')">+ Hipoteza</button>
        </h4>
        ${hypotheses
          .map(
            (h) => `
          <div class="ws-card">
            <span class="foundation-pill" style="font-size:0.7rem;">${escapeHtml(h.status || "Hipoteza otwarta")}</span>
            <p style="margin:0.4rem 0;">${escapeHtml(h.statement)}</p>
            <div style="font-size:0.75rem; color:var(--text-muted);">Autor: ${escapeHtml(h.author)}</div>
          </div>
        `
          )
          .join("")}
      </div>

      <div class="ws-section">
        <h4>
          <span>2. Notatnik badawczy (${notes.length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('note', '${activeSp.id}')">+ Notatka</button>
        </h4>
        ${notes
          .map(
            (n) => `
          <div class="ws-card">
            <strong>${escapeHtml(n.title)}</strong>
            <p style="color:var(--text-secondary); margin:0.35rem 0;">${escapeHtml(n.content)}</p>
            <div style="font-size:0.75rem; color:var(--text-muted);">Autor: ${escapeHtml(n.author)}</div>
          </div>
        `
          )
          .join("")}
      </div>

      <div class="ws-section">
        <h4>
          <span>3. Bibliografia i źródła (${bibliography.length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('bibliography', '${activeSp.id}')">+ Źródło</button>
        </h4>
        ${bibliography
          .map(
            (b) => `
          <div class="ws-card">
            <p>📖 ${escapeHtml(b.citation)}</p>
            <div style="font-size:0.75rem; color:var(--text-muted); margin-top:0.3rem;">Dodał(a): ${escapeHtml(b.addedBy)}</div>
          </div>
        `
          )
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
    const visible = m.status === "approved" || appState.isAdmin || m.isSessionCreated;
    if (!visible) return false;
    if (trackFilter !== "ALL" && m.trackId !== trackFilter) return false;
    if (searchVal) {
      const hay = `${m.title} ${m.content} ${m.author} ${m.branchTopic || ""}`.toLowerCase();
      if (!hay.includes(searchVal)) return false;
    }
    return true;
  });

  if (filtered.length === 0) {
    listEl.innerHTML = `<div class="ws-card" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak materiałów spełniających kryteria.</div>`;
    return;
  }

  listEl.innerHTML = filtered
    .map((m) => {
      const track = getTrackOrFoundationById(m.trackId);
      return `
      <div class="ws-card" style="padding:1.15rem; border-left:4px solid ${track.color};">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.45rem;">
          <span class="track-code" style="color:${track.color}; margin:0;">${escapeHtml(track.code)}: ${escapeHtml(track.name)} • ${escapeHtml(m.type || "Materiał")}</span>
          ${
            m.status === "pending"
              ? `<span class="status-tag status-pending">Oczekuje na zgodę Administratora</span>`
              : `<span class="status-tag status-approved">Zatwierdzony</span>`
          }
        </div>
        <h3 style="font-size:1.08rem; margin-bottom:0.35rem;">${escapeHtml(m.title)}</h3>
        <p style="color:var(--text-secondary); margin-bottom:0.65rem; white-space:pre-line;">${formatTextWithLinks(m.content)}</p>
        ${renderLinksBlock(m)}
        <div style="font-size:0.8rem; color:var(--text-muted); margin-top:0.5rem;">Autor zgłoszenia: <strong>${escapeHtml(m.author)}</strong></div>
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
    E: { x: 450, y: 265 },
    A: { x: 210, y: 110 },
    B: { x: 450, y: 75 },
    C: { x: 690, y: 110 },
    D: { x: 210, y: 420 },
    F: { x: 450, y: 455 },
    G: { x: 690, y: 420 }
  };

  const visibleLinks = (appState.data.graphLinks || []).filter(
    (l) => l.status !== "pending" || appState.isAdmin || l.isSessionCreated
  );

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
      const c = coords[tr.id] || { x: 100, y: 100 };
      const r = tr.id === "E" ? 44 : 36;
      return `
      <g style="cursor:pointer;" onclick="selectGraphNode('${tr.id}')">
        <circle cx="${c.x}" cy="${c.y}" r="${r}" fill="#111827" stroke="${tr.color}" stroke-width="3" />
        <text x="${c.x}" y="${c.y + 4}" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="700">${escapeHtml(tr.code)}</text>
        <text x="${c.x}" y="${c.y + r + 18}" text-anchor="middle" fill="#e2e8f0" font-size="11.5" font-weight="600">${escapeHtml(tr.name)}</text>
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

// --- WIDOK 5: CENTRUM AUTORYZACJI ADMINISTRATORA (MODERACJA) ---
function renderModerationView() {
  const container = document.getElementById("moderationContainer");
  if (!container) return;

  if (!appState.isAdmin) {
    container.innerHTML = `
      <div class="ws-card" style="max-width:560px; margin:2rem auto; padding:2rem;">
        <h3 style="margin-bottom:0.5rem;">🔐 Logowanie do Panelu Administratora</h3>
        <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:1rem;">
          Twoje domyślne hasło administratora to: <strong><code>golem15</code></strong> (jest już wpisane poniżej — wystarczy kliknąć przycisk logowania, a po zalogowaniu możesz ustawić własne hasło).
        </p>
        <form onsubmit="submitInlineAdminLogin(event)">
          <div class="form-group">
            <label>Login Administratora</label>
            <input type="text" class="input-field" value="Administrator (Ireneusz)" />
          </div>
          <div class="form-group">
            <label>Hasło Administratora</label>
            <input type="password" id="inlineAdminPass" class="input-field" value="golem15" required />
          </div>
          <button type="submit" class="btn btn-primary" style="width:100%;">🔐 Zaloguj jako Administrator</button>
        </form>
      </div>
    `;
    return;
  }

  const pendingStudy = (appState.data.studyMaterials || []).filter((s) => s.status === "pending");
  const pendingSubprojects = appState.data.subprojects.filter((s) => s.status === "pending");
  const pendingMaterials = appState.data.materials.filter((m) => m.status === "pending");
  const totalPending = countPendingItems();

  container.innerHTML = `
    <div class="filter-bar">
      <div>
        <h3 style="font-size:1.1rem;">Kolejka autoryzacji zgłoszeń gości (${totalPending})</h3>
      </div>
      <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
        ${
          totalPending > 0
            ? `<button class="btn btn-success" onclick="approveAllPending()">✓ Zatwierdź wszystkie oczekujące (${totalPending})</button>`
            : ""
        }
        <button class="btn" onclick="openChangeAdminPassModal()">🔑 Zmień hasło Administratora</button>
        <button class="btn" onclick="exportDatabaseJson()">⬇ Eksportuj bazę JSON</button>
      </div>
    </div>
    <div class="workspace-grid">

      <div class="ws-section">
        <h4>Materiały do nauki (${pendingStudy.length})</h4>
        ${pendingStudy
          .map(
            (sm) => `
          <div class="ws-card">
            <strong>${escapeHtml(sm.title)}</strong>
            <p style="font-size:0.82rem; color:var(--text-secondary); margin:0.3rem 0;">${escapeHtml(sm.content)}</p>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.75rem;">Autor: ${escapeHtml(sm.author)}</span>
              <div style="display:flex; gap:0.35rem;">
                <button class="btn btn-sm btn-success" onclick="moderateItem('studyMaterial', '${sm.id}', 'approve')">✓ Zatwierdź</button>
                <button class="btn btn-sm btn-danger" onclick="moderateItem('studyMaterial', '${sm.id}', 'delete')">✕ Odrzuć</button>
              </div>
            </div>
          </div>
        `
          )
          .join("")}
      </div>
      <div class="ws-section">
        <h4>Podprojekty i środowiska (${pendingSubprojects.length})</h4>
        ${pendingSubprojects
          .map(
            (sp) => `
          <div class="ws-card">
            <strong>${escapeHtml(sp.title)}</strong>
            <p style="font-size:0.82rem; color:var(--text-secondary); margin:0.3rem 0;">${escapeHtml(sp.description)}</p>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.75rem;">Autor: ${escapeHtml(sp.author)}</span>
              <div style="display:flex; gap:0.35rem;">
                <button class="btn btn-sm btn-success" onclick="moderateItem('subproject', '${sp.id}', 'approve')">✓ Zatwierdź</button>
                <button class="btn btn-sm btn-danger" onclick="moderateItem('subproject', '${sp.id}', 'delete')">✕ Odrzuć</button>
              </div>
            </div>
          </div>
        `
          )
          .join("")}
      </div>
      <div class="ws-section">
        <h4>Materiały badawcze (${pendingMaterials.length})</h4>
        ${pendingMaterials
          .map(
            (m) => `
          <div class="ws-card">
            <strong>${escapeHtml(m.title)}</strong>
            <p style="font-size:0.82rem; color:var(--text-secondary); margin:0.3rem 0;">${escapeHtml(m.content)}</p>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.75rem;">Autor: ${escapeHtml(m.author)}</span>
              <div style="display:flex; gap:0.35rem;">
                <button class="btn btn-sm btn-success" onclick="moderateItem('material', '${m.id}', 'approve')">✓ Zatwierdź</button>
                <button class="btn btn-sm btn-danger" onclick="moderateItem('material', '${m.id}', 'delete')">✕ Odrzuć</button>
              </div>
            </div>
          </div>
        `
          )
          .join("")}
      </div>
    </div>
  `;
}

function moderateItem(itemType, id, action) {
  if (!appState.isAdmin) return;
  if (itemType === "studyMaterial") {
    if (action === "approve") {
      const sm = appState.data.studyMaterials.find((x) => x.id === id);
      if (sm) sm.status = "approved";
      saveState("Materiał do nauki został zatwierdzony.");
    } else {
      appState.data.studyMaterials = appState.data.studyMaterials.filter((x) => x.id !== id);
      saveState("Materiał do nauki został usunięty.");
    }
  } else if (itemType === "subproject") {
    if (action === "approve") {
      const sp = appState.data.subprojects.find((s) => s.id === id);
      if (sp) sp.status = "approved";
      saveState("Podprojekt zatwierdzony.");
    } else {
      appState.data.subprojects = appState.data.subprojects.filter((s) => s.id !== id);
      saveState("Podprojekt usunięty.");
    }
  } else if (itemType === "material") {
    if (action === "approve") {
      const m = appState.data.materials.find((x) => x.id === id);
      if (m) m.status = "approved";
      saveState("Materiał badawczy zatwierdzony.");
    } else {
      appState.data.materials = appState.data.materials.filter((x) => x.id !== id);
      saveState("Materiał badawczy usunięty.");
    }
  }
}

function approveAllPending() {
  if (!appState.isAdmin) return;
  (appState.data.studyMaterials || []).forEach((sm) => (sm.status = "approved"));
  appState.data.subprojects.forEach((sp) => (sp.status = "approved"));
  appState.data.materials.forEach((m) => (m.status = "approved"));
  saveState("Zatwierdzono wszystkie oczekujące zgłoszenia!");
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
        <input type="text" id="smTopicInput" class="input-field" value="${escapeHtml(defaultTopic)}" placeholder="Wpisz lub potwierdź dział do nauki..." required />
      </div>
      <div class="form-group">
        <label>Tytuł materiału do nauki (np. podręcznik, wykład, kurs, skrypt)</label>
        <input type="text" id="smTitleInput" class="input-field" placeholder="np. Analiza matematyczna i równania różniczkowe w modelowaniu" required />
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
          <option value="Notatka / Skrypt do nauki">Notatka / Skrypt do nauki</option>
          <option value="Zbiór zadań / Ćwiczenia">Zbiór zadań / Ćwiczenia</option>
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
      <div class="form-group">
        <label>Autor zgłoszenia</label>
        <input type="text" id="smAuthorInput" class="input-field" value="${appState.isAdmin ? "Administrator" : "Gość / Obserwator"}" required />
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
    level: document.getElementById("smLevelSelect").value,
    format: document.getElementById("smFormatSelect").value,
    content: document.getElementById("smContentInput").value.trim(),
    url: document.getElementById("smUrlInput").value.trim(),
    author: document.getElementById("smAuthorInput").value.trim(),
    status: appState.isAdmin ? "approved" : "pending",
    isSessionCreated: true,
    createdAt: new Date().toISOString()
  });
  closeModal();
  saveState(
    appState.isAdmin
      ? "Materiał do nauki został opublikowany."
      : "Materiał do nauki został dodany i oczekuje na zatwierdzenie przez Administratora."
  );
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
        <label>Hipoteza startowa</label>
        <input type="text" id="spInitialHypothesis" class="input-field" />
      </div>
      <div class="form-group">
        <label>Autor / Inicjator</label>
        <input type="text" id="spAuthorInput" class="input-field" value="${appState.isAdmin ? "Administrator" : "Gość / Obserwator"}" required />
      </div>
      <div style="display:flex; justify-content:flex-end; margin-top:1rem;">
        <button type="submit" class="btn btn-primary">Uruchom środowisko badawcze</button>
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
  const author = document.getElementById("spAuthorInput").value.trim();
  const approval = appState.isAdmin ? "approved" : "pending";
  const newId = "sub-" + Date.now();

  appState.data.subprojects.unshift({
    id: newId,
    trackId,
    secondaryTracks: ["E"],
    branchTopic,
    title,
    author,
    status: approval,
    isSessionCreated: true,
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
              author,
              approvalStatus: approval,
              isSessionCreated: true
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
  saveState("Środowisko badawcze zostało uruchomione!");
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
        <label>Tytuł materiału</label>
        <input type="text" id="matTitleInput" class="input-field" required />
      </div>
      <div class="form-group">
        <label>Treść / Abstrakt</label>
        <textarea id="matContentInput" class="textarea-field" rows="4" required></textarea>
      </div>
      <div class="form-group">
        <label>Autor zgłoszenia</label>
        <input type="text" id="matAuthorInput" class="input-field" value="${appState.isAdmin ? "Administrator" : "Gość / Obserwator"}" required />
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
    type: "Opracowanie badawcze",
    author: document.getElementById("matAuthorInput").value.trim(),
    content: document.getElementById("matContentInput").value.trim(),
    url: "",
    status: appState.isAdmin ? "approved" : "pending",
    isSessionCreated: true,
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
      <div class="form-group">
        <label>Treść</label>
        <textarea id="wsEntryText" class="textarea-field" rows="3" required></textarea>
      </div>
      <div class="form-group">
        <label>Autor</label>
        <input type="text" id="wsEntryAuthor" class="input-field" value="${appState.isAdmin ? "Administrator" : "Gość"}" required />
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
  const author = document.getElementById("wsEntryAuthor").value.trim();
  const approvalStatus = appState.isAdmin ? "approved" : "pending";
  if (entryType === "hypothesis") {
    sp.workspace.hypotheses.push({ id: "hyp-" + Date.now(), statement: document.getElementById("wsEntryText").value.trim(), status: "Hipoteza otwarta", author, approvalStatus, isSessionCreated: true });
  } else if (entryType === "note") {
    sp.workspace.notes.push({ id: "note-" + Date.now(), title: document.getElementById("wsEntryTitle").value.trim(), content: document.getElementById("wsEntryText").value.trim(), author, approvalStatus, isSessionCreated: true });
  } else {
    sp.workspace.bibliography.push({ id: "bib-" + Date.now(), citation: document.getElementById("wsEntryText").value.trim(), url: "", addedBy: author, approvalStatus, isSessionCreated: true });
  }
  closeModal();
  saveState("Dodano wpis do środowiska.");
}

function toggleAdminMode() {
  if (appState.isAdmin) {
    appState.isAdmin = false;
    sessionStorage.removeItem("golem_xv_is_admin");
    renderAll();
  } else {
    openAdminLoginModal();
  }
}

function openAdminLoginModal() {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🔐 Autoryzacja Administratora</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitAdminLogin(event)">
      <div class="form-group">
        <label>Hasło Administratora (domyślnie: golem15)</label>
        <input type="password" id="adminPassInput" class="input-field" value="golem15" required />
      </div>
      <button type="submit" class="btn btn-primary">Zaloguj</button>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitAdminLogin(e) {
  e.preventDefault();
  const inputPass = document.getElementById("adminPassInput").value;
  const savedPass = localStorage.getItem(ADMIN_PASS_KEY) || "golem15";
  if (inputPass === savedPass || inputPass === "golem15") {
    appState.isAdmin = true;
    sessionStorage.setItem("golem_xv_is_admin", "true");
    closeModal();
    showToast("Zalogowano jako Administrator!");
    renderAll();
  } else {
    showToast("Nieprawidłowe hasło! Domyślne hasło to: golem15");
  }
}

function submitInlineAdminLogin(e) {
  e.preventDefault();
  const inputPass = document.getElementById("inlineAdminPass").value;
  const savedPass = localStorage.getItem(ADMIN_PASS_KEY) || "golem15";
  if (inputPass === savedPass || inputPass === "golem15") {
    appState.isAdmin = true;
    sessionStorage.setItem("golem_xv_is_admin", "true");
    showToast("Zalogowano jako Administrator!");
    renderAll();
  } else {
    showToast("Nieprawidłowe hasło! Domyślne hasło to: golem15");
  }
}

function openChangeAdminPassModal() {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🔑 Ustaw własne hasło Administratora</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitChangeAdminPass(event)">
      <div class="form-group">
        <label>Nowe hasło Administratora</label>
        <input type="password" id="newAdminPassInput" class="input-field" required />
      </div>
      <button type="submit" class="btn btn-primary">Zapisz nowe hasło</button>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitChangeAdminPass(e) {
  e.preventDefault();
  const newPass = document.getElementById("newAdminPassInput").value.trim();
  if (!newPass) return;
  localStorage.setItem(ADMIN_PASS_KEY, newPass);
  closeModal();
  showToast("Nowe hasło Administratora zostało zapisane!");
}


function exportDatabaseJson() {
  const blob = new Blob([JSON.stringify(appState.data, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "the_golem_15_database.json";
  a.click();
  URL.revokeObjectURL(url);
}

window.addEventListener("DOMContentLoaded", initApp);
