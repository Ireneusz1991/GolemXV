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
DEFAULT_SEED = {'projectMeta': {'title': "The Golem 15: A Human's Road to Reality",
                 'subtitle': 'Mapa projektu badawczego — wspólne podstawy naukowe (1–8), siedem ścieżek (A–G) oraz '
                             'Super-Projekt H (Energetyka jądrowa i termojądrowa)',
                 'adminAuth': {'algorithm': 'pbkdf2_sha256',
                               'iterations': 260000,
                               'salt': '9f4d8a2c6e1b3f7a5c8d0e2f4a6b8c1d',
                               'hash': '673a07dbc15ac855752d7c521ffc31e200302b03a3b296310b742421cbfd4d62'},
                 'overarchingGoal': 'Zrozumieć człowieka jako organizm biologiczny, umysł, twórcę technologii i część '
                                    'ziemskiej biosfery, a jednocześnie zbadać możliwości jego funkcjonowania poza '
                                    'naturalnym środowiskiem Ziemi.',
                 'organizationalRule': 'Każda ścieżka ma własne pytania badawcze, bibliografię i cele. Wspólne '
                                       'podstawy naukowe pozwalają łączyć wiedzę, ale nie oznaczają konieczności '
                                       'równoległego studiowania wszystkich dziedzin. Filozofia pozostaje przekrojową '
                                       'warstwą interpretacyjną. Pozostałe projekty rozwijają się w miarę dostępnego '
                                       'czasu i zainteresowania.',
                 'foundations': ['Matematyka i logika',
                                 'Informatyka',
                                 'Programowanie',
                                 'Fizyka',
                                 'Elektronika',
                                 'Chemia',
                                 'Biologia',
                                 'Sztuczna inteligencja'],
                 'fgRelation': {'summary': 'Oba projekty badają człowieka w relacji ze środowiskiem, ale z różnych '
                                           'perspektyw:',
                                'fPerspective': 'Projekt F — kosmos: jak stworzyć sztuczne środowisko podtrzymujące '
                                                'życie tam, gdzie naturalne warunki są dla człowieka nieprzyjazne. '
                                                'Koncentruje się na inżynierii środowiska i adaptacji do warunków '
                                                'pozaziemskich.',
                                'gPerspective': 'Projekt G — Ziemia: jak żyć w istniejącym, złożonym ekosystemie i '
                                                'chronić jego zdolność do podtrzymywania życia. Koncentruje się na '
                                                'ekologii, zdrowiu człowieka, zrównoważonej technologii i ochronie '
                                                'biosfery.'}},
 'foundationDisciplines': [{'id': 'FND-1',
                            'order': 1,
                            'name': 'Matematyka i logika',
                            'icon': '📐',
                            'color': '#38bdf8',
                            'description': 'Formalny język opisu rzeczywistości, wnioskowania dedukcyjnego, układów '
                                           'dynamicznych, prawdopodobieństwa i informacji.',
                            'topics': ['Logika formalna, rachunek zdań i kwantyfikatorów, teoria mnogości i '
                                       'dowodzenia.',
                                       'Analiza matematyczna, rachunek różniczkowy i całkowy, równania różniczkowe '
                                       'zwyczajne i cząstkowe.',
                                       'Algebra liniowa, przestrzenie wektorowe, tensory i metody spektralne.',
                                       'Rachunek prawdopodobieństwa, statystyka matematyczna i wnioskowanie '
                                       'bayesowskie.',
                                       'Teoria informacji, entropia Shannona, teoria układów dynamicznych i chaosu.',
                                       'Matematyka dyskretna, teoria grafów i topologia sieci (podstawa konektomiki i '
                                       'sieci złożonych).'],
                            'connectedTracks': ['A', 'B', 'C', 'E', 'F', 'G', 'H']},
                           {'id': 'FND-2',
                            'order': 2,
                            'name': 'Informatyka',
                            'icon': '💻',
                            'color': '#60a5fa',
                            'description': 'Teoria obliczeń, architektura systemów komputerowych, struktury danych, '
                                           'przetwarzanie informacji i cyberbezpieczeństwo.',
                            'topics': ['Teoria obliczeń, maszyny Turinga, obliczalność i złożoność obliczeniowa.',
                                       'Algorytmy i struktury danych (grafowe, drzewiaste, probabilistyczne, '
                                       'indeksowanie).',
                                       'Architektura komputerów (CPU, GPU, pamięci, systemy wbudowane i czasu '
                                       'rzeczywistego).',
                                       'Systemy operacyjne, współbieżność, systemy rozproszone i obliczenia wysokiej '
                                       'wydajności (HPC).',
                                       'Bazy danych, reprezentacja wiedzy, ontologie i przetwarzanie wielkich zbiorów '
                                       'danych.',
                                       'Niezawodność systemów (fault-tolerance) w zastosowaniach medycznych i '
                                       'kosmicznych.'],
                            'connectedTracks': ['A', 'B', 'C', 'F', 'G', 'H']},
                           {'id': 'FND-3',
                            'order': 3,
                            'name': 'Programowanie',
                            'icon': '⌨️',
                            'color': '#818cf8',
                            'description': 'Praktyczna konstrukcja oprogramowania, symulacji numerycznych, modeli '
                                           'badawczych, sterowników sprzętowych i narzędzi analitycznych.',
                            'topics': ['Paradygmaty programowania: imperatywne, obiektowe, funkcyjne i reaktywne.',
                                       'Python w obliczeniach naukowych i analizie danych (NumPy, SciPy, PyTorch, '
                                       'BioPython).',
                                       'Języki niskopoziomowe i systemowe (C, C++, Rust) do sterowania robotami, '
                                       'mikrokontrolerami i BCI.',
                                       'Symulacje numeryczne układów fizycznych, biologicznych i neuronalnych (np. '
                                       'Brian2, NEURON).',
                                       'Inżynieria oprogramowania, kontrola wersji, testy automatyczne i '
                                       'reprodukowalność badań.',
                                       'Wizualizacja danych naukowych, interfejsy webowe i wirtualne środowiska '
                                       'badawcze.'],
                            'connectedTracks': ['A', 'B', 'C', 'D', 'F', 'G', 'H']},
                           {'id': 'FND-4',
                            'order': 4,
                            'name': 'Fizyka',
                            'icon': '⚛️',
                            'color': '#f59e0b',
                            'description': 'Fundamentalne prawa przyrody rządzące materią, energią, polami, '
                                           'termodynamiką układów żywych, obliczaniem fizycznym i astronautyką.',
                            'topics': ['Mechanika klasyczna, analityczna (Lagrange’a i Hamiltona), biomechanika oraz '
                                       'mechanika orbitalna.',
                                       'Termodynamika klasyczna i nierównowagowa, fizyka statystyczna i entropia w '
                                       'układach żywych.',
                                       'Elektrodynamika, fale elektromagnetyczne, optyka i oddziaływanie pól z tkanką '
                                       'biologiczną.',
                                       'Fizyka ciała stałego i półprzewodników (podstawa elektroniki i układów '
                                       'neuromorficznych).',
                                       'Mechanika kwantowa, fizyka jądrowa oraz promieniowanie jonizujące (ochrona '
                                       'radiacyjna w kosmosie).',
                                       'Biofizyka błon komórkowych, transportu jonowego i potencjałów czynnościowych.'],
                            'connectedTracks': ['A', 'B', 'C', 'E', 'F', 'G', 'H']},
                           {'id': 'FND-5',
                            'order': 5,
                            'name': 'Elektronika',
                            'icon': '🔌',
                            'color': '#eab308',
                            'description': 'Projektowanie układów analogowych, cyfrowych, sensorów pomiarowych, '
                                           'bioelektroniki oraz fizycznych architektur obliczeniowych.',
                            'topics': ['Teoria obwodów elektrycznych, elementy bierne i czynne, stany nieustalone.',
                                       'Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i '
                                       'układy nieliniowe.',
                                       'Elektronika cyfrowa, układy logiczne, FPGA, mikrokontrolery i systemy SoC.',
                                       'Akwizycja sygnałów biologicznych (EEG, EMG, EKG): wzmacniacze pomiarowe o '
                                       'niskim szumie i przetworniki ADC/DAC.',
                                       'Czujniki (sensory) środowiskowe i biomedyczne, aktuatory oraz systemy '
                                       'zasilania i magazynowania energii.',
                                       'Układy neuromorficzne, memrystory i realizacja sztucznych synaps w krzemie.'],
                            'connectedTracks': ['A', 'B', 'C', 'F', 'G', 'H']},
                           {'id': 'FND-6',
                            'order': 6,
                            'name': 'Chemia',
                            'icon': '🧪',
                            'color': '#10b981',
                            'description': 'Budowa cząsteczek, reakcje chemiczne, biochemia metabolizmu, inżynieria '
                                           'biomateriałów oraz zamknięte obiegi pierwiastków.',
                            'topics': ['Chemia ogólna i nieorganiczna: wiązania chemiczne, stechiometria, równowagi '
                                       'kwasowo-zasadowe i redoks.',
                                       'Chemia organiczna: grupy funkcyjne, stereochemia, synteza i reaktywność '
                                       'związków węgla.',
                                       'Biochemia: struktura i funkcja białek, enzymów, lipidów, węglowodanów oraz '
                                       'kwasów nukleinowych (DNA/RNA).',
                                       'Elektrochemia i chemia fizyczna: potencjały błonowe, ogniwa paliwowe, baterie '
                                       'i elektroliza (np. O2 w kosmosie).',
                                       'Chemia materiałów: polimery biokompatybilne, hydrożele tkankowe i materiały '
                                       'biodegradowalne.',
                                       'Chemia środowiska i analityczna: obiegi C, N, P, oczyszczanie wody, powietrza '
                                       'i neutralizacja toksyn.'],
                            'connectedTracks': ['A', 'D', 'F', 'G', 'H']},
                           {'id': 'FND-7',
                            'order': 7,
                            'name': 'Biologia',
                            'icon': '🧬',
                            'color': '#22c55e',
                            'description': 'Nauka o organizacji życia od poziomu molekularnego i komórkowego po '
                                           'fizjologię człowieka, neurobiologię, regenerację i ekologię biosfery.',
                            'topics': ['Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, '
                                       'sygnalizacja komórkowa.',
                                       'Genetyka, epigenetyka, genomika i regulacja ekspresji genów.',
                                       'Anatomia i fizjologia człowieka: układ nerwowy, krążenia, '
                                       'mięśniowo-szkieletowy, odpornościowy i hormonalny.',
                                       'Neurobiologia: budowa neuronów i gleju, transmisja synaptyczna, plastyczność '
                                       'mózgu i narządy zmysłów.',
                                       'Biologia rozwoju (embriologia), komórki macierzyste, różnicowanie tkanek i '
                                       'procesy regeneracji.',
                                       'Mikrobiologia, mikrobiom człowieka oraz ekologia populacji, ekosystemów i '
                                       'biosfery.'],
                            'connectedTracks': ['A', 'B', 'D', 'F', 'G', 'H']},
                           {'id': 'FND-8',
                            'order': 8,
                            'name': 'Sztuczna inteligencja',
                            'icon': '🤖',
                            'color': '#a855f7',
                            'description': 'Algorytmy uczenia maszynowego, głębokie sieci neuronowe, dekodowanie '
                                           'sygnałów biologicznych, autonomia robotyczna i modelowanie poznania.',
                            'topics': ['Podstawy uczenia maszynowego (nadzorowane, nienadzorowane, samonadzorowane) i '
                                       'optymalizacja gradientowa.',
                                       'Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz '
                                       'impulsowe sieci neuronowe (SNN).',
                                       'Uczenie ze wzmocnieniem (Reinforcement Learning) i sterowanie autonomicznymi '
                                       'robotami.',
                                       'Zastosowania AI w neuroinżynierii (dekodowanie BCI), diagnostyce medycznej i '
                                       'biologii strukturalnej (np. fałdowanie białek).',
                                       'Modele poznawcze, reprezentacje semantyczne a biologiczne działanie mózgu '
                                       '(porównanie AI i Projektu B).',
                                       'Interpretowalność modeli (XAI), niezawodność, bezpieczeństwo i '
                                       'filozoficzno-etyczne aspekty AI.'],
                            'connectedTracks': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']}],
 'studyMaterials': [{'id': 'smat-1',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-1',
                     'topic': 'Algebra liniowa, przestrzenie wektorowe, rachunek macierzowy i teoria operatorów.',
                     'title': 'I. Matematyka (PL → EN): Podręczniki matematyki i algebry liniowej (OpenAGH, ZPE, '
                              'Skoczylas, Penrose) oraz Gilbert Strang',
                     'level': 'Podstawowy / Akademicki (Etap 1: Najpierw)',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Podręczniki matematyki i algebry liniowej na '
                                'poziomie szkoły średniej i studiów — darmowe e-podręczniki OpenAGH (Matematyka, '
                                'Algebra liniowa, Analiza matematyczna), Zintegrowana Platforma Edukacyjna (ZPE), '
                                'Marian Gewert i Zbigniew Skoczylas („Algebra liniowa 1–2”, „Analiza matematyczna '
                                '1–2”), Tadeusz Krasiński („Algebra liniowa”) oraz Roger Penrose („Droga do '
                                'rzeczywistości”, wyd. polskie).\n'
                                '2. Uzupełniająco (Po angielsku): Gilbert Strang — „Introduction to Linear Algebra” '
                                '(MIT 18.06) oraz OpenStax Mathematics.',
                     'url': 'https://open.agh.edu.pl/',
                     'links': [{'label': '🇵🇱 OpenAGH — Darmowe polskie e-podręczniki akademickie (Matematyka, Algebra '
                                         'liniowa, Analiza)',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Matematyka i logika po polsku',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇵🇱 OpenStax Polska — Darmowe podręczniki akademickie po polsku',
                                'url': 'https://openstax.pl/pl/zasoby'},
                               {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Podręczniki algebry liniowej i analizy '
                                         'matematycznej',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT 18.06 + wykłady)',
                                'url': 'https://math.mit.edu/~gs/linearalgebra/'},
                               {'label': '🇬🇧 OpenStax Mathematics (Calculus / Linear Algebra)',
                                'url': 'https://openstax.org/subjects/math'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:00:00Z'},
                    {'id': 'smat-1b',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-2',
                     'topic': 'Architektura systemów komputerowych, systemy wbudowane, praca w czasie rzeczywistym '
                              '(RTOS) i obliczenia rozproszone.',
                     'title': 'I. Informatyka (PL → EN): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II”, '
                              'Cormen („Wprowadzenie do algorytmów”), Ważniak MIMUW',
                     'level': 'Podstawowy (Etap 1: Najpierw)',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Charles Petzold — „Kod. Ukryty język '
                                'komputerów. Wydanie II” (Helion) — fundamentalna książka wyjaśniająca od podstaw, jak '
                                'z przekaźników, bramek logicznych i tranzystorów powstaje komputer; Thomas H. Cormen '
                                'i współautorzy — „Wprowadzenie do algorytmów” (PWN); Andrew S. Tanenbaum — '
                                '„Strukturalna organizacja komputerów” (Helion); darmowe kursy akademickie Ważniak '
                                'MIMUW (Uniwersytet Warszawski) oraz ZPE Informatyka.\n'
                                '2. Uzupełniająco (Po angielsku): Charles Petzold — „Code” oraz MIT OCW 6.006.',
                     'url': 'https://wazniak.mimuw.edu.pl/',
                     'links': [{'label': '🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” (Wydawnictwo '
                                         'Helion)',
                                'url': 'https://helion.pl/'},
                               {'label': '🇵🇱 Ważniak MIMUW (Uniwersytet Warszawski) — Darmowe polskie wykłady z '
                                         'informatyki i architektury komputerów',
                                'url': 'https://wazniak.mimuw.edu.pl/'},
                               {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Informatyka i algorytmika po '
                                         'polsku',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇵🇱 T. H. Cormen et al. — „Wprowadzenie do algorytmów” (Księgarnia PWN)',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇬🇧 Charles Petzold — „Code” (Strona autora z interaktywnymi symulacjami '
                                         'bramek)',
                                'url': 'https://codehiddenlanguage.com/'},
                               {'label': '🇬🇧 MIT OCW 6.006 — Introduction to Algorithms',
                                'url': 'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:02:00Z'},
                    {'id': 'smat-1c',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-3',
                     'topic': 'Obliczenia naukowe w Pythonie (NumPy, SciPy, PyTorch, JAX) oraz symulacje numeryczne.',
                     'title': 'I. Programowanie (PL → EN): Eric Matthes — „Python. Instrukcje dla programisty”, '
                              'oficjalna polska dokumentacja Pythona i obliczenia naukowe',
                     'level': 'Podstawowy (Etap 1: Najpierw)',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Eric Matthes — „Python. Instrukcje dla '
                                'programisty. Wydanie III” (Helion) — praktyczny podręcznik programowania od podstaw z '
                                'ćwiczeniami; oficjalny polski przewodnik po języku Python (docs.python.org/pl); Wes '
                                'McKinney — „Python w analizie danych (NumPy, pandas)” (Helion); kursy programowania '
                                'Ważniak MIMUW i ZPE.\n'
                                '2. Uzupełniająco (Po angielsku): Eric Matthes — „Python Crash Course”, Scientific '
                                'Python Lectures oraz symulator sieci neuronowych Brian2.',
                     'url': 'https://docs.python.org/pl/3/tutorial/',
                     'links': [{'label': '🇵🇱 Oficjalny samouczek języka Python po polsku (docs.python.org/pl)',
                                'url': 'https://docs.python.org/pl/3/tutorial/'},
                               {'label': '🇵🇱 Eric Matthes — „Python. Instrukcje dla programisty” (Wydawnictwo Helion)',
                                'url': 'https://helion.pl/'},
                               {'label': '🇵🇱 Ważniak MIMUW — Wstęp do programowania (kurs akademicki po polsku)',
                                'url': 'https://wazniak.mimuw.edu.pl/'},
                               {'label': '🇵🇱 ZPE — Programowanie i algorytmy w języku Python (po polsku)',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇬🇧 Eric Matthes — „Python Crash Course” (Repozytorium ćwiczeń i kodu)',
                                'url': 'https://ehmatthes.github.io/pcc_3e/'},
                               {'label': '🇬🇧 Scientific Python Lectures (NumPy, SciPy, Matplotlib)',
                                'url': 'https://lectures.scientific-python.org/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:03:00Z'},
                    {'id': 'smat-2',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-4',
                     'topic': 'Mechanika klasyczna, elektrodynamika i termodynamika układów otwartych (dalekich od '
                              'równowagi).',
                     'title': 'II. Fizyka i Komputery Kwantowe (PL → EN): OpenStax „Fizyka dla szkół wyższych Tom 1–3” '
                              '(PL), Halliday & Resnick, Griffiths („Wstęp do mechaniki kwantowej”) oraz Nielsen & '
                              'Chuang',
                     'level': 'Podstawowy → Zaawansowany',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Darmowy, trzytomowy podręcznik akademicki '
                                'OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3”; David Halliday, Robert '
                                'Resnick, Jearl Walker — „Podstawy fizyki. Tom 1–5” (PWN); Richard P. Feynman — '
                                '„Feynmana wykłady z fizyki” (PWN); David J. Griffiths — „Wstęp do mechaniki '
                                'kwantowej” (polskie wydanie PWN) oraz e-podręczniki fizyki OpenAGH.\n'
                                '2. Uzupełniająco (Po angielsku — etap zaawansowany): David J. Griffiths — '
                                '„Introduction to Quantum Mechanics” oraz Michael A. Nielsen, Isaac L. Chuang — '
                                '„Quantum Computation and Quantum Information”.',
                     'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1',
                     'links': [{'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (darmowy podręcznik '
                                         'PL online/PDF)',
                                'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                               {'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 2” (Elektrodynamika, '
                                         'termodynamika — PL)',
                                'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2'},
                               {'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 3” (Optyka i fizyka '
                                         'kwantowa — PL)',
                                'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3'},
                               {'label': '🇵🇱 OpenAGH — Darmowe polskie e-podręczniki z fizyki ogólnej',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Halliday/Resnick „Podstawy fizyki” oraz '
                                         'Griffiths „Wstęp do mechaniki kwantowej”',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇬🇧 David J. Griffiths — „Introduction to Quantum Mechanics” (Cambridge '
                                         'University Press)',
                                'url': 'https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E'},
                               {'label': '🇬🇧 Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum '
                                         'Information”',
                                'url': 'https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:05:00Z'},
                    {'id': 'smat-4',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-5',
                     'topic': 'Elektronika analogowa: wzmacniacze operacyjne, filtry aktywne, oscylatory i układy '
                              'nieliniowe.',
                     'title': 'II. Elektronika (PL → EN): Horowitz & Hill („Sztuka elektroniki”), polskie kursy '
                              'Forbot, ZPE, OpenAGH oraz układy cyfrowe',
                     'level': 'Podstawowy / Zaawansowany',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Paul Horowitz, Winfield Hill — „Sztuka '
                                'elektroniki. Część 1 i 2” (polskie wydanie WKŁ); Bogdan Głocki — „Układy cyfrowe” '
                                '(WSiP); darmowe polskojęzyczne kursy podstaw elektroniki i techniki cyfrowej Forbot; '
                                'materiały Zintegrowanej Platformy Edukacyjnej (ZPE) oraz e-podręczniki elektroniki '
                                'OpenAGH.\n'
                                '2. Uzupełniająco (Po angielsku): All About Circuits Textbook oraz MIT OCW Circuits '
                                'and Electronics.',
                     'url': 'https://zpe.gov.pl/',
                     'links': [{'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika analogowa i układy '
                                         'cyfrowe po polsku',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇵🇱 Forbot — Darmowe kursy podstaw elektroniki i techniki cyfrowej po polsku',
                                'url': 'https://forbot.pl/blog/kurs-elektroniki-poziom-1-spis-tresci-id5159'},
                               {'label': '🇵🇱 OpenAGH — Polskie e-podręczniki akademickie z elektroniki i '
                                         'elektrotechniki',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Paul Horowitz, Winfield Hill — „Sztuka elektroniki” (Wydawnictwa '
                                         'Komunikacji i Łączności — WKŁ)',
                                'url': 'https://wkl.com.pl/'},
                               {'label': '🇬🇧 All About Circuits — Textbook of Analog & Digital Electronics',
                                'url': 'https://www.allaboutcircuits.com/textbook/'},
                               {'label': '🇬🇧 MIT OCW — Circuits and Electronics',
                                'url': 'https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:12:00Z'},
                    {'id': 'smat-4b',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-6',
                     'topic': 'Biochemia: struktura i funkcja białek, enzymów, lipidów oraz kwasów nukleinowych '
                              '(DNA/RNA).',
                     'title': 'III. Chemia i Biochemia (PL → EN): Stryer („Biochemia” PWN), Bielański, Jones & Atkins, '
                              'McMurry oraz OpenStax Chemistry 2e',
                     'level': 'Podstawowy / Akademicki (Etap 2: Następnie)',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Akademickie podręczniki chemii ogólnej, '
                                'organicznej i biochemii w polskich wydaniach — Jeremy M. Berg, John L. Tymoczko, '
                                'Lubert Stryer — „Biochemia” (PWN); Robert K. Murray et al. — „Biochemia Harpera” '
                                '(PZWL); Loretta Jones, Peter Atkins — „Chemia ogólna. Cząsteczki, materia, reakcje” '
                                '(PWN); Adam Bielański — „Podstawy chemii nieorganicznej” (PWN); John McMurry — '
                                '„Chemia organiczna” (PWN) oraz darmowe materiały ZPE i OpenAGH.\n'
                                '2. Uzupełniająco (Po angielsku): OpenStax „Chemistry 2e” oraz „Organic Chemistry” '
                                '(darmowe podręczniki online).',
                     'url': 'https://ksiegarnia.pwn.pl/',
                     'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — Stryer „Biochemia”, Jones & Atkins „Chemia '
                                         'ogólna”, McMurry „Chemia organiczna”',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 OpenAGH — Darmowe polskie e-podręczniki akademickie z chemii ogólnej i '
                                         'fizycznej',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Chemia ogólna, organiczna i '
                                         'biochemia po polsku',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — „Biochemia Harpera”',
                                'url': 'https://pzwl.pl/'},
                               {'label': '🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii ogólnej online/PDF',
                                'url': 'https://openstax.org/details/books/chemistry-2e'},
                               {'label': '🇬🇧 OpenStax Organic Chemistry — Darmowy podręcznik chemii organicznej',
                                'url': 'https://openstax.org/details/books/organic-chemistry'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:13:00Z'},
                    {'id': 'smat-3',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-7',
                     'topic': 'Biologia komórki i biologia molekularna: replikacja, transkrypcja, translacja, '
                              'sygnalizacja komórkowa.',
                     'title': 'III. Biologia i Genetyka (PL → EN): Terence A. Brown („Genomy” PWN), „Biologia '
                              'Campbella” (Rebis), Alberts („Podstawy biologii komórki”) oraz OpenStax Biology 2e',
                     'level': 'Podstawowy / Akademicki (Etap 2: Następnie)',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Terence A. Brown — „Genomy” (Wydawnictwo '
                                'Naukowe PWN); Neil A. Campbell i współautorzy — „Biologia Campbella” (polskie '
                                'wydanie, Dom Wydawniczy REBIS); Bruce Alberts i współautorzy — „Podstawy biologii '
                                'komórki. Część 1–2” (PWN); Piotr Węgleński (red.) — „Genetyka molekularna” (PWN) oraz '
                                'polskojęzyczne materiały ZPE.\n'
                                '2. Uzupełniająco (Po angielsku): OpenStax „Biology 2e” oraz darmowe zasoby NCBI '
                                'Bookshelf.',
                     'url': 'https://ksiegarnia.pwn.pl/',
                     'links': [{'label': '🇵🇱 Terence A. Brown — „Genomy” oraz B. Alberts — „Podstawy biologii komórki” '
                                         '(Wydawnictwo Naukowe PWN)',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)',
                                'url': 'https://www.rebis.com.pl/'},
                               {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biologia komórki i genetyka po '
                                         'polsku',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii online/PDF',
                                'url': 'https://openstax.org/details/books/biology-2e'},
                               {'label': '🇬🇧 Terence A. Brown — „Genomes” (Darmowy dostęp w bazie NCBI Bookshelf)',
                                'url': 'https://www.ncbi.nlm.nih.gov/books/NBK21128/'},
                               {'label': '🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell (Alberts)',
                                'url': 'https://www.ncbi.nlm.nih.gov/books/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:10:00Z'},
                    {'id': 'smat-5',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-8',
                     'topic': 'Głębokie sieci neuronowe (CNN, RNN, Transformery, Graph Neural Networks) oraz impulsowe '
                              'sieci neuronowe (SNN).',
                     'title': 'IV & V. Sztuczna Inteligencja (PL → EN): Aurélien Géron („Uczenie maszynowe z użyciem '
                              'Scikit-Learn i TensorFlow” PL), Goodfellow („Deep Learning” PWN) oraz Dayan & Abbott',
                     'level': 'Średniozaawansowany / Zaawansowany',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku): Aurélien Géron — „Uczenie maszynowe z użyciem '
                                'Scikit-Learn, Keras i TensorFlow. Wydanie III” (Helion); Ian Goodfellow, Yoshua '
                                'Bengio, Aaron Courville — „Deep Learning. Systemy uczące się” (polskie wydanie PWN); '
                                'Stuart Russell, Peter Norvig — „Sztuczna inteligencja. Nowe spojrzenie” (Helion) oraz '
                                'Ryszard Tadeusiewicz — „Sieci neuronowe”.\n'
                                '2. Uzupełniająco (Po angielsku): Géron — „Hands-On Machine Learning” (notebooki '
                                'GitHub) oraz Peter Dayan, L. F. Abbott — „Theoretical Neuroscience”.',
                     'url': 'https://helion.pl/',
                     'links': [{'label': '🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” '
                                         '(Wydawnictwo Helion)',
                                'url': 'https://helion.pl/'},
                               {'label': '🇵🇱 Ian Goodfellow, Yoshua Bengio, Aaron Courville — „Deep Learning. Systemy '
                                         'uczące się” (PWN)',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 OpenStax Polska — Wprowadzenie do nauki o danych i Pythonie (po polsku)',
                                'url': 'https://openstax.pl/pl/zasoby'},
                               {'label': '🇬🇧 Aurélien Géron — Hands-On Machine Learning (Oficjalne notebooki GitHub)',
                                'url': 'https://github.com/ageron/handson-ml3'},
                               {'label': '🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience (MIT Press)',
                                'url': 'https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/'},
                               {'label': '🇬🇧 Neuromatch Academy — Computational Neuroscience & Deep Learning',
                                'url': 'https://compneuro.neuromatch.io/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:15:00Z'},
                    {'id': 'smat-a1',
                     'categoryType': 'TRACK',
                     'targetId': 'A',
                     'topic': 'Medycyna regeneracyjna, protezy i sztuczne narządy.',
                     'title': 'IV. Projekt A (PL → EN): Kalat („Biologiczne podstawy psychologii”), anatomia i '
                              'fizjologia (Bochenek, Traczyk, Konturek), biofizyka, robotyka i BCI oraz OpenStax '
                              'Anatomy 2e',
                     'level': 'Podstawowy → Zaawansowany',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku):\n'
                                '• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n'
                                '• Akademickie podręczniki anatomii i fizjologii człowieka: Władysław Traczyk, Andrzej '
                                'Trzebski — „Fizjologia człowieka” (PZWL); Stanisław Konturek — „Fizjologia '
                                'człowieka”; Adam Bochenek, Michał Reicher — „Anatomia człowieka” (PZWL).\n'
                                '• Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: Feliks Jaroszyk '
                                '(red.) — „Biofizyka” (PZWL); Jan Marciniak — „Biomateriały” (Politechnika Śląska); '
                                'seria „Biocybernetyka i Inżynieria Biomedyczna 2000” (PAN, red. M. Nałęcz, R. '
                                'Tadeusiewicz).\n'
                                '• Podręczniki robotyki, elektroniki i układów sterowania (K. Tchoń i współautorzy — '
                                '„Manipulatory i roboty mobilne”; A. Géron — wyd. Helion).\n'
                                '2. Uzupełniająco (Po angielsku): OpenStax „Anatomy and Physiology 2e”, Géron '
                                '„Hands-On ML” oraz literatura z neuroprotetyki i BCI.',
                     'url': 'https://ksiegarnia.pwn.pl/',
                     'links': [{'label': '🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe '
                                         'PWN)',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia (Bochenek), Fizjologia (Traczyk) i '
                                         'Biofizyka (Jaroszyk)',
                                'url': 'https://pzwl.pl/'},
                               {'label': '🇵🇱 OpenAGH — Polskie materiały z inżynierii biomedycznej, biocybernetyki i '
                                         'automatyki',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn i TensorFlow” '
                                         '(Helion)',
                                'url': 'https://helion.pl/'},
                               {'label': '🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik anatomii i '
                                         'fizjologii)',
                                'url': 'https://openstax.org/details/books/anatomy-and-physiology-2e'},
                               {'label': '🇬🇧 MIT OCW — Introduction to Robotics & Control Systems',
                                'url': 'https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:18:00Z'},
                    {'id': 'smat-b1',
                     'categoryType': 'TRACK',
                     'targetId': 'B',
                     'topic': 'Neurobiologia i neuronauka obliczeniowa.',
                     'title': 'V. Projekt B (PL → EN): Kalat, Longstaff („Neurobiologia”), Nęcka („Psychologia '
                              'poznawcza”), Seung („Konektom”), Miłkowski & Poczobut oraz Kandel, Dayan & Abbott, '
                              'Izhikevich i Sandberg & Bostrom',
                     'level': 'Podstawowy → Zaawansowany',
                     'format': 'Biblioteka Projektu (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku):\n'
                                '• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n'
                                '• Podręczniki neurobiologii i fizjologii układu nerwowego: Alan Longstaff — '
                                '„Neurobiologia. Krótkie wykłady” (PWN); T. Górska, A. Grabowska, J. Zagrodzka (red.) '
                                '— „Mózg a zachowanie” (PWN).\n'
                                '• Podręczniki psychologii poznawczej: Edward Nęcka, Jarosław Orzechowski, Błażej '
                                'Szymura — „Psychologia poznawcza” (PWN).\n'
                                '• Wprowadzenia do filozofii umysłu, kognitywistyki i konektomiki: Marcin Miłkowski, '
                                'Robert Poczobut (red.) — „Przewodnik po filozofii umysłu” (WAM); Sebastian Seung — '
                                '„Konektom. Jak połączenia w mózgu kształtują naszą tożsamość” (wyd. polskie); wykłady '
                                'prof. Włodzisława Ducha (UMK).\n'
                                '2. Następnie i na zaawansowanym etapie (Po angielsku): Kandel („Principles of Neural '
                                'Science”), Squire („Fundamental Neuroscience”), Dayan & Abbott („Theoretical '
                                'Neuroscience”), Izhikevich („Dynamical Systems in Neuroscience”), Miller, Churchland '
                                '& Sejnowski oraz Sandberg & Bostrom („Whole Brain Emulation: A Roadmap”).',
                     'url': 'https://ksiegarnia.pwn.pl/',
                     'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — Kalat „Biologiczne podstawy psychologii”, '
                                         'Longstaff „Neurobiologia”, Nęcka „Psychologia poznawcza”',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 Prof. Włodzisław Duch (UMK) — Polskie wykłady z kognitywistyki, '
                                         'neuroinformatyki i modelowania mózgu',
                                'url': 'https://www.fizyka.umk.pl/~duch/'},
                               {'label': '🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu, '
                                         'kognitywistyka i problem świadomości (po polsku)',
                                'url': 'https://ccpress.pl/'},
                               {'label': '🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (Darmowy PDF '
                                         'książki)',
                                'url': 'https://www.izhikevich.org/publications/dsn.pdf'},
                               {'label': '🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Pełny '
                                         'raport PDF)',
                                'url': 'https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf'},
                               {'label': '🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)',
                                'url': 'https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/'},
                               {'label': '🇬🇧 Paul Miller — „An Introductory Course in Computational Neuroscience” (MIT '
                                         'Press)',
                                'url': 'https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/'},
                               {'label': '🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain” '
                                         '(MIT Press)',
                                'url': 'https://mitpress.mit.edu/9780262531207/the-computational-brain/'},
                               {'label': '🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” & Larry Squire — '
                                         '„Fundamental Neuroscience”',
                                'url': 'https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:19:00Z'},
                    {'id': 'smat-6',
                     'categoryType': 'TRACK',
                     'targetId': 'C',
                     'topic': 'Elektronika analogowa i układy dynamiczne.',
                     'title': 'Projekt C (PL → EN): Elektronika analogowa (Horowitz & Hill, OpenAGH, ZPE, Forbot), '
                              'przetworniki ADC/DAC, sieci neuronowe (Osowski, Tadeusiewicz) i Neuromorphic Computing',
                     'level': 'Podstawowy / Akademicki',
                     'format': 'Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)',
                     'content': 'Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne '
                                '→ fizyczne modele neuronów → obliczenia neuromorficzne.\n'
                                '1. W pierwszej kolejności (Po polsku): Podręczniki akademickie z elektroniki '
                                'analogowej (Paul Horowitz, Winfield Hill — „Sztuka elektroniki”; e-podręczniki '
                                'OpenAGH): wzmacniacze, oscylatory, filtry, sprzężenie zwrotne i układy dynamiczne; '
                                'materiały o przetwornikach A/C i C/A (ZPE, Forbot); Stanisław Osowski — „Sieci '
                                'neuronowe do przetwarzania informacji” (Oficyna PW) oraz Ryszard Tadeusiewicz — '
                                '„Sieci neuronowe”.\n'
                                '2. Uzupełniająco (Po angielsku): Analog computing, neuromorphic computing, analog '
                                'neural networks i fizyczne modele neuronów.',
                     'url': 'https://zpe.gov.pl/',
                     'links': [{'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C '
                                         'oraz C/A',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇵🇱 OpenAGH — Darmowe polskie e-podręczniki z elektroniki i układów '
                                         'dynamicznych',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Forbot — Praktyczne kursy elektroniki analogowej i pomiarów po polsku',
                                'url': 'https://forbot.pl/'},
                               {'label': '🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering',
                                'url': 'https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering'},
                               {'label': '🇬🇧 arXiv — Neural and Evolutionary Computing (Neuromorphic & Analog NN)',
                                'url': 'https://arxiv.org/list/cs.NE/recent'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:20:00Z'},
                    {'id': 'smat-7',
                     'categoryType': 'TRACK',
                     'targetId': 'D',
                     'topic': 'Biologia syntetyczna i edycja genomu.',
                     'title': 'Projekt D (PL → EN): Biologia komórki (Alberts), genetyka (Brown, Węgleński), '
                              'embriologia (Bartel), inżynieria tkankowa, bioetyka (PAN) i Stanisław Lem („Summa '
                              'technologiae”)',
                     'level': 'Podstawowy → Badawczy',
                     'format': 'Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)',
                     'content': 'Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → '
                                'inżynieria tkankowa → biologia syntetyczna i bioetyka.\n'
                                '1. W pierwszej kolejności (Po polsku): Bruce Alberts — „Podstawy biologii komórki” '
                                '(PWN); Terence A. Brown — „Genomy” (PWN); Hieronim Bartel — „Embriologia. Podręcznik '
                                'dla studentów” (PZWL); literatura o komórkach macierzystych, inżynierii tkankowej i '
                                'medycynie regeneracyjnej (PZWL / PWN); stanowiska Komitetu Bioetyki PAN; Stanisław '
                                'Lem — „Summa technologiae” (klasyczna analiza inżynierii biologicznej a science '
                                'fiction).\n'
                                '2. Uzupełniająco (Po angielsku): National Academies (odpowiedzialny rozwój biologii '
                                'syntetycznej), NCBI Bookshelf, ISSCR i Nature.',
                     'url': 'https://bioetyka.pan.pl/',
                     'links': [{'label': '🇵🇱 Komitet Bioetyki Polskiej Akademii Nauk (PAN) — Opracowania i stanowiska '
                                         'bioetyczne po polsku',
                                'url': 'https://bioetyka.pan.pl/'},
                               {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — Hieronim Bartel „Embriologia”, medycyna '
                                         'regeneracyjna i komórki macierzyste',
                                'url': 'https://pzwl.pl/'},
                               {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Biologia komórki (Alberts), Genomy (Brown), '
                                         'Genetyka molekularna (Węgleński)',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biotechnologia, genetyka i '
                                         'inżynieria genetyczna po polsku',
                                'url': 'https://zpe.gov.pl/'},
                               {'label': '🇬🇧 National Academies — Odpowiedzialny rozwój biologii syntetycznej',
                                'url': 'https://www.nationalacademies.org/'},
                               {'label': '🇬🇧 NCBI Bookshelf — Developmental Biology & Cell Biology',
                                'url': 'https://www.ncbi.nlm.nih.gov/books/'},
                               {'label': '🇬🇧 ISSCR — International Society for Stem Cell Research',
                                'url': 'https://www.isscr.org/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:22:00Z'},
                    {'id': 'smat-8',
                     'categoryType': 'TRACK',
                     'targetId': 'E',
                     'topic': 'Filozofia nauki: dowód, hipoteza, teoria i granice modeli.',
                     'title': 'Projekt E (Filozofia — PL w pierwszej kolejności): Alan Chalmers, Thomas S. Kuhn, '
                              'Michał Heller, Władysław Tatarkiewicz, filozofia starożytna (Wolne Lektury) i bioetyka',
                     'level': 'Podstawowy / Akademicki',
                     'format': 'Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)',
                     'content': '1. W pierwszej kolejności (Po polsku):\n'
                                '• Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n'
                                '• Thomas S. Kuhn — „Struktura rewolucji naukowych”\n'
                                '• Michał Heller — „Filozofia nauki. Wprowadzenie” oraz „Filozofia przyrody” '
                                '(Copernicus Center Press)\n'
                                '• Filozofia starożytna po polsku: Platon („Państwo”, „Timajos”), Arystoteles '
                                '(„Metafizyka”, „O duszy”), stoicy (Marek Aureliusz — „Rozmyślania”, Seneka, Epiktet) '
                                'w serwisie Wolne Lektury oraz Władysław Tatarkiewicz — „Historia filozofii. Tom 1–3” '
                                '(PWN)\n'
                                '• Filozofia umysłu, techniki i bioetyka: M. Miłkowski, R. Poczobut (red.) — '
                                '„Przewodnik po filozofii umysłu”; Kazimierz Szewczyk — „Bioetyka. Tom 1–2” (PWN).\n'
                                '2. Uzupełniająco (Po angielsku): Stanford Encyclopedia of Philosophy (SEP) oraz '
                                'Internet Encyclopedia of Philosophy (IEP).',
                     'url': 'https://ccpress.pl/',
                     'links': [{'label': '🇵🇱 Copernicus Center Press — Książki ks. prof. Michała Hellera i filozofia '
                                         'nauki po polsku',
                                'url': 'https://ccpress.pl/'},
                               {'label': '🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Darmowe polskie '
                                         'wykłady z filozofii nauki, umysłu i etyki',
                                'url': 'https://www.copernicuscenter.edu.pl/'},
                               {'label': '🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, '
                                         'Marek Aureliusz, Seneka)',
                                'url': 'https://wolnelektury.pl/katalog/gatunek/filozofia/'},
                               {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Kuhn „Struktura rewolucji naukowych”, '
                                         'Tatarkiewicz „Historia filozofii”, Szewczyk „Bioetyka”',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇬🇧 Stanford Encyclopedia of Philosophy (Filozofia nauki, umysłu i bioetyka)',
                                'url': 'https://plato.stanford.edu/'},
                               {'label': '🇬🇧 Internet Encyclopedia of Philosophy (IEP)',
                                'url': 'https://iep.utm.edu/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:25:00Z'},
                    {'id': 'smat-9',
                     'categoryType': 'TRACK',
                     'targetId': 'F',
                     'topic': 'Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.',
                     'title': 'Projekt F (Człowiek w kosmosie — PL → EN): Polska Agencja Kosmiczna (POLSA), ESERO '
                              'Polska (Centrum Nauki Kopernik), medycyna kosmiczna i astronautyka oraz darmowe źródła '
                              'NASA i ESA',
                     'level': 'Podstawowy / Zaawansowany',
                     'format': 'Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)',
                     'content': 'Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → '
                                'fizjologia kosmiczna → systemy podtrzymywania życia i habitaty.\n'
                                '1. W pierwszej kolejności (Po polsku): Materiały edukacyjne i badawcze Polskiej '
                                'Agencji Kosmicznej (POLSA); polskojęzyczne scenariusze i opracowania ESERO Polska '
                                '(Biuro Edukacji Kosmicznej ESA przy Centrum Nauki Kopernik) dot. życia w '
                                'mikrograwitacji, ochrony radiacyjnej, mechaniki orbitalnej i budowy habitatów; '
                                'polskie podręczniki fizyki (OpenStax Fizyka PL), mechaniki nieba oraz medycyny '
                                'lotniczej i kosmicznej (K. Kwarecki, PZWL).\n'
                                '2. Darmowe źródła międzynarodowe (NASA i ESA): NASA Fundamentals of Human Health, ESA '
                                'Teach with Space, ESA Human and Robotic Exploration.',
                     'url': 'https://esero.kopernik.org.pl/',
                     'links': [{'label': '🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały '
                                         'edukacyjne o załogowych misjach kosmicznych i habitatach',
                                'url': 'https://esero.kopernik.org.pl/'},
                               {'label': '🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja, nauka, medycyna i '
                                         'technologie kosmiczne po polsku',
                                'url': 'https://polsa.gov.pl/'},
                               {'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych” (Mechanika, grawitacja, '
                                         'ruch orbitalny po polsku)',
                                'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                               {'label': '🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of Human Health)',
                                'url': 'https://www.nasa.gov/reference/fundamentals-of-human-health/'},
                               {'label': '🛰️ ESA — Edukacja kosmiczna (Teach with Space)',
                                'url': 'https://education.esa.int/teach-with-space/'},
                               {'label': '👩\u200d🚀 ESA — Eksploracja załogowa i robotyczna (Human and Robotic '
                                         'Exploration)',
                                'url': 'https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:28:00Z'},
                    {'id': 'smat-10',
                     'categoryType': 'TRACK',
                     'targetId': 'G',
                     'topic': 'Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.',
                     'title': 'Projekt G (Człowiek na Ziemi — PL → EN): Jan Krystek („Ochrona środowiska dla '
                              'inżynierów”), January Weiner („Życie i ewolucja biosfery”), Politechnika Śląska, GIOŚ i '
                              'ESA Education',
                     'level': 'Podstawowy / Inżynierski',
                     'format': 'Biblioteka uzupełniająca GOLEM 15 (PL w pierwszej kolejności)',
                     'content': 'Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe '
                                '→ technologie ochronne → ekonomia i polityka środowiskowa.\n'
                                '1. W pierwszej kolejności (Po polsku):\n'
                                '• Jan Krystek — „Ochrona środowiska dla inżynierów” (Wydawnictwo Naukowe PWN).\n'
                                '• January Weiner — „Życie i ewolucja biosfery. Podręcznik ekologii ogólnej” (PWN) — '
                                'fundamentalny polski podręcznik funkcjonowania ekosystemów.\n'
                                '• Czesława Rosik-Dulewska — „Podstawy gospodarki odpadami” (PWN).\n'
                                '• Bezpłatne materiały Politechniki Śląskiej i OpenAGH dot. ochrony wód, powietrza i '
                                'gleby oraz raporty GIOŚ (Państwowy Monitoring Środowiska).\n'
                                '2. Uzupełniająco: Europejska Agencja Środowiska (EEA — serwis w jęz. polskim) oraz '
                                'ESA Education.',
                     'url': 'https://www.polsl.pl/',
                     'links': [{'label': '🇵🇱 Politechnika Śląska — Bezpłatne materiały dotyczące podstaw ochrony '
                                         'środowiska',
                                'url': 'https://www.polsl.pl/'},
                               {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” '
                                         'oraz January Weiner „Życie i ewolucja biosfery”',
                                'url': 'https://ksiegarnia.pwn.pl/'},
                               {'label': '🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ) — Państwowy Monitoring '
                                         'Środowiska (wody, powietrze, gleby)',
                                'url': 'https://www.gios.gov.pl/'},
                               {'label': '🇵🇱 OpenAGH & ZPE — Darmowe polskie materiały o ekologii, odnawialnych '
                                         'źródłach energii i ochronie środowiska',
                                'url': 'https://open.agh.edu.pl/'},
                               {'label': '🇵🇱 Europejska Agencja Środowiska (EEA po polsku — klimat, bioróżnorodność, '
                                         'GOZ, LCA)',
                                'url': 'https://www.eea.europa.eu/pl'},
                               {'label': '🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji środowiska',
                                'url': 'https://education.esa.int/teach-with-space/'}],
                     'author': 'Administrator',
                     'status': 'approved',
                     'createdAt': '2026-10-25T12:30:00Z'},
                    {'id': 'smat-h1',
                     'categoryType': 'TRACK',
                     'targetId': 'H',
                     'topic': 'Reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt HTGR-POLA w '
                              'NCBJ Świerk) do kogeneracji i produkcji wodoru.',
                     'title': 'Super-Projekt H (PL → EN): Fizyka jądrowa, reaktor MARIA, projekt HTGR-POLA (NCBJ '
                              'Świerk), SMR, fuzja termojądrowa (IFPiLM) oraz profile badaczy w bazie Ludzie Nauki',
                     'level': 'Podstawowy → Zaawansowany',
                     'format': 'Biblioteka Super-Projektu H (PL w pierwszej kolejności)',
                     'sourceLang': 'PL+EN',
                     'content': '1. W pierwszej kolejności (Po polsku):\n'
                                '• Podręczniki akademickie: E. Skrzypczak, Z. Szefliński — „Wstęp do fizyki jądra '
                                'atomowego i cząstek elementarnych” (PWN); OpenStax Polska „Fizyka dla szkół wyższych. '
                                'Tom 3” (Fizyka jądrowa); materiały OpenAGH (Energetyka jądrowa).\n'
                                '• Narodowe Centrum Badań Jądrowych (NCBJ Świerk) i raporty w serwisie Nauka w Polsce: '
                                'polski reaktor badawczy MARIA (30 MW — produkcja radioizotopów medycznych '
                                'Mo-99/Lu-177, neutronowe domieszkowanie krzemu dla elektroniki i badania materiałowe '
                                'dla fuzji IFMIF-DONES) oraz projekt polskiego reaktora wysokotemperaturowego '
                                'HTGR-POLA.\n'
                                '• Baza „Ludzie Nauki” (ludzie.nauka.gov.pl/ln/) — dorobek polskich fizyków jądrowych, '
                                'reaktorowych i plazmowych (NCBJ, IFPiLM, AGH, PW).\n'
                                '2. Uzupełniająco (Po angielsku): IAEA SMR & HTGR Technology Roadmaps, ITER Fusion '
                                'oraz NASA Space Nuclear Power.',
                     'url': 'https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html',
                     'links': [{'label': '🇵🇱 Nauka w Polsce — NCBJ opracowało koncepcję polskiego reaktora '
                                         'wysokotemperaturowego (HTGR-POLA)',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html'},
                               {'label': '🇵🇱 Nauka w Polsce — Reaktor badawczy MARIA w NCBJ Świerk: izotopy medyczne, '
                                         'krzem i badania dla fuzji',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C105854%2Cdyrektor-ncbj-maria-chyba-jedyny-reaktor-badawczy-na-swiecie-bez-stabilnego'},
                               {'label': '🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Profile polskich ekspertów i '
                                         'grantów w obszarze energetyki jądrowej i fizyki plazmy',
                                'url': 'https://ludzie.nauka.gov.pl/ln/'},
                               {'label': '🇵🇱 Narodowe Centrum Badań Jądrowych (NCBJ Świerk) — Edukacja i badania '
                                         'jądrowe',
                                'url': 'https://www.ncbj.gov.pl/'},
                               {'label': '🇵🇱 Instytut Fizyki Plazmy i Laserowej Mikrosyntezy (IFPiLM) — Fuzja jądrowa',
                                'url': 'https://www.ifpilm.pl/'},
                               {'label': '🇬🇧 IAEA — Small Modular Reactors (SMR) & Advanced Reactors',
                                'url': 'https://www.iaea.org/'}],
                     'author': 'Ireneusz',
                     'status': 'approved',
                     'createdAt': '2026-10-25T22:50:00Z'},
                    {'id': 'smat-ai-nwp',
                     'categoryType': 'FOUNDATION',
                     'targetId': 'FND-8',
                     'topic': 'Modele poznawcze, reprezentacje semantyczne a biologiczne działanie mózgu (porównanie '
                              'AI i Projektu B).',
                     'title': 'Przegląd „Nauka w Polsce” i „Ludzie Nauki”: Inteligencja biologiczna a sztuczna — '
                              'systemy wzorowane na mózgu, cyfrowy sen sieci neuronowych i biokomputery',
                     'level': 'Średniozaawansowany / Badawczy',
                     'format': 'Zestawienie artykułów badawczych (Nauka w Polsce + Ludzie Nauki)',
                     'sourceLang': 'PL',
                     'content': 'Zbiór wyselekcjonowanych artykułów z serwisu Nauka w Polsce (naukawpolsce.pl) oraz '
                                'profili badawczych z bazy Ludzie Nauki (ludzie.nauka.gov.pl/ln/) łączących Sztuczną '
                                'Inteligencję (Dziedzina 8) z Projektem B (Cyfrowy umysł) i Projektem C (Układy '
                                'neuromorficzne):\n'
                                '• Prof. Włodzisław Duch o transformacji nauki przez AI i kierunkach '
                                'neuroinformatyki.\n'
                                '• Systemy neuromorficzne i chipy wzorowane na mózgu (memrystory) obniżające '
                                'gigantyczne zużycie energii przez współczesne modele AI.\n'
                                '• Algorytmy naśladujące ludzki sen w sztucznych sieciach neuronowych — zapobieganie '
                                'katastrofalnemu zapominaniu podczas uczenia ciągłego.\n'
                                '• Biokomputery hybrydowe (Brainoware) łączące żywe organoidy mózgowe z elektroniką.',
                     'url': 'https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na',
                     'links': [{'label': '🇵🇱 Nauka w Polsce — Kognitywista: przyszłością sztucznej inteligencji są '
                                         'systemy wzorowane na mózgu',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na'},
                               {'label': '🇵🇱 Nauka w Polsce — Prof. Włodzisław Duch: sztuczna inteligencja zmienia '
                                         'wszystko',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C95000%2Cprof-wlodzislaw-duch-sztuczna-inteligencja-zmienia-wszystko.html'},
                               {'label': '🇵🇱 Nauka w Polsce — Sztuczna inteligencja może lepiej „zapamiętać” treści, '
                                         'jeśli naśladuje ludzki sen',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C100463%2Csztuczna-inteligencja-moze-lepiej-zapamietac-tresci-jesli-nasladuje-ludzki'},
                               {'label': '🇵🇱 Nauka w Polsce — Inspirowany mózgiem chip ma ułatwić pracę SI (układy '
                                         'neuromorficzne)',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C112694%2Cinspirowany-mozgiem-chip-ma-ulatwic-prace-si.html'},
                               {'label': '🇵🇱 Nauka w Polsce — Komputer z żywym mózgiem (hybrydowe biokomputery '
                                         'organoidowe)',
                                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C100102%2Ckomputer-z-zywym-mozgiem.html'},
                               {'label': '🇵🇱 Ludzie Nauki (OPI PIB) — Baza polskich badaczy AI, kognitywistyki i sieci '
                                         'neuronowych',
                                'url': 'https://ludzie.nauka.gov.pl/ln/'}],
                     'author': 'Ireneusz',
                     'status': 'approved',
                     'createdAt': '2026-10-25T22:51:00Z'}],
 'supplementaryLibrary': {'title': 'BIBLIOTEKA PROJEKTU GOLEM 15 — Literatura polskojęzyczna (w pierwszej kolejności) '
                                   'i anglojęzyczna (I–VI oraz Projekty C–G)',
                          'description': 'Kompletna bibliografia projektu z priorytetem dla literatury i źródeł '
                                         'polskojęzycznych: Wspólne podstawy (I. Matematyka i Informatyka, II. Fizyka '
                                         'i Komputery Kwantowe, III. Chemia, Biologia i Genetyka), IV. Projekt A, V. '
                                         'Projekt B, VI. Kolejność czytania oraz Biblioteka uzupełniająca do Projektów '
                                         'C, D, E, F i G.',
                          'readingOrder': {'title': 'VI. KOLEJNOŚĆ CZYTANIA — Plan lektur krok po kroku (w pierwszej '
                                                    'kolejności wydania i źródła polskojęzyczne)',
                                           'principle': 'Zasada: zaczynamy od polskojęzycznych podręczników '
                                                        'podstawowych i bezpłatnych źródeł po polsku (OpenStax Polska, '
                                                        'OpenAGH, ZPE, Ważniak MIMUW) — najpierw jedna książka '
                                                        'podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero '
                                                        'kolejna pozycja. Literatura anglojęzyczna stanowi rozwinięcie '
                                                        'specjalistyczne i badawcze. Pełne odwzorowanie ludzkiego '
                                                        'mózgu i przeniesienie umysłu pozostają niezrealizowanymi '
                                                        'celami badawczymi.',
                                           'stages': [{'stage': '1. Najpierw (Fundamenty po polsku: obliczenia, '
                                                                'Python, matematyka i fizyka)',
                                                       'items': ['🇵🇱 Charles Petzold — *Kod. Ukryty język komputerów. '
                                                                 'Wydanie II* — [Wydawnictwo '
                                                                 'Helion](https://helion.pl/) (oryg. *Code*: '
                                                                 '[codehiddenlanguage.com](https://codehiddenlanguage.com/))',
                                                                 '🇵🇱 Eric Matthes — *Python. Instrukcje dla '
                                                                 'programisty* — [Wydawnictwo '
                                                                 'Helion](https://helion.pl/) + [Polski samouczek '
                                                                 'Python](https://docs.python.org/pl/3/tutorial/)',
                                                                 '🇵🇱 Podstawy matematyki i algebry liniowej — [OpenAGH '
                                                                 'Matematyka (PL)](https://open.agh.edu.pl/) | [ZPE '
                                                                 'Matematyka (PL)](https://zpe.gov.pl/) | [OpenStax '
                                                                 'Polska](https://openstax.pl/pl/zasoby)',
                                                                 '🇵🇱 Podręcznik fizyki ogólnej po polsku — [OpenStax '
                                                                 'Fizyka dla szkół wyższych Tom 1–3 (darmowy '
                                                                 'PL)](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1) '
                                                                 '| Halliday & Resnick *Podstawy fizyki* '
                                                                 '([PWN](https://ksiegarnia.pwn.pl/))']},
                                                      {'stage': '2. Następnie (Genomy, chemia, biologia i psychologia '
                                                                'biologiczna po polsku)',
                                                       'items': ['🇵🇱 Terence A. Brown — *Genomy* (polskie wydanie) — '
                                                                 '[Wydawnictwo Naukowe '
                                                                 'PWN](https://ksiegarnia.pwn.pl/)',
                                                                 '🇵🇱 Podstawy chemii, biologii i biochemii po polsku — '
                                                                 '*Biologia Campbella* '
                                                                 '([Rebis](https://www.rebis.com.pl/)), Stryer '
                                                                 '*Biochemia* ([PWN](https://ksiegarnia.pwn.pl/)), '
                                                                 'Alberts *Podstawy biologii komórki* '
                                                                 '([PWN](https://ksiegarnia.pwn.pl/)), '
                                                                 '[ZPE](https://zpe.gov.pl/)',
                                                                 '🇵🇱 James W. Kalat — *Biologiczne podstawy '
                                                                 'psychologii* (polskie wydanie) — [Wydawnictwo '
                                                                 'Naukowe PWN](https://ksiegarnia.pwn.pl/)']},
                                                      {'stage': '3. Później (Neurobiologia, konektomika, neuronauka '
                                                                'obliczeniowa i WBE)',
                                                       'items': ['🇵🇱 Alan Longstaff — *Neurobiologia. Krótkie wykłady* '
                                                                 '([PWN](https://ksiegarnia.pwn.pl/)), E. Nęcka — '
                                                                 '*Psychologia poznawcza* '
                                                                 '([PWN](https://ksiegarnia.pwn.pl/)) oraz 🇵🇱 '
                                                                 'Sebastian Seung — *Konektom. Jak połączenia w mózgu '
                                                                 'kształtują naszą tożsamość* (wyd. polskie)',
                                                                 '🇬🇧 Peter Dayan, L. F. Abbott — *Theoretical '
                                                                 'Neuroscience: Computational and Mathematical '
                                                                 'Modeling of Neural Systems* — [MIT '
                                                                 'Press](https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/)',
                                                                 '🇬🇧 Eugene M. Izhikevich — *Dynamical Systems in '
                                                                 'Neuroscience* — [Pełny PDF '
                                                                 'autora](https://www.izhikevich.org/publications/dsn.pdf)',
                                                                 '🇬🇧 Anders Sandberg, Nick Bostrom — *Whole Brain '
                                                                 'Emulation: A Roadmap* — [Pełny raport PDF (FHI '
                                                                 'Oxford)](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)']},
                                                      {'stage': '4. Na zaawansowanym etapie (Mechanika kwantowa, '
                                                                'neurobiologia akademicka i obliczenia kwantowe)',
                                                       'items': ['🇵🇱/🇬🇧 David J. Griffiths — *Wstęp do mechaniki '
                                                                 'kwantowej* ([polskie wydanie '
                                                                 'PWN](https://ksiegarnia.pwn.pl/)) / *Introduction to '
                                                                 'Quantum Mechanics* '
                                                                 '([CUP](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E))',
                                                                 '🇬🇧 Eric R. Kandel i współautorzy — *Principles of '
                                                                 'Neural Science* — [McGraw '
                                                                 'Hill](https://www.mheducation.com/)',
                                                                 '🇬🇧 Larry Squire i współautorzy — *Fundamental '
                                                                 'Neuroscience* — '
                                                                 '[ScienceDirect](https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience)',
                                                                 '🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — '
                                                                 '*The Computational Brain* — [MIT '
                                                                 'Press](https://mitpress.mit.edu/9780262531207/the-computational-brain/)',
                                                                 '🇬🇧 Michael A. Nielsen, Isaac L. Chuang — *Quantum '
                                                                 'Computation and Quantum Information* — [Cambridge '
                                                                 'University '
                                                                 'Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)']}]},
                          'rules': ['W pierwszej kolejności korzystać z literatury oraz darmowych źródeł '
                                    'polskojęzycznych (OpenStax Polska, e-podręczniki OpenAGH, Zintegrowana Platforma '
                                    'Edukacyjna ZPE, Ważniak MIMUW, polskie wydania PWN, Helion, PZWL i Copernicus '
                                    'Center Press).',
                                    'Zasada czytania: najpierw jedna książka podstawowa z aktualnej dziedziny, potem '
                                    'ćwiczenia i dopiero kolejna pozycja.',
                                    'Książki specjalistyczne i anglojęzyczne wprowadzać po opanowaniu podstaw danego '
                                    'obszaru po polsku.',
                                    'Przed zakupem sprawdzać dokładny tytuł, autora, wydanie i dostępność polskiego '
                                    'przekładu.',
                                    'W szybko rozwijających się dziedzinach korzystać również z aktualnych przeglądów '
                                    'naukowych i dokumentacji instytucji badawczych (PAN, POLSA, GIOŚ, NASA, ESA).',
                                    'Rozróżniać wiedzę potwierdzoną, aktywne badania, hipotezy i spekulacje (pełne '
                                    'odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają niezrealizowanymi '
                                    'celami badawczymi).',
                                    'Traktować bibliografię jako zasób długoterminowy, a nie listę lektur do '
                                    'przeczytania w całości od razu.'],
                          'projects': [{'trackId': 'FND-1',
                                        'title': 'I. MATEMATYKA I INFORMATYKA (Wspólne podstawy — PL w pierwszej '
                                                 'kolejności)',
                                        'sequenceLabel': 'Etap czytania',
                                        'sequence': 'Najpierw (po polsku): Petzold (Kod. Ukryty język komputerów) → '
                                                    'Matthes (Python. Instrukcje dla programisty) → Polskie '
                                                    'podręczniki matematyki i algebry liniowej (OpenAGH, ZPE, '
                                                    'Skoczylas) → Uzupełniająco (EN): Gilbert Strang (Introduction to '
                                                    'Linear Algebra).',
                                        'links': [{'label': '🇵🇱 Wydawnictwo Helion — Polskie wydania: Charles Petzold '
                                                            '„Kod” oraz Eric Matthes „Python. Instrukcje dla '
                                                            'programisty”',
                                                   'url': 'https://helion.pl/'},
                                                  {'label': '🇵🇱 OpenAGH — Darmowe polskie e-podręczniki: Matematyka i '
                                                            'Algebra Liniowa',
                                                   'url': 'https://open.agh.edu.pl/'},
                                                  {'label': '🇵🇱 Ważniak MIMUW (UW) — Darmowe polskie kursy akademickie '
                                                            'z matematyki i informatyki',
                                                   'url': 'https://wazniak.mimuw.edu.pl/'},
                                                  {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Matematyka, '
                                                            'logika i informatyka po polsku',
                                                   'url': 'https://zpe.gov.pl/'},
                                                  {'label': '🇵🇱 Oficjalna dokumentacja i samouczek Pythona po polsku',
                                                   'url': 'https://docs.python.org/pl/3/tutorial/'},
                                                  {'label': '🇬🇧 Gilbert Strang — Introduction to Linear Algebra (MIT '
                                                            '18.06)',
                                                   'url': 'https://math.mit.edu/~gs/linearalgebra/'},
                                                  {'label': '🇬🇧 Charles Petzold — Code (Strona książki i symulacje)',
                                                   'url': 'https://codehiddenlanguage.com/'},
                                                  {'label': '🇬🇧 Eric Matthes — Python Crash Course (Zasoby i '
                                                            'ćwiczenia)',
                                                   'url': 'https://ehmatthes.github.io/pcc_3e/'}],
                                        'groups': [{'heading': '1. Polskojęzyczne (w pierwszej kolejności)',
                                                    'items': ['1. Charles Petzold — *Kod. Ukryty język komputerów. '
                                                              'Wydanie II.* — [Wydawnictwo Helion](https://helion.pl/)',
                                                              '2. Eric Matthes — *Python. Instrukcje dla programisty. '
                                                              'Wydanie III.* — [Wydawnictwo '
                                                              'Helion](https://helion.pl/) + [Samouczek Python '
                                                              'PL](https://docs.python.org/pl/3/tutorial/)',
                                                              '3. Podręczniki matematyki i algebry liniowej na '
                                                              'poziomie szkoły średniej i studiów: M. Gewert, Z. '
                                                              'Skoczylas (*Algebra liniowa*, *Analiza matematyczna*), '
                                                              'T. Krasiński (*Algebra liniowa* PWN) oraz darmowe '
                                                              'zasoby: [OpenAGH Matematyka](https://open.agh.edu.pl/) '
                                                              '| [ZPE Matematyka](https://zpe.gov.pl/) | [Ważniak '
                                                              'MIMUW](https://wazniak.mimuw.edu.pl/)',
                                                              '4. Thomas H. Cormen i współautorzy — *Wprowadzenie do '
                                                              'algorytmów* (polskie wydanie, '
                                                              '[PWN](https://ksiegarnia.pwn.pl/)) oraz Roger Penrose — '
                                                              '*Droga do rzeczywistości* (wyd. polskie).']},
                                                   {'heading': '2. Anglojęzyczne (uzupełniające)',
                                                    'items': ['5. Gilbert Strang — *Introduction to Linear Algebra.* — '
                                                              '[MIT Linear '
                                                              'Algebra](https://math.mit.edu/~gs/linearalgebra/)',
                                                              '6. Charles Petzold — *Code.* — '
                                                              '[codehiddenlanguage.com](https://codehiddenlanguage.com/)',
                                                              '7. Eric Matthes — *Python Crash Course.* — '
                                                              '[ehmatthes.github.io/pcc_3e](https://ehmatthes.github.io/pcc_3e/)']}]},
                                       {'trackId': 'FND-4',
                                        'title': 'II. FIZYKA I KOMPUTERY KWANTOWE (Wspólne podstawy — PL w pierwszej '
                                                 'kolejności)',
                                        'sequenceLabel': 'Etap czytania',
                                        'sequence': 'Najpierw (po polsku): OpenStax „Fizyka dla szkół wyższych Tom '
                                                    '1–3”, Halliday & Resnick „Podstawy fizyki” oraz polskie '
                                                    'podręczniki elektroniki (Horowitz & Hill „Sztuka elektroniki”, '
                                                    'ZPE, Forbot) → Na zaawansowanym etapie: Griffiths („Wstęp do '
                                                    'mechaniki kwantowej” PL / EN) oraz Nielsen i Chuang.',
                                        'links': [{'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3” '
                                                            '(pełny darmowy podręcznik po polsku)',
                                                   'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                                                  {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Halliday & Resnick „Podstawy '
                                                            'fizyki”, Feynman „Wykłady z fizyki”, Griffiths „Wstęp do '
                                                            'mechaniki kwantowej”',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki fizyki, '
                                                            'elektroniki i układów cyfrowych',
                                                   'url': 'https://open.agh.edu.pl/'},
                                                  {'label': '🇵🇱 Forbot — Kursy podstaw elektroniki i techniki cyfrowej '
                                                            'po polsku',
                                                   'url': 'https://forbot.pl/blog/kurs-elektroniki-poziom-1-spis-tresci-id5159'},
                                                  {'label': '🇬🇧 David J. Griffiths — Introduction to Quantum Mechanics '
                                                            '(CUP)',
                                                   'url': 'https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E'},
                                                  {'label': '🇬🇧 Michael A. Nielsen, Isaac L. Chuang — Quantum '
                                                            'Computation and Quantum Information',
                                                   'url': 'https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE'}],
                                        'groups': [{'heading': '1. Polskojęzyczne (w pierwszej kolejności)',
                                                    'items': ['1. Akademickie podręczniki fizyki ogólnej i mechaniki '
                                                              'kwantowej w polskich wydaniach: *OpenStax Fizyka dla '
                                                              'szkół wyższych Tom 1–3* ([darmowy dostęp '
                                                              'PL](https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1)), '
                                                              'D. Halliday, R. Resnick, J. Walker — *Podstawy fizyki* '
                                                              '([PWN](https://ksiegarnia.pwn.pl/)), R. P. Feynman — '
                                                              '*Feynmana wykłady z fizyki* (PWN), D. J. Griffiths — '
                                                              '*Wstęp do mechaniki kwantowej* (polskie wydanie PWN).',
                                                              '2. Podręczniki podstaw elektroniki i układów cyfrowych '
                                                              'po polsku: P. Horowitz, W. Hill — *Sztuka elektroniki. '
                                                              'Cz. 1–2* (WKŁ), B. Głocki — *Układy cyfrowe* (WSiP), '
                                                              '[ZPE Elektronika](https://zpe.gov.pl/), '
                                                              '[OpenAGH](https://open.agh.edu.pl/) oraz [Kursy '
                                                              'Forbot](https://forbot.pl/).']},
                                                   {'heading': '2. Anglojęzyczne (etap zaawansowany)',
                                                    'items': ['3. David J. Griffiths — *Introduction to Quantum '
                                                              'Mechanics.* — [Cambridge University '
                                                              'Press](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E)',
                                                              '4. Michael A. Nielsen, Isaac L. Chuang — *Quantum '
                                                              'Computation and Quantum Information.* — [Cambridge '
                                                              'University '
                                                              'Press](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)']}]},
                                       {'trackId': 'FND-7',
                                        'title': 'III. CHEMIA, BIOLOGIA I GENETYKA (Wspólne podstawy — PL w pierwszej '
                                                 'kolejności)',
                                        'sequenceLabel': 'Etap czytania',
                                        'sequence': 'Następnie (w pierwszej kolejności po polsku): Terence A. Brown '
                                                    '(„Genomy” PWN) → „Biologia Campbella” (wyd. polskie Rebis) i B. '
                                                    'Alberts („Podstawy biologii komórki” PWN) → Polskie podręczniki '
                                                    'chemii i biochemii (Stryer „Biochemia”, Jones & Atkins, McMurry) '
                                                    '→ Uzupełniająco (EN): OpenStax Chemistry 2e i Biology 2e.',
                                        'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — T.A. Brown „Genomy”, Stryer '
                                                            '„Biochemia”, Alberts „Podstawy biologii komórki”, Jones & '
                                                            'Atkins „Chemia ogólna”',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇵🇱 Dom Wydawniczy REBIS — „Biologia Campbella” (polskie '
                                                            'wydanie)',
                                                   'url': 'https://www.rebis.com.pl/'},
                                                  {'label': '🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki chemii '
                                                            'ogólnej, biochemii, biologii i genetyki',
                                                   'url': 'https://open.agh.edu.pl/'},
                                                  {'label': '🇬🇧 OpenStax Chemistry 2e — Darmowy podręcznik chemii '
                                                            'ogólnej',
                                                   'url': 'https://openstax.org/details/books/chemistry-2e'},
                                                  {'label': '🇬🇧 OpenStax Biology 2e — Darmowy podręcznik biologii',
                                                   'url': 'https://openstax.org/details/books/biology-2e'},
                                                  {'label': '🇬🇧 Terence A. Brown — Genomes (NCBI Bookshelf)',
                                                   'url': 'https://www.ncbi.nlm.nih.gov/books/NBK21128/'}],
                                        'groups': [{'heading': '1. Polskojęzyczne (w pierwszej kolejności)',
                                                    'items': ['1. Terence A. Brown — *Genomy.* (polskie wydanie) — '
                                                              '[Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)',
                                                              '2. *Biologia Campbella* — polskie wydanie ([Dom '
                                                              'Wydawniczy REBIS](https://www.rebis.com.pl/)) oraz '
                                                              'Bruce Alberts i współautorzy — *Podstawy biologii '
                                                              'komórki* ([PWN](https://ksiegarnia.pwn.pl/)).',
                                                              '3. Akademickie podręczniki chemii ogólnej, organicznej '
                                                              'i biochemii po polsku: L. Stryer i współautorzy — '
                                                              '*Biochemia* (PWN), L. Jones, P. Atkins — *Chemia '
                                                              'ogólna* (PWN), A. Bielański — *Podstawy chemii '
                                                              'nieorganicznej* (PWN), J. McMurry — *Chemia organiczna* '
                                                              '(PWN), [OpenAGH Chemia](https://open.agh.edu.pl/) i '
                                                              '[ZPE](https://zpe.gov.pl/).']},
                                                   {'heading': '2. Anglojęzyczne (uzupełniające)',
                                                    'items': ['4. *OpenStax Chemistry 2e* — podręcznik chemii ogólnej: '
                                                              '[https://openstax.org/details/books/chemistry-2e](https://openstax.org/details/books/chemistry-2e)',
                                                              '5. *OpenStax Biology 2e* — podręcznik biologii: '
                                                              '[https://openstax.org/details/books/biology-2e](https://openstax.org/details/books/biology-2e)',
                                                              '6. Akademickie podręczniki biochemii i biologii '
                                                              'molekularnej — [NCBI '
                                                              'Bookshelf](https://www.ncbi.nlm.nih.gov/books/)']}]},
                                       {'trackId': 'A',
                                        'title': 'IV. PROJEKT A — CZŁOWIEK BIOCYFROWO-ROBOTYCZNY (PL w pierwszej '
                                                 'kolejności)',
                                        'sequenceLabel': 'Kolejność nauki',
                                        'sequence': 'W pierwszej kolejności po polsku: Biologiczne podstawy '
                                                    'psychologii (Kalat, PWN) oraz anatomia i fizjologia człowieka '
                                                    '(Bochenek, Traczyk, Konturek) → Biofizyka, biomechanika i '
                                                    'biomateriały (Jaroszyk, Marciniak, Tadeusiewicz) → Robotyka, '
                                                    'elektronika, sterowanie i uczenie maszynowe (Géron wyd. polskie '
                                                    'Helion) → Neuroprotetyka i interfejsy mózg–komputer (BCI).',
                                        'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — James W. Kalat „Biologiczne '
                                                            'podstawy psychologii” oraz podręczniki biofizyki i '
                                                            'robotyki',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia człowieka '
                                                            '(Bochenek), Fizjologia (Traczyk) i Biofizyka (Jaroszyk)',
                                                   'url': 'https://pzwl.pl/'},
                                                  {'label': '🇵🇱 Wydawnictwo Helion — Aurélien Géron „Uczenie maszynowe '
                                                            'z użyciem Scikit-Learn i TensorFlow” (wyd. polskie)',
                                                   'url': 'https://helion.pl/'},
                                                  {'label': '🇵🇱 OpenAGH — Polskie materiały z inżynierii biomedycznej, '
                                                            'biocybernetyki i automatyki',
                                                   'url': 'https://open.agh.edu.pl/'},
                                                  {'label': '🇬🇧 OpenStax Anatomy and Physiology 2e (Darmowy podręcznik '
                                                            'online/PDF)',
                                                   'url': 'https://openstax.org/details/books/anatomy-and-physiology-2e'},
                                                  {'label': '🇬🇧 Aurélien Géron — Hands-On Machine Learning '
                                                            '(Repozytorium GitHub)',
                                                   'url': 'https://github.com/ageron/handson-ml3'}],
                                        'groups': [{'heading': '1. Polskojęzyczne (w pierwszej kolejności)',
                                                    'items': ['1. James W. Kalat — *Biologiczne podstawy psychologii.* '
                                                              '— [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)',
                                                              '2. Akademickie podręczniki anatomii i fizjologii '
                                                              'człowieka: A. Bochenek, M. Reicher — *Anatomia '
                                                              'człowieka* ([PZWL](https://pzwl.pl/)); W. Traczyk, A. '
                                                              'Trzebski — *Fizjologia człowieka z elementami '
                                                              'fizjologii stosowanej i klinicznej* (PZWL); S. Konturek '
                                                              '— *Fizjologia człowieka*.',
                                                              '3. Akademickie podręczniki biofizyki, biomechaniki i '
                                                              'biomateriałów: F. Jaroszyk (red.) — *Biofizyka* (PZWL); '
                                                              'J. Marciniak — *Biomateriały* (Politechnika Śląska); '
                                                              'seria *Biocybernetyka i Inżynieria Biomedyczna 2000* '
                                                              '(PAN, red. M. Nałęcz, R. Tadeusiewicz) — '
                                                              '[OpenAGH](https://open.agh.edu.pl/).',
                                                              '4. Podręczniki robotyki, elektroniki, układów '
                                                              'sterowania i AI po polsku: K. Tchoń i współautorzy — '
                                                              '*Manipulatory i roboty mobilne*; A. Géron — *Uczenie '
                                                              'maszynowe z użyciem Scikit-Learn i TensorFlow* '
                                                              '([Helion](https://helion.pl/)).']},
                                                   {'heading': '2. Anglojęzyczne (uzupełniające i specjalistyczne)',
                                                    'items': ['5. *OpenStax Anatomy and Physiology 2e.* — '
                                                              '[https://openstax.org/details/books/anatomy-and-physiology-2e](https://openstax.org/details/books/anatomy-and-physiology-2e)',
                                                              '6. Géron — *Hands-On Machine Learning with '
                                                              'Scikit-Learn, Keras, and TensorFlow.* — [GitHub '
                                                              'ageron/handson-ml3](https://github.com/ageron/handson-ml3)',
                                                              '7. Akademickie podręczniki inżynierii tkankowej, '
                                                              'neuroprotetyki i interfejsów mózg–komputer — [NCBI '
                                                              'Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | '
                                                              '[Physiological Reviews '
                                                              'BCI](https://doi.org/10.1152/physrev.00027.2016)']}]},
                                       {'trackId': 'B',
                                        'title': 'V. PROJEKT B — CYFROWY UMYSŁ (PL w pierwszej kolejności)',
                                        'sequenceLabel': 'Kolejność czytania (Etapy 2 → 3 → 4)',
                                        'sequence': 'W pierwszej kolejności po polsku: Kalat („Biologiczne podstawy '
                                                    'psychologii”), Longstaff („Neurobiologia”), Nęcka („Psychologia '
                                                    'poznawcza”), Miłkowski i Poczobut („Przewodnik po filozofii '
                                                    'umysłu”) oraz Seung („Konektom” — wyd. polskie) → Później (EN): '
                                                    'Dayan & Abbott („Theoretical Neuroscience”), Izhikevich '
                                                    '(„Dynamical Systems in Neuroscience”), Sandberg & Bostrom („Whole '
                                                    'Brain Emulation: A Roadmap”) → Na zaawansowanym etapie: Kandel '
                                                    '(„Principles of Neural Science”), Squire („Fundamental '
                                                    'Neuroscience”), Churchland & Sejnowski („The Computational '
                                                    'Brain”).',
                                        'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — J.W. Kalat „Biologiczne '
                                                            'podstawy psychologii”, A. Longstaff „Neurobiologia”, E. '
                                                            'Nęcka „Psychologia poznawcza”',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇵🇱 Prof. Włodzisław Duch (UMK) — Polskojęzyczne materiały '
                                                            'z kognitywistyki, neuroinformatyki i modelowania mózgu',
                                                   'url': 'https://www.fizyka.umk.pl/~duch/'},
                                                  {'label': '🇵🇱 Copernicus Center Press / Centrum Kopernika — '
                                                            'Filozofia umysłu, kognitywistyka i problem świadomości po '
                                                            'polsku',
                                                   'url': 'https://ccpress.pl/'},
                                                  {'label': '🇬🇧 Eugene M. Izhikevich — Dynamical Systems in '
                                                            'Neuroscience (Darmowy PDF autora)',
                                                   'url': 'https://www.izhikevich.org/publications/dsn.pdf'},
                                                  {'label': '🇬🇧 Anders Sandberg, Nick Bostrom — Whole Brain Emulation: '
                                                            'A Roadmap (PDF)',
                                                   'url': 'https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf'},
                                                  {'label': '🇬🇧 Peter Dayan, L. F. Abbott — Theoretical Neuroscience '
                                                            '(MIT Press)',
                                                   'url': 'https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/'},
                                                  {'label': '🇬🇧 Paul Miller — An Introductory Course in Computational '
                                                            'Neuroscience',
                                                   'url': 'https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/'},
                                                  {'label': '🇬🇧 Patricia S. Churchland, Terrence J. Sejnowski — The '
                                                            'Computational Brain',
                                                   'url': 'https://mitpress.mit.edu/9780262531207/the-computational-brain/'},
                                                  {'label': '🇬🇧 Larry Squire et al. — Fundamental Neuroscience '
                                                            '(ScienceDirect)',
                                                   'url': 'https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience'}],
                                        'groups': [{'heading': '1. Polskojęzyczne (w pierwszej kolejności)',
                                                    'items': ['1. James W. Kalat — *Biologiczne podstawy psychologii.* '
                                                              '— [Wydawnictwo Naukowe PWN](https://ksiegarnia.pwn.pl/)',
                                                              '2. Podręczniki neurobiologii i fizjologii układu '
                                                              'nerwowego po polsku: Alan Longstaff — *Neurobiologia. '
                                                              'Krótkie wykłady* ([PWN](https://ksiegarnia.pwn.pl/)); '
                                                              'T. Górska, A. Grabowska, J. Zagrodzka (red.) — *Mózg a '
                                                              'zachowanie* (PWN).',
                                                              '3. Podręczniki psychologii poznawczej i konektomiki po '
                                                              'polsku: Edward Nęcka, Jarosław Orzechowski, Błażej '
                                                              'Szymura — *Psychologia poznawcza* '
                                                              '([PWN](https://ksiegarnia.pwn.pl/)); Sebastian Seung — '
                                                              '*Konektom. Jak połączenia w mózgu kształtują naszą '
                                                              'tożsamość* (polskie wydanie).',
                                                              '4. Wprowadzenia do filozofii umysłu, kognitywistyki i '
                                                              'problemu świadomości po polsku: Marcin Miłkowski, '
                                                              'Robert Poczobut (red.) — *Przewodnik po filozofii '
                                                              'umysłu*; wykłady z neuroinformatyki prof. Włodzisława '
                                                              'Ducha ([UMK](https://www.fizyka.umk.pl/~duch/)) oraz '
                                                              '[Centrum Kopernika / CCPress](https://ccpress.pl/).']},
                                                   {'heading': '2. Anglojęzyczne (etapy 3 i 4 — zaawansowane '
                                                               'modelowanie i neuronauka)',
                                                    'items': ['5. Eric R. Kandel i współautorzy — *Principles of '
                                                              'Neural Science.* — [McGraw '
                                                              'Hill](https://www.mheducation.com/)',
                                                              '6. Larry Squire i współautorzy — *Fundamental '
                                                              'Neuroscience.* — '
                                                              '[ScienceDirect](https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience)',
                                                              '7. Peter Dayan, L. F. Abbott — *Theoretical '
                                                              'Neuroscience: Computational and Mathematical Modeling '
                                                              'of Neural Systems.* — [MIT '
                                                              'Press](https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/)',
                                                              '8. Eugene M. Izhikevich — *Dynamical Systems in '
                                                              'Neuroscience.* — [Pełny PDF '
                                                              'autora](https://www.izhikevich.org/publications/dsn.pdf)',
                                                              "9. Sebastian Seung — *Connectome: How the Brain's "
                                                              'Wiring Makes Us Who We Are.* — [Seung Lab '
                                                              'MIT](https://seunglab.org/)',
                                                              '10. Paul Miller — *An Introductory Course in '
                                                              'Computational Neuroscience.* — [MIT '
                                                              'Press](https://mitpress.mit.edu/9780262038256/an-introductory-course-in-computational-neuroscience/)',
                                                              '11. Patricia S. Churchland, Terrence J. Sejnowski — '
                                                              '*The Computational Brain.* — [MIT '
                                                              'Press](https://mitpress.mit.edu/9780262531207/the-computational-brain/)',
                                                              '12. Anders Sandberg, Nick Bostrom — *Whole Brain '
                                                              'Emulation: A Roadmap.* — [Pełny raport '
                                                              'PDF](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)']}]},
                                       {'trackId': 'C',
                                        'title': 'Projekt C — Maszyny analogowe i obliczenia fizyczne (PL w pierwszej '
                                                 'kolejności)',
                                        'sequenceLabel': 'Kolejność nauki',
                                        'sequence': 'Elektronika analogowa (po polsku: Horowitz & Hill, OpenAGH, ZPE, '
                                                    'Forbot) → układy dynamiczne → modelowanie matematyczne (Osowski, '
                                                    'Tadeusiewicz) → fizyczne modele neuronów → obliczenia '
                                                    'neuromorficzne.',
                                        'links': [{'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika '
                                                            'i przetworniki A/C oraz C/A',
                                                   'url': 'https://zpe.gov.pl/'},
                                                  {'label': '🇵🇱 OpenAGH — E-podręczniki z elektroniki, układów '
                                                            'dynamicznych i fizyki po polsku',
                                                   'url': 'https://open.agh.edu.pl/'},
                                                  {'label': '🇵🇱 Forbot — Kursy elektroniki analogowej, wzmacniaczy '
                                                            'operacyjnych i ADC/DAC po polsku',
                                                   'url': 'https://forbot.pl/'},
                                                  {'label': '🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering',
                                                   'url': 'https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering'},
                                                  {'label': '🇬🇧 arXiv — Neuromorphic Computing & Analog Neural '
                                                            'Networks',
                                                   'url': 'https://arxiv.org/list/cs.NE/recent'},
                                                  {'label': '🇬🇧 MIT OCW — Circuits & Electronics',
                                                   'url': 'https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/'}],
                                        'groups': [{'heading': '1. Po polsku (w pierwszej kolejności)',
                                                    'items': ['Podręczniki akademickie z elektroniki analogowej: Paul '
                                                              'Horowitz, Winfield Hill — *Sztuka elektroniki* (wyd. '
                                                              'polskie WKŁ); wzmacniacze, oscylatory, filtry, '
                                                              'sprzężenie zwrotne i układy dynamiczne — [E-podręczniki '
                                                              'OpenAGH](https://open.agh.edu.pl/)',
                                                              'Materiały dydaktyczne o przetwornikach '
                                                              'analogowo-cyfrowych (ADC) i cyfrowo-analogowych (DAC) — '
                                                              '[Materiały ZPE](https://zpe.gov.pl/) | [Kursy '
                                                              'Forbot](https://forbot.pl/)',
                                                              'Polska literatura o sieciach neuronowych i '
                                                              'biocybernetyce: Stanisław Osowski — *Sieci neuronowe do '
                                                              'przetwarzania informacji* (Oficyna Wydawnicza PW); '
                                                              'Ryszard Tadeusiewicz — *Sieci neuronowe*.',
                                                              'Zintegrowana Platforma Edukacyjna — punkt wyjścia do '
                                                              'szukania materiałów o elektronice: '
                                                              '[https://zpe.gov.pl/](https://zpe.gov.pl/)']},
                                                   {'heading': '2. Po angielsku (uzupełniające i badawcze)',
                                                    'items': ['Materiały techniczne dotyczące analog computing — [MIT '
                                                              'OpenCourseWare '
                                                              'Electronics](https://ocw.mit.edu/search/?q=analog+computing)',
                                                              'Materiały badawcze dotyczące neuromorphic computing i '
                                                              'analog neural networks — [Frontiers in Neuromorphic '
                                                              'Engineering](https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering)',
                                                              'Publikacje o fizycznych modelach neuronów oraz '
                                                              'analogowych i hybrydowych procesorach — [arXiv '
                                                              'cs.NE](https://arxiv.org/list/cs.NE/recent) | [Neuronal '
                                                              'Dynamics (EPFL)](https://neuronaldynamics.epfl.ch/)']}]},
                                       {'trackId': 'D',
                                        'title': 'Projekt D — „Frankenstein”: biotechnologia i tworzenie organizmów '
                                                 '(PL w pierwszej kolejności)',
                                        'sequenceLabel': 'Kolejność nauki',
                                        'sequence': 'W pierwszej kolejności po polsku: Biologia komórki (Alberts, PWN) '
                                                    '→ genetyka (Brown „Genomy”, Węgleński) → embriologia (Bartel '
                                                    '„Embriologia”, PZWL) → komórki macierzyste i inżynieria tkankowa '
                                                    '→ biologia syntetyczna, bioetyka (Komitet Bioetyki PAN) i nauka a '
                                                    'SF (Stanisław Lem „Summa technologiae”).',
                                        'links': [{'label': '🇵🇱 Komitet Bioetyki Polskiej Akademii Nauk (PAN) — '
                                                            'Stanowiska i opracowania bioetyczne po polsku',
                                                   'url': 'https://bioetyka.pan.pl/'},
                                                  {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — Hieronim Bartel '
                                                            '„Embriologia”, histologia i medycyna regeneracyjna',
                                                   'url': 'https://pzwl.pl/'},
                                                  {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Alberts „Podstawy biologii '
                                                            'komórki”, Brown „Genomy”, Węgleński „Genetyka '
                                                            'molekularna”',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇵🇱 ZPE — Biologia komórki, genetyka i biotechnologia po '
                                                            'polsku',
                                                   'url': 'https://zpe.gov.pl/'},
                                                  {'label': '🇬🇧 National Academies — Responsible Development of '
                                                            'Synthetic Biology',
                                                   'url': 'https://www.nationalacademies.org/'},
                                                  {'label': '🇬🇧 NCBI Bookshelf — Darmowe podręczniki biologii komórki, '
                                                            'genetyki i embriologii',
                                                   'url': 'https://www.ncbi.nlm.nih.gov/books/'},
                                                  {'label': '🇬🇧 ISSCR — International Society for Stem Cell Research',
                                                   'url': 'https://www.isscr.org/'}],
                                        'groups': [{'heading': '1. Po polsku (w pierwszej kolejności)',
                                                    'items': ['Podręczniki akademickie z biologii komórki, genetyki i '
                                                              'biologii rozwoju: B. Alberts — *Podstawy biologii '
                                                              'komórki* ([PWN](https://ksiegarnia.pwn.pl/)), T. A. '
                                                              'Brown — *Genomy* (PWN), P. Węgleński — *Genetyka '
                                                              'molekularna* (PWN) oraz [ZPE '
                                                              'Biologia](https://zpe.gov.pl/).',
                                                              'Podręczniki z embriologii i komórek macierzystych po '
                                                              'polsku: Hieronim Bartel — *Embriologia. Podręcznik dla '
                                                              'studentów* ([PZWL](https://pzwl.pl/)).',
                                                              'Literatura o inżynierii tkankowej, medycynie '
                                                              'regeneracyjnej, bioetyce i granicach SF: publikacje '
                                                              '[Komitetu Bioetyki PAN](https://bioetyka.pan.pl/), K. '
                                                              'Szewczyk — *Bioetyka* (PWN) oraz Stanisław Lem — *Summa '
                                                              'technologiae*.']},
                                                   {'heading': '2. Po angielsku (uzupełniające i badawcze)',
                                                    'items': ['National Academies — materiały o odpowiedzialnym '
                                                              'rozwoju biologii syntetycznej: '
                                                              '[https://www.nationalacademies.org/](https://www.nationalacademies.org/)',
                                                              'Publikacje akademickie o stem cells, developmental '
                                                              'biology, tissue engineering i synthetic biology — [NCBI '
                                                              'Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | '
                                                              '[ISSCR](https://www.isscr.org/) | [Nature Synthetic '
                                                              'Biology](https://www.nature.com/subjects/synthetic-biology)']}]},
                                       {'trackId': 'E',
                                        'title': 'Projekt E — Filozofia (PL w pierwszej kolejności)',
                                        'sequenceLabel': 'Zastosowanie',
                                        'sequence': 'Ocena dowodów, rozróżnianie teorii i spekulacji, analiza '
                                                    'tożsamości osobowej oraz etycznych konsekwencji tworzenia i '
                                                    'modyfikowania organizmów.',
                                        'links': [{'label': '🇵🇱 Copernicus Center Press (ks. prof. Michał Heller — '
                                                            '„Filozofia nauki. Wprowadzenie”)',
                                                   'url': 'https://ccpress.pl/'},
                                                  {'label': '🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — '
                                                            'Wykłady i kursy po polsku',
                                                   'url': 'https://www.copernicuscenter.edu.pl/'},
                                                  {'label': '🇵🇱 Wolne Lektury — Filozofia starożytna po polsku '
                                                            '(Platon, Arystoteles, Marek Aureliusz, Seneka)',
                                                   'url': 'https://wolnelektury.pl/katalog/gatunek/filozofia/'},
                                                  {'label': '🇵🇱 Wydawnictwo Naukowe PWN — T.S. Kuhn „Struktura '
                                                            'rewolucji naukowych”, W. Tatarkiewicz „Historia '
                                                            'filozofii”, K. Szewczyk „Bioetyka”',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇬🇧 Stanford Encyclopedia of Philosophy (SEP)',
                                                   'url': 'https://plato.stanford.edu/'},
                                                  {'label': '🇬🇧 Internet Encyclopedia of Philosophy (IEP)',
                                                   'url': 'https://iep.utm.edu/'}],
                                        'groups': [{'heading': '1. Po polsku (w pierwszej kolejności)',
                                                    'items': ['Alan Chalmers — *Czym jest to, co zwiemy nauką?* — '
                                                              '[Katalog Biblioteki '
                                                              'Narodowej](https://katalogi.bn.org.pl/)',
                                                              'Thomas S. Kuhn — *Struktura rewolucji naukowych.* — '
                                                              '[Wydawnictwo PWN / '
                                                              'Aletheia](https://ksiegarnia.pwn.pl/)',
                                                              'Michał Heller — *Filozofia nauki. Wprowadzenie* oraz '
                                                              '*Filozofia przyrody* — [Copernicus Center '
                                                              'Press](https://ccpress.pl/)',
                                                              'Władysław Tatarkiewicz — *Historia filozofii. Tom 1–3* '
                                                              '(PWN) oraz klasyka filozofii starożytnej w polskich '
                                                              'przekładach ([Wolne '
                                                              'Lektury](https://wolnelektury.pl/katalog/gatunek/filozofia/)).']},
                                                   {'heading': '2. Obszary do dalszego uzupełnienia (PL i EN)',
                                                    'items': ['Filozofia starożytna: Platon (*Państwo*, *Timajos*), '
                                                              'Arystoteles (*Metafizyka*, *O duszy*) i stoicy '
                                                              '(*Rozmyślania* Marka Aureliusza, Seneka, Epiktet) — '
                                                              '[Wolne Lektury: Filozofia '
                                                              '(PL)](https://wolnelektury.pl/katalog/gatunek/filozofia/) '
                                                              '| [SEP Ancient Philosophy](https://plato.stanford.edu/)',
                                                              'Filozofia umysłu i problem świadomości — M. Miłkowski, '
                                                              'R. Poczobut (red.) *Przewodnik po filozofii umysłu* '
                                                              '(PL) | [Centrum Kopernika '
                                                              '(PL)](https://www.copernicuscenter.edu.pl/) | [SEP '
                                                              'Philosophy of '
                                                              'Mind](https://plato.stanford.edu/entries/mind-identity/)',
                                                              'Filozofia techniki, bioetyka i etyka środowiskowa — K. '
                                                              'Szewczyk *Bioetyka Tom 1–2* (PWN), S. Lem *Summa '
                                                              'technologiae*, [Komitet Bioetyki '
                                                              'PAN](https://bioetyka.pan.pl/) | [SEP Philosophy of '
                                                              'Technology](https://plato.stanford.edu/entries/technology/)']}]},
                                       {'trackId': 'F',
                                        'title': 'Projekt F — Człowiek w kosmosie (PL w pierwszej kolejności + darmowe '
                                                 'źródła NASA i ESA)',
                                        'sequenceLabel': 'Kolejność nauki',
                                        'sequence': 'Podstawy fizyki (OpenStax Fizyka PL) → mechanika orbitalna → '
                                                    'technika kosmiczna (POLSA, ESERO Polska) → fizjologia kosmiczna '
                                                    '(medycyna lotnicza i kosmiczna, NASA/ESA) → systemy '
                                                    'podtrzymywania życia i habitaty.',
                                        'links': [{'label': '🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie '
                                                            'materiały edukacyjne o eksploracji kosmosu, '
                                                            'mikrograwitacji i habitatach',
                                                   'url': 'https://esero.kopernik.org.pl/'},
                                                  {'label': '🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja kosmiczna, '
                                                            'inżynieria i medycyna kosmiczna po polsku',
                                                   'url': 'https://polsa.gov.pl/'},
                                                  {'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” '
                                                            '(Mechanika, grawitacja, ruch orbitalny po polsku)',
                                                   'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                                                  {'label': '🚀 NASA — Zdrowie człowieka w kosmosie (Fundamentals of '
                                                            'Human Health)',
                                                   'url': 'https://www.nasa.gov/reference/fundamentals-of-human-health/'},
                                                  {'label': '🛰️ ESA — Edukacja kosmiczna (Teach with Space)',
                                                   'url': 'https://education.esa.int/teach-with-space/'},
                                                  {'label': '👩\u200d🚀 ESA — Eksploracja załogowa (Human and Robotic '
                                                            'Exploration)',
                                                   'url': 'https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration'},
                                                  {'label': '🌱 MELiSSA Foundation — Systemy podtrzymywania życia '
                                                            '(BLSS)',
                                                   'url': 'https://www.melissafoundation.org/'}],
                                        'groups': [{'heading': '1. Po polsku (w pierwszej kolejności)',
                                                    'items': ['ESERO Polska (Biuro Edukacji Kosmicznej ESA przy '
                                                              'Centrum Nauki Kopernik) — polskojęzyczne materiały '
                                                              'dydaktyczne o bazach księżycowych/marsjańskich, '
                                                              'fizjologii w mikrograwitacji i mechanice orbitalnej: '
                                                              '[https://esero.kopernik.org.pl/](https://esero.kopernik.org.pl/)',
                                                              'Polska Agencja Kosmiczna (POLSA) — opracowania o '
                                                              'technologiach kosmicznych, sektorze kosmicznym i '
                                                              'medycynie kosmicznej po polsku: '
                                                              '[https://polsa.gov.pl/](https://polsa.gov.pl/)',
                                                              'Podręczniki polskojęzyczne: *OpenStax Fizyka dla szkół '
                                                              'wyższych Tom 1* (mechanika i grawitacja po polsku), '
                                                              'Krzysztof Kwarecki (red.) — *Medycyna lotnicza i '
                                                              'kosmiczna* (PZWL), literatura Polskiego Towarzystwa '
                                                              'Astronautycznego (*Astronautyka*).']},
                                                   {'heading': '2. Darmowe źródła międzynarodowe (NASA i ESA)',
                                                    'items': ['NASA — zdrowie człowieka w kosmosie: '
                                                              '[https://www.nasa.gov/reference/fundamentals-of-human-health/](https://www.nasa.gov/reference/fundamentals-of-human-health/)',
                                                              'ESA — edukacja kosmiczna: '
                                                              '[https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)',
                                                              'ESA — eksploracja załogowa: '
                                                              '[https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)']},
                                                   {'heading': '3. Tematy do dalszego studiowania',
                                                    'items': ['Fizjologia człowieka w mikrograwitacji — [NASA Human '
                                                              'Research Program](https://www.nasa.gov/hrp/)',
                                                              'Promieniowanie kosmiczne i ochrona biologiczna — [NASA '
                                                              'Space '
                                                              'Radiation](https://www.nasa.gov/hrp/elements/radiation/)',
                                                              'Mechanika orbitalna i napędy — [MIT OCW Space Systems '
                                                              'Engineering](https://ocw.mit.edu/search/?q=orbital+mechanics)',
                                                              'Systemy podtrzymywania życia — [Projekt ESA '
                                                              'MELiSSA](https://www.melissafoundation.org/)',
                                                              'Projektowanie habitatów i statków kosmicznych — [NASA '
                                                              'NTRS](https://ntrs.nasa.gov/)',
                                                              'Uprawa żywności, odzysk wody i wykorzystanie zasobów '
                                                              'lokalnych (ISRU) — [NASA '
                                                              'ISRU](https://www.nasa.gov/mission_pages/station/research/news/b4h-3rd/ev-isru)',
                                                              'Psychologia izolacji i medycyna długotrwałych misji — '
                                                              '[ESA Human '
                                                              'Exploration](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration)']}]},
                                       {'trackId': 'G',
                                        'title': 'Projekt G — Człowiek na Ziemi i ochrona ekosystemu (PL w pierwszej '
                                                 'kolejności)',
                                        'sequenceLabel': 'Kolejność nauki',
                                        'sequence': 'W pierwszej kolejności po polsku: Podstawy ekologii i '
                                                    'funkcjonowanie ekosystemów (January Weiner „Życie i ewolucja '
                                                    'biosfery”, PWN) → presje środowiskowe i monitoring (GIOŚ, '
                                                    'Politechnika Śląska) → technologie ochronne i inżynieria '
                                                    'środowiska (Jan Krystek „Ochrona środowiska dla inżynierów”, '
                                                    'Rosik-Dulewska) → ekonomia i polityka środowiskowa (EEA PL).',
                                        'links': [{'label': '🇵🇱 Politechnika Śląska — Materiały dotyczące podstaw '
                                                            'ochrony środowiska po polsku',
                                                   'url': 'https://www.polsl.pl/'},
                                                  {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona '
                                                            'środowiska dla inżynierów” oraz January Weiner „Życie i '
                                                            'ewolucja biosfery”',
                                                   'url': 'https://ksiegarnia.pwn.pl/'},
                                                  {'label': '🇵🇱 Główny Inspektorat Ochrony Środowiska (GIOŚ — '
                                                            'Państwowy Monitoring Środowiska w Polsce)',
                                                   'url': 'https://www.gios.gov.pl/'},
                                                  {'label': '🇵🇱 OpenAGH & ZPE — Darmowe polskie materiały o ekologii, '
                                                            'odnawialnych źródłach energii i ochronie środowiska',
                                                   'url': 'https://open.agh.edu.pl/'},
                                                  {'label': '🇵🇱 Europejska Agencja Środowiska (EEA w języku polskim — '
                                                            'Ekonomia ekologiczna, GOZ, LCA)',
                                                   'url': 'https://www.eea.europa.eu/pl'},
                                                  {'label': '🌍 ESA Education — Edukacja o Ziemi, klimacie i obserwacji '
                                                            'środowiska',
                                                   'url': 'https://education.esa.int/teach-with-space/'}],
                                        'groups': [{'heading': '1. Po polsku (w pierwszej kolejności)',
                                                    'items': ['Jan Krystek — *Ochrona środowiska dla inżynierów.* — '
                                                              '[Księgarnia Naukowa PWN](https://ksiegarnia.pwn.pl/)',
                                                              'January Weiner — *Życie i ewolucja biosfery. Podręcznik '
                                                              'ekologii ogólnej* ([PWN](https://ksiegarnia.pwn.pl/)) '
                                                              'oraz Czesława Rosik-Dulewska — *Podstawy gospodarki '
                                                              'odpadami* (PWN).',
                                                              'Podręczniki akademickie z ekologii, ochrony środowiska '
                                                              'i OZE — [OpenAGH (PL)](https://open.agh.edu.pl/) | [ZPE '
                                                              'Ekologia (PL)](https://zpe.gov.pl/)',
                                                              'Materiały polskich uczelni i instytucji dotyczące '
                                                              'ochrony wód, powietrza i gleby — [Politechnika '
                                                              'Śląska](https://www.polsl.pl/) | [GIOŚ Monitoring '
                                                              'Środowiska](https://www.gios.gov.pl/)']},
                                                   {'heading': '2. Źródła bezpłatne',
                                                    'items': ['Politechnika Śląska — materiały dotyczące podstaw '
                                                              'ochrony środowiska: '
                                                              '[https://www.polsl.pl/](https://www.polsl.pl/)',
                                                              'Europejska Agencja Środowiska (serwis po polsku): '
                                                              '[https://www.eea.europa.eu/pl](https://www.eea.europa.eu/pl)',
                                                              'ESA Education — edukacja o Ziemi, klimacie i obserwacji '
                                                              'środowiska: '
                                                              '[https://education.esa.int/teach-with-space/](https://education.esa.int/teach-with-space/)']},
                                                   {'heading': '3. Tematy do dalszego studiowania',
                                                    'items': ['Ekologia populacji i ekosystemów — J. Weiner *Życie i '
                                                              'ewolucja biosfery* (PWN) | [OpenStax Biology: '
                                                              'Ecology](https://openstax.org/details/books/biology-2e)',
                                                              'Różnorodność biologiczna i ochrona siedlisk — '
                                                              '[GIOŚ](https://www.gios.gov.pl/) | [IPBES Global '
                                                              'Assessment](https://www.ipbes.net/)',
                                                              'Obiegi biogeochemiczne i funkcjonowanie gleby — [FAO '
                                                              'Soils Portal](https://www.fao.org/soils-portal/en/)',
                                                              'Zmiany klimatu oraz zanieczyszczenia — [Nauka o '
                                                              'Klimacie (PL)](https://naukaoklimacie.pl/) | [Raporty '
                                                              'IPCC](https://www.ipcc.ch/)',
                                                              'Ochrona przyrody, renaturyzacja i odbudowa ekosystemów '
                                                              '— [EEA Nature & Biodiversity '
                                                              '(PL)](https://www.eea.europa.eu/pl)',
                                                              'Odnawialne źródła energii i efektywność energetyczna — '
                                                              '[OpenAGH Energetyka (PL)](https://open.agh.edu.pl/) | '
                                                              '[IEA Renewables](https://www.iea.org/)',
                                                              'Gospodarka obiegu zamkniętego — [EEA Circular Economy '
                                                              '(PL)](https://www.eea.europa.eu/pl)',
                                                              'Ocena cyklu życia produktów (LCA) i ekonomia '
                                                              'ekologiczna — [European Platform on '
                                                              'LCA](https://eplca.jrc.ec.europa.eu/)',
                                                              'Monitoring środowiska z użyciem czujników, satelitów i '
                                                              'AI — [POLSA Obserwacja Ziemi '
                                                              '(PL)](https://polsa.gov.pl/) | [ESA '
                                                              'Copernicus](https://earth.esa.int/)']}]},
                                       {'trackId': 'H',
                                        'title': 'VIII. SUPER-PROJEKT H — ENERGETYKA JĄDROWA, TERMOJĄDROWA I '
                                                 'ZASTOSOWANIA W PODWARIANTACH A–G (PL w pierwszej kolejności)',
                                        'sequenceLabel': 'Kolejność nauki',
                                        'sequence': 'Podstawy fizyki jądrowej i ochrony radiologicznej (po polsku: '
                                                    'Skrzypczak & Szefliński PWN, OpenStax Fizyka Tom 3 PL, OpenAGH) → '
                                                    'Inżynieria reaktorowa, reaktor MARIA, SMR i HTGR-POLA (NCBJ '
                                                    'Świerk, Nauka w Polsce, Ludzie Nauki) → Fizyka plazmy i fuzja '
                                                    'termojądrowa (IFPiLM, ITER, W7-X) → Zastosowania w podwariantach: '
                                                    'zasilanie klastrów AI/WBE (B/C), napędy i reaktory kosmiczne (F), '
                                                    'medycyna nuklearna (A/D) i dekarbonizacja Ziemi (G).',
                                        'links': [{'label': '🇵🇱 Narodowe Centrum Badań Jądrowych (NCBJ w Świerku) — '
                                                            'Reaktor MARIA, projekt HTGR-POLA, fizyka jądrowa i '
                                                            'plazmowa',
                                                   'url': 'https://www.ncbj.gov.pl/'},
                                                  {'label': '🇵🇱 Nauka w Polsce (PAP) — NCBJ opracowało koncepcję '
                                                            'polskiego reaktora wysokotemperaturowego HTGR-POLA',
                                                   'url': 'https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html'},
                                                  {'label': '🇵🇱 Nauka w Polsce (PAP) — Reaktor badawczy MARIA w NCBJ: '
                                                            'izotopy medyczne, badania materiałowe i zastosowania',
                                                   'url': 'https://naukawpolsce.pl/aktualnosci/news%2C105854%2Cdyrektor-ncbj-maria-chyba-jedyny-reaktor-badawczy-na-swiecie-bez-stabilnego'},
                                                  {'label': '🇵🇱 Ludzie Nauki (OPI PIB / MNiSW) — Baza polskich '
                                                            'naukowców, publikacji i projektów (energetyka jądrowa, '
                                                            'fizyka plazmy, AI)',
                                                   'url': 'https://ludzie.nauka.gov.pl/ln/'},
                                                  {'label': '🇵🇱 Instytut Fizyki Plazmy i Laserowej Mikrosyntezy '
                                                            '(IFPiLM) — Fuzja termojądrowa, tokamaki ITER/DEMO i '
                                                            'stellarator W7-X',
                                                   'url': 'https://www.ifpilm.pl/'},
                                                  {'label': '🇵🇱 Portal Gov.pl — Polskie Elektrownie Jądrowe i wiedza o '
                                                            'atomie (PAA / Ministerstwo Przemysłu)',
                                                   'url': 'https://www.gov.pl/web/polski-atom'},
                                                  {'label': '🇬🇧 IAEA (International Atomic Energy Agency) — Small '
                                                            'Modular Reactors (SMR), HTGR & Nuclear Fusion',
                                                   'url': 'https://www.iaea.org/'},
                                                  {'label': '🇬🇧 ITER Organization — Fusion Energy Research',
                                                   'url': 'https://www.iter.org/'}],
                                        'groups': [{'heading': '1. Po polsku (w pierwszej kolejności — podręczniki, '
                                                               'instytuty i serwisy naukowe)',
                                                    'items': ['Ewa Skrzypczak, Zygmunt Szefliński — *Wstęp do fizyki '
                                                              'jądra atomowego i cząstek elementarnych* ([Wydawnictwo '
                                                              'Naukowe PWN](https://ksiegarnia.pwn.pl/)) oraz '
                                                              '*OpenStax Fizyka dla szkół wyższych. Tom 3* (rozdziały '
                                                              'o fizyce jądrowej i energii jądrowej po polsku).',
                                                              'Narodowe Centrum Badań Jądrowych ([NCBJ '
                                                              'Świerk](https://www.ncbj.gov.pl/)) — materiały '
                                                              'edukacyjne i badawcze dot. reaktora MARIA, reaktorów '
                                                              'wysokotemperaturowych HTGR-POLA, bezpieczeństwa '
                                                              'jądrowego i radiofarmaceutyków.',
                                                              'Instytut Fizyki Plazmy i Laserowej Mikrosyntezy '
                                                              '([IFPiLM](https://www.ifpilm.pl/)) — polskie badania '
                                                              'nad kontrolowaną syntezą termojądrową, tokamakami i '
                                                              'plazmą laserową.',
                                                              'Serwis [Nauka w Polsce '
                                                              '(naukawpolsce.pl)](https://naukawpolsce.pl/tag/reaktor) '
                                                              'oraz baza ekspertów i grantów [Ludzie Nauki '
                                                              '(ludzie.nauka.gov.pl/ln/)](https://ludzie.nauka.gov.pl/ln/).']},
                                                   {'heading': '2. Po angielsku (uzupełniające i międzynarodowe)',
                                                    'items': ['John R. Lamarsh, Anthony J. Baratta — *Introduction to '
                                                              'Nuclear Engineering* oraz Samuel Glasstone — *Nuclear '
                                                              'Reactor Engineering*.',
                                                              'IAEA Nuclear Energy Series & PRIS Database — '
                                                              '[https://www.iaea.org/](https://www.iaea.org/)',
                                                              'NASA Kilopower & Space Nuclear Propulsion (NTP/NEP) — '
                                                              '[https://www.nasa.gov/](https://www.nasa.gov/)']}]}]},
 'tracks': [{'id': 'A',
             'code': 'Projekt A',
             'name': 'Człowiek biocyfrowo-robotyczny',
             'color': '#38bdf8',
             'goal': 'Wspomaganie, naprawa i rozszerzanie możliwości ludzkiego organizmu.',
             'guidingQuestion': 'Jak technologia może wspierać i rozszerzać możliwości człowieka?',
             'note': '',
             'sections': [{'title': 'Zakres badawczy',
                           'items': ['Medycyna regeneracyjna, protezy i sztuczne narządy.',
                                     'Robotyka, bioelektronika i inżynieria biomedyczna.',
                                     'Interfejsy mózg–komputer.',
                                     'Wspomaganie ludzkich zmysłów i funkcji ruchowych.']}]},
            {'id': 'B',
             'code': 'Projekt B',
             'name': 'Cyfrowy umysł',
             'color': '#a855f7',
             'goal': 'Poznanie zasad działania mózgu i zbadanie możliwości jego komputerowego modelowania.',
             'guidingQuestion': 'Czy można odtworzyć działanie umysłu w komputerze i co oznaczałoby takie odtworzenie?',
             'note': 'Pełne przeniesienie umysłu do komputera pozostaje hipotetycznym celem badawczym.',
             'sections': [{'title': 'Zakres badawczy',
                           'items': ['Neurobiologia i neuronauka obliczeniowa.',
                                     'Modelowanie neuronów i sieci neuronalnych.',
                                     'Konektomika i poznanie.',
                                     'Świadomość oraz hipotetyczna emulacja całego mózgu.']}]},
            {'id': 'C',
             'code': 'Projekt C',
             'name': 'Maszyny analogowe i obliczanie przez fizykę',
             'color': '#f59e0b',
             'goal': 'Poznanie alternatywnych sposobów realizowania obliczeń.',
             'guidingQuestion': 'Jak wykorzystać właściwości fizyczne układów do efektywnego obliczania i modelowania '
                                'procesów podobnych do pracy mózgu?',
             'note': '',
             'sections': [{'title': 'Zakres badawczy',
                           'items': ['Komputery analogowe i mechaniczne.',
                                     'Elektronika analogowa i układy dynamiczne.',
                                     'Komputery neuromorficzne.',
                                     'Fizyczne modele neuronów.',
                                     'Systemy hybrydowe analogowo-cyfrowe.']}]},
            {'id': 'D',
             'code': 'Projekt D',
             'name': '„Frankenstein”: tworzenie człowieka i science fiction',
             'color': '#10b981',
             'goal': 'Poznanie naukowych możliwości tworzenia, odtwarzania i modyfikowania organizmów.',
             'guidingQuestion': 'Co można rzeczywiście stworzyć lub zmodyfikować w żywym organizmie, a co pozostaje '
                                'fikcją?',
             'note': '',
             'sections': [{'title': 'Zakres badawczy',
                           'items': ['Genetyka, DNA i regulacja genów.',
                                     'Embriologia i rozwój organizmu.',
                                     'Klonowanie i komórki macierzyste.',
                                     'Inżynieria tkankowa i sztuczne narządy.',
                                     'Biologia syntetyczna i edycja genomu.',
                                     'Bioetyka oraz naukowe podstawy science fiction.']}]},
            {'id': 'E',
             'code': 'Projekt E',
             'name': 'Filozofia jako warstwa przekrojowa',
             'color': '#eab308',
             'goal': 'Interpretowanie osiągnięć nauki i badanie granic poznania.',
             'guidingQuestion': 'Co wiemy, jak to uzasadniamy i jakie konsekwencje wynikają z naszej wiedzy?',
             'note': 'Filozofia pozostaje osobnym obszarem nauki, rozwijanym niezależnie. W tym projekcie jest '
                     'nakładką interpretacyjną na pozostałe ścieżki, a nie dodatkowym obowiązkowym przedmiotem.',
             'sections': [{'title': 'Zakres badawczy',
                           'items': ['Filozofia starożytna: Platon, Arystoteles i stoicy.',
                                     'Filozofia nauki: dowód, hipoteza, teoria i granice modeli.',
                                     'Filozofia umysłu: świadomość, tożsamość i natura myślenia.',
                                     'Filozofia techniki: wpływ technologii na człowieka i społeczeństwo.',
                                     'Etyka tworzenia, modyfikowania i ulepszania organizmów.']}]},
            {'id': 'F',
             'code': 'Projekt F',
             'name': 'Człowiek w kosmosie',
             'color': '#6366f1',
             'goal': 'Poznanie sposobów przystosowania technologii, organizmu człowieka i środowiska życia do podróży '
                     'kosmicznych oraz długotrwałej obecności poza Ziemią.',
             'guidingQuestion': 'Jak stworzyć warunki, w których człowiek może bezpiecznie podróżować i żyć poza '
                                'Ziemią, nie zakładając, że jego organizm łatwo przystosuje się do każdego środowiska?',
             'note': '',
             'sections': [{'title': 'A. Technologia podróży kosmicznych',
                           'items': ['Mechanika orbitalna i podstawy astronautyki.',
                                     'Napędy rakietowe i przyszłe koncepcje napędu.',
                                     'Konstrukcja statków kosmicznych i habitatów.',
                                     'Systemy podtrzymywania życia: tlen, woda, żywność i gospodarka odpadami.',
                                     'Osłony przed promieniowaniem i mikrometeoroidami.',
                                     'Robotyka, automatyzacja i autonomiczne systemy.',
                                     'Energetyka, magazynowanie energii i niezawodność urządzeń.',
                                     'Wykorzystanie zasobów lokalnych na Księżycu i Marsie.']},
                          {'title': 'B. Przystosowanie organizmu człowieka',
                           'items': ['Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.',
                                     'Promieniowanie kosmiczne i jego skutki biologiczne.',
                                     'Równowaga, wzrok, sen i rytm dobowy.',
                                     'Żywienie, ćwiczenia i profilaktyka zdrowotna astronautów.',
                                     'Medycyna kosmiczna i samodzielna diagnostyka.',
                                     'Biologia regeneracji i możliwości ograniczania skutków długich misji.',
                                     'Granice biologicznej adaptacji człowieka do innych warunków grawitacyjnych.']},
                          {'title': 'C. Długotrwałe życie poza Ziemią',
                           'items': ['Zamknięte i częściowo zamknięte systemy podtrzymywania życia.',
                                     'Uprawa roślin i produkcja żywności w habitatach.',
                                     'Psychologia izolacji i funkcjonowanie małych załóg.',
                                     'Budowa baz księżycowych i marsjańskich.',
                                     'Terraformowanie jako odrębna, wysoce spekulatywna koncepcja.',
                                     'Etyka ekspansji kosmicznej i ochrona innych światów przed biologicznym '
                                     'skażeniem.']}]},
            {'id': 'G',
             'code': 'Projekt G',
             'name': 'Człowiek na Ziemi: adaptacja i ochrona ekosystemu',
             'color': '#22c55e',
             'goal': 'Zrozumienie zależności między ludzkim organizmem, cywilizacją techniczną i ziemskim środowiskiem '
                     'oraz opracowanie sposobów życia, które nie niszczą podstaw własnego istnienia.',
             'guidingQuestion': 'Jak człowiek może przystosować swoje życie i technologię do warunków Ziemi, chroniąc '
                                'jednocześnie ekosystemy, od których zależy?',
             'note': '',
             'sections': [{'title': 'A. Człowiek jako organizm ziemski',
                           'items': ['Fizjologia człowieka i adaptacja do temperatury, wysokości oraz wysiłku.',
                                     'Wpływ środowiska na zdrowie, odporność i rozwój.',
                                     'Relacje człowieka z mikroorganizmami i mikrobiomem.',
                                     'Znaczenie wody, powietrza, gleby i pożywienia.',
                                     'Ograniczenia biologiczne człowieka i zdolność organizmu do adaptacji.',
                                     'Wpływ miejskiego środowiska, hałasu, światła i zanieczyszczeń na organizm.']},
                          {'title': 'B. Ekologia i funkcjonowanie ekosystemów',
                           'items': ['Ekologia organizmów, populacji i całych ekosystemów.',
                                     'Różnorodność biologiczna i stabilność środowiska.',
                                     'Obiegi węgla, azotu, fosforu i wody.',
                                     'Gleby, lasy, oceany i ekosystemy słodkowodne.',
                                     'Zależności pokarmowe i wzajemne powiązania gatunków.',
                                     'Zmiany klimatu, zanieczyszczenia i utrata siedlisk.',
                                     'Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.']},
                          {'title': 'C. Technologia przyjazna środowisku',
                           'items': ['Odnawialne źródła energii i magazynowanie energii.',
                                     'Efektywność energetyczna budynków, transportu i przemysłu.',
                                     'Gospodarka obiegu zamkniętego i ograniczanie odpadów.',
                                     'Oczyszczanie wody i powietrza.',
                                     'Rolnictwo zrównoważone i ochrona gleb.',
                                     'Materiały biodegradowalne i ograniczanie toksycznych substancji.',
                                     'Monitoring środowiska z wykorzystaniem czujników, satelitów i sztucznej '
                                     'inteligencji.',
                                     'Ocena rzeczywistego wpływu technologii na środowisko w całym cyklu jej życia.']},
                          {'title': 'D. Cywilizacja a granice środowiskowe',
                           'items': ['Zużycie zasobów i możliwości ich odtwarzania.',
                                     'Rozwój miast i infrastruktury.',
                                     'Bezpieczeństwo żywnościowe i wodne.',
                                     'Odporność społeczeństw na katastrofy i zmiany klimatyczne.',
                                     'Konflikt między krótkoterminowym zyskiem a długoterminową stabilnością.',
                                     'Polityka środowiskowa, ekonomia ekologiczna i odpowiedzialność '
                                     'międzypokoleniowa.']}]},
            {'id': 'H',
             'code': 'Super-Projekt H',
             'name': 'Energetyka jądrowa, termojądrowa i architektura mocy (w kontekście podwariantów A–G)',
             'color': '#f43f5e',
             'goal': 'Zbadanie fizycznych, inżynieryjnych i systemowych podstaw gęstych źródeł energii (rozszczepienie '
                     'jądrowe, SMR, HTGR, systemy radioizotopowe oraz synteza termojądrowa) jako fundamentu mocy dla '
                     'gigantycznych klastrów obliczeniowych AI i emulacji mózgu (B i C), napędów i habitatów '
                     'kosmicznych (F), medycyny nuklearnej i bioniki (A i D) oraz dekarbonizacji biosfery Ziemi (G).',
             'guidingQuestion': 'Jak zapewnić bezpieczną, bezemisyjną i ultragęstą energię jądrową oraz termojądrową '
                                'zdolną zasilić cywilizację techniczną, centra obliczeniowe AI/WBE, medycynę nuklearną '
                                'oraz załogową eksplorację kosmosu?',
             'note': 'Super-Projekt H pełni rolę nadrzędnego filaru energetyczno-technologicznego spinającego '
                     'podwarianty wszystkich pozostałych ścieżek (A–G) oraz 8 dziedzin podstawowych.',
             'sections': [{'title': 'A. Fizyka jądrowa, reaktory III+/IV generacji, SMR i HTGR',
                           'items': ['Fizyka jądra atomowego, reakcje rozszczepienia, transport neutronów i kinetyka '
                                     'reaktorowa.',
                                     'Wielkoskalowe reaktory wodne (PWR / EPR / AP1000) oraz małe reaktory modułowe '
                                     '(SMR i mikroreaktory).',
                                     'Reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt '
                                     'HTGR-POLA w NCBJ Świerk) do kogeneracji i produkcji wodoru.',
                                     'Reaktory prędkie IV generacji, zamknięty cykl paliwowy, recykling aktynowców i '
                                     'bezpieczne składowanie odpadów.']},
                          {'title': 'B. Synteza termojądrowa (Fuzja) i fizyka gorącej plazmy',
                           'items': ['Fizyka plazmy wysokotemperaturowej, kryterium Lawsona i utrzymanie magnetyczne '
                                     '(tokamaki ITER, DEMO oraz stellarator Wendelstein 7-X).',
                                     'Synteza inercyjna i laserowa mikrosynteza plazmy (badania IFPiLM i NCBJ).',
                                     'Inżynieria materiałowa pierwszej ściany reaktorów fuzyjnych i badania odporności '
                                     'radiacyjnej w reaktorze MARIA (IFMIF-DONES).']},
                          {'title': 'C. Podwarianty integracyjne ze Ścieżkami A–G oraz Inteligencją (AI)',
                           'items': ['Podwariant B, C i AI: Zasilanie energochłonnych centrów obliczeniowych AI, '
                                     'superkomputerów i hipotetycznej emulacji mózgu (WBE) za pomocą reaktorów '
                                     'SMR/HTGR.',
                                     'Podwariant F (Kosmos): Kosmiczna energetyka jądrowa — generatory radioizotopowe '
                                     '(RTG: Pu-238, Am-241), mikroreaktory księżycowe/marsjańskie (Kilopower) i napędy '
                                     'jądrowe (NTP / NEP).',
                                     'Podwariant A i D (Medycyna nuklearna i bionika): Produkcja izotopów medycznych '
                                     '(reaktor MARIA: Mo-99/Tc-99m, Lu-177), neuroobrazowanie PET/SPECT mózgu, '
                                     'radioterapia celowana i mikrobaterie betawoltaiczne.',
                                     'Podwariant G i E (Ziemia i Filozofia energii): Głęboka dekarbonizacja przemysłu, '
                                     'ciepłownictwa i odsalania wody, kultura bezpieczeństwa jądrowego i '
                                     'odpowiedzialność międzypokoleniowa.']}]}],
 'subprojects': [{'id': 'sub-1',
                  'trackId': 'A',
                  'secondaryTracks': ['B', 'E'],
                  'branchTopic': 'Interfejsy mózg–komputer.',
                  'title': 'Dekodowanie intencji ruchowej i sprzężenie czuciowe w neuroprotezach',
                  'author': 'Administrator',
                  'status': 'approved',
                  'createdAt': '2026-10-25T12:00:00Z',
                  'description': 'Badanie dwukierunkowych interfejsów korowo-obwodowych pozwalających nie tylko '
                                 'sterować efektorami, ale też odbierać sygnały proprioceptywne i dotykowe.',
                  'philosophicalNote': 'Pytanie o granice schematu ciała i podmiotowości: kiedy sztuczny efektor staje '
                                       'się integralną częścią doświadczenia użytkownika?',
                  'workspace': {'hypotheses': [{'id': 'hyp-1',
                                                'statement': 'Zamknięcie pętli sprzężenia zwrotnego o opóźnieniu < 25 '
                                                             'ms znacząco przyspiesza neuroplastyczną integrację '
                                                             'protezy ze schematem ciała.',
                                                'status': 'W weryfikacji',
                                                'author': 'Administrator',
                                                'approvalStatus': 'approved'}],
                                'notes': [{'id': 'note-1',
                                           'title': 'Granica inwazyjności a stabilność sygnału',
                                           'content': 'Matryce mikroelektrod zapewniają wysoką rozdzielczość '
                                                      'przestrzenną, ale ulegają gliozie. Alternatywą są podejścia '
                                                      'wewnątrznaczyniowe (Stentrode) oraz optogenetyczne.',
                                           'author': 'Administrator',
                                           'createdAt': '2026-10-25T12:10:00Z',
                                           'approvalStatus': 'approved'}],
                                'bibliography': [{'id': 'bib-1-pl',
                                                  'citation': '🇵🇱 Kalat, J. W. — Biologiczne podstawy psychologii '
                                                              '(Wydawnictwo Naukowe PWN) oraz Tadeusiewicz, R., '
                                                              'Nałęcz, M. (red.) — Biocybernetyka i Inżynieria '
                                                              'Biomedyczna (PAN / PWN).',
                                                  'url': 'https://ksiegarnia.pwn.pl/',
                                                  'addedBy': 'Administrator',
                                                  'approvalStatus': 'approved'},
                                                 {'id': 'bib-1',
                                                  'citation': '🇬🇧 Lebedev, M. A., & Nicolelis, M. A. (2017). '
                                                              'Brain-Machine Interfaces: From Basic Science to '
                                                              'Neuroprostheses and Neurorehabilitation. Physiological '
                                                              'Reviews.',
                                                  'url': 'https://doi.org/10.1152/physrev.00027.2016',
                                                  'addedBy': 'Administrator',
                                                  'approvalStatus': 'approved'}]}},
                 {'id': 'sub-2',
                  'trackId': 'C',
                  'secondaryTracks': ['B', 'A'],
                  'branchTopic': 'Komputery neuromorficzne.',
                  'title': 'Oscylatory relaksacyjne i memrystorowe synapsy w obliczeniach ciągłych',
                  'author': 'Administrator',
                  'status': 'approved',
                  'createdAt': '2026-10-25T12:15:00Z',
                  'description': 'Środowisko badawcze poświęcone fizycznej realizacji impulsowych sieci neuronowych '
                                 '(SNN) w domenie analogowej bez dyskretyzacji zegarowej.',
                  'philosophicalNote': 'Czy obliczanie ciągłe realizowane bezpośrednio przez prawa fizyki układu '
                                       'analogowego przekracza ograniczenia klasycznych modeli symbolicznych?',
                  'workspace': {'hypotheses': [{'id': 'hyp-2',
                                                'statement': 'Szum termiczny w układach submikronowych może pełnić '
                                                             'funkcję rezonansu stochastycznego, obniżając próg '
                                                             'energetyczny detekcji słabych sygnałów.',
                                                'status': 'Hipoteza otwarta',
                                                'author': 'Administrator',
                                                'approvalStatus': 'approved'}],
                                'notes': [{'id': 'note-2',
                                           'title': 'Porównanie modelu Hodgkina-Huxleya i obwodu FitzHugh-Nagumo',
                                           'content': 'Układ analogowy FHN pozwala odwzorować pobudliwość błony przy '
                                                      'użyciu pojedynczego nieliniowego elementu i indukcyjności (lub '
                                                      'żyratora CMOS).',
                                           'author': 'Administrator',
                                           'createdAt': '2026-10-25T12:20:00Z',
                                           'approvalStatus': 'approved'}],
                                'bibliography': [{'id': 'bib-2-pl',
                                                  'citation': '🇵🇱 Horowitz, P., Hill, W. — Sztuka elektroniki (WKŁ) '
                                                              'oraz Osowski, S. — Sieci neuronowe do przetwarzania '
                                                              'informacji (Oficyna Wydawnicza Politechniki '
                                                              'Warszawskiej).',
                                                  'url': 'https://open.agh.edu.pl/',
                                                  'addedBy': 'Administrator',
                                                  'approvalStatus': 'approved'},
                                                 {'id': 'bib-2',
                                                  'citation': '🇬🇧 Indiveri, G., et al. (2011). Neuromorphic silicon '
                                                              'neuron circuits. Frontiers in Neuroscience.',
                                                  'url': 'https://doi.org/10.3389/fnins.2011.00073',
                                                  'addedBy': 'Administrator',
                                                  'approvalStatus': 'approved'}]}},
                 {'id': 'sub-3',
                  'trackId': 'F',
                  'secondaryTracks': ['G', 'D'],
                  'branchTopic': 'Zamknięte i częściowo zamknięte systemy podtrzymywania życia.',
                  'title': 'Bioregeneracyjne systemy podtrzymywania życia (BLSS) — obieg pierwiastków w habitacie i na '
                           'Ziemi',
                  'author': 'Administrator',
                  'status': 'approved',
                  'createdAt': '2026-10-25T12:30:00Z',
                  'description': 'Porównanie małych, sztucznie domykanych pętli metabolicznych (fotobioreaktory '
                                 'mikroglonowe + uprawy hydroponiczne) z buforową pojemnością ziemskich ekosystemów.',
                  'philosophicalNote': 'Próba odtworzenia biosfery w skali mikro uwidacznia niewidoczne na co dzień '
                                       'usługi ekosystemowe Ziemi (Projekt G) oraz kruchość sztucznych habitatów '
                                       '(Projekt F).',
                  'workspace': {'hypotheses': [{'id': 'hyp-3',
                                                'statement': 'Stabilność mikrobiomu ryzosfery w zamkniętym habitacie '
                                                             'wymaga kontrolowanej redundancji gatunkowej wzorowanej '
                                                             'na naturalnych glebach z Projektu G.',
                                                'status': 'W weryfikacji',
                                                'author': 'Administrator',
                                                'approvalStatus': 'approved'}],
                                'notes': [{'id': 'note-3',
                                           'title': 'Wnioski z eksperymentów MELiSSA i BIOS-3',
                                           'content': 'Największym wyzwaniem pozostaje pełna mineralizacja odpadów '
                                                      'lignocelulozowych oraz utrzymanie równowagi stechiometrycznej '
                                                      'O2/CO2 przy zmiennym metabolizmie załogi.',
                                           'author': 'Administrator',
                                           'createdAt': '2026-10-25T12:35:00Z',
                                           'approvalStatus': 'approved'}],
                                'bibliography': [{'id': 'bib-3-pl',
                                                  'citation': '🇵🇱 Weiner, J. — Życie i ewolucja biosfery. Podręcznik '
                                                              'ekologii ogólnej (Wydawnictwo Naukowe PWN) oraz '
                                                              'Krystek, J. — Ochrona środowiska dla inżynierów (PWN).',
                                                  'url': 'https://ksiegarnia.pwn.pl/',
                                                  'addedBy': 'Administrator',
                                                  'approvalStatus': 'approved'},
                                                 {'id': 'bib-3',
                                                  'citation': '🇬🇧 Lasseur, C., et al. (2010). MELiSSA: The European '
                                                              'project of closed life support system. Gravitational '
                                                              'and Space Biology.',
                                                  'url': 'https://www.melissafoundation.org/',
                                                  'addedBy': 'Administrator',
                                                  'approvalStatus': 'approved'}]}},
                 {'id': 'sub-4',
                  'trackId': 'H',
                  'secondaryTracks': ['B', 'C', 'F', 'G', 'A', 'D'],
                  'branchTopic': 'Podwariant B, C i AI: Zasilanie energochłonnych centrów obliczeniowych AI, '
                                 'superkomputerów i hipotetycznej emulacji mózgu (WBE) za pomocą reaktorów SMR/HTGR.',
                  'title': 'Architektura mocy jądrowej i termojądrowej (SMR / HTGR-POLA / RTG) dla klastrów AI, '
                           'emulacji mózgu i habitatów kosmicznych',
                  'author': 'Ireneusz',
                  'status': 'approved',
                  'createdAt': '2026-10-25T22:52:00Z',
                  'description': 'Środowisko badawcze integrujące Super-Projekt H ze wszystkimi podwariantami projektu '
                                 'Golem 15: (1) bilans energetyczny wielkoskalowych centrów AI oraz hipotetycznej '
                                 'emulacji mózgu (Projekt B) w porównaniu z biologicznym mózgiem (~20 W) i układami '
                                 'neuromorficznymi (Projekt C); (2) wykorzystanie polskich koncepcji reaktorów '
                                 'wysokotemperaturowych HTGR-POLA oraz reaktora MARIA (NCBJ Świerk) do kogeneracji, '
                                 'produkcji wodoru i radiofarmaceutyków (Projekt A i D); (3) kosmiczne mikroreaktory '
                                 'rozszczepieniowe i generatory radioizotopowe RTG dla baz księżycowych i marsjańskich '
                                 '(Projekt F) oraz bezemisyjna stabilizacja biosfery Ziemi (Projekt G).',
                  'philosophicalNote': 'Skala cywilizacyjna i poznawcza (w tym rozwój AI oraz eksploracja kosmosu) '
                                       'jest bezpośrednio ograniczona gęstością dostępnych strumieni energii i '
                                       'umiejętnością bezpiecznego zarządzania procesami jądrowymi w skali '
                                       'wielopokoleniowej (Projekt E).',
                  'workspace': {'hypotheses': [{'id': 'hyp-4',
                                                'statement': 'Dedykowane bloki SMR/HTGR zintegrowane bezpośrednio z '
                                                             'centrami obliczeniowymi AI i układami neuromorficznymi '
                                                             '(Projekt B/C) oraz odzyskiem ciepła odpadowego są '
                                                             'warunkiem koniecznym do skalowania sztucznej '
                                                             'inteligencji bez destabilizacji sieci '
                                                             'elektroenergetycznych i klimatu (Projekt G).',
                                                'status': 'W weryfikacji',
                                                'author': 'Ireneusz',
                                                'approvalStatus': 'approved'},
                                               {'id': 'hyp-5',
                                                'statement': 'W długotrwałych misjach załogowych na Księżyc i Marsa '
                                                             '(Projekt F) kompaktowe reaktory rozszczepieniowe klasy '
                                                             'Kilopower (10–100 kWe) oraz napędy jądrowe (NTP/NEP) '
                                                             'skracające czas ekspozycji na promieniowanie kosmiczne '
                                                             'są niezbędne do utrzymania zamkniętych systemów '
                                                             'podtrzymywania życia (BLSS).',
                                                'status': 'Hipoteza otwarta',
                                                'author': 'Ireneusz',
                                                'approvalStatus': 'approved'}],
                                'notes': [{'id': 'note-4',
                                           'title': 'Synergia NCBJ Świerk (reaktor MARIA i HTGR-POLA) z podwariantami '
                                                    'Golem 15',
                                           'content': '1. Podwariant elektroniki i AI (Projekt C / FND-5): W reaktorze '
                                                      'MARIA realizowane jest neutronowe domieszkowanie krzemu (NTD) '
                                                      'dla elektroniki mocy i półprzewodników.\n'
                                                      '2. Podwariant biomedyczny (Projekt A / B / D): Produkcja '
                                                      'molibdenu-99 / technetu-99m oraz lutetu-177 pozwala na '
                                                      'precyzyjną diagnostykę SPECT/PET (w tym neuroobrazowanie mózgu) '
                                                      'oraz terapię celowaną.\n'
                                                      '3. Podwariant reaktorów IV generacji i fuzji: Projekt HTGR-POLA '
                                                      '(chłodzony helem) dostarcza parę o temp. >500°C, a eksperymenty '
                                                      'w rdzeniu MARIA badają materiały dla reaktorów termojądrowych '
                                                      'DEMO / IFMIF-DONES.',
                                           'author': 'Ireneusz',
                                           'createdAt': '2026-10-25T22:53:00Z',
                                           'approvalStatus': 'approved'}],
                                'bibliography': [{'id': 'bib-4-pl',
                                                  'citation': '🇵🇱 Nauka w Polsce (PAP): NCBJ opracowało koncepcję '
                                                              'polskiego reaktora wysokotemperaturowego HTGR-POLA oraz '
                                                              'badania w reaktorze MARIA.',
                                                  'sourceLang': 'PL',
                                                  'url': 'https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html',
                                                  'addedBy': 'Ireneusz',
                                                  'approvalStatus': 'approved'},
                                                 {'id': 'bib-5-pl',
                                                  'citation': '🇵🇱 Portal Ludzie Nauki (OPI PIB / MNiSW): Profile '
                                                              'badawcze, publikacje i granty w dyscyplinach inżynierii '
                                                              'jądrowej, fizyki plazmy i neuroinformatyki.',
                                                  'sourceLang': 'PL',
                                                  'url': 'https://ludzie.nauka.gov.pl/ln/',
                                                  'addedBy': 'Ireneusz',
                                                  'approvalStatus': 'approved'}]}}],
 'materials': [{'id': 'mat-nwp-h1',
                'trackId': 'H',
                'branchTopic': 'Reaktory wysokotemperaturowe chłodzone gazem (HTGR, w tym polski projekt HTGR-POLA w '
                               'NCBJ Świerk) do kogeneracji i produkcji wodoru.',
                'subprojectId': 'sub-4',
                'title': 'SUPER-PROJEKT H (Nauka w Polsce & Ludzie Nauki): Koncepcja polskiego reaktora '
                         'wysokotemperaturowego HTGR-POLA, reaktor MARIA (NCBJ) oraz fuzja termojądrowa w kontekście '
                         'podwariantów A–G',
                'type': 'Raport badawczy — Nauka w Polsce & Ludzie Nauki [PL]',
                'sourceLang': 'PL',
                'author': 'Ireneusz',
                'content': 'Zestawienie badań z Narodowego Centrum Badań Jądrowych (NCBJ w Świerku) opublikowanych w '
                           'serwisie Nauka w Polsce (PAP) oraz powiązanych profili w bazie Ludzie Nauki:\n'
                           '1. Projekt HTGR-POLA (POLski Atomowy): Opracowana w NCBJ koncepcja '
                           'badawczo-demonstracyjnego reaktora wysokotemperaturowego chłodzonego helem (analizy '
                           'bezpieczeństwa opublikowane m.in. w „Nuclear Technology”). Reaktory HTGR i SMR mogą '
                           'zasilać zarówno przemysł chemiczny i produkcję wodoru (Projekt G), jak i wielkoskalowe '
                           'centra danych AI (Projekt B/C).\n'
                           '2. Reaktor badawczy MARIA (30 MW): Jedyny w Polsce reaktor jądrowy generujący intensywne '
                           'strumienie neutronów — kluczowy dla: (a) medycyny nuklearnej i neuroobrazowania (izotopy '
                           'Mo-99, Lu-177 — styk z Projektem A, B i D), (b) neutronowego domieszkowania krzemu dla '
                           'elektroniki i układów mocy (styk z Projektem C), (c) testowania materiałów osłonowych dla '
                           'przyszłych reaktorów syntezy termojądrowej (DEMO / IFMIF-DONES).\n'
                           '3. Kosmiczne i obronne podwarianty energetyki jądrowej (Projekt F): Zastosowanie '
                           'kompaktowych reaktorów rozszczepieniowych i generatorów radioizotopowych (RTG) w misjach '
                           'księżycowych i marsjańskich.',
                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html',
                'links': [{'label': '🇵🇱 Nauka w Polsce — NCBJ opracowało koncepcję polskiego reaktora '
                                    'wysokotemperaturowego (HTGR-POLA)',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C104569%2Cncbj-opracowalo-koncepcje-polskiego-reaktora-wysokotemperaturowego.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Reaktor badawczy MARIA w NCBJ Świerk: izotopy medyczne, '
                                    'badania materiałowe i fuzja',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C105854%2Cdyrektor-ncbj-maria-chyba-jedyny-reaktor-badawczy-na-swiecie-bez-stabilnego'},
                          {'label': '🇵🇱 Nauka w Polsce — Katalog artykułów: Reaktory jądrowe i energetyka jądrowa',
                           'url': 'https://naukawpolsce.pl/tag/reaktor'},
                          {'label': '🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Wyszukiwarka polskich ekspertów i '
                                    'projektów z fizyki jądrowej, energetyki i AI',
                           'url': 'https://ludzie.nauka.gov.pl/ln/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T22:54:00Z'},
               {'id': 'mat-nwp-b1',
                'trackId': 'B',
                'branchTopic': 'Modelowanie neuronów i sieci neuronalnych.',
                'subprojectId': 'sub-1',
                'title': 'INTELIGENCJA I MÓZG (Nauka w Polsce & Ludzie Nauki): Systemy AI wzorowane na mózgu, cyfrowy '
                         'sen sieci neuronowych, określenie wieku mózgu i dekodowanie myśli z fMRI',
                'type': 'Przegląd artykułów — Nauka w Polsce [PL]',
                'sourceLang': 'PL',
                'author': 'Ireneusz',
                'content': 'Wybrane artykuły z serwisu Nauka w Polsce (naukawpolsce.pl) oraz dorobku polskich '
                           'kognitywistów i neuroinformatyków (baza Ludzie Nauki) dla Projektu B (Cyfrowy umysł) i '
                           'Dziedziny 8 (AI):\n'
                           '1. Systemy wzorowane na mózgu (prof. Włodzisław Duch): Dlaczego klasyczne modele '
                           'głębokiego uczenia wymagają ogromnej mocy obliczeniowej i jak neuroinformatyka dąży do '
                           'połączenia architektury korowej z wnioskowaniem symbolicznym.\n'
                           '2. Cyfrowy sen w sztucznej inteligencji: Wprowadzenie stanów analogicznych do ludzkiego '
                           'snu (faza konsolidacji synaptycznej) zapobiega tzw. katastrofalnemu zapominaniu '
                           '(catastrophic forgetting) w sztucznych sieciach neuronowych uczących się w sposób ciągły.\n'
                           '3. Dekodowanie aktywności mózgu i diagnostyka AI: Wykorzystanie modeli językowych i '
                           'głębokich sieci neuronowych do nieinwazyjnej rekonstrukcji treści myśli ze skanów fMRI '
                           'oraz precyzyjnego wyznaczania biologicznego wieku mózgu.',
                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na',
                'links': [{'label': '🇵🇱 Nauka w Polsce — Kognitywista: przyszłością sztucznej inteligencji są systemy '
                                    'wzorowane na mózgu',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C76897%2Ckognitywista-przyszloscia-sztucznej-inteligencji-sa-systemy-wzorowane-na'},
                          {'label': '🇵🇱 Nauka w Polsce — Prof. Włodzisław Duch: sztuczna inteligencja zmienia wszystko',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C95000%2Cprof-wlodzislaw-duch-sztuczna-inteligencja-zmienia-wszystko.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Sztuczna inteligencja może lepiej „zapamiętać” treści, jeśli '
                                    'naśladuje ludzki sen',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C100463%2Csztuczna-inteligencja-moze-lepiej-zapamietac-tresci-jesli-nasladuje-ludzki'},
                          {'label': '🇵🇱 Nauka w Polsce — Sztuczna inteligencja pozwala określić prawdziwy wiek mózgu',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C94962%2Csztuczna-inteligencja-pozwala-okreslic-prawdziwy-wiek-mozgu.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Komputer nauczył się czytać ludzkie myśli ze skanów fMRI',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C96452%2Cusakomputer-nauczyl-sie-czytac-ludzkie-mysli-choc-jeszcze-popelnia-bledy'},
                          {'label': '🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Profile polskich badaczy '
                                    'neuroinformatyki i sztucznej inteligencji',
                           'url': 'https://ludzie.nauka.gov.pl/ln/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T22:55:00Z'},
               {'id': 'mat-nwp-c1',
                'trackId': 'C',
                'branchTopic': 'Komputery neuromorficzne.',
                'subprojectId': 'sub-2',
                'title': 'OBLICZANIE PRZEZ FIZYKĘ I BIOLOGIĘ (Nauka w Polsce): Chipy neuromorficzne inspirowane '
                         'mózgiem oraz hybrydowy biokomputer z żywym organoidem mózgowym (Brainoware)',
                'type': 'Przegląd artykułów — Nauka w Polsce [PL]',
                'sourceLang': 'PL',
                'author': 'Ireneusz',
                'content': 'Przełomowe badania z pogranicza Projektu C (Maszyny analogowe i neuromorficzne), Projektu '
                           'B (Cyfrowy umysł) i Projektu D (Organoidy) opisywane w serwisie Nauka w Polsce:\n'
                           '1. Inspirowany mózgiem chip neuromorficzny: Przetwarzanie informacji bezpośrednio w '
                           'pamięci (in-memory computing) z wykorzystaniem memrystorów i sztucznych synaps pozwala '
                           'wielokrotnie zredukować pobór mocy przez algorytmy AI (łącznik z Super-Projektem H).\n'
                           '2. Komputer z żywym mózgiem (Brainoware): Połączenie trójwymiarowego organoidu ludzkiego '
                           'mózgu wyhodowanego z komórek macierzystych z matrycą wieloelektrodową i układem uczenia '
                           'maszynowego (reservoir computing) do rozpoznawania mowy i przewidywania nieliniowych '
                           'układów dynamicznych.',
                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C112694%2Cinspirowany-mozgiem-chip-ma-ulatwic-prace-si.html',
                'links': [{'label': '🇵🇱 Nauka w Polsce — Inspirowany mózgiem chip ma ułatwić pracę SI (procesory '
                                    'neuromorficzne)',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C112694%2Cinspirowany-mozgiem-chip-ma-ulatwic-prace-si.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Komputer z żywym mózgiem (biokomputer hybrydowy Brainoware)',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C100102%2Ckomputer-z-zywym-mozgiem.html'}],
                'status': 'approved',
                'createdAt': '2026-10-25T22:56:00Z'},
               {'id': 'mat-nwp-af1',
                'trackId': 'A',
                'branchTopic': 'Interfejsy mózg–komputer.',
                'subprojectId': 'sub-1',
                'title': 'NEUROTECHNOLOGIA W KOSMOSIE (Nauka w Polsce): Misja IGNIS — polski interfejs mózg–komputer '
                         '(PhotonGrav / fNIRS) przetestowany na ISS oraz odporność astronautów',
                'type': 'Przegląd artykułów — Nauka w Polsce [PL]',
                'sourceLang': 'PL',
                'author': 'Ireneusz',
                'content': 'Bezpośredni punkt styku Projektu A (Człowiek biocyfrowo-robotyczny — BCI), Projektu B '
                           '(Dekodowanie sygnałów korowych AI) oraz Projektu F (Człowiek w kosmosie):\n'
                           '1. Eksperyment PhotonGrav podczas polskiej misji kosmicznej IGNIS na Międzynarodowej '
                           'Stacji Kosmicznej (ISS): Pierwsze w historii pomyślne testy polskiego nieinwazyjnego '
                           'interfejsu mózg–komputer opartego na funkcjonalnej spektroskopii bliskiej podczerwieni '
                           '(fNIRS, dr Dariusz Zapała / Cortivision, z udziałem polskiego astronauty dr. Sławosza '
                           'Uznańskiego-Wiśniewskiego). Skuteczność algorytmów AI dekodujących aktywność kory mózgowej '
                           'w mikrograwitacji przekroczyła 80%.\n'
                           '2. Genetyka i immunologia kosmiczna: Badania wykazujące, jak mikrograwitacja zmienia '
                           'ekspresję genów w leukocytach i osłabia układ odpornościowy astronautów oraz jak '
                           'projektować biotechnologiczne środki zaradcze.',
                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C111594%2Cmisja-ignis-polski-interfejs-mozg-komputer-potwierdzil-ze-dziala-w-kosmosie',
                'links': [{'label': '🇵🇱 Nauka w Polsce — Misja IGNIS: Polski interfejs mózg-komputer potwierdził, że '
                                    'działa w kosmosie',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C111594%2Cmisja-ignis-polski-interfejs-mozg-komputer-potwierdzil-ze-dziala-w-kosmosie'},
                          {'label': '🇵🇱 Nauka w Polsce — Przebywanie w kosmosie zaburza układ odpornościowy (zmiany '
                                    'ekspresji genów)',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C98124%2Cprzebywanie-w-kosmosie-zaburza-uklad-odpornosciowy.html'},
                          {'label': '🇵🇱 Ludzie Nauki (ludzie.nauka.gov.pl/ln/) — Profile polskich badaczy '
                                    'neuroinżynierii, fNIRS/EEG i medycyny kosmicznej',
                           'url': 'https://ludzie.nauka.gov.pl/ln/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T22:57:00Z'},
               {'id': 'mat-nwp-dg1',
                'trackId': 'D',
                'branchTopic': 'Inżynieria tkankowa i sztuczne narządy.',
                'subprojectId': None,
                'title': 'BIOTECHNOLOGIA, ORGANOIDY I EKOSYSTEM (Nauka w Polsce): Przeszczep wyhodowanej w '
                         'laboratorium tkanki przysadki, organizmy chimeryczne oraz reakcja biosfery na zmiany klimatu',
                'type': 'Przegląd artykułów — Nauka w Polsce [PL]',
                'sourceLang': 'PL',
                'author': 'Ireneusz',
                'content': 'Artykuły badawcze z serwisu Nauka w Polsce dla Projektu D („Frankenstein” — inżynieria '
                           'tkankowa i biologia syntetyczna) oraz Projektu G (Człowiek na Ziemi):\n'
                           '1. Medycyna regeneracyjna i organoidy (Projekt D): Wyhodowanie w laboratorium z ludzkich '
                           'pluripotencjalnych komórek macierzystych funkcjonalnego organoidu przysadki mózgowej, '
                           'który po przeszczepieniu naczelnych podjął wydzielanie hormonów.\n'
                           '2. Badania nad chimerami z komórek macierzystych i ich ścisłe ramy bioetyczne (styk '
                           'Projektu D i Projektu E).\n'
                           '3. Reakcja ekosystemów i mikroklimatu Ziemi (Projekt G i Super-Projekt H): Badania nad '
                           'wpływem zmian klimatycznych na mikroklimat siedlisk biologicznych oraz stanowiska '
                           'naukowców PAN dot. konieczności transformacji energetycznej (w tym wykorzystania '
                           'energetyki jądrowej i OZE).',
                'url': 'https://naukawpolsce.pl/aktualnosci/news%2C115244%2Cmalpie-wszczepiono-wyhodowana-w-laboratorium-tkanke-przysadki.html',
                'links': [{'label': '🇵🇱 Nauka w Polsce — Małpie wszczepiono wyhodowaną w laboratorium tkankę przysadki '
                                    '(organoid z komórek macierzystych)',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C115244%2Cmalpie-wszczepiono-wyhodowana-w-laboratorium-tkanke-przysadki.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Biotechnolodzy stworzyli chimeryczną małpę z komórek '
                                    'macierzystych',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C99291%2Cbiotechnolodzy-stworzyli-chimeryczna-malpe.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Zbadano dokładniej, jak Ziemia i mikroklimat reagują na '
                                    'zmiany klimatu',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C115569%2Czbadano-dokladniej-jak-ziemia-reaguje-na-zmiany-klimatu.html'},
                          {'label': '🇵🇱 Nauka w Polsce — Naukowcy apelują o systemowe działania chroniące przed '
                                    'skutkami zmiany klimatu',
                           'url': 'https://naukawpolsce.pl/aktualnosci/news%2C113734%2Cnaukowcy-apeluja-do-politykow-o-dzialania-chroniace-obywateli-przed'}],
                'status': 'approved',
                'createdAt': '2026-10-25T22:58:00Z'},
               {'id': 'mat-13',
                'trackId': 'E',
                'branchTopic': 'Filozofia nauki: dowód, hipoteza, teoria i granice modeli.',
                'subprojectId': None,
                'title': 'BIBLIOTEKA PROJEKTU — VI. Kolejność czytania i zasady pracy z literaturą (w pierwszej '
                         'kolejności źródła polskojęzyczne)',
                'type': 'Przewodnik metodologiczny GOLEM 15',
                'author': 'Administrator',
                'content': '1. Najpierw (po polsku): Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” '
                           '(Helion); Eric Matthes — „Python. Instrukcje dla programisty” (Helion); Podstawy '
                           'matematyki i algebry liniowej (OpenAGH, ZPE, Skoczylas); Podręcznik fizyki ogólnej po '
                           'polsku (OpenStax „Fizyka dla szkół wyższych Tom 1–3”, Halliday & Resnick „Podstawy '
                           'fizyki”).\n'
                           '2. Następnie (po polsku): Terence A. Brown — „Genomy” (PWN); Podstawy chemii, biologii i '
                           'biochemii („Biologia Campbella” Rebis, Stryer „Biochemia” PWN, Alberts „Podstawy biologii '
                           'komórki” PWN); James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n'
                           '3. Później (PL i EN): A. Longstaff „Neurobiologia” (PWN), E. Nęcka „Psychologia poznawcza” '
                           '(PWN), S. Seung „Konektom” (wyd. polskie); Dayan & Abbott „Theoretical Neuroscience”; '
                           'Izhikevich „Dynamical Systems in Neuroscience”; Sandberg & Bostrom „Whole Brain Emulation: '
                           'A Roadmap”.\n'
                           '4. Na zaawansowanym etapie: D. J. Griffiths — „Wstęp do mechaniki kwantowej” (wyd. polskie '
                           'PWN / CUP); Kandel — „Principles of Neural Science”; Squire — „Fundamental Neuroscience”; '
                           'Churchland & Sejnowski — „The Computational Brain”; Nielsen i Chuang — „Quantum '
                           'Computation and Quantum Information”.\n'
                           '\n'
                           'Zasada: Zaczynamy od polskojęzycznych podręczników i otwartych zasobów po polsku — '
                           'najpierw jedna książka podstawowa z aktualnej dziedziny, potem ćwiczenia i dopiero kolejna '
                           'pozycja. Pełne odwzorowanie ludzkiego mózgu i przeniesienie umysłu pozostają '
                           'niezrealizowanymi celami badawczymi.',
                'url': 'https://open.agh.edu.pl/',
                'links': [{'label': '1️⃣ 🇵🇱 Etap I (Po polsku): Petzold „Kod”, Matthes „Python” (Helion), OpenAGH '
                                    'Matematyka oraz OpenStax Fizyka Tom 1–3 (PL)',
                           'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                          {'label': '2️⃣ 🇵🇱 Etap II (Po polsku): T.A. Brown „Genomy”, „Biologia Campbella”, Stryer '
                                    '„Biochemia” oraz J.W. Kalat „Biologiczne podstawy psychologii” (PWN)',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '3️⃣ 🇵🇱/🇬🇧 Etap III: Longstaff „Neurobiologia”, Seung „Konektom” (PL) + Dayan & '
                                    'Abbott, Izhikevich, Sandberg & Bostrom (WBE Roadmap PDF)',
                           'url': 'https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf'},
                          {'label': '4️⃣ 🇵🇱/🇬🇧 Etap IV: Griffiths „Wstęp do mechaniki kwantowej” (PWN) + Kandel, '
                                    'Squire, Churchland & Sejnowski, Nielsen & Chuang',
                           'url': 'https://mitpress.mit.edu/9780262533393/the-computational-brain/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T15:25:00Z'},
               {'id': 'mat-8',
                'trackId': 'B',
                'branchTopic': 'Modelowanie neuronów i sieci neuronalnych.',
                'subprojectId': 'sub-1',
                'title': 'BIBLIOTEKA PROJEKTU — I. Matematyka i Informatyka (w pierwszej kolejności po polsku: '
                         'Petzold, Matthes, OpenAGH, ZPE, Ważniak MIMUW + Strang)',
                'type': 'Biblioteka Projektu GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': '1. W pierwszej kolejności — Polskojęzyczne:\n'
                           '• Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II.” (Wydawnictwo Helion)\n'
                           '• Eric Matthes — „Python. Instrukcje dla programisty. Wydanie III.” (Wydawnictwo Helion) + '
                           'oficjalny polski samouczek Pythona\n'
                           '• Podręczniki matematyki i algebry liniowej po polsku: e-podręczniki OpenAGH, ZPE, Ważniak '
                           'MIMUW, M. Gewert i Z. Skoczylas („Algebra liniowa”, „Analiza matematyczna”), T. H. Cormen '
                           'i współautorzy („Wprowadzenie do algorytmów”, PWN), R. Penrose („Droga do rzeczywistości”, '
                           'wyd. polskie).\n'
                           '\n'
                           '2. Uzupełniająco — Anglojęzyczne:\n'
                           '• Gilbert Strang — „Introduction to Linear Algebra.”\n'
                           '• Charles Petzold — „Code: The Hidden Language of Computer Hardware and Software.”\n'
                           '• Eric Matthes — „Python Crash Course.”',
                'url': 'https://open.agh.edu.pl/',
                'links': [{'label': '🇵🇱 Charles Petzold — „Kod. Ukryty język komputerów. Wydanie II” oraz Eric Matthes '
                                    '— „Python. Instrukcje dla programisty” (Helion)',
                           'url': 'https://helion.pl/'},
                          {'label': '🇵🇱 OpenAGH — Darmowe e-podręczniki akademickie: Matematyka i Algebra Liniowa po '
                                    'polsku',
                           'url': 'https://open.agh.edu.pl/'},
                          {'label': '🇵🇱 Ważniak MIMUW (UW) — Darmowe kursy akademickie z matematyki i informatyki po '
                                    'polsku',
                           'url': 'https://wazniak.mimuw.edu.pl/'},
                          {'label': '🇵🇱 Oficjalny samouczek języka Python po polsku (docs.python.org/pl)',
                           'url': 'https://docs.python.org/pl/3/tutorial/'},
                          {'label': '🇬🇧 Gilbert Strang — „Introduction to Linear Algebra” & MIT 18.06',
                           'url': 'https://math.mit.edu/~gs/linearalgebra/'},
                          {'label': '🇬🇧 Charles Petzold — „Code” (Oficjalna strona autora)',
                           'url': 'https://codehiddenlanguage.com/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T15:00:00Z'},
               {'id': 'mat-9',
                'trackId': 'C',
                'branchTopic': 'Komputery analogowe i mechaniczne.',
                'subprojectId': 'sub-2',
                'title': 'BIBLIOTEKA PROJEKTU — II. Fizyka i Komputery Kwantowe (w pierwszej kolejności po polsku: '
                         'OpenStax Fizyka PL, Halliday & Resnick, Griffiths PWN, Horowitz & Hill + Nielsen & Chuang)',
                'type': 'Biblioteka Projektu GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': '1. W pierwszej kolejności — Polskojęzyczne:\n'
                           '• Akademickie podręczniki fizyki ogólnej i mechaniki kwantowej w polskich wydaniach: '
                           'OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1–3” (darmowy podręcznik PL); D. '
                           'Halliday, R. Resnick, J. Walker — „Podstawy fizyki. Tom 1–5” (PWN); R. P. Feynman — '
                           '„Feynmana wykłady z fizyki” (PWN); David J. Griffiths — „Wstęp do mechaniki kwantowej” '
                           '(polskie wydanie PWN).\n'
                           '• Podręczniki podstaw elektroniki i układów cyfrowych po polsku: P. Horowitz, W. Hill — '
                           '„Sztuka elektroniki. Cz. 1–2” (WKŁ); B. Głocki — „Układy cyfrowe” (WSiP); ZPE i kursy '
                           'Forbot.\n'
                           '\n'
                           '2. Uzupełniająco — Anglojęzyczne:\n'
                           '• David J. Griffiths — „Introduction to Quantum Mechanics.”\n'
                           '• Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum Information.”',
                'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1',
                'links': [{'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tomy 1–3” (darmowy podręcznik '
                                    'akademicki po polsku)',
                           'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                          {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Halliday & Resnick „Podstawy fizyki” oraz D.J. '
                                    'Griffiths „Wstęp do mechaniki kwantowej”',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇵🇱 ZPE / OpenAGH / Forbot — Podstawy elektroniki analogowej i układów cyfrowych '
                                    'po polsku',
                           'url': 'https://zpe.gov.pl/'},
                          {'label': '🇬🇧 David J. Griffiths — „Introduction to Quantum Mechanics” (Cambridge University '
                                    'Press)',
                           'url': 'https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E'},
                          {'label': '🇬🇧 Michael A. Nielsen, Isaac L. Chuang — „Quantum Computation and Quantum '
                                    'Information”',
                           'url': 'https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE'}],
                'status': 'approved',
                'createdAt': '2026-10-25T15:05:00Z'},
               {'id': 'mat-10',
                'trackId': 'D',
                'branchTopic': 'Genetyka, DNA i regulacja genów.',
                'subprojectId': None,
                'title': 'BIBLIOTEKA PROJEKTU — III. Chemia, Biologia i Genetyka (w pierwszej kolejności po polsku: '
                         'Brown „Genomy”, „Biologia Campbella”, Alberts, Stryer + OpenStax 2e)',
                'type': 'Biblioteka Projektu GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': '1. W pierwszej kolejności — Polskojęzyczne:\n'
                           '• Terence A. Brown — „Genomy” (polskie wydanie, Wydawnictwo Naukowe PWN).\n'
                           '• „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS) oraz Bruce Alberts i '
                           'współautorzy — „Podstawy biologii komórki” (PWN).\n'
                           '• Akademickie podręczniki chemii ogólnej, organicznej i biochemii po polsku: L. Stryer — '
                           '„Biochemia” (PWN), L. Jones & P. Atkins — „Chemia ogólna” (PWN), A. Bielański — „Podstawy '
                           'chemii nieorganicznej” (PWN), J. McMurry — „Chemia organiczna” (PWN) oraz darmowe zasoby '
                           'OpenAGH i ZPE.\n'
                           '\n'
                           '2. Uzupełniająco — Anglojęzyczne:\n'
                           '• OpenStax „Chemistry 2e” — podręcznik chemii ogólnej.\n'
                           '• OpenStax „Biology 2e” — podręcznik biologii.\n'
                           '• Akademickie podręczniki biochemii i biologii molekularnej (NCBI Bookshelf).',
                'url': 'https://ksiegarnia.pwn.pl/',
                'links': [{'label': '🇵🇱 Terence A. Brown — „Genomy”, L. Stryer — „Biochemia”, B. Alberts — „Podstawy '
                                    'biologii komórki” (Wydawnictwo Naukowe PWN)',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇵🇱 „Biologia Campbella” — polskie wydanie (Dom Wydawniczy REBIS)',
                           'url': 'https://www.rebis.com.pl/'},
                          {'label': '🇵🇱 OpenAGH & ZPE — Darmowe polskie podręczniki chemii, biochemii, biologii i '
                                    'genetyki',
                           'url': 'https://open.agh.edu.pl/'},
                          {'label': '🇬🇧 OpenStax „Chemistry 2e” — darmowy podręcznik chemii ogólnej online',
                           'url': 'https://openstax.org/details/books/chemistry-2e'},
                          {'label': '🇬🇧 OpenStax „Biology 2e” — darmowy podręcznik biologii online',
                           'url': 'https://openstax.org/details/books/biology-2e'}],
                'status': 'approved',
                'createdAt': '2026-10-25T15:10:00Z'},
               {'id': 'mat-11',
                'trackId': 'A',
                'branchTopic': 'Interfejsy mózg–komputer.',
                'subprojectId': 'sub-1',
                'title': 'BIBLIOTEKA PROJEKTU — IV. Projekt A: Człowiek biocyfrowo-robotyczny (w pierwszej kolejności '
                         'po polsku: Kalat, Bochenek, Traczyk, Jaroszyk, Marciniak, Tadeusiewicz, Géron PL + OpenStax '
                         'Anatomy 2e)',
                'type': 'Biblioteka Projektu GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': '1. W pierwszej kolejności — Polskojęzyczne:\n'
                           '• James W. Kalat — „Biologiczne podstawy psychologii” (PWN).\n'
                           '• Akademickie podręczniki anatomii i fizjologii człowieka: A. Bochenek, M. Reicher — '
                           '„Anatomia człowieka” (PZWL); W. Traczyk, A. Trzebski — „Fizjologia człowieka” (PZWL); S. '
                           'Konturek — „Fizjologia człowieka”.\n'
                           '• Akademickie podręczniki biofizyki, biomechaniki i biomateriałów: F. Jaroszyk (red.) — '
                           '„Biofizyka” (PZWL); J. Marciniak — „Biomateriały”; seria „Biocybernetyka i Inżynieria '
                           'Biomedyczna 2000” (PAN, red. M. Nałęcz, R. Tadeusiewicz).\n'
                           '• Podręczniki robotyki, elektroniki, sterowania i uczenia maszynowego po polsku: K. Tchoń '
                           'i współautorzy — „Manipulatory i roboty mobilne”; Aurélien Géron — „Uczenie maszynowe z '
                           'użyciem Scikit-Learn, Keras i TensorFlow” (wyd. polskie Helion).\n'
                           '\n'
                           '2. Uzupełniająco — Anglojęzyczne:\n'
                           '• OpenStax „Anatomy and Physiology 2e.”\n'
                           '• Aurélien Géron — „Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.”\n'
                           '• Akademickie podręczniki inżynierii tkankowej, neuroprotetyki i interfejsów '
                           'mózg–komputer.',
                'url': 'https://ksiegarnia.pwn.pl/',
                'links': [{'label': '🇵🇱 James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN)',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — Anatomia człowieka (Bochenek), Fizjologia '
                                    '(Traczyk) i Biofizyka (Jaroszyk)',
                           'url': 'https://pzwl.pl/'},
                          {'label': '🇵🇱 Aurélien Géron — „Uczenie maszynowe z użyciem Scikit-Learn, Keras i '
                                    'TensorFlow” (Wydawnictwo Helion)',
                           'url': 'https://helion.pl/'},
                          {'label': '🇵🇱 OpenAGH — Inżynieria biomedyczna, biocybernetyka i automatyka po polsku',
                           'url': 'https://open.agh.edu.pl/'},
                          {'label': '🇬🇧 OpenStax „Anatomy and Physiology 2e” — darmowy podręcznik online',
                           'url': 'https://openstax.org/details/books/anatomy-and-physiology-2e'},
                          {'label': '🇬🇧 IEEE EMBS — Engineering in Medicine and Biology (Neuroprotetyka i BCI)',
                           'url': 'https://www.embs.org/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T15:15:00Z'},
               {'id': 'mat-12',
                'trackId': 'B',
                'branchTopic': 'Świadomość oraz hipotetyczna emulacja całego mózgu.',
                'subprojectId': 'sub-1',
                'title': 'BIBLIOTEKA PROJEKTU — V. Projekt B: Cyfrowy umysł (w pierwszej kolejności po polsku: Kalat, '
                         'Longstaff, Nęcka, Seung „Konektom”, Miłkowski & Poczobut + Kandel, Squire, Dayan & Abbott, '
                         'Izhikevich, Sandberg & Bostrom)',
                'type': 'Biblioteka Projektu GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': '1. W pierwszej kolejności — Polskojęzyczne:\n'
                           '• James W. Kalat — „Biologiczne podstawy psychologii” (Wydawnictwo Naukowe PWN).\n'
                           '• Podręczniki neurobiologii i fizjologii układu nerwowego po polsku: Alan Longstaff — '
                           '„Neurobiologia. Krótkie wykłady” (PWN); T. Górska, A. Grabowska, J. Zagrodzka — „Mózg a '
                           'zachowanie” (PWN).\n'
                           '• Podręczniki psychologii poznawczej i konektomiki po polsku: Edward Nęcka, Jarosław '
                           'Orzechowski, Błażej Szymura — „Psychologia poznawcza” (PWN); Sebastian Seung — „Konektom. '
                           'Jak połączenia w mózgu kształtują naszą tożsamość” (wyd. polskie).\n'
                           '• Wprowadzenia do filozofii umysłu i problemu świadomości po polsku: M. Miłkowski, R. '
                           'Poczobut (red.) — „Przewodnik po filozofii umysłu”; wykłady z kognitywistyki i '
                           'neuroinformatyki prof. Włodzisława Ducha (UMK) oraz publikacje Centrum Kopernika.\n'
                           '\n'
                           '2. Uzupełniająco i na zaawansowanym etapie — Anglojęzyczne:\n'
                           '• Eric R. Kandel i współautorzy — „Principles of Neural Science.”\n'
                           '• Larry Squire i współautorzy — „Fundamental Neuroscience.”\n'
                           '• Peter Dayan, L. F. Abbott — „Theoretical Neuroscience: Computational and Mathematical '
                           'Modeling of Neural Systems.”\n'
                           '• Eugene M. Izhikevich — „Dynamical Systems in Neuroscience.”\n'
                           '• Paul Miller — „An Introductory Course in Computational Neuroscience.”\n'
                           '• Patricia S. Churchland, Terrence J. Sejnowski — „The Computational Brain.”\n'
                           '• Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap.”',
                'url': 'https://ksiegarnia.pwn.pl/',
                'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — J.W. Kalat „Biologiczne podstawy psychologii”, A. '
                                    'Longstaff „Neurobiologia”, E. Nęcka „Psychologia poznawcza”',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇵🇱 Prof. Włodzisław Duch (UMK) — Polskie wykłady z kognitywistyki, '
                                    'neuroinformatyki i modelowania mózgu',
                           'url': 'https://www.fizyka.umk.pl/~duch/'},
                          {'label': '🇵🇱 Copernicus Center Press / Centrum Kopernika — Filozofia umysłu i '
                                    'kognitywistyka po polsku',
                           'url': 'https://ccpress.pl/'},
                          {'label': '🇬🇧 Peter Dayan, L. F. Abbott — „Theoretical Neuroscience” (MIT Press)',
                           'url': 'https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/'},
                          {'label': '🇬🇧 Eugene M. Izhikevich — „Dynamical Systems in Neuroscience” (MIT Press / PDF '
                                    'autora)',
                           'url': 'https://www.izhikevich.org/publications/dsn.pdf'},
                          {'label': '🇬🇧 Anders Sandberg, Nick Bostrom — „Whole Brain Emulation: A Roadmap” (Technical '
                                    'Report PDF)',
                           'url': 'https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf'},
                          {'label': '🇬🇧 Eric R. Kandel et al. — „Principles of Neural Science” & Larry Squire et al. — '
                                    '„Fundamental Neuroscience”',
                           'url': 'https://www.sciencedirect.com/book/9780123858702/fundamental-neuroscience'}],
                'status': 'approved',
                'createdAt': '2026-10-25T15:20:00Z'},
               {'id': 'mat-3',
                'trackId': 'C',
                'branchTopic': 'Elektronika analogowa i układy dynamiczne.',
                'subprojectId': 'sub-2',
                'title': 'GOLEM 15 — Projekt C: Maszyny analogowe i obliczenia fizyczne (w pierwszej kolejności po '
                         'polsku: Horowitz & Hill, OpenAGH, ZPE, Forbot, Osowski + Neuromorphic Computing)',
                'type': 'Biblioteka uzupełniająca GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': 'Kolejność nauki: Elektronika analogowa → układy dynamiczne → modelowanie matematyczne → '
                           'fizyczne modele neuronów → obliczenia neuromorficzne.\n'
                           '\n'
                           '1. W pierwszej kolejności — Po polsku: Podręczniki akademickie z elektroniki analogowej '
                           '(P. Horowitz, W. Hill — „Sztuka elektroniki”; e-podręczniki OpenAGH: wzmacniacze, '
                           'oscylatory, filtry, sprzężenie zwrotne, układy dynamiczne), materiały dydaktyczne o '
                           'przetwornikach A/C i C/A (ZPE, kursy Forbot), polska literatura o sieciach neuronowych (S. '
                           'Osowski, R. Tadeusiewicz).\n'
                           '2. Uzupełniająco — Po angielsku: Materiały techniczne dot. analog computing, badania dot. '
                           'neuromorphic computing i analog neural networks, publikacje o fizycznych modelach neuronów '
                           'oraz analogowych i hybrydowych procesorach.',
                'url': 'https://zpe.gov.pl/',
                'links': [{'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Elektronika i przetworniki A/C oraz '
                                    'C/A: https://zpe.gov.pl/',
                           'url': 'https://zpe.gov.pl/'},
                          {'label': '🇵🇱 OpenAGH — Polskie e-podręczniki akademickie: Elektronika i układy dynamiczne',
                           'url': 'https://open.agh.edu.pl/'},
                          {'label': '🇵🇱 Forbot — Kursy elektroniki analogowej i cyfrowej po polsku',
                           'url': 'https://forbot.pl/'},
                          {'label': '🇬🇧 Frontiers in Neuroscience — Neuromorphic Engineering',
                           'url': 'https://www.frontiersin.org/journals/neuroscience/sections/neuromorphic-engineering'},
                          {'label': '🇬🇧 arXiv — Neuromorphic Computing & Analog Neural Networks',
                           'url': 'https://arxiv.org/list/cs.NE/recent'}],
                'status': 'approved',
                'createdAt': '2026-10-25T14:00:00Z'},
               {'id': 'mat-4',
                'trackId': 'D',
                'branchTopic': 'Biologia syntetyczna i edycja genomu.',
                'subprojectId': None,
                'title': 'GOLEM 15 — Projekt D: „Frankenstein” — biotechnologia i tworzenie organizmów (w pierwszej '
                         'kolejności po polsku: Alberts, Brown, Bartel „Embriologia”, Komitet Bioetyki PAN, Lem „Summa '
                         'technologiae”)',
                'type': 'Biblioteka uzupełniająca GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': 'Kolejność nauki: Biologia komórki → genetyka → embriologia → komórki macierzyste → '
                           'inżynieria tkankowa → biologia syntetyczna i bioetyka.\n'
                           '\n'
                           '1. W pierwszej kolejności — Po polsku: Podręczniki akademickie z biologii komórki, '
                           'genetyki i biologii rozwoju (B. Alberts „Podstawy biologii komórki” PWN, T.A. Brown '
                           '„Genomy” PWN, P. Węgleński „Genetyka molekularna” PWN); podręczniki z embriologii i '
                           'komórek macierzystych (H. Bartel „Embriologia” PZWL); literatura o inżynierii tkankowej, '
                           'medycynie regeneracyjnej i bioetyce (Komitet Bioetyki PAN, K. Szewczyk „Bioetyka” PWN) '
                           'oraz Stanisław Lem — „Summa technologiae”.\n'
                           '2. Uzupełniająco — Po angielsku: National Academies — materiały o odpowiedzialnym rozwoju '
                           'biologii syntetycznej; publikacje akademickie o stem cells, developmental biology, tissue '
                           'engineering i synthetic biology.',
                'url': 'https://bioetyka.pan.pl/',
                'links': [{'label': '🇵🇱 Komitet Bioetyki PAN — Stanowiska i opracowania bioetyczne po polsku',
                           'url': 'https://bioetyka.pan.pl/'},
                          {'label': '🇵🇱 PZWL Wydawnictwo Lekarskie — H. Bartel „Embriologia”, komórki macierzyste i '
                                    'medycyna regeneracyjna',
                           'url': 'https://pzwl.pl/'},
                          {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Alberts „Podstawy biologii komórki”, Brown „Genomy”, '
                                    'Węgleński „Genetyka molekularna”',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇵🇱 Zintegrowana Platforma Edukacyjna (ZPE) — Biologia i biotechnologia po polsku',
                           'url': 'https://zpe.gov.pl/'},
                          {'label': '🇬🇧 National Academies — Biologia syntetyczna: https://www.nationalacademies.org/',
                           'url': 'https://www.nationalacademies.org/'},
                          {'label': '🇬🇧 NCBI Bookshelf — Molecular Biology of the Cell & Developmental Biology',
                           'url': 'https://www.ncbi.nlm.nih.gov/books/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T14:05:00Z'},
               {'id': 'mat-5',
                'trackId': 'E',
                'branchTopic': 'Filozofia nauki: dowód, hipoteza, teoria i granice modeli.',
                'subprojectId': None,
                'title': 'GOLEM 15 — Projekt E: Filozofia nauki, umysłu, techniki i bioetyka (w pierwszej kolejności '
                         'po polsku: Chalmers, Kuhn, Heller, Tatarkiewicz, Wolne Lektury)',
                'type': 'Biblioteka uzupełniająca GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': 'Zastosowanie: Ocena dowodów, rozróżnianie teorii i spekulacji, analiza tożsamości osobowej '
                           'oraz etycznych konsekwencji tworzenia i modyfikowania organizmów.\n'
                           '\n'
                           '1. W pierwszej kolejności — Po polsku:\n'
                           '  • Alan Chalmers — „Czym jest to, co zwiemy nauką?”\n'
                           '  • Thomas S. Kuhn — „Struktura rewolucji naukowych”\n'
                           '  • Michał Heller — „Filozofia nauki. Wprowadzenie” oraz „Filozofia przyrody” (Copernicus '
                           'Center Press)\n'
                           '  • Władysław Tatarkiewicz — „Historia filozofii. Tom 1–3” (PWN) oraz klasyka filozofii '
                           'starożytnej po polsku (Platon, Arystoteles, Marek Aureliusz, Seneka) w serwisie Wolne '
                           'Lektury\n'
                           '  • Marcin Miłkowski, Robert Poczobut (red.) — „Przewodnik po filozofii umysłu” oraz '
                           'Kazimierz Szewczyk — „Bioetyka. Tom 1–2” (PWN).\n'
                           '2. Uzupełniająco — Po angielsku: Stanford Encyclopedia of Philosophy (SEP) oraz Internet '
                           'Encyclopedia of Philosophy (IEP).',
                'url': 'https://ccpress.pl/',
                'links': [{'label': '🇵🇱 Copernicus Center Press — Michał Heller „Filozofia nauki. Wprowadzenie”',
                           'url': 'https://ccpress.pl/'},
                          {'label': '🇵🇱 Centrum Kopernika Badań Interdyscyplinarnych (UJ) — Wykłady z filozofii nauki '
                                    'i umysłu po polsku',
                           'url': 'https://www.copernicuscenter.edu.pl/'},
                          {'label': '🇵🇱 Wolne Lektury — Filozofia starożytna po polsku (Platon, Arystoteles, stoicy)',
                           'url': 'https://wolnelektury.pl/katalog/gatunek/filozofia/'},
                          {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Kuhn, Tatarkiewicz, Szewczyk („Bioetyka”)',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇬🇧 Stanford Encyclopedia of Philosophy (SEP — Nauka, Umysł, Technika, Bioetyka)',
                           'url': 'https://plato.stanford.edu/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T14:10:00Z'},
               {'id': 'mat-6',
                'trackId': 'F',
                'branchTopic': 'Wpływ mikrograwitacji na mięśnie, kości i układ krążenia.',
                'subprojectId': 'sub-3',
                'title': 'GOLEM 15 — Projekt F: Człowiek w kosmosie (w pierwszej kolejności po polsku: POLSA, ESERO '
                         'Polska, OpenStax Fizyka PL, medycyna kosmiczna + darmowe źródła NASA i ESA)',
                'type': 'Biblioteka uzupełniająca GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': 'Kolejność nauki: Podstawy fizyki → mechanika orbitalna → technika kosmiczna → fizjologia '
                           'kosmiczna → systemy podtrzymywania życia i habitaty.\n'
                           '\n'
                           '1. W pierwszej kolejności — Po polsku: Materiały edukacyjne i badawcze Polskiej Agencji '
                           'Kosmicznej (POLSA) oraz ESERO Polska (Centrum Nauki Kopernik / ESA) dot. załogowych misji '
                           'kosmicznych, życia w mikrograwitacji, ochrony przed promieniowaniem i projektowania '
                           'habitatów; OpenStax Polska — „Fizyka dla szkół wyższych” (mechanika i grawitacja po '
                           'polsku); K. Kwarecki (red.) — „Medycyna lotnicza i kosmiczna” (PZWL).\n'
                           '2. Darmowe źródła międzynarodowe: NASA (zdrowie człowieka w kosmosie), ESA (edukacja '
                           'kosmiczna — Teach with Space), ESA (eksploracja załogowa i robotyczna).',
                'url': 'https://esero.kopernik.org.pl/',
                'links': [{'label': '🇵🇱 ESERO Polska (Centrum Nauki Kopernik / ESA) — Polskie materiały edukacyjne o '
                                    'eksploracji kosmosu i habitatach',
                           'url': 'https://esero.kopernik.org.pl/'},
                          {'label': '🇵🇱 Polska Agencja Kosmiczna (POLSA) — Edukacja, nauka i medycyna kosmiczna po '
                                    'polsku',
                           'url': 'https://polsa.gov.pl/'},
                          {'label': '🇵🇱 OpenStax Polska — „Fizyka dla szkół wyższych. Tom 1” (Mechanika i grawitacja '
                                    'po polsku)',
                           'url': 'https://openstax.org/details/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1'},
                          {'label': '🚀 NASA — Zdrowie człowieka w kosmosie: '
                                    'https://www.nasa.gov/reference/fundamentals-of-human-health/',
                           'url': 'https://www.nasa.gov/reference/fundamentals-of-human-health/'},
                          {'label': '🛰️ ESA — Edukacja kosmiczna: https://education.esa.int/teach-with-space/',
                           'url': 'https://education.esa.int/teach-with-space/'},
                          {'label': '👩\u200d🚀 ESA — Eksploracja załogowa: '
                                    'https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration',
                           'url': 'https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration'}],
                'status': 'approved',
                'createdAt': '2026-10-25T14:15:00Z'},
               {'id': 'mat-7',
                'trackId': 'G',
                'branchTopic': 'Ochrona przyrody, odbudowa ekosystemów i renaturyzacja.',
                'subprojectId': 'sub-3',
                'title': 'GOLEM 15 — Projekt G: Człowiek na Ziemi i ochrona ekosystemu (w pierwszej kolejności po '
                         'polsku: Krystek, Weiner „Życie i ewolucja biosfery”, Politechnika Śląska, GIOŚ, EEA PL + ESA '
                         'Education)',
                'type': 'Biblioteka uzupełniająca GOLEM 15 (PL → EN)',
                'author': 'Administrator',
                'content': 'Kolejność nauki: Podstawy ekologii → funkcjonowanie ekosystemów → presje środowiskowe → '
                           'technologie ochronne → ekonomia i polityka środowiskowa.\n'
                           '\n'
                           '1. W pierwszej kolejności — Po polsku: Jan Krystek — „Ochrona środowiska dla inżynierów” '
                           '(PWN); January Weiner — „Życie i ewolucja biosfery. Podręcznik ekologii ogólnej” (PWN); '
                           'Czesława Rosik-Dulewska — „Podstawy gospodarki odpadami” (PWN); bezpłatne materiały '
                           'Politechniki Śląskiej i OpenAGH dot. ochrony wód, powietrza i gleby; raporty GIOŚ '
                           '(Państwowy Monitoring Środowiska) oraz serwis Europejskiej Agencji Środowiska po polsku '
                           '(EEA PL).\n'
                           '2. Uzupełniająco: ESA Education (Ziemia, klimat, obserwacja środowiska) oraz raporty IPCC '
                           'i IPBES.',
                'url': 'https://www.polsl.pl/',
                'links': [{'label': '🇵🇱 Politechnika Śląska — Podstawy ochrony środowiska po polsku: '
                                    'https://www.polsl.pl/',
                           'url': 'https://www.polsl.pl/'},
                          {'label': '🇵🇱 Wydawnictwo Naukowe PWN — Jan Krystek „Ochrona środowiska dla inżynierów” oraz '
                                    'January Weiner „Życie i ewolucja biosfery”',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇵🇱 GIOŚ — Państwowy Monitoring Środowiska w Polsce (wody, powietrze, gleby)',
                           'url': 'https://www.gios.gov.pl/'},
                          {'label': '🇵🇱 Europejska Agencja Środowiska (EEA w języku polskim)',
                           'url': 'https://www.eea.europa.eu/pl'},
                          {'label': '🌍 ESA Education — Ziemia, klimat i obserwacja środowiska: '
                                    'https://education.esa.int/teach-with-space/',
                           'url': 'https://education.esa.int/teach-with-space/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T14:20:00Z'},
               {'id': 'mat-1',
                'trackId': 'E',
                'branchTopic': 'Filozofia nauki: dowód, hipoteza, teoria i granice modeli.',
                'subprojectId': None,
                'title': 'Granice modeli formalnych a interpretacja stanów umysłowych i biologicznych (Heller, '
                         'Miłkowski & Poczobut, SEP)',
                'type': 'Artykuł / Notatka przekrojowa',
                'author': 'Administrator',
                'content': 'Rozróżnienie między symulacją składniową (syntaktyczną) a realizacją właściwości '
                           'przyczynowych układu fizycznego — punkt styku Projektu B, C oraz E. W pierwszej kolejności '
                           'opracowania polskojęzyczne (Centrum Kopernika, M. Heller, M. Miłkowski & R. Poczobut).',
                'url': 'https://ccpress.pl/',
                'links': [{'label': '🇵🇱 Centrum Kopernika / CCPress — Filozofia nauki i granice modeli matematycznych',
                           'url': 'https://ccpress.pl/'},
                          {'label': '🇬🇧 Stanford Encyclopedia of Philosophy — Models in Science',
                           'url': 'https://plato.stanford.edu/entries/models-science/'},
                          {'label': '🇬🇧 SEP — The Chinese Room Argument & Syntax vs Semantics',
                           'url': 'https://plato.stanford.edu/entries/chinese-room/'}],
                'status': 'approved',
                'createdAt': '2026-10-25T11:50:00Z'},
               {'id': 'mat-2',
                'trackId': 'B',
                'branchTopic': 'Neurobiologia i neuronauka obliczeniowa.',
                'subprojectId': 'sub-1',
                'title': 'Zestawienie rozdzielczości czasowo-przestrzennej metod neuroobrazowania (EEG, fNIRS, fMRI, '
                         'ECoG)',
                'type': 'Zestaw danych / Opracowanie',
                'author': 'Ireneusz',
                'content': 'Porównanie pasma przenoszenia, stosunku sygnału do szumu (SNR) oraz biokompatybilności '
                           'długoterminowej dla zastosowań w Projektach A i B.',
                'url': 'https://ksiegarnia.pwn.pl/',
                'links': [{'label': '🇵🇱 Wydawnictwo Naukowe PWN — Neurobiologia i metody neuroobrazowania (Kalat, '
                                    'Longstaff)',
                           'url': 'https://ksiegarnia.pwn.pl/'},
                          {'label': '🇬🇧 Physiological Reviews — Brain-Machine Interfaces (Lebedev & Nicolelis)',
                           'url': 'https://doi.org/10.1152/physrev.00027.2016'}],
                'status': 'approved',
                'createdAt': '2026-10-25T13:10:00Z'}],
 'graphLinks': [{'id': 'lnk-1',
                 'source': 'A',
                 'target': 'B',
                 'label': 'Interfejsy mózg–komputer i dekodowanie sygnałów nerwowych',
                 'status': 'approved'},
                {'id': 'lnk-2',
                 'source': 'B',
                 'target': 'C',
                 'label': 'Fizyczne i neuromorficzne modele sieci neuronalnych',
                 'status': 'approved'},
                {'id': 'lnk-3',
                 'source': 'A',
                 'target': 'D',
                 'label': 'Inżynieria tkankowa, sztuczne narządy i medycyna regeneracyjna',
                 'status': 'approved'},
                {'id': 'lnk-4',
                 'source': 'F',
                 'target': 'G',
                 'label': 'Zamknięte obiegi materii (BLSS) vs. ziemska biosfera i ekologia',
                 'status': 'approved'},
                {'id': 'lnk-5',
                 'source': 'A',
                 'target': 'F',
                 'label': 'Medycyna kosmiczna, ochrona organizmu i robotyka autonomiczna',
                 'status': 'approved'},
                {'id': 'lnk-6',
                 'source': 'D',
                 'target': 'F',
                 'label': 'Biologia regeneracji i odporność radiacyjna w długich misjach',
                 'status': 'approved'},
                {'id': 'lnk-7',
                 'source': 'E',
                 'target': 'A',
                 'label': 'Filozofia techniki i etyka ulepszania człowieka',
                 'status': 'approved'},
                {'id': 'lnk-8',
                 'source': 'E',
                 'target': 'B',
                 'label': 'Filozofia umysłu, świadomość i granice modeli obliczeniowych',
                 'status': 'approved'},
                {'id': 'lnk-9',
                 'source': 'E',
                 'target': 'D',
                 'label': 'Bioetyka edycji genomu i granice tworzenia organizmów',
                 'status': 'approved'},
                {'id': 'lnk-10',
                 'source': 'E',
                 'target': 'F',
                 'label': 'Etyka ekspansji kosmicznej i ochrona planetarna',
                 'status': 'approved'},
                {'id': 'lnk-11',
                 'source': 'E',
                 'target': 'G',
                 'label': 'Odpowiedzialność międzypokoleniowa i filozofia przyrody',
                 'status': 'approved'},
                {'id': 'lnk-12',
                 'source': 'H',
                 'target': 'B',
                 'label': 'Zasilanie centrów obliczeniowych AI i emulacji mózgu (WBE) przez reaktory SMR/HTGR',
                 'status': 'approved'},
                {'id': 'lnk-13',
                 'source': 'H',
                 'target': 'C',
                 'label': 'Neutronowe domieszkowanie krzemu (reaktor MARIA) i efektywność energetyczna układów '
                          'neuromorficznych',
                 'status': 'approved'},
                {'id': 'lnk-14',
                 'source': 'H',
                 'target': 'F',
                 'label': 'Kosmiczne mikroreaktory jądrowe (Kilopower), generatory RTG i napędy jądrowe (NTP/NEP) dla '
                          'misji załogowych',
                 'status': 'approved'},
                {'id': 'lnk-15',
                 'source': 'H',
                 'target': 'G',
                 'label': 'Zeroemisyjna energetyka jądrowa i termojądrowa, kogeneracja HTGR i produkcja wodoru dla '
                          'ochrony klimatu Ziemi',
                 'status': 'approved'},
                {'id': 'lnk-16',
                 'source': 'H',
                 'target': 'A',
                 'label': 'Medycyna nuklearna, radioizotopy diagnostyczne (SPECT/PET) i mikrobaterie betawoltaiczne do '
                          'implantów',
                 'status': 'approved'},
                {'id': 'lnk-17',
                 'source': 'H',
                 'target': 'D',
                 'label': 'Radiobiologia molekularna, naprawa uszkodzeń DNA po napromieniowaniu i radiofarmaceutyki '
                          'celowane',
                 'status': 'approved'},
                {'id': 'lnk-18',
                 'source': 'E',
                 'target': 'H',
                 'label': 'Filozofia i etyka energii jądrowej: bezpieczeństwo systemowe i odpowiedzialność '
                          'międzypokoleniowa',
                 'status': 'approved'}],
 'manhattanSystem': {'codename': 'MED-G15 // MANHATTAN DISTRIBUTED SYSTEM',
                     'startCalendarYear': 2026,
                     'doctrine': {'titlePl': 'Doktryna Rozproszonego Systemu Projektowego „Manhattan Golem 15”',
                                  'titleEn': "Doctrine of the 'Manhattan Golem 15' Distributed Project System",
                                  'summaryPl': 'Architektura organizacyjna wzorowana na Projekcie Manhattan (Dual '
                                               'Command: Sztab Administracyjno-Inżynieryjny + Rozproszone Ośrodki '
                                               'Badawcze). System rozpoczyna się od 3-letniego fundamentu studiów '
                                               'Administracji (Lata 1–3), po którym następuje nieprzerwany ciąg '
                                               '5-letnich studiów magisterskich z każdej wybranej tematyki '
                                               'realizowanych ściśle z rzędu (3 + 5×N lat). Równolegle cel nadrzędny '
                                               'ulega kontrolowanemu rozszczepieniu (Fission) w bazie operacyjnej '
                                               'zarządzanej przez wyspecjalizowane Agenty AI.',
                                  'summaryEn': 'Organizational architecture modeled on the Manhattan Project (Dual '
                                               'Command: Administrative-Engineering HQ + Compartmentalized Distributed '
                                               'Labs). The timeline begins with a mandatory 3-year Administration '
                                               'degree (Years 1–3), followed by a continuous back-to-back sequence of '
                                               "5-year Master's curricula for each selected discipline (3 + 5×N "
                                               'years). Simultaneously, the overarching goal undergoes controlled '
                                               'chain-reaction fission across a project database orchestrated by '
                                               'specialized AI Agents.',
                                  'rulesPl': ['1. Prymat Sztabu Administracyjnego (Lata 1–3): Zanim ruszą 5-letnie '
                                              'bloki badawcze, właściciel buduje aparat prawny, finansowy, logistyczny '
                                              'i regulacyjny (prawo B+R, atomowe, medyczne, kosmiczne i nadzór nad '
                                              'AI).',
                                              '2. Sekwencyjna Głębia Akademicka (5 lat z rzędu na każdą wybraną '
                                              'tematykę): Brak powierzchownej wielozadaniowości — każda wybrana '
                                              'dziedzina otrzymuje pełny 5-letni cykl studiów I+II stopnia (10 '
                                              'semestrów, 300 ECTS) realizowany jeden po drugim.',
                                              '3. Kompartmentalizacja Ośrodków (5 Sektorów Manhattan): Prace są '
                                              'rozproszone pomiędzy autonomiczne laboratoria (District W-0, Los Alamos '
                                              'Y-15, Oak Ridge X-10, Hanford B-7, Trinity-Biosphere T-9).',
                                              '4. Reakcja Łańcuchowa Agentów AI (Graf Rozszczepień): Każdy złożony '
                                              'problem badawczy jest rozszczepiany przez Agenta-Kierownika na mniejsze '
                                              'fragmenty robocze oraz neutrony międzyścieżkowe zasilające sąsiednie '
                                              'projekty.'],
                                  'rulesEn': ['1. Primacy of Administrative Command (Years 1–3): Before 5-year '
                                              'scientific blocks begin, the owner establishes legal, financial, '
                                              'logistical, and regulatory mastery (R&D, nuclear, medical, space, and '
                                              'AI law).',
                                              '2. Sequential Academic Depth (5 consecutive years per selected topic): '
                                              'Zero shallow multitasking — every selected topic receives a full 5-year '
                                              'B.Sc.+M.Sc. cycle (10 semesters, 300 ECTS) executed back-to-back.',
                                              '3. Site Compartmentalization (5 Manhattan Sectors): Research is '
                                              'distributed across autonomous sites (District W-0, Los Alamos Y-15, Oak '
                                              'Ridge X-10, Hanford B-7, Trinity-Biosphere T-9).',
                                              '4. AI-Agent Chain Reaction (Fission Graph): Every complex research '
                                              'challenge is fissioned by a Director AI Agent into atomic work packages '
                                              'and cross-sector neutrons feeding neighboring tracks.']},
                     'sites': [{'id': 'SITE-W0',
                                'code': 'DISTRICT W-0',
                                'historicalAnalog': 'Washington HQ & Oak Ridge Admin',
                                'namePl': 'Sztab Centralny Administracji, Prawa i Epistemologii',
                                'nameEn': 'Central HQ for Administration, Law & Epistemology',
                                'color': '#f59e0b',
                                'clearance': 'POZIOM OMEGA (DYREKCJA)',
                                'scopePl': '3-letnie studia Administracji, prawo sektorowe (atomowe, medyczne, '
                                           'kosmiczne, AI), finanse B+R oraz Projekt E (Filozofia i rygor '
                                           'epistemiczny).',
                                'scopeEn': '3-year Administration core, sector law (nuclear, medical, space, AI), R&D '
                                           'finance, and Project E (Philosophy & epistemic rigor).',
                                'linkedIds': ['ADMIN-3Y', 'E']},
                               {'id': 'SITE-Y15',
                                'code': 'LOS ALAMOS Y-15',
                                'historicalAnalog': 'Site Y — Los Alamos Theoretical & Computing Division',
                                'namePl': 'Laboratorium Teorii, Obliczeń, AI i Cyfrowego Umysłu',
                                'nameEn': 'Laboratory for Theory, Computing, AI & Digital Mind',
                                'color': '#38bdf8',
                                'clearance': 'POZIOM ALFA-TEORIA',
                                'scopePl': 'Matematyka (FND-1), Informatyka (FND-2), Programowanie (FND-3), AI (FND-8) '
                                           'oraz Projekt B (Cyfrowy umysł / WBE) i Projekt C (Maszyny analogowe i '
                                           'neuromorficzne).',
                                'scopeEn': 'Mathematics (FND-1), CS (FND-2), Programming (FND-3), AI (FND-8), Project '
                                           'B (Digital Mind / WBE), and Project C (Analog & Neuromorphic Computing).',
                                'linkedIds': ['FND-1', 'FND-2', 'FND-3', 'FND-8', 'B', 'C']},
                               {'id': 'SITE-X10',
                                'code': 'OAK RIDGE X-10',
                                'historicalAnalog': 'Site X — Clinton Pile Reactor & Electromagnetic Plant',
                                'namePl': 'Kompleks Fizyki, Elektroniki i Mocy Jądrowej / Fuzji',
                                'nameEn': 'Physics, Electronics & Nuclear/Fusion Power Complex',
                                'color': '#f43f5e',
                                'clearance': 'POZIOM SIGMA-ATOM',
                                'scopePl': 'Fizyka (FND-4), Elektronika (FND-5) oraz Super-Projekt H (Reaktory SMR, '
                                           'HTGR-POLA, MARIA, fuzja termojądrowa i architektura mocy dla A–G).',
                                'scopeEn': 'Physics (FND-4), Electronics (FND-5), and Super-Project H (SMR, HTGR-POLA, '
                                           'MARIA reactor, nuclear fusion, and power architecture for A–G).',
                                'linkedIds': ['FND-4', 'FND-5', 'H']},
                               {'id': 'SITE-B7',
                                'code': 'HANFORD B-7',
                                'historicalAnalog': 'Site W — Hanford Chemical & Synthesis Complex',
                                'namePl': 'Kompleks Chemii, Biologii, Neurobioniki i Bioinżynierii',
                                'nameEn': 'Chemistry, Biology, Neurobionics & Bioengineering Complex',
                                'color': '#10b981',
                                'clearance': 'POZIOM BIO-DELTA',
                                'scopePl': 'Chemia (FND-6), Biologia (FND-7) oraz Projekt A (Człowiek '
                                           'biocyfrowo-robotyczny, BCI) i Projekt D (Organoidy, inżynieria tkankowa, '
                                           'biologia syntetyczna).',
                                'scopeEn': 'Chemistry (FND-6), Biology (FND-7), Project A (Bio-Digital-Robotic Human, '
                                           'BCI), and Project D (Organoids, tissue engineering, synthetic biology).',
                                'linkedIds': ['FND-6', 'FND-7', 'A', 'D']},
                               {'id': 'SITE-T9',
                                'code': 'TRINITY T-9',
                                'historicalAnalog': 'Trinity Proving Ground & Field Systems Integration',
                                'namePl': 'Poligon Integracji Środowiskowej: Kosmos (F) ↔ Biosfera Ziemi (G)',
                                'nameEn': 'Environmental Proving Ground: Space (F) ↔ Earth Biosphere (G)',
                                'color': '#a855f7',
                                'clearance': 'POZIOM TERRA-ORBIT',
                                'scopePl': 'Projekt F (Człowiek w kosmosie, zamknięte obiegi BLSS, ochrona radiacyjna) '
                                           'oraz Projekt G (Adaptacja na Ziemi, ochrona ekosystemów i klimatu).',
                                'scopeEn': 'Project F (Humans in Space, closed-loop BLSS, radiation shielding) and '
                                           'Project G (Earth adaptation, ecosystem & climate protection).',
                                'linkedIds': ['FND-4', 'FND-6', 'FND-7', 'F', 'G']}],
                     'adminCore3Y': {'id': 'ADMIN-3Y',
                                     'durationYears': 3,
                                     'semesters': 6,
                                     'ects': 180,
                                     'siteId': 'SITE-W0',
                                     'sourceLang': 'PL+EN',
                                     'titlePl': 'Etap Zerowy (Obowiązkowy Rdzeń Manhattan): 3 Lata Studiów '
                                                'Administracji (Licencjat — 180 ECTS)',
                                     'titleEn': 'Stage Zero (Mandatory Manhattan Core): 3-Year Administration Degree '
                                                '(B.A. — 180 ECTS)',
                                     'subtitlePl': 'Fundament organizacyjny, prawny, finansowy i regulacyjny '
                                                   'otwierający kaskadę 5-letnich studiów specjalistycznych',
                                     'subtitleEn': 'Organizational, legal, financial, and regulatory foundation '
                                                   'preceding the continuous sequence of 5-year specialist degrees',
                                     'completedYears': [],
                                     'years': [{'year': 1,
                                                'semesters': 'Semestry I–II (60 ECTS)',
                                                'titlePl': 'Rok 1 Administracji: Architektura Prawna, Teoria '
                                                           'Organizacji i Logika Systemowa',
                                                'titleEn': 'Year 1 Administration: Legal Architecture, Organization '
                                                           'Theory & Systems Logic',
                                                'coursesPl': ['🇵🇱 [PL] Wstęp do prawoznawstwa, logika prawnicza i '
                                                              'teoria wykładni norm',
                                                              '🇵🇱/🇬🇧 [PL+EN] Nauka o administracji i teoria '
                                                              'organizacji rozproszonych (modele Webera, Manhattan '
                                                              'MED, DARPA)',
                                                              '🇵🇱 [PL] Prawo konstytucyjne i ustrój instytucji '
                                                              'publicznych oraz agencji międzynarodowych (UE, ONZ, '
                                                              'ESA, MAEA)',
                                                              '🇵🇱 [PL] Ekonomia sektora publicznego, finanse B+R i '
                                                              'budżetowanie zadaniowe',
                                                              '🇵🇱 [PL] Statystyka, bazy danych i systemy '
                                                              'teleinformatyczne w administracji (EZD, bezpieczeństwo '
                                                              'rejestrów)'],
                                                'coursesEn': ['🇵🇱 [PL] Jurisprudence fundamentals, legal logic, and '
                                                              'statutory interpretation',
                                                              '🇵🇱/🇬🇧 [PL+EN] Public administration science & '
                                                              'distributed organization theory (Weber, Manhattan MED, '
                                                              'DARPA models)',
                                                              '🇵🇱 [PL] Constitutional law & international regulatory '
                                                              'bodies (EU, UN, ESA, IAEA)',
                                                              '🇵🇱 [PL] Public economics, R&D finance, and '
                                                              'mission-oriented budgeting',
                                                              '🇵🇱 [PL] Administrative statistics, databases, and '
                                                              'e-governance information security'],
                                                'deliverablePl': 'Statut organizacyjny i matryca uprawnień Sztabu '
                                                                 'Centralnego Golem 15 (District W-0).',
                                                'deliverableEn': 'Organizational charter and clearance matrix for '
                                                                 'Golem 15 Central HQ (District W-0).'},
                                               {'year': 2,
                                                'semesters': 'Semestry III–IV (60 ECTS)',
                                                'titlePl': 'Rok 2 Administracji: Postępowanie Administracyjne, Patenty '
                                                           'Deep-Tech i Inżynieria Programów',
                                                'titleEn': 'Year 2 Administration: Administrative Procedure, Deep-Tech '
                                                           'IP & Program Engineering',
                                                'coursesPl': ['🇵🇱 [PL] Postępowanie administracyjne (KPA) i '
                                                              'sądowoadministracyjne (decyzje środowiskowe, '
                                                              'lokalizacyjne i regulacyjne)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Prawo cywilne, konsorcja badawcze oraz '
                                                              'własność intelektualna i prawo patentowe (UPRP, EPO, '
                                                              'WIPO)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Zamówienia publiczne w nauce, granty '
                                                              'badawcze (NCN, NCBR, Horizon Europe) i logistyka '
                                                              'aparaturowa',
                                                              '🇬🇧 [EN] Zarządzanie megaprojektami technologicznymi '
                                                              '(NASA Systems Engineering, PRINCE2, analiza ścieżki '
                                                              'krytycznej)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Cyberbezpieczeństwo, ochrona tajemnicy '
                                                              'badawczej i kompartmentalizacja dostępu'],
                                                'coursesEn': ['🇵🇱 [PL] Administrative & judicial-administrative '
                                                              'procedure (environmental, siting, and licensing '
                                                              'decisions)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Civil law, R&D consortia, intellectual '
                                                              'property, and patent law (UPRP, EPO, WIPO)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Scientific public procurement, research '
                                                              'grants (NCN, NCBR, Horizon Europe), and lab logistics',
                                                              '🇬🇧 [EN] Megaproject management (NASA Systems '
                                                              'Engineering, PRINCE2, Critical Path Method)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Cybersecurity, research secrecy '
                                                              'protection, and compartmentalized access governance'],
                                                'deliverablePl': 'System obiegu dokumentacji badawczej, polityka IP '
                                                                 'oraz procedury zakupowo-logistyczne dla 5 ośrodków.',
                                                'deliverableEn': 'Research documentation workflow, IP policy, and '
                                                                 'procurement protocols across all 5 distributed '
                                                                 'sites.'},
                                               {'year': 3,
                                                'semesters': 'Semestry V–VI (60 ECTS)',
                                                'titlePl': 'Rok 3 Administracji: Prawo Sektorów Strategicznych (Atom, '
                                                           'Bioetyka, Kosmos, AI) i Dyplom',
                                                'titleEn': 'Year 3 Administration: Strategic Sector Law (Nuclear, '
                                                           'Bioethics, Space, AI) & B.A. Thesis',
                                                'coursesPl': ['🇵🇱/🇬🇧 [PL+EN] Prawo atomowe, dozór jądrowy (PAA, '
                                                              'Euratom, IAEA) i certyfikacja reaktorów SMR/HTGR (pod '
                                                              'Super-Projekt H)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Prawo medyczne, komisje bioetyczne, '
                                                              'badania kliniczne i regulacje wyrobów medycznych/BCI '
                                                              'MDR (pod Projekty A i D)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Międzynarodowe prawo kosmiczne (POLSA, '
                                                              'traktaty ONZ) oraz prawo ochrony środowiska i klimatu '
                                                              '(pod Projekty F i G)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Regulacje sztucznej inteligencji (EU AI '
                                                              'Act), audyt algorytmiczny i nadzór nad flotą Agentów AI '
                                                              '(pod Projekty B, C, E)',
                                                              '🇵🇱 [PL] Seminarium dyplomowe (Licencjat): Projekt '
                                                              'rozproszonego instytutu badawczego na kanwie Projektu '
                                                              'Manhattan'],
                                                'coursesEn': ['🇵🇱/🇬🇧 [PL+EN] Nuclear law, radiological oversight (PAA, '
                                                              'Euratom, IAEA) & SMR/HTGR licensing (for Super-Project '
                                                              'H)',
                                                              '🇵🇱/🇬🇧 [PL+EN] Medical law, bioethics committees, '
                                                              'clinical trials & BCI medical device regulations (for '
                                                              'Projects A & D)',
                                                              '🇵🇱/🇬🇧 [PL+EN] International space law (POLSA, UN '
                                                              'treaties) & environmental/climate protection law (for '
                                                              'Projects F & G)',
                                                              '🇵🇱/🇬🇧 [PL+EN] AI governance (EU AI Act), algorithmic '
                                                              'auditing & multi-agent AI supervision (for Projects B, '
                                                              'C, E)',
                                                              '🇵🇱 [PL] B.A. Thesis Seminar: Blueprint of a '
                                                              'Manhattan-style distributed research institute'],
                                                'deliverablePl': 'Obrona licencjatu z Administracji i pełne '
                                                                 'odblokowanie sekwencji 5-letnich studiów '
                                                                 'kierunkowych.',
                                                'deliverableEn': 'Administration B.A. defense and full operational '
                                                                 'clearance for the continuous 5-year specialist study '
                                                                 'queue.'}]},
                     'fiveYearCatalog': [{'id': 'STU-FND-1',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-1',
                                          'siteId': 'SITE-Y15',
                                          'icon': '📐',
                                          'color': '#38bdf8',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Matematyka i Logika Matematyczna (5 lat — I+II stopień)',
                                          'titleEn': 'Mathematics & Mathematical Logic (5 Years — B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Logika formalna, teoria mnogości, analiza matematyczna '
                                                           'I–II, algebra liniowa z geometrią (OpenAGH, Skoczylas, '
                                                           'Strang).',
                                                     'en': 'Formal logic, set theory, calculus I–II, linear algebra '
                                                           'with geometry (OpenAGH, Strang).'},
                                                    {'year': 2,
                                                     'pl': 'Równania różniczkowe zwyczajne i cząstkowe, topologia '
                                                           'ogólna, analiza zespolona, matematyka dyskretna i teoria '
                                                           'grafów.',
                                                     'en': 'ODEs & PDEs, general topology, complex analysis, discrete '
                                                           'math & graph theory.'},
                                                    {'year': 3,
                                                     'pl': 'Rachunek prawdopodobieństwa, statystyka matematyczna, '
                                                           'analiza funkcjonalna, metody numeryczne i obrona I '
                                                           'stopnia.',
                                                     'en': 'Probability theory, mathematical statistics, functional '
                                                           'analysis, numerical methods & B.Sc. thesis.'},
                                                    {'year': 4,
                                                     'pl': 'Układy dynamiczne i teoria chaosu, geometria różniczkowa i '
                                                           'rachunek tensorowy (Penrose), teoria informacji i '
                                                           'entropia.',
                                                     'en': 'Dynamical systems & chaos, differential geometry & tensor '
                                                           'calculus (Penrose), information theory.'},
                                                    {'year': 5,
                                                     'pl': 'Procesy stochastyczne, wnioskowanie bayesowskie, topologia '
                                                           'algebraiczna konektomów i praca magisterska dla Projektów '
                                                           'B/C/H.',
                                                     'en': 'Stochastic processes, Bayesian inference, algebraic '
                                                           'topology of connectomes & M.Sc. thesis for B/C/H.'}]},
                                         {'id': 'STU-FND-2',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-2',
                                          'siteId': 'SITE-Y15',
                                          'icon': '💻',
                                          'color': '#60a5fa',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Informatyka Teoretyczna i Systemowa (5 lat — I+II stopień)',
                                          'titleEn': 'Computer Science & Distributed Systems (5 Years — B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Logika układów cyfrowych i architektura komputerów '
                                                           '(Petzold), algorytmy i struktury danych (Cormen, Ważniak '
                                                           'MIMUW).',
                                                     'en': 'Digital logic & computer architecture (Petzold), '
                                                           'algorithms & data structures (Cormen).'},
                                                    {'year': 2,
                                                     'pl': 'Systemy operacyjne, programowanie współbieżne, sieci '
                                                           'komputerowe, relacyjne i grafowe bazy danych.',
                                                     'en': 'Operating systems, concurrency, computer networks, '
                                                           'relational & graph databases.'},
                                                    {'year': 3,
                                                     'pl': 'Teoria obliczeń i złożoności, systemy czasu rzeczywistego '
                                                           '(RTOS), kryptografia stosowana i projekt inżynierski.',
                                                     'en': 'Theory of computation & complexity, RTOS, applied '
                                                           'cryptography & B.Eng. project.'},
                                                    {'year': 4,
                                                     'pl': 'Systemy rozproszone wielkiej skali, obliczenia wysokiej '
                                                           'wydajności (HPC / klastry GPU), architektury odporne na '
                                                           'błędy (fault-tolerant).',
                                                     'en': 'Large-scale distributed systems, HPC / GPU clusters, '
                                                           'fault-tolerant space/medical architectures.'},
                                                    {'year': 5,
                                                     'pl': 'Reprezentacja wiedzy, ontologie grafowe, bezpieczeństwo '
                                                           'systemów krytycznych i praca magisterska z architektury '
                                                           'rozproszonej.',
                                                     'en': 'Knowledge representation, graph ontologies, critical '
                                                           'systems security & M.Sc. thesis.'}]},
                                         {'id': 'STU-FND-3',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-3',
                                          'siteId': 'SITE-Y15',
                                          'icon': '⌨️',
                                          'color': '#818cf8',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Inżynieria Oprogramowania i Symulacji Naukowych (5 lat — I+II '
                                                     'stopień)',
                                          'titleEn': 'Software Engineering & Scientific Simulation (5 Years — '
                                                     'B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Programowanie strukturalne, obiektowe i funkcyjne (Python, '
                                                           'C, C++), kontrola wersji Git i testowanie jednostkowe.',
                                                     'en': 'Procedural, OOP & functional programming (Python, C, C++), '
                                                           'Git & unit testing.'},
                                                    {'year': 2,
                                                     'pl': 'Programowanie systemowe i niskopoziomowe (Rust, C++20), '
                                                           'interfejsy sprzętowe, sterowniki i akwizycja danych '
                                                           'pomiarowych.',
                                                     'en': 'Systems & low-level programming (Rust, C++20), hardware '
                                                           'APIs & sensor data acquisition.'},
                                                    {'year': 3,
                                                     'pl': 'Obliczenia naukowe (NumPy, SciPy, Julia), architektura '
                                                           'aplikacji webowych/mobilnych i inżynierski system '
                                                           'symulacyjny.',
                                                     'en': 'Scientific computing (NumPy, SciPy, Julia), web/mobile '
                                                           'architecture & B.Eng. simulation platform.'},
                                                    {'year': 4,
                                                     'pl': 'Symulatory fizyczne, biologiczne i neuronalne (NEURON, '
                                                           'Brian2, OpenMM), programowanie równoległe CUDA/Triton.',
                                                     'en': 'Physical, biological & neural simulators (NEURON, Brian2, '
                                                           'OpenMM), CUDA/Triton parallel kernels.'},
                                                    {'year': 5,
                                                     'pl': 'Weryfikacja formalna kodu krytycznego, reprodukowalne '
                                                           'potoki badawcze MLOps i magisterium z inżynierii '
                                                           'symulacyjnej.',
                                                     'en': 'Formal verification of safety-critical code, reproducible '
                                                           'MLOps pipelines & M.Sc. thesis.'}]},
                                         {'id': 'STU-FND-4',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-4',
                                          'siteId': 'SITE-X10',
                                          'icon': '⚛️',
                                          'color': '#f59e0b',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Fizyka Techniczna, Kwantowa i Jądrowa (5 lat — I+II stopień)',
                                          'titleEn': 'Technical, Quantum & Nuclear Physics (5 Years — B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Mechanika klasyczna i relatywistyczna, fale i optyka, '
                                                           'pracownia fizyczna I (OpenStax Fizyka, Feynman).',
                                                     'en': 'Classical & relativistic mechanics, waves & optics, '
                                                           'physics lab I (OpenStax, Feynman).'},
                                                    {'year': 2,
                                                     'pl': 'Elektrodynamika klasyczna (równania Maxwella), '
                                                           'termodynamika i fizyka statystyczna, mechanika analityczna '
                                                           'Lagrange’a–Hamiltona.',
                                                     'en': 'Classical electrodynamics (Maxwell), thermodynamics & '
                                                           'statistical physics, Lagrangian/Hamiltonian mechanics.'},
                                                    {'year': 3,
                                                     'pl': 'Mechanika kwantowa I (Griffiths), fizyka ciała stałego i '
                                                           'półprzewodników, podstawy fizyki jądrowej i dyplom I '
                                                           'stopnia.',
                                                     'en': 'Quantum mechanics I (Griffiths), solid-state & '
                                                           'semiconductor physics, nuclear basics & B.Sc.'},
                                                    {'year': 4,
                                                     'pl': 'Fizyka reaktorów jądrowych i transportu neutronów, fizyka '
                                                           'plazmy i syntezy termojądrowej, dozymetria i ochrona '
                                                           'radiacyjna.',
                                                     'en': 'Nuclear reactor physics & neutron transport, plasma '
                                                           'physics & fusion, radiation dosimetry.'},
                                                    {'year': 5,
                                                     'pl': 'Termodynamika nierównowagowa układów żywych, informacja '
                                                           'kwantowa (Nielsen & Chuang) i praca magisterska (Projekty '
                                                           'C/F/H).',
                                                     'en': 'Non-equilibrium thermodynamics of life, quantum '
                                                           'information & M.Sc. thesis (Projects C/F/H).'}]},
                                         {'id': 'STU-FND-5',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-5',
                                          'siteId': 'SITE-X10',
                                          'icon': '🔌',
                                          'color': '#eab308',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Elektronika, Bioelektronika i Układy Neuromorficzne (5 lat — '
                                                     'I+II stopień)',
                                          'titleEn': 'Electronics, Bioelectronics & Neuromorphic Hardware (5 Years — '
                                                     'B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Teoria obwodów elektrycznych, metrologia elektroniczna, '
                                                           'elementy półprzewodnikowe (Horowitz & Hill „Sztuka '
                                                           'elektroniki”).',
                                                     'en': 'Circuit theory, electronic metrology, semiconductor '
                                                           'devices (The Art of Electronics).'},
                                                    {'year': 2,
                                                     'pl': 'Elektronika analogowa (wzmacniacze operacyjne, filtry, '
                                                           'oscylatory), elektronika cyfrowa i języki opisu sprzętu '
                                                           'Verilog/VHDL (FPGA).',
                                                     'en': 'Analog circuits (op-amps, filters, oscillators), digital '
                                                           'logic & FPGA design (Verilog/VHDL).'},
                                                    {'year': 3,
                                                     'pl': 'Mikrokontrolery, systemy wbudowane SoC, cyfrowe '
                                                           'przetwarzanie sygnałów (DSP), przetworniki ADC/DAC i '
                                                           'projekt inżynierski.',
                                                     'en': 'Microcontrollers, embedded SoCs, DSP, precision ADC/DAC & '
                                                           'B.Eng. hardware prototype.'},
                                                    {'year': 4,
                                                     'pl': 'Aparatura biomedyczna niskoszumowa (EEG, ECoG, EMG, '
                                                           'fNIRS), elektronika mocy i sterowanie napędami '
                                                           'bioniczno-robotycznymi.',
                                                     'en': 'Low-noise biomedical front-ends (EEG, ECoG, EMG, fNIRS), '
                                                           'power electronics & bionic actuators.'},
                                                    {'year': 5,
                                                     'pl': 'Układy VLSI, memrystory, procesory neuromorficzne i '
                                                           'fotoniczne oraz praca magisterska dla Projektów A i C.',
                                                     'en': 'VLSI design, memristors, neuromorphic & photonic '
                                                           'processors, and M.Sc. thesis for A & C.'}]},
                                         {'id': 'STU-FND-6',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-6',
                                          'siteId': 'SITE-B7',
                                          'icon': '🧪',
                                          'color': '#10b981',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Chemia, Biochemia i Inżynieria Materiałowa (5 lat — I+II '
                                                     'stopień)',
                                          'titleEn': 'Chemistry, Biochemistry & Biomaterials Engineering (5 Years — '
                                                     'B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Chemia ogólna i nieorganiczna, stechiometria, równowagi '
                                                           'jonowe i analiza jakościowo-ilościowa (OpenStax Chemia, '
                                                           'Bielański).',
                                                     'en': 'General & inorganic chemistry, stoichiometry, ionic '
                                                           'equilibria & analytical lab.'},
                                                    {'year': 2,
                                                     'pl': 'Chemia organiczna I–II (mechanizmy reakcji, stereochemia, '
                                                           'synteza), chemia fizyczna, termodynamika chemiczna i '
                                                           'elektrochemia.',
                                                     'en': 'Organic chemistry I–II, physical chemistry, chemical '
                                                           'thermodynamics & electrochemistry.'},
                                                    {'year': 3,
                                                     'pl': 'Biochemia strukturalna i metaboliczna (Stryer: białka, '
                                                           'enzymy, kwasy nukleinowe), spektroskopia (NMR, MS, IR) i '
                                                           'dyplom I stopnia.',
                                                     'en': 'Structural & metabolic biochemistry (Stryer), spectroscopy '
                                                           '(NMR, MS, IR) & B.Sc. thesis.'},
                                                    {'year': 4,
                                                     'pl': 'Chemia polimerów biokompatybilnych i hydrożeli tkankowych, '
                                                           'radiochemia izotopów medycznych i chemia jądrowego cyklu '
                                                           'paliwowego.',
                                                     'en': 'Biocompatible polymers & hydrogels, medical isotope '
                                                           'radiochemistry & nuclear fuel chemistry.'},
                                                    {'year': 5,
                                                     'pl': 'Zamknięte obiegi katalityczne (regeneracja O2/H2O '
                                                           'Sabatiera–Boscha dla kosmosu), chemia środowiska i praca '
                                                           'magisterska.',
                                                     'en': 'Closed-loop catalytic life-support chemistry '
                                                           '(Sabatier/Bosch), environmental chemistry & M.Sc.'}]},
                                         {'id': 'STU-FND-7',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-7',
                                          'siteId': 'SITE-B7',
                                          'icon': '🧬',
                                          'color': '#22c55e',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Biologia Molekularna, Neurobiologia i Fizjologia Człowieka (5 '
                                                     'lat — I+II stopień)',
                                          'titleEn': 'Molecular Biology, Neurobiology & Human Physiology (5 Years — '
                                                     'B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Biologia komórki, histologia, anatomia prawidłowa '
                                                           'człowieka i podstawy ewolucjonizmu (Biologia Campbella, '
                                                           'Alberts).',
                                                     'en': 'Cell biology, histology, human anatomy & evolutionary '
                                                           'biology (Campbell, Alberts).'},
                                                    {'year': 2,
                                                     'pl': 'Biologia molekularna, genetyka klasyczna i genomika (Brown '
                                                           '„Genomy”), mikrobiologia i immunologia podstawowa.',
                                                     'en': 'Molecular biology, genetics & genomics (Brown), '
                                                           'microbiology & immunology.'},
                                                    {'year': 3,
                                                     'pl': 'Fizjologia układów człowieka (nerwowy, krążenia, '
                                                           'oddechowy, hormonalny), biofizyka błon komórkowych i '
                                                           'licencjat.',
                                                     'en': 'Human systems physiology, membrane biophysics & B.Sc. '
                                                           'thesis.'},
                                                    {'year': 4,
                                                     'pl': 'Neurobiologia komórkowa i systemowa (Kandel), '
                                                           'elektrofizjologia synaps, embriologia, komórki macierzyste '
                                                           'i organoidy.',
                                                     'en': 'Cellular & systems neurobiology (Kandel), synaptic '
                                                           'electrophysiology, stem cells & organoids.'},
                                                    {'year': 5,
                                                     'pl': 'Ekologia systemowa biosfery, fizjologia ekstremalna '
                                                           '(mikrograwitacja, radiacja) i praca magisterska (Projekty '
                                                           'A/B/D/F/G).',
                                                     'en': 'Systems biosphere ecology, extreme space physiology & '
                                                           'M.Sc. thesis (Projects A/B/D/F/G).'}]},
                                         {'id': 'STU-FND-8',
                                          'group': 'FOUNDATION',
                                          'refId': 'FND-8',
                                          'siteId': 'SITE-Y15',
                                          'icon': '🤖',
                                          'color': '#a855f7',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Sztuczna Inteligencja, Uczenie Maszynowe i Systemy Wieloagentowe '
                                                     '(5 lat — I+II stopień)',
                                          'titleEn': 'Artificial Intelligence, Deep Learning & Multi-Agent Systems (5 '
                                                     'Years — B.Sc.+M.Sc.)',
                                          'years': [{'year': 1,
                                                     'pl': 'Matematyczne podstawy ML, optymalizacja wypukła, klasyczne '
                                                           'uczenie maszynowe i eksploracja danych (Géron, '
                                                           'scikit-learn).',
                                                     'en': 'Mathematical foundations of ML, convex optimization & '
                                                           'classical machine learning (Géron).'},
                                                    {'year': 2,
                                                     'pl': 'Głębokie sieci neuronowe (PyTorch/JAX): architektury CNN, '
                                                           'rekurencyjne, Transformery i modele generatywne.',
                                                     'en': 'Deep neural networks (PyTorch/JAX): CNNs, sequence models, '
                                                           'Transformers & generative models.'},
                                                    {'year': 3,
                                                     'pl': 'Uczenie ze wzmocnieniem (RL), sterowanie robotyczne, wizja '
                                                           'komputerowa, przetwarzanie języka i projekt inżynierski '
                                                           'AI.',
                                                     'en': 'Reinforcement learning (RL), robotic control, computer '
                                                           'vision, NLP & B.Eng. AI project.'},
                                                    {'year': 4,
                                                     'pl': 'Impulsowe sieci neuronowe (SNN), dekodowanie sygnałów '
                                                           'mózgowych BCI/fMRI, AI w biologii strukturalnej i fizyce '
                                                           'reaktorowej.',
                                                     'en': 'Spiking Neural Networks (SNN), BCI/fMRI neural decoding, '
                                                           'AI for structural biology & reactor physics.'},
                                                    {'year': 5,
                                                     'pl': 'Architektury wieloagentowe (MAS), interpretowalność (XAI), '
                                                           'alignment, bezpieczeństwo AI i praca magisterska.',
                                                     'en': 'Multi-Agent Systems (MAS), interpretability (XAI), AI '
                                                           'safety/alignment & M.Sc. thesis.'}]},
                                         {'id': 'STU-TRK-A',
                                          'group': 'TRACK',
                                          'refId': 'A',
                                          'siteId': 'SITE-B7',
                                          'icon': '🦾',
                                          'color': '#38bdf8',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt A: Inżynieria Biomedyczna, Bionika i Neuroinżynieria (5 '
                                                     'lat)',
                                          'titleEn': 'Project A: Biomedical Engineering, Bionics & Neuroengineering (5 '
                                                     'Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Anatomia i biomechanika układu ruchu, materiałoznawstwo '
                                                           'medyczne, podstawy elektroniki i sygnałów biomedycznych.',
                                                     'en': 'Musculoskeletal biomechanics, medical materials, '
                                                           'biomedical signals & electronics.'},
                                                    {'year': 2,
                                                     'pl': 'Sensory i aktuatory medyczne, biokompatybilność implantów, '
                                                           'przetwarzanie sygnałów EEG/EMG/EKG/fNIRS.',
                                                     'en': 'Medical sensors & actuators, implant biocompatibility, '
                                                           'EEG/EMG/ECG/fNIRS signal processing.'},
                                                    {'year': 3,
                                                     'pl': 'Mechatronika protetyczna, egzoszkielety rehabilitacyjne, '
                                                           'sztuczne narządy wspomagające i projekt inżynierski.',
                                                     'en': 'Prosthetic mechatronics, rehabilitation exoskeletons, '
                                                           'artificial organs & B.Eng. design.'},
                                                    {'year': 4,
                                                     'pl': 'Inwazyjne i nieinwazyjne interfejsy mózg–komputer (BCI), '
                                                           'neurostymulacja zamkniętej pętli i dekodowanie intencji '
                                                           'ruchowej.',
                                                     'en': 'Invasive & non-invasive Brain-Computer Interfaces (BCI), '
                                                           'closed-loop neurostimulation.'},
                                                    {'year': 5,
                                                     'pl': 'Integracja kliniczna człowiek–maszyna, bezpieczeństwo '
                                                           'cybernetyczne implantów i praca magisterska z '
                                                           'neurobioniki.',
                                                     'en': 'Clinical human-machine integration, implant cybersecurity '
                                                           '& M.Sc. thesis in neurobionics.'}]},
                                         {'id': 'STU-TRK-B',
                                          'group': 'TRACK',
                                          'refId': 'B',
                                          'siteId': 'SITE-Y15',
                                          'icon': '🧠',
                                          'color': '#818cf8',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt B: Neuronauka Obliczeniowa i Modelowanie Cyfrowego '
                                                     'Umysłu (5 lat)',
                                          'titleEn': 'Project B: Computational Neuroscience & Digital Mind Modeling (5 '
                                                     'Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Kognitywistyka, neuroanatomia funkcjonalna, psychologia '
                                                           'poznawcza (pamięć, uwaga, percepcja) i modelowanie '
                                                           'matematyczne.',
                                                     'en': 'Cognitive science, functional neuroanatomy, '
                                                           'memory/perception & mathematical modeling.'},
                                                    {'year': 2,
                                                     'pl': 'Biofizyczne modele pojedynczych neuronów (Hodgkin–Huxley, '
                                                           'Izhikevich), plastyczność synaptyczna STDP i kodowanie '
                                                           'neuronalne.',
                                                     'en': 'Biophysical neuron models (Hodgkin-Huxley, Izhikevich), '
                                                           'STDP plasticity & neural coding.'},
                                                    {'year': 3,
                                                     'pl': 'Obrazowanie mózgu (fMRI, MEG, mikroskopia elektronowa), '
                                                           'konektomika grafowa i dyplom licencjacki.',
                                                     'en': 'Neuroimaging (fMRI, MEG, EM), graph connectomics & B.Sc. '
                                                           'thesis.'},
                                                    {'year': 4,
                                                     'pl': 'Wielkoskalowe symulacje sieci korowo-wzgórzowych, '
                                                           'konsolidacja pamięci i cyfrowy sen w sieciach sztucznych i '
                                                           'biologicznych.',
                                                     'en': 'Large-scale thalamocortical simulations, memory '
                                                           'consolidation & digital sleep dynamics.'},
                                                    {'year': 5,
                                                     'pl': ' Metodologia i ograniczenia Whole Brain Emulation (WBE), '
                                                           'problem tożsamości i świadomości oraz praca magisterska.',
                                                     'en': 'Methodology & physical limits of Whole Brain Emulation '
                                                           '(WBE), consciousness & M.Sc. thesis.'}]},
                                         {'id': 'STU-TRK-C',
                                          'group': 'TRACK',
                                          'refId': 'C',
                                          'siteId': 'SITE-Y15',
                                          'icon': '〰️',
                                          'color': '#f59e0b',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt C: Obliczanie Fizyczne, Fotonika i Maszyny '
                                                     'Analogowo-Neuromorficzne (5 lat)',
                                          'titleEn': 'Project C: Physical Computing, Photonics & Analog-Neuromorphic '
                                                     'Machines (5 Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Historia i teoria komputerów analogowych, równania '
                                                           'różniczkowe realizowane w obwodach ciągłych RC/RLC.',
                                                     'en': 'Analog computing theory, continuous differential analyzers '
                                                           '& RC/RLC dynamical circuits.'},
                                                    {'year': 2,
                                                     'pl': 'Nieliniowe układy dynamiczne, obliczenia zbiornikowe '
                                                           '(Reservoir Computing) i oscylatorowe sieci sprzężone.',
                                                     'en': 'Nonlinear dynamical systems, Reservoir Computing & coupled '
                                                           'oscillator networks.'},
                                                    {'year': 3,
                                                     'pl': 'Fizyka memrystorów, macierze skrzyżowane in-memory '
                                                           'computing, energetyka obliczeń (limit Landauera) i projekt '
                                                           'inżynierski.',
                                                     'en': 'Memristor physics, crossbar in-memory computing, Landauer '
                                                           'thermodynamic limits & B.Eng.'},
                                                    {'year': 4,
                                                     'pl': 'Procesory fotoniczne i optyczne mnożenie macierzy, '
                                                           'obliczenia kwantowe i hybrydowe biokomputery (Brainoware).',
                                                     'en': 'Photonic processors & optical matrix multiplication, '
                                                           'quantum & organoid biocomputing.'},
                                                    {'year': 5,
                                                     'pl': 'Projektowanie ultra-energooszczędnych akceleratorów '
                                                           'fizycznych dla AI/BCI i praca magisterska.',
                                                     'en': 'Ultra-low-power physical AI/BCI accelerators & M.Sc. '
                                                           'thesis.'}]},
                                         {'id': 'STU-TRK-D',
                                          'group': 'TRACK',
                                          'refId': 'D',
                                          'siteId': 'SITE-B7',
                                          'icon': '🧫',
                                          'color': '#10b981',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt D: Biotechnologia Medyczna, Inżynieria Tkankowa i '
                                                     'Biologia Syntetyczna (5 lat)',
                                          'titleEn': 'Project D: Medical Biotechnology, Tissue Engineering & Synthetic '
                                                     'Biology (5 Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Biologia komórki i rozwoju, hodowle komórkowe in vitro, '
                                                           'sterylność laboratoryjna i podstawy genetyki molekularnej.',
                                                     'en': 'Developmental cell biology, aseptic cell culture & '
                                                           'molecular genetics.'},
                                                    {'year': 2,
                                                     'pl': 'Inżynieria genetyczna, edycja genomu (CRISPR-Cas, prime '
                                                           'editing), epigenetyka i przeprogramowywanie komórek '
                                                           '(iPSC).',
                                                     'en': 'Genetic engineering, genome editing (CRISPR/prime '
                                                           'editing), epigenetics & iPSC reprogramming.'},
                                                    {'year': 3,
                                                     'pl': 'Biomateriały rusztowaniowe, biodruk 3D tkanek '
                                                           'unaczynionych, bioreaktory perfuzyjne i dyplom I stopnia.',
                                                     'en': 'Scaffold biomaterials, 3D bioprinting of vascularized '
                                                           'tissues, perfusion bioreactors & B.Sc.'},
                                                    {'year': 4,
                                                     'pl': 'Hodowla organoidów (mózgowych, przysadkowych, '
                                                           'wątrobowych), biologia syntetyczna obwodów genowych i '
                                                           'terapie genowe.',
                                                     'en': 'Organoid engineering (cerebral, pituitary, hepatic), '
                                                           'synthetic gene circuits & gene therapies.'},
                                                    {'year': 5,
                                                     'pl': 'Medycyna regeneracyjna i transplantacyjna, analiza '
                                                           'kulturowo-bioetyczna („Frankenstein”) i praca magisterska.',
                                                     'en': 'Regenerative transplantation medicine, bioethical '
                                                           'boundaries & M.Sc. thesis.'}]},
                                         {'id': 'STU-TRK-E',
                                          'group': 'TRACK',
                                          'refId': 'E',
                                          'siteId': 'SITE-W0',
                                          'icon': '⚖️',
                                          'color': '#eab308',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt E: Filozofia Nauki, Umysłu, Technologii i Bioetyka '
                                                     'Stosowana (5 lat)',
                                          'titleEn': 'Project E: Philosophy of Science, Mind, Technology & Applied '
                                                     'Bioethics (5 Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Logika klasyczna i nieklasyczna, epistemologia, teoria '
                                                           'prawdy i historia metodologii nauk przyrodniczych.',
                                                     'en': 'Classical & non-classical logic, epistemology & history of '
                                                           'scientific methodology.'},
                                                    {'year': 2,
                                                     'pl': 'Filozofia nauki (Popper, Kuhn, Lakatos), kryteria '
                                                           'falsyfikowalności, wnioskowanie przyczynowe i status '
                                                           'modeli naukowych.',
                                                     'en': 'Philosophy of science (Popper, Kuhn, Lakatos), '
                                                           'falsifiability, causal inference & scientific models.'},
                                                    {'year': 3,
                                                     'pl': 'Filozofia umysłu i kognitywistyki (funkcjonalizm, '
                                                           'emergencja, problem świadomości, tożsamość osobowa) i '
                                                           'licencjat.',
                                                     'en': 'Philosophy of mind (functionalism, emergence, '
                                                           'consciousness, personal identity) & B.A. thesis.'},
                                                    {'year': 4,
                                                     'pl': 'Bioetyka kliniczna i regulacyjna, etyka inżynierii '
                                                           'genetycznej, neuroetyka (prawa neuronalne / neurorights) i '
                                                           'etyka AI.',
                                                     'en': 'Clinical & regulatory bioethics, genetic ethics, '
                                                           'neuroethics (neurorights) & AI alignment ethics.'},
                                                    {'year': 5,
                                                     'pl': 'Filozofia techniki, etyka środowiskowa i kosmiczna oraz '
                                                           'magisterium z rygoru epistemicznego megaprojektów.',
                                                     'en': 'Philosophy of technology, planetary/space ethics & M.A. '
                                                           'thesis on epistemic rigor.'}]},
                                         {'id': 'STU-TRK-F',
                                          'group': 'TRACK',
                                          'refId': 'F',
                                          'siteId': 'SITE-T9',
                                          'icon': '🚀',
                                          'color': '#ec4899',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt F: Inżynieria Kosmiczna, Systemy BLSS i Medycyna '
                                                     'Astronautyczna (5 lat)',
                                          'titleEn': 'Project F: Space Systems Engineering, BLSS & Bioastronautics (5 '
                                                     'Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Mechanika orbitalna, środowisko kosmiczne (próżnia, '
                                                           'termika, mikrometeoroidy, promieniowanie GCR/SPE) i '
                                                           'inżynieria systemowa.',
                                                     'en': 'Orbital mechanics, space environment (vacuum, thermal, '
                                                           'GCR/SPE radiation) & systems engineering.'},
                                                    {'year': 2,
                                                     'pl': 'Fizjologia człowieka w mikrograwitacji (zanik '
                                                           'kostno-mięśniowy, układ krążenia, neuro-okulistyka, '
                                                           'immunologia kosmiczna).',
                                                     'en': 'Human physiology in microgravity (bone/muscle loss, '
                                                           'cardiovascular, space immunology).'},
                                                    {'year': 3,
                                                     'pl': 'Fizyczno-chemiczne systemy podtrzymywania życia (ECLSS: '
                                                           'tlen, CO2, recykling wody), skafandry i projekt '
                                                           'inżynierski.',
                                                     'en': 'Physicochemical ECLSS (O2, CO2 scrubbing, water recovery), '
                                                           'EVA suits & B.Eng. project.'},
                                                    {'year': 4,
                                                     'pl': 'Bioregeneracyjne systemy BLSS (algi, hydroponika, '
                                                           'mikrobiomy zamknięte), osłony radiacyjne i architektura '
                                                           'baz Księżyc/Mars.',
                                                     'en': 'Bioregenerative BLSS (algae, hydroponics), radiation '
                                                           'shielding & Lunar/Martian habitats.'},
                                                    {'year': 5,
                                                     'pl': 'Zasilanie jądrowe misji (RTG/Kilopower), telemedycyna '
                                                           'autonomiczna i praca magisterska z inżynierii habitatów.',
                                                     'en': 'Space nuclear power (RTG/Kilopower), autonomous space '
                                                           'medicine & M.Sc. thesis.'}]},
                                         {'id': 'STU-TRK-G',
                                          'group': 'TRACK',
                                          'refId': 'G',
                                          'siteId': 'SITE-T9',
                                          'icon': '🌍',
                                          'color': '#22c55e',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Projekt G: Inżynieria Środowiska, Klimatologia i Ochrona '
                                                     'Biosfery Ziemi (5 lat)',
                                          'titleEn': 'Project G: Environmental Engineering, Climatology & Biosphere '
                                                     'Protection (5 Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Nauka o systemie Ziemi, cykle biogeochemiczne (C, N, P, '
                                                           'H2O), meteorologia, hydrologia i chemia środowiska.',
                                                     'en': 'Earth system science, biogeochemical cycles (C, N, P, '
                                                           'H2O), hydrology & environmental chemistry.'},
                                                    {'year': 2,
                                                     'pl': 'Ekologia populacji i ekosystemów, bioróżnorodność, '
                                                           'mikrobiologia gleby i wód oraz toksykologia środowiskowa.',
                                                     'en': 'Ecosystem ecology, biodiversity, soil/water microbiology & '
                                                           'environmental toxicology.'},
                                                    {'year': 3,
                                                     'pl': 'Technologie oczyszczania wody, powietrza i remediacji '
                                                           'gleb, gospodarka obiegu zamkniętego i projekt inżynierski.',
                                                     'en': 'Water/air purification, soil remediation, circular economy '
                                                           '& B.Eng. thesis.'},
                                                    {'year': 4,
                                                     'pl': 'Modelowanie klimatu, mikroklimat leśny i miejski, zdrowie '
                                                           'środowiskowe (One Health) i bezemisyjna transformacja '
                                                           'energetyczna.',
                                                     'en': 'Climate modeling, forest/urban microclimates, One Health & '
                                                           'zero-emission energy transition.'},
                                                    {'year': 5,
                                                     'pl': 'Teledetekcja satelitarna Ziemi, inżynieria regeneracji '
                                                           'ekosystemów i praca magisterska z ochrony biosfery.',
                                                     'en': 'Satellite Earth observation, ecosystem regeneration '
                                                           'engineering & M.Sc. thesis.'}]},
                                         {'id': 'STU-TRK-H',
                                          'group': 'TRACK',
                                          'refId': 'H',
                                          'siteId': 'SITE-X10',
                                          'icon': '☢️',
                                          'color': '#f43f5e',
                                          'sourceLang': 'PL+EN',
                                          'titlePl': 'Super-Projekt H: Energetyka Jądrowa, Reaktory SMR/HTGR i Fuzja '
                                                     'Termojądrowa (5 lat)',
                                          'titleEn': 'Super-Project H: Nuclear Engineering, SMR/HTGR Reactors & Fusion '
                                                     'Energy (5 Years)',
                                          'years': [{'year': 1,
                                                     'pl': 'Fizyka jądrowa, reakcje rozszczepienia i syntezy, '
                                                           'termodynamika techniczna, mechanika płynów i wymiana '
                                                           'ciepła.',
                                                     'en': 'Nuclear physics, fission & fusion reactions, engineering '
                                                           'thermodynamics & heat transfer.'},
                                                    {'year': 2,
                                                     'pl': 'Teoria reaktorów jądrowych (równanie dyfuzji i transportu '
                                                           'neutronów, współczynnik k_eff), materiały jądrowe i paliwa '
                                                           'TRISO.',
                                                     'en': 'Nuclear reactor theory (neutron transport, k_eff '
                                                           'criticality), nuclear materials & TRISO fuels.'},
                                                    {'year': 3,
                                                     'pl': 'Eksploatacja i bezpieczeństwo reaktorów PWR, SMR oraz '
                                                           'wysokotemperaturowych HTGR (HTGR-POLA, NCBJ Świerk) i '
                                                           'dyplom inżynierski.',
                                                     'en': 'PWR, SMR & high-temperature HTGR reactor safety/operations '
                                                           '(HTGR-POLA) & B.Eng.'},
                                                    {'year': 4,
                                                     'pl': 'Fuzja magnetyczna i inercyjna (tokamaki ITER/DEMO, '
                                                           'stellaratory), produkcja radioizotopów medycznych (MARIA) '
                                                           'i napędy kosmiczne.',
                                                     'en': 'Magnetic/inertial fusion (ITER/DEMO, stellarators), '
                                                           'medical radioisotopes (MARIA) & space reactors.'},
                                                    {'year': 5,
                                                     'pl': 'Integracja gigawatowych bloków jądrowych z klastrami '
                                                           'AI/WBE, kogeneracja wodoru i praca magisterska dla '
                                                           'podwariantów A–G.',
                                                     'en': 'Gigawatt nuclear power integration for AI/WBE clusters, '
                                                           'hydrogen cogeneration & M.Sc. thesis.'}]}],
                     'selectedQueue': ['STU-FND-1',
                                       'STU-FND-2',
                                       'STU-FND-3',
                                       'STU-FND-4',
                                       'STU-FND-5',
                                       'STU-FND-6',
                                       'STU-FND-7',
                                       'STU-FND-8',
                                       'STU-TRK-H'],
                     'completedTopicYears': {},
                     'aiAgents': [{'id': 'AGT-00',
                                   'codename': 'GROVES-OPPENHEIMER-00',
                                   'namePl': 'Agent Naczelny Sztabu Rozproszonego',
                                   'nameEn': 'Supreme Distributed Command Agent',
                                   'siteId': 'SITE-W0',
                                   'color': '#f59e0b',
                                   'rolePl': 'Orkiestracja 3-letniego rdzenia Administracji, kolejki 5-letnich studiów '
                                             'i globalnego bilansu rozszczepień k_eff.',
                                   'roleEn': 'Orchestrates the 3-year Administration core, 5-year sequential study '
                                             'queue, and global fission balance k_eff.',
                                   'promptTemplate': 'Działasz jako Agent Naczelny Sztabu Manhattan Golem 15 (District '
                                                     'W-0). Rozbij podany cel strategiczny na kompartmentalizowane '
                                                     'pakiety badawcze dla 5 ośrodków (W-0, Y-15, X-10, B-7, T-9), '
                                                     'wskaż wymogi prawno-administracyjne oraz określ punkty krytyczne '
                                                     'integracji.'},
                                  {'id': 'AGT-01',
                                   'codename': 'EPISTEMIC-LAW-01',
                                   'namePl': 'Agent Administracji, Prawa i Demarkacji Epistemicznej',
                                   'nameEn': 'Administration, Law & Epistemic Demarcation Agent',
                                   'siteId': 'SITE-W0',
                                   'color': '#eab308',
                                   'rolePl': 'Audyt zgodności regulacyjnej (PAA, MDR, AI Act, traktaty kosmiczne) i '
                                             'oznaczanie statusu twierdzeń (wiedza potwierdzona vs hipoteza).',
                                   'roleEn': 'Regulatory compliance audit (nuclear, medical, AI, space law) and '
                                             'epistemic demarcation of scientific claims.',
                                   'promptTemplate': 'Działasz jako Agent Audytu Prawno-Epistemicznego (District W-0 / '
                                                     'Projekt E). Oceń badany problem pod kątem: 1) faktów '
                                                     'empirycznych vs hipotez, 2) wymogów prawa '
                                                     'atomowego/medycznego/kosmicznego/AI, 3) ryzyk bioetycznych.'},
                                  {'id': 'AGT-02',
                                   'codename': 'TURING-NEUMANN-02',
                                   'namePl': 'Agent Teorii, Obliczeń i Cyfrowego Umysłu',
                                   'nameEn': 'Theory, Computing & Digital Mind Agent',
                                   'siteId': 'SITE-Y15',
                                   'color': '#38bdf8',
                                   'rolePl': 'Rozszczepianie zagadnień matematycznych, algorytmicznych, konektomiki, '
                                             'dekodowania mózgu i emulacji poznawczej (Projekt B).',
                                   'roleEn': 'Fissions mathematical, algorithmic, connectomic, neural decoding, and '
                                             'cognitive emulation problems (Project B).',
                                   'promptTemplate': 'Działasz jako Agent Laboratorium Los Alamos Y-15 (Matematyka, '
                                                     'Informatyka, AI, Projekt B). Sformułuj model formalny, złożoność '
                                                     'obliczeniową, architekturę symulacji oraz hipotezy '
                                                     'falsyfikowalne dla zadanego zagadnienia.'},
                                  {'id': 'AGT-03',
                                   'codename': 'SHANNON-ANALOG-03',
                                   'namePl': 'Agent Obliczania Fizycznego i Układów Neuromorficznych',
                                   'nameEn': 'Physical Computing & Neuromorphic Hardware Agent',
                                   'siteId': 'SITE-Y15',
                                   'color': '#fb923c',
                                   'rolePl': 'Projektowanie obliczeń ciągłych, memrystorowych, fotonicznych i '
                                             'energooszczędnych sieci impulsowych SNN (Projekt C).',
                                   'roleEn': 'Designs continuous analog, memristive, photonic, and ultra-low-power '
                                             'spiking neural architectures (Project C).',
                                   'promptTemplate': 'Działasz jako Agent Układów Analogowo-Neuromorficznych (Y-15 / '
                                                     'Projekt C). Zaproponuj fizyczny nośnik obliczeń, bilans '
                                                     'termodynamiczny (limit Landauera) i architekturę sprzętową dla '
                                                     'zadanego problemu.'},
                                  {'id': 'AGT-04',
                                   'codename': 'FERMI-PILE-04',
                                   'namePl': 'Agent Energetyki Jądrowej, SMR/HTGR i Fuzji',
                                   'nameEn': 'Nuclear Fission, SMR/HTGR & Fusion Power Agent',
                                   'siteId': 'SITE-X10',
                                   'color': '#f43f5e',
                                   'rolePl': 'Obliczenia mocy reaktorowej, ciepła procesowego HTGR-POLA, izotopów '
                                             'MARIA oraz zasilania dla klastrów AI i baz kosmicznych (Super-Projekt '
                                             'H).',
                                   'roleEn': 'Reactor power balances, HTGR-POLA process heat, MARIA medical isotopes, '
                                             'and nuclear power for AI & space (Super-Project H).',
                                   'promptTemplate': 'Działasz jako Agent Kompleksu Oak Ridge X-10 (Super-Projekt H). '
                                                     'Wyznacz architekturę zasilania jądrowego/termojądrowego, bilans '
                                                     'cieplno-elektryczny, bariery bezpieczeństwa radiacyjnego i '
                                                     'sprzężenia ze ścieżkami A–G.'},
                                  {'id': 'AGT-05',
                                   'codename': 'CYBORG-SYNTH-05',
                                   'namePl': 'Agent Neurobioniki, BCI i Bioinżynierii Tkankowej',
                                   'nameEn': 'Neurobionics, BCI & Tissue Bioengineering Agent',
                                   'siteId': 'SITE-B7',
                                   'color': '#10b981',
                                   'rolePl': 'Rozszczepianie problemów interfejsów mózg–maszyna (fNIRS/EEG/implanty), '
                                             'bioniki oraz hodowli organoidów i edycji genów (Projekty A i D).',
                                   'roleEn': 'Fissions BCI (fNIRS/EEG/implants), bionic prosthetics, organoid '
                                             'engineering, and genome editing tasks (Projects A & D).',
                                   'promptTemplate': 'Działasz jako Agent Kompleksu Hanford B-7 (Chemia, Biologia, '
                                                     'Projekty A i D). Rozpisz protokół biokompatybilności, sprzężenia '
                                                     'tkanka–elektronika, hodowli komórkowej/organoidowej oraz '
                                                     'kryteria bezpieczeństwa klinicznego.'},
                                  {'id': 'AGT-06',
                                   'codename': 'BIOSFERA-ORBIT-06',
                                   'namePl': 'Agent Systemów Podtrzymywania Życia: Kosmos ↔ Ziemia',
                                   'nameEn': 'Life-Support & Biosphere Agent: Space ↔ Earth',
                                   'siteId': 'SITE-T9',
                                   'color': '#a855f7',
                                   'rolePl': 'Integracja zamkniętych obiegów materii (BLSS), ochrony radiacyjnej '
                                             'astronautów i inżynierii regeneracji ekosystemów Ziemi (Projekty F i G).',
                                   'roleEn': 'Integrates closed-loop BLSS, astronaut radiation shielding, and Earth '
                                             'ecosystem regeneration engineering (Projects F & G).',
                                   'promptTemplate': 'Działasz jako Agent Poligonu Trinity T-9 (Oś Kosmos F ↔ Ziemia '
                                                     'G). Przeprowadź bilans masy, energii, tlenu, wody i odporności '
                                                     'biologicznej dla badanego habitatu pozaziemskiego lub ekosystemu '
                                                     'ziemskiego.'}],
                     'fissionNodes': [{'id': 'FIS-00',
                                       'parentId': None,
                                       'generation': 0,
                                       'code': 'CORE-235',
                                       'siteId': 'SITE-W0',
                                       'agentId': 'AGT-00',
                                       'trackRef': 'ADMIN-3Y',
                                       'status': 'active',
                                       'titlePl': 'Rdzeń Rozszczepialny Golem 15 + 3-Letni Sztab Administracji',
                                       'titleEn': 'Golem 15 Fissile Core + 3-Year Administrative HQ',
                                       'descPl': 'Punkt inicjacji reakcji łańcuchowej: cel nadrzędny zrozumienia, '
                                                 'wspomagania i ochrony człowieka rozszczepiany z poziomu 3-letniego '
                                                 'aparatu administracyjno-prawnego na 5 autonomicznych ośrodków '
                                                 'Manhattan.',
                                       'descEn': 'Chain-reaction initiation point: overarching human research mission '
                                                 'fissioned through a 3-year administrative-legal command core into 5 '
                                                 'autonomous Manhattan laboratories.',
                                       'neutronTargets': ['FIS-S1', 'FIS-S2', 'FIS-S3', 'FIS-S4', 'FIS-S5'],
                                       'deliverablePl': 'Globalna dyrektywa kompartmentalizacji i harmonogram 3 + 5×N '
                                                        'lat.',
                                       'deliverableEn': 'Global compartmentalization directive and 3 + 5×N year master '
                                                        'schedule.'},
                                      {'id': 'FIS-S1',
                                       'parentId': 'FIS-00',
                                       'generation': 1,
                                       'code': 'W0-GOV',
                                       'siteId': 'SITE-W0',
                                       'agentId': 'AGT-01',
                                       'trackRef': 'E',
                                       'status': 'active',
                                       'titlePl': 'Dyrekcja W-0: Prawo Sektorowe, Finanse B+R i Filtr Epistemiczny (E)',
                                       'titleEn': 'Directorate W-0: Sector Law, R&D Finance & Epistemic Filter (E)',
                                       'descPl': 'Rozszczepia wymogi formalno-prawne (PAA, komisje bioetyczne, AI Act, '
                                                 'POLSA) oraz metodologiczne kryteria demarkacji nauki od spekulacji '
                                                 'dla wszystkich ośrodków.',
                                       'descEn': 'Fissions legal-regulatory compliance and epistemological demarcation '
                                                 'criteria across all distributed laboratories.',
                                       'neutronTargets': ['FIS-H1', 'FIS-D1'],
                                       'deliverablePl': 'Matryca legalności i rygoru epistemicznego (4 poziomy '
                                                        'pewności wiedzy).',
                                       'deliverableEn': 'Legality and epistemic rigor matrix (4 certainty tiers).'},
                                      {'id': 'FIS-S2',
                                       'parentId': 'FIS-00',
                                       'generation': 1,
                                       'code': 'Y15-MIND',
                                       'siteId': 'SITE-Y15',
                                       'agentId': 'AGT-02',
                                       'trackRef': 'B',
                                       'status': 'active',
                                       'titlePl': 'Dyrekcja Y-15: Teoria, AI, Cyfrowy Umysł (B) i Fizyka Obliczeń (C)',
                                       'titleEn': 'Directorate Y-15: Theory, AI, Digital Mind (B) & Physical Computing '
                                                  '(C)',
                                       'descPl': 'Ośrodek obliczeniowy rozszczepiający fundamenty '
                                                 'matematyczno-informatyczne (FND 1–3, 8) na modele konektomu, '
                                                 'dekodery AI oraz maszyny analogowo-neuromorficzne.',
                                       'descEn': 'Theoretical hub splitting mathematical/CS foundations (FND 1–3, 8) '
                                                 'into connectome models, AI decoders, and neuromorphic machines.',
                                       'neutronTargets': ['FIS-A1', 'FIS-H1'],
                                       'deliverablePl': 'Stos symulacyjny mózg–AI–sprzęt neuromorficzny.',
                                       'deliverableEn': 'Brain–AI–neuromorphic simulation stack.'},
                                      {'id': 'FIS-S3',
                                       'parentId': 'FIS-00',
                                       'generation': 1,
                                       'code': 'X10-ATOM',
                                       'siteId': 'SITE-X10',
                                       'agentId': 'AGT-04',
                                       'trackRef': 'H',
                                       'status': 'critical',
                                       'titlePl': 'Dyrekcja X-10: Rozszczepienie Jądrowe, Fuzja i Architektura Mocy '
                                                  '(H)',
                                       'titleEn': 'Directorate X-10: Nuclear Fission, Fusion & Power Architecture (H)',
                                       'descPl': 'Serce energetyczne systemu: reaktory SMR/HTGR-POLA, fuzja '
                                                 'termojądrowa i elektronika mocy dostarczające gęstą, bezemisyjną '
                                                 'energię dla podwariantów A–G.',
                                       'descEn': 'Energetic core: SMR/HTGR-POLA reactors, fusion, and power '
                                                 'electronics supplying dense zero-emission power to sub-variants A–G.',
                                       'neutronTargets': ['FIS-B1', 'FIS-F1', 'FIS-G1'],
                                       'deliverablePl': 'Architektura mocy jądrowej i izotopowej dla klastrów AI, '
                                                        'medycyny i kosmosu.',
                                       'deliverableEn': 'Nuclear & isotope power architecture for AI clusters, '
                                                        'medicine, and space.'},
                                      {'id': 'FIS-S4',
                                       'parentId': 'FIS-00',
                                       'generation': 1,
                                       'code': 'B7-BIO',
                                       'siteId': 'SITE-B7',
                                       'agentId': 'AGT-05',
                                       'trackRef': 'A',
                                       'status': 'active',
                                       'titlePl': 'Dyrekcja B-7: Integracja Biocyfrowa (A) i Inżynieria Życia (D)',
                                       'titleEn': 'Directorate B-7: Bio-Digital Integration (A) & Life Engineering (D)',
                                       'descPl': 'Łączy chemię biomateriałów i biologię molekularną (FND 6–7) w '
                                                 'interfejsy mózg–maszyna, bionikę oraz hodowlę organoidów i medycynę '
                                                 'regeneracyjną.',
                                       'descEn': 'Combines biomaterials chemistry & molecular biology (FND 6–7) into '
                                                 'BCIs, bionics, organoids, and regenerative medicine.',
                                       'neutronTargets': ['FIS-B1', 'FIS-F1'],
                                       'deliverablePl': 'Platforma interfejsów tkankowo-elektronicznych i organoidów.',
                                       'deliverableEn': 'Tissue-electronic interface & organoid platform.'},
                                      {'id': 'FIS-S5',
                                       'parentId': 'FIS-00',
                                       'generation': 1,
                                       'code': 'T9-HAB',
                                       'siteId': 'SITE-T9',
                                       'agentId': 'AGT-06',
                                       'trackRef': 'F',
                                       'status': 'active',
                                       'titlePl': 'Dyrekcja T-9: Habitacja Kosmiczna (F) ↔ Ochrona Biosfery Ziemi (G)',
                                       'titleEn': 'Directorate T-9: Space Habitation (F) ↔ Earth Biosphere Protection '
                                                  '(G)',
                                       'descPl': 'Poligon weryfikacji środowiskowej: zamknięte systemy podtrzymywania '
                                                 'życia poza Ziemią w lustrzanym sprzężeniu z regeneracją ziemskich '
                                                 'ekosystemów.',
                                       'descEn': 'Environmental proving ground: closed extraterrestrial life support '
                                                 'coupled with terrestrial biosphere regeneration.',
                                       'neutronTargets': ['FIS-G1', 'FIS-F1'],
                                       'deliverablePl': 'Zunifikowany model obiegu materii i odporności środowiskowej '
                                                        'F↔G.',
                                       'deliverableEn': 'Unified matter-cycle and environmental resilience model F↔G.'},
                                      {'id': 'FIS-ADM1',
                                       'parentId': 'FIS-S1',
                                       'generation': 2,
                                       'code': 'W0-LIC',
                                       'siteId': 'SITE-W0',
                                       'agentId': 'AGT-01',
                                       'trackRef': 'E',
                                       'status': 'active',
                                       'titlePl': 'Licencjonowanie B+R: Dozór Jądrowy PAA, Komisje Bioetyczne i AI Act',
                                       'titleEn': 'R&D Licensing: Nuclear Oversight, Bioethics Boards & AI Act',
                                       'descPl': 'Pakiet procedur administracyjnych z 3-letnich studiów pozwalający '
                                                 'legalnie prowadzić badania nad izotopami, BCI, organoidami i '
                                                 'autonomicznymi agentami.',
                                       'descEn': 'Administrative compliance suite derived from the 3-year degree for '
                                                 'legal research on isotopes, BCIs, organoids, and AI agents.',
                                       'neutronTargets': ['FIS-H1', 'FIS-A1', 'FIS-D1'],
                                       'deliverablePl': 'Repozytorium wniosków regulacyjnych i matryc ryzyka.',
                                       'deliverableEn': 'Regulatory filings and risk assessment repository.'},
                                      {'id': 'FIS-B1',
                                       'parentId': 'FIS-S2',
                                       'generation': 2,
                                       'code': 'Y15-WBE',
                                       'siteId': 'SITE-Y15',
                                       'agentId': 'AGT-02',
                                       'trackRef': 'B',
                                       'status': 'active',
                                       'titlePl': 'Dekodowanie Sygnałów Mózgu (fMRI/EEG) i Konsolidacja Pamięci '
                                                  '(„Cyfrowy Sen”)',
                                       'titleEn': "Brain Decoding (fMRI/EEG) & Memory Consolidation ('Digital Sleep')",
                                       'descPl': 'Rozszczepienie Projektu B na dekodery semantyczne aktywności korowej '
                                                 'oraz algorytmy snu falowego zapobiegające katastroficznemu '
                                                 'zapominaniu w sieciach neuronowych.',
                                       'descEn': 'Splits Project B into semantic cortical decoders and slow-wave '
                                                 'digital sleep algorithms preventing catastrophic forgetting.',
                                       'neutronTargets': ['FIS-A1', 'FIS-C1'],
                                       'deliverablePl': 'Benchmark dekodowania neuronalnego i ciągłego uczenia SNN.',
                                       'deliverableEn': 'Neural decoding & continual SNN learning benchmark.'},
                                      {'id': 'FIS-C1',
                                       'parentId': 'FIS-S2',
                                       'generation': 2,
                                       'code': 'Y15-NEURO',
                                       'siteId': 'SITE-Y15',
                                       'agentId': 'AGT-03',
                                       'trackRef': 'C',
                                       'status': 'active',
                                       'titlePl': 'Procesory Neuromorficzne, Memrystory i Hybrydowe Biokomputery '
                                                  '(Brainoware)',
                                       'titleEn': 'Neuromorphic Processors, Memristors & Hybrid Biocomputers '
                                                  '(Brainoware)',
                                       'descPl': 'Fizyczne obliczanie niskiej mocy redukujące zapotrzebowanie '
                                                 'energetyczne sztucznej inteligencji o rzędy wielkości względem '
                                                 'klasycznych klastrów GPU.',
                                       'descEn': 'Low-power physical computing slashing AI energy demand by orders of '
                                                 'magnitude compared to von Neumann GPU clusters.',
                                       'neutronTargets': ['FIS-B1', 'FIS-D1'],
                                       'deliverablePl': 'Specyfikacja hybrydowego koprocesora analogowo-impulsowego.',
                                       'deliverableEn': 'Hybrid analog-spiking coprocessor specification.'},
                                      {'id': 'FIS-H1',
                                       'parentId': 'FIS-S3',
                                       'generation': 2,
                                       'code': 'X10-HTGR',
                                       'siteId': 'SITE-X10',
                                       'agentId': 'AGT-04',
                                       'trackRef': 'H',
                                       'status': 'critical',
                                       'titlePl': 'Bloki SMR / HTGR-POLA dla Centrów Danych AI/WBE i Kogeneracji '
                                                  'Wodoru',
                                       'titleEn': 'SMR / HTGR-POLA Units for AI/WBE Data Centers & Hydrogen '
                                                  'Cogeneration',
                                       'descPl': 'Bezpośrednie sprzężenie reaktorów wysokotemperaturowych z '
                                                 'infrastrukturą obliczeniową Projektu B oraz dekarbonizacją przemysłu '
                                                 'w Projekcie G.',
                                       'descEn': 'Direct coupling of high-temperature reactors with Project B '
                                                 'supercomputing clusters and Project G industrial decarbonization.',
                                       'neutronTargets': ['FIS-B1', 'FIS-G1'],
                                       'deliverablePl': 'Model bilansu mocy 300 MWe SMR + ciepło procesowe 750°C.',
                                       'deliverableEn': '300 MWe SMR + 750°C process heat power-balance model.'},
                                      {'id': 'FIS-H2',
                                       'parentId': 'FIS-S3',
                                       'generation': 2,
                                       'code': 'X10-MEDSPC',
                                       'siteId': 'SITE-X10',
                                       'agentId': 'AGT-04',
                                       'trackRef': 'H',
                                       'status': 'active',
                                       'titlePl': 'Radioizotopy Medyczne (MARIA: Lu-177/Mo-99) oraz Mikroreaktory '
                                                  'Kosmiczne Kilopower',
                                       'titleEn': 'Medical Radioisotopes (MARIA: Lu-177/Mo-99) & Space Kilopower '
                                                  'Microreactors',
                                       'descPl': 'Dwuwektorowe rozszczepienie technologii jądrowych: medycyna '
                                                 'nuklearna dla ochrony zdrowia (A/D) oraz zasilanie baz '
                                                 'księżycowo-marsjańskich w nocy polarnej (F).',
                                       'descEn': 'Dual-vector nuclear fission spin-off: targeted radionuclide therapy '
                                                 '(A/D) and surface fission power for Moon/Mars habitats (F).',
                                       'neutronTargets': ['FIS-A1', 'FIS-F1'],
                                       'deliverablePl': 'Karta izotopowo-energetyczna H→A/D/F.',
                                       'deliverableEn': 'Isotope & space nuclear power datasheet H→A/D/F.'},
                                      {'id': 'FIS-A1',
                                       'parentId': 'FIS-S4',
                                       'generation': 2,
                                       'code': 'B7-BCI',
                                       'siteId': 'SITE-B7',
                                       'agentId': 'AGT-05',
                                       'trackRef': 'A',
                                       'status': 'active',
                                       'titlePl': 'Optyczne i Elektryczne Interfejsy BCI (fNIRS PhotonGrav / ECoG) i '
                                                  'Neuroprotetyka',
                                       'titleEn': 'Optical & Electrical BCIs (fNIRS PhotonGrav / ECoG) & '
                                                  'Neuroprosthetics',
                                       'descPl': 'Dwukierunkowa komunikacja układ nerwowy ↔ maszyna testowana zarówno '
                                                 'w klinice rehabilitacyjnej na Ziemi, jak i na orbicie ISS (misja '
                                                 'IGNIS).',
                                       'descEn': 'Bidirectional nervous system ↔ machine interfaces validated in '
                                                 'clinical rehabilitation and orbital microgravity (ISS IGNIS).',
                                       'neutronTargets': ['FIS-F1', 'FIS-B1'],
                                       'deliverablePl': 'Architektura niskoszumowego toru akwizycji i dekodowania BCI.',
                                       'deliverableEn': 'Low-noise BCI acquisition and decoding pipeline.'},
                                      {'id': 'FIS-D1',
                                       'parentId': 'FIS-S4',
                                       'generation': 2,
                                       'code': 'B7-ORG',
                                       'siteId': 'SITE-B7',
                                       'agentId': 'AGT-05',
                                       'trackRef': 'D',
                                       'status': 'active',
                                       'titlePl': 'Organoidy Funkcjonalne z Komórek Macierzystych i Regeneracja '
                                                  'Tkankowa',
                                       'titleEn': 'Stem-Cell Functional Organoids & Regenerative Tissue Engineering',
                                       'descPl': 'Od różnicowania iPSC do unaczynionych organoidów (mózgowych, '
                                                 'przysadkowych, narządowych) z pełną kontrolą bezpieczeństwa '
                                                 'onkologicznego i bioetycznego.',
                                       'descEn': 'From iPSC differentiation to vascularized organoids under strict '
                                                 'oncological and bioethical safety gates.',
                                       'neutronTargets': ['FIS-A1', 'FIS-C1'],
                                       'deliverablePl': 'Drzewo decyzyjne regeneracja vs syntetyczna konstrukcja '
                                                        'organizmu.',
                                       'deliverableEn': 'Regeneration vs. synthetic organism construction decision '
                                                        'tree.'},
                                      {'id': 'FIS-F1',
                                       'parentId': 'FIS-S5',
                                       'generation': 2,
                                       'code': 'T9-BLSS',
                                       'siteId': 'SITE-T9',
                                       'agentId': 'AGT-06',
                                       'trackRef': 'F',
                                       'status': 'active',
                                       'titlePl': 'Zamknięty Habitat Pozaziemski BLSS, Osłony Radiacyjne i Immunologia '
                                                  'Kosmiczna',
                                       'titleEn': 'Closed Extraterrestrial BLSS Habitat, Radiation Shielding & Space '
                                                  'Immunology',
                                       'descPl': 'Integracja fotobioreaktorów algowych, recyklingu wody/tlenu, ochrony '
                                                 'przed GCR oraz monitoringu ekspresji genów odpornościowych '
                                                 'astronautów.',
                                       'descEn': 'Integrates algal photobioreactors, O2/H2O recycling, GCR shielding, '
                                                 'and astronaut immune gene-expression monitoring.',
                                       'neutronTargets': ['FIS-G1'],
                                       'deliverablePl': 'Bilans pętli podtrzymywania życia dla załogi 4-osobowej.',
                                       'deliverableEn': 'Closed-loop life-support balance for a 4-person crew.'},
                                      {'id': 'FIS-G1',
                                       'parentId': 'FIS-S5',
                                       'generation': 2,
                                       'code': 'T9-EARTH',
                                       'siteId': 'SITE-T9',
                                       'agentId': 'AGT-06',
                                       'trackRef': 'G',
                                       'status': 'active',
                                       'titlePl': 'Odporność Biosfery Ziemi: Mikroklimat Leśny, Retencja i '
                                                  'Dekarbonizacja Jądrowo-OZE',
                                       'titleEn': 'Earth Biosphere Resilience: Forest Microclimates, Retention & '
                                                  'Nuclear-Renewable Grid',
                                       'descPl': 'Transfer czystych technologii zamkniętego obiegu z kosmosu (F) oraz '
                                                 'energetyki jądrowej (H) do ochrony klimatu i ekosystemów '
                                                 'lądowo-wodnych Ziemi.',
                                       'descEn': 'Transfers closed-loop space tech (F) and nuclear baseload (H) to '
                                                 "protect Earth's climate and terrestrial-aquatic ecosystems.",
                                       'neutronTargets': ['FIS-F1'],
                                       'deliverablePl': 'Model synergii energetyczno-ekologicznej H + G.',
                                       'deliverableEn': 'Nuclear-ecological synergy model H + G.'},
                                      {'id': 'FIS-G3-1',
                                       'parentId': 'FIS-H1',
                                       'generation': 3,
                                       'code': 'NTR-HB-01',
                                       'siteId': 'SITE-X10',
                                       'agentId': 'AGT-04',
                                       'trackRef': 'H',
                                       'status': 'critical',
                                       'titlePl': 'Neutron Kaskadowy: Zasilanie 100 MW SMR dla Klastra Emulacji Kory '
                                                  'Mózgowej',
                                       'titleEn': 'Cascade Neutron: 100 MW SMR Power Feed for Cortical Emulation '
                                                  'Supercluster',
                                       'descPl': 'Atomowe zadanie łączące 5-letnie studia Energetyki Jądrowej (H) ze '
                                                 'studiami Neuronauki Obliczeniowej (B): porównanie kosztu '
                                                 'energetycznego mózgu (20 W) z klastrem krzemowym i neuromorficznym.',
                                       'descEn': 'Atomic task bridging 5-year Nuclear Engineering (H) and '
                                                 'Computational Neuroscience (B): 20 W biological brain vs. '
                                                 'silicon/neuromorphic cluster power budget.',
                                       'neutronTargets': ['FIS-B1', 'FIS-C1'],
                                       'deliverablePl': 'Raport porównawczy: 20 W mózg vs GPU vs Neuromorf + SMR.',
                                       'deliverableEn': 'Comparative report: 20 W brain vs. GPU vs. Neuromorphic + '
                                                        'SMR.'},
                                      {'id': 'FIS-G3-2',
                                       'parentId': 'FIS-A1',
                                       'generation': 3,
                                       'code': 'NTR-AF-02',
                                       'siteId': 'SITE-B7',
                                       'agentId': 'AGT-05',
                                       'trackRef': 'A',
                                       'status': 'active',
                                       'titlePl': 'Neutron Kaskadowy: Telemetria BCI + Immunologia w Misjach '
                                                  'Długotrwałych',
                                       'titleEn': 'Cascade Neutron: BCI Telemetry + Space Immunology in Long-Duration '
                                                  'Missions',
                                       'descPl': 'Pakiet roboczy Agenta B-7 i T-9: nieinwazyjne monitorowanie '
                                                 'obciążenia poznawczego fNIRS oraz markerów zapalnych u operatorów w '
                                                 'izolowanych habitatach.',
                                       'descEn': 'Joint B-7 & T-9 agent work package: non-invasive fNIRS cognitive '
                                                 'load and immune biomarker tracking in isolated habitats.',
                                       'neutronTargets': ['FIS-F1'],
                                       'deliverablePl': 'Protokół diagnostyczny operatora w habitacie analogowym.',
                                       'deliverableEn': 'Operator diagnostic protocol for analog space habitats.'}]}}

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_FILE = os.path.join(DATA_DIR, "database.json")
SEED_FILE = os.path.join(DATA_DIR, "seed.json")
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


def create_admin_auth_record(new_password: str, iterations: int = 260000) -> dict:
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
        return hmac.compare_digest(candidate_hash, expected_hash)
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
expected_dev_token = get_expected_device_token(db)

if "lang" not in st.session_state:
    st.session_state.lang = "pl"
if "theme" not in st.session_state:
    st.session_state.theme = "light"
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
            if sel_theme_gate and sel_theme_gate != st.session_state.theme:
                st.session_state.theme = sel_theme_gate
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
            if sel_lang and sel_lang != st.session_state.lang:
                st.session_state.lang = sel_lang
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
    if new_theme and new_theme != st.session_state.theme:
        st.session_state.theme = new_theme
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
    if new_lang and new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
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

tab_manhattan, tab_study, tab_map, tab_ws, tab_mat, tab_new, tab_graph, tab_security = st.tabs([
    f"{L['tab0']} ({len(ms_state.get('fissionNodes', []))})",
    L["tab1"],
    L["tab2"],
    f"{L['tab3']} ({len(db['subprojects'])})",
    f"{L['tab4']} ({len(db['materials'])})",
    L["tab5"],
    L["tab6"],
    L["tab7"],
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

            with st.expander(
                f"{c_item['icon']} OGNIWO #{idx_q} • LATA {p_start}–{p_end} ({cal_s}–{cal_e}) • {c_item['titleEn'] if is_en else c_item['titlePl']} [{len(done_yrs_topic)}/5]",
                expanded=(idx_q in (1, len(ms_state.get("selectedQueue", [])))),
            ):
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


# ------------------------------------------------------------------------------
# ZAKŁADKA 1: MATERIAŁY DO NAUKI (8 DZIEDZIN + ODNOGI A-G + BIBLIOTEKA)
# ------------------------------------------------------------------------------
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
