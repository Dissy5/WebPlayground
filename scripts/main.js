import * as themes from "./themes.js";

themes.init();

const testBackendButton = document.querySelector("#js-backend-test-button");
const outputText = document.querySelector("#test-server-response");

if (testBackendButton && outputText) {
  testBackendButton.addEventListener("click", async () => {
    const response = await fetch("http://192.168.1.174:3000");
    const text = await response.text();

    outputText.textContent = text;
  });
}

const mainNav = document.querySelector("#main-nav");
const navMenu = document.querySelector("#nav-menu");
const upCaret = document.querySelector("#up-caret");
const downCaret = document.querySelector("#down-caret");

function toggleNavMenu() {
  let navOpen = mainNav.classList.toggle("open");

  if (navOpen) {
    //down caret hidden, activate up caret
    upCaret.classList.add("active");
    downCaret.classList.remove("active");
  } else {
    upCaret.classList.remove("active");
    downCaret.classList.add("active");
  }
}

if (navMenu) {
  navMenu.addEventListener("click", toggleNavMenu);
}
