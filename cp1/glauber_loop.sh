#!/bin/bash

TEMP=22
for i in range {1..9}
do
    echo "T = $TEMP"
    python3 interface.py 50 $TEMP G
    TEMP=$((TEMP+1))
done 

echo All Done

