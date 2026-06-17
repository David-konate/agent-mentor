const Chat = {
  historique: [],   // memoire de la conversation

  // recharge les anciens messages du user
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

const formulaire = document.getElementById("formulaire");
const saisie = document.getElementById("saisie");

// Entrée = envoyer / Maj+Entrée = saut de ligne
saisie.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    formulaire.requestSubmit();
  }
});

formulaire.addEventListener("submit", async (event) => {
  event.preventDefault();

  const question = saisie.value.trim();
  if (!question) return;

  // affiche la question + l'ajoute a l'historique
  UI.addMessage(question, "user");
  Chat.historique.push({ role: "user", content: question });
  saisie.value = "";

  const mode = document.querySelector('input[name="mode"]:checked').value;
  const { ok, data } = await API.sendChat(mode, Chat.historique);

  if (ok) {
    UI.addMessage(data.response, "agent");
    Chat.historique.push({ role: "assistant", content: data.response });
  } else {
    UI.addMessage("⚠️ " + (data.error || "Erreur"), "agent");
  }
});
