import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def nearest_neighbours(i,j, spin, lx):
    neighbout_matrix = spin[np.mod(i-1,lx):np.mod(i+2,lx), np.mod(j-1,lx):np.mod(j+2,lx)]
    for val in neighbout_matrix:
        if val == -1:
            return True


def rules(spin, lx, p1, p2, p3):
    for i in range(lx):
        for j in range(lx):
            r = random.random()
            if spin[i,j] == -1:
                if nearest_neighbours(i, j, spin, lx): # If the statement is true it goes forward with it
                    if p1 <= r:
                        spin[i,j] = 0
            elif spin[i,j] == 0:
                if p2 <= r:
                    spin[i,j] = 1
            else:
                if p3 <= r:
                    spin[i,j] = -1
    return spin


    

def main():
    nstep = 10000

    lx = sys.argv[1]
    lx = ly

    p1 = sys.argv[2]
    p2 = sys.argv[3]
    p3 = sys.argv[4]

    spin=np.zeros((lx,ly),dtype=int)
    # initialise spin amtrix with 1 = R, 0 = I, -1 = S
    for i in range(lx):
        for j in range(50):
            r = random.random()
            if r >= 2/3: spin[i,j] = 1
            elif r < 1/3: spin[i,j] = -1

    fig = plt.figure()
    im=plt.imshow(spin, animated=True)

    for n in range(nstep):
        rules(spin, lx, p1, p2, p3)