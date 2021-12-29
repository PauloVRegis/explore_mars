import sys
import os
import math

x1, y1 = input().split()
x1, y1 = int(x1), int(y1)
x, y, direct = input().split()
x, y = int(x), int(y)
mov = input()
x2, y2, direct2 = input().split()
x2, y2 = int(x2), int(y2)
mov2 = input()
lst = []

def check(x, y, x2, y2, x1, y1):
    if x < 0 or x > x1 or y < 0 or y > y1 or x2 < 0 or x2 > x1 or y2 < 0 or y2 > y1:
        return False
    else:
        return True
def probe1(x, y, direct, mov, x1, y1):
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
    if check(x, y, x2, y2, x1, y1):
        print(x, y, direct)
    else:
        print('You are out of the Mars!')
        sys.exit()


def probe2(direct2, x2, y2, mov2, x1, y1):
    for j in range(len(mov2)):
        if mov2[j] == 'L':
            if direct2 == 'N':
                direct2 = 'W'
            elif direct2 == 'S':
                direct2 = 'E'
            elif direct2 == 'E':
                direct2 = 'N'
            elif direct2 == 'W':
                direct2 = 'S'
        elif mov2[j] == 'R':
            if direct2 == 'N':
                direct2 = 'E'
            elif direct2 == 'S':
                direct2 = 'W'
            elif direct2 == 'E':
                direct2 = 'S'
            elif direct2 == 'W':
                direct2 = 'N'
        elif mov2[j] == 'M':
            if direct2 == 'N':
                y2 += 1
            elif direct2 == 'S':
                y2 -= 1
            elif direct2 == 'E':
                x2 += 1
            elif direct2 == 'W':
                x2 -= 1
    if check(x, y, x2, y2, x1, y1):
        print(x2, y2, direct2)
    else:
        print('You are out of the Mars!')
        sys.exit()

def main():
    probe1(x, y, direct, mov, x1, y1)
    probe2(direct2, x2, y2, mov2, x1, y1)
    check(x, y, x2, y2, x1, y1)

if __name__== "__main__":
    main()


