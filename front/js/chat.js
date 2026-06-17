// chat.js — COUCHE CONTROLLER (chat)
// Orchestre la logique du chat en utilisant API (réseau) et UI (affichage).

const Chat = {
  historique: [],   // la mémoire de la conversation (renvoyée à chaque requête)

  // Recharge l'historique de l'utilisateur connecté
  async loadHistory() {
    UI.clearConversation();
    Chat.historique.length = 0;

    const data = await API.getHistory();
    data.messages.forEach((m) => {
      UI.addMessage(m.content, m.role === "user" ? "user" : "agent");
      Chat.historique.push({ role: m.role, content: m.content });
    });
  },
};

// Envoi d'un message
document.getElementById("formulaire").addEventListener("submit", async (event) => {
  event.preventDefault();

  const saisie = document.getElementById("saisie");
  const question = saisie.value.trim();
  if (!question) return;

  // 1. Afficher + mémoriser la question
  UI.addMessage(question, "user");
  Chat.historique.push({ role: "user", content: question });
  saisie.value = "";

  // 2. Mode choisi + envoi au back (via la couche API)
  const mode = document.querySelector('input[name="mode"]:checked').value;
  const { ok, data } = await API.sendChat(mode, Chat.historique);

  // 3. Afficher + mémoriser la réponse
  if (ok) {
    UI.addMessage(data.response, "agent");
    Chat.historique.push({ role: "assistant", content: data.response });
  } else {
    UI.addMessage("⚠️ " + (data.error || "Erreur"), "agent");
  }
});
