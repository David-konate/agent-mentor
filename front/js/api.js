// api.js — COUCHE SERVICE
// Centralise TOUS les appels au back (fetch). Aucune manipulation du DOM ici.

const API = {
  // Qui est connecté ? -> { connected, first_name }
  async getMe() {
    const reponse = await fetch("/api/me");
    return reponse.json();
  },

  // Inscription -> { ok, data }
  async register(firstName, email, password) {
    const reponse = await fetch("/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ first_name: firstName, email: email, password: password }),
    });
    return { ok: reponse.ok, data: await reponse.json() };
  },

  // Connexion -> { ok, data }
  async login(email, password) {
    const reponse = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password }),
    });
    return { ok: reponse.ok, data: await reponse.json() };
  },

  // Déconnexion
  async logout() {
    await fetch("/api/logout", { method: "POST" });
  },

  // Envoyer un message au chat -> { ok, data }
  async sendChat(mode, messages) {
    const reponse = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mode: mode, messages: messages }),
    });
    return { ok: reponse.ok, data: await reponse.json() };
  },

  // Récupérer l'historique -> { messages: [...] }
  async getHistory() {
    const reponse = await fetch("/api/history");
    if (!reponse.ok) return { messages: [] };
    return reponse.json();
  },
};
