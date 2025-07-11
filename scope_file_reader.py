#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 14:57:40 2025
Scope file reader
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("scope_0.csv", delimiter=',')
t    = data[2:,0]    # temps en secondes
ch1  = data[2:,1]    # tension mesurée sur le canal 1, en volts
ch2  = data[2:,2]    # tension mesurée sur la canal 2, en volts

plt.figure()
plt.plot(t, ch1, label="CH1")
plt.plot(t, ch2, label="CH2")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.show()
