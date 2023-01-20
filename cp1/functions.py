import numpy as np
import random

# def E_spin(spin, lx , ly):
#     '''spin: numpy array
#              spin matrix

#        lx, ly: Interger
#                Dimensions of the spin array 
#     '''
#     spin_x = spin.copy()

   
#     E = 0
#     for i in range(lx):
#         for j in range(ly):
#             E += -spin_x[i, j]*(spin_x[np.mod(i-1,lx),j] + spin_x[np.mod(i+1, lx),j] + spin_x[i,np.mod(j-1,ly)] + spin_x[i,np.mod(j+1,ly)])
#             spin_x[i, j] = 0

#     return E

# i am sure that there is a way to reduce the number of calculations, but this works for now

# def metropolis(spin, spin_new, lx, ly, itrial, jtrial, kT):

#     delta_E = -2*spin_new * (
#         spin[np.mod(itrial-1,lx),jtrial] +\
#                          spin[np.mod(itrial+1, lx),jtrial] +\
#                                           spin[itrial,np.mod(jtrial-1,ly)] +\
#                                                              spin[itrial,np.mod(jtrial+1,ly)])


#     else :
#         p = np.exp(-delta_E/kT)
#         r = random.random()
#         if r <= p: 
#             spin[itrial, jtrial] = spin_new 
#             return spin
#         else: 
#             return spin