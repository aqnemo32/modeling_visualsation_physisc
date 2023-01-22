import numpy as np
import matplotlib.pyplot as plt

from functions import susceptibility


susc_list = np.zeros(21)

T_list = np.zeros(21)

T = 1.0
for i in range(21):

    a = np.load(f"spin_data/spin_data_50_{T:.3}_G.npy")

    susc_list[i] = susceptibility(a, 50, T)
    T_list[i] = T

    T += 0.1

plt.scatter(T_list, susc_list, marker = 'x',color = 'k', linewidths=0.5)
plt.ylabel("Magnetic Susceptibility")
plt.xlabel("Temperature")
plt.savefig("/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/mag_susc_vs_temp.png")
plt.clf()