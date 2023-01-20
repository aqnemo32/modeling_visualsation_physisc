import subprocess

msg =  "Welcome,\nThis little interface will allow you to simulate an Ising Model.\nYou may choose between a Kawazaki Algorithm or a Glauber Algorithm\nTo select Kawazaki press k, to select Glauber press g: "
choice = input(msg)

if choice == 'g' or choice == 'G':
    print("You have chose the Glauber Algorithm ")
    N = int(input("Input the size of the array (as an integer): "))
    T = float(input("Input the temperature of the system (as a float): "))
    subprocess.run(f"python3 cp1_glauber.py {N} {T}")