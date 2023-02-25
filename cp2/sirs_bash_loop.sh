#!/bin/bash

P2=$(echo " scale=2; 0.5" | bc)
P3=$(echo "scale = 3; 0.0" | bc)
for KVAL in {1..100}
echo ${KVAL}
# P1=$(echo " scale=3; 0.0 + $KVAL * 0.05" | bc)
# echo $P1

# python3 sirs.py 50 $P1 $P2 $P3

