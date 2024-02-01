import matplotlib.pyplot as plt
from random import *
from Cellule import *


class Grille :
   
    #constructeur
    def __init__(self,lig,col):  #lig,col les dimensions du rectangle 
        tab=[]
        for i in range (col):
            for j in range (lig):
                if i==0 and j==0:
                    c=Cellule(i,j)
                    c.graphCellule(i,j)
                    tab.append([c])
                elif i==0 and j>0:
                    c=Cellule(i,j)
                    c.setSud(tab[i][j-1].getNord())
                    c.graphCellule(i,j)
                    tab[i].append(c)
                elif i>0 and j==0:
                    c=Cellule(i,j)
                    c.setOuest(tab[i-1][j].getEst())
                    c.graphCellule(i,j)
                    tab.append([c])
                else:
                    c=Cellule(i,j)
                    c.setSud(tab[i][j-1].getNord())
                    c.setOuest(tab[i-1][j].getEst())
                    c.graphCellule(i,j)
                    tab[i].append(c)
        self._g  =tab
        self._lig = lig
        self._col = col


    #getteurs
    def getLig(self):
        return self._lig
    
    def getCol(self):
        return self._col


    # To String 
    def __str__(self):
        res=""
        
        for i in range (len(self._g)):
            for j in range(len(self._g[0])):
                res  += "pos : "+str(i)+","+str(j)+"\n"+self._g[i][j].__str__()+"\n ####"
        return res 


    #affichage de la grille
    def graphGrille(self):
        for i in range(len(self._g)):
            for j in range(len(self._g[i])):
                self._g[i][j].graphCellule(i,j)
                

    #renvoie le numéro d'une cellule dans la grille suivant ses coordonées
    def numeroCellule(self,posX,posY):
        cpt=-1
        for j in range(len(self._g[0])-1,-1,-1):
            for i in range(0,len(self._g)):
                cpt+=1
                if i==posX and j == posY:
                    return cpt

    #renvoie la liste des numéros des cellules présentes dans la grille avec leurs coordonées
    def numerosCellule(self):
        cpt=-1
        L=[]
        for j in range(len(self._g[0])-1,-1,-1):
            for i in range(0,len(self._g)):
                cpt+=1
                L.append(((i,j),cpt))
        return L

    #renvoie la liste des voisins d'une cellule avec la liste des murs qui touchent la cellule
    def casesVoisines(self,i,j):
        L=[]
        C = []
        #coin en haut à gauche
        if i==0 and j==len(self._g[0])-1:
            L.append(self._g[i+1][j])
            L.append(self._g[i][j-1])
            C.append(self._g[i+1][j].getOuest())
            C.append(self._g[i][j-1].getNord())

        #coin en bas à gauche
        elif i==0 and j==0:
            L.append(self._g[i][j+1])
            L.append(self._g[i+1][j])
            C.append(self._g[i][j+1].getSud())
            C.append(self._g[i+1][j].getOuest())

        #coin en haut à droite
        elif i==len(self._g)-1 and j==len(self._g[0])-1:
            L.append(self._g[i-1][j])
            L.append(self._g[i][j-1])
            C.append(self._g[i-1][j].getEst())
            C.append(self._g[i][j-1].getNord())

        #coin en bas à droite
        elif i==len(self._g)-1 and j==0:
            L.append(self._g[i][j+1])
            L.append(self._g[i-1][j])
            C.append(self._g[i][j+1].getSud())
            C.append(self._g[i-1][j].getEst())

        #bord haut
        elif j==len(self._g[0])-1 :
            L.append(self._g[i+1][j])
            L.append(self._g[i-1][j])
            L.append(self._g[i][j-1])
            C.append(self._g[i+1][j].getOuest())
            C.append(self._g[i-1][j].getEst())
            C.append(self._g[i][j-1].getNord())

        #bord bas
        elif j==0:
            L.append(self._g[i+1][j])
            L.append(self._g[i-1][j])
            L.append(self._g[i][j+1])
            C.append(self._g[i+1][j].getOuest())
            C.append(self._g[i-1][j].getEst())
            C.append(self._g[i][j+1].getSud())
        
        #bord gauche
        elif i==0:
            L.append(self._g[i][j+1])
            L.append(self._g[i][j-1])
            L.append(self._g[i+1][j])
            C.append(self._g[i][j+1].getSud())
            C.append(self._g[i][j-1].getNord())
            C.append(self._g[i+1][j].getOuest())
        
        #bord droit
        elif i==len(self._g)-1:
            L.append(self._g[i][j+1])
            L.append(self._g[i][j-1])
            L.append(self._g[i-1][j])
            C.append(self._g[i][j+1].getSud())
            C.append(self._g[i][j-1].getNord())
            C.append(self._g[i-1][j].getEst())
        
        #toutes les autres cases
        else:
            L.append(self._g[i+1][j])
            L.append(self._g[i-1][j])
            L.append(self._g[i][j+1])
            L.append(self._g[i][j-1])
            C.append(self._g[i+1][j].getOuest())
            C.append(self._g[i-1][j].getEst())
            C.append(self._g[i][j+1].getSud())
            C.append(self._g[i][j-1].getNord())

        return (L,C)
    

    #"transforme" la grille en un graphe pondéré
    def Grille2graph(self): 
        G={}
        k=0
        invois=[]
        L=self.numerosCellule()
        l=0
        for j in range(len(self._g[0])-1,-1,-1):
            for i in range(0,len(self._g)):
                (vois,epaiss) = self.casesVoisines(i,j)
                while k<len(vois):      #parcours de toutes les cases voisines de la cellule en i,j
                    while (vois[k].geti(),vois[k].getj())!=L[l][0]:
                        l+=1 
                    invois.append((L[l][1],epaiss[k]))
                    l=0
                    k+=1
                G[self.numeroCellule(i,j)]=invois
                k=0
                invois=[]
        return G 


    #algorithme de Dijkstra
    def dijkstra_pred(self,G,s):
        D={} #tableau final des distances minimales
        d={k: float('inf') for k in G} #distances initiales infinies
        d[s]=0 #sommet de départ
        P={} #liste des prédécesseurs
        while len(d)>0: #fin quand d est vide
            k=self.minimum(d) #sommet de distance minimale pour démarrer une étape
            for i in range(len(G[k])): #on parcourt les voisins de k
                v, c = G[k][i] #v voisin de k, c la distance à k
                if v not in D: #si v n'a pas été déjà traité
                    if d[v]>d[k]+c: #est-ce plus court en passant par k ?
                        d[v]=d[k]+c
                        P[v]=k #stockage du prédécesseur de v
            D[k]=d[k] #copie du sommet et de la distance dans D
            del(d[k]) #suppression du sommet de d
        return D, P #on retourne aussi la liste des prédécesseurs


    #fonction minimum utilisée dans l'algorithme de Dijkstra
    def minimum(self,dico):
        m=float('inf')
        for k in dico: #parcours des clés
            if dico[k] < m:
                m=dico[k]
                i=k
        return i  

    #renvoie les coordonées d'une cellule en fonction de son numéro (position)
    def numero2pos(self,x):
        cpt=0
        for j in range(len(self._g[0])-1,-1,-1):
            for i in range(0,len(self._g)):
                if cpt==x:
                    return (i,j)
                else:   
                    cpt+=1

    #renvoie le chemin optimal sous la forme d'une liste des numéros des cellules
    def cheminOptimalNum(self):
        G = self.Grille2graph()
        D,P = self.dijkstra_pred(G,0)
        p= self.getCol()*self.getLig()-1
        L = []
        L.append(p)
        while p!=0:
            p = P[p]
            L.append(p)
        
        L.reverse()
        return L
    
    #renvoie le chemin optimal sous la forme d'une liste des coordonées des cellules
    def cheminOptimalCoord(self):
        L = self.cheminOptimalNum()
        C=[]
        for i in range (len(L)):
            C.append(self.numero2pos(L[i]))
        return C
    
    #renvoie le coût du chemin optimal
    def coutChemin(self):
        G = self.Grille2graph()
        D,P = self.dijkstra_pred(G,0)
        p= self.getCol()*self.getLig()-1
        return D[p]

    #renvoie les coordonées dans lesquels on doit dessiner le chemin et les trous dans les murs
    def GrilleTrou(self):
        X = []
        Y = []
        L = self.cheminOptimalCoord()
        for i in range(len(L)-1):
            x1 = L[i][0]
            x1 = x1+0.5
            x2 = L[i+1][0]
            x2 = x2+0.5
            y1 = L[i][1]
            y1 = y1+0.5
            y2 = L[i+1][1]
            y2 = y2+0.5
            X.append(x1)
            X.append(x2)
            Y.append(y1)
            Y.append(y2)
        return (X,Y)

    #dessine les trous dans la grille
    def DessinTrou(self):
        X,Y = self.GrilleTrou()
        plt.plot(X,Y,linewidth = 30,color = "#FFFFFF")  
    
    #dessine le chemin optimal dans la grille
    def DessinChemin(self):
        X,Y = self.GrilleTrou()
        plt.plot(X,Y,linewidth = 15,color = "#FF0000")  

