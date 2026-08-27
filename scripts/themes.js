const themeSelect = document.getElementById("theme-select");

function setTheme() {
  const selectedTheme = themeSelect.value;
  document.documentElement.setAttribute("data-theme", selectedTheme);
}
function init() {
  if (themeSelect) {
    themeSelect.addEventListener("change", setTheme);
  }
}

export { init };
