const CACHE_NAME = "chat-biblico-v1";
const APP_SHELL = [
    "/",
    "/static/style.css?v=2",
    "/static/script.js?v=2",
    "/static/avatar.svg",
    "/static/manifest.webmanifest"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(APP_SHELL))
    );
    self.skipWaiting();
});

self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(keys => Promise.all(
            keys
                .filter(key => key !== CACHE_NAME)
                .map(key => caches.delete(key))
        ))
    );
    self.clients.claim();
});

self.addEventListener("fetch", event => {
    if (event.request.method !== "GET") return;

    const url = new URL(event.request.url);
    if (url.pathname === "/chat" || url.pathname === "/feedback" || url.pathname === "/devocionais") {
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then(response => {
                const copia = response.clone();
                caches.open(CACHE_NAME).then(cache => cache.put(event.request, copia));
                return response;
            })
            .catch(() => caches.match(event.request).then(response => response || caches.match("/")))
    );
});
