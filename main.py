import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import os
import math
import matplotlib.patches as patches
from matplotlib.pyplot import cm
from numpy.lib.index_tricks import IndexExpression

x1, y1 = 5, 5
nx, ny, direct = input().split()
x = np.arange(0, 6)
y = np.arange(5, -1 , -1)
xx, yy = np.meshgrid(x, y)
mov = input()
lst = []


def move(x, y, direct):
    if direct == 'N':
        return x, y + 1
    elif direct == 'E':
        return x + 1, y
    elif direct == 'S':
        return x, y - 1
    else:
        return x - 1, y

def check(x, y, x1, y1):
    if x < 0 or x > x1 or y < 0 or y > y1:
        return False
    else:
        return True

def explore(nx,ny,x,y,mov,direct):
    if move(x, y, nx, ny, mov, direct):
        x, y = move(x, y, nx, ny, direct)
        lst.append((x, y, mov))
        return x, y, direct
    else:
        return x, y, direct
def main():
    for i in range(len(mov)):
        x, y = explore(int(nx), int(ny), x, y, mov[i], direct)
    print(x, y)
    print(lst)
    plt.plot(x, y)
    plt.show()



# xx, yy = np.meshgrid(np.arange(0, 6), np.array([5, 4, 3, 2, 1, 0]), sparse=True)
# xx1, yy1 = np.meshgrid(xx, yy, indexing='xy')
# plt.plot(xx1, yy1, marker='.', color='k', linestyle='None')

if __name__== "__main__":
    main()