
#/usr/bin/env python3
# coding: utf8


import numpy as np
from matplotlib import pyplot as plt

x = [0.8, 3.2, 7.1, 12.6, 19.7, 28.4, 38.7]
t= [0.1,0.2,0.3,0.4,0.5,0.6,0.7]

v=[]

for i in range(len(t)-1):
    v.append((x[i+1]-x[i])/0.1)

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(t,x)
ax1.grid(color='grey', linestyle='-', linewidth=0.25)
ax1.set_title("trajectoire")
ax1.set_xlabel("temps (s)")
ax1.set_ylabel("position (cm)")

ax2.plot(t[:-1],v, '-o')
ax2.grid(color='grey', linestyle='-', linewidth=0.25)
ax2.set_title("variation temporelle de la vitesse")
ax2.set_xlabel("temps (s)")
ax2.set_ylabel("vitesse (cm/s)")

plt.show()
