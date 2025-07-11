#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:12:43 2022
Algorithme de type Monte-Carlo pour la composition des incertitudes
@author: remimetzdorff
"""
import numpy as np

def r(u,i):    # loi d'Ohm
    return u/i
# MESURES
u   = 15.4     # tension en volts
d_u =  0.5     # incertitude sur u en volts
i   = 242.2e-3 # intensité en ampère
d_i =   0.2e-3 # incertitude sur i en ampère

# MONTE-CARLO : simulation de 10000 mesures
u_sim = np.random.uniform(u-d_u, u+d_u, 10000)
i_sim = np.random.uniform(i-d_i, i+d_i, 10000)
r_sim = r(u_sim, i_sim)
print("Valeur           :", r(u,i))
print("Incertitude-type :", np.std(r_sim, ddof=1))