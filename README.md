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
🎯 Principe

On adopte une approche exhaustive :

Générer tous les réseaux possibles respectant certaines contraintes,
puis calculer en moyenne combien d’individus entendent la rumeur.

📌 Hypothèses du modèle

Chaque individu possède au moins 1 abonné

Un individu qui entend la rumeur la transmet à tous ses abonnés avec une probabilité p

L’individu initial (individu 0) transmet avec une probabilité 1

Chaque individu décide une seule fois de transmettre ou non

📊 Complexité

Le nombre total de réseaux possibles est extrêmement élevé :

(2n−1−1)n
(2
n−1
−1)
n

Des optimisations sont introduites :

- Réduction des cas symétriques

- Suppression des configurations équivalentes

- Exploitation du fait que les abonnés de l’individu 0 sont automatiquement infectés

La complexité reste néanmoins explosive.

Estimation large :

O(n⋅2n2)
O(n⋅2
n
2
)

👉 En pratique, le programme devient rapidement inutilisable pour des valeurs modérées de n.

✅ Avantage

Permet de visualiser précisément l’effet de p sur la propagation

Donne une référence théorique exhaustive

❌ Inconvénients

Complexité computationnelle prohibitive

Hypothèse irréaliste : tous les réseaux ont la même probabilité d’exister

Ne tient pas compte des lois empiriques de distribution des abonnés

📊 2️⃣ Étude statistique — loi abonnee.Rmd

Objectif :

Étudier des datasets issus de réseaux sociaux réels afin de déterminer la loi statistique décrivant le nombre d’abonnés.

Cette analyse permet de :

Identifier une distribution réaliste (ex : loi de puissance)

Améliorer le réalisme du modèle

Comparer modèle théorique et données empiriques

🎲 3️⃣ Approche Monte Carlo — MonteCarlo.py

Face à l’explosion combinatoire de l’approche déterministe, on adopte une méthode probabiliste :

Principe

Générer aléatoirement des réseaux

Simuler la propagation

Répéter l’expérience un grand nombre de fois

Estimer l’espérance du nombre d’individus atteints

Avantages

Complexité drastiquement réduite

Permet de traiter des réseaux de grande taille

Approche plus réaliste

📈 Objectif scientifique

Comparer :

Approche exhaustive (déterministe)

Approche probabiliste (Monte Carlo)

Distribution réelle des abonnements

Et analyser l’influence de p sur :

Le seuil critique de propagation

La taille moyenne de la cascade

L’émergence éventuelle d’un phénomène type percolation

🚀 Améliorations possibles

Introduire une distribution réaliste des degrés (loi de puissance)

Ajouter des graphes orientés pondérés

Étudier les seuils critiques analytiquement

Paralléliser les simulations Monte Carlo

Ajouter visualisation interactive

📌 Conclusion

Ce projet met en évidence :

Les limites d’une approche exhaustive face à l’explosion combinatoire

L’intérêt des méthodes probabilistes pour l’étude des phénomènes de diffusion

L’importance d’intégrer des distributions réalistes issues de données empiriques

Si tu veux, je peux maintenant te faire :

🔬 Une version plus académique (rapport de recherche)

💼 Une version optimisée pour portfolio/école d’ingénieur

📈 Une version orientée data science / IA

🧠 Une version avec mise en forme mathématique encore plus propre