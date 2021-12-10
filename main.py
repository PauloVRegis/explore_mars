import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import os
import math
import matplotlib.patches as patches

xvalues=np.array([0, 1, 2, 3, 4, 5])
yvalues=np.array([5, 4, 3, 2, 1, 0])
xx, yy = np.meshgrid(xvalues, yvalues)
def sonda_explore(xvalues, yvalues):
    return xvalues, yvalues

print(xx)
print("\n",yy)

plt.plot(xx, yy, marker='.', color='k', linestyle='none')
