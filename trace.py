
#/usr/bin/env python3
# coding: utf8


import numpy as np
from matplotlib import pyplot as plt

x = np.array([0.8, 3.2, 7.1, 12.6, 19.7, 28.4, 38.7])*0.01
t= np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7])

v=[]

for i in range(len(t)-1):
    v.append((x[i+1]-x[i])/0.1)

#fig, (ax1, ax2) = plt.subplots(1,2)
fig, ax1 = plt.subplots()
ax1.plot(t,x)
ax1.grid(color='grey', linestyle='-', linewidth=0.25)
ax1.set_title("variation temporelle de la position")
ax1.set_xlabel("temps (s)")
ax1.set_ylabel("position (m)")

fig, ax2 = plt.subplots()
ax2.plot(t[:-1],v, '-o')
ax2.grid(color='grey', linestyle='-', linewidth=0.25)
ax2.set_title("variation temporelle de la vitesse")
ax2.set_xlabel("temps (s)")
ax2.set_ylabel("vitesse (m/s)")

fig, ax3 = plt.subplots()
ax3.plot(t[:-1],[1.58]*len(t[:-1]), '-')
ax3.grid(color='grey', linestyle='-', linewidth=0.25)
ax3.set_title("variation temporelle de l'accélération")
ax3.set_xlabel("temps (s)")
ax3.set_ylabel("accélération (m/s^2)")

x=np.linspace(0.8,38.7,100)*0.01
fig, ax4 = plt.subplots()
ax4.plot(x,-2*x**2+0.7*x, '-')
ax4.grid(color='grey', linestyle='-', linewidth=0.25)
ax4.set_title("trajectoire")
ax4.set_xlabel("x (m)")
ax4.set_ylabel("y (m)")

plt.show()
