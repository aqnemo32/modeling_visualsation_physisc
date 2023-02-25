import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# REDOOO
def nearest_neighbours(i,j, spin, lx):
    # wrote this to check if when person is Susceptible f there is an in
    neighbour_matrix = np.zeros((3,3), dtype=int)

    for k in range(3):
        for l in range(3):
            neighbour_matrix[k,l] = spin[np.mod(i-k,lx), np.mod(j-l, lx)]
    neighbour_matrix = neighbour_matrix.flatten() * np.array(([1,1,1,1,0,1,1,1,1]), dtype=int)
    for k in range(9):
        if neighbour_matrix[k] == 0:
            return True
        else: return False


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
    nstep = 1000

    lx = int(sys.argv[1])
    ly = lx

    p1 = float(sys.argv[2])
    p2 = float(sys.argv[3])
    p3 = float(sys.argv[4])

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
        spin = rules(spin, lx, p1, p2, p3)

        if n%10 == 0:
            print(n)
            plt.cla()
            im=plt.imshow(spin, animated=True)
            plt.draw()
            plt.pause(0.0001)

main()