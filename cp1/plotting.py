import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
import sys


plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)

data = np.loadtxt(f"{sys.argv[1]}_final_data.dat")

plt.errorbar(data[:,0], data[:,3], marker = 'x',color = 'k', yerr= data[:, 4], barsabove=True, capsize = 2.0, linewidth = 0.5, elinewidth = 1.0, linestyle = '--')
plt.ylabel("Magnetic Susceptibility")
plt.xlabel("Temperature")
plt.title(f"Mangetic Susceptibility versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/mag_susc_vs_temp_{sys.argv[1]}.png")
plt.clf()

plt.errorbar(data[:,0],data[:,1], marker = 'x',color = 'k', yerr= data[:, 2], barsabove=True, capsize = 2.0, linewidth = 0.5, elinewidth = 1.0, linestyle = '--')
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.title(f"Energy versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/energy_vs_temp_{sys.argv[1]}.png")
plt.clf()

# plt.plot(data[:,0],data[:,4], marker = 'x',color = 'k')
plt.errorbar(data[:,0],data[:,5], marker = 'x',color = 'k', yerr=data[:, 6], barsabove=True, capsize = 2.0, linewidth = 0.5, elinewidth = 1.0, linestyle = '--')
plt.xlabel("Temperature")
plt.ylabel("Heat Capacity")
plt.title(f"Heat Capacity versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/heat_vs_temp_{sys.argv[1]}.png")
plt.clf()


plt.errorbar(data[:,0],data[:,7], marker = 'x',color = 'k', yerr = data[:,8], barsabove = True, capsize = 2.0, linewidth = 0.5, elinewidth = 1.0, linestyle = '--')
plt.xlabel("Temperature")
plt.ylabel("Magnetisation")
plt.title(f"Magnetisation versus Temperature ({sys.argv[1]})")
plt.savefig(f"/Users/achillequarante/Desktop/mod_vis/cp1/cp1_graphs/magnetisation_vs_temp_{sys.argv[1]}.png")
plt.clf()