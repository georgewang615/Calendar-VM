import os

#testing more invalid and edge commands with error messages printing to stdout
commands = [
    "ADD 00-10-2000 PARTY HOME\n",
    "DELETE 13-10-2020 CLEANUP WITH MOM\n",
    "ADD 12-10-2020 NOTHING\n",
    "UPD 12-10-2020 NOTHING 'SOMETHING EXTRA!'\n"]

with open("/tmp/cald_pipe", "w") as fifo:
    for elem in commands:
        fifo.write(elem)