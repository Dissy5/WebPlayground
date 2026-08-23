import { setDarkTheme, setLightTheme } from "./themes.js";

const themeSelect = document.getElementById("theme-select");

function setTheme() {
  const selectedTheme = themeSelect.value;
  document.documentElement.setAttribute("data-theme", selectedTheme);
}

themeSelect.addEventListener("change", setTheme);
