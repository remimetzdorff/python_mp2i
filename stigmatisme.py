#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:12:43 2021
Simulation de tracé de rayon sur un dipotre sphérique
@author: remimetzdorff
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

############
# PARAMÈTRES
############
N      = 25          # nb de rayons lumineux
radius = .5            # rayon du dioptre sphérique
n      = 1.5          # indice de la lentille
alpha  = .25            # transparence rayons
frac   = 0.3          # fraction du rayon de la lentille utilisé
D      = 1 * 2*radius # diamètre de la lentille

###############
# figure layout
###############
plt.figure(figsize=(12,8))
ax = plt.subplot2grid((1,1), (0,0))
ax.set_aspect("equal")
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 1)
ax.set_title("Dioptre sphérique")
# diaphragme
diaphragmd, = ax.plot([-1,-1], [-2*radius, -frac*radius], "k", lw=10, solid_capstyle="butt")
diaphragmu, = ax.plot([-1,-1], [2*radius, frac*radius], "k", lw=10, solid_capstyle="butt")
ax.plot([-1, 5], [0,0], "k") # axe optique

# sphere
t = np.linspace(0,2*np.pi,1000)
plt.plot(radius*np.cos(t), radius*np.sin(t), alpha=.1)
# dioptre sphérique
ouverture = np.arcsin(D/2/radius)
t = np.linspace(-ouverture,ouverture,1000)
x, y = radius*np.cos(t),radius*np.sin(t)
ax.plot(x, y,"C0")
ax.plot([np.min(x), np.min(x)], [np.min(y), np.max(y)], "C0")

# rayons
height  = np.linspace(-frac * radius, frac * radius, N)
rayons  = []
for h in height:
    xd = np.sqrt(radius ** 2 - h ** 2)
    i = np.arcsin(h / radius)
    r = np.arcsin(h / radius / n)
    xf = xd - h / np.tan(r-i)
    ray, = ax.plot([-1, xd, xf, 2 * xf - xd], [h, h, 0, -h], color="C3", alpha=alpha)
    rayons.append(ray)

#########
# SLIDERS
#########
plt.subplots_adjust(left=0.25, bottom=0.25)

ax_frac = plt.axes([0.25, 0.1, 0.65, 0.03])
frac_slider = Slider(
    ax=ax_frac,
    label="frac",
    valmin=0,
    valmax=1,
    valinit=frac,
)

def update(val):
    diaphragmu.set_ydata([2*radius, val*radius])
    diaphragmd.set_ydata([-2*radius, -val*radius])
    height  = np.linspace(-val * radius, val * radius, N)
    for h, ray in zip(height,rayons):
        xd = np.sqrt(radius ** 2 - h ** 2)
        i = np.arcsin(h / radius)
        r = np.arcsin(h / radius / n)
        xf = xd - h / np.tan(r-i)
        ray.set_xdata([-1, xd, xf, 2 * xf - xd])
        ray.set_ydata([h, h, 0, -h])
    return

frac_slider.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(resetax, 'Reset', hovercolor='0.975')
def reset(event):
    frac_slider.reset()
button_reset.on_clicked(reset)

plt.show()