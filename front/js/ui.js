// ui.js — COUCHE VUE (DOM)
// Centralise toute la manipulation de la page (afficher, basculer les vues).
// Aucun appel réseau ici (ça, c'est api.js).

// Les éléments de la page (déclarés UNE seule fois, ici)
const _authView = document.getElementById("auth-view");
const _chatView = document.getElementById("chat-view");
const _bonjour = document.getElementById("bonjour");
const _authError = document.getElementById("auth-error");
const _conversation = document.getElementById("conversation");

const UI = {
  // Affiche la vue CHAT (connecté) + salue par le prénom
  showChat(firstName) {
    _authView.style.display = "none";
    _chatView.style.display = "block";
    _bonjour.textContent = "Bonjour " + firstName + " 👋";
  },

  // Affiche la vue AUTH (déconnecté)
  showAuth() {
    _authView.style.display = "block";
    _chatView.style.display = "none";
  },

  // Affiche un message d'erreur d'auth (ou le vide)
  showError(message) {
    _authError.textContent = message || "";
  },

  // Ajoute une bulle de message dans la conversation
  addMessage(text, author) {
    const div = document.createElement("div");
    div.className = "message " + author;   // "message user" ou "message agent"
    div.textContent = text;
    _conversation.appendChild(div);
    _conversation.scrollTop = _conversation.scrollHeight;
  },

  // Vide la conversation affichée
  clearConversation() {
    _conversation.innerHTML = "";
  },
};
