#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:53:25 2023
Flux thermique à travers un barreau métalique
Puissance imposée à gauche
Température imposée à droite
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

######################
# PARAMÈTRES PHYSIQUES
######################
L   = .1         # m            : longueur du barreau
r   = 1e-2       # m            : rayon du bareau
S   = np.pi*r**2 # m^2          : section du barreau
l   = 390        # W.m^-1.K^-1  : conductivité thermique du cuivre
rho = 8.96e3     # kg.m^-3      : masse volumique du cuivre
c   = 385        # J.K^-1.kg^-1 : capacité thermique massique du cuivre
D   = l/rho/c    # m^2.s^-1     : coefficient de diffusion thermique
Pg  = 200         # W            : puissance imposée à gauche
Td  = 300        # K            : température de l'extrémité droite
tau = L**2/D     # s            : temps caractéristique de diffusion
start_heat = 0   # s            : début du chauffage
stop_heat  = 1e6 # s            : fin du chauffage
n_capteurs = 6   #              : nombre de capteurs de température
complete_plot = False #         : set to False to avoid excessive lag 

# En RP, température de l'extrémité gauche
Tg = Td + L * Pg / l / S

#############################
# PARAMÈTRES DE LA SIMULATION
#############################
t_start = -10      # s            : date du début de la simulation 
t_stop  = int(5*tau+1)       # s            : date de la fin de la simulation
n_L = 101          #              : nombre de pas d'espace
dx = L/(n_L-1)     # m            : pas d'espace
dt_lim = dx**2/2/D # s            : pas minimal de temps pour convergence
n_t = int(1.1*(t_stop - t_start)/dt_lim) # : nombre de pas de temps

t  = np.linspace(t_start, t_stop, n_t) # s : tableau des instants
x  = np.linspace(0, L, n_L)            # m : tableau des positions

#################
# MÉTHODE D'EULER
#################
T0   = np.ones(n_L) * Td                 
T    = np.zeros((n_t,n_L)) # K : tableau des températures
T[0] = T0
dt = t[1] - t[0]
dx = x[1] - x[0]
for n in range(n_t-1):
    # exception pour l'extrémité gauche du barreau
    P = 0
    actual_t = t_start + n*dt
    if actual_t >= start_heat and actual_t < stop_heat:
        P = Pg
    source = P * dt / rho/c/S/dx
    conduc = D*dt/dx**2 * (T[n,2]-T[n,1])
    T[n+1,0] = T[n,0] + conduc + source
    for i in range(1,n_L-1):
        lap = (T[n,i+1] + T[n,i-1] - 2*T[n,i]) / dx**2
        T[n+1,i] = T[n,i] + D * lap * dt
    T[n+1,n_L-1] = Td      # condition aux limites à droite

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
if complete_plot:
    plt.figure(1)
    N = 10
    colormap = plt.cm.viridis
    colorst = [colormap(i) for i in np.linspace(0, 1, N+1)]
    for k in range(N+1):
        k_t = k*(n_t-1)//N
        plt.plot(x,T[k_t], color=colorst[k], label="$t$ = {:.0f} s".format(t[k_t]))
    plt.xlabel("$x$ (m)")
    plt.ylabel("$T$ (K)")
    plt.grid()
    plt.legend()

###########
# ANIMATION
###########
speed = 20
fps   = 25

fig = plt.figure(2, figsize=(10,6))
sps = (3,2)
ax1 = plt.subplot2grid(sps, (0,0), rowspan=2, colspan=1)
ax3 = plt.subplot2grid(sps, (2,0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid(sps, (0,1), rowspan=2, colspan=1)

if False: # affiche les courbes de temprétaures à différents instants
    N = 101
    colormap = plt.cm.viridis
    colorst = [colormap(i) for i in np.linspace(0, 1, N)]
    for k in range(N):
        k_t = k*(n_t-1)//(N-1)
        ax1.plot(x,T[k_t], color=colorst[k],alpha=.25)
ax1.set_xlabel("$x$ (m)")
ax1.set_ylabel("$T$ (K)")
ax1.set_xlim(0,L)

T_spatial = np.zeros((2,n_L))
z = np.linspace(-r,r,2)
X, Z = np.meshgrid(x,z)
def barreau(j):
    for i in range(2):
        T_spatial[i] = T[j]
    levels = np.linspace(min(Td,Tg),max(Td,Tg),101)
    ax3.clear()
    ax3.contourf(X,Z,T_spatial,levels=levels,cmap="coolwarm")
    ax3.set_aspect("equal")
    #ax3.set_xticks([])
    ax3.set_yticks([])
    return

ax2.set_xlabel("$t$ (s)")
ax2.set_ylabel("$T$ (K)")
ax2.set_xlim(t_start,t_stop)

for ax in  [ax1, ax2]:
    #ax.set_ylim(.99*min(Tg,Td),1.01*max(Tg,Td))
    ax.grid()

Tx, = ax1.plot(x,T[0],"-k")
x_capteur = np.linspace(0,L,n_capteurs)
capteurs, T_capteurs = [], []
for k in range(n_capteurs):
    capteur, = ax1.plot([x_capteur[k]], [T[0,min(k*n_L//(n_capteurs-1),100)]], "o")
    capteurs.append(capteur)
    T_capteur,  = ax2.plot([0],[0])
    T_capteurs.append(T_capteur)
    
def animate(i):
    j = int((speed*i*n_t/fps) / t_stop)
    ax1.set_title("$t$ = {:.0f} s".format(t[j]))
    Tx.set_data(x, T[j])
    T_capteurs[-1].set_data(t[:j], np.ones(j)*Td)
    for k in range(0,n_capteurs-1):
        capteurs[k].set_data([x_capteur[k]], [T[j, k*n_L//(n_capteurs-1)]])
        T_capteurs[k].set_data(t[:j], T.transpose()[k*n_L//(n_capteurs-1),:j])
    if complete_plot:
        barreau(j)
    for ax in  [ax1, ax2]:
        ax.set_ylim(.99*min(Tg,Td),1.01*max(T[j]))
    return

animate(0)
plt.tight_layout()
ani = animation.FuncAnimation(fig, animate, frames=25*t_stop//speed, interval=1e3/fps)
plt.show()