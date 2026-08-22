const returnToTopButton = document.getElementById("return-to-top");

function toggleReturnToTopButton() {
  if (window.scrollY > window.innerHeight) {
    returnToTopButton.style.display = "block";
  } else {
    returnToTopButton.style.display = "none";
  }
}

// Listen for scroll events

window.addEventListener("scroll", toggleReturnToTopButton);
