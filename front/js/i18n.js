// traductions fr / en
let traductions = {};

async function chargerLangue(langue) {
  const reponse = await fetch(`i18n/${langue}.json`);
  traductions = await reponse.json();
  appliquerTraductions();
  localStorage.setItem("langue", langue);
  document.documentElement.lang = langue;
}

function appliquerTraductions() {
  // texte
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const cle = el.getAttribute("data-i18n");
    if (traductions[cle]) el.textContent = traductions[cle];
  });
  // placeholder
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const cle = el.getAttribute("data-i18n-placeholder");
    if (traductions[cle]) el.placeholder = traductions[cle];
  });
}

// boutons fr/en
document.querySelectorAll("[data-lang]").forEach((bouton) => {
  bouton.addEventListener("click", () => chargerLangue(bouton.getAttribute("data-lang")));
});

// langue memorisee, sinon fr
chargerLangue(localStorage.getItem("langue") || "fr");
