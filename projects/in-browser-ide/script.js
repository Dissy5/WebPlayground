const editor = document.querySelector("#editor");
const preview = document.querySelector("#preview");

editor.addEventListener("input", () => {
  preview.srcdoc = editor.value;
});
