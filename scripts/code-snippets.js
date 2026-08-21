function dedent(text) {
  const lines = text.replace(/\r\n/g, "\n").split("\n");
  const indents = lines
    .filter((line) => line.trim().length > 0)
    .map((line) => line.match(/^(\s*)/)[1].length);

  if (indents.length === 0) return text.trim();

  const minIndent = Math.min(...indents);
  return lines
    .map((line) => line.slice(Math.min(minIndent, line.length)))
    .join("\n")
    .trim();
}

document.querySelectorAll("code[data-source]").forEach((code) => {
  const source = document.getElementById(code.dataset.source);
  if (source) {
    code.textContent = dedent(source.innerHTML);
  }
});
