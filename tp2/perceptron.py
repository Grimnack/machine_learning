import numpy as np
import random as r
from matplotlib import pyplot as plt

def generePoint() :
    x1 = r.random()
    x2 = r.random()
    return [x1,x2]
    
def tireNPoints(n) :
    lesPoints = []
    for i in range(n) :
        lesPoints.append(generePoint())
    return lesPoints
    
def attribuerClasse(listPoints) :
    lesClasses = []
    for liste in listPoints :
        x1 = liste[0]
        x2 = liste[1]
        calcule = -0.5*x1 + 0.75
        if calcule <= x2 :
            lesClasses.append(1)
            #plt.plot(x1,x2,"bo")
        else :
            lesClasses.append(-1)
            #plt.plot(x1,x2,"ro")
    return lesClasses
       


def ptrain(Xlearn, ylearn,tetaArgs) :
    allGoods = False
    teta = tetaArgs
    while(not(allGoods)) :
        allGoods = True
        nbError = 0
        for i in range(len(Xlearn)) :
            x = Xlearn[i]
            predict = np.sign(np.dot(np.transpose(teta),x))
            if not(predict == ylearn[i] ) :
                allGoods = False
                nbError += 1
                teta = teta + np.dot(ylearn[i],x)
        #print("learning ",1-nbError/len(Xlearn))
    return teta        


def ptest(x,teta) :
    '''
    Prend un exemple x et un teta et fournit une prediction selon fteta(x)
    '''
    return (-(teta[0]*x+teta[2])/teta[1])

def traceDroite(X,teta) :
    x1s = []
    x2s = []
    for ligne in X :
        x1s.append(ligne[0])
        x2s.append(ptest(ligne[0],teta))
    return (x1s,x2s)
    

def datagen(nbPoints):
    '''
    Tire n points et retourne :
    X_train
    X_test
    c_train
    c_test
    avec 10% de train et 90% de test
    '''
    X = tireNPoints(nbPoints)
    for vec in X :
        vec.append(1)
    c_total = attribuerClasse(X)
    separateur = int(nbPoints/10)
    X_train  = X[:separateur]
    X_test = X[separateur:]
    c_train = c_total[:separateur]
    c_test = c_total[separateur:]
    return (X_train,X_test,c_train,c_test)
    
def get_test_err(nbPoints) :
    '''
    appelle datagen et observe l'erreur dans la base test.
    '''
    (X_train,X_test,c_train,c_test) = datagen(nbPoints)
    teta = np.random.random(size=3)
    teta = ptrain(X_train,c_train,teta)
    # On a appris on va maintenant compter les erreurs sur la base de test
    nbErr = 0
    for i in range(len(X_test)) :
        x = X_test[i]
        c_pred = np.sign(np.dot(np.transpose(teta),x))
        if not(c_pred == c_test[i] ) :
            nbErr += 1
    return nbErr/len(X_test)
    
def itere_get_test_err(nbPoints,nbFois) :
    lesTauxDErreur = []    
    for i in range(nbFois) :
        print(i)
        lesTauxDErreur.append(get_test_err(nbPoints)*100)
    return lesTauxDErreur

lesTauxDErreur = itere_get_test_err(445,1000)
bins_perc = np.arange(0,20,0.5)
hist_perc , bins_perc = np.histogram(lesTauxDErreur,bins=bins_perc)    
plt.bar(bins_perc[:-1],hist_perc,0.5)

    
print("esperance erreur = " ,np.average(lesTauxDErreur))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    