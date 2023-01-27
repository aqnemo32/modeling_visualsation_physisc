import numpy as np
import matplotlib.pyplot as plt
import time

from functions import susceptibility, energy

start = time.time()
susc_list = np.zeros(21)

T_list = np.zeros(21)

energy_list = np.zeros(21)

T = 1.0
for i in range(21):

    a = np.load(f"spin_data/spin_data_50_{T:.3}_G.npy")
    
    e_prime = np.zeros(990)
    for j in range(a.shape[0]):
        e_prime[j] = energy(a[j, :, :], 50)

    # print(np.average(e_prime))
    energy_list[i] = np.average(e_prime)

    susc_list[i] = susceptibility(a, 50, T)
    T_list[i] = T

    T += 0.1
# suscetibility is like the variance of the Magnetisation of the system
# at low temp, boltzmann weight not very big, so system tends to uniform magnetisation
# at high tem
plt.plot(T_list, susc_list, marker = 'x',color = 'k')
plt.ylabel("Magnetic Susceptibility")
plt.xlabel("Temperature")
plt.show()
# "/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/mag_susc_vs_temp_line.png"
plt.clf()

plt.plot(T_list, energy_list, marker = 'x',color = 'k')
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.show()
plt.clf()

print(f"Run time = {time.time() - start}")