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
        distance = np.abs(-0.5*x1-x2+0.75)/np.sqrt((0.5**2)+1)
        tet = np.exp(-(distance**2/(2*(0.05**2))))
        permut = r.random() < tet/2
        if calcule <= x2 :
            if not permut :
                lesClasses.append(1)
            else :
                lesClasses.append(-1)
            #plt.plot(x1,x2,"bo")
        else :
            if not permut :
                lesClasses.append(-1)
            else :
                lesClasses.append(1)
            #plt.plot(x1,x2,"ro")
    return lesClasses
    
    
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
    
def tracePoints(X,c) :
    for i in range(len(X)) :
        if c[i] == 1 :
            form = "bo"
        else :
            form = "ro"
        plt.plot(X[i][0],X[i][1],form)

(X_train,X_test,c_train,c_test) = datagen(10000)
tracePoints(X_train,c_train)