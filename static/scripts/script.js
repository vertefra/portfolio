const applyParallax = (base, DOMElement, Yvalue, Xvalue = 0) => {
  const distance = base.getBoundingClientRect().top;
  const wHeigth = window.innerHeight;
  if (Math.abs(distance) < wHeigth && isInScreen(DOMElement)) {
    DOMElement.style.transform = `translate(${(distance * Xvalue) / 5}px, ${
      distance * Yvalue
    }px)`;
  }
};

const makeSticky = DOMElement => {
  const position = DOMElement.offsetTop;
  if (position < window.pageYOffset) {
    DOMElement.classList.add('stickyHeader');
    // DOMElement.classList.remove("header");
  } else {
    DOMElement.classList.remove('stickyHeader');
    // DOMElement.classList.add("header");
  }
};

const fadeIn = DOMElement => {
  let opacity = 1;
  // distance for the element from the top screen. when negative is out of screen
  const halfPage = window.innerHeight / 2;
  const rect = DOMElement.getBoundingClientRect();
  const posFromTop = window.innerHeight - rect.top;
  if (isInScreen(DOMElement)) {
    if (scrollDirection() === 'down' && opacity <= 1) {
      opacity = posFromTop / halfPage;
      if (posFromTop > halfPage) {
        opacity = posFromTop / halfPage;
      }
      DOMElement.style.opacity = `${opacity}`;
    } else if (scrollDirection() === 'up' && opacity >= 0) {
      opacity = posFromTop / halfPage;

      DOMElement.style.opacity = `${opacity}`;
    }
  }
  return opacity;
};

let lastScroll = 0;
const scrollDirection = () => {
  const currentScroll = window.pageYOffset;
  if (currentScroll > lastScroll) {
    currentScroll === 0 ? (lastScroll = 0) : (lastScroll = currentScroll);
    return 'down';
  } else {
    currentScroll === 0 ? (lastScroll = 0) : (lastScroll = currentScroll);
    lastScroll = currentScroll;
    return 'up';
  }
};

const isInScreen = DOMElement => {
  const viewportOffset = DOMElement.getBoundingClientRect().top;
  const windowY = window.innerHeight;
  if (viewportOffset < windowY && viewportOffset > 0) {
    return true;
  } else {
    return false;
  }
};
