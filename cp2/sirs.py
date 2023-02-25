import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# REDOOO
def nearest_neighbours(i,j, spin, lx):
    # wrote this to check if when person is Susceptible f there is an in
    neighbour_matrix = np.zeros(4)

    neighbour_matrix[0] = spin[np.mod(i-1,lx),j]
    neighbour_matrix[1] = spin[np.mod(i+1,lx),j]
    neighbour_matrix[2] = spin[i,np.mod(j-1,lx)]
    neighbour_matrix[3] = spin[i,np.mod(j+1,lx)]

    for k in neighbour_matrix:
        if k == 0:
            return True
        else: return False


def rules(spin, lx, p1, p2, p3):
    for i in range(lx):
        for j in range(lx):

            if spin[i,j] == -1:
                if nearest_neighbours(i, j, spin, lx): # If the statement is true it goes forward with it
                    r = random.random()
                    if p1 <= r:
                        spin[i,j] = 0
            elif spin[i,j] == 0:
                r = random.random()
                if p2 <= r:
                    spin[i,j] = 1
            else:
                r = random.random()
                if p3 <= r:
                    spin[i,j] = -1
    return spin




def main():
    nstep = 1000

    lx = int(sys.argv[1])
    ly = lx
    #  p1 is the probability that S->I
    p1 = float(sys.argv[2])
    #  p2 is the probability that I->R
    p2 = float(sys.argv[3])
    #  p3 is the probability that R->S
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

        # if n%10 == 0:
        #     print
        plt.cla()
        im=plt.imshow(spin, animated=True)
        plt.draw()
        plt.pause(0.0001)
        print(np.sum(spin, axis = (0,1)))

main()