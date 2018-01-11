from sys import argv

script, filename = argv
# use argv to get a filename

txt = open(filename)
# new command - open

print "Here's your file %r:" % filename
print txt.read()
txt.close()
