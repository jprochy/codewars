#!/bin/python36
from copy import deepcopy

testcake = '''
.o.o....
........
....o...
........
.....o..
........
'''.strip()

def sliceToString(slice):
    nsl = []
    for row in slice:
        nsl.append(''.join(row))
    return '\n'.join(nsl)

def testValidSlice(cake, x, y, width, height):
    ns = []
    if x + width > len(cake[0]):
        return False
    if y + height > len(cake):
        return False
    slice = cake[y:y+height]
    for row in slice:
        ns.append(row[x:x+width])
    raisins = 0
    exes = 0
    for row in ns:
        raisins += row.count('o')
        exes  += row.count('x')
    if raisins != 1:
        return False
    if exes > 0:
        return False
    return ns


def doCut(cake, x, y, width, height):
    for i in range(y,y+height):
        for j in range(x,x+width):
            cake[i][j] = 'x'
    return cake


def findFirstTopLeftCorner(cake):
    for i in range(0,len(cake)):
        for j in range(0,len(cake[0])):
            if cake[i][j] != 'x': return [i,j]


def run(cake,size,slices, loop):
    corner = findFirstTopLeftCorner(cake)
    if not corner: return slices
    x = corner[1]
    y = corner[0]
    for width in reversed(range(1,size+1)):
        for height in range(1,size+1):
            if width * height != size: continue
            print(loop)
            slice = testValidSlice(cake, x, y, width, height)
            if not slice: continue
            newSlices = deepcopy(slices)
            newCake = deepcopy(cake)
            newSlices.append(sliceToString(slice))
            print(width, '-', height, sep = ' ')
            print(sliceToString(cake))
            newCake = doCut(newCake, x, y, width, height)
            print(sliceToString(cake), sliceToString(newCake), ' ', sep = '\n')
            r = run(newCake, size, newSlices, loop + 1)
            if r != None: return r
    return None


def cut(cake):
    # 1. preparation
    raisins = cake.count('o')
    arr_cake = [list(line) for line in cake.split('\n')]
    rows = len(arr_cake)
    cols = len(arr_cake[0])
    slice_size = (rows * cols) // raisins

    # 2. Run
    out = run(arr_cake,slice_size,[],1)
    if out == None:
        return []
    else:
        return out

for row in cut(testcake):
    print(row)
    print()


