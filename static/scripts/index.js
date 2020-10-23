console.log('index Script');

const protectedRequest = async url => {
  const token = localStorage.getItem('token');
  parsedToken = JSON.parse(token);
  console.log('starting protected request', url);

  try {
    const res = await fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: parsedToken,
      },
    });

    const data = await res.text();

    return data;
  } catch (err) {
    console.log(err);
  }
};
