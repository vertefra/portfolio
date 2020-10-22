console.log('login script');

const loginBtn = document.getElementById('login-btn');
const loginInp = document.getElementById('login-inp');

loginBtn.onclick = async ev => {
  ev.preventDefault();

  if (loginInp.value === '') {
    alert('please insert a password');
  } else {
    try {
      const res = await fetch('/login/', {
        method: 'POST',
        headers: {
          'Application-Type': 'application/json',
        },
        body: JSON.stringify({ psw: loginInp.value }),
      });

      const data = await res.json();
      loginInp.value = '';

      if (data.success === false) {
        flash('flash', data.message);
      } else {
        flash('flash', 'you are now admin');
        localStorage.setItem('token', JSON.stringify(data.token));

        setTimeout(() => {
          protectedRequest('/projects/admin-index/');
        }, 10);
      }
    } catch (err) {
      console.log(err);
    }
  }
};
