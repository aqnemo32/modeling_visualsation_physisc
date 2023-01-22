#!/bin/bash

TEMP=10
for i in range {1..20}
do
    echo "T = $TEMP"
    python3 interface.py 50 $TEMP G
    TEMP=$((TEMP+1))
done 

echo All Done

