console.log('projectIndex');

const toggleDescriptionVisibility = id => {
  const description = document.querySelector(`.description-box[name="${id}"]`);
  if (description) {
    description.classList.toggle('description-visible');
  }
};

const projectCards = document.querySelectorAll('.project-card');

for (let card of projectCards) {
  card.addEventListener('mouseover', ev => {
    toggleDescriptionVisibility(ev.target.id);
  });

  card.addEventListener('mouseout', ev => {
    toggleDescriptionVisibility(ev.target.id);
  });
}

// enable effect of delay animation for each card

for (let card of projectCards) {
  if (isInScreen(card) && !card.classList.contains('animate-card')) {
    card.classList.add('animate-card');
  }
}

window.addEventListener('scroll', e => {
  for (let card of projectCards) {
    if (isInScreen(card) && !card.classList.contains('animate-card')) {
      card.classList.add('animate-card');
    }
  }
});

// let anDelay = 0;

// for (let card of projectCards) {
//   if (isInScreen(card) && card.style.display =) {
//     console.log('in screen');
//     card.style.display = 'none';
//     card.style.display = 'block';
//     card.style.animationDelay = `${anDelay}s`;
//     anDelay += 0.6;
//   }
// }
