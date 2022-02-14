import matplotlib.pylab as plt
import numpy as np

f, a = plt.subplots()
x = np.linspace(1, 10, 100)
y = np.sin(x)
a.plot(x, y)
pos = []
plt.show()


def onclick(event):
    pos.append([event.xdata, event.ydata])


f.canvas.mpl_connect('button_press_event', onclick)
f.show()