#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:25:48 2022
Circuit RLC Euler
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

###########
# RLC SÉRIE
###########

#############################
# PARAMÈTRES DE LA RÉSOLUTION
#############################
t0 = -.1e-3               # bornes de l'intervalle de résolution
tf = 1e-3
dt = 1e-8                # pas de temps
n  = int((tf-t0)/dt + 1) # nombre de points
t = np.linspace(t0,tf,n) # temps en seconde

###########################
# PARAMÈTRES DU CIRCUIT RLC
###########################
R = 1000     # en ohms Rc = 200
L = 1e-3   # en henry
C = 1e-7    # en farads
omega0 = 1 / np.sqrt(L * C) # pulsation propre en s^-1
Q = L * omega0 / R   # facteur de qualité

print("Q = {:.2f}".format(Q))

############
# SIGNAL GBF
############
E   = 1   # offset
amp = 1   # amplitude
f   = 200   # fréquence en hertz

constant = np.ones(n) * E
step     = np.array([(E if val>=0 else 0) for val in t]) 
square   = amp * np.sign(np.sin(2*np.pi*f*t)) + E
sinus    = amp * np.sin(2*np.pi*f*t) + E
noise    = np.random.normal(0,.05,n) # modélisation d'un bruit aléatoire

e = step # signal aux bornes du GBF

#################
# MÉTHODE D'EULER
#################
u0  = 0   # CI en volts
i0  = 0   # CI en ampères
u = np.zeros(len(t))  # préparation du tableau
i = np.zeros(len(t))
u[0] = u0             # initialisation en fonction de la CI
i[0] = i0
for k in range(n-1):  # méthode d'Euler explicite
    i[k+1] = i[k] + dt/L * (e[k] - u[k]) - dt * R/L * i[k]
    u[k+1] = u[k] + dt * i[k] / C

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.plot(t*1e3,e, label="e(t)")
plt.plot(t*1e3,u, label="u(t)")
plt.grid()
plt.xlabel("Temps $t$ (ms)")
plt.ylabel("Tension $u_C(t)$ (V)")
plt.legend()
plt.show()