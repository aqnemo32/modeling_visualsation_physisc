import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import time
import sys
from functions import susceptibility, energy

start = time.time()

plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)

# 0, 1,      2,       3,    4,          5,    6,          7,   8
# T, Energy, Error E, Susc, Error Susc, Heat, Error Heat, Mag, Error Mag
data = np.zeros((21,9), dtype = float)

# label = Temperature, Energy, Error Energy, Susceptibility, Error Susceptibility, Heat Capacity, Error Heat Capacity, Magnetisation, Error Magnetisation

def delta_e(E):

    return np.average(np.square(E)) - np.square(np.average(E))

T = 1.0
for i in range(21):

    a = np.load(f"spin_data/spin_data_50_{T:.3}_{sys.argv[1]}.npy")

    data[i,0] = T

    M = np.sum(a, axis = (1,2))


    # susceptibility calculations 
    dummy = susceptibility(M, 50, T)

    data[i,3] = dummy[0]

    data[i,4] = dummy[1]

    data[i,7] = np.absolute(dummy[2])

    data[i,8] = dummy[3]



    # heat capacity calculations
    e_prime = np.zeros(a.shape[0])
    for j in range(a.shape[0]):
        e_prime[j] = energy(a[j, :, :], 50)
    # average E
    data[i,1] = np.average(e_prime)
    # error for E
    data[i,2] = np.sqrt(delta_e(e_prime)/(a.shape[0]-1))
    # Heat Capacity
    data[i,5] = 1/(50**2 * T**2) * (delta_e(e_prime))

    # error calc heat capacity
    c_i = np.zeros(a.shape[0])

    for k in range(a.shape[0]):
        E_removed = np.delete(e_prime, k)


        c_i[k] = 1/(50**2 * T**2) * (delta_e(E_removed))

    data[i,6] = np.sqrt(np.sum((c_i - data[i,5])**2, axis = 0))

    T += 0.1


np.savetxt(f"{sys.argv[1]}_final_data.dat", data, fmt = "%1.5e")
# suscetibility is like the variance of the Magnetisation of the system
# at low temp, boltzmann weight not very big, so system tends to uniform magnetisation
# at high tem
print(f"Run time = {time.time() - start}")
