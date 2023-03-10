# https://github.com/aqnemo32
import matplotlib
matplotlib.use('TKAgg') #what does this do

import sys
import os.path
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from functions import kawazaki, glauber

start = time.time()
nstep = 10000
J = 1.0

#input
# sys.argv is the input on the commande line, 
# here is interface.py N T K/G
# where N is array side length and T is temp
if(len(sys.argv) != 4):
    print ("Usage python interface.py N T K/G")
    sys.exit()

lx=int(sys.argv[1]) 
ly=lx

# to use a bash script to run all the programs in one go I needed to input 
# the temp aa integers as bash does not accept float point,
# input of 10 represents a Temp of 1.0
kT=float(sys.argv[2])/10 

spin=np.zeros((lx,ly),dtype=float)

# create an array to store all the spin data
super_spin = np.zeros((int((nstep-100)/10),lx, ly), dtype = float)

# set the initial spin matrix

# if the previous temp run does exist then tit will load the last frame of the previous temp as the initial spin matrix
# if the previous temp does not exist then a random matrix will be generated

if os.path.exists(f"spin_data/eq_spin_50_{kT-0.1:.3}_{sys.argv[3]}.npy") == True:
    print('1')
    spin = np.load(f"spin_data/eq_spin_50_{kT-0.1:.3}_{sys.argv[3]}.npy")
else:
    print('2')
    for i in range(lx):
        for j in range(ly):
            r=random.random()
            if(r<0.5): spin[i,j]=-1
            if(r>=0.5): spin[i,j]=1

fig = plt.figure()
im=plt.imshow(spin, animated=True)

for n in range(nstep):
# to speed up I would ideally have the if statement outsde the bif for 
# loop, would prevent it checking all the time
    if sys.argv[3] == 'K' or sys.argv[3] == 'k':
        spin = kawazaki(spin, lx, ly, kT)

    elif sys.argv[3] == 'G' or sys.argv[3] == 'g':
        spin = glauber(spin, lx, ly, kT)



    if(n%10==0):
        # print(f"{n}")
        if n > 100: # thats what causing the fist frame to be all zeros, n = 99 is the 10 th sweep but I am ingnoring it
            super_spin[int(n/10) - 10, :, :] = spin

    # #       update measurements
    # #       dump output
        f=open('spins.dat','w')
        for i in range(lx):
            for j in range(ly):
                f.write('%d %d %lf\n'%(i,j,spin[i,j]))
        f.close()
    #       show animation
        plt.cla()
        im=plt.imshow(spin, animated=True)
        plt.draw()
        plt.pause(0.0001)



np.save(f"spin_data/spin_data_{lx}_{kT}_{sys.argv[3]}", super_spin)
np.save(f"spin_data/eq_spin_{lx}_{kT}_{sys.argv[3]}", super_spin[-1,:,:])

end = time.time()
print(f"Done {kT}\nRun Time = {end - start}")
# import subprocess

# msg =  "Welcome,\nThis little interface will allow you to simulate an Ising Model.\nYou may choose between a Kawazaki Algorithm or a Glauber Algorithm\nTo select Kawazaki press k, to select Glauber press g: "
# choice = input(msg)

# if choice == 'g' or choice == 'G':
#     print("You have chose the Glauber Algorithm ")
#     N = int(input("Input the size of the array (as an integer): "))
#     T = float(input("Input the temperature of the system (as a float): "))
#     subprocess.run(f"/Users/achillequarante/Documents/github/modeling_visualsation_physisc/cp1/python3 cp1_glauber.py {N} {T}")
