// tout ce qui touche au DOM
const _authView = document.getElementById("auth-view");
const _chatView = document.getElementById("chat-view");
const _bonjour = document.getElementById("bonjour");
const _authError = document.getElementById("auth-error");
const _conversation = document.getElementById("conversation");

const UI = {
  showChat(firstName) {
    _authView.style.display = "none";
    _chatView.style.display = "block";
    _bonjour.textContent = firstName;   // le "Bonjour" est gere par l'i18n dans le html
  },

  showAuth() {
    _authView.style.display = "block";
    _chatView.style.display = "none";
  },

  showError(message) {
    _authError.textContent = message || "";
  },

  addMessage(text, author) {
    // author = "user" ou "agent" (pour la couleur de la bulle)
    const div = document.createElement("div");
    div.className = "message " + author;
    div.textContent = text;
    _conversation.appendChild(div);
    _conversation.scrollTop = _conversation.scrollHeight;
  },

  clearConversation() {
    _conversation.innerHTML = "";
  },
};
