// JavaScript code for dropdown menu functionality
document.addEventListener("DOMContentLoaded", function() {
  // Get the dropdown button and dropdown content
  var dropdownBtn = document.querySelector(".dropbtn");
  var dropdownContent = document.querySelector(".dropdown-content");

  // Toggle the dropdown menu when the button is clicked
  dropdownBtn.addEventListener("click", function() {
    dropdownContent.classList.toggle("show");
  });

  // Close the dropdown menu when clicking outside of it
  window.addEventListener("click", function(event) {
    if (!event.target.matches(".dropbtn")) {
      if (dropdownContent.classList.contains("show")) {
        dropdownContent.classList.remove("show");
      }
    }
  });
});

