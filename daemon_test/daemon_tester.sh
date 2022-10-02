#!/bin/bash

#executes python script that writes to cald_pipe
python3 $1

#compares the contents in cald_db.csv with the expected result. If correct, nothing is outputted
diff cald_db.csv $2

#prints out the errors. If no errors exist, nothing is outputted
cat /tmp/cald_err.log

#empties database for the next test case
> cald_db.csv