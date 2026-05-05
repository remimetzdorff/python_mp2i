import numpy as np

def enthalpie_de_fusion(ml, ms, mu, Tl, Ts, Tf, Tfus, cl, cs):
    # Renvoie l'enthlpie de fusion de l'eau
    # ml : masse d'eau 1 en g
    # ms : masse d'eau 2 en g
    # mu : valeur en eau du calorimètre en g
    # Tl : température de l'eau 1 en K
    # Ts : température de l'eau 2 en K
    # Tfus : température de changement d'état de l'eau en K
    # Tf : température après fonte en K
    # cl : capacité themrique massique de l'eau liquide
    # cs : capacité themrique massique de l'eau solide
    terme1 = -(ml + mu)/ms * cs * (Tf-Tl)
    terme2 = -cs*(Tfus-Ts)
    terme3 = -cl*(Tf-Tfus) 
    return terme1 + terme2 + terme3  
 
###########
# DONNÉES #
###########
cl = 1          # J/K/kg, capacité thermique massique eau liquide
dcl = 0
cs = 1          # J/K/kg, capacité thermique massique eau solide
dcs = 0
Tfus = 273.15   # K
dTfus = 0

###########
# MESURES #
###########
# calorimètre
mu = 100            # g
dmu = .1            # g
# eau liquide
ml = 100            # g
dml = .1            # g
Tl = 273.15 + 26    # K
dTl = .1            # K

# eau solide
ms = 100            # g
dms = .1            # g
Ts = 273.15 + 27    # K
dTs = .1            # K

# après mélange et fonte
Tf = 273.15 + 28    # K
dTf = .1            # K

###############
# MONTE-CARLO #
###############
l_fus = enthalpie_de_fusion(ml, ms, mu, Tl, Ts, Tf, Tfus, cl, cs)

N = 10000
ml_sim = np.random.uniform(ml-dml, ml+dml, N)
ms_sim = np.random.uniform(ms-dms, ms+dms, N)
mu_sim = np.random.uniform(mu-dmu, mu+dmu, N)
Tl_sim = np.random.uniform(Tl-dTl, Tl+dTl, N)
Ts_sim = np.random.uniform(Ts-dTs, Ts+dTs, N)
Tf_sim = np.random.uniform(Tf-dTf, Tf+dTf, N)
Tfus_sim = np.random.uniform(Tfus-dTfus, Tfus+dTfus, N)
cl_sim = np.random.uniform(cl-dcl, cl+dcl, N)
cs_sim = np.random.uniform(cs-dcs, cs+dcs, N)

l_fus_sim = enthalpie_de_fusion(ml_sim, ms_sim, mu_sim, Tl_sim, Ts_sim, Tf_sim, Tfus_sim, cl_sim, cs_sim)

u_l_fus = np.std(l_fus_sim, ddof=1)

#############
# AFFICHAGE #
#############
print("enthalpie massique de fusion : {:10.3f} J/kg".format(l_fus))
print("Incertitude-type             : {:10.3f} J/kg".format(u_l_fus))