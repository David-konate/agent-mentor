// app.js - logique du chat cote navigateur (JavaScript vanilla, zero framework)
//
// Role : recuperer ce que tape le junior -> l'envoyer au back Python (/api/chat)
//        -> afficher la reponse de l'agent. La cle API n'est JAMAIS ici.

const conversation = document.getElementById("conversation");
const formulaire = document.getElementById("formulaire");
const saisie = document.getElementById("saisie");
const boutonEnvoyer = document.getElementById("envoyer");

// On garde l'historique pour donner du contexte a l'agent (memoire de la discussion).
const historique = [];

/**
 * Ajoute un message a l'ecran et retourne l'element cree.
 * @param {string} texte - le contenu du message
 * @param {string} auteur - "user" ou "agent"
 */
function afficherMessage(texte, auteur) {
  const div = document.createElement("div");
  div.className = "message " + auteur;
  div.textContent = texte;
  conversation.appendChild(div);
  conversation.scrollTop = conversation.scrollHeight;
  return div;
}

/** Recupere le mode pedagogique selectionne (tuteur / copilote). */
function modeSelectionne() {
  return document.querySelector('input[name="mode"]:checked').value;
}

formulaire.addEventListener("submit", async (evenement) => {
  evenement.preventDefault();

  const question = saisie.value.trim();
  if (!question) return;

  // 1. Afficher la question du junior et l'ajouter a l'historique.
  afficherMessage(question, "user");
  historique.push({ role: "user", content: question });
  saisie.value = "";
  boutonEnvoyer.disabled = true;

  // 2. Afficher un indicateur de chargement.
  const chargement = afficherMessage("Le mentor reflechit…", "agent");
  chargement.classList.add("chargement");

  try {
    // 3. Appeler le back Python.
    const reponseHttp = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        mode: modeSelectionne(),
        messages: historique,
      }),
    });

    const donnees = await reponseHttp.json();

    if (!reponseHttp.ok) {
      throw new Error(donnees.erreur || "Erreur inconnue");
    }

    // 4. Remplacer le chargement par la vraie reponse.
    chargement.classList.remove("chargement");
    chargement.textContent = donnees.reponse;
    historique.push({ role: "assistant", content: donnees.reponse });
  } catch (erreur) {
    chargement.classList.remove("chargement");
    chargement.textContent = "⚠️ " + erreur.message;
  } finally {
    boutonEnvoyer.disabled = false;
    saisie.focus();
  }
});
