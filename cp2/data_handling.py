import numpy as np
import matplotlib.pyplot as plt
import os


files = os.listdir('output-activesite/')
print(files)

file_1 = np.load(f"output-activesite/{files[0]}")
file_2 = np.load(f"output-activesite/{files[2]}")
file_2 = file_2[file_2 > 0]
print(file_1[file_1 > 0].shape)

# plt.plot(np.linspace(0, 5000, 5000)[::50], file_1[::50])
plt.scatter(np.arange(0, file_2.shape[0]), file_2, color = 'k')
plt.show()