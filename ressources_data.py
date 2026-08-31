from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_file
import io
import sqlite3
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ressources_data import RESSOURCES, MATIERES_RESSOURCES, SERIES_RESSOURCES, CLASSES_RESSOURCES

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-cette-cle-secrete-avant-la-mise-en-ligne")
DB_PATH = os.path.join(os.path.dirname(__file__), "revision.db")

MATIERES = ["Mathématiques", "Physique", "Chimie", "SVT", "Français",
            "Philosophie", "Histoire-Géo", "Anglais", "Informatique"]


# ---------- Base de données ----------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        mot_de_passe TEXT NOT NULL,
        classe TEXT NOT NULL,
        age INTEGER NOT NULL,
        ecole TEXT NOT NULL,
        date_inscription TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS groupes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        matiere TEXT NOT NULL,
        description TEXT,
        createur_id INTEGER NOT NULL,
        date_creation TEXT NOT NULL,
        FOREIGN KEY (createur_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS membres_groupe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        groupe_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        UNIQUE(groupe_id, user_id)
    );

    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        groupe_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        contenu TEXT NOT NULL,
        date_envoi TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS fiches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        groupe_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        nom_fichier TEXT NOT NULL,
        type_fichier TEXT NOT NULL,
        contenu BLOB NOT NULL,
        taille INTEGER NOT NULL,
        date_ajout TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS signalements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        signale_par INTEGER NOT NULL,
        message_id INTEGER,
        groupe_id INTEGER,
        raison TEXT NOT NULL,
        date_signalement TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()


# ---------- Décorateur simple pour vérifier la connexion ----------

def utilisateur_connecte():
    return session.get("user_id") is not None


def est_administrateur():
    email_admin = os.environ.get("ADMIN_EMAIL", "")
    return session.get("email", "").lower() == email_admin.lower() and email_admin != ""


# ---------- Pages publiques ----------

@app.route("/")
def index():
    return render_template("index.html", connecte=utilisateur_connecte())


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        email = request.form.get("email", "").strip().lower()
        mot_de_passe = request.form.get("mot_de_passe", "")
        classe = request.form.get("classe", "")
        age = request.form.get("age", "")
        ecole = request.form.get("ecole", "").strip()

        erreurs = []

        if not nom or not email or not mot_de_passe or not ecole:
            erreurs.append("Merci de remplir tous les champs.")

        if classe not in ["Premiere", "Terminale"]:
            erreurs.append("Ce site est réservé aux élèves en classe de Première ou Terminale.")

        try:
            age_int = int(age)
            if age_int < 17:
                erreurs.append("Tu dois avoir au moins 17 ans pour t'inscrire.")
        except ValueError:
            erreurs.append("Âge invalide.")
            age_int = 0

        if len(mot_de_passe) < 6:
            erreurs.append("Le mot de passe doit contenir au moins 6 caractères.")

        if erreurs:
            for e in erreurs:
                flash(e)
            return render_template("inscription.html")

        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (nom, email, mot_de_passe, classe, age, ecole, date_inscription) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (nom, email, generate_password_hash(mot_de_passe), classe, age_int, ecole, datetime.now().isoformat())
            )
            conn.commit()
        except sqlite3.IntegrityError:
            flash("Cet email est déjà utilisé.")
            conn.close()
            return render_template("inscription.html")
        conn.close()

        flash("Inscription réussie ! Tu peux maintenant te connecter.")
        return redirect(url_for("connexion"))

    return render_template("inscription.html")


@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        mot_de_passe = request.form.get("mot_de_passe", "")

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user["mot_de_passe"], mot_de_passe):
            session["user_id"] = user["id"]
            session["nom"] = user["nom"]
            session["email"] = user["email"]
            return redirect(url_for("tableau_de_bord"))
        else:
            flash("Email ou mot de passe incorrect.")

    return render_template("connexion.html")


@app.route("/deconnexion")
def deconnexion():
    session.clear()
    return redirect(url_for("index"))


# ---------- Espace connecté ----------

@app.route("/tableau-de-bord")
def tableau_de_bord():
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    mes_groupes = conn.execute("""
        SELECT g.* FROM groupes g
        JOIN membres_groupe m ON g.id = m.groupe_id
        WHERE m.user_id = ?
    """, (session["user_id"],)).fetchall()
    conn.close()

    return render_template("tableau_de_bord.html", nom=session["nom"], mes_groupes=mes_groupes)


@app.route("/groupes")
def liste_groupes():
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    matiere_filtre = request.args.get("matiere", "")
    conn = get_db()
    if matiere_filtre:
        groupes = conn.execute(
            "SELECT g.*, (SELECT COUNT(*) FROM membres_groupe WHERE groupe_id = g.id) as nb_membres FROM groupes g WHERE matiere = ?",
            (matiere_filtre,)
        ).fetchall()
    else:
        groupes = conn.execute(
            "SELECT g.*, (SELECT COUNT(*) FROM membres_groupe WHERE groupe_id = g.id) as nb_membres FROM groupes g"
        ).fetchall()
    conn.close()

    return render_template("groupes.html", groupes=groupes, matieres=MATIERES, matiere_filtre=matiere_filtre)


@app.route("/groupes/creer", methods=["GET", "POST"])
def creer_groupe():
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        matiere = request.form.get("matiere", "")
        description = request.form.get("description", "").strip()

        if not nom or matiere not in MATIERES:
            flash("Merci de remplir correctement le formulaire.")
            return render_template("creer_groupe.html", matieres=MATIERES)

        conn = get_db()
        cur = conn.execute(
            "INSERT INTO groupes (nom, matiere, description, createur_id, date_creation) VALUES (?, ?, ?, ?, ?)",
            (nom, matiere, description, session["user_id"], datetime.now().isoformat())
        )
        groupe_id = cur.lastrowid
        conn.execute(
            "INSERT INTO membres_groupe (groupe_id, user_id) VALUES (?, ?)",
            (groupe_id, session["user_id"])
        )
        conn.commit()
        conn.close()

        return redirect(url_for("voir_groupe", groupe_id=groupe_id))

    return render_template("creer_groupe.html", matieres=MATIERES)


@app.route("/groupes/<int:groupe_id>/rejoindre")
def rejoindre_groupe(groupe_id):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO membres_groupe (groupe_id, user_id) VALUES (?, ?)",
            (groupe_id, session["user_id"])
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # déjà membre
    conn.close()

    return redirect(url_for("voir_groupe", groupe_id=groupe_id))


@app.route("/groupes/<int:groupe_id>")
def voir_groupe(groupe_id):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    groupe = conn.execute("SELECT * FROM groupes WHERE id = ?", (groupe_id,)).fetchone()
    est_membre = conn.execute(
        "SELECT * FROM membres_groupe WHERE groupe_id = ? AND user_id = ?",
        (groupe_id, session["user_id"])
    ).fetchone()
    conn.close()

    if not groupe:
        return "Groupe introuvable", 404

    peut_supprimer = est_administrateur() or (groupe["createur_id"] == session["user_id"])

    return render_template("groupe.html", groupe=groupe, est_membre=est_membre is not None, peut_supprimer=peut_supprimer)


@app.route("/groupes/<int:groupe_id>/supprimer", methods=["POST"])
def supprimer_groupe(groupe_id):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    groupe = conn.execute("SELECT * FROM groupes WHERE id = ?", (groupe_id,)).fetchone()

    if not groupe:
        conn.close()
        return "Groupe introuvable", 404

    if not (est_administrateur() or groupe["createur_id"] == session["user_id"]):
        conn.close()
        return "Accès refusé", 403

    conn.execute("DELETE FROM messages WHERE groupe_id = ?", (groupe_id,))
    conn.execute("DELETE FROM fiches WHERE groupe_id = ?", (groupe_id,))
    conn.execute("DELETE FROM membres_groupe WHERE groupe_id = ?", (groupe_id,))
    conn.execute("DELETE FROM groupes WHERE id = ?", (groupe_id,))
    conn.commit()
    conn.close()

    flash("Groupe supprimé.")
    return redirect(url_for("liste_groupes"))


# ---------- Fiches de révision ----------

@app.route("/ressources")
def liste_ressources():
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    matiere_filtre = request.args.get("matiere", "")
    serie_filtre = request.args.get("serie", "")
    classe_filtre = request.args.get("classe", "")

    ressources = RESSOURCES
    if matiere_filtre:
        ressources = [r for r in ressources if r["matiere"] == matiere_filtre]
    if serie_filtre:
        ressources = [r for r in ressources if serie_filtre in r["series"]]
    if classe_filtre:
        ressources = [r for r in ressources if r["classe"] == classe_filtre]

    return render_template(
        "ressources.html",
        ressources=ressources,
        matieres=MATIERES_RESSOURCES,
        series=SERIES_RESSOURCES,
        classes=CLASSES_RESSOURCES,
        matiere_filtre=matiere_filtre,
        serie_filtre=serie_filtre,
        classe_filtre=classe_filtre
    )


@app.route("/ressources/<id_ressource>")
def voir_ressource(id_ressource):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    ressource = next((r for r in RESSOURCES if r["id"] == id_ressource), None)
    if not ressource:
        return "Fiche introuvable", 404

    return render_template("ressource_detail.html", ressource=ressource)


EXTENSIONS_AUTORISEES = {"pdf", "doc", "docx", "txt", "png", "jpg", "jpeg"}
TAILLE_MAX_FICHE = 5 * 1024 * 1024  # 5 Mo max par fiche


def extension_autorisee(nom_fichier):
    return "." in nom_fichier and nom_fichier.rsplit(".", 1)[1].lower() in EXTENSIONS_AUTORISEES


@app.route("/groupes/<int:groupe_id>/fiches")
def voir_fiches(groupe_id):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    groupe = conn.execute("SELECT * FROM groupes WHERE id = ?", (groupe_id,)).fetchone()
    est_membre = conn.execute(
        "SELECT * FROM membres_groupe WHERE groupe_id = ? AND user_id = ?",
        (groupe_id, session["user_id"])
    ).fetchone()

    if not est_membre:
        conn.close()
        return redirect(url_for("voir_groupe", groupe_id=groupe_id))

    fiches = conn.execute("""
        SELECT f.id, f.nom_fichier, f.taille, f.date_ajout, u.nom
        FROM fiches f JOIN users u ON f.user_id = u.id
        WHERE f.groupe_id = ?
        ORDER BY f.date_ajout DESC
    """, (groupe_id,)).fetchall()
    conn.close()

    return render_template("fiches.html", groupe=groupe, fiches=fiches)


@app.route("/groupes/<int:groupe_id>/fiches/ajouter", methods=["POST"])
def ajouter_fiche(groupe_id):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    est_membre = conn.execute(
        "SELECT * FROM membres_groupe WHERE groupe_id = ? AND user_id = ?",
        (groupe_id, session["user_id"])
    ).fetchone()
    if not est_membre:
        conn.close()
        return redirect(url_for("voir_groupe", groupe_id=groupe_id))

    fichier = request.files.get("fichier")

    if not fichier or fichier.filename == "":
        flash("Merci de choisir un fichier.")
        conn.close()
        return redirect(url_for("voir_fiches", groupe_id=groupe_id))

    if not extension_autorisee(fichier.filename):
        flash("Type de fichier non autorisé. Utilise PDF, Word, image ou texte.")
        conn.close()
        return redirect(url_for("voir_fiches", groupe_id=groupe_id))

    contenu = fichier.read()
    if len(contenu) > TAILLE_MAX_FICHE:
        flash("Fichier trop volumineux (5 Mo maximum).")
        conn.close()
        return redirect(url_for("voir_fiches", groupe_id=groupe_id))

    extension = fichier.filename.rsplit(".", 1)[1].lower()

    conn.execute(
        "INSERT INTO fiches (groupe_id, user_id, nom_fichier, type_fichier, contenu, taille, date_ajout) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (groupe_id, session["user_id"], fichier.filename, extension, contenu, len(contenu), datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

    flash("Fiche ajoutée avec succès.")
    return redirect(url_for("voir_fiches", groupe_id=groupe_id))


@app.route("/fiches/<int:fiche_id>/telecharger")
def telecharger_fiche(fiche_id):
    if not utilisateur_connecte():
        return redirect(url_for("connexion"))

    conn = get_db()
    fiche = conn.execute("SELECT * FROM fiches WHERE id = ?", (fiche_id,)).fetchone()

    if not fiche:
        conn.close()
        return "Fiche introuvable", 404

    est_membre = conn.execute(
        "SELECT * FROM membres_groupe WHERE groupe_id = ? AND user_id = ?",
        (fiche["groupe_id"], session["user_id"])
    ).fetchone()
    conn.close()

    if not est_membre:
        return "Accès refusé", 403

    return send_file(
        io.BytesIO(fiche["contenu"]),
        download_name=fiche["nom_fichier"],
        as_attachment=True
    )


# ---------- API du chat (polling toutes les quelques secondes en JS) ----------

@app.route("/api/groupes/<int:groupe_id>/messages", methods=["GET"])
def api_messages(groupe_id):
    if not utilisateur_connecte():
        return jsonify({"erreur": "non connecté"}), 401

    conn = get_db()
    est_membre = conn.execute(
        "SELECT * FROM membres_groupe WHERE groupe_id = ? AND user_id = ?",
        (groupe_id, session["user_id"])
    ).fetchone()
    if not est_membre:
        conn.close()
        return jsonify({"erreur": "tu dois rejoindre le groupe"}), 403

    messages = conn.execute("""
        SELECT m.id, m.contenu, m.date_envoi, u.nom
        FROM messages m JOIN users u ON m.user_id = u.id
        WHERE m.groupe_id = ?
        ORDER BY m.id ASC
        LIMIT 100
    """, (groupe_id,)).fetchall()
    conn.close()

    return jsonify([dict(m) for m in messages])


@app.route("/api/groupes/<int:groupe_id>/messages", methods=["POST"])
def api_envoyer_message(groupe_id):
    if not utilisateur_connecte():
        return jsonify({"erreur": "non connecté"}), 401

    contenu = request.json.get("contenu", "").strip()
    if not contenu:
        return jsonify({"erreur": "message vide"}), 400

    conn = get_db()
    est_membre = conn.execute(
        "SELECT * FROM membres_groupe WHERE groupe_id = ? AND user_id = ?",
        (groupe_id, session["user_id"])
    ).fetchone()
    if not est_membre:
        conn.close()
        return jsonify({"erreur": "tu dois rejoindre le groupe"}), 403

    conn.execute(
        "INSERT INTO messages (groupe_id, user_id, contenu, date_envoi) VALUES (?, ?, ?, ?)",
        (groupe_id, session["user_id"], contenu, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

    return jsonify({"succes": True})


@app.route("/api/signaler", methods=["POST"])
def api_signaler():
    if not utilisateur_connecte():
        return jsonify({"erreur": "non connecté"}), 401

    data = request.json
    conn = get_db()
    conn.execute(
        "INSERT INTO signalements (signale_par, message_id, groupe_id, raison, date_signalement) VALUES (?, ?, ?, ?, ?)",
        (session["user_id"], data.get("message_id"), data.get("groupe_id"), data.get("raison", ""), datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

    return jsonify({"succes": True})


init_db()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
