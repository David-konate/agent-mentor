// auth.js — COUCHE CONTROLLER (authentification)
// Orchestre connexion / inscription / déconnexion via API et UI.

// Au chargement : qui est connecté ?
async function checkAuth() {
  const data = await API.getMe();
  if (data.connected) {
    UI.showChat(data.first_name);
    Chat.loadHistory();          // recharge ses anciens messages
  } else {
    UI.showAuth();
  }
}

// INSCRIPTION
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

// CONNEXION
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

// DÉCONNEXION
document.getElementById("logout-btn").addEventListener("click", async () => {
  await API.logout();
  UI.showAuth();
});

checkAuth();   // on lance la vérif dès l'ouverture
