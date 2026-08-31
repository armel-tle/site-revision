# -*- coding: utf-8 -*-
# Bibliothèque de fiches de révision — contenu rédigé pour RévisionTle
# Chaque fiche : id, matiere, series (liste), sequence, titre, type (cours/exercices), contenu_html

RESSOURCES = [
    {
        "id": "maths-complexes-cours",
        "matiere": "Mathématiques",
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
        "classe": "Terminale",
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
    {
        "id": "maths-suites-cours",
        "matiere": "Mathématiques",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Suites numériques — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Définition d'une suite</h3>
<p>Une suite numérique (uₙ) est une fonction définie sur ℕ (ou une partie de ℕ) à valeurs dans ℝ. On note uₙ le terme de rang n.</p>

<h3>2. Suite arithmétique</h3>
<p>(uₙ) est arithmétique de raison r si uₙ₊₁ = uₙ + r pour tout n. Terme général : uₙ = u₀ + nr. Somme des n premiers termes : Sₙ = n×(u₀ + uₙ₋₁)/2.</p>

<h3>3. Suite géométrique</h3>
<p>(uₙ) est géométrique de raison q si uₙ₊₁ = q×uₙ pour tout n. Terme général : uₙ = u₀×qⁿ. Somme : Sₙ = u₀×(1-qⁿ)/(1-q) si q ≠ 1.</p>

<h3>4. Sens de variation</h3>
<p>Une suite est croissante si uₙ₊₁ ≥ uₙ pour tout n, décroissante si uₙ₊₁ ≤ uₙ. On étudie souvent le signe de uₙ₊₁ - uₙ.</p>

<h3>5. Raisonnement par récurrence (niveau C approfondi)</h3>
<p>Pour démontrer une propriété P(n) pour tout n ≥ n₀ : 1) Initialisation : vérifier P(n₀). 2) Hérédité : montrer que si P(n) est vraie, alors P(n+1) l'est aussi. 3) Conclure par le principe de récurrence.</p>

<h3>Point d'attention série C</h3>
<p>La série C insiste davantage sur le raisonnement par récurrence et les suites définies par une relation plus complexe (uₙ₊₁ = f(uₙ)).</p>
"""
    },
    {
        "id": "maths-suites-exercices",
        "matiere": "Mathématiques",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Suites numériques — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Soit (uₙ) une suite arithmétique de premier terme u₀ = 5 et de raison r = 3. Calculer u₁₀, puis la somme S = u₀ + u₁ + ... + u₁₀.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Soit (vₙ) une suite géométrique de premier terme v₀ = 2 et de raison q = 3. Calculer v₅.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Soit (uₙ) définie par u₀ = 1 et uₙ₊₁ = 2uₙ + 1. Démontrer par récurrence que uₙ = 2ⁿ⁺¹ - 1 pour tout n ≥ 0.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : u₁₀ = 5 + 10×3 = 35. S = 11×(5+35)/2 = 220.<br>
Ex2 : v₅ = 2×3⁵ = 486.<br>
Ex3 : à démontrer en groupe (initialisation n=0, puis hérédité).</p>
"""
    },
    {
        "id": "maths-derivation-cours",
        "matiere": "Mathématiques",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Dérivation — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Nombre dérivé</h3>
<p>Le nombre dérivé de f en a est f'(a) = lim (h→0) [f(a+h) - f(a)] / h, s'il existe. Il représente le coefficient directeur de la tangente à la courbe au point d'abscisse a.</p>

<h3>2. Fonction dérivée</h3>
<p>Si f est dérivable en tout point d'un intervalle I, on définit la fonction dérivée f' sur I.</p>

<h3>3. Dérivées usuelles</h3>
<p>(xⁿ)' = nxⁿ⁻¹ ; (1/x)' = -1/x² ; (√x)' = 1/(2√x) ; (eˣ)' = eˣ.</p>

<h3>4. Opérations sur les dérivées</h3>
<p>(u+v)' = u'+v' ; (uv)' = u'v+uv' ; (u/v)' = (u'v-uv')/v² ; (u∘v)' = v'×u'(v) (dérivée composée).</p>

<h3>5. Application : sens de variation</h3>
<p>Si f'(x) &gt; 0 sur I, f est strictement croissante sur I. Si f'(x) &lt; 0, f est strictement décroissante. Si f'(x) = 0, f a un extremum local.</p>

<h3>Point d'attention série C</h3>
<p>La série C exige la maîtrise complète de la dérivée composée et son utilisation dans l'étude de fonctions plus complexes (racines, exponentielles combinées).</p>
"""
    },
    {
        "id": "maths-derivation-exercices",
        "matiere": "Mathématiques",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 2",
        "titre": "Dérivation — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Calculer la dérivée de f(x) = 3x² - 5x + 2.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Calculer la dérivée de f(x) = (2x+1)/(x-3) sur son domaine de définition.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Calculer la dérivée de f(x) = √(x²+1), puis étudier le sens de variation de f sur ℝ.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : f'(x) = 6x - 5.<br>
Ex2 : f'(x) = [(2)(x-3) - (2x+1)(1)] / (x-3)² = -7/(x-3)².<br>
Ex3 : f'(x) = x/√(x²+1) — à finir en groupe (étudier le signe de f').</p>
"""
    },
    {
        "id": "maths-vecteurs-cours",
        "matiere": "Mathématiques",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 3",
        "titre": "Vecteurs et produit scalaire — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Vecteurs du plan</h3>
<p>Un vecteur AB⃗ est caractérisé par sa direction, son sens et sa norme ‖AB⃗‖. Deux vecteurs sont égaux s'ils ont même direction, même sens et même norme.</p>

<h3>2. Coordonnées d'un vecteur</h3>
<p>Si A(xₐ, yₐ) et B(x_B, y_B), alors AB⃗(x_B - xₐ ; y_B - yₐ).</p>

<h3>3. Produit scalaire — définition</h3>
<p>u⃗·v⃗ = ‖u⃗‖×‖v⃗‖×cos(u⃗,v⃗). En coordonnées : u⃗(x;y)·v⃗(x';y') = xx' + yy'.</p>

<h3>4. Propriétés du produit scalaire</h3>
<p>u⃗·v⃗ = v⃗·u⃗ (symétrie). u⃗·u⃗ = ‖u⃗‖². u⃗·v⃗ = 0 si et seulement si u⃗ et v⃗ sont orthogonaux.</p>

<h3>5. Applications (niveau C approfondi)</h3>
<p>Le produit scalaire permet de calculer des angles (cos θ = u⃗·v⃗ / (‖u⃗‖‖v⃗‖)), de démontrer des orthogonalités, et d'établir des équations de droites/cercles.</p>

<h3>Point d'attention série C</h3>
<p>La série C combine souvent produit scalaire et démonstrations géométriques (théorème de la médiane, relations métriques dans le triangle).</p>
"""
    },
    {
        "id": "maths-vecteurs-exercices",
        "matiere": "Mathématiques",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 3",
        "titre": "Vecteurs et produit scalaire — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Soit A(1;2) et B(4;6). Calculer les coordonnées de AB⃗ et sa norme.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Soit u⃗(2;3) et v⃗(-1;4). Calculer u⃗·v⃗. Les vecteurs sont-ils orthogonaux ?</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Dans un triangle ABC, démontrer à l'aide du produit scalaire que : BC² = AB² + AC² - 2×AB×AC×cos(Â) (théorème d'Al-Kashi).</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : AB⃗(3;4), ‖AB⃗‖ = 5.<br>
Ex2 : u⃗·v⃗ = 2×(-1) + 3×4 = 10, non nul donc pas orthogonaux.<br>
Ex3 : à démontrer en groupe en écrivant BC⃗ = AC⃗ - AB⃗ puis en développant BC⃗·BC⃗.</p>
"""
    },
    {
        "id": "physique-mouvement-cours",
        "matiere": "Physique",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Cinématique du mouvement — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Référentiel et trajectoire</h3>
<p>Le mouvement d'un point est toujours décrit par rapport à un référentiel. La trajectoire est l'ensemble des positions successives du point.</p>

<h3>2. Vitesse moyenne et instantanée</h3>
<p>Vitesse moyenne : v_moy = distance parcourue / durée. Vitesse instantanée : v(t) = dx/dt (dérivée de la position par rapport au temps).</p>

<h3>3. Mouvement rectiligne uniforme (MRU)</h3>
<p>La vitesse est constante. x(t) = x₀ + v×t.</p>

<h3>4. Mouvement rectiligne uniformément varié (MRUV)</h3>
<p>L'accélération est constante. v(t) = v₀ + a×t. x(t) = x₀ + v₀t + ½at².</p>

<h3>5. Mouvement circulaire (niveau C approfondi)</h3>
<p>Vitesse angulaire ω = dθ/dt. Vitesse linéaire v = R×ω. Accélération centripète a = v²/R, dirigée vers le centre.</p>

<h3>Point d'attention série C</h3>
<p>La série C traite plus en profondeur le mouvement circulaire et les changements de référentiel, avec davantage de rigueur vectorielle.</p>
"""
    },
    {
        "id": "physique-mouvement-exercices",
        "matiere": "Physique",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Cinématique du mouvement — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Une voiture parcourt 150 km en 2 heures à vitesse constante. Calculer sa vitesse moyenne en km/h puis en m/s.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Un mobile part sans vitesse initiale avec une accélération constante de 2 m/s². Calculer sa vitesse et sa position après 5 secondes.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Un point mobile décrit un cercle de rayon 0,5 m à une vitesse angulaire constante de 4 rad/s. Calculer sa vitesse linéaire et son accélération centripète.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : v = 150/2 = 75 km/h ≈ 20,8 m/s.<br>
Ex2 : v(5) = 2×5 = 10 m/s. x(5) = ½×2×25 = 25 m.<br>
Ex3 : v = R×ω = 0,5×4 = 2 m/s. a = v²/R = 4/0,5 = 8 m/s².</p>
"""
    },
    {
        "id": "chimie-atome-cours",
        "matiere": "Chimie",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Structure de l'atome — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Constitution de l'atome</h3>
<p>Un atome est composé d'un noyau (protons chargés +, neutrons neutres) entouré d'électrons (charge -). Le nombre de protons Z est le numéro atomique.</p>

<h3>2. Nombre de masse</h3>
<p>A = Z + N, où N est le nombre de neutrons. On note un atome ᴬ_Z X.</p>

<h3>3. Isotopes</h3>
<p>Deux atomes sont isotopes s'ils ont le même Z mais un nombre de neutrons N différent (donc un A différent).</p>

<h3>4. Structure électronique</h3>
<p>Les électrons se répartissent en couches (K, L, M...) selon des règles précises : K (2 électrons max), L (8 électrons max), M (8 ou 18 selon le cas).</p>

<h3>5. La mole et nombre d'Avogadro</h3>
<p>Une mole contient N_A = 6,02×10²³ entités. La masse molaire M (g/mol) permet de convertir masse et quantité de matière : n = m/M.</p>

<h3>Point d'attention série C</h3>
<p>La série C demande une maîtrise plus poussée de la configuration électronique complète et son lien avec la position dans le tableau périodique.</p>
"""
    },
    {
        "id": "chimie-atome-exercices",
        "matiere": "Chimie",
        "classe": "Premiere",
        "series": ["C", "D", "TI"],
        "sequence": "Séquence 1",
        "titre": "Structure de l'atome — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un atome de sodium a Z = 11 et A = 23. Déterminer le nombre de protons, neutrons et électrons.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Calculer la quantité de matière (en mol) contenue dans 36 g d'eau (M(H₂O) = 18 g/mol).</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Donner la structure électronique complète de l'atome de chlore (Z = 17) en couches K, L, M, et déterminer le nombre d'électrons de valence.</p>

<h3>Corrigés indicatifs</h3>
<p>Ex1 : 11 protons, 23-11=12 neutrons, 11 électrons (atome neutre).<br>
Ex2 : n = m/M = 36/18 = 2 mol.<br>
Ex3 : K(2) L(8) M(7) — 7 électrons de valence.</p>
"""
    },
]

MATIERES_RESSOURCES = sorted(set(r["matiere"] for r in RESSOURCES))
SERIES_RESSOURCES = ["A", "C", "D", "TI"]
CLASSES_RESSOURCES = ["Premiere", "Terminale"]
