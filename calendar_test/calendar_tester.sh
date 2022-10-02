#!/bin/bash

#executes python script that writes to database
python3 writer.py

#executes calendar scripts and compares to expected output
./$1 | diff - $2

#empties database for the next test case
> ../cald_db.csv