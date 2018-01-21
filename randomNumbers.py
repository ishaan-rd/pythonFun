#######################################################################
# Script: Generating a hundred thousand numbers in range 0 to 100,000 #
#         randomly without repitition and saving to a file.           #
#         Range of numbers to be generated can be changed.            #
# Author: Ishaan R Dharamdas                                          #
# Date: 21/01/18                                                      #
#######################################################################

import random

# generating 100,000 numbers
myList = list(xrange(0,100000))

# shuffling the list
random.shuffle(myList)

# opening a file and writing down the list
target = open("file.txt", 'r+') # can change the filename

for item in myList:
    target.write("%s\n" % item)
