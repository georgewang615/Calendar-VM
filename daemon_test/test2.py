import os

#testing normal use of DEL and deleting non-existent event
commands = [
    "ADD 10-10-2020 PARTY HOME\n",
    "ADD 13-10-2020 CLEANUP\n",
    "DEL 10-10-2020 PARTY\n",
    "DEL 12-10-2020 NONEXISTENT\n"]

with open("/tmp/cald_pipe", "w") as fifo:
    for elem in commands:
        fifo.write(elem)