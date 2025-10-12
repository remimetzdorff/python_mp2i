import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import odeint

##############
# PARAMÈTRES #
##############
L = 1e-3       # inductance (H)
C = 1e-6       # capacité (F)
E = 1          # amplitude de l’échelon (V)
omega0 = 1 / np.sqrt(L * C)  # pulsation propre (rad/s)

t = np.linspace(0, 0.01, 10000)


##############
# RÉSOLUTION #
##############
def rlc(V, t, Q):
    u, du = V
    ddu = omega0**2*E - omega0/Q*du - omega0**2*u
    return [du, ddu]

def compute_u(Q):
    V0 = [0, 0] # i(0) = 0, u(0) = 0
    V = odeint(rlc, V0, t, args=(Q,))
    u = V[:, 0]
    return u

############################
# REPRÉSENTATION GRAPHIQUE #
############################
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

initial_logQ = 0  # log10(Q) = 0 soit Q = 1
initial_Q = 10 ** initial_logQ
u = compute_u(initial_Q)
[line] = ax.plot(t * 1e3, u, "C1")

ax.set_xlabel('Temps (ms)')
ax.set_ylabel('Tension aux bornes du condensateur (V)')
ax.set_title(f'Réponse à un échelon (Q = {initial_Q:.2f})')
ax.grid(True)
ax.set_ylim(-0.2, 2)
ax.plot([-np.max(t)/10*1e3, 0, 0, np.max(t)*1e3], [0,0,E,E]) # échelon

axcolor = 'lightgoldenrodyellow'
ax_q = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider_logq = Slider(ax_q, "$\log_{10}(Q)$", -2, 2, valinit=initial_logQ, valstep=0.01)

def update(val):
    logQ = slider_logq.val
    Q = 10 ** logQ
    u = compute_u(Q)
    line.set_ydata(u)
    ax.set_title(f'Réponse à un échelon (Q = {Q:.2f})')
    fig.canvas.draw_idle()

slider_logq.on_changed(update)

plt.show()

