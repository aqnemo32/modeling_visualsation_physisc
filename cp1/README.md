## How to run the `interface.py`:

In the command line:

```
python3 interface.py N T <K/G>
```
- `N` is a side length of the Square lattice, a value of 50 for N means that there 2500 spins that can be flipped
- `T` is the temperature at which the simulation is run where a value of 10 for T is considered low. The value of input for T should be 10 times the value you run it at. This is because I used a bash script to run the simulations one after the other and realised 
that bash doesn't like float points. So my solution to this problem was to just make an input of 10 equivalent to a T of 1.0
- `<K/G>` is the dynamics model used for the simulatio where G is Glauber Dynamics and K is Kawazaki Dynamics

When `interface.py` runs, for every sweep >= 100 and a multiple of 10 the spin matrix is saved into a nupy array called `super_spin`. This array of dimensions `(nstep-100)/10), N, N)` is then saved wih the following name: `spin_data_N_T_<K/G>.npy`.
`interface.py` also saves the last spin array for each temperature of dimensions`(N, N)` with the following name: `eq_spin_N_T_<K/G>.npy`.

Both files are saved in binary format to save space

interface.py and interface_k.py initialise the initial spin matrix differently:
- ### interface.py
    - The initial spin matrix is either the previous temperatures last spin matrix or if it is not available then an array of random spins is created
- ### interface_k.py
    - The initial spin matrix is either the previous temperatures last spin matrix or if it is not available then an array of equal spin up/down is created where the LHS is spin up and the RHS is down

## How to run `magnet.py`:

In the Command line:
```
python3 magnet.py <K/G>
```
- `<K/G>` just tells magnet to retrieve the data necessary from either the Glauber or Kawazaki simulations.

The data is then used to calculate the Average Energy, Magnetic Susceptibility, Heat Capacity and Average Magnetisation for a given Temperature.

The erros in Magnetic Susceptibility and Heat Capacity were calculated using the Jacknife method. The Errors in Average Magnetisation and Energy were calculated by finding the standard error of the mean

The output of `magnet.py` is then stored in a file called `<K/G>_final_data.dat` in the format of 
    Temperature, Energy, Error Energy, Susceptibility, Error Susceptibility, Heat Capacity, Error Heat Capacity, Magnetisation, Error Magnetisation

This file can can then be used to plot using the `plotting.py` file

## How to run `plotting.py`:

In the Command Line:
```
python3 plotting.py <K/G>
```
- `<K/G>` just tells `plotting.py` to retrieve the data necessary from either the Glauber or Kawazaki datafiles created by `magnet.py`.




