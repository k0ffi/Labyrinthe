import matplotlib.pyplot as plt
import random
from Cellule import *
from Grille import *




lig = input("Entrez le nombre de lignes du labyrinthe : ")
col = input("Entrez le nombre de colonnes du labyrinthe : ")
print("+++++++++++++++++++++++++++++++++++++++++++\n")
print("               LA GRILLE   ")
print("+++++++++++++++++++++++++++++++++++++++++++\n\n")
g=Grille(int(lig),int(col))




plt.show()
plt.close()

print("+++++++++++++++++++++++++++++++++++++++++++\n")
print("               LA GRILLE PERCEE  ")
print("+++++++++++++++++++++++++++++++++++++++++++\n\n")

g.graphGrille()
g.DessinTrou()
plt.show()
plt.close()


print("+++++++++++++++++++++++++++++++++++++++++++\n")
print("        LA GRILLE  ET LE CHEMIN OPTIMAL ")
print("+++++++++++++++++++++++++++++++++++++++++++\n\n")

print("+++++++++++++++++++++++++++++++++++++++++++\n")
print("           Le chemin optimal => "+str(g.cheminOptimalCoord()))
print("*******************************************")
print("     Le coût minimal de la traversée => "+str(g.coutChemin()))

print("+++++++++++++++++++++++++++++++++++++++++++\n\n")

g.graphGrille()
g.DessinTrou()
g.DessinChemin()
plt.show()
plt.close()




