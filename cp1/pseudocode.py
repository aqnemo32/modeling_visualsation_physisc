import matplotlib
matplotlib.use('TKAgg') #what does this do

import sys
import math #do i need this
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    for i in range(lx):
        for j in range(ly):

#select spin randomly
            itrial=np.random.randint(0,lx)
            jtrial=np.random.randint(0,ly)
            spin_new=-spin[itrial,jtrial]

#compute delta E eg via function (account for periodic BC)
# delta E is the difference in energy -> ∂E = E_new - E_original
# if ∂E <0 then we keep the new conformation as it minimises the energy
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
 