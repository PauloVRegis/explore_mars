#import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import sys
import os
import math

x1, y1 = input().split()
x1, y1 = int(x1), int(y1)
x, y, direct = input().split()
x, y = int(x), int(y)
mov = input()
lst = []

def check(x, y, x1, y1):
    if x < 0 or x > x1 or y < 0 or y > y1:
        return False
    else:
        return True


if __name__== "__main__":
    # check(x,y,direct)
    for i in range(len(mov)):
        if mov[i] == 'L':
            if direct == 'N':
                direct = 'W'
            elif direct == 'S':
                direct = 'E'
            elif direct == 'E':
                direct = 'N'
            elif direct == 'W':
                direct = 'S'
        elif mov[i] == 'R':
            if direct == 'N':
                direct = 'E'
            elif direct == 'S':
                direct = 'W'
            elif direct == 'E':
                direct = 'S'
            elif direct == 'W':
                direct = 'N'
        elif mov[i] == 'M':
            if direct == 'N':
                y += 1
            elif direct == 'S':
                y -= 1
            elif direct == 'E':
                x += 1
            elif direct == 'W':
                x -= 1
if check(x, y, x1, y1):
                # lst.append(x), lst.append(y), lst.append(direct)
    print(x, y, direct)
else:
    print('You are out of the Mars!')
    sys.exit()

