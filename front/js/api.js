// tous les appels au back
const API = {
  async getMe() {
    const reponse = await fetch("api/me");
    return reponse.json();
  },

  async register(firstName, email, password) {
    const reponse = await fetch("api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ first_name: firstName, email: email, password: password }),
    });
    return { ok: reponse.ok, data: await reponse.json() };
  },

  async login(email, password) {
    const reponse = await fetch("api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password }),
    });
    return { ok: reponse.ok, data: await reponse.json() };
  },

  async logout() {
    await fetch("api/logout", { method: "POST" });
  },

  async sendChat(mode, messages, lang) {
    const reponse = await fetch("api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mode: mode, messages: messages, lang: lang }),
    });
    return { ok: reponse.ok, data: await reponse.json() };
  },

  async getHistory() {
    const reponse = await fetch("api/history");
    if (!reponse.ok) return { messages: [] };
    return reponse.json();
  },
};
