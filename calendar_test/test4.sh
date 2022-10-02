#!/bin/bash

#testing GET errors
python3 ../calendar.py GET NAME

python3 ../calendar.py GET INTERVAL 11-11-2021

python3 ../calendar.py GET DATE INVALID-INVALID-INVALID