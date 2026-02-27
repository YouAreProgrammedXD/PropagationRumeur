🧪 Contexte

Projet d’étude sur la propagation d’une rumeur dans un réseau social de taille N.

L’objectif est d’analyser, selon différentes approches (déterministe et probabiliste), le nombre moyen d’individus atteints en fonction :

- de la structure du réseau

- de la probabilité de transmission p

- des propriétés statistiques des abonnements

⚙️ Environnement

Python : 3.13.5

Analyse statistique : R (.Rmd)

Simulation : Monte Carlo

📂 Structure du projet
.
├── main.py  
├── MonteCarlo.py  
├── loi abonnee.Rmd  
└── README.md  

🧮 1️⃣ Approche déterministe — main.py  

On adopte une approche exhaustive :

Générer tous les réseaux possibles respectant certaines contraintes,
puis calculer en moyenne combien d’individus entendent la rumeur.

On fait des hypothèses du modèle

Chaque individu possède au moins 1 abonné. Un individu qui entend la rumeur la transmet à tous ses abonnés avec une probabilité p. L’individu initial (individu 0) transmet avec une probabilité 1

Chaque individu décide une seule fois de transmettre ou non

📊 Complexité

Le nombre total de réseaux possibles est extrêmement élevé :

$$
(2^{n-1} - 1)^n
$$

Des optimisations sont introduites :

- Réduction des cas symétriques

- Suppression des configurations équivalentes

- Exploitation du fait que les abonnés de l’individu 0 sont automatiquement infectés

La complexité reste néanmoins explosive.

Estimation large :

$O(n \cdot 2^{n^2})$.

👉 En pratique, le programme devient rapidement inutilisable pour des valeurs modérées de n.

✅ Avantage

- Permet de visualiser précisément l’effet de p sur la propagation

- Donne une référence théorique exhaustive

❌ Inconvénients

- Complexité computationnelle prohibitive

- Hypothèse irréaliste : tous les réseaux ont la même probabilité d’exister

- Ne tient pas compte des lois empiriques de distribution des abonnés

📊 2️⃣ Étude statistique — loi abonnee.Rmd

Objectif :

Étudier des datasets issus de réseaux sociaux réels afin de déterminer la loi statistique décrivant le nombre d’abonnés.

Cette analyse permet de :

- Identifier une distribution réaliste (ex : loi de puissance)

- Améliorer le réalisme du modèle

- Comparer modèle théorique et données empiriques

🎲 3️⃣ Approche Monte Carlo — MonteCarlo.py

Face à l’explosion combinatoire de l’approche déterministe, on adopte une méthode probabiliste :

On Génère aléatoirement des réseaux et on simule la propagation puis on Répète l’expérience un grand nombre de fois et on Estime l’espérance du nombre d’individus atteints

Avantages

- Complexité drastiquement réduite

- Permet de traiter des réseaux de grande taille

