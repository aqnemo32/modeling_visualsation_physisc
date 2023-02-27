import numpy as np
import matplotlib.pyplot as plt
import os


files = os.listdir('output-activesite/')
sim_time = np.zeros(len(files))

for i, file in enumerate(files):
    sim_time[i] = np.load(f"output-activesite/{file}").shape[0]

plt.hist(sim_time[sim_time < 3000], bins = 100)
plt.savefig('gol_sim_time_hist.png', format = 'png')
# file_1 = np.load(f"output-activesite/{files[0]}")
# file_2 = np.load(f"output-activesite/{files[2]}")
# file_2 = file_2[file_2 > 0]
# print(file_1[file_1 > 0].shape)

# # plt.plot(np.linspace(0, 5000, 5000)[::50], file_1[::50])
# plt.scatter(np.arange(0, file_2.shape[0]), file_2, color = 'k')
# plt.show()
