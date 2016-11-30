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
            plt.plot(x1,x2,"bo")
        else :
            lesClasses.append(-1)
            plt.plot(x1,x2,"ro")
    return lesClasses
       
X = tireNPoints(100)
for vec in X :
    vec.append(1)
y = attribuerClasse(X)       
       
Xlearn = np.array(X[:80])
Xtest = np.array(X[80:])
ylearn = np.array(y[:80])
ytest = np.array(y[80:])
teta = np.random.random(size=3)

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
        print("learning ",1-nbError/len(Xlearn))
    return teta        

teta = ptrain(Xlearn,ylearn,teta)

def ptest(Xtest,ylearn,teta) :
    x1s = []
    x2s = []
    for liste in Xtest :
        x1s.append(liste[0])
        x2s.append(-(teta[0]*liste[0]+teta[2])/teta[1])
    return (x1s,x2s)

(x1s,x2s) = ptest(Xtest,ylearn,teta)
plt.plot(x1s,x2s)

plt.show()

    