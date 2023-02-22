from pylab import *

n = 10
X,Y = np.mgrid[0:n,0:n]
quiver(X,Y), show()