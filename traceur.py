# tp8_traceur.py
# Ce programme permet :
#   - lire un fichier de donnée .txt ;
#   - représenter graphiquement les données ;
#   - dériver une gradeur par rapport au temps ;

import numpy as np
import matplotlib.pyplot as plt

def deriv(x,t):
    """calcule la dérivée numérique des valeurs de x par rapport à t"""
    # S'aider de du notebook accessible depuis l'application capytale sur l'ENT
    # Code du notebook : 215b-989450
    # URL : https://capytale2.ac-paris.fr/web/c/215b-989450
    return # À COMPLÉTER

def norme(x,y):
    """calcule la norme d'un vecteur (x,y)"""
    return # À COMPLÉTER

#########################
# IMPORTATION DES DONNÉES
#########################
filename = "rampe_prof.txt" # À MODIFIER
data     = np.loadtxt(filename, skiprows=1)
temps_pos = data[:,0]
pos_x     = data[:,1]
pos_y     = data[:,3]

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
plt.plot(temps_pos, pos_x, "o")
plt.xlabel("Temps (s)")
plt.ylabel("Position $y$ (m)")
plt.title("Mouvement d'une balle sur une rampe")
plt.grid()
plt.show()