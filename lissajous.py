#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 12:08:58 2025

@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initialisation des paramètres
A = 1      # Amplitude du signal X
B = 1      # Amplitude du signal Y
phi = 0    # Déphasage initial (en degrés)

# Fonction pour générer la courbe de Lissajous
def lissajous(phi):
    t = np.linspace(0, 2*np.pi, 1000)
    x = A * np.sin(t)
    y = B * np.sin(t + phi*np.pi/180)
    return x, y

# Création de la figure et de l'axe
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
x, y = lissajous(phi)
lissajous_line, = ax.plot(x, y)
ax.set_title("Courbe de Lissajous")
ax.set_aspect('equal')
ax.set_xlabel("$s_1(t)$")
ax.set_ylabel("$s_2(t)$")
ax.grid()

# Ajout du curseur de déphasage
ax_phi = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_phi = Slider(ax_phi, 'Déphasage (°)', 0, 360, valinit=phi, valfmt='%0.0f')

def update(val):
    phi = slider_phi.val
    x, y = lissajous(phi)
    lissajous_line.set_data(x, y)
    fig.canvas.draw_idle()

slider_phi.on_changed(update)
plt.show()