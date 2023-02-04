#!/bin/bash

TEMP=9
for i in range {1..22}
do
    echo "T = $TEMP"
    python3 interface_copy.py 50 $TEMP K
    TEMP=$((TEMP+1))
done 

echo All Done

