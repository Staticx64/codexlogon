async function login() {
  const username = document.getElementById("loginUser").value;
  const password = document.getElementById("loginPass").value;

  const res = await fetch('/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();
  if (res.ok) {
    alert(`${data.message} as ${data.role}`);
    window.location.href = "dashboard.html";
  } else {
    alert(data.error);
  }
}

async function register() {
  const username = document.getElementById("regUser").value;
  const password = document.getElementById("regPass").value;
  const role = document.getElementById("regRole").value;

  const res = await fetch('/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password, role })
  });

  const data = await res.json();
  if (res.ok) {
    alert(data.message);
    window.location.href = "login.html";
  } else {
    alert(data.error);
  }
}
