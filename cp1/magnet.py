import numpy as np
import matplotlib.pyplot as plt
import time

from functions import susceptibility, energy

start = time.time()

# 0,  1,     2,    3,          4,    5,          6
# T, Energy, Susc, Error Susc, Heat, Error Heat, Mag 
data = np.zeros((21,7), dtype = float)


T = 1.0
for i in range(21):

    a = np.load(f"spin_data/spin_data_50_{T:.3}_G.npy")[1:, :, :]

    data[i,0] = T

    M = np.sum(a, axis = (1,2))


    
    dummy = susceptibility(M, 50, T)

    data[i,2] = dummy[0]

    data[i,3] = dummy[1]

    data[i,6] = np.absolute(dummy[2])


    e_prime = np.zeros(a.shape[0])
    for j in range(a.shape[0]):
        e_prime[j] = energy(a[j, :, :], 50)
    
    data[i,1] = np.average(e_prime)

    E_sq_avg = np.average(e_prime**2)

    E_avg_sq = np.square(data[i,1])
    delta_e = E_sq_avg - E_avg_sq
    data[i,4] = 1/(50**2 * T**2) * (delta_e)

    data[i,5] = np.sqrt(delta_e/a.shape[0]) * np.sqrt(2/2500)

    T += 0.1


np.savetxt("glauber_final_data.dat", data, fmt = "%1.5e")
# suscetibility is like the variance of the Magnetisation of the system
# at low temp, boltzmann weight not very big, so system tends to uniform magnetisation
# at high tem
plt.errorbar(data[:,0], data[:,2], marker = 'x',color = 'k', yerr= data[:, 3])
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
plt.errorbar(data[:,0],data[:,4], marker = 'x',color = 'k', yerr=data[:, 5])
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
