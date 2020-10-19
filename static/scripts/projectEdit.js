console.log('projectEdit');

const projectObj = {
  title: '',
  description: '',
  tags: '',
  github: '',
  live: '',
  img_url: '',
};

const submitBtn = document.getElementById('submit-created');

const updateState = state => {
  const cpState = { ...state };
  for (let key in cpState) {
    const element = document.getElementById(key);
    const value = element.value;
    cpState[key] = value;
  }
  return cpState;
};

const clearForm = state => {
  for (let key in state) {
    const input = document.getElementById(key);
    input.value = '';
  }
};

submitBtn.onclick = async ev => {
  // ev.preventDefault();

  const project = updateState(projectObj);
  try {
    const res = await fetch(`/projects/${ev.target.name}/`, {
      credentials: 'same-origin',
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(project),
    });
    const data = await res.json();
    console.log(data);
    flash('flash', `project_id ${data.projectUpdated} updated!`);
    clearForm(projectObj);
  } catch (err) {
    console.log(err);
    flash('flash', err);
  }
  // clearForm(projectObj);
};
