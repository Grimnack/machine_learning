import numpy as np
from matplotlib import pyplot as plt


taille_h = np.loadtxt("taille_h.txt")
taille_f = np.loadtxt("taille_f.txt")
classe_h = [1]*len(taille_h)
classe_f = [0]*len(taille_f)
nbins = int(max(taille_h)) + 1

X1 = np.append(taille_h,taille_f)
X2 = np.append(classe_h,classe_f)

taille_min = int(min(X1))
taille_max = int(max(X1)) + 1


plt.hist(taille_h,bins=nbins,color="blue")
plt.hist(taille_f,bins=nbins,color="pink")

# LES Variables X1 ET X2 ne sont pas indépendantes car on observe bien
# que les hommes sont en moyenne plus grands que les femmes

plt.hist(X1,bins=nbins,color='green')

def loi_marginale(lesTailles) :
    loi_marginale = [0]*(taille_max - taille_min)
