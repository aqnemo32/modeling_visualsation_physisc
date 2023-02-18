import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# The random initialisation Game of Life


'''
I think the problem is that i update as i go, i must look at the whole thing and update it after I checked every point --> Fixed it pretty sure
'''
def rules(spin):
    n = np.zeros((50,50))
    for i in range(50):
        for j in range(50):
            #compute the sum of all the nearest neighbpurs (1 = alive, 0 = dead)
            n[i,j] = spin[
                i, np.mod(j+1, 50)] + spin[
                i, np.mod(j-1, 50)] + spin[
                np.mod(i+1, 50), j] + spin[
                np.mod(i-1, 50), j] + spin[
                np.mod(i+1, 50), np.mod(j+1, 50)] + spin[
                np.mod(i-1, 50), np.mod(j-1, 50)] + spin[
                np.mod(i+1, 50), np.mod(j-1, 50)] + spin[
                np.mod(i-1, 50), np.mod(j+1, 50)]
# now that I have the sum of nearest neighbours i can check the spin matrix and n matrix side by side update all positions simultaneously
    for i in range(50):
            for j in range(50):
                if spin[i,j] == 1:
                    if n[i,j] == 2 or n[i,j] == 3:
                        pass
                    elif n[i,j] > 3 or n[i,j] < 2:
                        spin[i,j] = 0
                else:
                    if n[i,j] == 3:
                        spin[i,j] = 1

    return spin



def main():
    nstep = 5000

    lx=50 
    ly=lx 

    activesites = np.zeros(nstep)

    spin=np.zeros((lx,ly),dtype=int)

    #initialise spins randomly for GoL 
    for i in range(lx):
        for j in range(ly):
            r=random.random()
            if(r>=0.5): spin[i,j]=1

    print(np.sum(spin, axis = (0,1)))
    
    fig = plt.figure()
    im=plt.imshow(spin, animated=True)

    for n in range(nstep):
        spin = rules(spin)
        activesites[n] = np.sum(spin, axis = (0,1))
        plt.cla()
        im=plt.imshow(spin, animated=True)
        plt.draw()
        plt.pause(0.0001)
        if n > 200:
            conv_test = np.std(activesites[n-20:n])
            if conv_test < 1.0:
                print(f"Finished early : {n}")
                activesites = activesites[activesites > 0]
                break
    np.save(f"output-activesite/random-{sys.argv[1]}.npy", activesites)
main()
# Set 0 to dead and 1 to alive, as int, to reduce the number of necessary bits