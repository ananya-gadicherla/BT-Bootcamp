
  function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem(
      "darkMode",
      document.body.classList.contains("dark-mode")
    );
  }

  // Persist dark mode
  if (localStorage.getItem("darkMode") === "true") {
    document.body.classList.add("dark-mode");
  }