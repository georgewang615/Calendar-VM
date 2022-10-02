import os

#testing normal use of UPD and special cases
commands = [
    "ADD 10-10-2020 PARTY HOME\n",
    "ADD 13-10-2020 CLEANUP\n",
    "UPD 10-10-2020 PARTY STUDY\n",
    "UPD 13-10-2020 CLEANUP SHOPPING ONLINE!\n"
    "UPD 12-10-2020 NOTHING SOMETHING\n"]

with open("/tmp/cald_pipe", "w") as fifo:
    for elem in commands:
        fifo.write(elem)