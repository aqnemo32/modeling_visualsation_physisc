import matplotlib
matplotlib.use('TKAgg') #what does this do


import random
import numpy as np

def kawazaki(spin, lx, ly, kT):
    '''
    '''

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


            
    return spin


def glauber(spin, lx, ly, kT):

    '''
    '''
    for i in range(lx):
        for j in range(ly):
            #select spin randomly
            itrial=np.random.randint(0,lx)
            jtrial=np.random.randint(0,ly)
            
            spin_new = -spin[itrial,jtrial]

            delta_E = -2*spin_new * (
            spin[np.mod(itrial-1,lx),jtrial] +\
                                spin[np.mod(itrial+1, lx),jtrial] +\
                                                spin[itrial,np.mod(jtrial-1,ly)] +\
                                                                    spin[itrial,np.mod(jtrial+1,ly)])

            if delta_E <= 0:
                spin[itrial, jtrial] = spin_new
            else:
                p = np.exp(-delta_E/kT)
                r = random.random()
                if r <= p: 
                    spin[itrial, jtrial] = spin_new 

    return spin

def susceptibility(M, lx, kT):
    '''
    super_spin: numpy array
                Spin arrays for an Ising model dimension = (numstep-100/10, lx, ly)
    '''
    # M = np.sum(super_spin, axis = (1,2))

    M_avg = np.average(M)

    M_sq = np.square(M)
    M_sq_avg = np.average(M_sq)

    M_avg_sq = np.square(M_avg)

    error_M = np.sqrt((M_sq_avg - M_avg_sq)/(M.shape[0]-1))
    
    susc = 1/((lx**2)*kT) * (M_sq_avg - M_avg_sq)
    # error calc in susceptibility
    c_i = np.zeros(M.shape[0])

    for k in range(M.shape[0]):
        M_removed = np.delete(M,k)

        c_i[k] = 1/(50**2 * kT) * (np.average(np.square(M_removed)) - np.square(np.average(M_removed)))
    error_susc = np.sqrt(np.sum((c_i - susc)**2, axis = 0))

    return susc, error_susc, M_avg, error_M


def energy(spin, lx):
    '''
    '''
    E = 0
    for i in range(lx):
        for j in range(lx):
            E += -spin[i,j] * (
                    spin[np.mod(i-1,lx),j] +spin[i,np.mod(j+1,lx)])
    
    return E