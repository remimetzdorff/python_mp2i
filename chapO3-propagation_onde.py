#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 13:06:43 2023
Propagation d'une onde sinusoidale
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fps   = 25
duration = 10

f     = 1
wl    = 2
omega = 2*np.pi * f
k     = 2*np.pi / wl

xe = 0
xr = 5
xmin = -1
xmax = 10
x = np.linspace(xmin, xmax, 200)

fig = plt.figure(figsize=(8,8))
sps = (2,2)
ax1 = plt.subplot2grid(sps, (0,0), colspan=2)
ax2 = plt.subplot2grid(sps, (1,0))
ax3 = plt.subplot2grid(sps, (1,1))

ax1.set_xlim(xmin, xmax)
ax1.set_ylim(-1.1,1.1)

emetteur,  = ax1.plot([xe], [0], "ok")
recepteur, = ax1.plot([xr], [0], "ok")
onde,      = ax1.plot([], [], "C0", alpha=.25)

def animate(i):
    t = i / fps
    y = np.cos(omega*t - k*x)
    onde.set_data(x, y)
    return

ani = animation.FuncAnimation(fig, animate, frames=int(10*fps), interval=1e3/fps)
plt.tight_layout()
plt.show()