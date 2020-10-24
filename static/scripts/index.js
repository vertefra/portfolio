console.log('index Script');

const protectedRequest = async (url, method = 'GET', body = {}) => {
  const token = localStorage.getItem('token');
  parsedToken = JSON.parse(token);
  console.log('starting protected request', url);

  try {
    const request = {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        Authorization: parsedToken,
      },
    };

    if (Object.keys(body).length !== 0) request.body = JSON.stringify(body);

    const res = await fetch(url, request);

    return res;
  } catch (err) {
    return err;
  }
};

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
