#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:35:20 2024

@author: remimetzdorff
"""

# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy.random as rd


# -----------------------------------------
# PARAMETRES

c = 1
f = 1
w = 2*np.pi*f
k = w/c
T = 2*np.pi/w
lambd = 2*np.pi/k

# pas de temps
dt = 0.01

# fin de la simulation
tf = 4*T
N = int(tf/dt)+1

# array des instants de l'animation
t = np.linspace(0, tf, N)
array_t = np.arange(0,tf+dt,dt)




# bornes pour le tracé spatial de l'onde
xmin = 0
xmax = 3*lambd
# nombre de petits points gris sur le tracé spatial de l'onde
nbx = 55
# pas dx d'un point gris à un autre
dx = (xmax-xmin)/(nbx-1)

# array des absisses pour le tracé du profil spatial
array_x = np.linspace(xmin, xmax, nbx)


# couleurs associées aux capteurs
colorA = 'blue'
colorB = 'orange'

# position des capteurs
xA = 1*lambd
xB = 2.5*lambd

################
# SIGNAL ET ONDE
################
def signal(t):
    # signal émis
    return np.exp(-(t-T/3)**2 / (T/4)**2) * np.sin(w*t)

def onde(x,t):
    tau = t-x/c
    return signal(tau)





sigma_bruit = 0.01


# -----------------------------------------
# CREATION DE LISTES POUR REALISER L'ANIMATION

# liste de array chacun représentant le profil spatial de l'onde pour chaque t
y1=[] 

# Valeurs du signal pour le tracé du profil spatial
y1P=[] # pour le point P (point où est généré la perturbation)
y1A=[] # pour le catpeur A
y1B=[] # pour le capteur B

# valeurs du signal pour le tracé du profil temporel
y2A=[]
y2B=[]

# boucle pour remplir les listes ci-dessus au cours du temps
for i in range(len(array_t)):
    t = array_t[i]
    y1.append(onde(array_x,t))
    y1P.append(signal(t))
    y1A.append(signal(t-xA/c))
    y2A.append(signal(t-xA/c) + rd.normal(0,sigma_bruit))
    y1B.append(signal(t-xB/c))
    y2B.append(signal(t-xB/c) + rd.normal(0,sigma_bruit))



# -----------------------------------------
# TRACES SPATIAL ET TEMPOREL


plt.close('all')
fig, (ax1,ax2)  = plt.subplots(1,2,figsize=(20, 5))


# PROFIL SPATIAL

# forme de l'onde
line, = ax1.plot([], [], color='gray', alpha=.4, marker='o', label='onde') 

# perturbation
pointP, = ax1.plot([], [],'o', color='black', alpha=.75, markersize = 8,label='perturbation') 

# capteurs A et B
capteurA, = ax1.plot([], [],'D', color=colorA, alpha=.6, markersize = 10,label='capteur A') 
capteurB, = ax1.plot([], [],'D', color=colorB, alpha=.6, markersize = 10,label='capteur B') 


# mise en forme
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(-1., 1.5)
ax1.set_xlabel('$x\, (m)$')
ax1.set_ylabel('Signal')
ax1.set_title('Profil spatial')
ax1.grid()
ax1.legend(loc='upper center')


# affichage du temps écoulé
chrono = ax1.text(2.1,1.25,'chrono',va='center',ha='left')


# PROFIL TEMPOREL
signalA, = ax2.plot([], [], color=colorA, alpha=.7, linewidth = 2.5, label='capteur A') 
signalB, = ax2.plot([], [], color=colorB, alpha=.8, linewidth = 2.5, label='capteur B') 


# mise en forme
ax2.set_xlim(0, tf)
ax2.set_ylim(-1., 1.5)
ax2.set_xlabel('$t\, (s)$')
ax2.set_ylabel('Signal')
ax2.set_title('Profil temporel')
ax2.grid()
ax2.legend(loc='upper center')



# ----------------------------------------- 
# ANIMATION

def animate(i): 
    t = array_t[i]

    # tracé du profil spatial à t
    line.set_data(array_x, y1[i])
    
    # perturbation
    pointP.set_data([0],  [y1P[i]])
    
    # capteur A
    capteurA.set_data([xA],  [y1A[i]])
    signalA.set_data(array_t[0:i],y2A[0:i])
    
    # capteur B
    capteurB.set_data([xB],  [y1B[i]])
    signalB.set_data(array_t[0:i],y2B[0:i])
    
    # affichage du temps écoulé                    
    chrono_affichage = t/T
    global chrono
    chrono.remove()
    chrono = ax1.text(2.1,1.25,r'$t = %.2f\,s$'%chrono_affichage,va='center',ha='left')
   

    return line, chrono, pointP, capteurA, signalA, capteurB, signalB,


ani = animation.FuncAnimation(fig, animate, frames=len(array_t),
                              interval=dt, blit=True, repeat=True)




# Pour sauvegarder au format mp4
"""
plt.rcParams['animation.ffmpeg_path'] = r'C:\Program Files\FFMPEG\bin\ffmpeg.exe'
w = animation.FFMpegWriter(fps=30, bitrate=1000)
ani.save(filename="S2_anim_onde_qlcq.mp4", writer=w, dpi = 100)
"""

# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
