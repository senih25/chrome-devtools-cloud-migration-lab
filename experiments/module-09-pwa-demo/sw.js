const CACHE_NAME = "pwa-cache-v1";
const ASSETS = [
  "./index.html",
  "./styles.css",
  "./app.js",
  "./manifest.json"
];

// Install Event - cache core files
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.info("[SW] Pre-caching static assets");
        return cache.addAll(ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate Event - clean old caches
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME) {
            console.info("[SW] Removing old cache:", key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event - intercept and serve from cache if offline
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(cachedResponse => {
        if (cachedResponse) {
          console.info("[SW] Serving from cache:", event.request.url);
          return cachedResponse;
        }
        return fetch(event.request).then(response => {
          // Check if valid response
          if (!response || response.status !== 200 || response.type !== "basic") {
            return response;
          }
          // Dynamically cache other assets if loaded
          const responseToCache = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseToCache);
          });
          return response;
        }).catch(() => {
          // Fallback if both cache and network fail (offline fallback)
          console.warn("[SW] Fetch failed, resource not available offline.");
        });
      })
  );
});
