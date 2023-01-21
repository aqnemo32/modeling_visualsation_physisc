# https://github.com/aqnemo32
import matplotlib
matplotlib.use('TKAgg') #what does this do

import sys
import math #do i need this
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functions import *

nstep = 10000
J = 1.0

#input
# sys.argv is the input on the commande line, 
# here is pseudocode.animation.py N T 
# where N is array side length and T is temp (close to 1)
if(len(sys.argv) != 4):
    print ("Usage python ising.animation.py N T K/G")
    sys.exit()

lx=int(sys.argv[1]) 
ly=lx 
kT=float(sys.argv[2]) 

spin=np.zeros((lx,ly),dtype=float)

#initialise spins randomly
# print('i')
for i in range(lx):
    # print(f"j{i}")
    for j in range(ly):
        r=random.random()
        if(r<0.5): spin[i,j]=-1
        if(r>=0.5): spin[i,j]=1
# need to add the Energy Calculation

fig = plt.figure()
im=plt.imshow(spin, animated=True)

for n in range(nstep):

    if sys.argv[3] == 'K' or sys.argv[3] == 'k':
        spin = kawazaki(spin, lx, ly, kT)

    elif sys.argv[3] == 'G' or sys.argv[3] == 'g':
        spin = glauber(spin, lx, ly, kT)

    if(n%10==0): 
    #       update measurements
    #       dump output
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
# import subprocess

# msg =  "Welcome,\nThis little interface will allow you to simulate an Ising Model.\nYou may choose between a Kawazaki Algorithm or a Glauber Algorithm\nTo select Kawazaki press k, to select Glauber press g: "
# choice = input(msg)

# if choice == 'g' or choice == 'G':
#     print("You have chose the Glauber Algorithm ")
#     N = int(input("Input the size of the array (as an integer): "))
#     T = float(input("Input the temperature of the system (as a float): "))
#     subprocess.run(f"/Users/achillequarante/Documents/github/modeling_visualsation_physisc/cp1/python3 cp1_glauber.py {N} {T}")