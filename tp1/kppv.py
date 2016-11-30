from sklearn import datasets
import numpy as np

db = datasets.load_iris()

X = db.data
y = db.target

#le nombre d'exemples
n = len(X)
nb_classes = 3
d = len(X[0])

Xlearn = []
Xtest = []
ylearn = []
ytest = []

#Division base learn / base Test
for i in range(n) :
    if i % 8 == 0 :
        Xtest.append(X[i])
        ytest.append(y[i])        
    else :
        Xlearn.append(X[i])
        ylearn.append(y[i])


def kppv(x, Xlearn, ylearn, k) :
    lesDist = []
    for vec in Xlearn :
        lesDist.append(np.linalg.norm(vec-x))
    lesDistSorted = np.argsort(lesDist)
    # maintenant on observe que les kppv    
    lesKVoisins =  []
    for i in range(k) :
        laClasse = ylearn[lesDistSorted[i]]
        lesKVoisins.append(laClasse)
    return lesKVoisins[np.argmax(lesKVoisins)]
    
def testKPPV(Xlearn, ylearn, Xtest, ytest,k) :
    nbError = 0
    for i in range(len(Xtest)) :
        x = Xtest[i]
        yTruth = ytest[i]
        predict = kppv(x,Xlearn,ylearn,k)
        print(predict , yTruth)
        if not(predict ==  yTruth) :
            nbError += 1
    print("taux d'erreur = ",1 - nbError/(len(Xtest)))
    
testKPPV(Xlearn,ylearn,Xtest,ytest,4)