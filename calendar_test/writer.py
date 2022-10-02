import os

with open("/tmp/calendar_link", "r") as f:
    path = f.read()

events = [
    "12-11-2021,CLASS,MATH\n",
    "11-11-2021,CLASS,ENGLISH\n",
    "10-11-2021,WEEKEND,SUNDAY\n",
    "09-11-2021,WEEKEND,SATURDAY\n"
    "13-11-2021,PRACTICE,\n"
]

with open(path, "a") as f:
    for elem in events:
        f.write(elem)