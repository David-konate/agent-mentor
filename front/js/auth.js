// au chargement : qui est connecte ?
async function checkAuth() {
  const data = await API.getMe();
  if (data.connected) {
    UI.showChat(data.first_name);
    Chat.loadHistory();
  } else {
    UI.showAuth();
  }
}

// inscription
document.getElementById("register-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  UI.showError("");

  const { ok, data } = await API.register(
    document.getElementById("register-firstname").value,
    document.getElementById("register-email").value,
    document.getElementById("register-password").value,
  );

  if (ok) {
    UI.showChat(data.first_name);
    Chat.loadHistory();
  } else {
    UI.showError(data.error);
  }
});

// connexion
document.getElementById("login-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  UI.showError("");

  const { ok, data } = await API.login(
    document.getElementById("login-email").value,
    document.getElementById("login-password").value,
  );

  if (ok) {
    UI.showChat(data.first_name);
    Chat.loadHistory();
  } else {
    UI.showError(data.error);
  }
});

// deconnexion
document.getElementById("logout-btn").addEventListener("click", async () => {
  await API.logout();
  UI.showAuth();
});

checkAuth();
