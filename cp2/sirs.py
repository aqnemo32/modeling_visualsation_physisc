import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rules(spin, lx):
    for i in range(lx):
        for j in range(lx):
            if spin[i,j] == -1:
                
    

def main():

    lx = 50
    lx = ly
    spin=np.zeros((lx,ly),dtype=int)

    # initialise spin amtrix with 1 = R, 0 = I, -1 = S
    for i in range(lx):
        for j in range(50):
            r = random.random()
            if r >= 2/3: spin[i,j] = 1
            elif r < 1/3: spin[i,j] = -1