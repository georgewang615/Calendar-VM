#!/bin/bash

#testing error messages
python3 ../calendar.py ADD 01-10-2021 PARTY

python3 ../calendar.py UPD 01-10-2021 PARTY WEDDING

python3 ../calendar.py GET DATE 01-10-2021