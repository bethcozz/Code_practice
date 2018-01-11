#for this one: needs more than one file name
from sys import argv ; from os.path import exists
# exists = returns true if file exists (based on name, in string, as arg)
# returns false if not

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these on one line... how = ;;;
in_file = open(from_file); indata = in_file.read()

print "The input file is %d bytes long" % len(indata)
#len gets the length of the string & returns a number

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort." ; raw_input()

out_file = open(to_file, 'w'); out_file.write(indata)

print "Alright, all done."

out_file.close(); in_file.close()
