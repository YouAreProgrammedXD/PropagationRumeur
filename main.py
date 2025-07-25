
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    n,p,mode,mode2=demander_parametres()
    infecte_pol = propagationrumeurs(n,mode2)
    print(infecte_pol)
    moy=moyenne(infecte_pol)
    if (mode==2):
        print("\n")
        total=0
        for i in range(len(infecte_pol)):
            print("Pour ",i+1,"abonnée(s) initial le nombre d'infecte moyen est:",moy[i](p))
            total=total+math.comb(n-1,i+1)*moy[i]*len(infecte_pol[i])
        total=total/(math.pow(math.pow(2,n-1)-1,n))
        print("\n",total(p))
    else:
        if (mode2==0):
            total=0
            for i in range(len(infecte_pol)):
                total=total+math.comb(n-1,i+1)*moy[i]*len(infecte_pol[i])
            total=total/(math.pow(math.pow(2,n-1)-1,n))
            print("\nEn moyenne, pour un réseau de taille ",n," le nombre d'infecte suit une fonction de p qui est: ",total,"\n")
            p_values = np.linspace(0, 1, 100)
            y_values = total(p_values)

            plt.plot(p_values, y_values)
            plt.axhline(y=n, color='red', linestyle='--', label=f"y = {n}")
            plt.xlabel("probabilité p")
            plt.ylabel("nombre de personnes ayant entendu la rumeur")
            plt.title("Propagation de la rumeur en fonction de p")
            plt.grid(True)
            plt.show()
        else:
            print("\nEn moyenne pour un réseau de taille ",n," et avec ",mode2,"abonné initiaux, le nombre d'infecté suit une fonction de p qui est: ",moy[mode2-1],"\n")
            p_values = np.linspace(0, 1, 100)
            y_values = moy[mode2-1](p_values)

            plt.plot(p_values, y_values)
            plt.axhline(y=n, color='red', linestyle='--', label=f"y = {n}")
            plt.xlabel("probabilité p")
            plt.ylabel("nombre de personnes ayant entendu la rumeur")
            plt.title(f"Propagation de la rumeur en fonction de p avec {mode2} infecte initial")
            plt.grid(True)
            plt.show()
            
        


def demander_parametres():
    while True:
        try:
            n = int(input("Nombre d'individus (entier > 0,recommendé <=5) : "))
            if n <= 0:
                print("Erreur : n doit être > 0.\n\n")
                continue
            mode = int(input("Mode 1/2 (1:courbe selon p, 2:p donné) : "))
            if not (mode==1 or mode==2):
                print("Erreur : mode doit être 1 ou 2.\n\n")
                continue
            if mode==2:
                mode2=0
                p = float(input("Probabilité de propagation (entre 0 et 1) : "))
                if not (0 <= p <= 1):
                    print("Erreur : p doit être entre 0 et 1.\n\n")
                    continue
            else:
                p=0
                limite=n-1
                mode2 = int(input(f"Nombre d'infecté au depart (0: tout les cas; pas au dessus de {limite}) : "))
                if (mode2<0 or mode2>n-1):
                    print("Erreur : le nombre d'infecte initial est un entier entre 0 et",n-1,"\n\n")
                    continue
            return n, p, mode, mode2
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier pour n et un float pour p.")



def propagation(reseau, infectes=None, en_cours=None):
    if infectes is None:
        infectes = set([0])      # Individu 0 lance la rumeur
    if en_cours is None:
        en_cours = [0]           # Ceux qui doivent encore décider

    if not en_cours:
        return np.poly1d([len(infectes)])     # Cas terminal : plus personne ne peut propager

    courant = en_cours.pop()
    
    abonnés = [reseau[courant][i] for i in range(len(reseau[courant])) if reseau[courant][i] not in infectes]

    if not abonnés:
        return propagation(reseau, infectes, en_cours[:])

    if (courant!=0):
        # Cas 1 : courant propage
        nouveaux1 = infectes.union(abonnés)
        en_cours1 = en_cours + abonnés
        e1 = propagation(reseau, nouveaux1, en_cours1)

        # Cas 2 : courant ne propage pas
        e2 = propagation(reseau, infectes, en_cours[:])
        p1=np.poly1d([1,0])
        p2=np.poly1d([-1,1])
        return p1 * e1 + p2 * e2
    else:
        nouveaux1 = infectes.union(abonnés)
        en_cours1 = en_cours + abonnés
        e1 = propagation(reseau, nouveaux1, en_cours1)
        return e1 




#une personne a au moins une autre qui la suis; 
# mode:0 l'individus 0 peut avoir toute les combinaison possible d'abonné; sinon il a exactement m abonné
# (si m=1, que l'abonné soit l'individus 1 ou 2 ou 3 etc ne change rien donc on teste juste pour 1)
def propagationrumeurs(n,m):
    reseau = np.empty(n, dtype=object)
    reseau[0]=[1]
    for i in range(1,n):
        reseau[i]=[0]
    if (m==0):
        reseau[0]=creer(m,0)
        infecte=[[] for i in range(n-1)]
    else:
        infecte=[[]]
    k=n-1
    retour=False
    classe=1
    while (k!=-1):
        infecte[classe-1].append(propagation(reseau))
        while (complet(reseau[k],n-1)):
            if (k==0):
                reseau[k]=[1]
            else:
                reseau[k]=[0]
            k=k-1
            retour=True
        if (k!=-1): 
            if (k==0 and m!=0):
                k=-1
            elif (k==0 or besoinajout(reseau[k],k,n)):
                reseau[k]=creer(len(reseau[k])+1,k)
                if k==0:
                    classe=classe+1
            else:
                reseau[k]=increment(reseau[k],k,n)
            if (k<n-1 and k!=-1):
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