#!/bin/bash

TEMP=17
for i in range {1..14}
do
    echo "T = $TEMP"
    python3 interface.py 50 $TEMP K
    TEMP=$((TEMP+1))
done 

echo All Done

