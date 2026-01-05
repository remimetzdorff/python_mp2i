#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 10:00:00 2022
Battement
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,0.2,20000)

f1 = 440
f2 = 440

s1 = np.cos(2*np.pi*f1*t)
s2 = np.cos(2*np.pi*f2*t)

plt.plot(t, s1, label="$s_1$")
plt.plot(t, s2, label="$s_2$")
plt.plot(t, s1+s2, label="$s_1 + s_2$")

plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()