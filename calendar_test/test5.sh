#!/bin/bash

#testing GET and errors
python3 ../calendar.py GET NAME "HELLO WORLD"

python3 ../calendar.py GET INTERVAL 11-11-2021 13-11-2021 15-11-2021

python3 ../calendar.py GET DATE

python3 ../calendar.py GET EVENT MATH