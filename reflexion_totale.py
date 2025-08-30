#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 19:09:36 2022
Reflexion totale
@author: remimetzdorff
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

i = 30*np.pi/180 # angle d'incidence en radian
n_air = 1.00     # indice optique de l'air
n_eau = 1.33     # indice optique de l'eau
eau_air = True   # sens du rayon incident

##########################
# PRÉPARATION DE LA FIGURE
##########################
fig, ax = plt.subplots(figsize=(6,4))
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.gca().set_aspect('equal') # même échelle sur les deux axes
plt.gca().set_axis_off()
# Le décor
plt.plot([-2,2], [0,0], "-k")
plt.fill_between([-2,2], 0,-2, color="C0", alpha=0.25)
plt.plot([0,0], [-2,2], "--k", alpha=0.2) # normale au dioptre
plt.gca().annotate("air", (-1,.1))
plt.gca().annotate("eau", (-1,-.1))

#################
# TRACÉ DE RAYON
#################
if eau_air:
    var_eau_air = 1
else:
    var_eau_air = -1
# rayon incident
xa = -np.sin(i)      # abscisse du point A
ya = -var_eau_air * np.cos(i)      # ordonnée du point A
rayon_incident, = plt.plot([xa,0], [ya,0])
# rayon réfléchi
xb = np.sin(i)       # abscisse du point B
yb = -var_eau_air * np.cos(i)      # ordonnée du point B
rayon_reflechi, = plt.plot([xb,0], [yb,0])
# rayon réfracté
if eau_air:
    r = np.arcsin(n_eau * np.sin(i) / n_air) # angle réfracté en radian
else:
    r = np.arcsin(n_air * np.sin(i) / n_eau) # angle réfracté en radian
xc = np.sin(r)   # abscisse du point C
yc = var_eau_air * np.cos(r)   # ordonnée du point C
rayon_refracte, = plt.plot([xc,0], [yc,0])

#########
# SLIDERS
#########
# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the omega.
axi = plt.axes([0.25, 0.1, 0.65, 0.03])
i_slider = Slider(
    ax=axi,
    label="$i\ (°)$",
    valmin=0,
    valmax=90,
    valinit=30,
)

# The function to be called anytime a slider's value changes
def update(val):
    i = val*np.pi/180
    xa = -np.sin(i)      # abscisse du point A
    ya = -var_eau_air * np.cos(i)      # ordonnée du point A
    rayon_incident.set_xdata([xa,0])
    rayon_incident.set_ydata([ya,0])
    xb = np.sin(i)       # abscisse du point B
    yb = - var_eau_air * np.cos(i)      # ordonnée du point B
    rayon_reflechi.set_xdata([xb,0])
    rayon_reflechi.set_ydata([yb,0])
    if eau_air and (np.abs(i) < np.arcsin(n_air/n_eau)):
        r = np.arcsin(n_eau * np.sin(i) / n_air) # angle réfracté en radian
        xc = np.sin(r)   # abscisse du point C
        yc = np.cos(r)   # ordonnée du point C
        rayon_refracte.set_xdata([xc, 0])
        rayon_refracte.set_ydata([yc, 0])
    elif not eau_air:
        r = np.arcsin(n_air * np.sin(i) / n_eau) # angle réfracté en radian
        xc = np.sin(r)   # abscisse du point C
        yc = var_eau_air * np.cos(r)   # ordonnée du point C
        rayon_refracte.set_xdata([xc, 0])
        rayon_refracte.set_ydata([yc, 0])
    else:
        rayon_refracte.set_xdata([0, 0])
        rayon_refracte.set_ydata([0, 0])
    
    fig.canvas.draw_idle()

# register the update function with each slider
i_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    i_slider.reset()
button_reset.on_clicked(reset)

plt.show()                     # pour afficher le graphique