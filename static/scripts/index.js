console.log('index Script');

const protectedRequest = async url => {
  const token = localStorage.getItem('token');
  decodedToken = JSON.parse(token);
  console.log('starting protected request', url);
  const res = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: decodedToken,
    },
  });
};
