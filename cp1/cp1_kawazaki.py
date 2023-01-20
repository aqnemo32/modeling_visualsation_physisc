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

#update loop here - for Glauber dynamics

for n in range(nstep):
    for i in range(lx):
        for j in range(ly):

            #select spin randomly
            itrial_1=np.random.randint(0,lx)
            jtrial_1=np.random.randint(0,ly)
            spin_1 = spin[itrial_1,jtrial_1]

            itrial_2=np.random.randint(0,lx)
            jtrial_2=np.random.randint(0,ly)
            spin_2 = spin[itrial_2,jtrial_2]

            if spin_1 != spin_2:

                delta_E_2 = -2*spin_2 * (
                    spin[np.mod(itrial_1-1,lx),jtrial_1] +\
                                spin[np.mod(itrial_1+1, lx),jtrial_1] +\
                                                spin[itrial_1,np.mod(jtrial_1-1,ly)] +\
                                                                    spin[itrial_1,np.mod(jtrial_1+1,ly)])
                delta_E_1 = -2*spin_1 * (
                    spin[np.mod(itrial_2-1,lx),jtrial_2] +\
                                spin[np.mod(itrial_2+1, lx),jtrial_2] +\
                                                spin[itrial_2,np.mod(jtrial_2-1,ly)] +\
                                                                    spin[itrial_2,np.mod(jtrial_2+1,ly)])
                
                delta_E = delta_E_1 + delta_E_2

                if delta_E <= 0:
                    spin[itrial_1, jtrial_1] = spin_2
                    spin[itrial_2, jtrial_2] = spin_1

                else:
                    p = np.exp(-delta_E/kT)
                    r = random.random()
                    if r <= p:
                        spin[itrial_1, jtrial_1] = spin_2
                        spin[itrial_2, jtrial_2] = spin_1
# check wether the new spin has at least half of the neighbours alike. 
# if it does no need to calc ∂E as it will for sure be < 0 so new spin matrix can be adopted

# if it does not then you do the metropolis test

#compute delta E eg via function (account for periodic BC)
# delta E is the difference in energy -> ∂E = E_new - E_original
# if ∂E < =0 then we keep the new conformation as it minimises the energy
# If ∂E>0 then the fip happens with a prob of e^(-∂E/k_b t)




          
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
 