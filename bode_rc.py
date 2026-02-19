#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:13:54 2022
Filtre RC
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

f  = np.linspace(1e-3,1e3,1000)
f0 = 1

def H(f):
    return 1 / (1+1j*f/f0)

def G(f):
    return np.abs(H(f))

def phi(f):
    return np.angle(H(f)) * 180/np.pi

plt.figure(1, figsize=(6,4))
sps = (2,1)
ax1 = plt.subplot2grid(sps, (0,0))
ax2 = plt.subplot2grid(sps, (1,0))

ax1.plot(f, np.real(H(f)))
ax2.plot(f, np.imag(H(f)))

ax1.set_ylabel("Partie réelle")
ax1.set_xticklabels([])
ax1.grid()
ax2.set_xlabel("Fréquence ($f/f_0$)")
ax2.set_ylabel("Partie imaginaire")
ax2.grid()
plt.show()
