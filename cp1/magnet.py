import numpy as np
import matplotlib.pyplot as plt
import time
import sys
from functions import susceptibility, energy

start = time.time()

# 0,  1,     2,    3,          4,    5,          6
# T, Energy, Susc, Error Susc, Heat, Error Heat, Mag 
data = np.zeros((21,7), dtype = float)


def delta_e(E):

    return np.average(np.square(E)) - np.square(np.average(E))

T = 1.0
for i in range(21):

    a = np.load(f"spin_data/spin_data_50_{T:.3}_{sys.argv[1]}.npy")
    print(a[0])
    data[i,0] = T

    M = np.sum(a, axis = (1,2))


    # susceptibility calculations 
    dummy = susceptibility(M, 50, T)

    data[i,2] = dummy[0]

    data[i,3] = dummy[1]

    data[i,6] = np.absolute(dummy[2])

    # heat capacity calculations
    e_prime = np.zeros(a.shape[0])
    for j in range(a.shape[0]):
        e_prime[j] = energy(a[j, :, :], 50)
    
    data[i,1] = np.average(e_prime)

    data[i,4] = 1/(50**2 * T**2) * (delta_e(e_prime))

    c_i = np.zeros(a.shape[0])

    for k in range(a.shape[0]):
        E_removed = e_prime[k:]

        c_i[k] = 1/(50**2 * T**2) * (delta_e(E_removed))

    data[i,5] = np.sqrt(np.sum((c_i - data[i,4])**2, axis = 0))

    T += 0.1


np.savetxt(f"{sys.argv[1]}_final_data.dat", data, fmt = "%1.5e")
# suscetibility is like the variance of the Magnetisation of the system
# at low temp, boltzmann weight not very big, so system tends to uniform magnetisation
# at high tem
plt.errorbar(data[:,0], data[:,2], marker = 'x',color = 'k', yerr= data[:, 3])
plt.ylabel("Magnetic Susceptibility")
plt.xlabel("Temperature")
plt.title(f"Mangetic Susceptibility versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/mag_susc_vs_temp_line_{sys.argv[1]}.png")
plt.clf()

plt.plot(data[:,0],data[:,1], marker = 'x',color = 'k')
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.title(f"Energy versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/energy_vs_temp_line_{sys.argv[1]}.png")
plt.clf()

# plt.plot(data[:,0],data[:,4], marker = 'x',color = 'k')
plt.errorbar(data[:,0],data[:,4], marker = 'x',color = 'k', yerr=data[:, 5])
plt.xlabel("Temperature")
plt.ylabel("Heat Capacity")
plt.title(f"Heat Capacity versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/heat_vs_temp_line_{sys.argv[1]}.png")
plt.clf()


plt.plot(data[:,0],data[:,6], marker = 'x',color = 'k')
plt.xlabel("Temperature")
plt.ylabel("Magnetisation")
plt.title(f"Magnetisation versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/magnetisation_vs_temp_line_{{sys.argv[1]}}.png")
plt.clf()
print(f"Run time = {time.time() - start}")
