import numpy as np

def valeur_en_eau(m1, m2, T1, T2, Tf):
    # Renvoie la valeur en eau du calorimètre
    # d'après la méthode des mélanges
    # m1 : masse d'eau 1 en g
    # m2 : masse d'eau 2 en g
    # T1 : température de l'eau 1 en K
    # T2 : température de l'eau 2 en K
    # Tf : température après mélange en K
    return - m2 * (Tf - T2) / (Tf - T1) - m1
 
###########
# MESURES #
###########
# eau 1
m1 = 100            # g
dm1 = .1            # g
T1 = 273.15 + 26    # K
dT1 = .1            # K

# eau 2
m2 = 100            # g
dm2 = .1            # g
T2 = 273.15 + 27    # K
dT2 = .1            # K

# après mélange
Tf = 273.15 + 28    # K
dTf = .1            # K

###############
# MONTE-CARLO #
###############
mu = valeur_en_eau(m1, m2, T1, T2, Tf)

N = 10000
m1_sim = np.random.uniform(m1-dm1, m1+dm1, N)
m2_sim = np.random.uniform(m2-dm2, m2+dm2, N)
T1_sim = np.random.uniform(T1-dT1, T1+dT1, N)
T2_sim = np.random.uniform(T2-dT2, T2+dT2, N)
Tf_sim = np.random.uniform(Tf-dTf, Tf+dTf, N)

mu_sim = valeur_en_eau(m1_sim, m2_sim, T1_sim, T2_sim, Tf_sim)

u_mu = np.std(mu_sim, ddof=1)

#############
# AFFICHAGE #
#############
print("Valeur en eau    : {:8.3f} g".format(mu))
print("Incertitude-type : {:8.3f} g".format(u_mu))