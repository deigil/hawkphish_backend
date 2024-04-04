// script.js

// Select the link element
const link = document.querySelector('a');

// Add an event listener to the link
link.addEventListener('click', () => {
  // When the link is clicked, navigate to the database page
  window.location.href = '/database';
});