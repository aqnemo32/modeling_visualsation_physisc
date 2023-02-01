import numpy as np
import matplotlib.pyplot as plt
import time

from functions import susceptibility, energy

start = time.time()


# T, Energy, Susc, Error Susc, Heat, Error Heat, Mag 
data = np.zeros((21,7), dtype = float)


T = 1.0
for i in range(21):

    a = np.load(f"spin_data/spin_data_50_{T:.3}_G.npy")

    data[i,0] = T

    M = np.sum(a, axis = (1,2))

    
    dummy = susceptibility(M, 50, T)

    data[i,2] = dummy[0]

    data[i,3] = dummy[1]

    data[i,6] = np.absolute(dummy[2])


    e_prime = np.zeros(990)
    for j in range(a.shape[0]):
        e_prime[j] = energy(a[j, :, :], 50)

    # print(np.average(e_prime))
    data[i,1] = np.average(e_prime)

    E_sq = e_prime**2

    data[i,4] = 1/(50**2 * T**2) * (np.average(E_sq) - np.square(data[i,1]))

    data[1,5] = np.std(E_sq) + 2*np.std(e_prime)

    T += 0.1


np.savetxt("glauber_final_data.dat", data, fmt = "%1.5e")
# suscetibility is like the variance of the Magnetisation of the system
# at low temp, boltzmann weight not very big, so system tends to uniform magnetisation
# at high tem
plt.plot(data[:,0], data[:,2], marker = 'x',color = 'k')
plt.ylabel("Magnetic Susceptibility")
plt.xlabel("Temperature")
plt.title("Mangetic Susceptibility versus Temperature (Glauber)")
plt.savefig("/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/mag_susc_vs_temp_line.png")
plt.clf()

plt.plot(data[:,0],data[:,1], marker = 'x',color = 'k')
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.title("Energy versus Temperature (Glauber)")
plt.savefig("/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/energy_vs_temp_line.png")
plt.clf()

# plt.plot(data[:,0],data[:,4], marker = 'x',color = 'k')
plt.errorbar(data[:,0],data[:,4], marker = 'x',color = 'k')
plt.xlabel("Temperature")
plt.ylabel("Heat Capacity")
plt.title("Heat Capacity versus Temperature (Glauber)")
plt.savefig("/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/heat_vs_temp_line.png")
plt.clf()


plt.plot(data[:,0],data[:,6], marker = 'x',color = 'k')
plt.xlabel("Temperature")
plt.ylabel("Magnetisation")
plt.title("Magnetisation versus Temperature (Glauber)")
plt.savefig("/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/magnetisation_vs_temp_line.png")
plt.clf()
print(f"Run time = {time.time() - start}")
