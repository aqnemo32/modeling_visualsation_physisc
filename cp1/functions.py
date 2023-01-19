import numpy as np

def E_spin(spin, lx , ly):
    '''spin: numpy array
             spin matrix

       lx, ly: Interger
               Dimensions of the spin array 
    '''
    spin_x = spin
    print(f"{spin = }")
   
    E = 0
    for i in range(lx):
        for j in range(ly):
            E += -spin_x[i, j]*(spin_x[np.mod(i-1,lx),j] + spin_x[np.mod(i+1, lx),j] + spin_x[i,np.mod(j-1,ly)] + spin_x[i,np.mod(j+1,ly)])
            spin_x[i, j] = 0
    print(f"{spin = }")
    # why does the spin array become all zeros, spin_X sould be all zeros but the but spin should not
    return E

# i am sure that there is a way to reduce the number of calculations, but this works for now