import numpy as np
import random

def E_spin(spin, lx , ly):
    '''spin: numpy array
             spin matrix

       lx, ly: Interger
               Dimensions of the spin array 
    '''
    spin_x = spin.copy()

   
    E = 0
    for i in range(lx):
        for j in range(ly):
            E += -spin_x[i, j]*(spin_x[np.mod(i-1,lx),j] + spin_x[np.mod(i+1, lx),j] + spin_x[i,np.mod(j-1,ly)] + spin_x[i,np.mod(j+1,ly)])
            spin_x[i, j] = 0

    return E

# i am sure that there is a way to reduce the number of calculations, but this works for now

def metropolis(spin, spin_new, lx, ly, itrial, jtrial, kT):

    nearest_neighbour_sum = spin_new[itrial, jtrial] * (
        spin_new[np.mod(itrial-1,lx),jtrial] +\
                         spin_new[np.mod(itrial+1, lx),jtrial] +\
                                          spin_new[itrial,np.mod(jtrial-1,ly)] +\
                                                             spin_new[itrial,np.mod(jtrial+1,ly)])
    if nearest_neighbour_sum >= 0: 
        return spin_new

    else :
        delta_E = E_spin(spin_new, lx, ly) - E_spin(spin, lx, ly) 
        p = np.exp(-delta_E/kT)
        r = random.random()
        if r <= p: 
            return spin_new
        else: 
            return spin