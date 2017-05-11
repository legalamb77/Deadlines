This is a simple script that I wrote to provide some functionality to my terminal.

Functionality includes addition and deletion of deadlines, and displaying a sorted list of open deadlines.

The sorting algorithm, used when calling 'default' as the argument to the --s command, balances priority with the remaining days until the deadline passes.

1 is the highest priority, and 10 is the lowest, in this application.

ADDING:
In order to have the script display deadlines on startup, please place it in the same directory as your .bashrc file, and add the following line to the file:

python Deadlines.py --s 'default'

SYNTAX:
Adding Deadlines: python Deadlines.py --a '(NAME,DATE,PRIORITY)', where Date is formatted as DAY/MONTH/YEAR, and Priority ranges from 1 to 10.

Deleting Deadlines: python Deadlines.py --d 'NAME', where NAME is the deadline to be removed.

Displaying List: python Deadlines.py --s 'SORT', where the sorting algorithm used will balance priority and due date upon use of the 'default' sort, and any other entry will simply display the list in order of entry.
