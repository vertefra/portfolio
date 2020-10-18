console.log('sanity');

const handleSubmit = formId => {
  const form = document.getElementById(formId);
  console.log(form);
};

const project = {
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
  for (let key in project) {
    const element = document.getElementById(key);
    const value = element.value;
    cpState[key] = value;
  }
  return cpState;
};
