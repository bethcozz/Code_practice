# close - closes the file
# read - reads contents of file
# readline - reads just one line from file
# truncate - empties the file **CAREFUL**
# write(stuff) - writes 'stuff' to the file.

from sys import argv
#use argv
script, filename = argv
#I still dk what this means
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#we open, truncate, erase, replace this file
raw_input("?")
#waits for you to respond on this

print "Opening the file..."
target = open(filename, 'w')
#w=write mode, r=read mode, a=append mode
#w+ = write plus, r+=read plus, a+=append plus
#open() = default is open in read mode
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
