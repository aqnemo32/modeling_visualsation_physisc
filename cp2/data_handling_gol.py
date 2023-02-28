import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams

plt.style.use('ggplot')
rcParams['font.family'] = 'serif'
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.dpi'] = 250
rcParams['lines.linewidth'] = 0.5
rcParams['lines.markersize'] = 1.5
rcParams['errorbar.capsize'] = 1.5
rcParams['figure.constrained_layout.use'] = True
rcParams['figure.figsize'] = [1.61803398875 * 6, 6]

files = os.listdir('output-activesite/')
sim_time = np.zeros(len(files))

for i, file in enumerate(files):
    sim_time[i] = np.load(f"output-activesite/{file}").shape[0]

plt.hist(sim_time[sim_time < 5000], bins = 85)
plt.savefig('gol_sim_time_hist.png', format = 'png')
plt.clf()
# file_1 = np.load(f"output-activesite/{files[0]}")
# file_2 = np.load(f"output-activesite/{files[2]}")
# file_2 = file_2[file_2 > 0]
# print(file_1[file_1 > 0].shape)

# # plt.plot(np.linspace(0, 5000, 5000)[::50], file_1[::50])
# plt.scatter(np.arange(0, file_2.shape[0]), file_2, color = 'k')
# plt.show()

glider_pos = np.load('glider_com_pos.npy')[::4]
print(glider_pos[:10])
print(glider_pos[:10:4])
t = np.linspace(0, glider_pos.shape[0]-1, glider_pos.shape[0], dtype = int)

x_pos = glider_pos[:,0]

y_pos = glider_pos[:,1]


plt.scatter(t, x_pos)
plt.show()
