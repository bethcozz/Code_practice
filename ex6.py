x = "There are %d types of people." % 10
#string inside a string
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#strings inside strings?
print x
print y

print "I said: %r." % y
print "I also said: '%s'." % y
#strings inside strings?

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#string inside string?

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
