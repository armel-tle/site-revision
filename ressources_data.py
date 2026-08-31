# -*- coding: utf-8 -*-
# Bibliothèque de fiches de révision — contenu rédigé pour RévisionTle
# Chaque fiche : id, matiere, series (liste), sequence, titre, type (cours/exercices), contenu_html

RESSOURCES = [
    {
        "id": "maths-complexes-cours",
        "matiere": "Mathématiques",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Nombres complexes — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Définitions de base</h3>
<p>Un nombre complexe s'écrit sous la forme <b>z = a + ib</b>, où a = Re(z) est la partie réelle, b = Im(z) est la partie imaginaire, et i² = -1. L'ensemble des nombres complexes est noté ℂ.</p>

<h3>2. Conjugué et module</h3>
<p><b>Conjugué</b> : z̄ = a - ib. Propriétés : z + z̄ = 2a, z × z̄ = a² + b² = |z|², (z̄)̄ = z.</p>
<p><b>Module</b> : |z| = √(a² + b²). Propriétés : |z₁z₂| = |z₁||z₂|, |z₁/z₂| = |z₁|/|z₂|, |z̄| = |z|.</p>

<h3>3. Forme trigonométrique et exponentielle</h3>
<p>z = r(cos θ + i sin θ) = r·e^(iθ), avec r = |z| et θ = arg(z) (défini à 2π près).</p>
<p>Formule de Moivre : (e^(iθ))ⁿ = e^(inθ), soit (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ).</p>

<h3>4. Équations du second degré dans ℂ</h3>
<p>Pour az² + bz + c = 0, Δ = b² - 4ac. Si Δ &lt; 0 : deux solutions complexes conjuguées z₁,₂ = (-b ± i√(-Δ)) / 2a.</p>

<h3>5. Interprétation géométrique</h3>
<p>M(a, b) représente z = a + ib. |z| = distance OM. arg(z) = angle (u⃗, OM⃗). |z₂ - z₁| = distance entre A(z₁) et B(z₂).</p>

<h3>Point d'attention série C</h3>
<p>Pour la série C, attends-toi à des exercices combinant nombres complexes et transformations géométriques (similitudes, rotations complexes) — niveau d'exigence plus élevé qu'en D/TI.</p>
"""
    },
    {
        "id": "maths-complexes-exercices",
        "matiere": "Mathématiques",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Nombres complexes — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Résoudre dans ℂ : z² - 4z + 13 = 0. Donner le module et un argument de chaque solution.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Soit z = 1 + i√3. Écrire z sous forme trigonométrique, puis calculer z⁶.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Le plan est muni d'un repère orthonormé (O, u⃗, v⃗). On considère les points A(1+2i) et B(4-i).
Déterminer l'écriture complexe de la rotation de centre A et d'angle π/2 qui envoie un point M(z) sur M'(z').
En déduire l'image de B par cette rotation.</p>

<h3>Exercice 4 (Niveau C — plus difficile)</h3>
<p>Résoudre dans ℂ l'équation z³ = 8i. (Indication : chercher les solutions sous forme exponentielle.)</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : Δ = -36, z₁ = 2+3i, z₂ = 2-3i, |z| = √13 pour les deux.<br>
Ex2 : |z| = 2, arg(z) = π/3, donc z⁶ = 2⁶·e^(i·6·π/3) = 64·e^(i2π) = 64.<br>
Ex3/4 : à traiter en groupe — poste ta démarche dans le chat pour vérification collective.</p>
"""
    },
    {
        "id": "maths-primitives-cours",
        "matiere": "Mathématiques",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Primitives et intégrales — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Primitive d'une fonction</h3>
<p>F est une primitive de f sur un intervalle I si F est dérivable sur I et F'(x) = f(x) pour tout x de I. Deux primitives d'une même fonction diffèrent d'une constante.</p>

<h3>2. Primitives usuelles</h3>
<p>xⁿ → xⁿ⁺¹/(n+1) (n ≠ -1) ; 1/x → ln|x| ; eˣ → eˣ ; cos x → sin x ; sin x → -cos x.</p>

<h3>3. Intégrale d'une fonction continue</h3>
<p>∫ₐᵇ f(x)dx = F(b) - F(a), où F est une primitive de f. Interprétation géométrique : aire algébrique sous la courbe entre a et b.</p>

<h3>4. Propriétés de l'intégrale</h3>
<p>Linéarité : ∫(f+g) = ∫f + ∫g. Relation de Chasles : ∫ₐᵇ + ∫ᵦᶜ = ∫ₐᶜ. Positivité si f ≥ 0 sur [a,b].</p>

<h3>5. Intégration par parties (niveau C surtout)</h3>
<p>∫ₐᵇ u'(x)v(x)dx = [u(x)v(x)]ₐᵇ - ∫ₐᵇ u(x)v'(x)dx. Technique essentielle pour les produits (x·eˣ, x·ln x, etc.)</p>

<h3>Point d'attention série C</h3>
<p>La série C aborde plus systématiquement l'intégration par parties et le calcul d'aires entre deux courbes avec changement de variable — à maîtriser en priorité.</p>
"""
    },
    {
        "id": "maths-primitives-exercices",
        "matiere": "Mathématiques",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Primitives et intégrales — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Calculer une primitive de f(x) = 3x² - 2x + 5 sur ℝ.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Calculer I = ∫₀¹ (2x + 1)dx.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>À l'aide d'une intégration par parties, calculer J = ∫₀¹ x·eˣ dx.</p>

<h3>Exercice 4 (Niveau C — plus difficile)</h3>
<p>Calculer l'aire du domaine délimité par les courbes de f(x) = x² et g(x) = x sur l'intervalle où f(x) ≤ g(x).</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : F(x) = x³ - x² + 5x + K.<br>
Ex2 : I = [x² + x]₀¹ = 2.<br>
Ex3/4 : à résoudre en groupe et comparer vos méthodes dans le chat.</p>
"""
    },
    {
        "id": "maths-probabilites-cours",
        "matiere": "Mathématiques",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 3",
        "titre": "Probabilités — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Vocabulaire de base</h3>
<p>Univers Ω : ensemble de toutes les issues possibles. Événement : sous-ensemble de Ω. P(A) = nombre de cas favorables / nombre de cas possibles (équiprobabilité).</p>

<h3>2. Propriétés des probabilités</h3>
<p>0 ≤ P(A) ≤ 1. P(Ω) = 1. P(A∪B) = P(A) + P(B) - P(A∩B). P(Ā) = 1 - P(A).</p>

<h3>3. Probabilités conditionnelles</h3>
<p>P(A|B) = P(A∩B) / P(B), pour P(B) ≠ 0. A et B sont indépendants si P(A∩B) = P(A)×P(B).</p>

<h3>4. Formule des probabilités totales</h3>
<p>Si B₁, B₂, ..., Bₙ forment une partition de Ω : P(A) = Σ P(A|Bᵢ)×P(Bᵢ).</p>

<h3>5. Variables aléatoires (niveau C approfondi)</h3>
<p>Espérance : E(X) = Σ xᵢ·P(X=xᵢ). Variance : V(X) = E(X²) - [E(X)]². Écart-type : σ(X) = √V(X).</p>

<h3>Point d'attention série C</h3>
<p>La série C insiste davantage sur les lois de probabilité (loi binomiale notamment) et le calcul d'espérance/variance dans des situations complexes.</p>
"""
    },
    {
        "id": "maths-probabilites-exercices",
        "matiere": "Mathématiques",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 3",
        "titre": "Probabilités — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un sac contient 5 boules rouges et 3 boules vertes. On tire une boule au hasard. Calculer la probabilité de tirer une boule rouge.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Dans une classe, 60% des élèves sont des filles. Parmi elles, 40% pratiquent un sport. Parmi les garçons, 55% pratiquent un sport. Calculer la probabilité qu'un élève choisi au hasard pratique un sport.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Une urne contient 10 boules numérotées de 1 à 10. On tire 3 boules sans remise. Soit X le nombre de boules paires tirées. Déterminer la loi de probabilité de X, puis calculer E(X).</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : P = 5/8.<br>
Ex2 : Formule des probabilités totales : P = 0,6×0,4 + 0,4×0,55 = 0,24 + 0,22 = 0,46.<br>
Ex3 : à traiter en groupe (loi hypergéométrique) — discute ta démarche avec tes camarades.</p>
"""
    },
    {
        "id": "physique-mecanique-cours",
        "matiere": "Physique",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Mécanique — Lois de Newton — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Première loi de Newton (Principe d'inertie)</h3>
<p>Dans un référentiel galiléen, un objet reste au repos ou en mouvement rectiligne uniforme si la somme des forces qui s'exercent sur lui est nulle.</p>

<h3>2. Deuxième loi de Newton (PFD)</h3>
<p>ΣF⃗ = m·a⃗, où ΣF⃗ est la somme vectorielle des forces, m la masse, et a⃗ le vecteur accélération du centre d'inertie.</p>

<h3>3. Troisième loi de Newton (Actions réciproques)</h3>
<p>Si un corps A exerce une force sur un corps B, alors B exerce sur A une force de même intensité, même direction, mais de sens opposé.</p>

<h3>4. Application : chute libre</h3>
<p>Seul le poids s'exerce : ΣF⃗ = P⃗ = mg⃗, donc a⃗ = g⃗ (indépendant de la masse). v(t) = g·t + v₀, x(t) = ½g·t² + v₀t + x₀.</p>

<h3>5. Application : plan incliné (niveau C approfondi)</h3>
<p>Décomposer le poids en une composante parallèle au plan (mg·sin α) et une composante perpendiculaire (mg·cos α). Appliquer le PFD selon les deux axes.</p>

<h3>Point d'attention série C</h3>
<p>La série C traite plus fréquemment des systèmes avec plusieurs forces combinées (frottements, plans inclinés, mouvements circulaires) demandant une décomposition vectorielle rigoureuse.</p>
"""
    },
    {
        "id": "physique-mecanique-exercices",
        "matiere": "Physique",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Mécanique — Lois de Newton — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un corps de masse 2 kg est soumis à une force constante de 10 N. Calculer son accélération (on néglige les frottements).</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Une balle est lâchée sans vitesse initiale d'une hauteur de 20 m. Calculer sa vitesse à l'arrivée au sol (g = 10 m/s²).</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Un solide de masse 5 kg glisse sans frottement sur un plan incliné à 30° par rapport à l'horizontale. Calculer son accélération le long du plan, puis la vitesse acquise après avoir parcouru 4 m sur le plan.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : a = F/m = 10/2 = 5 m/s².<br>
Ex2 : v² = 2gh, v = √(2×10×20) = 20 m/s.<br>
Ex3 : a = g·sin(30°) = 5 m/s², puis v² = 2a·d = 2×5×4 = 40, v ≈ 6,3 m/s.</p>
"""
    },
    {
        "id": "physique-electricite-cours",
        "matiere": "Physique",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Électricité — Circuit RC — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Le condensateur</h3>
<p>Un condensateur emmagasine une charge Q = C·U, où C est la capacité (en Farad) et U la tension à ses bornes.</p>

<h3>2. Charge d'un condensateur à travers une résistance</h3>
<p>Lors de la charge, la tension suit : u(t) = E(1 - e^(-t/τ)), avec τ = RC (constante de temps).</p>

<h3>3. Décharge d'un condensateur</h3>
<p>u(t) = U₀·e^(-t/τ). Au bout de t = 5τ, le condensateur est considéré comme totalement déchargé (moins de 1%).</p>

<h3>4. Énergie stockée</h3>
<p>E = ½·C·U².</p>

<h3>5. Résolution de l'équation différentielle (niveau C approfondi)</h3>
<p>La loi des mailles donne : RC·(du/dt) + u = E. Il faut savoir résoudre cette équation différentielle du premier ordre et identifier τ = RC.</p>

<h3>Point d'attention série C</h3>
<p>La série C exige la résolution complète de l'équation différentielle (pas seulement l'utilisation de la formule), avec justification mathématique de la solution.</p>
"""
    },
    {
        "id": "physique-electricite-exercices",
        "matiere": "Physique",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Électricité — Circuit RC — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un condensateur de capacité C = 100 µF est chargé sous une tension de 12 V. Calculer la charge Q stockée et l'énergie E emmagasinée.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Un circuit RC a R = 1000 Ω et C = 200 µF. Calculer la constante de temps τ.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Établir l'équation différentielle vérifiée par u(t) lors de la charge d'un condensateur à travers une résistance R sous une tension E, puis vérifier que u(t) = E(1-e^(-t/RC)) est bien solution.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : Q = C×U = 100.10⁻⁶×12 = 1,2.10⁻³ C. E = ½CU² = 7,2.10⁻³ J.<br>
Ex2 : τ = RC = 1000×200.10⁻⁶ = 0,2 s.<br>
Ex3 : à démontrer en groupe par dérivation et substitution.</p>
"""
    },
    {
        "id": "chimie-oxydoreduction-cours",
        "matiere": "Chimie",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Oxydoréduction — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Définitions</h3>
<p>Une oxydation est une perte d'électrons. Une réduction est un gain d'électrons. Un oxydant capte des électrons, un réducteur en cède.</p>

<h3>2. Couple oxydant/réducteur</h3>
<p>Noté Ox/Red. Demi-équation : Ox + n e⁻ = Red. Exemple : Cu²⁺ + 2e⁻ = Cu.</p>

<h3>3. Équilibrer une équation d'oxydoréduction</h3>
<p>Méthode : écrire les deux demi-équations, équilibrer les électrons échangés (multiplier si besoin), puis additionner en éliminant les électrons.</p>

<h3>4. Nombre d'oxydation</h3>
<p>Le nombre d'oxydation (n.o.) permet de repérer si un élément est oxydé (n.o. augmente) ou réduit (n.o. diminue) dans une réaction.</p>

<h3>5. Piles électrochimiques (niveau C approfondi)</h3>
<p>Une pile associe deux couples redox séparés par un pont salin. La force électromotrice E = E°(cathode) - E°(anode). Calcul des potentiels standards à maîtriser.</p>

<h3>Point d'attention série C</h3>
<p>La série C demande la maîtrise des calculs de potentiel de pile et l'utilisation des potentiels standards (tables de E°), en plus de l'équilibrage classique.</p>
"""
    },
    {
        "id": "chimie-oxydoreduction-exercices",
        "matiere": "Chimie",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Oxydoréduction — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Équilibrer la réaction entre le zinc métallique Zn et les ions cuivre Cu²⁺, sachant que les couples sont Zn²⁺/Zn et Cu²⁺/Cu.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Identifier l'oxydant et le réducteur dans la réaction : Fe + Cu²⁺ → Fe²⁺ + Cu.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>On réalise une pile Daniell (couples Zn²⁺/Zn, E° = -0,76 V et Cu²⁺/Cu, E° = +0,34 V). Calculer la force électromotrice de la pile et préciser quelle électrode est la cathode.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : Zn + Cu²⁺ → Zn²⁺ + Cu.<br>
Ex2 : Fe est réducteur (oxydé en Fe²⁺), Cu²⁺ est oxydant (réduit en Cu).<br>
Ex3 : E = 0,34 - (-0,76) = 1,10 V. La cathode est l'électrode de cuivre (potentiel le plus élevé).</p>
"""
    },
    {
        "id": "chimie-cinetique-cours",
        "matiere": "Chimie",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Cinétique chimique — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Vitesse de réaction</h3>
<p>La vitesse volumique de réaction v = (1/V)×(dξ/dt), où ξ est l'avancement de la réaction et V le volume.</p>

<h3>2. Facteurs cinétiques</h3>
<p>La vitesse d'une réaction augmente avec : la température, la concentration des réactifs, et la présence d'un catalyseur.</p>

<h3>3. Temps de demi-réaction t½</h3>
<p>C'est le temps au bout duquel l'avancement atteint la moitié de sa valeur finale (ou la moitié du réactif limitant a été consommé).</p>

<h3>4. Suivi cinétique</h3>
<p>On peut suivre une réaction par des mesures physiques (conductimétrie, spectrophotométrie) et tracer [réactif] ou [produit] en fonction du temps.</p>

<h3>5. Catalyse (niveau C approfondi)</h3>
<p>Un catalyseur accélère une réaction sans être consommé, en abaissant l'énergie d'activation. Distinction catalyse homogène/hétérogène à connaître avec exemples précis.</p>

<h3>Point d'attention série C</h3>
<p>La série C demande souvent l'exploitation graphique de courbes cinétiques (détermination de vitesse instantanée par tangente) en plus des définitions.</p>
"""
    },
    {
        "id": "chimie-cinetique-exercices",
        "matiere": "Chimie",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Cinétique chimique — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Citer trois facteurs qui peuvent augmenter la vitesse d'une réaction chimique.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Un réactif a une concentration initiale de 0,8 mol/L. Au bout du temps de demi-réaction, quelle est sa concentration restante (si la réaction est totale et le réactif limitant) ?</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>À partir d'un tableau de mesures [A] = f(t), expliquer la méthode pour déterminer graphiquement la vitesse instantanée de disparition de A à un instant t₁ donné.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : température, concentration, catalyseur.<br>
Ex2 : 0,4 mol/L (la moitié de la concentration initiale).<br>
Ex3 : tracer la tangente à la courbe au point d'abscisse t₁, la vitesse est l'opposé du coefficient directeur de cette tangente.</p>
"""
    },
]

MATIERES_RESSOURCES = sorted(set(r["matiere"] for r in RESSOURCES))
SERIES_RESSOURCES = ["A", "C", "D", "TI"]
