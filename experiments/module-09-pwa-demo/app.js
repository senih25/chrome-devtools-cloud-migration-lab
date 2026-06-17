(function () {
  "use strict";

  const networkStatus = document.getElementById("network-status");
  const interactionBtn = document.getElementById("interaction-btn");
  const interactionStatus = document.getElementById("interaction-status");

  // Update status based on navigator.onLine
  function updateOnlineStatus() {
    if (navigator.onLine) {
      networkStatus.textContent = "Online";
      networkStatus.className = "status-indicator status-online";
    } else {
      networkStatus.textContent = "Offline";
      networkStatus.className = "status-indicator status-offline";
    }
  }

  // Register Service Worker
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("./sw.js")
        .then(reg => {
          console.info("Service Worker registered successfully with scope:", reg.scope);
        })
        .catch(err => {
          console.error("Service Worker registration failed:", err);
        });
    });
  } else {
    console.warn("Service Worker is not supported in this browser.");
  }

  // Interaction behavior
  interactionBtn.addEventListener("click", () => {
    interactionStatus.textContent = `Local interaction registered at ${new Date().toLocaleTimeString()}`;
    console.info("Local interaction triggered.");
  });

  window.addEventListener("online", updateOnlineStatus);
  window.addEventListener("offline", updateOnlineStatus);
  updateOnlineStatus();
})();
