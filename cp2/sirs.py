import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rules(spin, lx, ly, p1, p2, p3):
    for i in range(lx):
        for j in range(ly):
            itrial=np.random.randint(0,lx)
            jtrial=np.random.randint(0,ly)

            trial_spin = spin[itrial, jtrial]

            if trial_spin == -1:
                # If the statement is true it goes forward with it
                if spin[np.mod(itrial-1,lx),jtrial] == 0 or spin[np.mod(itrial+1,lx),jtrial] == 0 or spin[itrial,np.mod(jtrial-1,lx)]==0 or spin[itrial,np.mod(jtrial+1,lx)] == 0: 

                    r = random.random()
                    if p1 >= r:
                        spin[itrial,jtrial] = 0
            elif trial_spin == 0:
                
                r = random.random()
                if p2 >= r:
                    spin[itrial,jtrial] = 1
            else:
                
                r = random.random()
                if p3 >= r:
                    spin[itrial,jtrial] = -1
    return spin




def main():
    nstep = 1000

    lx = int(sys.argv[1])
    ly = lx
    #  p1 is the probability that S->I
    p1 = float(sys.argv[2])
    #  p2 is the probability that I->R
    p2 = float(sys.argv[3])
    #  p3 is the probability that R->S
    p3 = float(sys.argv[4])

    spin=np.zeros((lx,ly),dtype=int)
    # initialise spin amtrix with 1 = R, 0 = I, -1 = S
    for i in range(lx):
        for j in range(ly):
            r = random.random()
            if r >= 2/3: spin[i,j] = int(1)
            elif r < 1/3: spin[i,j] = int(-1)

    fig = plt.figure()
    im=plt.imshow(spin, animated=True)
    avg_infected = np.zeros(int((nstep-100)/10))

    for n in range(nstep):
        # should do 2500 attempted flips to progress to the next sweep.
        spin = rules(spin, lx, ly, p1, p2, p3)

        if n%10 == 0:
            if n >= 100:
                dummy = spin.flatten()
                avg_infected[int(n/10 - 10)] = dummy[dummy == 0].shape[0]
                conv_test = avg_infected[int(n/10 - 10)]
                if conv_test == 0:
                    print(f"Finished early : {n}")
                    break

            plt.cla()
            im=plt.imshow(spin, animated=True)
            plt.draw()
            plt.pause(0.0001)
            # print(f"{n}, {spin.flatten()[spin.flatten() == 0].shape[0]}")
    # print(type(avg_infected))
    np.save(f"output-sirs/infected-{p1}-{p3}", avg_infected)
    # np.save(f"spin_data/eq_spin_{lx}_{kT}_{sys.argv[3]}", super_spin[-1,:,:])

main()