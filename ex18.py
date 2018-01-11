#this one is like your scripts w/ argv
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)
#def = make a function and give it a name - should say what it does
#don't actually need arg, can do it this way:
# *args means we want args, but must put in parentheses
# end w/ colon and start indenting - all colon and indented are attached to the name of the function
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
#this is a better way of doing it
#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
      print "I got nothin'."
#function with no arguments...      

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
