import os

#testing normal use of ADD
commands = [
    "ADD 10-10-2020 PARTY HOME\n",
    "ADD 13-10-2020 CLEANUP\n"]

with open("/tmp/cald_pipe", "w") as fifo:
    for elem in commands:
        fifo.write(elem)