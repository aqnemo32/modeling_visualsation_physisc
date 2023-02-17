import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import convolve


def rules(spin):
    for i in range(50):
        for j in range(50):
            #compute the sum of all the nearest neighbpurs (1 = alive, 0 = dead)
            n = spin[i, np.mod(j+1, 50)] + spin[i, np.mod(j-1, 50)] + spin[np.mod(i+1, 50), j] + spin[np.mod(i-1, 50), j] + spin[np.mod(i+1, 50), np.mod(j+1, 50)] + spin[np.mod(i-1, 50), np.mod(j-1, 50)] + spin[np.mod(i+1, 50), np.mod(j-1, 50)] + spin[np.mod(i-1, 50), np.mod(j+1, 50)]
            if spin[i,j] == 1:
                if n == 2 or n == 3:
                    pass
                elif n > 3 or n < 2:
                    spin[i,j] = 0
            else:
                if n == 3:
                    spin[i,j] = 1
    return spin


nstep = 10000

lx=50 
ly=lx 

spin=np.zeros((lx,ly),dtype=int)

#initialise spins randomly for GoL

for i in range(lx):
    for j in range(ly):
        r=random.random()
        if(r>=0.5): spin[i,j]=1

fig = plt.figure()
im=plt.imshow(spin, animated=True)

for n in range(nstep):
    spin = rules(spin)
    if(n%10==0): 
        print(n)
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

# Set 0 to dead and 1 to alive, as int, to reduce the number of necessary bits