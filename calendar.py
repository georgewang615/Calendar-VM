import os
import sys
import datetime

#reads the path to the database from the tmp file
try:
    with open("/tmp/calendar_link", "r") as f:
        path = f.read()

#error case when the path is invalid or it doesn't exist
except:
    print("Unable to process calendar database")
    exit(0)

#function that processes get command with date as an action option
def get_date(data):
    #error case when the number of arguments is incorrect
    if len(sys.argv) != 4:
        print("Incorrect number of arguments")
        exit(0)

    #breaking the date into its numbers and testing if it's in the right format
    date = sys.argv[3].split("-")
    try:
        d = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        
    #error case when the date from the command is invalid
    except:
        print("Unable to parse date")
        exit(0)

    #iterating through each line of the database and priting the line in stdout if the dates match
    for i in range(len(data)):
        if data[i][0] == sys.argv[3]:
            print("{} : {} : {}".format(data[i][0], data[i][1], data[i][2]).rstrip("\n"))

#function that processes get command with interval as an action option
def get_interval(data):
    #error case when the number of arguments is incorrect
    if len(sys.argv) != 5:
        print("Incorrect number of arguments")
        exit(0)

    #breaking the dates into their numbers and testing if they're in the right format
    date1 = sys.argv[3].split("-")
    date2 = sys.argv[4].split("-")
    try:
        d1 = datetime.datetime(int(date1[2]), int(date1[1]), int(date1[0]))
        d2 = datetime.datetime(int(date2[2]), int(date2[1]), int(date2[0]))

    #error case when either date from the command is invalid
    except:
        print("Unable to parse date")
        exit(0)

    #error case when start date is after end date
    if d1 > d2:
        print("Unable to Process, Start date is after End date")
        exit(0)

    #iterating through each line of the data base and turning the date into datetime format
    for i in range(len(data)):
        nums = data[i][0].split("-")
        d = datetime.datetime(int(nums[2]), int(nums[1]), int(nums[0]))

        #if the date fits in the interval, the event printed to stdout
        if d >= d1 and d <= d2:
            if len(data[i]) == 3:
                print("{} : {} : {}".format(data[i][0], data[i][1], data[i][2]).rstrip("\n"))
            else:
                print("{} : {} : ".format(data[i][0], data[i][1]).rstrip("\n"))

#function that processes get command with name as an action option
def get_name(data):
    #error case when no name was given in command
    if len(sys.argv) < 4:
        print("Please specify an argument")
        exit(0)

    #iterating through each line of the database
    for i in range(len(data)):

        #if the name of the event starts with the string given, the event is printed to stdout
        if data[i][1].startswith(" ".join(sys.argv[3:])):
            if len(data[i]) == 3:
                print("{} : {} : {}".format(data[i][0], data[i][1], data[i][2]).rstrip("\n"))
            else:
                print("{} : {} : ".format(data[i][0], data[i][1]).rstrip("\n"))

#function that processes add command to the daemon
def add(cmd, data):
    err_count = 0
    err = ""
    date = cmd[1].split("-")

    #testing if the date can be parsed
    try:
        d = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    except:
        err = "Unable to parse date"
        err_count += 1

    #error case when event name is missing
    if len(cmd) < 3:
        err = "Missing event name"
        err_count += 1
    
    #checking if the event already exists
    for i in range(len(data)):
        if data[i][0] == cmd[1] and data[i][1] == cmd[2]:
            err = "Event already exists"
            err_count += 1

    #if no errors exist, the command is passed on to the daemon via the named pipe
    if err_count == 0:
        with open("/tmp/cald_pipe", "a") as fifo:
            fifo.write(" ".join(cmd))
            fifo.write("\n")

    #if there is one error message, it is printed to stdout
    elif err_count == 1:
        print(err)

    #if there is more than one error message, a special message is printed
    else:
        print("Multiple errors occur")

#function that processes upd command to the daemon
def upd(cmd, data):
    err_count = 0
    err = ""
    event_exist = 0
    date = cmd[1].split("-")

    #testing if the date can be parsed
    try:
        d = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    except:
        err = "Unable to parse date"
        err_count += 1

    #testing if the event exists
    for i in range(len(data)):
        if data[i][0] == cmd[1] and data[i][1] == cmd[2]:
            event_exist = 1
    
    if event_exist == 0:
        err = "Unable to update, event does not exist"
        err_count += 1

    #error case when not enough arguments are given
    if len(cmd) < 4:
        err = "Not enough arguments given"
        err_count += 1

    #if no errors exist, the command is passed on to the daemon via the named pipe
    if err_count == 0:
        with open("/tmp/cald_pipe", "a") as fifo:
            fifo.write(" ".join(cmd))
            fifo.write("\n")

    #if there is one error message, it is printed to stdout
    elif err_count == 1:
        print(err)

    #if there is more than one error message, a special message is printed
    else:
        print("Multiple errors occur")

#function that processes del command to the daemon
def delete(cmd):
    err_count = 0
    err = ""
    date = cmd[1].split("-")

    #testing if the date can be parsed
    try:
        d = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    except:
        err = "Unable to parse date"
        err_count += 1

    #error case when event name is missing
    if len(cmd) < 3:
        err = "Missing event name"
        err_count += 1

    #if no errors exist, the command is passed on to the daemon via the named pipe
    if err_count == 0:
        with open("/tmp/cald_pipe", "a") as fifo:
            fifo.write(" ".join(cmd))
            fifo.write("\n")

    #if there is one error message, it is printed to stdout
    elif err_count == 1:
        print(err)

    #if there is more than one error message, a special message is printed
    else:
        print("Multiple errors occur")


def run():
    action = sys.argv[1]

    #opening the database and reading the data as a list
    with open(path, "r") as f:
        data = f.readlines()

    #splitting each event into its elements as a list
    for i in range(len(data)):
        data[i] = data[i].split(",")

    #calling get functions depending on the action option
    if action == "GET":
        if sys.argv[2] == "DATE":
            get_date(data)
   
        elif sys.argv[2] == "INTERVAL":
            get_interval(data)

        elif sys.argv[2] == "NAME":
            get_name(data)

        #error case when the action option for GET is invalid
        else:
            print("Invalid action option for GET")

    #calling ADD function with the database and the command line excluding the python extension as arguments
    elif action == "ADD":
        add(sys.argv[1:], data)
    
    #calling UPD function with the database and the command line excluding the python extension as arguments
    elif action == "UPD":
        upd(sys.argv[1:], data)

    #calling DEL function with the database and the command line excluding the python extension as arguments
    elif action == "DEL":
        delete(sys.argv[1:])

    #error case when action is invalid
    else:
        print("Invalid action")


if __name__ == '__main__':
    run()

