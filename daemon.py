#!/bin/python

import signal
import os
import sys


#Use this variable for your loop
daemon_quit = False

#Do not modify or remove this handler
def quit_gracefully(signum, frame):
    global daemon_quit
    daemon_quit = True

#function that processes ADD command, arguments are the csv data, error log, and command from cald_pipe
def add(contents, err_msg, entry):

    #error case for wrong number of arguments from the command
    if len(entry) != 3 and len(entry) != 4:
        err_msg.append("Wrong number of arguments")
    
    else:
        #breaking the date into a list of numbers
        numbers = entry[1].split("-")
        try:
            #testing if the date is in the format DD-MM-YYYY
            if int(numbers[0]) in range(1, 32) and int(numbers[1]) in range(1, 13) and int(numbers[2]) in range(1000, 10000):

                #appending the date and event (and description) into contents
                if len(entry) == 3:
                    contents.append("{},{},\n".format(entry[1], entry[2]))
                else:
                    contents.append("{},{},{}\n".format(entry[1], entry[2], entry[3]))

            #error case when numbers are not in DD-MM-YYYY format
            else:
                err_msg.append("Incorrect date format")

        #error case when the date cannot be turned into integers
        except:
            err_msg.append("Incorrect date format")

    return contents, err_msg

#function that processes DEL command, arguments are the csv data, error log, and command from cald_pipe
def delete(contents, err_msg, entry):
    #error case for wrong number of arguments from the command
    if len(entry) != 3:
        err_msg.append("Wrong number of arguments")

    else:
        #iterating through every event in the database
        for row in contents:
            elements = row.split(",")

            #if the date and the event name in the database match those in the command, the event is removed
            if elements[0] == entry[1] and elements[1] == entry[2]:
                contents.remove(row)

    return contents, err_msg

#function that processes UPD command, arguments are the csv data, error log, and command from cald_pipe
def upd(contents, err_msg, entry):
    #error case for wrong number of arguments from the command
    if len(entry) != 4 and len(entry) != 5:
        err_msg.append("Wrong number of arguments")

    else:
        #iterating through every event in the data base
        for i in range(len(contents)):
            elements = contents[i].split(",")

            #testing if the date and the event name in the database match those in the command
            if elements[0] == entry[1] and elements[1] == entry[2]:
                                
                if len(entry) == 4:
                    description = ""

                elif len(entry) == 5:
                    description = entry[4]

                #the elements of the old event is replaced with the new date, name, and description (optional)
                elements = [entry[1], entry[3], description]
                
                #elements are reformatted for the database
                contents[i] = ",".join(elements) + '\n'

    return contents, err_msg

def run(db_path):
    #Do not modify or remove this function call
    signal.signal(signal.SIGINT, quit_gracefully)
    
    pipe_path = "/tmp/cald_pipe"
    #if the pipe doesn't already exist, it is created
    try:
        os.mkfifo(pipe_path)
    except FileExistsError:
        pass
    
    
    global daemon_quit
    #while the daemon is active it receives commands from the pipe
    while daemon_quit == False:
        err_msg = []

        #reading and storing the commands as a list
        with open(pipe_path, "r") as fifo:
            commands = fifo.readlines()    

        #reading and storing the existing events as a list
        with open(db_path) as f:
            contents = f.readlines()

            #iterating through each command
            for i in range(len(commands)):
                #breaking up the command and executing the appropriate program, returning the updated contents and error messages
                entry = commands[i].split()

                if entry[0] == "ADD":
                    contents, err_msg = add(contents, err_msg, entry)
                    
                elif entry[0] == "DEL":
                    contents, err_msg = delete(contents, err_msg, entry)
            
                elif entry[0] == "UPD":
                    contents, err_msg = upd(contents, err_msg, entry)

                #error case when command is not valid
                else:
                    err_msg.append("Invalid command")

        #overwriting the database with the updated contents
        with open(db_path, "w") as f: 
            for i in range(len(contents)):
                f.write(contents[i])

        #writing the error messages to the error log
        with open("/tmp/cald_err.log", "w") as f:
            for i in range(len(err_msg)):
                f.write(err_msg[i])
                f.write("\n")

                    
        

if __name__ == '__main__':
    #if no additional argument is given, the path of the data base is the current directory
    if len(sys.argv) == 1:
        db_path = os.getcwd() + "/cald_db.csv"

    #otherwise the path is given as a command line argument
    else:
        db_path = sys.argv[1]

    #testing if the database already exists, if not, it is created
    try:
        f = open(db_path, "r")
    except:
        f = open(db_path, "w")
    f.close()

    #writing the path to the tmp file so calendar.py can read it
    with open("/tmp/calendar_link", "w") as f:
        f.write(db_path)

    run(db_path)
