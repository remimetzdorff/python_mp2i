#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:23:57 2022
Circuit RLC
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#########################
# MODÉLISATION DU CIRCUIT
#########################
# Circuit RLC série alimenté par le signal sinusoïdal e d'un GBF,
# On mesure de la tension s aux bornes du condensateur
R = 100     # résistance en ohms
L = 11e-3   # inductance en henry
C = 10e-9   # capacité en farad
omega0 = 1/np.sqrt(L*C)
f0     = omega0/ 2 / np.pi
Q      = 1/R * np.sqrt(L/C)

f = 1e3     # fréquence du GBF

V0  = [1,0] # conditions initiales pour la résolution

def e(t):
    # signal du GBF
    return 1*np.cos(2*np.pi*f*t)

def rlc(V,t):
    # fonction associée à l'équation différentielle pour la tension aux bornes de C
    s, ds = V
    dds = (e(t) - s) / (L*C) - R/L * ds
    dV = [ds, dds]
    return dV

############
# RÉSOLUTION
############
t = np.linspace(0,1e-2,100000) # temps t en seconde
V = odeint(rlc, V0, t)
uc = V[:,0]                    # tension aux bornes du condensateur
duc = V[:,1]                   # dérivée de la tension aux bornes du condensateur
i   = C * duc                # intensité du courant dans le circuit

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0))

ax1.set_title("Réponse d'un circuit RLC à une excitation sinusoïdale")
ax1.plot(t*1e3,e(t),label="$e(t)$")
ax1.plot(t*1e3,uc,label="$s(t)$")
ax1.set_ylabel("Tension (V)")
ax1.legend()

ax2.plot(t*1e3,i*1e3, "C2",label="$i(t)$")
ax2.set_ylabel("Intensité (mA)")
ax2.legend()


for ax in [ax1, ax2]:
    ax.set_xlabel("Temps (ms)")
    ax.grid()

plt.tight_layout()
plt.show()