// Chat de groupe : récupération des messages toutes les 3 secondes,
// envoi de nouveaux messages, et signalement d'un message problématique.

const zoneMessages = document.getElementById("messages");
const formulaireMessage = document.getElementById("formulaire-message");
const champMessage = document.getElementById("contenu-message");

function formaterHeure(dateISO) {
    const date = new Date(dateISO);
    return date.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
}

async function chargerMessages() {
    try {
        const reponse = await fetch(`/api/groupes/${groupeId}/messages`);
        if (!reponse.ok) return;
        const messages = await reponse.json();

        zoneMessages.innerHTML = "";
        messages.forEach((msg) => {
            const div = document.createElement("div");
            div.className = "message-item";
            div.innerHTML = `
                <div class="message-auteur">${msg.nom}
                    <span class="message-signaler" onclick="signalerMessage(${msg.id})">Signaler</span>
                </div>
                <div>${msg.contenu.replace(/</g, "&lt;")}</div>
                <div style="font-size:0.7rem;color:#999;">${formaterHeure(msg.date_envoi)}</div>
            `;
            zoneMessages.appendChild(div);
        });
        zoneMessages.scrollTop = zoneMessages.scrollHeight;
    } catch (erreur) {
        console.error("Erreur de chargement des messages :", erreur);
    }
}

formulaireMessage.addEventListener("submit", async (e) => {
    e.preventDefault();
    const contenu = champMessage.value.trim();
    if (!contenu) return;

    try {
        await fetch(`/api/groupes/${groupeId}/messages`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ contenu })
        });
        champMessage.value = "";
        chargerMessages();
    } catch (erreur) {
        console.error("Erreur d'envoi du message :", erreur);
    }
});

async function signalerMessage(messageId) {
    const raison = prompt("Pourquoi veux-tu signaler ce message ?");
    if (!raison) return;

    try {
        await fetch("/api/signaler", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message_id: messageId, groupe_id: groupeId, raison })
        });
        alert("Message signalé. Merci de contribuer à un espace sûr.");
    } catch (erreur) {
        console.error("Erreur de signalement :", erreur);
    }
}

// Chargement initial + rafraîchissement automatique
chargerMessages();
setInterval(chargerMessages, 3000);
