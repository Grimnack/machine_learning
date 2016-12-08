import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as s


taille_h = np.loadtxt("taille_h.txt")
taille_f = np.loadtxt("taille_f.txt")
classe_h = [1]*len(taille_h)
classe_f = [0]*len(taille_f)
nbins = int(max(taille_h)) + 1

X1 = np.append(taille_h,taille_f)
X2 = np.append(classe_h,classe_f)

taille_min = int(min(X1))
taille_max = int(max(X1)) + 1



#plt.hist(taille_h,bins=nbins,color="blue")
#plt.hist(taille_f,bins=nbins,color="pink")

# LES Variables X1 ET X2 ne sont pas indépendantes car on observe bien
# que les hommes sont en moyenne plus grands que les femmes

#plt.hist(X1,bins=nbins,color='green')

def loi_marginale(lesTailles) :
    loi_marginale = [0]*taille_max
    for taille in lesTailles :
        loi_marginale[int(taille)] += 1
    return loi_marginale

def mode(marginale) :
    max_value = 0
    cm_save = 0
    for cm in range(len(marginale)) :
        if marginale[cm] > max_value :
            max_value = marginale[cm]
            cm_save = cm
    return cm_save
    
def esperance(marginale,nbSample) :
    esp = 0
    for cm in range(len(marginale)) :
        esp += cm * (marginale[cm]/nbSample)
    return esp
        
def mediane(marginale,nbSample) :
    nbVues = 0
    for cm in range(len(marginale)) :
        nbVues += marginale[cm]
        if nbVues >= nbSample/2 :
            return cm
            
    

marginale_hommes = loi_marginale(taille_h)
marginale_femmes = loi_marginale(taille_f)  
marginale_x1 = loi_marginale(X1)
taille_frequente = mode(marginale_x1)
taille_moyenne = esperance(marginale_x1,len(X1))
taille_moyenne_homme = esperance(marginale_hommes,len(taille_h))
taille_mediane = mediane(marginale_x1,len(X1))
ecartType_hommes = np.std(taille_h)
ecartType_femmes = np.std(taille_f)
mm_centre_ordre3_h = s.skew(taille_h)
mm_centre_ordre3_f = s.skew(taille_f)

marginale_hommes_nomalised = np.array([x/len(marginale_hommes) for x in marginale_hommes])


# Question 8 calculer la Negative Log Likelyhood
listeMu = [x for x in range(140,220,1)]
listeSigma = [x/10 for x in range(100,400,2)]


def gauss(mu,sigma,x) :
    top = np.exp(-((x-mu)**2)/((2*sigma)**2))
    return top/(np.sqrt(2*np.pi*sigma))

def NegLogLikelyhood(mu,sigma,dataset) :
    '''
    donne la vraissemblance par rapport a une gaussienne
    '''
    somme = 0
    for data in dataset :
        somme += np.log(gauss(mu,sigma,data))
    return -somme
    
def chercheTeta(listeMu,listeSigma,dataset) :
    '''
    On chercher les valeurs de mu et teta maximisant la vraissemblance,
    donc minimisant la NLL
    '''
    res = []
    couple = []
    for mu in listeMu :
        for sigma in listeSigma :
            res.append(NegLogLikelyhood(mu,sigma,dataset))
            couple.append((mu,sigma))
    return couple[np.argmin(res)]

#ça prend du temps, je l'ai calculé mu vaut 175 et sigma vaut 16.8
#(mu,sigma) = chercheTeta(listeMu,listeSigma,taille_h)
x_gauss = [x for x in range(0,taille_max)]
y_gauss = [gauss(175,16.8,x) for x in range(0,taille_max)]

plt.bar(x_gauss,marginale_hommes_nomalised)
plt.plot(x_gauss,y_gauss,color="red")
 

