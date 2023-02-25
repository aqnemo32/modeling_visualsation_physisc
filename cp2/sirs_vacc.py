import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# REDOOO
def nearest_neighbours(i,j, spin, lx):
    # wrote this to check if when person is Susceptible f there is an in
    neighbour_matrix = np.zeros(4)

    neighbour_matrix[0] = int(spin[np.mod(i-1,lx),j])
    neighbour_matrix[1] = int(spin[np.mod(i+1,lx),j])
    neighbour_matrix[2] = int(spin[i,np.mod(j-1,lx)])
    neighbour_matrix[3] = int(spin[i,np.mod(j+1,lx)])


    for papa in neighbour_matrix:
        if int(papa) == 0:
            return True
        else: return False


def rules(spin, lx, ly, p1, p2, p3, i_immune, j_immune):
    for i in range(lx):
        for j in range(ly):
            itrial=np.random.randint(0,lx)
            jtrial=np.random.randint(0,ly)
            # checks is the selected spin is one of the permanently immune ones, selects new spins (HOPEFULLY)
            for k,l in (i_immune, j_immune):
                if itrial == i_immune and jtrial == j_immune:
                    break
            else:
                trial_spin = -spin[itrial, jtrial]

            if trial_spin == -1:
                # If the statement is true it goes forward with it
                if nearest_neighbours(itrial, jtrial, spin, lx): 
                    
                    r = random.random()
                    if p1 <= r:
                        spin[itrial,jtrial] = 0
            elif trial_spin == 0:
                
                r = random.random()
                if p2 <= r:
                    spin[itrial,jtrial] = 1
            else:
                
                r = random.random()
                if p3 <= r:
                    spin[itrial,jtrial] = -1
            return spin




def main():
    nstep = 10000

    lx = int(sys.argv[1])
    ly = lx
    #  p1 is the probability that S->I
    p1 = float(sys.argv[2])
    #  p2 is the probability that I->R
    p2 = float(sys.argv[3])
    #  p3 is the probability that R->S
    p3 = float(sys.argv[4])

    n_vacc = int(sys.argv[5])

    spin=np.zeros((lx,ly),dtype=int)
    # initialise spin amtrix with 1 = R, 0 = I, -1 = S
    for i in range(lx):
        for j in range(ly):
            r = random.random()
            if r >= 2/3: spin[i,j] = 1
            elif r < 1/3: spin[i,j] = -1

    fig = plt.figure()
    im=plt.imshow(spin, animated=True)
    avg_infected = np.zeros(int((nstep-100)/10))

    # define the permanently immunes patients
    i_immune = np.array((np.random.randint(0,lx, size = n_vacc)))
    j_immune = np.array((np.random.randint(0,lx, size = n_vacc)))

    for k, l in (i_immune, j_immune):
        spin[k,l] = 0

    for n in range(nstep):
        # should do 2500 attempted flips to progress to the next sweep.
        dummy = spin.flatten()
        

        spin = rules(spin, lx, ly, p1, p2, p3)




        if n%10 == 0:
            if n >= 100:
                avg_infected[int(n/10 - 10)] = dummy[dummy == 0].shape[0]

            plt.cla()
            im=plt.imshow(spin, animated=True)
            plt.draw()
            plt.pause(0.0001)
            # print(f"{n}, {spin.flatten()[spin.flatten() == 0].shape[0]}")
    # print(type(avg_infected))
    np.save(f"output_sirs/infected_{p1}_{p3}", avg_infected)
    # np.save(f"spin_data/eq_spin_{lx}_{kT}_{sys.argv[3]}", super_spin[-1,:,:])

main()