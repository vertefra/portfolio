console.log('projectIndex');

const projectImages = document.querySelectorAll('.project-img');

const toggleDescriptionVisibility = id => {
  const description = document.querySelector(`.description-box[name="${id}"]`);
  description.classList.toggle('description-visible');
};

for (let img of projectImages) {
  img.addEventListener('mouseover', ev => {
    toggleDescriptionVisibility(ev.target.id);
  });

  img.addEventListener('mouseout', ev => {
    toggleDescriptionVisibility(ev.target.id);
  });
}
