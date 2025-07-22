
import numpy as np
import matplotlib.pyplot as plt

def main(n,p):
    reseau = np.ones((n, 1), dtype=list)
    nbinfecte = propagationrumeurs(n,p) #infecté par tour/incrément
    plt.plot(nbinfecte)
    plt.xlabel("tour/incrément")
    plt.ylabel("nombre de personnes ayant entendu la rumeur")
    plt.show()




#nbinfecte->nombre d'infecté par tour/increment; infecte-> numéro infecté actuellement
def propagation(reseau,p,propagateurs,nbinfecte,infecte):
    if (propagateurs==[]):
        return(nbinfecte)
    else:
        print("XD")
    return([1])

def propagationrumeurs(n,p):
    reseau = np.ones((n, 1), dtype=list)
    nbinfecte=[[1]]
    n=len(reseau)
    k=n-1
    while (k!=-1):
        if (complet(reseau[k],k,n-1)):
            reseau[k]=[]
            k=k-1
        else:
            if (reseau[k]==[]):
                if (k==0):
                    reseau[k].append(1)
                else:
                    reseau[k].append(0)
            else:
                if (besoinajout(reseau[k],k,n)):
                    reseau[k]=creer(len(reseau[k])+1,k)
                else:
                    reseau[k]=increment(reseau[k],k,n)
            k=k+1
            nbinfecte.append(propagation(reseau,p,[reseau[0]],[[1]],[1]))
    return(moyenne(nbinfecte))

def moyenne(liste):
    taille=len(liste)
    total=[1]
    i=0
    while (total[-1]!=0):
        t=0
        for l in range(0,taille):
            if (i<len(liste[l])):
                t=t+liste[l][i]
        total.append(t/taille)
    del total[0]
    del total[len(total)-1]
    return(total)



def besoinajout(liste,k,n):
    if ((liste[-len(liste)]==n-len(liste) and k<n-len(liste)) or (liste[-len(liste)]==n-len(liste)-1 and k>=n-len(liste))):
        return(True)
    else:
        return(False)


def creer(taille,k):
    if (k>=taille):
        return([i for i in range(0,taille)])
    else:
        liste=[i for i in range(0,taille+1)]
        liste.remove(k)
        return(liste)

def increment(liste,k,n):
    i=1
    while (liste[-i]==n-i or n-i==k):
        i=i+1
    liste[-i]=liste[-i]+1
    return(liste)

def complet(liste,k,taille):
    if (len(liste)!=taille):
        return(False)
    else:
        return(True)




main(1000,0.3)