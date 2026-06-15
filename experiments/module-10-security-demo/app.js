(function () {
  "use strict";

  const storageButton = document.querySelector("#write-storage");
  const storageStatus = document.querySelector("#storage-status");
  const demoForm = document.querySelector("#demo-form");
  const formStatus = document.querySelector("#form-status");

  function writeSyntheticStorageValues() {
    localStorage.setItem("module10SecurityDemo", "local-only");
    sessionStorage.setItem("module10SessionDemo", "synthetic-session-value");

    storageStatus.textContent =
      "Synthetic localStorage and sessionStorage values were written.";

    console.info("Module 10 security demo: synthetic storage values written.");
  }

  function handleDemoFormSubmit(event) {
    event.preventDefault();

    const formData = new FormData(demoForm);
    const syntheticValue = formData.get("demoInput");

    formStatus.textContent =
      `Local-only action completed for synthetic value: ${syntheticValue}`;

    console.info("Module 10 security demo: local-only form action completed.");
  }

  storageButton.addEventListener("click", writeSyntheticStorageValues);
  demoForm.addEventListener("submit", handleDemoFormSubmit);

  console.info("Module 10 security demo loaded. No external requests were made.");
})();
