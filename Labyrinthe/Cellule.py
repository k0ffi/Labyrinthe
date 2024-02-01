import matplotlib.pyplot as plt
import random

class Cellule :

    #constructeur
    def __init__(self,i,j):
        self._nord = random.randint(1,5)
        self._sud =  random.randint(1,5)
        self._ouest = random.randint(1,5)
        self._est =  random.randint(1,5)
        self._i = i
        self._j = j

    # assesseurs (setteurs)
    def setNord(self, n):
        self._nord =n

    def setSud(self, n):
        self._sud =n

    def setOuest(self, n):
        self._ouest =n   

    def setEst(self, n):
        self._est =n

    def setGrille(self, g):
        self._g = g

    # getteurs 
    def getNord(self): 
            return self._nord

    def getSud(self): 
            return self._sud

    def getOuest(self): 
            return self._ouest
        
    def getEst(self): 
            return self._est
    
    def geti(self):
        return self._i
    
    def getj(self):
        return self._j


    # to String 
    def __str__(self):
        return " [Nord] "+ str(self._nord)+"\n[Sud] "+ str(self._sud)+"\n[ouest] "+str(self._ouest)+"\n[Est] "+str(self._est)

    # affichage graphique 
    def graphCellule(self,i,j):
        X1=[i,i+1]
        Y1=[j,j]

        X2=[i+1,i+1]
        Y2=[j,j+1]

        X3=[i+1,i]
        Y3=[j+1,j+1]

        X4=[i,i]
        Y4=[j+1,j]
        
        plt.plot(X1,Y1,linewidth = self._sud*5,color = "#0000FF")       
        plt.plot(X2,Y2,linewidth = self._est*5,color = "#0000FF")
        plt.plot(X3,Y3,linewidth = self._nord*5,color = "#0000FF")
        plt.plot(X4,Y4,linewidth = self._ouest*5,color = "#0000FF")
    
