// i18n.js — COUCHE i18n (internationalisation FR / EN)
// Charge le bon fichier JSON, applique les traductions, mémorise le choix.

let traductions = {};

async function chargerLangue(langue) {
  const reponse = await fetch(`i18n/${langue}.json`);
  traductions = await reponse.json();

  appliquerTraductions();
  localStorage.setItem("langue", langue);
  document.documentElement.lang = langue;
}

function appliquerTraductions() {
  // Texte (data-i18n="cle")
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const cle = el.getAttribute("data-i18n");
    if (traductions[cle]) el.textContent = traductions[cle];
  });

  // Placeholder (data-i18n-placeholder="cle")
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const cle = el.getAttribute("data-i18n-placeholder");
    if (traductions[cle]) el.placeholder = traductions[cle];
  });
}

// Boutons de langue
document.querySelectorAll("[data-lang]").forEach((bouton) => {
  bouton.addEventListener("click", () => chargerLangue(bouton.getAttribute("data-lang")));
});

// Langue mémorisée, sinon FR
chargerLangue(localStorage.getItem("langue") || "fr");
