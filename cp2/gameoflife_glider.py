import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import convolve


# I want to set up a class that can calucalte the velocity and CoM position for a glider
# class glider:
#     def __init__(self, CoM, vel):
#         self.CoM = CoM
#         self.vel = vel

'''
I think the problem is that i update as i go, i must look at the whole thing and update it after I checked every point --> Fixed it pretty sure
'''

def nearest_neighbour(spin, lx):
    n = np.zeros((lx,lx))
    for i in range(lx):
        for j in range(lx):
            #compute the sum of all the nearest neighbpurs (1 = alive, 0 = dead)
            n[i,j] = spin[
                i, np.mod(j+1, 50)] + spin[
                i, np.mod(j-1, 50)] + spin[
                np.mod(i+1, 50), j] + spin[
                np.mod(i-1, 50), j] + spin[
                np.mod(i+1, 50), np.mod(j+1, 50)] + spin[
                np.mod(i-1, 50), np.mod(j-1, 50)] + spin[
                np.mod(i+1, 50), np.mod(j-1, 50)] + spin[
                np.mod(i-1, 50), np.mod(j+1, 50)]
    return n
def rules(spin, n):
# now that I have the sum of nearest neighbours i can check the spin matrix and n matrix side by side update all positions simultaneously
    for i in range(n.shape[0]):
            for j in range(n.shape[0]):
                if spin[i,j] == 1:
                    if n[i,j] == 2 or n[i,j] == 3:
                        pass
                    elif n[i,j] > 3 or n[i,j] < 2:
                        spin[i,j] = 0
                else:
                    if n[i,j] == 3:
                        spin[i,j] = 1

    return spin

def center_of_mass(n):
    i_com_pos = np.sum(n, axis = 0).argmax()
    j_com_pos = np.sum(n, axis = 1).argmax()
    if i_com_pos > 95 and j_com_pos > 95:
        return -1
    else: 
        return np.array((np.sum(n, axis = 0).argmax(), np.sum(n, axis = 1).argmax()))



    # find the spot with most nearest neighbour

def main():
    nstep = 500

    glider_pos = np.zeros((nstep, 2), dtype = int)

    lx=100 
    ly=lx 

    spin=np.zeros((lx,ly),dtype=int)

    #initialise spins to generate a glider at anypoint on the grid

    i = 3
    j = 3

    spin[i-1:i+2, j-1:j+2] = np.array(([0,0,1], [1,0,1], [0,1,1]), dtype = int)# or np.array(([1,0,0], [0,1,1], [1,1,0]), dtype = int)

    # i = random.randint(0, 50)
    # j = random.randint(0, 50)
    # print(np.array(([0,1,0], [0,1,0], [0,1,0]), dtype = int).shape)
    # spin[np.mod(i-1,50):np.mod(i+2,50), np.mod(j-1,50):np.mod(j+2,50)] = np.array(([0,1,0], [0,1,0], [0,1,0]), dtype = int)

    fig = plt.figure()
    im=plt.imshow(spin, animated=True)

    for n in range(nstep):
        sum_n = nearest_neighbour(spin, lx)
        glider_pos[n] = center_of_mass(sum_n)
        spin = rules(spin,sum_n)

    #       show animation
        plt.cla()
        im=plt.imshow(spin, animated=True)
        plt.draw()
        plt.pause(0.0001)
    np.save('glider_com_pos.npy', glider_pos)
main()
# Set 0 to dead and 1 to alive, as int, to reduce the number of necessary bits