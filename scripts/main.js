import * as themes from "./themes.js";

themes.init();

const testBackendButton = document.querySelector("#js-backend-test-button");
const outputText = document.querySelector("#test-server-response");

testBackendButton.addEventListener("click", async () => {
  const response = await fetch("http://192.168.1.174:3000");
  const text = await response.text();

  outputText.textContent = text;
});
