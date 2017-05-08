import sys
import re
import argparse

#Special checker for deadline type
def deadlineCheck(v):
    try:
        return re.match("^\(.*,[0-9]*,([0-9]|10)\)$", v).group(0)
    except:
        raise argparse.ArgumentTypeError("The deadline entered, '%s', does not meet the formatting criteria. Please enter a deadline with the format '(NAME,DAYS UNTIL DUE,PRIORITY)', where priority is a number from 1 to 10, inclusive."%(v,))


#Does 0 need to exist? Depends on where the file is...
#Functions:
#0: "init" calls the init function, which writes a file in the correct spot for storing data
def init():
        print "yo"
#1: "add" calls the add function, which adds a deadline when given a string corresponding to the deadlineCheck format.
def add(deadline):
    print "Adding deadline: %s" %deadline
    #Write to a specific file in same directory as .bashrc in the format (name,date,priority)
    log=open('.DeadlinesLog.txt', 'a')
    log.write("%s\n" %deadline)
    log.close()
#2: "delete" calls the delete function, which removes a deadline when given the name, date, and priority in a list.
def delete(name):
    print "del"
    #delete the line from the file corresponding to "name", return true if successful, false if not found.
#3: "display" displays the sorted dictionary, with sorting type specified
def display(sort):
    print "sort"


#Main body: Check arguments it's called with, and call the appropriate function.
#use sys.argv[#], #0 is always just Deadlines.py
parser=argparse.ArgumentParser(description='Choose function to run.')
#The only functions that can be called right now are these three.
#parser.add_argument('function-name',choices=['add','delete','display'])
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