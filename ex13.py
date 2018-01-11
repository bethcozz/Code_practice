#this is the line of how to open this in command line:
    #python ex13.py first 2nd 3rd

#from sys import argv
#add modules from python

#script, first, second, third = argv
#unpack argv so it is assigned to four vars
    #take whatever's in argv, unpack, assign to variables on the left in order

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

from sys import argv
script, first, second = argv

print "Script is a", script
print "1st var is", first
print "2nd var is", second
