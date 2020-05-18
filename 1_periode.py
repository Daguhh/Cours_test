#/usr/bin/env python3
# coding: utf8


import numpy as np
from matplotlib import pyplot as plt

plt.ion()

# données
v = 8.5 # m/s
d = 3 # m

# convertion km/h => m/s
v = v/3.6

# pulsation
w = v/d


t = np.linspace(0, 20, 300) # secondes

x = v/w*np.cos(w*t) + d -v/w
y = v/w*np.sin(w*t)


fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(3*np.cos(np.linspace(0,2*np.pi,50)),
         3*np.sin(np.linspace(0,2*np.pi,50)))
ax1.set(xlabel='x', ylabel='y', title='Trajectoire')

x_plot, = ax2.plot([],[], label='x')
y_plot, = ax2.plot([],[], label='y')
pos_plot, = ax1.plot(x[0],y[0], 'o', label='pos')
ax2.set(xlabel='temps', ylabel='valeur des coordonnées',  title='Trajectoire')
ax2.set_autoscaley_on(True)
plt.legend()

for i in range(len(t)):
    x_plot.set_xdata(t[:i])
    x_plot.set_ydata(x[:i])
    y_plot.set_xdata(t[:i])
    y_plot.set_ydata(y[:i])
    pos_plot.set_xdata(x[i])
    pos_plot.set_ydata(y[i])

    ax2.relim()
    ax2.autoscale_view()

    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.001)

plt.show()




