console.log('messages Script');

const flash = (DOMElementID, message, duration = 3000) => {
  const flash = document.getElementById(DOMElementID);
  window.scrollTo(0, 0);

  setTimeout(() => {
    flash.innerText = '';
    flash.style.display = 'none';
  }, duration);

  flash.style.display = 'flex';
  flash.innerText = message;
};
