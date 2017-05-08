import sys
import re
import argparse

#Priority 1 is most important, priority 10 is least important.

#Special checker for deadline type
def deadlineCheck(v):
    try:
        return re.match("^\(.*,[0-9]*,([0-9]|10)\)$", v).group(0)
    except:
        raise argparse.ArgumentTypeError("The deadline entered, '%s', does not meet the formatting criteria. Please enter a deadline with the format '(NAME,DAYS UNTIL DUE,PRIORITY)', where priority is a number from 1 to 10, inclusive."%(v,))


#Functions:

#In this section are the auxillary functions.
def defaultSort(lines):
    print "Sorting..."
    #In this function, we must take a list of lines, and sort it by a customized algorithm
    #Algorithm: We want to take into account both the days and the priority.
    ##option: days*priority? might weigh priority too much...
    newLines=lines
    return newLines

#Three Functions are accessible to users, detailed below.
#1: "add" calls the add function, which adds a deadline when given a string corresponding to the deadlineCheck format.
def add(deadline):
    print "Adding deadline: %s" %deadline
    #Write to a specific file in same directory as .bashrc in the format (name,date,priority)
    log=open('.DeadlinesLog.txt', 'a')
    log.write("%s\n" %deadline)
    log.close()
#2: "delete" calls the delete function, which removes a deadline when given the name, date, and priority in a list.
def delete(name):
    #delete the line from the file corresponding to "name".
    logR=0
    try:
        logR=open('.DeadlinesLog.txt', 'r')
    except:
        raise "No log file exists in the current directory, or if it does, it cannot be opened. So you cannot remove anything from it."
    lines=logR.readlines()
    logR.close()
    logW=open('.DeadlinesLog.txt', 'w')
    for line in lines:
        if(not re.match(r"^\("+re.escape(name)+r",[0-9]*,([0-9]|10)\)$", line).group(0)):
            logW.write(line)
#3: "display" displays the sorted collection of deadlines, with sorting type specified
def display(sort):
    logR=0
    try:
        logR=open('.DeadlinesLog.txt', 'r')
    except:
        raise "No log file exists in the current directory. Please add a deadline."
    lines=logR.readlines()
    logR.close()
    #Basic display. I would like to implement a prettier one, where it says something like:
    ##"DEADLINE: Due in DAYS day(s), with a priority of PRIORITY."
    for l in defaultSort(lines):
        print "%s\n" %l

#Main body: Check arguments it's called with, and call the appropriate function.
parser=argparse.ArgumentParser(description='Choose function to run.')
#To enter a deadline, one uses -a, which is then followed by:
##The deadline name
##The date
##The priority
parser.add_argument('--a', nargs=1,type=deadlineCheck)

parser.add_argument('--d', nargs=1)

parser.add_argument('--s', nargs=1, choices=['default'])

comms=vars(parser.parse_args())

print comms

if(comms['a']):
    add(comms['a'].pop())
if(comms['d']):
    delete(comms['d'].pop())
if(comms['s']):
    display(comms['s'].pop())
