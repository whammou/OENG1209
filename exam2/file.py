import numpy as np
import pylab as pyl

x = np.linspace(-5, 5, num=20)
y = np.sqrt(x)

pyl.plot(x, y)
pyl.show()
