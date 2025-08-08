Quand tu clones un dépôt sur un autre PC :
Tu fais python -m venv venv
Puis pip install -r requirements.txt

Pour ajouter au repertoire:
git status #montre les fichiers avec modification
git add .  #ajoute tout les changements au commit
git commit -m "Ta description ici" 
git push origin main

------------------INTRODUCTION---------------------------

Etude de la propagation d'une rumeur dans un réseau social de taille n.


------------------main.py---------------------------

On approche le problème de façon déterministe, on génère tout les réseaux possible et on regarde en moyenne combien de personnes entendent la rumeur.

On se met des règles/restrictions:
- Un individus a au moins 1 abonné.
- Un individu qui entend la rumeur a une proba p de transmettre la rumeur à tout ses abonées
- Le(s) individus qui transmettent la rumeur initialement ont une proba=1 de le faire
- Un individus choisit de transmettre (ou non) la rumeur une seule fois 

COMPLEXITE:
Cette chose est une monstruosité de complexité: il y a (2^(n-1)-1)^n réseau possible mais des optimisations sont possible:
- Si l'individu 0 (celui qui propage la rumeur) a 2 abonnés, que ce soit les combinaisons (1,2) ou (1,3) ne changent rien donc on doit générer (n-1)*(2^(n-1)-1)^(n-1) réseaux
- Les abonnés de 0 sont forcément infecté donc on peut les ignorer par la suite. Si 0 a comme abonné (1) alors les combinaisons (4), (0,4), (1,4) et (0,1,4) ne changent rien. On génère alors 
somme de c allant de 1 à (n-1) de ((2^(n-c-1)-1)^c)*(2^(n-c-2)-1)^(n-1-c)   (je crois) réseaux. (on doit multiplier cette complexité par n)

Pour chacun de ces réseaux il faut calculer la moyenne d'individus qui entendent la rumeur ce qui est en O(n*2^(n^2))

AVANTAGE:
- on peut graphiquement voir l'effet de p sur la propagation

INCONVENIENT:
- tout les réseaux ont la meme proba d'exister (pour n=15, avoir 10 abonné est plus rare qu'en avoir 2 et avoir 10 abonnement est plus rare qu'en avoir 2 mais ce n'est pas pris en compte)
- trop grosse complexité, le programme est en pratique inutilisable
