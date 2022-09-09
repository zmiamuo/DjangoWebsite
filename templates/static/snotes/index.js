window.addEventListener('DOMContentLoaded', function() {

  // Pop up window for deleting a note
  const overlay = document.getElementById('overlay');
  const deletebtn = document.getElementById('delete-btn');
  const closebtn = document.getElementById('close-popup');

  const togglepopup = () => {
    overlay.classList.toggle("hidden");
    overlay.classList.toggle("flex");
  };

  deletebtn?.addEventListener('click', togglepopup);
  closebtn?.addEventListener('click', togglepopup);

  // Mobile menu button
  const btn = document.getElementById('mobile-button');
  const menu = document.getElementById('mobile-menu');

  btn?.addEventListener('click', () => {
    menu.classList.toggle("hidden");
  })
});
