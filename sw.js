// ==============================================================================
// THE GOLEM 15: ADAPTIVE SERVICE WORKER & AUTO-UPDATE ENGINE (v2.2)
// Strategia hybrydowa: Network-First dla bazy danych, Stale-While-Revalidate dla assetów
// ==============================================================================

const CACHE_NAME = "golem-xv-pwa-v2.2";
const ASSETS_TO_CACHE = [
  "./",
  "./index.html",
  "./app.js",
  "./styles.css",
  "./manifest.json",
  "./data/seed.json"
];

// Instalacja: pre-cache kluczowych zasobów PWA
self.addEventListener("install", (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE).catch((err) => {
        console.warn("Pre-cache warning:", err);
      });
    })
  );
});

// Aktywacja: automatyczne czyszczenie przestarzałych wersji pamięci podręcznej
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log("[ServiceWorker] Usuwanie przestarzałego cache:", key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Obsługa zapytań sieciowych (Fetch)
self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);

  // 1. DANE DYNAMICZNE: Network-First (zawsze pobieraj najświeższy stan bazy danych, fallback do cache)
  if (url.pathname.includes("/data/database.json") || url.pathname.includes("/data/seed.json")) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          if (response && response.status === 200) {
            const respClone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, respClone));
          }
          return response;
        })
        .catch(() => {
          return caches.match(event.request);
        })
    );
    return;
  }

  // 2. KOD APLIKACJI I STYLE: Stale-While-Revalidate (błyskawiczny start + samoczynna aktualizacja w tle)
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200 && event.request.method === "GET") {
            const respClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, respClone));
          }
          return networkResponse;
        })
        .catch(() => cachedResponse);

      return cachedResponse || fetchPromise;
    })
  );
});

// Odbiór poleceń z aplikacji (np. natychmiastowe przejście do nowej wersji po kliknięciu 'Aktualizuj')
self.addEventListener("message", (event) => {
  if (event.data && event.data.action === "skipWaiting") {
    self.skipWaiting();
  }
});
