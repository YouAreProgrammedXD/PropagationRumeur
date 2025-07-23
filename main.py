
import numpy as np
import matplotlib.pyplot as plt

def main(n,p):
    nbinfecte = propagationrumeurs(n,p) #infecté par tour/incrément
    plt.plot(nbinfecte)
    plt.xlabel("tour/incrément")
    plt.ylabel("nombre de personnes ayant entendu la rumeur")
    plt.show()


#infecte.append(propagation(reseau,p,[reseau[0]],[[1]],[1]))

#nbinfecte->nombre d'infecté par tour/increment; infecte-> numéro infecté actuellement
def propagation(reseau,p,propagateurs,nbinfecte,infecte):
    return(1)


#une personne a au moins une autre qui la suis
def propagationrumeurs(n,p):
    reseau = np.empty(n, dtype=object)
    reseau[0]=[1]
    for i in range(1,n):
        reseau[i]=[0]
    infecte=[]
    k=0
    retour=False
    while (k!=-1):
        infecte.append(propagation(reseau,p,[reseau[0]],[[1]],[1]))
        while (complet(reseau[k],n-1)):
            if (k==0):
                reseau[k]=[1]
            else:
                reseau[k]=[0]
            k=k-1       
        if (k!=-1): 
            if (besoinajout(reseau[k],k,n)):
                reseau[k]=creer(len(reseau[k])+1,k)
            else:
                reseau[k]=increment(reseau[k],k,n)
            if (k<n-1):
                k=k+1
    return(moyenne(infecte))

def moyenne(liste):
    L=len(liste)
    t=0
    for i in range(L):
       t=t+liste[i]
    t=t/L 
    return(t)


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




main(100,0.3)