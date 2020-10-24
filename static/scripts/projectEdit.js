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

submitBtn.onclick = async ev => {
  // ev.preventDefault();

  const project = updateState(projectObj);
  try {
    const res = await protectedRequest(
      `/projects/${ev.target.name}/`,
      'PUT',
      project
    );
    const data = await res.json();
    console.log(data);
    if (data.projectUpdated) {
      flash('flash', `project_id ${data.projectUpdated} updated!`);
      clearForm(projectObj);
    } else {
      flash('flash', 'Not authorized');
    }
  } catch (err) {
    console.log(err);
    flash('flash', err);
  }
  // clearForm(projectObj);
};
