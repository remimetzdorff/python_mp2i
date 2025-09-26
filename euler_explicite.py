import numpy as np
import matplotlib.pyplot as plt

##########################
# PARAMÈTRES DU CIRCUIT RC
##########################
u0  = 1   # u(0) en volts (CI)
tau = 1 # temps caractéristique en secondes

#############################
# PARAMÈTRES DE LA RÉSOLUTION
#############################
t0 = 0                   # bornes de l'intervalle de résolution
tf = 10                   # en secondes
dt = tau/1e3             # pas de temps en secondes

n  = int((tf-t0)/dt + 1) # nombre de points
t = np.linspace(t0,tf,n) # temps en secondes

############
# SIGNAL GBF
############
E   = 0   # offset en volts
amp = 1   # amplitude en volts
f   = 10   # fréquence en hertz

constant = np.ones(n) * E
square   = amp * np.sign(np.sin(2*np.pi*f*t)) + E
sinus    = amp * np.sin(2*np.pi*f*t) + E
noise    = np.random.normal(0,5,n) # bruit aléatoire
e = constant # signal aux bornes du GBF
# À vous de créer le signal que vous voulez tester...

#################
# MÉTHODE D'EULER
#################
u = np.zeros(len(t))  # préparation du tableau
u[0] = u0             # initialisation en fonction de la CI
for k in range(n-1):  # méthode d'Euler explicite
    u[k+1] = e[k] * dt / tau + u[k] * (1 - dt / tau)
    
ul = [u0]
for k in range(n-1):
    ul.append( e[k] * dt / tau + ul[k] * (1 - dt / tau) )

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.plot(t, e, label="e(t)")
plt.plot(t, u, label="u(t)")

#plt.plot(t, u0 * np.exp(-t/tau))

plt.grid()
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.legend()
plt.show() # pour afficher le graphique