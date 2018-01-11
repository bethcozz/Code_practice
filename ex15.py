from sys import argv

script, filename = argv
# use argv to get a filename

txt = open(filename)
# new command - open

print "Here's your file %r:" % filename
print txt.read()
txt.close()
#this is a function on txt named read
#give file a command by using . name of command, parameters

print "Type the filename again:"
file_again = raw_input("- ")
#asking raw input, saving filename to use & open
txt_again = open(file_again)

print txt_again.read()
txt.close()
#print copy of contents
