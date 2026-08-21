const examples = document.querySelectorAll(".html-example");

examples.forEach(async (example) => {
  const filePath = example.dataset.source;

  try {
    const response = await fetch(filePath);

    if (!response.ok) {
      throw new Error(`Could not load ${filePath}`);
    }

    example.textContent = await response.text();
  } catch (error) {
    example.textContent = `Error loading example: ${error.message}`;
  }
});
