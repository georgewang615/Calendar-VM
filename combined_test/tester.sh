#!/bin/bash

#executes calendar scripts to write to database
./$1

#compares the contents in cald_db.csv with the expected result. If correct, nothing is outputted
diff ../cald_db.csv $2

#prints error messages to stdout
cat /tmp/cald_err.log

#empties database for the next test case
> ../cald_db.csv