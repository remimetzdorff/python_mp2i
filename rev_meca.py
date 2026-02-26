#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 09:27:27 2023
Réversibilité
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
import matplotlib.animation as animation

reverse = True

############
# PARAMÈTRES
############
m     = 1
g     = 10
alpha = 3
v0    = [20,40]
fps   = 25

#######################
# SOLUTIONS ANALYTIQUES
#######################
if alpha == 0: # CHUTE LIBRE
    tf = 2 * v0[1] / g      # fin de la chute
    
    def vx(t): # vitesse horizontale
        return v0[0] * t/t
    
    def vy(t): # vitesse verticale
        return v0[1] - g * t
    
    def x(t): # coordonnée horizontale
        return v0[0] * t
    
    def y(t): # coordonnée verticale
        return v0[1] * t - g/2 * t**2

else: # CHUTE AVEC FROTTEMENTS LINÉAIRES
    vlim  = - m * g / alpha # vitesse limite verticale
    tau   = m / alpha       # temps caractéristique
    def f(t):
        return tau * (v0[1] - vlim) * (1 - np.exp(-t/tau)) + vlim * t
    tf = bisect(f,1e-3,1e9) # fin de la chute
    
    def vx(t): # vitesse horizontale
        return v0[0] * np.exp(-t/tau)
    
    def vy(t): # vitesse verticale
        return (v0[1] - vlim) * np.exp(-t/tau) + vlim
    
    def x(t): # coordonnée horizontale
        return tau * v0[0] * (1 - np.exp(-t/tau))
    
    def y(t): # coordonnée verticale
        return f(t)

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
t = np.linspace(0, tf, int(tf*fps))

fig = plt.figure()
ax = plt.subplot2grid((1,1), (0,0))
ax.plot(x(t), y(t))
ax.set_aspect("equal")
ax.grid()

###########
# ANIMATION
###########
if reverse:
    t = t[::-1]

particule, = ax.plot([], [], "ok")
def animate(i):
    particule.set_data([x(t[i])], [y(t[i])])
    return particule

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=1e3/fps)
plt.tight_layout()

plt.show()