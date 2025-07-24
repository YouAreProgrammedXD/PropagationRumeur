
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    n,p,mode=demander_parametres()
    infecte = propagationrumeurs(n,p) #infecté par tour/incrément
    moy=moyenne(infecte)
    print("\n")
    total=0
    for i in range(len(infecte)):
        print("Pour ",i+1,"abonnée(s) le nombre d'infecte moyen est:",moy[i])
        total=total+math.comb(n-1,i+1)*moy[i]*len(infecte[i])
    total=total/(math.pow(math.pow(2,n-1)-1,n))
    print("\n",total)
    
    #plt.plot(nbinfecte)
    #plt.xlabel("tour/incrément")
    #plt.ylabel("nombre de personnes ayant entendu la rumeur")
    #plt.show()


def demander_parametres():
    while True:
        try:
            n = int(input("Nombre d'individus (entier > 0,recommendé <=5) : "))
            if n <= 0:
                print("Erreur : n doit être > 0.\n\n")
                continue
            mode = int(input("Mode 1/2 (1:courbe selon p, 2:p donné)"))
            if not (mode==1 or mode==2):
                print("Erreur : mode doit être 1 ou 2.\n\n")
                continue
            if mode==1:
                p = float(input("Probabilité de propagation (entre 0 et 1) : "))
                if not (0 <= p <= 1):
                    print("Erreur : p doit être entre 0 et 1.\n\n")
                    continue
            else:
                p=0
            return n, p, mode
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier pour n et un float pour p.")



def propagation(reseau, p, infectes=None, en_cours=None):
    if infectes is None:
        infectes = set([0])      # Individu 0 lance la rumeur
    if en_cours is None:
        en_cours = [0]           # Ceux qui doivent encore décider

    if not en_cours:
        return len(infectes)     # Cas terminal : plus personne ne peut propager

    courant = en_cours.pop()
    abonnés = [reseau[courant][i] for i in range(len(reseau[courant])) if reseau[courant][i] not in infectes]

    if not abonnés:
        return propagation(reseau, p, infectes, en_cours[:])

    if (courant!=0):
        # Cas 1 : courant propage
        nouveaux1 = infectes.union(abonnés)
        en_cours1 = en_cours + abonnés
        e1 = propagation(reseau, p, nouveaux1, en_cours1)

        # Cas 2 : courant ne propage pas
        e2 = propagation(reseau, p, infectes, en_cours[:])
    else:
        e2=0
        nouveaux1 = infectes.union(abonnés)
        en_cours1 = en_cours + abonnés
        e1 = propagation(reseau, p, nouveaux1, en_cours1)*1/p
    return p * e1 + (1 - p) * e2




#une personne a au moins une autre qui la suis
def propagationrumeurs(n,p):
    reseau = np.empty(n, dtype=object)
    reseau[0]=[1]
    for i in range(1,n):
        reseau[i]=[0]
    infecte=[[] for i in range(n-1)]
    k=n-1
    retour=False
    classe=1
    while (k!=-1):
        infecte[classe-1].append(propagation(reseau,p))
        while (complet(reseau[k],n-1)):
            if (k==0):
                reseau[k]=[1]
            else:
                reseau[k]=[0]
            k=k-1
            retour=True
        if (k!=-1): 
            if (besoinajout(reseau[k],k,n) or k==0):
                reseau[k]=creer(len(reseau[k])+1,k)
                if k==0:
                    classe=classe+1
            else:
                reseau[k]=increment(reseau[k],k,n)
            if (k<n-1):
                k=k+1
        if retour:
            retour=False
            if (k!=-1):
                k=n-1    
    return(infecte)

def moyenne(liste):
    retour=[]
    for i in range(len(liste)):
        L=len(liste[i])
        t=0
        for r in range(L):
            t=t+liste[i][r]
        t=t/L 
        retour.append(t)
    return(retour)


#si on ne peut rien incrémenter <=> les abonnées sont bloquer sur la fin de la bande disponible [0;n-1]/k
def besoinajout(liste,k,n):
    if ((liste[0]==n-len(liste) and k<liste[0]) or (liste[0]==n-len(liste)-1 and k>liste[0])):
        return(True)
    else:
        return(False)

#créer une nouvelle liste d'abonnée de len=taille+1
def creer(taille,k):
    if (k>=taille):
        return([i for i in range(0,taille)])
    else:
        liste=[i for i in range(0,taille+1)]
        liste.remove(k)
        return(liste)

#on incrémente le premier numéro d'abonnée possible
def increment(liste,k,n):
    i=1
    while (liste[-i]==n-i or (liste[-i]+1==k and (k==n-1 or (i!=1 and liste[-i+1]==liste[-i]+2)))):
        i=i+1
    if (liste[-i]+1==k):
        liste[-i]=liste[-i]+2
    else:
        liste[-i]=liste[-i]+1
    return(liste)


#si la liste d'abonné comprend tout les individus possible
def complet(liste,taille):
    if (len(liste)!=taille):
        return(False)
    else:
        return(True)




main()