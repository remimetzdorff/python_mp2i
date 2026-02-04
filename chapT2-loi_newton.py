#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:50:36 2024
chapT2 Illustration expérimentale de la loi de Newton
On plongue un thermomètre froid dans de l'eau chaude
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.loadtxt("data/regime_transitoire_thermique copie.csv",
                  skiprows=1, delimiter=";")

t = data[:,0] - 137
T = data[:,1]
data = pd.Series(T, index=t)
T0 = np.mean(data[-10:0])
Tf = np.mean(data[55:])

t_plot = np.linspace(0,70,1000)

plt.figure()
plt.plot(t,T,".")
plt.plot(t_plot, Tf - (Tf-T0)*np.exp(-t_plot/10))
plt.xlim(-10,60)
plt.grid()
plt.xlabel("Temps (s)")
plt.ylabel("Température (°C)")

#plt.figure()
#plt.plot(data[1:].index,np.log(Tf - data[1:].values))
#plt.grid()
#plt.xlabel("Temps (s)")
#plt.ylabel("Température (°C)")