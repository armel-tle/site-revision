# -*- coding: utf-8 -*-
# Bibliothèque de fiches de révision — contenu rédigé pour RévisionTle

RESSOURCES = [
    {
        "id": 'maths-complexes-cours',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Nombres complexes — Cours',
        "type": 'Cours',
        "contenu": """
<h3>1. Définitions de base</h3>
<p>Un nombre complexe s'écrit sous la forme <b>z = a + ib</b>, où a et b sont des nombres réels, et i vérifie <b>i² = -1</b>. On dit que a est la <b>partie réelle</b> de z, notée Re(z), et que b est la <b>partie imaginaire</b> de z, notée Im(z). L'ensemble des nombres complexes est noté <b>ℂ</b>. ℝ est inclus dans ℂ (un réel est un complexe dont la partie imaginaire est nulle).</p>
<p>Deux nombres complexes sont égaux si et seulement si ils ont la même partie réelle ET la même partie imaginaire. Cette propriété, appelée <i>unicité de l'écriture algébrique</i>, est très utilisée pour résoudre des équations en identifiant partie réelle et partie imaginaire de chaque côté.</p>

<h3>2. Opérations sur les complexes</h3>
<p><b>Addition :</b> (a+ib) + (c+id) = (a+c) + i(b+d).</p>
<p><b>Multiplication :</b> (a+ib)(c+id) = (ac - bd) + i(ad + bc) — on développe comme un produit classique en remplaçant i² par -1.</p>
<p><b>Inverse :</b> pour z = a+ib non nul, 1/z = (a - ib) / (a² + b²) — on multiplie numérateur et dénominateur par le conjugué.</p>

<h3>3. Conjugué et module</h3>
<p><b>Conjugué</b> de z = a + ib : z̄ = a - ib. Propriétés essentielles : z + z̄ = 2a (toujours réel), z × z̄ = a² + b² (toujours réel positif), (z̄)̄ = z, et z̄₁ + z̄₂ = (z₁+z₂)̄ (le conjugué d'une somme est la somme des conjugués — idem pour un produit).</p>
<p><b>Module</b> de z : |z| = √(a² + b²) = √(z×z̄). C'est toujours un réel positif ou nul. Propriétés : |z₁×z₂| = |z₁|×|z₂| ; |z₁/z₂| = |z₁|/|z₂| (z₂≠0) ; |z̄| = |z| ; |z| = 0 si et seulement si z = 0.</p>

<h3>4. Forme trigonométrique et forme exponentielle</h3>
<p>Tout nombre complexe non nul peut s'écrire z = r(cos θ + i sin θ) = r·e^(iθ), avec r = |z| (le module) et θ = arg(z) un argument de z, défini à 2π près (ou 2kπ, k entier relatif).</p>
<p>Pour déterminer θ à partir de a et b : cos θ = a/r et sin θ = b/r. Il faut toujours vérifier dans quel "cadran" se trouve le point pour choisir le bon angle.</p>
<p><b>Propriétés des exponentielles complexes</b> (très utiles pour simplifier des calculs) : e^(iθ₁) × e^(iθ₂) = e^(i(θ₁+θ₂)) ; e^(iθ₁) / e^(iθ₂) = e^(i(θ₁-θ₂)) ; (e^(iθ))ⁿ = e^(inθ) — c'est la <b>formule de Moivre</b>, qui permet de calculer facilement des puissances de nombres complexes.</p>

<h3>5. Équations du second degré dans ℂ</h3>
<p>Pour résoudre az² + bz + c = 0 (a ≠ 0, coefficients réels), on calcule le discriminant Δ = b² - 4ac, exactement comme dans ℝ :</p>
<p>— Si Δ > 0 : deux solutions réelles distinctes, comme d'habitude.<br>
— Si Δ = 0 : une solution réelle double.<br>
— <b>Si Δ < 0</b> (le cas nouveau propre à ℂ) : deux solutions complexes conjuguées : z₁ = (-b + i√(-Δ)) / 2a et z₂ = (-b - i√(-Δ)) / 2a = z̄₁.</p>

<h3>6. Interprétation géométrique</h3>
<p>Dans le plan complexe muni d'un repère (O, u⃗, v⃗), un nombre complexe z = a + ib est représenté par le point M de coordonnées (a, b), appelé <i>image de z</i>. Réciproquement, z est appelé <i>affixe</i> du point M.</p>
<p>— |z| représente la distance OM.<br>
— arg(z) représente une mesure de l'angle (u⃗, OM⃗).<br>
— Pour deux points A(zₐ) et B(z_B), le vecteur AB⃗ a pour affixe z_B - zₐ, et |z_B - zₐ| représente la distance AB.<br>
— Le milieu I de [AB] a pour affixe zᵢ = (zₐ + z_B)/2.</p>

<h3>Point d'attention série C</h3>
<p>La série C combine plus souvent nombres complexes et transformations géométriques (rotations, similitudes directes de la forme z' = az + b) — il faut savoir identifier le centre, l'angle et le rapport d'une transformation à partir de son écriture complexe.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un architecte dessine le plan d'un jardin circulaire sur un logiciel qui utilise les nombres complexes pour repérer les points. Le centre du jardin est à l'origine O du repère. Un premier arbre est planté au point A d'affixe zₐ = 3 + 4i (unités en mètres).</p>
<p><b>Tâche 1 :</b> Calculer la distance entre le centre du jardin et l'arbre A.</p>
<p><b>Tâche 2 :</b> L'architecte veut planter un second arbre B, symétrique de A par rapport à l'axe des ordonnées (axe des imaginaires). Donner l'affixe de B, puis calculer la distance AB.</p>
<p><b>Tâche 3 :</b> On veut faire pivoter l'arbre A de 90° autour du centre O pour créer un troisième point C. Sachant qu'une rotation d'angle 90° autour de O correspond à la transformation z' = iz, calculer l'affixe de C et vérifier que OC = OA.</p>
<p><i>Cette situation mobilise : le calcul de module (distance), la manipulation algébrique des affixes, et l'interprétation géométrique d'une transformation complexe — compétences attendues en fin de séquence.</i></p>
""",
    },
    {
        "id": 'maths-complexes-exercices',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Nombres complexes — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Résoudre dans ℂ : z² - 4z + 13 = 0. Donner le module et un argument de chaque solution.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Soit z = 1 + i√3. Écrire z sous forme trigonométrique, puis calculer z⁶.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Le plan est muni d'un repère orthonormé (O, u⃗, v⃗). On considère les points A(1+2i) et B(4-i).
Déterminer l'écriture complexe de la rotation de centre A et d'angle π/2 qui envoie un point M(z) sur M'(z').
En déduire l'image de B par cette rotation.</p>

<h3>Exercice 4 (Niveau C — plus difficile)</h3>
<p>Résoudre dans ℂ l'équation z³ = 8i. (Indication : chercher les solutions sous forme exponentielle.)</p>""",
    },
    {
        "id": 'maths-primitives-cours',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Primitives et intégrales — Cours',
        "type": 'Cours',
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


<h3>6. Calcul d'aires entre deux courbes</h3>
<p>L'aire entre deux courbes représentatives de f et g sur [a,b], lorsque f(x) ≥ g(x) sur cet intervalle, est A = ∫ₐᵇ [f(x) - g(x)] dx (exprimée en unités d'aire). Il faut d'abord déterminer les points d'intersection des deux courbes pour connaître les bornes correctes et le signe de f(x) - g(x).</p>

<h3>7. Méthode pratique de résolution</h3>
<p>Pour calculer une intégrale : 1) Trouver une primitive F de f. 2) Calculer F(b) et F(a). 3) Faire la différence F(b) - F(a). Toujours vérifier le signe du résultat selon la position de la courbe par rapport à l'axe des abscisses.</p>

<h3>Point d'attention série C</h3>
<p>La série C aborde plus systématiquement l'intégration par parties et le calcul d'aires entre deux courbes avec changement de variable — à maîtriser en priorité.</p>
""",
    },
    {
        "id": 'maths-primitives-exercices',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Primitives et intégrales — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Calculer une primitive de f(x) = 3x² - 2x + 5 sur ℝ.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Calculer I = ∫₀¹ (2x + 1)dx.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>À l'aide d'une intégration par parties, calculer J = ∫₀¹ x·eˣ dx.</p>

<h3>Exercice 4 (Niveau C — plus difficile)</h3>
<p>Calculer l'aire du domaine délimité par les courbes de f(x) = x² et g(x) = x sur l'intervalle où f(x) ≤ g(x).</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un artisan souhaite fabriquer une pièce métallique dont le profil est délimité par les courbes de f(x) = 4 - x² et g(x) = x sur l'intervalle où f(x) ≥ g(x), les longueurs étant exprimées en centimètres.</p>
<p><b>Tâche 1 :</b> Déterminer les valeurs de x pour lesquelles f(x) = g(x) (bornes de la zone à calculer).</p>
<p><b>Tâche 2 :</b> Calculer l'aire de la pièce métallique délimitée par ces deux courbes sur cet intervalle.</p>
<p><i>Cette situation mobilise : la résolution d'une équation pour trouver des bornes, et le calcul d'une aire entre deux courbes par intégration.</i></p>
""",
    },
    {
        "id": 'maths-probabilites-cours',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 3',
        "titre": 'Probabilités — Cours',
        "type": 'Cours',
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


<h3>6. Arbre pondéré</h3>
<p>Un arbre pondéré représente une succession d'épreuves : chaque branche porte une probabilité, et la probabilité d'un chemin complet est le produit des probabilités des branches qui le composent. La somme des probabilités partant d'un même nœud vaut toujours 1.</p>

<h3>7. Épreuve de Bernoulli et loi binomiale</h3>
<p>Une épreuve de Bernoulli n'a que deux issues (succès/échec) de probabilités p et 1-p. Répétée n fois de façon indépendante, le nombre de succès suit une loi binomiale : P(X=k) = C(n,k)×pᵏ×(1-p)ⁿ⁻ᵏ.</p>

<h3>Point d'attention série C</h3>
<p>La série C insiste davantage sur les lois de probabilité (loi binomiale notamment) et le calcul d'espérance/variance dans des situations complexes.</p>
""",
    },
    {
        "id": 'maths-probabilites-exercices',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 3',
        "titre": 'Probabilités — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un sac contient 5 boules rouges et 3 boules vertes. On tire une boule au hasard. Calculer la probabilité de tirer une boule rouge.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Dans une classe, 60% des élèves sont des filles. Parmi elles, 40% pratiquent un sport. Parmi les garçons, 55% pratiquent un sport. Calculer la probabilité qu'un élève choisi au hasard pratique un sport.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Une urne contient 10 boules numérotées de 1 à 10. On tire 3 boules sans remise. Soit X le nombre de boules paires tirées. Déterminer la loi de probabilité de X, puis calculer E(X).</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un contrôle de qualité dans une usine teste des ampoules. La probabilité qu'une ampoule soit défectueuse est de 0,05. On prélève un lot de 10 ampoules au hasard, de manière indépendante.</p>
<p><b>Tâche 1 :</b> Justifier que le nombre d'ampoules défectueuses dans ce lot suit une loi binomiale, en précisant ses paramètres.</p>
<p><b>Tâche 2 :</b> Calculer la probabilité qu'exactement 2 ampoules du lot soient défectueuses.</p>
<p><i>Cette situation mobilise : la reconnaissance d'un schéma de Bernoulli répété et l'application de la formule de la loi binomiale.</i></p>
""",
    },
    {
        "id": 'physique-mecanique-cours',
        "matiere": 'Physique',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Mécanique — Lois de Newton — Cours',
        "type": 'Cours',
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


<h3>6. Travail et énergie (complément)</h3>
<p>Le travail d'une force constante F⃗ sur un déplacement d est W = F×d×cos(θ), où θ est l'angle entre la force et le déplacement. Le théorème de l'énergie cinétique relie le travail des forces à la variation d'énergie cinétique : W(ΣF⃗) = ΔEc = ½m·v²(final) - ½m·v²(initial).</p>

<h3>7. Méthode de résolution d'un problème de mécanique</h3>
<p>1) Faire le bilan des forces (schéma). 2) Choisir un repère adapté. 3) Appliquer le PFD (ΣF⃗ = ma⃗) en projetant sur les axes. 4) Résoudre le système d'équations obtenu.</p>

<h3>Point d'attention série C</h3>
<p>La série C traite plus fréquemment des systèmes avec plusieurs forces combinées (frottements, plans inclinés, mouvements circulaires) demandant une décomposition vectorielle rigoureuse.</p>
""",
    },
    {
        "id": 'physique-mecanique-exercices',
        "matiere": 'Physique',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Mécanique — Lois de Newton — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un corps de masse 2 kg est soumis à une force constante de 10 N. Calculer son accélération (on néglige les frottements).</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Une balle est lâchée sans vitesse initiale d'une hauteur de 20 m. Calculer sa vitesse à l'arrivée au sol (g = 10 m/s²).</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Un solide de masse 5 kg glisse sans frottement sur un plan incliné à 30° par rapport à l'horizontale. Calculer son accélération le long du plan, puis la vitesse acquise après avoir parcouru 4 m sur le plan.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un skieur de masse 70 kg dévale une piste inclinée à 20° par rapport à l'horizontale, sans frottement, sur une longueur de 100 m, en partant du repos.</p>
<p><b>Tâche 1 :</b> Calculer l'accélération du skieur le long de la piste.</p>
<p><b>Tâche 2 :</b> Calculer sa vitesse (en m/s puis en km/h) à l'arrivée en bas de la piste.</p>
<p><i>Cette situation mobilise : l'application du PFD sur un plan incliné, et le calcul de vitesse à partir de l'accélération et de la distance.</i></p>
""",
    },
    {
        "id": 'physique-electricite-cours',
        "matiere": 'Physique',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Électricité — Circuit RC — Cours',
        "type": 'Cours',
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


<h3>6. Lecture d'un oscillogramme</h3>
<p>Sur un oscillogramme représentant u(t) lors d'une charge ou décharge, on peut lire graphiquement τ : c'est l'abscisse du point où la tangente à l'origine coupe l'asymptote horizontale (valeur finale E, ou 0 pour une décharge).</p>

<h3>7. Méthode de résolution d'un exercice de circuit RC</h3>
<p>1) Identifier s'il s'agit d'une charge ou d'une décharge. 2) Écrire la loi des mailles. 3) En déduire l'équation différentielle. 4) Utiliser la solution générale u(t) adaptée, avec τ = RC.</p>

<h3>Point d'attention série C</h3>
<p>La série C exige la résolution complète de l'équation différentielle (pas seulement l'utilisation de la formule), avec justification mathématique de la solution.</p>
""",
    },
    {
        "id": 'physique-electricite-exercices',
        "matiere": 'Physique',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Électricité — Circuit RC — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un condensateur de capacité C = 100 µF est chargé sous une tension de 12 V. Calculer la charge Q stockée et l'énergie E emmagasinée.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Un circuit RC a R = 1000 Ω et C = 200 µF. Calculer la constante de temps τ.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Établir l'équation différentielle vérifiée par u(t) lors de la charge d'un condensateur à travers une résistance R sous une tension E, puis vérifier que u(t) = E(1-e^(-t/RC)) est bien solution.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un flash d'appareil photo utilise un condensateur de 470 µF chargé sous 300 V, qui se décharge dans une lampe à travers une résistance de 10 Ω lors du déclenchement.</p>
<p><b>Tâche 1 :</b> Calculer la constante de temps τ de la décharge.</p>
<p><b>Tâche 2 :</b> Calculer l'énergie disponible dans le condensateur avant le déclenchement du flash.</p>
<p><i>Cette situation mobilise : le calcul de la constante de temps et de l'énergie stockée dans un condensateur, appliqués à un objet réel.</i></p>
""",
    },
    {
        "id": 'chimie-oxydoreduction-cours',
        "matiere": 'Chimie',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Oxydoréduction — Cours',
        "type": 'Cours',
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


<h3>6. Dosage d'oxydoréduction (notion)</h3>
<p>Un dosage redox permet de déterminer la concentration inconnue d'une espèce en la faisant réagir avec une solution de concentration connue, jusqu'à l'équivalence (quantités stœchiométriques). On repère l'équivalence par un changement de couleur ou une mesure de potentiel.</p>

<h3>7. Méthode pour équilibrer une équation redox complète</h3>
<p>1) Écrire les deux demi-équations séparément. 2) Équilibrer les éléments autres que O et H. 3) Équilibrer l'oxygène avec H₂O, l'hydrogène avec H⁺. 4) Équilibrer les charges avec des électrons. 5) Multiplier chaque demi-équation pour égaliser le nombre d'électrons échangés, puis additionner.</p>

<h3>Point d'attention série C</h3>
<p>La série C demande la maîtrise des calculs de potentiel de pile et l'utilisation des potentiels standards (tables de E°), en plus de l'équilibrage classique.</p>
""",
    },
    {
        "id": 'chimie-oxydoreduction-exercices',
        "matiere": 'Chimie',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Oxydoréduction — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Équilibrer la réaction entre le zinc métallique Zn et les ions cuivre Cu²⁺, sachant que les couples sont Zn²⁺/Zn et Cu²⁺/Cu.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Identifier l'oxydant et le réducteur dans la réaction : Fe + Cu²⁺ → Fe²⁺ + Cu.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>On réalise une pile Daniell (couples Zn²⁺/Zn, E° = -0,76 V et Cu²⁺/Cu, E° = +0,34 V). Calculer la force électromotrice de la pile et préciser quelle électrode est la cathode.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> On souhaite recouvrir un objet en fer d'une fine couche de cuivre par une réaction chimique, en le plongeant dans une solution de sulfate de cuivre (Cu²⁺).</p>
<p><b>Tâche 1 :</b> Écrire l'équation de la réaction entre le fer et les ions cuivre (couples Fe²⁺/Fe et Cu²⁺/Cu).</p>
<p><b>Tâche 2 :</b> Identifier l'oxydant et le réducteur, et expliquer pourquoi cette réaction permet effectivement de déposer du cuivre sur l'objet en fer.</p>
<p><i>Cette situation mobilise : l'écriture équilibrée d'une équation redox et l'interprétation physique du sens de la réaction.</i></p>
""",
    },
    {
        "id": 'chimie-cinetique-cours',
        "matiere": 'Chimie',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Cinétique chimique — Cours',
        "type": 'Cours',
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


<h3>6. Loi de vitesse et ordre de réaction (notion introductive)</h3>
<p>Pour certaines réactions, la vitesse peut s'exprimer en fonction de la concentration des réactifs : v = k×[A]ⁿ, où k est la constante de vitesse et n l'ordre de la réaction par rapport à A. Ceci reste une notion introductive au niveau Terminale.</p>

<h3>7. Méthode d'exploitation d'une courbe cinétique</h3>
<p>1) Identifier les grandeurs en abscisse et ordonnée. 2) Repérer l'allure générale (croissante pour un produit, décroissante pour un réactif). 3) Déterminer t½ en cherchant l'abscisse correspondant à la moitié de la valeur finale (ou initiale).</p>

<h3>Point d'attention série C</h3>
<p>La série C demande souvent l'exploitation graphique de courbes cinétiques (détermination de vitesse instantanée par tangente) en plus des définitions.</p>
""",
    },
    {
        "id": 'chimie-cinetique-exercices',
        "matiere": 'Chimie',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Cinétique chimique — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Citer trois facteurs qui peuvent augmenter la vitesse d'une réaction chimique.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Un réactif a une concentration initiale de 0,8 mol/L. Au bout du temps de demi-réaction, quelle est sa concentration restante (si la réaction est totale et le réactif limitant) ?</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>À partir d'un tableau de mesures [A] = f(t), expliquer la méthode pour déterminer graphiquement la vitesse instantanée de disparition de A à un instant t₁ donné.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un chimiste suit l'évolution de la concentration d'un réactif A au cours du temps par des mesures régulières, et observe que la concentration initiale de 1,0 mol/L descend à 0,5 mol/L après 20 minutes, puis reste quasiment stable ensuite.</p>
<p><b>Tâche 1 :</b> Déterminer le temps de demi-réaction t½ à partir de ces données.</p>
<p><b>Tâche 2 :</b> Proposer deux moyens concrets que le chimiste pourrait utiliser pour accélérer cette réaction lors d'une prochaine expérience.</p>
<p><i>Cette situation mobilise : l'identification du temps de demi-réaction à partir de données expérimentales et la connaissance des facteurs cinétiques.</i></p>
""",
    },
    {
        "id": 'maths-suites-cours',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Suites numériques — Cours',
        "type": 'Cours',
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


<h3>6. Limite d'une suite (notion introductive)</h3>
<p>Une suite (uₙ) tend vers +∞ si uₙ devient aussi grand que l'on veut à partir d'un certain rang. Une suite géométrique de raison q tend vers +∞ si q > 1 (et u₀ > 0), vers 0 si -1 < q < 1, et n'a pas de limite si q ≤ -1.</p>

<h3>7. Méthode pour étudier une suite</h3>
<p>1) Identifier le type (arithmétique, géométrique, ou définie par récurrence). 2) Calculer les premiers termes pour observer une tendance. 3) Démontrer rigoureusement (calcul direct ou récurrence) plutôt que de se fier uniquement à l'observation.</p>

<h3>Point d'attention série C</h3>
<p>La série C insiste davantage sur le raisonnement par récurrence et les suites définies par une relation plus complexe (uₙ₊₁ = f(uₙ)).</p>
""",
    },
    {
        "id": 'maths-suites-exercices',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Suites numériques — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Soit (uₙ) une suite arithmétique de premier terme u₀ = 5 et de raison r = 3. Calculer u₁₀, puis la somme S = u₀ + u₁ + ... + u₁₀.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Soit (vₙ) une suite géométrique de premier terme v₀ = 2 et de raison q = 3. Calculer v₅.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Soit (uₙ) définie par u₀ = 1 et uₙ₊₁ = 2uₙ + 1. Démontrer par récurrence que uₙ = 2ⁿ⁺¹ - 1 pour tout n ≥ 0.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un capital de 100 000 FCFA est placé dans une banque à intérêts composés de 5% par an. Chaque année, le capital est multiplié par 1,05.</p>
<p><b>Tâche 1 :</b> Modéliser le capital Cₙ après n années sous forme d'une suite, en précisant sa nature (arithmétique ou géométrique) et sa raison.</p>
<p><b>Tâche 2 :</b> Calculer le capital disponible après 5 ans.</p>
<p><i>Cette situation mobilise : la modélisation d'une situation réelle par une suite géométrique et le calcul de son terme général.</i></p>
""",
    },
    {
        "id": 'maths-derivation-cours',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Dérivation — Cours',
        "type": 'Cours',
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


<h3>6. Tangente à une courbe</h3>
<p>L'équation de la tangente à la courbe de f au point d'abscisse a est : y = f'(a)(x - a) + f(a). Le coefficient directeur de cette tangente est exactement le nombre dérivé f'(a).</p>

<h3>7. Méthode pour étudier les variations d'une fonction</h3>
<p>1) Calculer f'(x). 2) Étudier le signe de f'(x) (factoriser si besoin, étudier le signe de chaque facteur). 3) En déduire le tableau de variation, avec les extremums correspondant aux changements de signe de f'.</p>

<h3>Point d'attention série C</h3>
<p>La série C exige la maîtrise complète de la dérivée composée et son utilisation dans l'étude de fonctions plus complexes (racines, exponentielles combinées).</p>
""",
    },
    {
        "id": 'maths-derivation-exercices',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Dérivation — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Calculer la dérivée de f(x) = 3x² - 5x + 2.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Calculer la dérivée de f(x) = (2x+1)/(x-3) sur son domaine de définition.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Calculer la dérivée de f(x) = √(x²+1), puis étudier le sens de variation de f sur ℝ.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Une entreprise modélise son bénéfice mensuel (en milliers de FCFA) par B(x) = -2x² + 40x - 150, où x représente la quantité produite (en centaines d'unités).</p>
<p><b>Tâche 1 :</b> Calculer B'(x), puis déterminer la quantité x qui maximise le bénéfice.</p>
<p><b>Tâche 2 :</b> Calculer ce bénéfice maximal.</p>
<p><i>Cette situation mobilise : l'utilisation de la dérivée pour trouver un extremum dans un contexte économique concret.</i></p>
""",
    },
    {
        "id": 'maths-vecteurs-cours',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 3',
        "titre": 'Vecteurs et produit scalaire — Cours',
        "type": 'Cours',
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


<h3>6. Équation d'une droite avec un vecteur normal</h3>
<p>Si n⃗(a;b) est un vecteur normal à une droite (perpendiculaire à celle-ci), alors cette droite a une équation de la forme ax + by + c = 0. Cette méthode utilise directement le produit scalaire : pour tout point M(x,y) de la droite, n⃗·AM⃗ = 0.</p>

<h3>7. Méthode pour démontrer une orthogonalité</h3>
<p>1) Déterminer les coordonnées des deux vecteurs concernés. 2) Calculer leur produit scalaire. 3) Conclure : si le produit scalaire est nul, les vecteurs (et donc les droites qu'ils dirigent) sont orthogonaux.</p>

<h3>Point d'attention série C</h3>
<p>La série C combine souvent produit scalaire et démonstrations géométriques (théorème de la médiane, relations métriques dans le triangle).</p>
""",
    },
    {
        "id": 'maths-vecteurs-exercices',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 3',
        "titre": 'Vecteurs et produit scalaire — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Soit A(1;2) et B(4;6). Calculer les coordonnées de AB⃗ et sa norme.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Soit u⃗(2;3) et v⃗(-1;4). Calculer u⃗·v⃗. Les vecteurs sont-ils orthogonaux ?</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Dans un triangle ABC, démontrer à l'aide du produit scalaire que : BC² = AB² + AC² - 2×AB×AC×cos(Â) (théorème d'Al-Kashi).</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un urbaniste place trois lampadaires aux points A(0;0), B(6;0) et C(3;4) (coordonnées en mètres) pour éclairer une place triangulaire, et souhaite vérifier si l'angle en A est droit.</p>
<p><b>Tâche 1 :</b> Calculer les vecteurs AB⃗ et AC⃗.</p>
<p><b>Tâche 2 :</b> À l'aide du produit scalaire, déterminer si l'angle en A est droit.</p>
<p><i>Cette situation mobilise : le calcul de vecteurs à partir de coordonnées et l'utilisation du produit scalaire pour caractériser un angle droit.</i></p>
""",
    },
    {
        "id": 'physique-mouvement-cours',
        "matiere": 'Physique',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Cinématique du mouvement — Cours',
        "type": 'Cours',
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


<h3>6. Représentation graphique du mouvement</h3>
<p>Le graphe x(t) d'un MRU est une droite (pente = vitesse constante). Le graphe v(t) d'un MRUV est une droite (pente = accélération constante). Le graphe x(t) d'un MRUV est une parabole.</p>

<h3>7. Méthode de résolution d'un problème de cinématique</h3>
<p>1) Identifier le type de mouvement (uniforme ou uniformément varié). 2) Choisir les bonnes formules (x(t), v(t)). 3) Utiliser les conditions initiales données dans l'énoncé pour déterminer les constantes (x₀, v₀).</p>

<h3>Point d'attention série C</h3>
<p>La série C traite plus en profondeur le mouvement circulaire et les changements de référentiel, avec davantage de rigueur vectorielle.</p>
""",
    },
    {
        "id": 'physique-mouvement-exercices',
        "matiere": 'Physique',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Cinématique du mouvement — Exercices',
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Une voiture parcourt 150 km en 2 heures à vitesse constante. Calculer sa vitesse moyenne en km/h puis en m/s.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Un mobile part sans vitesse initiale avec une accélération constante de 2 m/s². Calculer sa vitesse et sa position après 5 secondes.</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Un point mobile décrit un cercle de rayon 0,5 m à une vitesse angulaire constante de 4 rad/s. Calculer sa vitesse linéaire et son accélération centripète.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un cycliste roule à vitesse constante de 36 km/h pendant 10 minutes, puis freine avec une décélération constante de 2 m/s² jusqu'à l'arrêt complet.</p>
<p><b>Tâche 1 :</b> Convertir la vitesse initiale en m/s, puis calculer la distance parcourue pendant les 10 premières minutes.</p>
<p><b>Tâche 2 :</b> Calculer le temps et la distance nécessaires pour que le cycliste s'arrête complètement lors du freinage.</p>
<p><i>Cette situation mobilise : le calcul de distance en MRU et l'utilisation des équations du MRUV pour une phase de freinage.</i></p>
""",
    },
    {
        "id": 'chimie-atome-cours',
        "matiere": 'Chimie',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": "Structure de l'atome — Cours",
        "type": 'Cours',
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


<h3>6. Le tableau périodique (lien avec la structure électronique)</h3>
<p>Les éléments d'une même colonne (famille) du tableau périodique ont le même nombre d'électrons de valence, ce qui explique leurs propriétés chimiques similaires. La ligne (période) correspond au nombre de couches électroniques occupées.</p>

<h3>7. Méthode pour déterminer la structure électronique</h3>
<p>1) Identifier Z (numéro atomique = nombre d'électrons pour un atome neutre). 2) Remplir les couches dans l'ordre K, L, M en respectant leur capacité maximale (2, 8, 8 ou 18). 3) Le dernier chiffre donne le nombre d'électrons de valence.</p>

<h3>Point d'attention série C</h3>
<p>La série C demande une maîtrise plus poussée de la configuration électronique complète et son lien avec la position dans le tableau périodique.</p>
""",
    },
    {
        "id": 'chimie-atome-exercices',
        "matiere": 'Chimie',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": "Structure de l'atome — Exercices",
        "type": 'Exercices',
        "contenu": """<h3>Exercice 1 (Niveau D / TI)</h3>
<p>Un atome de sodium a Z = 11 et A = 23. Déterminer le nombre de protons, neutrons et électrons.</p>

<h3>Exercice 2 (Niveau D / TI)</h3>
<p>Calculer la quantité de matière (en mol) contenue dans 36 g d'eau (M(H₂O) = 18 g/mol).</p>

<h3>Exercice 3 (Niveau C — plus difficile)</h3>
<p>Donner la structure électronique complète de l'atome de chlore (Z = 17) en couches K, L, M, et déterminer le nombre d'électrons de valence.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un professeur présente deux atomes X (Z=12) et Y (Z=17) à ses élèves et leur demande de prévoir leur comportement chimique probable à partir de leur structure électronique.</p>
<p><b>Tâche 1 :</b> Donner la structure électronique complète de X et de Y (répartition en couches K, L, M).</p>
<p><b>Tâche 2 :</b> Sachant qu'un atome tend à compléter sa couche externe à 8 électrons (règle de l'octet), indiquer si X aura plutôt tendance à céder ou capter des électrons, et faire de même pour Y.</p>
<p><i>Cette situation mobilise : la détermination de la structure électronique et son lien avec la réactivité chimique prévisible d'un élément.</i></p>
""",
    },
    {
        "id": 'maths-complexes-corriges',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Nombres complexes — Corrigés',
        "type": 'Corrigé',
        "contenu": """<h3>Corrigés indicatifs</h3>
<p>Ex1 : Δ = -36, z₁ = 2+3i, z₂ = 2-3i, |z| = √13 pour les deux.<br>
Ex2 : |z| = 2, arg(z) = π/3, donc z⁶ = 2⁶·e^(i·6·π/3) = 64·e^(i2π) = 64.<br>
Ex3/4 : à traiter en groupe — poste ta démarche dans le chat pour vérification collective.</p>
""",
    },
    {
        "id": 'maths-primitives-corriges',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Primitives et intégrales — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>On cherche une primitive terme à terme : pour 3x², une primitive est x³. Pour -2x, une primitive est -x². Pour 5, une primitive est 5x. On obtient donc F(x) = x³ - x² + 5x + K, où K est une constante réelle quelconque (à ne pas oublier).</p>

<h3>Corrigé — Exercice 2</h3>
<p>Une primitive de 2x+1 est x²+x. Donc I = [x²+x]₀¹ = (1²+1) - (0²+0) = 2 - 0 = 2.</p>

<h3>Corrigé — Exercice 3</h3>
<p>On pose u(x) = x et v'(x) = eˣ, donc u'(x) = 1 et v(x) = eˣ. Par intégration par parties : J = [x·eˣ]₀¹ - ∫₀¹ eˣ dx = (1·e¹ - 0) - [eˣ]₀¹ = e - (e - 1) = e - e + 1 = 1.</p>

<h3>Corrigé — Exercice 4</h3>
<p>On résout x² = x, soit x² - x = 0, soit x(x-1) = 0 : x = 0 ou x = 1. Sur [0;1], on vérifie que x ≥ x² (par exemple en x=0,5 : 0,5 > 0,25), donc l'aire vaut A = ∫₀¹ (x - x²) dx = [x²/2 - x³/3]₀¹ = (1/2 - 1/3) - 0 = 1/6 unité d'aire.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> f(x) = g(x) donne 4 - x² = x, soit x² + x - 4 = 0. Δ = 1 + 16 = 17, x = (-1 ± √17)/2. On garde les deux valeurs comme bornes de la zone étudiée.</p>
<p><b>Tâche 2 :</b> L'aire est A = ∫ [f(x) - g(x)] dx = ∫ [4 - x² - x] dx entre les deux bornes trouvées — à calculer en trouvant une primitive de 4 - x² - x, soit 4x - x³/3 - x²/2, puis en évaluant aux deux bornes (calcul numérique à finaliser avec les valeurs exactes de x trouvées).</p>
""",
    },
    {
        "id": 'maths-probabilites-corriges',
        "matiere": 'Mathématiques',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 3',
        "titre": 'Probabilités — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Nombre total de boules : 5 + 3 = 8. Nombre de boules rouges : 5. Par équiprobabilité, P(rouge) = 5/8.</p>

<h3>Corrigé — Exercice 2</h3>
<p>Notons F l'événement "être une fille" et S "pratiquer un sport". On a P(F) = 0,6, P(S|F) = 0,4, et P(S|F̄) = 0,55, avec P(F̄) = 0,4. D'après la formule des probabilités totales : P(S) = P(S|F)×P(F) + P(S|F̄)×P(F̄) = 0,4×0,6 + 0,55×0,4 = 0,24 + 0,22 = 0,46.</p>

<h3>Corrigé — Exercice 3</h3>
<p>Il y a 5 boules paires (2,4,6,8,10) et 5 impaires parmi les 10. X suit une loi hypergéométrique. La loi de probabilité s'obtient en dénombrant les tirages possibles pour X=0,1,2,3, et E(X) = n×(nombre de boules paires/total) = 3×(5/10) = 1,5 (formule de l'espérance pour une loi hypergéométrique).</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> On répète 10 fois une épreuve à deux issues indépendantes (défectueuse ou non), avec probabilité de succès (défaut) constante p=0,05. C'est bien un schéma de Bernoulli répété : X suit la loi binomiale de paramètres n=10 et p=0,05.</p>
<p><b>Tâche 2 :</b> P(X=2) = C(10,2)×(0,05)²×(0,95)⁸ = 45×0,0025×0,6634 ≈ 0,0746, soit environ 7,5%.</p>
""",
    },
    {
        "id": 'physique-mecanique-corriges',
        "matiere": 'Physique',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Mécanique — Lois de Newton — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>D'après le PFD, a = F/m = 10/2 = 5 m/s².</p>

<h3>Corrigé — Exercice 2</h3>
<p>La balle est en chute libre : v² = 2gh (formule dérivée du PFD pour une chute sans vitesse initiale), donc v = √(2×10×20) = √400 = 20 m/s.</p>

<h3>Corrigé — Exercice 3</h3>
<p>Sur le plan incliné, la composante du poids parallèle au plan est mg·sin(30°). D'après le PFD projeté sur l'axe du plan : a = g·sin(30°) = 10×0,5 = 5 m/s². Ensuite, avec v² = 2a·d (formule du MRUV sans vitesse initiale) : v² = 2×5×4 = 40, donc v = √40 ≈ 6,32 m/s.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> a = g·sin(20°) = 10×0,342 ≈ 3,42 m/s².</p>
<p><b>Tâche 2 :</b> v² = 2×a×d = 2×3,42×100 = 684, donc v = √684 ≈ 26,15 m/s, soit environ 94,1 km/h (en multipliant par 3,6).</p>
""",
    },
    {
        "id": 'physique-electricite-corriges',
        "matiere": 'Physique',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Électricité — Circuit RC — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Q = C×U = 100×10⁻⁶×12 = 1,2×10⁻³ C. Énergie : E = ½×C×U² = 0,5×100×10⁻⁶×144 = 7,2×10⁻³ J.</p>

<h3>Corrigé — Exercice 2</h3>
<p>τ = R×C = 1000×200×10⁻⁶ = 0,2 s.</p>

<h3>Corrigé — Exercice 3</h3>
<p>La loi des mailles donne E = u_R + u_C, avec u_R = R×i et i = C×(du/dt). Donc E = RC×(du/dt) + u, soit l'équation différentielle RC·(du/dt) + u = E. En substituant u(t) = E(1-e^(-t/RC)), on calcule du/dt = (E/RC)×e^(-t/RC), puis RC×(E/RC)×e^(-t/RC) + E(1-e^(-t/RC)) = E×e^(-t/RC) + E - E×e^(-t/RC) = E, ce qui vérifie bien l'équation.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> τ = R×C = 10×470×10⁻⁶ = 4,7×10⁻³ s, soit environ 4,7 ms.</p>
<p><b>Tâche 2 :</b> E = ½×C×U² = 0,5×470×10⁻⁶×300² = 0,5×470×10⁻⁶×90000 ≈ 21,15 J.</p>
""",
    },
    {
        "id": 'chimie-oxydoreduction-corriges',
        "matiere": 'Chimie',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Oxydoréduction — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Demi-équations : Zn → Zn²⁺ + 2e⁻ (oxydation) et Cu²⁺ + 2e⁻ → Cu (réduction). Le nombre d'électrons échangés est déjà égal (2 de chaque côté), donc l'équation globale est : Zn + Cu²⁺ → Zn²⁺ + Cu.</p>

<h3>Corrigé — Exercice 2</h3>
<p>Fe perd des électrons (Fe → Fe²⁺ + 2e⁻) : c'est le réducteur, il est oxydé. Cu²⁺ gagne des électrons (Cu²⁺ + 2e⁻ → Cu) : c'est l'oxydant, il est réduit.</p>

<h3>Corrigé — Exercice 3</h3>
<p>E = E°(cathode, réduction) - E°(anode, oxydation) = E°(Cu²⁺/Cu) - E°(Zn²⁺/Zn) = 0,34 - (-0,76) = 1,10 V. La cathode est l'électrode où se produit la réduction, donc l'électrode de cuivre (potentiel le plus élevé).</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Demi-équations : Fe → Fe²⁺ + 2e⁻ et Cu²⁺ + 2e⁻ → Cu. Équation globale : Fe + Cu²⁺ → Fe²⁺ + Cu.</p>
<p><b>Tâche 2 :</b> Le fer est le réducteur (il cède des électrons), les ions Cu²⁺ sont l'oxydant (ils captent des électrons et se transforment en cuivre métallique Cu, qui se dépose sur l'objet en fer) — c'est bien ce dépôt métallique qui recouvre l'objet.</p>
""",
    },
    {
        "id": 'chimie-cinetique-corriges',
        "matiere": 'Chimie',
        "classe": 'Terminale',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Cinétique chimique — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Température (plus elle est élevée, plus la vitesse augmente), concentration des réactifs (plus elle est élevée, plus les chocs efficaces sont fréquents), et catalyseur (abaisse l'énergie d'activation).</p>

<h3>Corrigé — Exercice 2</h3>
<p>Au bout du temps de demi-réaction, la moitié du réactif limitant a été consommée (si la réaction est totale) : concentration restante = 0,8/2 = 0,4 mol/L.</p>

<h3>Corrigé — Exercice 3</h3>
<p>On trace la tangente à la courbe [A]=f(t) au point d'abscisse t₁. Le coefficient directeur de cette tangente donne d[A]/dt à cet instant. La vitesse instantanée de disparition de A est l'opposé de cette valeur (car [A] diminue) : v = -d[A]/dt à l'instant t₁.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> La concentration passe de 1,0 à 0,5 mol/L (soit la moitié) en 20 minutes : le temps de demi-réaction est donc t½ = 20 minutes.</p>
<p><b>Tâche 2 :</b> Augmenter la température du milieu réactionnel, ou ajouter un catalyseur adapté à cette réaction.</p>
""",
    },
    {
        "id": 'maths-suites-corriges',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Suites numériques — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>u₁₀ = u₀ + 10r = 5 + 10×3 = 35. Somme des 11 premiers termes (de u₀ à u₁₀) : S = 11×(u₀+u₁₀)/2 = 11×(5+35)/2 = 11×20 = 220.</p>

<h3>Corrigé — Exercice 2</h3>
<p>v₅ = v₀×q⁵ = 2×3⁵ = 2×243 = 486.</p>

<h3>Corrigé — Exercice 3</h3>
<p><b>Initialisation :</b> pour n=0, u₀=1 et 2⁰⁺¹-1 = 2-1 = 1. La propriété est vraie au rang 0.<br>
<b>Hérédité :</b> supposons uₙ = 2ⁿ⁺¹-1 vraie pour un n donné. Alors uₙ₊₁ = 2uₙ+1 = 2(2ⁿ⁺¹-1)+1 = 2ⁿ⁺²-2+1 = 2ⁿ⁺²-1 = 2⁽ⁿ⁺¹⁾⁺¹-1, ce qui est bien la propriété au rang n+1.<br>
<b>Conclusion :</b> par le principe de récurrence, uₙ = 2ⁿ⁺¹-1 pour tout n ≥ 0.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Chaque année, Cₙ₊₁ = 1,05×Cₙ : c'est une suite géométrique de raison q=1,05 et de premier terme C₀ = 100 000.</p>
<p><b>Tâche 2 :</b> C₅ = 100 000×1,05⁵ ≈ 100 000×1,2763 ≈ 127 628 FCFA.</p>
""",
    },
    {
        "id": 'maths-derivation-corriges',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 2',
        "titre": 'Dérivation — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>f'(x) = 6x - 5 (dérivée terme à terme : (3x²)'=6x, (-5x)'=-5, (2)'=0).</p>

<h3>Corrigé — Exercice 2</h3>
<p>Avec u(x)=2x+1, v(x)=x-3 : u'(x)=2, v'(x)=1. f'(x) = (u'v-uv')/v² = [2(x-3) - (2x+1)(1)] / (x-3)² = [2x-6-2x-1]/(x-3)² = -7/(x-3)².</p>

<h3>Corrigé — Exercice 3</h3>
<p>f(x)=√(x²+1) = (x²+1)^(1/2). En posant u=x²+1, f'(x) = u'/(2√u) = 2x/(2√(x²+1)) = x/√(x²+1). Comme √(x²+1) > 0 toujours, le signe de f'(x) est celui de x : f est décroissante sur ]-∞;0], croissante sur [0;+∞[, avec un minimum en x=0.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> B'(x) = -4x + 40. B'(x)=0 donne x = 10. Comme le coefficient de x² est négatif, il s'agit bien d'un maximum en x=10.</p>
<p><b>Tâche 2 :</b> B(10) = -2×100 + 40×10 - 150 = -200+400-150 = 50, soit un bénéfice maximal de 50 000 FCFA (pour x en centaines d'unités).</p>
""",
    },
    {
        "id": 'maths-vecteurs-corriges',
        "matiere": 'Mathématiques',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 3',
        "titre": 'Vecteurs et produit scalaire — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>AB⃗(x_B-xₐ; y_B-yₐ) = (4-1; 6-2) = (3;4). ‖AB⃗‖ = √(3²+4²) = √25 = 5.</p>

<h3>Corrigé — Exercice 2</h3>
<p>u⃗·v⃗ = (2)×(-1) + (3)×(4) = -2+12 = 10. Comme le produit scalaire n'est pas nul, les vecteurs ne sont pas orthogonaux.</p>

<h3>Corrigé — Exercice 3</h3>
<p>On écrit BC⃗ = AC⃗ - AB⃗. Alors BC² = BC⃗·BC⃗ = (AC⃗-AB⃗)·(AC⃗-AB⃗) = AC⃗·AC⃗ - 2×AC⃗·AB⃗ + AB⃗·AB⃗ = AC² + AB² - 2×AB×AC×cos(Â), car AC⃗·AB⃗ = AB×AC×cos(Â) par définition du produit scalaire.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> AB⃗ = (6-0; 0-0) = (6;0). AC⃗ = (3-0; 4-0) = (3;4).</p>
<p><b>Tâche 2 :</b> AB⃗·AC⃗ = 6×3 + 0×4 = 18. Comme ce produit scalaire n'est pas nul, l'angle en A n'est pas droit.</p>
""",
    },
    {
        "id": 'physique-mouvement-corriges',
        "matiere": 'Physique',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'Cinématique du mouvement — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>v = 150/2 = 75 km/h. Conversion : 75×(1000/3600) ≈ 20,83 m/s.</p>

<h3>Corrigé — Exercice 2</h3>
<p>v(5) = 0 + 2×5 = 10 m/s. x(5) = 0 + 0×5 + ½×2×5² = 25 m.</p>

<h3>Corrigé — Exercice 3</h3>
<p>v = R×ω = 0,5×4 = 2 m/s. a = v²/R = 2²/0,5 = 4/0,5 = 8 m/s².</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> 36 km/h = 36/3,6 = 10 m/s. Distance en MRU : d = v×t = 10×600 (10 minutes = 600s) = 6000 m = 6 km.</p>
<p><b>Tâche 2 :</b> Freinage : v(t) = v₀ - a×t, l'arrêt correspond à v=0, donc t = v₀/a = 10/2 = 5 s. Distance parcourue : d = v₀×t - ½×a×t² = 10×5 - ½×2×25 = 50-25 = 25 m.</p>
""",
    },
    {
        "id": 'chimie-atome-corriges',
        "matiere": 'Chimie',
        "classe": 'Premiere',
        "series": ['C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": "Structure de l'atome — Corrigés",
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Z=11 protons, donc 11 électrons (atome neutre). Neutrons = A - Z = 23-11 = 12.</p>

<h3>Corrigé — Exercice 2</h3>
<p>n = m/M = 36/18 = 2 mol.</p>

<h3>Corrigé — Exercice 3</h3>
<p>Z=17 électrons à répartir : couche K (2 max) → 2 électrons ; couche L (8 max) → 8 électrons ; il reste 17-2-8=7 électrons pour la couche M → 7 électrons. Structure : K(2) L(8) M(7). Le nombre d'électrons de valence est celui de la dernière couche occupée : 7.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> X (Z=12) : K(2) L(8) M(2). Y (Z=17) : K(2) L(8) M(7).</p>
<p><b>Tâche 2 :</b> X a 2 électrons de valence : il aura tendance à céder ces 2 électrons pour atteindre une couche complète à 8 (règle de l'octet). Y a 7 électrons de valence : il aura tendance à capter 1 électron pour compléter sa couche externe à 8.</p>
""",
    },
    {
        "id": 'philo-conscience-cours',
        "matiere": 'Philosophie',
        "classe": 'Terminale',
        "series": ['A', 'C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'La conscience — Cours',
        "type": 'Cours',
        "contenu": """
<h3>1. Qu'est-ce que la conscience ?</h3>
<p>La conscience est la faculté qui permet à un individu de se percevoir lui-même, de percevoir le monde extérieur, et de réfléchir sur ses propres pensées. On distingue la <b>conscience spontanée</b> (perception immédiate du monde et de soi) et la <b>conscience réfléchie</b> (capacité à se prendre soi-même comme objet de pensée, à s'interroger sur ses propres actes).</p>

<h3>2. Descartes et le cogito</h3>
<p>Descartes, dans le <i>Discours de la méthode</i>, affirme "Je pense donc je suis" (cogito ergo sum). Pour lui, la conscience est la certitude première : même si je doute de tout, je ne peux douter que je pense, donc que j'existe en tant qu'être pensant. La conscience est ici transparente à elle-même : je sais immédiatement ce que je pense.</p>

<h3>3. La remise en cause par Freud</h3>
<p>Freud, avec la découverte de l'inconscient, remet en question la transparence de la conscience. Selon lui, une grande partie de notre vie psychique (désirs refoulés, pulsions) échappe à la conscience et pourtant influence nos actes. La conscience n'est donc pas toute la vie psychique, mais seulement une partie visible d'un appareil psychique plus vaste.</p>

<h3>4. Conscience et liberté</h3>
<p>Sartre affirme que l'homme est "condamné à être libre" : la conscience, en se distinguant des choses (qui sont ce qu'elles sont), a le pouvoir de se projeter, de choisir, de se définir par ses actes. La conscience est donc liée à la responsabilité : parce que je suis conscient de mes actes, je peux en être tenu responsable.</p>

<h3>5. Enjeux du débat</h3>
<p>Le problème philosophique central : la conscience nous donne-t-elle un accès fiable à la vérité sur nous-mêmes, ou est-elle en partie illusoire, aveugle à ce qui nous détermine réellement (inconscient, déterminismes sociaux, biologiques) ?</p>


<h3>6. Bergson et la durée</h3>
<p>Bergson distingue le temps mesurable (celui de l'horloge) de la <i>durée vécue</i>, propre à la conscience : notre conscience ne perçoit pas le temps comme une succession d'instants séparés, mais comme un flux continu où passé et présent s'interpénètrent.</p>

<h3>7. Méthode pour traiter un sujet de dissertation sur la conscience</h3>
<p>1) Bien définir les termes du sujet dès l'introduction. 2) Formuler une problématique qui met en tension deux positions (ex: conscience = transparence vs conscience = illusion). 3) Construire un plan dialectique (thèse/antithèse/synthèse) ou thématique, toujours illustré d'exemples ou de références précises (Descartes, Freud, Sartre, Bergson).</p>

<h3>Point d'attention série A</h3>
<p>La série A (littéraire) attend une argumentation plus développée, avec davantage de références précises aux auteurs (citations, contextualisation des œuvres) et une problématisation plus fine que pour les séries scientifiques.</p>
""",
    },
    {
        "id": 'philo-conscience-exercices',
        "matiere": 'Philosophie',
        "classe": 'Terminale',
        "series": ['A', 'C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'La conscience — Exercices',
        "type": 'Exercices',
        "contenu": """
<h3>Exercice 1 (Niveau D / TI / C)</h3>
<p>Expliquer en un paragraphe la différence entre conscience spontanée et conscience réfléchie, avec un exemple personnel pour chacune.</p>

<h3>Exercice 2 (Niveau D / TI / C)</h3>
<p>Peut-on dire que l'inconscient freudien contredit totalement la thèse cartésienne de la transparence de la conscience ? Justifier en une dizaine de lignes.</p>

<h3>Situation-problème / dissertation (Niveau A — plus exigeant)</h3>
<p><b>Sujet :</b> "La conscience est-elle une preuve suffisante de la connaissance de soi ?"</p>
<p>Consignes : Construire une introduction avec accroche, définition des termes, problématique et annonce de plan. Développer au moins deux parties opposant la thèse cartésienne (conscience = accès direct à soi) et la thèse freudienne (conscience limitée par l'inconscient). Illustrer chaque partie d'un exemple ou d'une référence philosophique précise.</p>

<h3>Situation-problème / dissertation courte (évaluation des ressources)</h3>
<p><b>Sujet :</b> "Peut-on se connaître soi-même sans l'aide d'autrui ?"</p>
<p><b>Tâche 1 :</b> Formuler une problématique qui met en tension l'idée cartésienne d'un accès direct à soi par la conscience, et l'idée que le regard d'autrui pourrait être nécessaire à la connaissance de soi.</p>
<p><b>Tâche 2 :</b> Construire un plan en deux parties, chacune appuyée sur au moins une référence philosophique précise (auteur et notion).</p>
<p><i>Cette situation mobilise : la problématisation d'un sujet et la construction argumentée d'un plan de dissertation, compétences centrales évaluées à l'examen.</i></p>
""",
    },
    {
        "id": 'reseau-terminale-cours',
        "matiere": 'Réseau',
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": 'Module 2 : Réseau, Internet et sécurité',
        "titre": 'Réseaux informatiques — Cours',
        "type": 'Cours',
        "contenu": """
<h3>1. Définitions fondamentales</h3>
<p>Un <b>réseau informatique</b> est un ensemble d'équipements (ordinateurs, serveurs, imprimantes...) reliés entre eux pour échanger des données. On distingue selon l'étendue géographique : <b>LAN</b> (Local Area Network — réseau local, ex: réseau d'un lycée), <b>MAN</b> (Metropolitan Area Network — échelle d'une ville), <b>WAN</b> (Wide Area Network — grande distance, ex: Internet).</p>

<h3>2. Topologies de réseau</h3>
<p><b>Topologie en bus :</b> tous les équipements sont reliés à un même câble central. Simple mais vulnérable (une coupure isole tout le réseau).</p>
<p><b>Topologie en étoile :</b> tous les équipements sont reliés à un équipement central (switch/hub). La plus utilisée actuellement — une panne d'un poste n'affecte pas les autres.</p>
<p><b>Topologie en anneau :</b> chaque équipement est relié à exactement deux autres, formant une boucle. Les données circulent dans un sens (ou les deux).</p>

<h3>3. Les équipements réseau</h3>
<p><b>Switch (commutateur) :</b> relie plusieurs équipements d'un même réseau local, dirige les données vers le bon destinataire.</p>
<p><b>Routeur :</b> relie deux réseaux différents (ex: le réseau local à Internet), achemine les paquets de données selon leur adresse IP.</p>
<p><b>Point d'accès Wi-Fi :</b> permet la connexion sans fil au réseau.</p>

<h3>4. Le modèle TCP/IP et l'adressage IP</h3>
<p>Une adresse IP identifie de façon unique un équipement sur un réseau. Format IPv4 : quatre nombres de 0 à 255 séparés par des points (ex: 192.168.1.10). Une adresse IP comprend une partie réseau et une partie machine, déterminées par le <b>masque de sous-réseau</b>.</p>
<p>Le protocole <b>TCP</b> (Transmission Control Protocol) découpe les données en paquets et garantit leur arrivée correcte. Le protocole <b>IP</b> (Internet Protocol) s'occupe de l'acheminement des paquets à travers le réseau.</p>

<h3>5. Sécurité informatique — notions essentielles</h3>
<p><b>Pare-feu (firewall) :</b> filtre le trafic entrant/sortant d'un réseau selon des règles définies, bloque les connexions non autorisées.</p>
<p><b>Chiffrement :</b> transforme une donnée lisible en donnée illisible sans la clé de déchiffrement, pour protéger la confidentialité.</p>
<p><b>Menaces courantes :</b> virus (se reproduit en infectant d'autres fichiers), ver (se propage seul via le réseau), phishing (tentative de vol d'identifiants par usurpation), attaque par déni de service (DoS, saturation volontaire d'un serveur).</p>

<h3>Point d'attention</h3>
<p>Les épreuves TI demandent souvent de justifier le choix d'une topologie ou d'un équipement selon un contexte donné (nombre de postes, budget, contrainte de fiabilité) — pas seulement de réciter les définitions.</p>
""",
    },
    {
        "id": 'reseau-terminale-exercices',
        "matiere": 'Réseau',
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": 'Module 2 : Réseau, Internet et sécurité',
        "titre": 'Réseaux informatiques — Exercices',
        "type": 'Exercices',
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Donner la différence entre un switch et un routeur, avec un exemple d'usage pour chacun.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Citer deux avantages et un inconvénient de la topologie en étoile.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Le proviseur d'un lycée de 300 élèves souhaite équiper l'établissement d'un réseau informatique reliant la salle des professeurs, la bibliothèque, le secrétariat et une salle informatique de 20 postes. Il souhaite que la panne d'un poste n'affecte jamais le reste du réseau, et veut aussi protéger le réseau contre les intrusions venant d'Internet.</p>
<p><b>Tâche 1 :</b> Proposer et justifier une topologie de réseau adaptée à cette situation.</p>
<p><b>Tâche 2 :</b> Lister les équipements réseau nécessaires (avec leur rôle précis) pour relier ces quatre salles et connecter l'ensemble à Internet.</p>
<p><b>Tâche 3 :</b> Proposer une mesure de sécurité pour protéger le réseau de l'établissement contre les menaces venant d'Internet, en expliquant son fonctionnement.</p>
<p><i>Cette situation mobilise : le choix argumenté d'une architecture réseau, l'identification des équipements adaptés à un contexte réel, et une mesure de sécurité justifiée — compétences visées par le module.</i></p>
""",
    },
    {
        "id": 'si-premiere-cours',
        "matiere": "Système d'Information",
        "classe": 'Premiere',
        "series": ['TI'],
        "sequence": "Introduction aux systèmes d'information",
        "titre": "Systèmes d'Information — Cours (Première)",
        "type": 'Cours',
        "contenu": """
<h3>1. Qu'est-ce qu'un système d'information (SI) ?</h3>
<p>Un système d'information est l'ensemble organisé des ressources (personnes, données, procédures, matériels, logiciels) permettant de collecter, stocker, traiter et diffuser de l'information dans une organisation. Exemple : le système qui gère les inscriptions et notes des élèves dans un établissement scolaire.</p>

<h3>2. Les fonctions d'un SI</h3>
<p><b>Collecte :</b> saisie de données (ex: formulaire d'inscription). <b>Stockage :</b> conservation organisée des données (ex: base de données des élèves). <b>Traitement :</b> transformation des données en informations utiles (ex: calcul de moyennes). <b>Diffusion :</b> mise à disposition de l'information aux bonnes personnes (ex: bulletin remis aux parents).</p>

<h3>3. Notion de donnée, information et connaissance</h3>
<p>Une <b>donnée</b> est un fait brut sans interprétation (ex: 14). Une <b>information</b> est une donnée mise en contexte, porteuse de sens (ex: "14 est la moyenne de Kevin en mathématiques"). Une <b>connaissance</b> résulte de l'analyse d'informations pour agir (ex: "Kevin a besoin de soutien en mathématiques").</p>

<h3>4. Introduction aux bases de données</h3>
<p>Une base de données organise l'information en <b>tables</b> composées de <b>lignes</b> (enregistrements) et de <b>colonnes</b> (champs). Exemple : une table "Élèves" avec les colonnes Nom, Prénom, Classe, Date de naissance.</p>
<p>Une <b>clé primaire</b> est un champ (ou groupe de champs) qui identifie de façon unique chaque enregistrement d'une table (ex: un numéro matricule).</p>

<h3>5. Le modèle entité-association (notions de base)</h3>
<p>Une <b>entité</b> représente un objet du monde réel à mémoriser (ex: Élève, Cours). Une <b>association</b> représente un lien entre deux entités (ex: un Élève "suit" un Cours). Chaque entité possède des <b>attributs</b> (propriétés), par exemple pour Élève : nom, prénom, date de naissance.</p>

<h3>Point d'attention</h3>
<p>En Première TI, l'accent est mis sur la compréhension des concepts (donnée/information, entités/associations) plus que sur la manipulation technique poussée, qui sera approfondie en Terminale.</p>
""",
    },
    {
        "id": 'si-premiere-exercices',
        "matiere": "Système d'Information",
        "classe": 'Premiere',
        "series": ['TI'],
        "sequence": "Introduction aux systèmes d'information",
        "titre": "Systèmes d'Information — Exercices (Première)",
        "type": 'Exercices',
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Donner un exemple de donnée, d'information et de connaissance à partir d'un contexte de bibliothèque scolaire.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Expliquer pourquoi une clé primaire doit être unique pour chaque enregistrement d'une table.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Le club informatique d'un lycée souhaite organiser une base de données pour gérer les emprunts de livres à la bibliothèque de l'établissement. Il faut mémoriser les livres disponibles, les élèves inscrits, et savoir quel élève a emprunté quel livre et à quelle date.</p>
<p><b>Tâche 1 :</b> Identifier les entités nécessaires pour ce système (au moins deux).</p>
<p><b>Tâche 2 :</b> Proposer au moins trois attributs pertinents pour chaque entité identifiée.</p>
<p><b>Tâche 3 :</b> Décrire en une phrase l'association qui relie ces entités entre elles.</p>
<p><i>Cette situation mobilise : l'identification d'entités et d'attributs pertinents à partir d'un besoin réel — compétence de base en modélisation de données.</i></p>
""",
    },
    {
        "id": 'si-terminale-cours',
        "matiere": "Système d'Information",
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": "Module 3 : Systèmes d'Information et bases de données",
        "titre": "Systèmes d'Information — Cours (Terminale)",
        "type": 'Cours',
        "contenu": """
<h3>1. Rappel et approfondissement du modèle entité-association</h3>
<p>En Terminale, on approfondit la modélisation : une association peut avoir une <b>cardinalité</b>, qui précise combien d'occurrences d'une entité sont liées à combien d'occurrences d'une autre. Exemple : un Élève "suit" plusieurs Cours (cardinalité 0,n), un Cours est "suivi par" plusieurs Élèves (cardinalité 0,n) — c'est une relation <b>plusieurs-à-plusieurs</b>.</p>

<h3>2. Le modèle relationnel</h3>
<p>Le modèle entité-association se traduit en <b>tables relationnelles</b>. Une relation plusieurs-à-plusieurs nécessite une <b>table d'association</b> intermédiaire contenant les clés primaires des deux tables liées (appelées <b>clés étrangères</b>).</p>

<h3>3. Introduction au langage SQL</h3>
<p><b>Créer une table :</b> <code>CREATE TABLE Eleve (id INTEGER PRIMARY KEY, nom TEXT, classe TEXT);</code></p>
<p><b>Insérer une donnée :</b> <code>INSERT INTO Eleve (nom, classe) VALUES ('Kamga', 'TleD');</code></p>
<p><b>Interroger une table :</b> <code>SELECT nom FROM Eleve WHERE classe = 'TleD';</code> — cette requête sélectionne les noms de tous les élèves de Terminale D.</p>
<p><b>Jointure :</b> permet de combiner des données de plusieurs tables liées par une clé étrangère, ex: <code>SELECT Eleve.nom, Cours.titre FROM Eleve JOIN Inscription ON Eleve.id = Inscription.eleve_id JOIN Cours ON Cours.id = Inscription.cours_id;</code></p>

<h3>4. Normalisation (notions de base)</h3>
<p>La normalisation vise à éviter la redondance des données dans une base. Une table est mal conçue si une même information (ex: le nom d'un professeur) est répétée dans plusieurs lignes sans nécessité — elle devrait être stockée une seule fois dans une table dédiée.</p>

<h3>5. Sécurité et gouvernance de l'information</h3>
<p>Un SI doit garantir : la <b>confidentialité</b> (seules les personnes autorisées accèdent à l'information), l'<b>intégrité</b> (les données ne sont pas altérées sans autorisation), et la <b>disponibilité</b> (l'information est accessible quand on en a besoin).</p>

<h3>Point d'attention</h3>
<p>Les épreuves de Terminale TI demandent souvent d'écrire des requêtes SQL simples à partir d'un schéma de base de données donné — il faut s'entraîner à lire un schéma relationnel rapidement.</p>
""",
    },
    {
        "id": 'si-terminale-exercices',
        "matiere": "Système d'Information",
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": "Module 3 : Systèmes d'Information et bases de données",
        "titre": "Systèmes d'Information — Exercices (Terminale)",
        "type": 'Exercices',
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Expliquer la différence entre une clé primaire et une clé étrangère.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Écrire la requête SQL permettant d'afficher tous les élèves de la table Eleve dont la classe est "TleTI".</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Une base de données scolaire comprend trois tables : <code>Eleve(id, nom, classe)</code>, <code>Matiere(id, nom_matiere)</code>, et <code>Note(id, eleve_id, matiere_id, valeur)</code>, où eleve_id et matiere_id sont des clés étrangères.</p>
<p><b>Tâche 1 :</b> Justifier pourquoi la table Note est nécessaire plutôt que d'ajouter directement les notes dans la table Eleve.</p>
<p><b>Tâche 2 :</b> Écrire la requête SQL affichant le nom de l'élève et la valeur de sa note pour la matière "Mathématiques" (jointures nécessaires).</p>
<p><b>Tâche 3 :</b> Proposer une mesure pour garantir que la valeur d'une note ne puisse jamais être supérieure à 20.</p>
<p><i>Cette situation mobilise : la compréhension du modèle relationnel, l'écriture de requêtes avec jointures, et la réflexion sur l'intégrité des données.</i></p>
""",
    },
    {
        "id": 'programmation-premiere-cours',
        "matiere": 'Programmation',
        "classe": 'Premiere',
        "series": ['TI'],
        "sequence": 'Algorithmique et structures de base',
        "titre": 'Programmation — Cours (Première)',
        "type": 'Cours',
        "contenu": """
<h3>1. Qu'est-ce qu'un algorithme ?</h3>
<p>Un algorithme est une suite finie et ordonnée d'instructions permettant de résoudre un problème. Avant d'écrire du code, on rédige souvent un algorithme en langage naturel structuré ou en pseudo-code.</p>

<h3>2. Variables et types de données</h3>
<p>Une <b>variable</b> est un espace mémoire nommé qui contient une valeur pouvant changer. Types de base : <b>entier</b> (nombre sans virgule), <b>réel/flottant</b> (nombre à virgule), <b>chaîne de caractères</b> (texte), <b>booléen</b> (Vrai ou Faux).</p>
<p>Exemple en pseudo-code : <code>age ← 17</code> (age est une variable entière valant 17).</p>

<h3>3. Les structures conditionnelles</h3>
<p><code>Si (condition) Alors ... Sinon ... FinSi</code> — permet d'exécuter des instructions différentes selon qu'une condition est vraie ou fausse.</p>
<p>Exemple : <code>Si age >= 18 Alors Afficher("Majeur") Sinon Afficher("Mineur") FinSi</code></p>

<h3>4. Les structures itératives (boucles)</h3>
<p><b>Boucle Pour :</b> répète un nombre connu de fois. <code>Pour i de 1 à 10 Faire ... FinPour</code></p>
<p><b>Boucle Tant que :</b> répète tant qu'une condition reste vraie (nombre de répétitions inconnu à l'avance). <code>Tant que (condition) Faire ... FinTantQue</code></p>

<h3>5. Introduction à un langage de programmation (ex: Python)</h3>
<p>Traduction directe du pseudo-code : <code>age = 17</code><br><code>if age >= 18:<br>&nbsp;&nbsp;&nbsp;&nbsp;print("Majeur")<br>else:<br>&nbsp;&nbsp;&nbsp;&nbsp;print("Mineur")</code></p>
<p>Boucle : <code>for i in range(1, 11):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(i)</code></p>

<h3>Point d'attention</h3>
<p>En Première, l'objectif est de bien maîtriser la logique algorithmique (savoir décomposer un problème en étapes) avant de se concentrer sur la syntaxe exacte d'un langage — cette rigueur logique sera indispensable en Terminale.</p>
""",
    },
    {
        "id": 'programmation-premiere-exercices',
        "matiere": 'Programmation',
        "classe": 'Premiere',
        "series": ['TI'],
        "sequence": 'Algorithmique et structures de base',
        "titre": 'Programmation — Exercices (Première)',
        "type": 'Exercices',
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Écrire l'algorithme (en pseudo-code) qui demande un nombre à l'utilisateur et affiche s'il est pair ou impair.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Écrire l'algorithme qui affiche les nombres de 1 à 20 à l'aide d'une boucle Pour.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Le professeur d'informatique souhaite un petit programme qui calcule automatiquement la moyenne d'un élève à partir de plusieurs notes saisies une par une, et qui indique si l'élève est admis (moyenne ≥ 10) ou non.</p>
<p><b>Tâche 1 :</b> Identifier les variables nécessaires pour ce programme (avec leur type).</p>
<p><b>Tâche 2 :</b> Écrire l'algorithme en pseudo-code permettant de saisir 5 notes (boucle), de calculer leur moyenne, et d'afficher "Admis" ou "Non admis" selon le résultat.</p>
<p><i>Cette situation mobilise : la combinaison d'une boucle et d'une structure conditionnelle pour résoudre un problème concret — compétence centrale du module.</i></p>
""",
    },
    {
        "id": 'programmation-terminale-cours',
        "matiere": 'Programmation',
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": 'Module 1 : Algorithmique et programmation avancée',
        "titre": 'Programmation — Cours (Terminale)',
        "type": 'Cours',
        "contenu": """
<h3>1. Les fonctions (sous-programmes)</h3>
<p>Une fonction est un bloc d'instructions réutilisable, qui peut recevoir des <b>paramètres</b> et renvoyer un <b>résultat</b>. Elle permet de découper un programme complexe en parties plus simples et évite la duplication de code.</p>
<p>Exemple en pseudo-code : <code>Fonction Carre(x) : Retourner x × x FinFonction</code></p>
<p>En Python : <code>def carre(x):<br>&nbsp;&nbsp;&nbsp;&nbsp;return x * x</code></p>

<h3>2. Les tableaux (structures de données)</h3>
<p>Un tableau permet de stocker plusieurs valeurs sous un même nom, accessibles par un indice (position). En pseudo-code : <code>T[0], T[1], T[2]...</code> En Python, un tableau est représenté par une liste : <code>notes = [12, 15, 8, 17]</code>, et <code>notes[0]</code> vaut 12.</p>

<h3>3. Parcours et traitement de tableaux</h3>
<p>Calculer la somme d'un tableau : <code>somme = 0<br>Pour i de 0 à taille(T)-1 Faire<br>&nbsp;&nbsp;&nbsp;&nbsp;somme ← somme + T[i]<br>FinPour</code></p>
<p>Recherche du maximum, tri (par exemple le tri à bulles), recherche d'un élément : ce sont des algorithmes classiques à connaître par cœur en Terminale TI.</p>

<h3>4. Algorithmes de tri (notion de base : tri à bulles)</h3>
<p>Le tri à bulles compare deux éléments consécutifs et les échange s'ils sont dans le mauvais ordre, en répétant l'opération jusqu'à ce que le tableau soit trié. C'est un algorithme simple mais peu efficace pour de grands tableaux (complexité en n²).</p>

<h3>5. Récursivité (notion introductive)</h3>
<p>Une fonction récursive s'appelle elle-même pour résoudre un problème en le décomposant en sous-problèmes plus petits. Exemple classique : la factorielle. <code>Fonction Factorielle(n) :<br>&nbsp;&nbsp;&nbsp;&nbsp;Si n <= 1 Alors Retourner 1<br>&nbsp;&nbsp;&nbsp;&nbsp;Sinon Retourner n × Factorielle(n-1)<br>&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>FinFonction</code> — toute fonction récursive doit avoir un <b>cas d'arrêt</b>, sinon elle boucle indéfiniment.</p>

<h3>Point d'attention</h3>
<p>Les épreuves de Terminale TI demandent souvent d'écrire un algorithme complet avec fonction(s) à partir d'un énoncé concret, et d'en tracer l'exécution pas à pas (trace de variables) — s'entraîner à cet exercice de "traçage" est essentiel.</p>
""",
    },
    {
        "id": 'programmation-terminale-exercices',
        "matiere": 'Programmation',
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": 'Module 1 : Algorithmique et programmation avancée',
        "titre": 'Programmation — Exercices (Terminale)',
        "type": 'Exercices',
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Écrire une fonction en pseudo-code qui reçoit un tableau de notes et renvoie la moyenne.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Tracer l'exécution de Factorielle(4) étape par étape (montrer chaque appel récursif et sa valeur de retour).</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un club sportif scolaire souhaite un programme qui reçoit les temps (en secondes) de tous les coureurs d'une course dans un tableau, et doit afficher le meilleur temps (minimum) ainsi que le classement complet (tableau trié du plus petit au plus grand temps).</p>
<p><b>Tâche 1 :</b> Écrire une fonction qui reçoit un tableau de temps et renvoie le temps minimum.</p>
<p><b>Tâche 2 :</b> Écrire l'algorithme du tri à bulles permettant de trier ce tableau de temps par ordre croissant.</p>
<p><b>Tâche 3 :</b> Expliquer comment on afficherait ensuite le classement (position 1 = meilleur temps, etc.) à partir du tableau trié.</p>
<p><i>Cette situation mobilise : l'écriture de fonctions, la manipulation de tableaux, et l'application d'un algorithme de tri à un cas concret — compétences clés du module.</i></p>
""",
    },
    {
        "id": 'reseau-terminale-corriges',
        "matiere": 'Réseau',
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": 'Module 2 : Réseau, Internet et sécurité',
        "titre": 'Réseaux informatiques — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Le switch relie plusieurs équipements d'un même réseau local (usage : relier les postes d'une salle informatique). Le routeur relie deux réseaux différents (usage : connecter le réseau local à Internet).</p>

<h3>Corrigé — Exercice 2</h3>
<p>Avantages de la topologie en étoile : la panne d'un poste n'affecte pas les autres ; facilité d'ajout de nouveaux postes. Inconvénient : si l'équipement central (switch) tombe en panne, tout le réseau est coupé.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Topologie en étoile recommandée, car elle isole les pannes individuelles et facilite l'ajout futur de postes, ce qui correspond au besoin exprimé par le proviseur.</p>
<p><b>Tâche 2 :</b> Un switch dans chaque salle pour relier les postes locaux ; un routeur pour relier l'ensemble à Internet ; éventuellement un point d'accès Wi-Fi pour la bibliothèque et la salle des professeurs.</p>
<p><b>Tâche 3 :</b> Installation d'un pare-feu au niveau du routeur, qui filtrera le trafic entrant et bloquera les connexions suspectes venant d'Internet.</p>
""",
    },
    {
        "id": 'si-premiere-corriges',
        "matiere": "Système d'Information",
        "classe": 'Premiere',
        "series": ['TI'],
        "sequence": "Introduction aux systèmes d'information",
        "titre": "Systèmes d'Information — Corrigés (Première)",
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Donnée : "245" (numéro d'un livre). Information : "Le livre 245 est actuellement emprunté". Connaissance : "Ce livre est très demandé, il faudrait en acheter un second exemplaire".</p>

<h3>Corrigé — Exercice 2</h3>
<p>Une clé primaire doit être unique car elle sert à identifier précisément un enregistrement parmi tous les autres ; si deux lignes avaient la même clé, il serait impossible de savoir à laquelle on fait référence.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Entités : Livre, Élève (et éventuellement Emprunt comme association porteuse de données).</p>
<p><b>Tâche 2 :</b> Livre : id, titre, auteur. Élève : id, nom, classe.</p>
<p><b>Tâche 3 :</b> Un Élève "emprunte" un ou plusieurs Livres, à une date donnée.</p>
""",
    },
    {
        "id": 'si-terminale-corriges',
        "matiere": "Système d'Information",
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": "Module 3 : Systèmes d'Information et bases de données",
        "titre": "Systèmes d'Information — Corrigés (Terminale)",
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>La clé primaire identifie de façon unique les enregistrements d'une table (ex: id d'un Élève). La clé étrangère est un champ qui fait référence à la clé primaire d'une autre table, pour créer un lien entre elles (ex: eleve_id dans la table Note).</p>

<h3>Corrigé — Exercice 2</h3>
<p><code>SELECT * FROM Eleve WHERE classe = 'TleTI';</code></p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Une table Note séparée évite la redondance : un élève a plusieurs notes dans plusieurs matières, il serait impossible de stocker cela proprement dans une seule ligne de la table Eleve.</p>
<p><b>Tâche 2 :</b> <code>SELECT Eleve.nom, Note.valeur FROM Eleve JOIN Note ON Eleve.id = Note.eleve_id JOIN Matiere ON Matiere.id = Note.matiere_id WHERE Matiere.nom_matiere = 'Mathématiques';</code></p>
<p><b>Tâche 3 :</b> Ajouter une contrainte de validation sur le champ valeur (ex: CHECK (valeur <= 20) en SQL), pour empêcher l'insertion d'une note invalide.</p>
""",
    },
    {
        "id": 'programmation-premiere-corriges',
        "matiere": 'Programmation',
        "classe": 'Premiere',
        "series": ['TI'],
        "sequence": 'Algorithmique et structures de base',
        "titre": 'Programmation — Corrigés (Première)',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p><code>Lire(n)<br>Si (n MOD 2 == 0) Alors Afficher("Pair")<br>Sinon Afficher("Impair")<br>FinSi</code></p>

<h3>Corrigé — Exercice 2</h3>
<p><code>Pour i de 1 à 20 Faire<br>&nbsp;&nbsp;&nbsp;&nbsp;Afficher(i)<br>FinPour</code></p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Variables : note (réel, à saisir 5 fois), somme (réel, initialisée à 0), moyenne (réel).</p>
<p><b>Tâche 2 :</b><br>
<code>somme ← 0<br>
Pour i de 1 à 5 Faire<br>
&nbsp;&nbsp;&nbsp;&nbsp;Lire(note)<br>
&nbsp;&nbsp;&nbsp;&nbsp;somme ← somme + note<br>
FinPour<br>
moyenne ← somme / 5<br>
Si moyenne >= 10 Alors<br>
&nbsp;&nbsp;&nbsp;&nbsp;Afficher("Admis")<br>
Sinon<br>
&nbsp;&nbsp;&nbsp;&nbsp;Afficher("Non admis")<br>
FinSi</code></p>
""",
    },
    {
        "id": 'programmation-terminale-corriges',
        "matiere": 'Programmation',
        "classe": 'Terminale',
        "series": ['TI'],
        "sequence": 'Module 1 : Algorithmique et programmation avancée',
        "titre": 'Programmation — Corrigés (Terminale)',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p><code>Fonction Moyenne(T) :<br>
&nbsp;&nbsp;&nbsp;&nbsp;somme ← 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;Pour i de 0 à taille(T)-1 Faire<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;somme ← somme + T[i]<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinPour<br>
&nbsp;&nbsp;&nbsp;&nbsp;Retourner somme / taille(T)<br>
FinFonction</code></p>

<h3>Corrigé — Exercice 2</h3>
<p>Factorielle(4) = 4 × Factorielle(3) = 4 × (3 × Factorielle(2)) = 4 × (3 × (2 × Factorielle(1))) = 4 × (3 × (2 × 1)) = 4 × 3 × 2 × 1 = 24.</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b><br>
<code>Fonction Minimum(T) :<br>
&nbsp;&nbsp;&nbsp;&nbsp;min ← T[0]<br>
&nbsp;&nbsp;&nbsp;&nbsp;Pour i de 1 à taille(T)-1 Faire<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si T[i] < min Alors min ← T[i] FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinPour<br>
&nbsp;&nbsp;&nbsp;&nbsp;Retourner min<br>
FinFonction</code></p>
<p><b>Tâche 2 :</b> Appliquer le tri à bulles : parcourir le tableau plusieurs fois, comparer chaque paire d'éléments consécutifs, les échanger si le premier est plus grand que le second, jusqu'à ce qu'aucun échange ne soit nécessaire.</p>
<p><b>Tâche 3 :</b> Une fois le tableau trié par ordre croissant, la position 0 correspond au meilleur temps (1er), la position 1 au 2e, etc. — il suffit d'afficher chaque élément avec son rang (indice + 1).</p>
""",
    },
    {
        "id": 'philo-conscience-corriges',
        "matiere": 'Philosophie',
        "classe": 'Terminale',
        "series": ['A', 'C', 'D', 'TI'],
        "sequence": 'Séquence 1',
        "titre": 'La conscience — Corrigés',
        "type": 'Corrigé',
        "contenu": """
<h3>Corrigé indicatif — Tâche 1 (problématique)</h3>
<p>On peut formuler : "Si, selon Descartes, la conscience donne un accès immédiat et certain à soi-même, ne faut-il pas néanmoins le regard et la reconnaissance d'autrui pour véritablement se connaître dans ce que l'on est socialement et moralement ?" Cette problématique met en tension l'introspection solitaire et la connaissance de soi médiatisée par autrui (on pense notamment à Hegel et à la dialectique de la reconnaissance).</p>

<h3>Corrigé indicatif — Tâche 2 (plan)</h3>
<p><b>Partie 1 :</b> La conscience suffit à se connaître soi-même (référence : Descartes, le cogito comme certitude immédiate de sa propre existence et de sa pensée).</p>
<p><b>Partie 2 :</b> Mais la conscience seule est limitée : elle peut être aveugle à certains aspects de soi (référence : Freud et l'inconscient, ou Hegel et la nécessité du regard d'autrui pour accéder à une conscience de soi pleinement reconnue).</p>
<p><i>Un plan de dissertation réussi articule clairement ces deux moments avec une transition logique, plutôt que de simplement juxtaposer les références.</i></p>
""",
    },
]

RESSOURCES.extend([
    {
        "id": "info-cd-systemes-cours",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 1 : Systèmes informatiques",
        "titre": "Environnement numérique et réseaux locaux — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Composants d'un système informatique</h3>
<p>Un système informatique comprend le <b>matériel</b> (unité centrale, processeur, mémoire RAM, disque de stockage, périphériques) et le <b>logiciel</b> : le <b>système d'exploitation</b> (Windows, Linux...) qui gère les ressources de la machine, et les <b>logiciels d'application</b> (traitement de texte, tableur...) utilisés par l'utilisateur final.</p>

<h3>2. Protection d'un environnement de travail</h3>
<p>Protéger son environnement numérique passe par : des <b>mots de passe robustes</b> (mélange de lettres, chiffres, symboles), des <b>sauvegardes régulières</b> des fichiers importants, un <b>antivirus</b> à jour, et la vigilance face aux pièces jointes ou liens suspects (phishing).</p>

<h3>3. Création de contenus numériques (tableur)</h3>
<p>Un tableur organise les données en <b>cellules</b> repérées par une colonne et une ligne (ex: B4). Les formules commencent par "=" : <code>=SOMME(A1:A10)</code> additionne les cellules de A1 à A10. <code>=MOYENNE(B1:B5)</code> calcule une moyenne. Les références peuvent être <b>relatives</b> (changent en recopiant) ou <b>absolues</b> (fixées avec $, ex: $A$1).</p>

<h3>4. Création d'un petit réseau local</h3>
<p>Pour créer un réseau local simple : relier les postes à un switch (topologie en étoile), attribuer une adresse IP à chaque poste (souvent automatiquement via un serveur DHCP), et vérifier la connectivité (commande <code>ping</code> pour tester si un poste répond).</p>

<h3>5. Notion de partage de ressources</h3>
<p>Un réseau local permet le <b>partage de fichiers</b> (dossier accessible à plusieurs postes) et le <b>partage d'imprimante</b> (une seule imprimante utilisable par tous les postes connectés), ce qui optimise les ressources matérielles d'une organisation.</p>

<h3>Point d'attention</h3>
<p>Les épreuves demandent souvent des manipulations pratiques sur tableur (formules, mise en forme) autant que des questions théoriques sur les composants et la sécurité — s'entraîner sur un vrai tableur est indispensable.</p>
""",
    },
    {
        "id": "info-cd-systemes-exercices",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 1 : Systèmes informatiques",
        "titre": "Environnement numérique et réseaux locaux — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Citer trois composants matériels et deux exemples de logiciels d'application.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Écrire la formule tableur permettant de calculer la moyenne des cellules C2 à C10.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Le secrétariat d'un lycée utilise un tableur pour gérer les frais de scolarité de 50 élèves. La colonne A contient les noms, la colonne B le montant déjà payé, et la colonne C le montant total dû (75 000 FCFA pour tous).</p>
<p><b>Tâche 1 :</b> Écrire la formule à placer en D2 pour calculer le montant restant à payer par l'élève de la ligne 2 (colonne D = C - B).</p>
<p><b>Tâche 2 :</b> Écrire la formule permettant de calculer, en bas de la colonne B, le total déjà encaissé par le secrétariat pour tous les élèves (de B2 à B51).</p>
<p><i>Cette situation mobilise : l'écriture de formules de calcul et de sommation dans un contexte de gestion réelle.</i></p>
""",
    },
    {
        "id": "info-cd-systemes-corriges",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 1 : Systèmes informatiques",
        "titre": "Environnement numérique et réseaux locaux — Corrigés",
        "type": "Corrigé",
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Composants matériels : processeur, mémoire RAM, disque dur. Logiciels d'application : traitement de texte (Word), tableur (Excel).</p>

<h3>Corrigé — Exercice 2</h3>
<p><code>=MOYENNE(C2:C10)</code></p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> En D2 : <code>=C2-B2</code></p>
<p><b>Tâche 2 :</b> En bas de la colonne B (par exemple B52) : <code>=SOMME(B2:B51)</code></p>
""",
    },
    {
        "id": "info-cd-bdd-cours",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 2 : Systèmes d'Information et Bases de Données",
        "titre": "Modèle de données (MCD/MLD) — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Le Modèle Conceptuel des Données (MCD)</h3>
<p>Le MCD représente les données d'un système sous forme d'<b>entités</b> (objets à mémoriser, ex: Client) reliées par des <b>associations</b> (liens entre entités, ex: "passe" une Commande). Chaque entité a des <b>attributs</b> (propriétés, ex: nom, adresse).</p>

<h3>2. Les cardinalités</h3>
<p>Une cardinalité précise combien de fois une entité participe à une association, exprimée sous la forme (min,max). Exemple : un Client "passe" (0,n) Commande — un client peut passer 0 ou plusieurs commandes ; une Commande "est passée par" (1,1) Client — une commande est passée par exactement un client.</p>

<h3>3. Du MCD au Modèle Logique des Données (MLD)</h3>
<p>Le MLD traduit le MCD en <b>tables relationnelles</b>. Règle de transformation : chaque entité devient une table, avec ses attributs comme colonnes et un identifiant comme clé primaire. Une association de type "plusieurs-à-plusieurs" (n,n) devient une table à part, contenant les clés primaires des deux entités liées (clés étrangères).</p>

<h3>4. Exemple complet</h3>
<p>MCD : Client (0,n) "passe" (1,1) Commande. MLD : table Client(id_client, nom, adresse) ; table Commande(id_commande, date, id_client) où id_client est une clé étrangère vers Client.</p>

<h3>5. Notions de base de SQL</h3>
<p><code>CREATE TABLE Client (id_client INTEGER PRIMARY KEY, nom TEXT, adresse TEXT);</code><br>
<code>SELECT nom FROM Client WHERE adresse LIKE '%Yaoundé%';</code> sélectionne les clients dont l'adresse contient "Yaoundé".</p>

<h3>Point d'attention</h3>
<p>Il est essentiel de savoir passer directement d'un énoncé en français à un MCD (identifier entités/associations/cardinalités), puis du MCD au MLD — c'est le cœur des épreuves sur ce module.</p>
""",
    },
    {
        "id": "info-cd-bdd-exercices",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 2 : Systèmes d'Information et Bases de Données",
        "titre": "Modèle de données (MCD/MLD) — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Définir ce qu'est une cardinalité dans un MCD, avec un exemple.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Expliquer comment une association plusieurs-à-plusieurs (n,n) se traduit au niveau du MLD.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Une pharmacie souhaite informatiser la gestion de ses ventes. Elle vend des Médicaments (référence, nom, prix), à des Clients (nom, téléphone), et chaque vente concerne un ou plusieurs médicaments, à une date donnée.</p>
<p><b>Tâche 1 :</b> Proposer les entités nécessaires pour ce système (au moins trois, incluant une entité "Vente").</p>
<p><b>Tâche 2 :</b> Indiquer les cardinalités entre Client et Vente, puis entre Vente et Médicament.</p>
<p><b>Tâche 3 :</b> Traduire ce MCD en tables du MLD, avec leurs clés primaires et étrangères.</p>
<p><i>Cette situation mobilise : la modélisation complète d'un système d'information, du MCD au MLD, à partir d'un contexte métier réel.</i></p>
""",
    },
    {
        "id": "info-cd-bdd-corriges",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 2 : Systèmes d'Information et Bases de Données",
        "titre": "Modèle de données (MCD/MLD) — Corrigés",
        "type": "Corrigé",
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p>Une cardinalité précise le nombre de fois qu'une occurrence d'une entité participe à une association. Exemple : un Élève "suit" (0,n) Cours — un élève peut suivre 0 ou plusieurs cours.</p>

<h3>Corrigé — Exercice 2</h3>
<p>Une association (n,n) devient une table à part entière, contenant en clés étrangères les identifiants des deux entités reliées (plus, éventuellement, des attributs propres à l'association elle-même, comme une date).</p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> Entités : Client, Vente, Médicament.</p>
<p><b>Tâche 2 :</b> Client (1,1) — (0,n) Vente : un client peut faire plusieurs ventes, une vente concerne un seul client. Vente (1,n) — (0,n) Médicament : une vente concerne un ou plusieurs médicaments, un médicament peut apparaître dans plusieurs ventes (association n,n).</p>
<p><b>Tâche 3 :</b> Client(id_client, nom, téléphone) ; Médicament(id_médicament, nom, prix) ; Vente(id_vente, date, id_client) ; LigneVente(id_vente, id_médicament, quantité) — cette dernière table gère l'association n,n entre Vente et Médicament.</p>
""",
    },
    {
        "id": "info-cd-algo-cours",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 3 : Algorithmique et programmation en C",
        "titre": "Algorithmique et programmation en langage C — Cours",
        "type": "Cours",
        "contenu": """
<h3>1. Structure générale d'un programme en C</h3>
<p><code>#include &lt;stdio.h&gt;<br>int main() {<br>&nbsp;&nbsp;&nbsp;&nbsp;// instructions<br>&nbsp;&nbsp;&nbsp;&nbsp;return 0;<br>}</code> — tout programme C commence par des inclusions de bibliothèques et une fonction main() qui est le point d'entrée du programme.</p>

<h3>2. Déclaration de variables et types en C</h3>
<p>En C, il faut déclarer le type avant d'utiliser une variable : <code>int age = 17;</code> (entier), <code>float moyenne = 12.5;</code> (réel), <code>char lettre = 'A';</code> (caractère).</p>

<h3>3. Structures conditionnelles et itératives en C</h3>
<p><code>if (age >= 18) {<br>&nbsp;&nbsp;&nbsp;&nbsp;printf("Majeur");<br>} else {<br>&nbsp;&nbsp;&nbsp;&nbsp;printf("Mineur");<br>}</code></p>
<p>Boucle for : <code>for (int i=1; i&lt;=10; i++) {<br>&nbsp;&nbsp;&nbsp;&nbsp;printf("%d\\n", i);<br>}</code></p>
<p>Boucle while : <code>while (condition) { ... }</code> — répète tant que la condition est vraie.</p>

<h3>4. Les tableaux en C</h3>
<p><code>int notes[5] = {12, 15, 8, 17, 10};</code> déclare un tableau de 5 entiers. On accède à un élément par son indice : <code>notes[0]</code> vaut 12. Les indices commencent toujours à 0 en C.</p>

<h3>5. Les fonctions en C</h3>
<p><code>int carre(int x) {<br>&nbsp;&nbsp;&nbsp;&nbsp;return x * x;<br>}</code> — une fonction en C précise son type de retour (ici int), son nom, ses paramètres entre parenthèses, et un bloc d'instructions se terminant par un <code>return</code>.</p>

<h3>Point d'attention</h3>
<p>Contrairement au pseudo-code, le C exige une syntaxe stricte (point-virgule à la fin de chaque instruction, accolades pour délimiter les blocs, déclaration explicite des types) — la rigueur syntaxique est très souvent évaluée en plus de la logique de l'algorithme.</p>
""",
    },
    {
        "id": "info-cd-algo-exercices",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 3 : Algorithmique et programmation en C",
        "titre": "Algorithmique et programmation en langage C — Exercices",
        "type": "Exercices",
        "contenu": """
<h3>Exercice 1 — Connaissances</h3>
<p>Écrire en langage C le programme qui demande un nombre et affiche s'il est positif, négatif ou nul.</p>

<h3>Exercice 2 — Connaissances</h3>
<p>Écrire en langage C une boucle qui affiche les nombres pairs de 2 à 20.</p>

<h3>Situation-problème (évaluation des ressources)</h3>
<p><b>Contexte :</b> Un enseignant veut un petit programme en C qui reçoit un tableau de 6 notes d'un élève, calcule leur moyenne, et affiche "Admis" si la moyenne est supérieure ou égale à 10, sinon "Ajourné".</p>
<p><b>Tâche 1 :</b> Déclarer le tableau de notes et les variables nécessaires en C.</p>
<p><b>Tâche 2 :</b> Écrire la boucle en C qui parcourt le tableau pour calculer la somme des notes.</p>
<p><b>Tâche 3 :</b> Écrire le test conditionnel en C affichant "Admis" ou "Ajourné" selon la moyenne calculée.</p>
<p><i>Cette situation mobilise : la déclaration de tableaux, l'écriture de boucles de parcours, et de structures conditionnelles en syntaxe C correcte.</i></p>
""",
    },
    {
        "id": "info-cd-algo-corriges",
        "matiere": "Informatique",
        "classe": "Terminale",
        "series": ["C", "D"],
        "sequence": "Module 3 : Algorithmique et programmation en C",
        "titre": "Algorithmique et programmation en langage C — Corrigés",
        "type": "Corrigé",
        "contenu": """
<h3>Corrigé — Exercice 1</h3>
<p><code>#include &lt;stdio.h&gt;<br>
int main() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;int n;<br>
&nbsp;&nbsp;&nbsp;&nbsp;printf("Entrez un nombre : ");<br>
&nbsp;&nbsp;&nbsp;&nbsp;scanf("%d", &amp;n);<br>
&nbsp;&nbsp;&nbsp;&nbsp;if (n &gt; 0) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;printf("Positif");<br>
&nbsp;&nbsp;&nbsp;&nbsp;} else if (n &lt; 0) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;printf("Négatif");<br>
&nbsp;&nbsp;&nbsp;&nbsp;} else {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;printf("Nul");<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;return 0;<br>
}</code></p>

<h3>Corrigé — Exercice 2</h3>
<p><code>for (int i=2; i&lt;=20; i=i+2) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;printf("%d\\n", i);<br>
}</code></p>

<h3>Corrigé — Situation-problème</h3>
<p><b>Tâche 1 :</b> <code>float notes[6]; float somme = 0, moyenne;</code></p>
<p><b>Tâche 2 :</b> <code>for (int i=0; i&lt;6; i++) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;scanf("%f", &amp;notes[i]);<br>
&nbsp;&nbsp;&nbsp;&nbsp;somme = somme + notes[i];<br>
}</code></p>
<p><b>Tâche 3 :</b> <code>moyenne = somme / 6;<br>
if (moyenne &gt;= 10) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;printf("Admis");<br>
} else {<br>
&nbsp;&nbsp;&nbsp;&nbsp;printf("Ajourné");<br>
}</code></p>
""",
    },
])

MATIERES_RESSOURCES = sorted(set(r["matiere"] for r in RESSOURCES))
SERIES_RESSOURCES = ["A", "C", "D", "TI"]
CLASSES_RESSOURCES = ["Premiere", "Terminale"]
TYPES_RESSOURCES = ["Cours", "Exercices", "Corrigé"]
