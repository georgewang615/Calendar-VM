import os

#testing invalid commands with error messages printing to stdout
commands = [
    "ADD 10-10-20200 PARTY HOME\n",
    "ADD 13-10-2020 CLEANUP WITH MOM\n",
    "UPD 12-10-2020 NOTHING SOMETHING EXTRA!\n"]

with open("/tmp/cald_pipe", "w") as fifo:
    for elem in commands:
        fifo.write(elem)