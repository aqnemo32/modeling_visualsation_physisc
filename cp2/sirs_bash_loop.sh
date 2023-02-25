#!/bin/bash

P2=$(echo " scale=2; 0.5" | bc)
P3=$(echo "scale = 3; 0.0" | bc)
for DUM in {1..100}
do
    echo "P3 = $P3"
    for KVAL in {1..100}
    do
        P1=$(echo " scale=3; 0.0 + ($KVAL-1) * 0.01" | bc)
        echo "P1 = $P1"
        python3 sirs.py 50 $P1 $P2 $P3 


    done
    P3=$(echo " scale=3; $P3 + 0.01" | bc)
done    


