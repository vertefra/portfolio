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

// delete request

const deleteBtns = document.querySelectorAll('.delete-btn');

deleteBtns.length > 0 &&
  deleteBtns.forEach(deleteBtn => {
    deleteBtn.onclick = async ev => {
      const id = ev.target.name;
      const res = await protectedRequest(`/projects/${id}/delete/`, 'DELETE');

      setTimeout(async () => {
        document.location = '/projects/';
      }, 2000);

      console.log('redirecting to admin-index');
      flash('flash', 'Project deleted!');
    };
  });

// edit request

const editBtns = document.querySelectorAll('.edit-btn');

editBtns.length > 0 &&
  editBtns.forEach(editBtn => {
    editBtn.onclick = async ev => {
      const id = ev.target.name;
      const res = await protectedRequest(`/projects/${id}/edit/`);
      const editPage = await res.text();
      document.body.innerHTML = '';
      document.write(editPage);
    };
  });

// editBtn.onclick = ev => {
//   const id = ev.target.name;
// };
