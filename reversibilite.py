#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 09:58:17 2024
Réversibilité d'une chute
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

############
# PARAMÈTRES
############
REVERSED = True

# Paramètres physiques
g = 10 # accélération de la pesanteur (m/s^2)
m = 1  # masse du projectile (kg)
k = 1  # coefficient de frottement (kg/s)

# Conditions initiales
alpha = 1.2 # angle du tir par rapport à l'horizontale (rad)
v0    = 25      # vitesse initiale (m/s)
V0    = [0, 0, v0*np.cos(alpha), v0*np.sin(alpha)]

# Paramètres de la simulation
fps = 25
ti, tf = 0, 5
t = np.linspace(ti, tf, (tf-ti)*fps)
N = len(t)

######################
# RÉSOLUTION NUMÉRIQUE
######################
def chute(V,t):
    x, z, vx, vz = V
    ax = -k/m * vx
    az = -g - k/m * vz
    return [vx, vz, ax, az]

V = odeint(chute, V0, t)
x = V[:,0]
z = V[:,1]

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
fig = plt.figure()
ax  = plt.subplot()

ax.plot(x,z)
ax.set_aspect("equal")
ax.set_xlabel("$x$ (m)")
ax.set_ylabel("$z$ (m)")

###########
# ANIMATION
###########

bullet, = ax.plot([], [], "ok")

def animate(i):
    if REVERSED:
        i = N-i-1
    bullet.set_data([x[i]], z[i])
    return  bullet

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=1e3/25)
plt.show()