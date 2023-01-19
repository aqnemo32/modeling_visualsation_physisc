import matplotlib
matplotlib.use('TKAgg') #what does this do

import sys
import math #do i need this
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functions import *

J=1.0
nstep=10000

#input
# sys.argv is the input on the commande line, 
# here is pseudocode.animation.py N T 
# where N is array side length and T is temp (close to 1)
if(len(sys.argv) != 3):
    print ("Usage python ising.animation.py N T")
    sys.exit()

lx=int(sys.argv[1]) 
ly=lx 
kT=float(sys.argv[2]) 

spin=np.zeros((lx,ly),dtype=float)

#initialise spins randomly

for i in range(lx):
    for j in range(ly):
        r=random.random()
        if(r<0.5): spin[i,j]=-1
        if(r>=0.5): spin[i,j]=1
# need to add the Energy Calculation

fig = plt.figure()
im=plt.imshow(spin, animated=True)

#update loop here - for Glauber dynamics

for n in range(nstep):
    # this goes through all of the points in the matrix
    for i in range(lx):
        for j in range(ly):

#select spin randomly
            itrial=np.random.randint(0,lx)
            jtrial=np.random.randint(0,ly)
            # this should flip one spin in the matrix, i think
            spin_new=-spin[itrial,jtrial]

            # do the checking of the new spin and wether half or more the nearest neighbours are the same

            delta_E = E_spin(spin_new, lx, ly) - E_spin(spin, lx, ly)

            if delta_E <= 0: spin = spin_new

            else:
                p = np.exp(-delta_E/kT)
                r = random.random()
                if r <= p: spin = spin_new
                else: spin = spin

# check wether the new spin has at least half of the neighbours alike. 
# if it does no need to calc ∂E as it will for sure be < 0 so new spin matrix can be adopted

# if it does not then you do the metropolis test

#compute delta E eg via function (account for periodic BC)
# delta E is the difference in energy -> ∂E = E_new - E_original
# if ∂E < =0 then we keep the new conformation as it minimises the energy
# If ∂E>0 then the fip happens with a prob of e^(-∂E/k_b t)

#perform metropolis test


          
#occasionally plot or update measurements, eg every 10 sweeps
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
 