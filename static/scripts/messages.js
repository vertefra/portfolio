const flash = (DOMElementID, message) => {
  const flash = document.getElementById(DOMElementID);
  window.scrollTo(0, 0);

  setTimeout(() => {
    flash.innerText = '';
    flash.style.display = 'none';
  }, 3000);

  flash.style.display = 'flex';
  flash.innerText = message;
};
