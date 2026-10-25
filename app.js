// The Golem 15: A Human's Road to Reality
// Główny moduł aplikacji (obsługa API serwera + automatyczny fallback localStorage)

const DEFAULT_SEED = {
  projectMeta: {
    title: "The Golem 15: A Human's Road to Reality",
    subtitle: "Mapa projektu badawczego — wspólne podstawy naukowe oraz siedem powiązanych ścieżek (A–G)",
    overarchingGoal: "Zrozumieć człowieka jako organizm biologiczny, umysł, twórcę technologii i część ziemskiej biosfery, a jednocześnie zbadać możliwości jego funkcjonowania poza naturalnym środowiskiem Ziemi.",
    organizationalRule: "Każda ścieżka ma własne pytania badawcze, bibliografię i cele. Wspólne podstawy naukowe pozwalają łączyć wiedzę, ale nie oznaczają konieczności równoległego studiowania wszystkich dziedzin. Filozofia pozostaje przekrojową warstwą interpretacyjną. Pozostałe projekty rozwijają się w miarę dostępnego czasu i zainteresowania.",
    foundations: [
      "Matematyka i logika",
      "Informatyka",
      "Programowanie",
      "Fizyka",
      "Elektronika",
      "Chemia",
      "Biologia",
      "Sztuczna inteligencja"
    ],
    fgRelation: {
      summary: "Oba projekty badają człowieka w relacji ze środowiskiem, ale z różnych perspektyw:",
      fPerspective: "Projekt F — kosmos: jak stworzyć sztuczne środowisko podtrzymujące życie tam, gdzie naturalne warunki są dla człowieka nieprzyjazne. Koncentruje się na inżynierii środowiska i adaptacji do warunków pozaziemskich.",
      gPerspective: "Projekt G — Ziemia: jak żyć w istniejącym, złożonym ekosystemie i chronić jego zdolność do podtrzymywania życia. Koncentruje się na ekologii, zdrowiu człowieka, zrównoważonej technologii i ochronie biosfery."
    }
  },
  foundationDisciplines: [
    {
      id: "FND-1",
      order: 1,
      name: "Matematyka i logika",
      icon: "📐",
      color: "#38bdf8",
      description: "Formalny język opisu rzeczywistości, wnioskowania dedukcyjnego, układów dynamicznych, prawdopodobieństwa i informacji.",
      topics: [
        "Logika formalna, rachunek zdań i kwantyfikatorów, teoria mnogości i dowodzenia.",
        "Analiza matematyczna, rachunek różniczkowy i całkowy, równania różniczkowe zwyczajne i cząstkowe.",
        "Algebra liniowa, przestrzenie wektorowe, tensory i metody spektralne.",
        "Rachunek prawdopodobieństwa, statystyka matematyczna i wnioskowanie bayesowskie.",
        "Teoria informacji, entropia Shannona, teoria układów dynamicznych i chaosu.",
        "Matematyka dyskretna, teoria grafów i topologia sieci (podstawa konektomiki i sieci złożonych)."
      ],
      connectedTracks: ["A", "B", "C", "E", "F", "G"]
    },
    {
      id: "FND-2",
      order: 2,
      name: "Informatyka",
      icon: "💻",
      color: "#60a5fa",
      description: "Teoria obliczeń, architektura systemów komputerowych, struktury danych, przetwarzanie informacji i cyberbezpieczeństwo.",
      topics: [
        "Teoria obliczeń, maszyny Turinga, obliczalność i złożoność obliczeniowa.",
        "Algorytmy i struktury danych (grafowe, drzewiaste, probabilistyczne, indeksowanie).",
        "Architektura komputerów (CPU, GPU, pamięci, systemy wbudowane i czasu rzeczywistego).",
        "Systemy operacyjne, współbieżność, systemy rozproszone i obliczenia wysokiej wydajności (HPC).",
        "Bazy danych, reprezentacja wiedzy, ontologie i przetwarzanie wielkich zbiorów danych.",
        "Niezawodność systemów (fault-tolerance) w zastosowaniach medycznych i kosmicznych."
      ],
      connectedTracks: ["A", "B", "C", "F", "G"]
    },
    {
      id: "FND-3",
      order: 3,
      name: "Programowanie",
      icon: "⌨️",
      color: "#818cf8",
      description: "Praktyczna konstrukcja oprogramowania, symulacji numerycznych, modeli badawczych, sterowników sprzętowych i narzędzi analitycznych.",
      topics: [
        "Paradygmaty programowania: imperatywne, obiektowe, funkcyjne i reaktywne.",
        "Python w obliczeniach naukowych i analizie danych (NumPy, SciPy, PyTorch, BioPython).",
        "Języki niskopoziomowe i systemowe (C, C++, Rust) do sterowania robotami, mikrokontrolerami i BCI.",
        "Symulacje numeryczne układów fizycznych, biologicznych i neuronalnych (np. Brian2, NEURON).",
        "Inżynieria oprogramowania, kontrola wersji, testy automatyczne i reprodukowalność badań.",
        "Wizualizacja danych naukowych, interfejsy webowe i wirtualne środowiska badawcze."
      ],
      connectedTracks: ["A", "B", "C", "D", "F", "G"]
    },
    {
      id: "FND-4",
      order: 4,
      name: "Fizyka",
      icon: "⚛️",
      color: "#f59e0b",
      description: "Fundamentalne prawa przyrody rządzące materią, energią, polami, termodynamiką układów żywych, obliczaniem fizycznym i astronautyką.",
      topics: [
        "Mechanika klasyczna, analityczna (Lagrange’a i Hamiltona), biomechanika oraz mechanika orbitalna.",
        "Termodynamika klasyczna i nierównowagowa, fizyka statystyczna i entropia w układach żywych.",
        "Elektrodynamika, fale elektromagnetyczne, optyka i oddziaływanie pól z tkanką biologiczną.",
        "Fizyka ciała stałego i półprzewodników (podstawa elektroniki i układów neuromorficznych).",
        "Mechanika kwantowa, fizyka jądrowa oraz promieniowanie jonizujące (ochrona radiacyjna w kosmosie).",
        "Biofizyka błon komórkowych, transportu jonowego i potencjałów czynnościowych."
      ],
      connectedTracks: ["A", "B", "C", "E", "F", "G"]
    },
    {
      id: "FND-5",
      order: 5,
      name: "Elektronika",
      icon: "🔌",
      color: "#eab308",
      description: "Projektowanie układów analogowych, cyfrowych, sensorów pomiarowych, bioelektroniki oraz fizycznych architektur obliczeniowych.",
      topics: [
        "Teoria obwodów elektrycznych, elementy bierne i czynne, stany nieustalone.",
        "Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy nieliniowe.",
        "Elektronika cyfrowa, układy logiczne, FPGA, mikrokontrolery i systemy SoC.",
        "Akwizycja sygnałów biologicznych (EEG, EMG, EKG): wzmacniacze pomiarowe o niskim szumie i przetworniki ADC/DAC.",
        "Czujniki (sensory) środowiskowe i biomedyczne, aktuatory oraz systemy zasilania i magazynowania energii.",
        "Układy neuromorficzne, memrystory i realizacja sztucznych synaps w krzemie."
      ],
      connectedTracks: ["A", "B", "C", "F", "G"]
    },
    {
      id: "FND-6",
      order: 6,
      name: "Chemia",
      icon: "🧪",
      color: "#10b981",
      description: "Budowa cząsteczek, reakcje chemiczne, biochemia metabolizmu, inżynieria biomateriałów oraz zamknięte obiegi pierwiastków.",
      topics: [
        "Chemia ogólna i nieorganiczna: wiązania chemiczne, stechiometria, równowagi kwasowo-zasadowe i redoks.",
        "Chemia organiczna: grupy funkcyjne, stereochemia, synteza i reaktywność związków węgla.",
        "Biochemia: struktura i funkcja białek, enzymów, lipidów, węglowodanów oraz kwasów nukleinowych (DNA/RNA).",
        "Elektrochemia i chemia fizyczna: potencjały błonowe, ogniwa paliwowe, baterie i elektroliza (np. O2 w kosmosie).",
        "Chemia materiałów: polimery biokompatybilne, hydrożele tkankowe i materiały biodegradowalne.",
        "Chemia środowiska i analityczna: obiegi C, N, P, oczyszczanie wody, powietrza i neutralizacja toksyn."
      ],
      connectedTracks: ["A", "D", "F", "G"]
    },
    {
      id: "FND-7",
      order: 7,
      name: "Biologia",
      icon: "🧬",
      color: "#22c55e",
      description: "Nauka o organizacji życia od poziomu molekularnego i komórkowego po fizjologię człowieka, neurobiologię, regenerację i ekologię biosfery.",
      topics: [
        "Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, sygnalizacja komórkowa.",
        "Genetyka, epigenetyka, genomika i regulacja ekspresji genów.",
        "Anatomia i fizjologia człowieka: układ nerwowy, krążenia, mięśniowo-szkieletowy, odpornościowy i hormonalny.",
        "Neurobiologia: budowa neuronów i gleju, transmisja synaptyczna, plastyczność mózgu i narządy zmysłów.",
        "Biologia rozwoju (embriologia), komórki macierzyste, różnicowanie tkanek i procesy regeneracji.",
        "Mikrobiologia, mikrobiom człowieka oraz ekologia populacji, ekosystemów i biosfery."
      ],
      connectedTracks: ["A", "B", "D", "F", "G"]
    },
    {
      id: "FND-8",
      order: 8,
      name: "Sztuczna inteligencja",
      icon: "🤖",
      color: "#a855f7",
      description: "Algorytmy uczenia maszynowego, głębokie sieci neuronowe, dekodowanie sygnałów biologicznych, autonomia robotyczna i modelowanie poznania.",
      topics: [
        "Podstawy uczenia maszynowego (nadzorowane, nienadzorowane, samonadzorowane) i optymalizacja gradientowa.",
        "Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe sieci neuronowe (SNN).",
        "Uczenie ze wzmocnieniem (Reinforcement Learning) i sterowanie autonomicznymi robotami.",
        "Zastosowania AI w neuroinżynierii (dekodowanie BCI), diagnostyce medycznej i biologii strukturalnej (np. fałdowanie białek).",
        "Modele poznawcze, reprezentacje semantyczne a biologiczne działanie mózgu (porównanie AI i Projektu B).",
        "Interpretowalność modeli (XAI), niezawodność, bezpieczeństwo i filozoficzno-etyczne aspekty AI."
      ],
      connectedTracks: ["A", "B", "C", "D", "E", "F", "G"]
    }
  ],
  studyMaterials: [
    {
      id: "smat-1",
      categoryType: "FOUNDATION",
      targetId: "FND-1",
      topic: "Analiza matematyczna, rachunek różniczkowy i całkowy, równania różniczkowe zwyczajne i cząstkowe.",
      title: "Road to Reality (R. Penrose) — Matematyczne podstawy opisu praw fizyki i układów dynamicznych",
      level: "Podstawowy / Średniozaawansowany",
      format: "Podręcznik / Kompendium",
      content: "Przewodnik po strukturach geometrycznych, liczbach zespolonych, analizie na rozmaitościach i równaniach różniczkowych stanowiących fundament fizyki i modelowania.",
      url: "",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:00:00Z"
    },
    {
      id: "smat-2",
      categoryType: "FOUNDATION",
      targetId: "FND-4",
      topic: "Biofizyka błon komórkowych, transportu jonowego i potencjałów czynnościowych.",
      title: "Równanie Nernsta, Goldmana-Hodgkina-Katza i model błony komórkowej jako obwodu RC",
      level: "Średniozaawansowany",
      format: "Skrypt wykładowy / Notatka do nauki",
      content: "Wyprowadzenie potencjału spoczynkowego i czynnościowego z praw termodynamiki statystycznej oraz elektrodynamiki. Punkt wyjścia dla Projektu A, B i C.",
      url: "",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:05:00Z"
    },
    {
      id: "smat-3",
      categoryType: "FOUNDATION",
      targetId: "FND-7",
      topic: "Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, sygnalizacja komórkowa.",
      title: "Alberts et al. — Molecular Biology of the Cell (Podstawy biologii molekularnej i komórkowej)",
      level: "Podstawowy / Akademicki",
      format: "Podręcznik bazowy",
      content: "Kluczowe kompendium do zrozumienia mechanizmów genetycznych, regulacji genów, komórek macierzystych i inżynierii tkankowej (Projekty A, D, F, G).",
      url: "",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:10:00Z"
    },
    {
      id: "smat-4",
      categoryType: "FOUNDATION",
      targetId: "FND-5",
      topic: "Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy nieliniowe.",
      title: "Horowitz & Hill — Sztuka Elektroniki (The Art of Electronics)",
      level: "Podstawowy / Zaawansowany",
      format: "Podręcznik inżynierski",
      content: "Praktyczne podstawy projektowania obwodów analogowych, niskoszumowych wzmacniaczy biopotencjałów (Projekt A) oraz układów dynamicznych (Projekt C).",
      url: "",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:12:00Z"
    },
    {
      id: "smat-5",
      categoryType: "FOUNDATION",
      targetId: "FND-8",
      topic: "Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe sieci neuronowe (SNN).",
      title: "Dayan & Abbott — Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems",
      level: "Zaawansowany",
      format: "Podręcznik / Kurs",
      content: "Most łączący sztuczną inteligencję, matematykę i neurobiologię: kodowanie neuronalne, plastyczność synaptyczna Hebba i uczenie w sieciach biologicznych.",
      url: "",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:15:00Z"
    }
  ],
  tracks: [
    {
      id: "A",
      code: "Projekt A",
      name: "Człowiek biocyfrowo-robotyczny",
      color: "#38bdf8",
      goal: "Wspomaganie, naprawa i rozszerzanie możliwości ludzkiego organizmu.",
      guidingQuestion: "Jak technologia może wspierać i rozszerzać możliwości człowieka?",
      note: "",
      sections: [
        {
          title: "Zakres badawczy",
          items: [
            "Medycyna regeneracyjna, protezy i sztuczne narządy.",
            "Robotyka, bioelektronika i inżynieria biomedyczna.",
            "Interfejsy mózg–komputer.",
            "Wspomaganie ludzkich zmysłów i funkcji ruchowych."
          ]
        }
      ]
    },
    {
      id: "B",
      code: "Projekt B",
      name: "Cyfrowy umysł",
      color: "#a855f7",
      goal: "Poznanie zasad działania mózgu i zbadanie możliwości jego komputerowego modelowania.",
      guidingQuestion: "Czy można odtworzyć działanie umysłu w komputerze i co oznaczałoby takie odtworzenie?",
      note: "Pełne przeniesienie umysłu do komputera pozostaje hipotetycznym celem badawczym.",
      sections: [
        {
          title: "Zakres badawczy",
          items: [
            "Neurobiologia i neuronauka obliczeniowa.",
            "Modelowanie neuronów i sieci neuronalnych.",
            "Konektomika i poznanie.",
            "Świadomość oraz hipotetyczna emulacja całego mózgu."
          ]
        }
      ]
    },
    {
      id: "C",
      code: "Projekt C",
      name: "Maszyny analogowe i obliczanie przez fizykę",
      color: "#f59e0b",
      goal: "Poznanie alternatywnych sposobów realizowania obliczeń.",
      guidingQuestion: "Jak wykorzystać właściwości fizyczne układów do efektywnego obliczania i modelowania procesów podobnych do pracy mózgu?",
      note: "",
      sections: [
        {
          title: "Zakres badawczy",
          items: [
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
      id: "D",
      code: "Projekt D",
      name: "„Frankenstein”: tworzenie człowieka i science fiction",
      color: "#10b981",
      goal: "Poznanie naukowych możliwości tworzenia, odtwarzania i modyfikowania organizmów.",
      guidingQuestion: "Co można rzeczywiście stworzyć lub zmodyfikować w żywym organizmie, a co pozostaje fikcją?",
      note: "",
      sections: [
        {
          title: "Zakres badawczy",
          items: [
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
      id: "E",
      code: "Projekt E",
      name: "Filozofia jako warstwa przekrojowa",
      color: "#eab308",
      goal: "Interpretowanie osiągnięć nauki i badanie granic poznania.",
      guidingQuestion: "Co wiemy, jak to uzasadniamy i jakie konsekwencje wynikają z naszej wiedzy?",
      note: "Filozofia pozostaje osobnym obszarem nauki, rozwijanym niezależnie. W tym projekcie jest nakładką interpretacyjną na pozostałe ścieżki, a nie dodatkowym obowiązkowym przedmiotem.",
      sections: [
        {
          title: "Zakres badawczy",
          items: [
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
      id: "F",
      code: "Projekt F",
      name: "Człowiek w kosmosie",
      color: "#6366f1",
      goal: "Poznanie sposobów przystosowania technologii, organizmu człowieka i środowiska życia do podróży kosmicznych oraz długotrwałej obecności poza Ziemią.",
      guidingQuestion: "Jak stworzyć warunki, w których człowiek może bezpiecznie podróżować i żyć poza Ziemią, nie zakładając, że jego organizm łatwo przystosuje się do każdego środowiska?",
      note: "",
      sections: [
        {
          title: "A. Technologia podróży kosmicznych",
          items: [
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
          title: "B. Przystosowanie organizmu człowieka",
          items: [
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
          title: "C. Długotrwałe życie poza Ziemią",
          items: [
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
      id: "G",
      code: "Projekt G",
      name: "Człowiek na Ziemi: adaptacja i ochrona ekosystemu",
      color: "#22c55e",
      goal: "Zrozumienie zależności między ludzkim organizmem, cywilizacją techniczną i ziemskim środowiskiem oraz opracowanie sposobów życia, które nie niszczą podstaw własnego istnienia.",
      guidingQuestion: "Jak człowiek może przystosować swoje życie i technologię do warunków Ziemi, chroniąc jednocześnie ekosystemy, od których zależy?",
      note: "",
      sections: [
        {
          title: "A. Człowiek jako organizm ziemski",
          items: [
            "Fizjologia człowieka i adaptacja do temperatury, wysokości oraz wysiłku.",
            "Wpływ środowiska na zdrowie, odporność i rozwój.",
            "Relacje człowieka z mikroorganizmami i mikrobiomem.",
            "Znaczenie wody, powietrza, gleby i pożywienia.",
            "Ograniczenia biologiczne człowieka i zdolność organizmu do adaptacji.",
            "Wpływ miejskiego środowiska, hałasu, światła i zanieczyszczeń na organizm."
          ]
        },
        {
          title: "B. Ekologia i funkcjonowanie ekosystemów",
          items: [
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
          title: "C. Technologia przyjazna środowisku",
          items: [
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
          title: "D. Cywilizacja a granice środowiskowe",
          items: [
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
  subprojects: [
    {
      id: "sub-1",
      trackId: "A",
      secondaryTracks: ["B", "E"],
      branchTopic: "Interfejsy mózg–komputer.",
      title: "Dekodowanie intencji ruchowej i sprzężenie czuciowe w neuroprotezach",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:00:00Z",
      description: "Badanie dwukierunkowych interfejsów korowo-obwodowych pozwalających nie tylko sterować efektorami, ale też odbierać sygnały proprioceptywne i dotykowe.",
      philosophicalNote: "Pytanie o granice schematu ciała i podmiotowości: kiedy sztuczny efektor staje się integralną częścią doświadczenia użytkownika?",
      workspace: {
        hypotheses: [
          {
            id: "hyp-1",
            statement: "Zamknięcie pętli sprzężenia zwrotnego o opóźnieniu < 25 ms znacząco przyspiesza neuroplastyczną integrację protezy ze schematem ciała.",
            status: "W weryfikacji",
            author: "Administrator",
            approvalStatus: "approved"
          }
        ],
        notes: [
          {
            id: "note-1",
            title: "Granica inwazyjności a stabilność sygnału",
            content: "Matryce mikroelektrod zapewniają wysoką rozdzielczość przestrzenną, ale ulegają gliozie. Alternatywą są podejścia wewnątrznaczyniowe (Stentrode) oraz optogenetyczne.",
            author: "Administrator",
            createdAt: "2026-10-25T12:10:00Z",
            approvalStatus: "approved"
          }
        ],
        bibliography: [
          {
            id: "bib-1",
            citation: "Lebedev, M. A., & Nicolelis, M. A. (2017). Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation. Physiological Reviews.",
            url: "https://doi.org/10.1152/physrev.00027.2016",
            addedBy: "Administrator",
            approvalStatus: "approved"
          }
        ]
      }
    },
    {
      id: "sub-2",
      trackId: "C",
      secondaryTracks: ["B", "A"],
      branchTopic: "Komputery neuromorficzne.",
      title: "Oscylatory relaksacyjne i memrystorowe synapsy w obliczeniach ciągłych",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:15:00Z",
      description: "Środowisko badawcze poświęcone fizycznej realizacji impulsowych sieci neuronowych (SNN) w domenie analogowej bez dyskretyzacji zegarowej.",
      philosophicalNote: "Czy obliczanie ciągłe realizowane bezpośrednio przez prawa fizyki układu analogowego przekracza ograniczenia klasycznych modeli symbolicznych?",
      workspace: {
        hypotheses: [
          {
            id: "hyp-2",
            statement: "Szum termiczny w układach submikronowych może pełnić funkcję rezonansu stochastycznego, obniżając próg energetyczny detekcji słabych sygnałów.",
            status: "Hipoteza otwarta",
            author: "Administrator",
            approvalStatus: "approved"
          }
        ],
        notes: [
          {
            id: "note-2",
            title: "Porównanie modelu Hodgkina-Huxleya i obwodu FitzHugh-Nagumo",
            content: "Układ analogowy FHN pozwala odwzorować pobudliwość błony przy użyciu pojedynczego nieliniowego elementu i indukcyjności (lub żyratora CMOS).",
            author: "Administrator",
            createdAt: "2026-10-25T12:20:00Z",
            approvalStatus: "approved"
          }
        ],
        bibliography: [
          {
            id: "bib-2",
            citation: "Indiveri, G., et al. (2011). Neuromorphic silicon neuron circuits. Frontiers in Neuroscience.",
            url: "https://doi.org/10.3389/fnins.2011.00073",
            addedBy: "Administrator",
            approvalStatus: "approved"
          }
        ]
      }
    },
    {
      id: "sub-3",
      trackId: "F",
      secondaryTracks: ["G", "D"],
      branchTopic: "Zamknięte i częściowo zamknięte systemy podtrzymywania życia.",
      title: "Bioregeneracyjne systemy podtrzymywania życia (BLSS) — obieg pierwiastków w habitacie i na Ziemi",
      author: "Administrator",
      status: "approved",
      createdAt: "2026-10-25T12:30:00Z",
      description: "Porównanie małych, sztucznie domykanych pętli metabolicznych (fotobioreaktory mikroglonowe + uprawy hydroponiczne) z buforową pojemnością ziemskich ekosystemów.",
      philosophicalNote: "Próba odtworzenia biosfery w skali mikro uwidacznia niewidoczne na co dzień usługi ekosystemowe Ziemi (Projekt G) oraz kruchość sztucznych habitatów (Projekt F).",
      workspace: {
        hypotheses: [
          {
            id: "hyp-3",
            statement: "Stabilność mikrobiomu ryzosfery w zamkniętym habitacie wymaga kontrolowanej redundancji gatunkowej wzorowanej na naturalnych glebach z Projektu G.",
            status: "W weryfikacji",
            author: "Administrator",
            approvalStatus: "approved"
          }
        ],
        notes: [
          {
            id: "note-3",
            title: "Wnioski z eksperymentów MELiSSA i BIOS-3",
            content: "Największym wyzwaniem pozostaje pełna mineralizacja odpadów lignocelulozowych oraz utrzymanie równowagi stechiometrycznej O2/CO2 przy zmiennym metabolizmie załogi.",
            author: "Administrator",
            createdAt: "2026-10-25T12:35:00Z",
            approvalStatus: "approved"
          }
        ],
        bibliography: [
          {
            id: "bib-3",
            citation: "Lasseur, C., et al. (2010). MELiSSA: The European project of closed life support system. Gravitational and Space Biology.",
            url: "",
            addedBy: "Administrator",
            approvalStatus: "approved"
          }
        ]
      }
    }
  ],
  materials: [
    {
      id: "mat-1",
      trackId: "E",
      branchTopic: "Filozofia nauki: dowód, hipoteza, teoria i granice modeli.",
      subprojectId: null,
      title: "Granice modeli formalnych a interpretacja stanów umysłowych i biologicznych",
      type: "Artykuł / Notatka przekrojowa",
      author: "Administrator",
      content: "Rozróżnienie między symulacją składniową (syntaktyczną) a realizacją właściwości przyczynowych układu fizycznego — punkt styku Projektu B, C oraz E.",
      url: "",
      status: "approved",
      createdAt: "2026-10-25T11:50:00Z"
    },
    {
      id: "mat-2",
      trackId: "B",
      branchTopic: "Neurobiologia i neuronauka obliczeniowa.",
      subprojectId: "sub-1",
      title: "Zestawienie rozdzielczości czasowo-przestrzennej metod neuroobrazowania (EEG, fNIRS, fMRI, ECoG)",
      type: "Zestaw danych / Opracowanie",
      author: "Dr Janina Kowalska (Gość)",
      content: "Porównanie pasma przenoszenia, stosunku sygnału do szumu (SNR) oraz biokompatybilności długoterminowej dla zastosowań w Projektach A i B.",
      url: "https://example.org/neuro-resolution-matrix",
      status: "pending",
      createdAt: "2026-10-25T13:10:00Z"
    }
  ],
  graphLinks: [
    { id: "lnk-1", source: "A", target: "B", label: "Interfejsy mózg–komputer i dekodowanie sygnałów nerwowych", status: "approved" },
    { id: "lnk-2", source: "B", target: "C", label: "Fizyczne i neuromorficzne modele sieci neuronalnych", status: "approved" },
    { id: "lnk-3", source: "A", target: "D", label: "Inżynieria tkankowa, sztuczne narządy i medycyna regeneracyjna", status: "approved" },
    { id: "lnk-4", source: "F", target: "G", label: "Zamknięte obiegi materii (BLSS) vs. ziemska biosfera i ekologia", status: "approved" },
    { id: "lnk-5", source: "A", target: "F", label: "Medycyna kosmiczna, ochrona organizmu i robotyka autonomiczna", status: "approved" },
    { id: "lnk-6", source: "D", target: "F", label: "Biologia regeneracji i odporność radiacyjna w długich misjach", status: "approved" },
    { id: "lnk-7", source: "E", target: "A", label: "Filozofia techniki i etyka ulepszania człowieka", status: "approved" },
    { id: "lnk-8", source: "E", target: "B", label: "Filozofia umysłu, świadomość i granice modeli obliczeniowych", status: "approved" },
    { id: "lnk-9", source: "E", target: "D", label: "Bioetyka edycji genomu i granice tworzenia organizmów", status: "approved" },
    { id: "lnk-10", source: "E", target: "F", label: "Etyka ekspansji kosmicznej i ochrona planetarna", status: "approved" },
    { id: "lnk-11", source: "E", target: "G", label: "Odpowiedzialność międzypokoleniowa i filozofia przyrody", status: "approved" }
  ]
};

const STORAGE_KEY = "the_golem_15_state_v2";
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
  if (!d.studyMaterials) {
    d.studyMaterials = JSON.parse(JSON.stringify(DEFAULT_SEED.studyMaterials));
  }
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

// --- WIDOK 0 (PIERWSZA OPCJA): MATERIAŁY DO NAUKI (8 DZIEDZIN PODSTAWOWYCH PO KOLEI + ODNOGI A-G) ---
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
                      <p style="font-size:0.82rem; color:var(--text-secondary);">${escapeHtml(m.content)}</p>
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
    tracksTree.innerHTML = appState.data.tracks
      .map((tr) => {
        const mats = (appState.data.studyMaterials || []).filter(
          (sm) =>
            sm.categoryType === "TRACK" &&
            sm.targetId === tr.id &&
            (sm.status === "approved" || appState.isAdmin || sm.isSessionCreated)
        );
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
                          <p style="font-size:0.82rem; color:var(--text-secondary);">${escapeHtml(m.content)}</p>
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
          <span class="track-code" style="color:${track.color}; margin:0;">${escapeHtml(track.code)}: ${escapeHtml(track.name)}</span>
          ${
            m.status === "pending"
              ? `<span class="status-tag status-pending">Oczekuje na zgodę Administratora</span>`
              : `<span class="status-tag status-approved">Zatwierdzony</span>`
          }
        </div>
        <h3 style="font-size:1.08rem; margin-bottom:0.35rem;">${escapeHtml(m.title)}</h3>
        <p style="color:var(--text-secondary); margin-bottom:0.65rem;">${escapeHtml(m.content)}</p>
        <div style="font-size:0.8rem; color:var(--text-muted);">Autor zgłoszenia: <strong>${escapeHtml(m.author)}</strong></div>
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
