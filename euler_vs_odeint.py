#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 16:44:18 2025
Comparaison entre les méthodes d'Euler et odeint
On simule la réponse de la tension aux bornes du condensateur
dans un circuit RLC série soumis à un échelon entre 0 et E
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

###############################
# PARAMÈTRES DE LA SIMULATION #
###############################
t0 = -.1e-3              # bornes de l'intervalle de résolution
tf = 1e-3
dt = 1e-8                # pas de temps
n  = int((tf-t0)/dt + 1) # nombre de points
t = np.linspace(t0, tf,n) # temps en seconde

R = 1000     # en ohms Rc = 200
L = 1e-3   # en henry
C = 1e-7    # en farads
omega0 = 1 / np.sqrt(L * C) # pulsation propre en rad/s
Q = L * omega0 / R          # facteur de qualité
E = 1                       # amplitude de l'échelon (V)
e = np.zeros(n)
for k in range(n):
    if t[k] >= 0:
        e[k] = E

i0, u0 = 0, 0            # conditions initiales

#############################
# MÉTHODE D'EULER EXPLICITE #
#############################
i, u = np.zeros(n), np.zeros(n)
i[0] = i0    # initialisation
u[0] = u0    # initialisation

for k in range(n-1):
    i[k+1] = i[k] + dt * (e[k] - u[k] - R*i[k]) / L
    u[k+1] = u[k] + dt * i[k] / C

i_euler = i
u_euler = u
e_euler = e

##########
# ODEINT #
##########
def e(t):
    val = 0
    if t >= 0:
        return E
    else:
        return 0
    
def rlc(V, t):
    u, i = V
    du = i/C
    di = 1/L * ( e(t) - u - R*i )
    return [du, di]
V = odeint(rlc, [u0,i0], t)
u_odeint = V[:,0]
i_odeint = V[:,1]

##############################
# REPRÉSENTATIONS GRAPHIQUES #
##############################
plt.figure()
sps=(2,1)
ax1 = plt.subplot2grid(sps, (0,0))
plt.tick_params('x', labelbottom=False)
ax2 = plt.subplot2grid(sps, (1,0), sharex=ax1)

ax1.set_title("Réponse d'un circuit RLC à un échelon de tension")
ax1.plot(t*1e3, e_euler, label="$e(t)$") # échelon
ax1.plot(t*1e3, u_euler, "C1", label="$u_C(t)$ (Euler)")
ax1.plot(t*1e3, u_odeint, "C2", label="$u_C(t)$ (odeint)")
ax1.legend()
ax1.grid()
ax1.set_ylabel("Tension (V)")

ax2.plot(t*1e3, i_euler*1e3, "C1", label="$i(t)$ (Euler)")
ax2.plot(t*1e3, i_odeint*1e3, "C2", label="$i(t)$ (odeint)")
ax2.legend()
ax2.grid()
ax2.set_ylabel("Intensité (mA)")
ax2.set_xlabel("Temps (ms)")

plt.tight_layout()