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
def rules(spin):
    n = np.zeros((50,50))
    for i in range(50):
        for j in range(50):
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
# now that I have the sum of nearest neighbours i can check the spin matrix and n matrix side by side update all positions simultaneously
    for i in range(50):
            for j in range(50):
                if spin[i,j] == 1:
                    if n[i,j] == 2 or n[i,j] == 3:
                        pass
                    elif n[i,j] > 3 or n[i,j] < 2:
                        spin[i,j] = 0
                else:
                    if n[i,j] == 3:
                        spin[i,j] = 1

    return spin


# def glider(spin_ij):
#     return np.array(([0,0,1], [1,0,1], [0,1,1]), dtype = int) or np.array(([1,0,0], [0,1,1], [1,1,0]), dtype = int)

# def blinker(spin_ij):
#     return np.array(([0,1,0], [0,1,0], [0,1,0]))


def main():
    nstep = 10000

    lx=50 
    ly=lx 

    spin=np.zeros((lx,ly),dtype=int)

    #initialise spins randomly for GoL

    i = random.randint(0, 50)
    j = random.randint(0, 50)

    spin[np.mod(i-1,50):np.mod(i+2,50), np.mod(j-1,50):np.mod(j+2,50)] = np.array(([0,0,1], [1,0,1], [0,1,1]), dtype = int)# or np.array(([1,0,0], [0,1,1], [1,1,0]), dtype = int)

    i = random.randint(0, 50)
    j = random.randint(0, 50)
    print(np.array(([0,1,0], [0,1,0], [0,1,0]), dtype = int).shape)
    spin[np.mod(i-1,50):np.mod(i+2,50), np.mod(j-1,50):np.mod(j+2,50)] = np.array(([0,1,0], [0,1,0], [0,1,0]), dtype = int)


    print(np.sum(spin, axis = (0,1)))
    fig = plt.figure()
    im=plt.imshow(spin, animated=True)

    for n in range(1000):
        spin = rules(spin)
        # spin = np.copy(rules(spin))
        # if(n%10==0):  
    #       update measurements
    # #       dump output
    #     f=open('spins.dat','w')
    #     for i in range(lx):
    #         for j in range(ly):
    #             f.write('%d %d %lf\n'%(i,j,spin[i,j]))
    #     f.close()
    #       show animation
        plt.cla()
        im=plt.imshow(spin, animated=True)
        plt.draw()
        plt.pause(0.0001)
main()
# Set 0 to dead and 1 to alive, as int, to reduce the number of necessary bits