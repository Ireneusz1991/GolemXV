// Golem XV — Ludzie: Droga do Rzeczywistości
// Główny moduł aplikacji (obsługa API serwera + automatyczny fallback localStorage)

const DEFAULT_SEED = {
  projectMeta: {
    title: "Golem XV — Ludzie: Droga do Rzeczywistości",
    subtitle: "Mapa projektu badawczego — siedem powiązanych ścieżek",
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
      philosophicalNote: "Pytanie o granice schematu ciała i podmiotowości: kiedy sztuczny efektor staje się integralną częścią doświadczenia fenomelogicznego użytkownika?",
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
      content: "Rozróżnienie między symulacją składniową (syntaktyczną) a realizacją właściwości przyczynowych układu fizycznego — punkt styku Projektu B (Cyfrowy umysł), Projektu C (Obliczanie przez fizykę) oraz Projektu E.",
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

const STORAGE_KEY = "golem_xv_state_v1";
const ADMIN_PASS_KEY = "golem_xv_admin_pass";

const appState = {
  data: null,
  isAdmin: false,
  serverOnline: false,
  activeTab: "map", // 'map' | 'workspaces' | 'materials' | 'graph' | 'moderation'
  selectedTrackFilter: "ALL",
  selectedSubprojectId: "sub-1",
  materialFilterTrack: "ALL",
  materialSearch: "",
  selectedGraphNode: null
};

// --- Inicjalizacja i synchronizacja danych ---
async function initApp() {
  // Sprawdź zapisaną sesję admina
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
      appState.data = await res.json();
      appState.serverOnline = true;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(appState.data));
      updateServerBadge();
      return;
    }
  } catch (e) {
    // Brak uruchomionego serwera HTTP — używamy localStorage / DEFAULT_SEED
  }

  appState.serverOnline = false;
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    try {
      appState.data = JSON.parse(saved);
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
    el.innerHTML = `<span class="status-dot" style="background:#38bdf8"></span> Baza lokalna przeglądarki (Tryb bezpośredni)`;
  }
}

// --- Pomocnicze funkcje UI ---
function showToast(message) {
  const container = document.getElementById("toastContainer");
  if (!container) return;
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(() => {
    toast.remove();
  }, 4000);
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function getTrackById(id) {
  return appState.data.tracks.find((t) => t.id === id) || { id, code: `Projekt ${id}`, name: id, color: "#38bdf8" };
}

function countPendingItems() {
  if (!appState.data) return 0;
  let count = 0;
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

// --- Nawigacja ---
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

// --- Renderowanie główne ---
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
    roleBadge.innerHTML = `<span>👁</span> Tryb Gościa / Obserwatora (Zgłoszenia wymagają autoryzacji)`;
    authBtn.textContent = "Zaloguj jako Administrator";
    authBtn.className = "btn btn-sm btn-primary";
  }
}

function renderNavCounts() {
  const approvedSubprojects = appState.data.subprojects.filter(
    (s) => s.status === "approved" || appState.isAdmin
  ).length;
  const approvedMaterials = appState.data.materials.filter(
    (m) => m.status === "approved" || appState.isAdmin
  ).length;
  const pendingTotal = countPendingItems();

  const subCountEl = document.getElementById("navSubprojectsCount");
  const matCountEl = document.getElementById("navMaterialsCount");
  const modCountEl = document.getElementById("navModerationCount");

  if (subCountEl) subCountEl.textContent = approvedSubprojects;
  if (matCountEl) matCountEl.textContent = approvedMaterials;
  if (modCountEl) {
    modCountEl.textContent = pendingTotal;
    modCountEl.className = pendingTotal > 0 ? "badge-count pending-alert" : "badge-count";
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
        <span style="font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--text-muted); font-weight:700;">Wspólne podstawy naukowe:</span>
        <div class="foundations-list">
          ${meta.foundations.map((f) => `<span class="foundation-pill">${escapeHtml(f)}</span>`).join("")}
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
            <button class="btn btn-sm" onclick="openNewSubprojectModal('${track.id}', '')" title="Uruchom nowy podprojekt i środowisko badawcze w tej ścieżce">
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
                        <button class="btn btn-sm branch-launch-btn" onclick="openNewSubprojectModal('${track.id}', '${escapeHtml(item).replace(/'/g, "\\'")}')" title="Uruchom środowisko badawcze dla tej odnogi">
                          🚀 Środowisko
                        </button>
                        <button class="btn btn-sm branch-launch-btn" onclick="openNewMaterialModal('${track.id}', '${escapeHtml(item).replace(/'/g, "\\'")}')" title="Dodaj materiał do tej odnogi">
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
            <span>🔬 Środowiska / Podprojekty: <strong>${subCount}</strong></span>
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
    listEl.innerHTML = `<p style="color:var(--text-muted); font-size:0.86rem;">Brak podprojektów dla wybranego filtru. Kliknij „+ Nowy podprojekt / środowisko”, aby zainicjować badanie.</p>`;
  } else {
    listEl.innerHTML = visibleSubprojects
      .map((sp) => {
        const track = getTrackById(sp.trackId);
        const activeClass = sp.id === appState.selectedSubprojectId ? "active" : "";
        const statusBadge =
          sp.status === "pending"
            ? `<span class="status-tag status-pending">Oczekuje na zgodę Admina</span>`
            : `<span class="status-tag status-approved">Zatwierdzony</span>`;
        return `
        <div class="subproject-item ${activeClass}" onclick="selectSubproject('${sp.id}')">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:0.4rem; margin-bottom:0.3rem;">
            <span style="font-size:0.74rem; font-weight:700; color:${track.color};">${escapeHtml(track.code)}</span>
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

  const primaryTrack = getTrackById(activeSp.trackId);
  const secondaryBadges = (activeSp.secondaryTracks || [])
    .map((tid) => {
      const t = getTrackById(tid);
      return `<span class="foundation-pill" style="border-color:${t.color}; color:${t.color}; background:transparent;">Powiązanie: ${escapeHtml(t.code)}</span>`;
    })
    .join("");

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
  const relatedMaterials = appState.data.materials.filter(
    (m) =>
      m.subprojectId === activeSp.id &&
      (m.status === "approved" || appState.isAdmin || m.isSessionCreated)
  );

  panelEl.innerHTML = `
    <div style="border-bottom:1px solid var(--border-color); padding-bottom:1.1rem;">
      <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-start; gap:0.75rem;">
        <div>
          <div style="display:flex; flex-wrap:wrap; gap:0.45rem; align-items:center; margin-bottom:0.4rem;">
            <span class="track-code" style="color:${primaryTrack.color}; margin:0;">${escapeHtml(primaryTrack.code)} — ${escapeHtml(primaryTrack.name)}</span>
            ${secondaryBadges}
            ${
              activeSp.status === "pending"
                ? `<span class="status-tag status-pending">Oczekuje na zatwierdzenie przez Administratora</span>`
                : `<span class="status-tag status-approved">Środowisko Aktywne</span>`
            }
          </div>
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
              ? `<button class="btn btn-sm btn-danger" onclick="moderateItem('subproject', '${activeSp.id}', 'delete')">Usuń podprojekt</button>`
              : ""
          }
          <button class="btn btn-sm btn-primary" onclick="openNewMaterialModal('${activeSp.trackId}', '${escapeHtml(activeSp.branchTopic || "").replace(/'/g, "\\'")}', '${activeSp.id}')">
            + Dodaj materiał do tego środowiska
          </button>
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
      <!-- MODUŁ 1: HIPOTEZY BADAWCZE -->
      <div class="ws-section">
        <h4>
          <span>1. Hipotezy badawcze (${hypotheses.length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('hypothesis', '${activeSp.id}')">+ Hipoteza</button>
        </h4>
        ${
          hypotheses.length === 0
            ? `<p style="font-size:0.82rem; color:var(--text-muted);">Brak hipotez. Dodaj pierwszą hipotezę badawczą.</p>`
            : hypotheses
                .map(
                  (h) => `
              <div class="ws-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem; gap:0.4rem;">
                  <span class="foundation-pill" style="font-size:0.7rem;">${escapeHtml(h.status || "Hipoteza otwarta")}</span>
                  ${
                    h.approvalStatus === "pending"
                      ? `<span class="status-tag status-pending">Do akceptacji Admina</span>`
                      : ""
                  }
                </div>
                <p style="margin-bottom:0.4rem;">${escapeHtml(h.statement)}</p>
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem; color:var(--text-muted);">
                  <span>Autor: ${escapeHtml(h.author)}</span>
                  ${
                    appState.isAdmin
                      ? `<div style="display:flex; gap:0.3rem;">
                          ${
                            h.approvalStatus === "pending"
                              ? `<button class="btn btn-sm btn-success" onclick="moderateWorkspaceEntry('${activeSp.id}', 'hypotheses', '${h.id}', 'approve')">✓</button>`
                              : ""
                          }
                          <button class="btn btn-sm btn-danger" onclick="moderateWorkspaceEntry('${activeSp.id}', 'hypotheses', '${h.id}', 'delete')">✕</button>
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

      <!-- MODUŁ 2: NOTATNIK BADAWCZY -->
      <div class="ws-section">
        <h4>
          <span>2. Notatnik laboratoryjny / badawczy (${notes.length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('note', '${activeSp.id}')">+ Notatka</button>
        </h4>
        ${
          notes.length === 0
            ? `<p style="font-size:0.82rem; color:var(--text-muted);">Brak notatek w tym środowisku.</p>`
            : notes
                .map(
                  (n) => `
              <div class="ws-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                  <strong>${escapeHtml(n.title)}</strong>
                  ${
                    n.approvalStatus === "pending"
                      ? `<span class="status-tag status-pending">Do akceptacji Admina</span>`
                      : ""
                  }
                </div>
                <p style="color:var(--text-secondary); margin-bottom:0.4rem;">${escapeHtml(n.content)}</p>
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem; color:var(--text-muted);">
                  <span>Autor: ${escapeHtml(n.author)}</span>
                  ${
                    appState.isAdmin
                      ? `<div style="display:flex; gap:0.3rem;">
                          ${
                            n.approvalStatus === "pending"
                              ? `<button class="btn btn-sm btn-success" onclick="moderateWorkspaceEntry('${activeSp.id}', 'notes', '${n.id}', 'approve')">✓</button>`
                              : ""
                          }
                          <button class="btn btn-sm btn-danger" onclick="moderateWorkspaceEntry('${activeSp.id}', 'notes', '${n.id}', 'delete')">✕</button>
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

      <!-- MODUŁ 3: BIBLIOGRAFIA I MATERIAŁY -->
      <div class="ws-section">
        <h4>
          <span>3. Bibliografia i przypisane materiały (${bibliography.length + relatedMaterials.length})</span>
          <button class="btn btn-sm" onclick="openWorkspaceEntryModal('bibliography', '${activeSp.id}')">+ Źródło</button>
        </h4>
        ${
          bibliography.length === 0 && relatedMaterials.length === 0
            ? `<p style="font-size:0.82rem; color:var(--text-muted);">Brak pozycji bibliograficznych.</p>`
            : ""
        }
        ${bibliography
          .map(
            (b) => `
          <div class="ws-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:0.4rem;">
              <p style="margin-bottom:0.3rem;">📖 ${escapeHtml(b.citation)}</p>
              ${
                b.approvalStatus === "pending"
                  ? `<span class="status-tag status-pending">Do akceptacji</span>`
                  : ""
              }
            </div>
            ${
              b.url
                ? `<a href="${escapeHtml(b.url)}" target="_blank" rel="noopener" style="color:var(--accent-blue); font-size:0.78rem; word-break:break-all;">${escapeHtml(b.url)}</a>`
                : ""
            }
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem; color:var(--text-muted); margin-top:0.35rem;">
              <span>Dodał(a): ${escapeHtml(b.addedBy)}</span>
              ${
                appState.isAdmin
                  ? `<div style="display:flex; gap:0.3rem;">
                      ${
                        b.approvalStatus === "pending"
                          ? `<button class="btn btn-sm btn-success" onclick="moderateWorkspaceEntry('${activeSp.id}', 'bibliography', '${b.id}', 'approve')">✓</button>`
                          : ""
                      }
                      <button class="btn btn-sm btn-danger" onclick="moderateWorkspaceEntry('${activeSp.id}', 'bibliography', '${b.id}', 'delete')">✕</button>
                    </div>`
                  : ""
              }
            </div>
          </div>
        `
          )
          .join("")}
        ${relatedMaterials
          .map(
            (m) => `
          <div class="ws-card" style="border-left:3px solid var(--accent-blue);">
            <div style="font-size:0.74rem; color:var(--accent-blue); font-weight:600;">MATERIAŁ BADAWCZY (${escapeHtml(m.type)})</div>
            <strong>${escapeHtml(m.title)}</strong>
            <p style="font-size:0.82rem; color:var(--text-secondary); margin-top:0.25rem;">${escapeHtml(m.content)}</p>
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
    listEl.innerHTML = `<div class="ws-card" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak materiałów spełniających kryteria. Dodaj nowy materiał badawczy przyciskiem powyżej.</div>`;
    return;
  }

  listEl.innerHTML = filtered
    .map((m) => {
      const track = getTrackById(m.trackId);
      const linkedSp = m.subprojectId
        ? appState.data.subprojects.find((s) => s.id === m.subprojectId)
        : null;
      return `
      <div class="ws-card" style="padding:1.15rem; border-left:4px solid ${track.color};">
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:0.5rem; margin-bottom:0.45rem;">
          <div style="display:flex; flex-wrap:wrap; gap:0.45rem; align-items:center;">
            <span class="track-code" style="color:${track.color}; margin:0;">${escapeHtml(track.code)}: ${escapeHtml(track.name)}</span>
            <span class="foundation-pill">${escapeHtml(m.type)}</span>
            ${
              m.status === "pending"
                ? `<span class="status-tag status-pending">Oczekuje na zgodę Administratora</span>`
                : `<span class="status-tag status-approved">Zatwierdzony</span>`
            }
          </div>
          <div style="display:flex; gap:0.4rem;">
            ${
              appState.isAdmin && m.status === "pending"
                ? `<button class="btn btn-sm btn-success" onclick="moderateItem('material', '${m.id}', 'approve')">✓ Zatwierdź materiał</button>`
                : ""
            }
            ${
              appState.isAdmin
                ? `<button class="btn btn-sm btn-danger" onclick="moderateItem('material', '${m.id}', 'delete')">Usuń</button>`
                : ""
            }
          </div>
        </div>
        <h3 style="font-size:1.08rem; margin-bottom:0.35rem;">${escapeHtml(m.title)}</h3>
        ${
          m.branchTopic
            ? `<div style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.35rem;">Odnoga: <strong>${escapeHtml(m.branchTopic)}</strong></div>`
            : ""
        }
        <p style="color:var(--text-secondary); margin-bottom:0.65rem;">${escapeHtml(m.content)}</p>
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:0.5rem; font-size:0.8rem; color:var(--text-muted);">
          <span>Autor zgłoszenia: <strong>${escapeHtml(m.author)}</strong></span>
          <div style="display:flex; gap:0.75rem; align-items:center;">
            ${
              linkedSp
                ? `<a href="javascript:void(0)" onclick="selectSubproject('${linkedSp.id}'); switchTab('workspaces');" style="color:var(--accent-blue);">🔬 Powiązane środowisko: ${escapeHtml(linkedSp.title)}</a>`
                : ""
            }
            ${
              m.url
                ? `<a href="${escapeHtml(m.url)}" target="_blank" rel="noopener" style="color:var(--accent-blue);">🔗 Link zewnętrzny / DOI</a>`
                : ""
            }
          </div>
        </div>
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

  // Pozycje 7 ścieżek (E w centrum jako warstwa przekrojowa, pozostałe na okręgu)
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
      const isPending = lnk.status === "pending";
      const isFG =
        (lnk.source === "F" && lnk.target === "G") ||
        (lnk.source === "G" && lnk.target === "F");
      const stroke = isPending ? "#f59e0b" : isFG ? "#818cf8" : "#475569";
      const dash = isPending ? "6,4" : isFG ? "none" : "none";
      const width = isFG ? 3.2 : 2;
      return `
      <g>
        <line x1="${s.x}" y1="${s.y}" x2="${t.x}" y2="${t.y}" stroke="${stroke}" stroke-width="${width}" stroke-dasharray="${dash}" opacity="0.75" />
      </g>
    `;
    })
    .join("");

  const nodesSvg = appState.data.tracks
    .map((tr) => {
      const c = coords[tr.id] || { x: 100, y: 100 };
      const r = tr.id === "E" ? 44 : 36;
      const subCount = appState.data.subprojects.filter(
        (s) => s.trackId === tr.id && (s.status === "approved" || appState.isAdmin)
      ).length;
      return `
      <g style="cursor:pointer;" onclick="selectGraphNode('${tr.id}')">
        <circle cx="${c.x}" cy="${c.y}" r="${r + 6}" fill="${tr.color}" opacity="0.15" />
        <circle cx="${c.x}" cy="${c.y}" r="${r}" fill="#111827" stroke="${tr.color}" stroke-width="3" />
        <text x="${c.x}" y="${c.y - 4}" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="700">${escapeHtml(tr.code)}</text>
        <text x="${c.x}" y="${c.y + 14}" text-anchor="middle" fill="#94a3b8" font-size="10">${subCount} środ.</text>
        <text x="${c.x}" y="${c.y + r + 18}" text-anchor="middle" fill="#e2e8f0" font-size="11.5" font-weight="600">${escapeHtml(tr.name)}</text>
      </g>
    `;
    })
    .join("");

  svgWrapper.innerHTML = `
    <svg viewBox="0 0 900 520" width="100%" height="100%">
      ${linesSvg}
      ${nodesSvg}
    </svg>
  `;

  const filteredLinks = appState.selectedGraphNode
    ? visibleLinks.filter(
        (l) => l.source === appState.selectedGraphNode || l.target === appState.selectedGraphNode
      )
    : visibleLinks;

  linksListEl.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
      <h4>
        ${
          appState.selectedGraphNode
            ? `Powiązania dla: Projekt ${appState.selectedGraphNode} (${filteredLinks.length})`
            : `Wszystkie relacje międzyścieżkowe (${filteredLinks.length})`
        }
      </h4>
      <div style="display:flex; gap:0.4rem;">
        ${
          appState.selectedGraphNode
            ? `<button class="btn btn-sm" onclick="selectGraphNode(null)">Pokaż wszystkie</button>`
            : ""
        }
        <button class="btn btn-sm btn-primary" onclick="openNewGraphLinkModal()">+ Dodaj powiązanie międzyścieżkowe</button>
      </div>
    </div>
    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(290px, 1fr)); gap:0.75rem;">
      ${filteredLinks
        .map((l) => {
          const s = getTrackById(l.source);
          const t = getTrackById(l.target);
          return `
          <div class="ws-card" style="display:flex; justify-content:space-between; align-items:flex-start; gap:0.5rem;">
            <div>
              <div style="font-size:0.78rem; font-weight:700; margin-bottom:0.25rem;">
                <span style="color:${s.color}">${escapeHtml(s.code)}</span> ↔ <span style="color:${t.color}">${escapeHtml(t.code)}</span>
                ${l.status === "pending" ? `<span class="status-tag status-pending">Oczekujące</span>` : ""}
              </div>
              <p style="font-size:0.84rem; color:var(--text-secondary);">${escapeHtml(l.label)}</p>
            </div>
            ${
              appState.isAdmin
                ? `<div style="display:flex; gap:0.25rem;">
                    ${
                      l.status === "pending"
                        ? `<button class="btn btn-sm btn-success" onclick="moderateGraphLink('${l.id}', 'approve')">✓</button>`
                        : ""
                    }
                    <button class="btn btn-sm btn-danger" onclick="moderateGraphLink('${l.id}', 'delete')">✕</button>
                  </div>`
                : ""
            }
          </div>
        `;
        })
        .join("")}
    </div>
  `;
}

function selectGraphNode(trackId) {
  appState.selectedGraphNode = trackId;
  renderGraphView();
}

// --- WIDOK 5: CENTRUM AUTORYZACJI ADMINISTRATORA (MODERACJA) ---
function renderModerationView() {
  const container = document.getElementById("moderationContainer");
  if (!container) return;

  const pendingSubprojects = appState.data.subprojects.filter((s) => s.status === "pending");
  const pendingMaterials = appState.data.materials.filter((m) => m.status === "pending");
  const pendingLinks = (appState.data.graphLinks || []).filter((l) => l.status === "pending");

  const pendingWorkspaceItems = [];
  appState.data.subprojects.forEach((sp) => {
    if (!sp.workspace) return;
    (sp.workspace.hypotheses || []).forEach((h) => {
      if (h.approvalStatus === "pending") {
        pendingWorkspaceItems.push({
          spId: sp.id,
          spTitle: sp.title,
          collection: "hypotheses",
          typeLabel: "Hipoteza badawcza",
          id: h.id,
          text: h.statement,
          author: h.author
        });
      }
    });
    (sp.workspace.notes || []).forEach((n) => {
      if (n.approvalStatus === "pending") {
        pendingWorkspaceItems.push({
          spId: sp.id,
          spTitle: sp.title,
          collection: "notes",
          typeLabel: "Notatka laboratoryjna",
          id: n.id,
          text: `${n.title}: ${n.content}`,
          author: n.author
        });
      }
    });
    (sp.workspace.bibliography || []).forEach((b) => {
      if (b.approvalStatus === "pending") {
        pendingWorkspaceItems.push({
          spId: sp.id,
          spTitle: sp.title,
          collection: "bibliography",
          typeLabel: "Źródło bibliograficzne",
          id: b.id,
          text: b.citation,
          author: b.addedBy
        });
      }
    });
  });

  if (!appState.isAdmin) {
    container.innerHTML = `
      <div class="ws-card" style="max-width:560px; margin:2rem auto; padding:2rem; text-align:center;">
        <h3 style="margin-bottom:0.5rem;">Wymagana autoryzacja Administratora</h3>
        <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:1.25rem;">
          Jako zewnętrzny obserwator (Gość) możesz swobodnie zgłaszać nowe materiały, inicjować podprojekty i uruchamiać środowiska badawcze. Aby zatwierdzać zgłoszenia gości do widoku publicznego, zaloguj się jako Administrator.
        </p>
        <button class="btn btn-primary" onclick="openAdminLoginModal()">Zaloguj jako Administrator</button>
      </div>
    `;
    return;
  }

  const totalPending =
    pendingSubprojects.length +
    pendingMaterials.length +
    pendingWorkspaceItems.length +
    pendingLinks.length;

  container.innerHTML = `
    <div class="filter-bar">
      <div>
        <h3 style="font-size:1.1rem;">Kolejka autoryzacji zgłoszeń gości (${totalPending})</h3>
        <p style="font-size:0.82rem; color:var(--text-muted);">Zatwierdzaj lub odrzucaj materiały, podprojekty i wpisy badawcze nadesłane przez zewnętrznych obserwatorów.</p>
      </div>
      <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
        ${
          totalPending > 0
            ? `<button class="btn btn-success" onclick="approveAllPending()">✓ Zatwierdź wszystkie oczekujące (${totalPending})</button>`
            : ""
        }
        <button class="btn" onclick="exportDatabaseJson()">⬇ Eksportuj bazę JSON</button>
        <button class="btn" onclick="resetToDefaultSeed()">↺ Przywróć stan początkowy</button>
      </div>
    </div>

    <div class="workspace-grid">
      <div class="ws-section">
        <h4>Oczekujące podprojekty i środowiska (${pendingSubprojects.length})</h4>
        ${
          pendingSubprojects.length === 0
            ? `<p style="font-size:0.82rem; color:var(--text-muted);">Brak oczekujących podprojektów.</p>`
            : pendingSubprojects
                .map(
                  (sp) => `
              <div class="ws-card">
                <div style="font-size:0.75rem; color:var(--accent-blue); font-weight:700;">Projekt ${escapeHtml(sp.trackId)} • ${escapeHtml(sp.branchTopic)}</div>
                <strong style="font-size:0.95rem;">${escapeHtml(sp.title)}</strong>
                <p style="font-size:0.83rem; color:var(--text-secondary); margin:0.35rem 0;">${escapeHtml(sp.description)}</p>
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.76rem; color:var(--text-muted);">
                  <span>Zgłosił(a): ${escapeHtml(sp.author)}</span>
                  <div style="display:flex; gap:0.4rem;">
                    <button class="btn btn-sm btn-success" onclick="moderateItem('subproject', '${sp.id}', 'approve')">✓ Zatwierdź</button>
                    <button class="btn btn-sm btn-danger" onclick="moderateItem('subproject', '${sp.id}', 'delete')">✕ Odrzuć</button>
                  </div>
                </div>
              </div>
            `
                )
                .join("")
        }
      </div>

      <div class="ws-section">
        <h4>Oczekujące materiały badawcze (${pendingMaterials.length})</h4>
        ${
          pendingMaterials.length === 0
            ? `<p style="font-size:0.82rem; color:var(--text-muted);">Brak oczekujących materiałów.</p>`
            : pendingMaterials
                .map(
                  (m) => `
              <div class="ws-card">
                <div style="font-size:0.75rem; color:var(--accent-blue); font-weight:700;">Projekt ${escapeHtml(m.trackId)} • ${escapeHtml(m.type)}</div>
                <strong style="font-size:0.95rem;">${escapeHtml(m.title)}</strong>
                <p style="font-size:0.83rem; color:var(--text-secondary); margin:0.35rem 0;">${escapeHtml(m.content)}</p>
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.76rem; color:var(--text-muted);">
                  <span>Zgłosił(a): ${escapeHtml(m.author)}</span>
                  <div style="display:flex; gap:0.4rem;">
                    <button class="btn btn-sm btn-success" onclick="moderateItem('material', '${m.id}', 'approve')">✓ Zatwierdź</button>
                    <button class="btn btn-sm btn-danger" onclick="moderateItem('material', '${m.id}', 'delete')">✕ Odrzuć</button>
                  </div>
                </div>
              </div>
            `
                )
                .join("")
        }
      </div>

      <div class="ws-section">
        <h4>Wpisy w środowiskach i powiązania (${pendingWorkspaceItems.length + pendingLinks.length})</h4>
        ${
          pendingWorkspaceItems.length === 0 && pendingLinks.length === 0
            ? `<p style="font-size:0.82rem; color:var(--text-muted);">Brak oczekujących wpisów w środowiskach badawczych.</p>`
            : ""
        }
        ${pendingWorkspaceItems
          .map(
            (item) => `
          <div class="ws-card">
            <div style="font-size:0.74rem; color:var(--warning); font-weight:700;">${escapeHtml(item.typeLabel)} w: ${escapeHtml(item.spTitle)}</div>
            <p style="margin:0.3rem 0;">${escapeHtml(item.text)}</p>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem; color:var(--text-muted);">
              <span>Autor: ${escapeHtml(item.author)}</span>
              <div style="display:flex; gap:0.35rem;">
                <button class="btn btn-sm btn-success" onclick="moderateWorkspaceEntry('${item.spId}', '${item.collection}', '${item.id}', 'approve')">✓ Zatwierdź</button>
                <button class="btn btn-sm btn-danger" onclick="moderateWorkspaceEntry('${item.spId}', '${item.collection}', '${item.id}', 'delete')">✕ Odrzuć</button>
              </div>
            </div>
          </div>
        `
          )
          .join("")}
        ${pendingLinks
          .map(
            (l) => `
          <div class="ws-card">
            <div style="font-size:0.74rem; color:var(--accent-blue); font-weight:700;">Powiązanie grafu: Projekt ${escapeHtml(l.source)} ↔ Projekt ${escapeHtml(l.target)}</div>
            <p style="margin:0.3rem 0;">${escapeHtml(l.label)}</p>
            <div style="display:flex; justify-content:flex-end; gap:0.35rem;">
              <button class="btn btn-sm btn-success" onclick="moderateGraphLink('${l.id}', 'approve')">✓ Zatwierdź</button>
              <button class="btn btn-sm btn-danger" onclick="moderateGraphLink('${l.id}', 'delete')">✕ Odrzuć</button>
            </div>
          </div>
        `
          )
          .join("")}
      </div>
    </div>
  `;
}

// --- Akcje moderacji i zarządzania ---
function moderateItem(itemType, id, action) {
  if (!appState.isAdmin) return;
  if (itemType === "subproject") {
    if (action === "approve") {
      const sp = appState.data.subprojects.find((s) => s.id === id);
      if (sp) sp.status = "approved";
      saveState("Podprojekt i środowisko badawcze zostały zatwierdzone.");
    } else if (action === "delete") {
      appState.data.subprojects = appState.data.subprojects.filter((s) => s.id !== id);
      saveState("Podprojekt został usunięty.");
    }
  } else if (itemType === "material") {
    if (action === "approve") {
      const m = appState.data.materials.find((x) => x.id === id);
      if (m) m.status = "approved";
      saveState("Materiał badawczy został zatwierdzony i opublikowany.");
    } else if (action === "delete") {
      appState.data.materials = appState.data.materials.filter((x) => x.id !== id);
      saveState("Materiał został usunięty.");
    }
  }
}

function moderateWorkspaceEntry(spId, collection, entryId, action) {
  if (!appState.isAdmin) return;
  const sp = appState.data.subprojects.find((s) => s.id === spId);
  if (!sp || !sp.workspace || !sp.workspace[collection]) return;

  if (action === "approve") {
    const entry = sp.workspace[collection].find((e) => e.id === entryId);
    if (entry) entry.approvalStatus = "approved";
    saveState("Wpis w środowisku badawczym został zatwierdzony.");
  } else if (action === "delete") {
    sp.workspace[collection] = sp.workspace[collection].filter((e) => e.id !== entryId);
    saveState("Wpis został usunięty.");
  }
}

function moderateGraphLink(linkId, action) {
  if (!appState.isAdmin) return;
  if (action === "approve") {
    const lnk = appState.data.graphLinks.find((l) => l.id === linkId);
    if (lnk) lnk.status = "approved";
    saveState("Powiązanie międzyścieżkowe zatwierdzone.");
  } else if (action === "delete") {
    appState.data.graphLinks = appState.data.graphLinks.filter((l) => l.id !== linkId);
    saveState("Powiązanie zostało usunięte.");
  }
}

function approveAllPending() {
  if (!appState.isAdmin) return;
  appState.data.subprojects.forEach((sp) => {
    sp.status = "approved";
    if (sp.workspace) {
      (sp.workspace.hypotheses || []).forEach((h) => (h.approvalStatus = "approved"));
      (sp.workspace.notes || []).forEach((n) => (n.approvalStatus = "approved"));
      (sp.workspace.bibliography || []).forEach((b) => (b.approvalStatus = "approved"));
    }
  });
  appState.data.materials.forEach((m) => (m.status = "approved"));
  (appState.data.graphLinks || []).forEach((l) => (l.status = "approved"));
  saveState("Wszystkie oczekujące zgłoszenia zostały zatwierdzone!");
}

// --- Modale i formularze ---
function closeModal() {
  document.getElementById("modalBackdrop").classList.remove("open");
}

function getAllBranchesForTrack(trackId) {
  const tr = getTrackById(trackId);
  if (!tr || !tr.sections) return [];
  const items = [];
  tr.sections.forEach((s) => {
    (s.items || []).forEach((i) => items.push(i));
  });
  return items;
}

function openNewSubprojectModal(defaultTrackId = "A", defaultBranch = "") {
  const modalBody = document.getElementById("modalContentBox");
  const branches = getAllBranchesForTrack(defaultTrackId);

  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🚀 Nowy podprojekt i środowisko badawcze</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewSubproject(event)">
      <div class="form-group">
        <label>Główna ścieżka projektu (A–G)</label>
        <select id="spTrackSelect" class="select-field" onchange="updateBranchOptionsForModal(this.value)" required>
          ${appState.data.tracks
            .map(
              (t) =>
                `<option value="${t.id}" ${t.id === defaultTrackId ? "selected" : ""}>${escapeHtml(t.code)} — ${escapeHtml(t.name)}</option>`
            )
            .join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Odnoga zakresu badawczego (wybierz z listy lub wpisz własną)</label>
        <input list="branchSuggestions" id="spBranchInput" class="input-field" value="${escapeHtml(defaultBranch)}" placeholder="Wybierz lub wpisz odnogę badawczą..." required />
        <datalist id="branchSuggestions">
          ${branches.map((b) => `<option value="${escapeHtml(b)}"></option>`).join("")}
        </datalist>
      </div>
      <div class="form-group">
        <label>Tytuł podprojektu / środowiska badawczego</label>
        <input type="text" id="spTitleInput" class="input-field" placeholder="np. Biohybrydowe rusztowania naczyniowe w warunkach mikrograwitacji" required />
      </div>
      <div class="form-group">
        <label>Powiązane ścieżki dodatkowe (opcjonalnie)</label>
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; margin-top:0.25rem;">
          ${appState.data.tracks
            .map(
              (t) => `
            <label style="display:inline-flex; align-items:center; gap:0.3rem; font-weight:400; font-size:0.82rem;">
              <input type="checkbox" name="spSecondary" value="${t.id}" ${t.id === "E" ? "checked" : ""} />
              ${escapeHtml(t.code)}
            </label>
          `
            )
            .join("")}
        </div>
      </div>
      <div class="form-group">
        <label>Cel i opis problemu badawczego</label>
        <textarea id="spDescInput" class="textarea-field" rows="3" placeholder="Opisz cel środowiska badawczego, metodologię oraz powiązanie z podstawami naukowymi..." required></textarea>
      </div>
      <div class="form-group">
        <label>Hipoteza startowa (automatycznie inicjuje moduł hipotez w środowisku)</label>
        <input type="text" id="spInitialHypothesis" class="input-field" placeholder="np. Zastosowanie struktur biomimetycznych zwiększa przeżywalność komórek o..." />
      </div>
      <div class="form-group">
        <label>Nakładka filozoficzna / epistemologiczna (Projekt E — opcjonalnie)</label>
        <input type="text" id="spPhilInput" class="input-field" placeholder="Jakie pytania o granice poznania lub etykę rodzi ten podprojekt?" />
      </div>
      <div class="form-group">
        <label>Autor / Inicjator</label>
        <input type="text" id="spAuthorInput" class="input-field" value="${appState.isAdmin ? "Administrator" : "Obserwator zewnętrzny (Gość)"}" required />
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1.25rem;">
        <span style="font-size:0.78rem; color:var(--text-muted);">
          ${
            appState.isAdmin
              ? "✓ Jako Administrator od razu publikujesz środowisko."
              : "ℹ️ Jako Gość uruchomisz środowisko od razu; trafi ono również do akceptacji Administratora."
          }
        </span>
        <button type="submit" class="btn btn-primary">Uruchom środowisko badawcze</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function updateBranchOptionsForModal(trackId) {
  const dl = document.getElementById("branchSuggestions");
  if (!dl) return;
  const branches = getAllBranchesForTrack(trackId);
  dl.innerHTML = branches.map((b) => `<option value="${escapeHtml(b)}"></option>`).join("");
}

function submitNewSubproject(e) {
  e.preventDefault();
  const trackId = document.getElementById("spTrackSelect").value;
  const branchTopic = document.getElementById("spBranchInput").value.trim();
  const title = document.getElementById("spTitleInput").value.trim();
  const description = document.getElementById("spDescInput").value.trim();
  const initialHyp = document.getElementById("spInitialHypothesis").value.trim();
  const philosophicalNote = document.getElementById("spPhilInput").value.trim();
  const author = document.getElementById("spAuthorInput").value.trim();

  const secondaryTracks = Array.from(
    document.querySelectorAll('input[name="spSecondary"]:checked')
  )
    .map((cb) => cb.value)
    .filter((v) => v !== trackId);

  const newId = "sub-" + Date.now();
  const approval = appState.isAdmin ? "approved" : "pending";

  const newSp = {
    id: newId,
    trackId,
    secondaryTracks,
    branchTopic,
    title,
    author,
    status: approval,
    isSessionCreated: true,
    createdAt: new Date().toISOString(),
    description,
    philosophicalNote,
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
  };

  appState.data.subprojects.unshift(newSp);
  appState.selectedTrackFilter = "ALL";
  appState.selectedSubprojectId = newId;
  closeModal();
  switchTab("workspaces");
  saveState(
    appState.isAdmin
      ? "Nowe środowisko badawcze zostało utworzone i zatwierdzone."
      : "Środowisko badawcze zostało uruchomione i przesłane do autoryzacji Administratora!"
  );
}

function openNewMaterialModal(defaultTrackId = "A", defaultBranch = "", defaultSubprojectId = "") {
  const modalBody = document.getElementById("modalContentBox");
  const branches = getAllBranchesForTrack(defaultTrackId);

  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>📚 Dodaj materiał badawczy</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewMaterial(event)">
      <div class="form-group">
        <label>Ścieżka projektu (A–G)</label>
        <select id="matTrackSelect" class="select-field" onchange="updateBranchOptionsForModal(this.value)" required>
          ${appState.data.tracks
            .map(
              (t) =>
                `<option value="${t.id}" ${t.id === defaultTrackId ? "selected" : ""}>${escapeHtml(t.code)} — ${escapeHtml(t.name)}</option>`
            )
            .join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Odnoga badawcza (opcjonalnie)</label>
        <input list="branchSuggestions" id="matBranchInput" class="input-field" value="${escapeHtml(defaultBranch)}" placeholder="Wskaż odnogę zakresu..." />
        <datalist id="branchSuggestions">
          ${branches.map((b) => `<option value="${escapeHtml(b)}"></option>`).join("")}
        </datalist>
      </div>
      <div class="form-group">
        <label>Przypisz do istniejącego podprojektu / środowiska (opcjonalnie)</label>
        <select id="matSubprojectSelect" class="select-field">
          <option value="">-- Ogólny materiał dla ścieżki --</option>
          ${appState.data.subprojects
            .map(
              (s) =>
                `<option value="${s.id}" ${s.id === defaultSubprojectId ? "selected" : ""}>[${s.trackId}] ${escapeHtml(s.title)}</option>`
            )
            .join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Typ materiału</label>
        <select id="matTypeSelect" class="select-field">
          <option value="Artykuł / Opracowanie naukowe">Artykuł / Opracowanie naukowe</option>
          <option value="Zestaw danych / Pomiary">Zestaw danych / Pomiary</option>
          <option value="Model matematyczny / Symulacja">Model matematyczny / Symulacja</option>
          <option value="Analiza filozoficzna / Bioetyczna">Analiza filozoficzna / Bioetyczna</option>
          <option value="Bibliografia / Źródło zewnętrzne">Bibliografia / Źródło zewnętrzne</option>
        </select>
      </div>
      <div class="form-group">
        <label>Tytuł materiału</label>
        <input type="text" id="matTitleInput" class="input-field" placeholder="Wpisz tytuł materiału badawczego..." required />
      </div>
      <div class="form-group">
        <label>Treść / Abstrakt / Wnioski badawcze</label>
        <textarea id="matContentInput" class="textarea-field" rows="4" placeholder="Opisz zawartość materiału, główne tezy lub dane..." required></textarea>
      </div>
      <div class="form-group">
        <label>Link zewnętrzny / DOI (opcjonalnie)</label>
        <input type="url" id="matUrlInput" class="input-field" placeholder="https://doi.org/..." />
      </div>
      <div class="form-group">
        <label>Autor zgłoszenia</label>
        <input type="text" id="matAuthorInput" class="input-field" value="${appState.isAdmin ? "Administrator" : "Gość / Obserwator zewnętrzny"}" required />
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1.25rem;">
        <span style="font-size:0.78rem; color:var(--text-muted);">
          ${
            appState.isAdmin
              ? "✓ Publikacja natychmiastowa (Tryb Administratora)."
              : "ℹ️ Materiał zostanie zapisany ze statusem „Oczekuje na zgodę Administratora”."
          }
        </span>
        <button type="submit" class="btn btn-primary">Zapisz materiał</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitNewMaterial(e) {
  e.preventDefault();
  const trackId = document.getElementById("matTrackSelect").value;
  const branchTopic = document.getElementById("matBranchInput").value.trim();
  const subprojectId = document.getElementById("matSubprojectSelect").value || null;
  const type = document.getElementById("matTypeSelect").value;
  const title = document.getElementById("matTitleInput").value.trim();
  const content = document.getElementById("matContentInput").value.trim();
  const url = document.getElementById("matUrlInput").value.trim();
  const author = document.getElementById("matAuthorInput").value.trim();

  const newMat = {
    id: "mat-" + Date.now(),
    trackId,
    branchTopic,
    subprojectId,
    title,
    type,
    author,
    content,
    url,
    status: appState.isAdmin ? "approved" : "pending",
    isSessionCreated: true,
    createdAt: new Date().toISOString()
  };

  appState.data.materials.unshift(newMat);
  closeModal();
  saveState(
    appState.isAdmin
      ? "Materiał badawczy został opublikowany."
      : "Materiał został dodany i oczekuje na zatwierdzenie przez Administratora."
  );
}

function openWorkspaceEntryModal(entryType, spId) {
  const modalBody = document.getElementById("modalContentBox");
  const titles = {
    hypothesis: "🔬 Dodaj hipotezę badawczą do środowiska",
    note: "📝 Dodaj notatkę laboratoryjną / badawczą",
    bibliography: "📖 Dodaj pozycję bibliograficzną"
  };

  let fieldsHtml = "";
  if (entryType === "hypothesis") {
    fieldsHtml = `
      <div class="form-group">
        <label>Treść hipotezy badawczej</label>
        <textarea id="wsEntryText" class="textarea-field" rows="3" placeholder="Sformułuj weryfikowalną hipotezę..." required></textarea>
      </div>
      <div class="form-group">
        <label>Status weryfikacji</label>
        <select id="wsEntryStatus" class="select-field">
          <option value="Hipoteza otwarta">Hipoteza otwarta</option>
          <option value="W weryfikacji">W weryfikacji</option>
          <option value="Potwierdzona częściowo">Potwierdzona częściowo</option>
          <option value="Wymaga korekty">Wymaga korekty</option>
        </select>
      </div>
    `;
  } else if (entryType === "note") {
    fieldsHtml = `
      <div class="form-group">
        <label>Tytuł notatki / obserwacji</label>
        <input type="text" id="wsEntryTitle" class="input-field" placeholder="np. Analiza stabilności pętli sprzężenia" required />
      </div>
      <div class="form-group">
        <label>Treść notatki badawczej</label>
        <textarea id="wsEntryText" class="textarea-field" rows="4" placeholder="Zapisz wyniki, równania, obserwacje lub pytania..." required></textarea>
      </div>
    `;
  } else {
    fieldsHtml = `
      <div class="form-group">
        <label>Cytowanie (Autor, Rok, Tytuł, Czasopismo / Wydawca)</label>
        <textarea id="wsEntryText" class="textarea-field" rows="2" placeholder="np. Penrose, R. (2004). The Road to Reality..." required></textarea>
      </div>
      <div class="form-group">
        <label>Link / DOI (opcjonalnie)</label>
        <input type="url" id="wsEntryUrl" class="input-field" placeholder="https://doi.org/..." />
      </div>
    `;
  }

  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>${titles[entryType]}</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitWorkspaceEntry(event, '${entryType}', '${spId}')">
      ${fieldsHtml}
      <div class="form-group">
        <label>Autor wpisu</label>
        <input type="text" id="wsEntryAuthor" class="input-field" value="${appState.isAdmin ? "Administrator" : "Gość / Obserwator"}" required />
      </div>
      <div style="display:flex; justify-content:flex-end; margin-top:1rem;">
        <button type="submit" class="btn btn-primary">Dodaj do środowiska</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitWorkspaceEntry(e, entryType, spId) {
  e.preventDefault();
  const sp = appState.data.subprojects.find((s) => s.id === spId);
  if (!sp) return;
  if (!sp.workspace) sp.workspace = { hypotheses: [], notes: [], bibliography: [] };

  const author = document.getElementById("wsEntryAuthor").value.trim();
  const approvalStatus = appState.isAdmin ? "approved" : "pending";

  if (entryType === "hypothesis") {
    sp.workspace.hypotheses.push({
      id: "hyp-" + Date.now(),
      statement: document.getElementById("wsEntryText").value.trim(),
      status: document.getElementById("wsEntryStatus").value,
      author,
      approvalStatus,
      isSessionCreated: true
    });
  } else if (entryType === "note") {
    sp.workspace.notes.push({
      id: "note-" + Date.now(),
      title: document.getElementById("wsEntryTitle").value.trim(),
      content: document.getElementById("wsEntryText").value.trim(),
      author,
      createdAt: new Date().toISOString(),
      approvalStatus,
      isSessionCreated: true
    });
  } else if (entryType === "bibliography") {
    sp.workspace.bibliography.push({
      id: "bib-" + Date.now(),
      citation: document.getElementById("wsEntryText").value.trim(),
      url: document.getElementById("wsEntryUrl").value.trim(),
      addedBy: author,
      approvalStatus,
      isSessionCreated: true
    });
  }

  closeModal();
  saveState(
    appState.isAdmin
      ? "Wpis został dodany do środowiska badawczego."
      : "Wpis został dodany do środowiska i oczekuje na zatwierdzenie przez Administratora."
  );
}

function openNewGraphLinkModal() {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🔗 Nowe powiązanie międzyścieżkowe (A–G)</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitNewGraphLink(event)">
      <div class="form-group">
        <label>Ścieżka źródłowa</label>
        <select id="lnkSource" class="select-field">
          ${appState.data.tracks.map((t) => `<option value="${t.id}">${escapeHtml(t.code)} — ${escapeHtml(t.name)}</option>`).join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Ścieżka docelowa</label>
        <select id="lnkTarget" class="select-field">
          ${appState.data.tracks.map((t, i) => `<option value="${t.id}" ${i === 1 ? "selected" : ""}>${escapeHtml(t.code)} — ${escapeHtml(t.name)}</option>`).join("")}
        </select>
      </div>
      <div class="form-group">
        <label>Opis powiązania badawczego</label>
        <input type="text" id="lnkLabel" class="input-field" placeholder="np. Bioelektroniczne czujniki środowiskowe i monitoring ekosystemów" required />
      </div>
      <div style="display:flex; justify-content:flex-end; margin-top:1rem;">
        <button type="submit" class="btn btn-primary">Dodaj powiązanie</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitNewGraphLink(e) {
  e.preventDefault();
  const source = document.getElementById("lnkSource").value;
  const target = document.getElementById("lnkTarget").value;
  const label = document.getElementById("lnkLabel").value.trim();

  if (source === target) {
    showToast("Wybierz dwie różne ścieżki badawcze.");
    return;
  }

  appState.data.graphLinks.push({
    id: "lnk-" + Date.now(),
    source,
    target,
    label,
    status: appState.isAdmin ? "approved" : "pending",
    isSessionCreated: true
  });

  closeModal();
  saveState("Dodano powiązanie międzyścieżkowe.");
}

// --- Logowanie Administratora ---
function toggleAdminMode() {
  if (appState.isAdmin) {
    appState.isAdmin = false;
    sessionStorage.removeItem("golem_xv_is_admin");
    showToast("Przełączono na tryb Gościa / Obserwatora zewnętrznego.");
    renderAll();
  } else {
    openAdminLoginModal();
  }
}

function openAdminLoginModal() {
  const modalBody = document.getElementById("modalContentBox");
  modalBody.innerHTML = `
    <div class="modal-header">
      <h3>🔐 Autoryzacja Administratora projektu</h3>
      <button class="btn btn-sm" onclick="closeModal()">✕</button>
    </div>
    <form onsubmit="submitAdminLogin(event)">
      <p style="font-size:0.86rem; color:var(--text-secondary); margin-bottom:1rem;">
        Wprowadź hasło administratora, aby zatwierdzać materiały dodawane przez gości oraz zarządzać środowiskami badawczymi.<br/>
        <span style="color:var(--text-muted); font-size:0.8rem;">(Domyślne hasło wdrożeniowe: <code>golem15</code>)</span>
      </p>
      <div class="form-group">
        <label>Hasło Administratora</label>
        <input type="password" id="adminPassInput" class="input-field" value="golem15" required autofocus />
      </div>
      <div style="display:flex; justify-content:flex-end; gap:0.5rem; margin-top:1rem;">
        <button type="button" class="btn" onclick="closeModal()">Anuluj</button>
        <button type="submit" class="btn btn-primary">Odblokuj panel Administratora</button>
      </div>
    </form>
  `;
  document.getElementById("modalBackdrop").classList.add("open");
}

function submitAdminLogin(e) {
  e.preventDefault();
  const inputPass = document.getElementById("adminPassInput").value;
  const savedPass = localStorage.getItem(ADMIN_PASS_KEY) || "golem15";

  if (inputPass === savedPass) {
    appState.isAdmin = true;
    sessionStorage.setItem("golem_xv_is_admin", "true");
    closeModal();
    showToast("Zalogowano jako Administrator projektu Golem XV.");
    renderAll();
  } else {
    showToast("Nieprawidłowe hasło administratora!");
  }
}

function exportDatabaseJson() {
  const blob = new Blob([JSON.stringify(appState.data, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "golem_xv_baza_badawcza.json";
  a.click();
  URL.revokeObjectURL(url);
}

function resetToDefaultSeed() {
  if (!confirm("Czy na pewno chcesz przywrócić początkowy stan bazy badawczej Golem XV?")) return;
  appState.data = JSON.parse(JSON.stringify(DEFAULT_SEED));
  saveState("Przywrócono stan początkowy bazy projektu.");
}

window.addEventListener("DOMContentLoaded", initApp);
