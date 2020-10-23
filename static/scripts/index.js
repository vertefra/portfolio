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
    console.log(err);
  }
};
