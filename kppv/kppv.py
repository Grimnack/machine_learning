from sklearn import datasets

db = datasets.load_iris()

X = db.data
y = db.target


#le nombre d'exemples
n = len(X)

nb_classes = 3

print(db)
