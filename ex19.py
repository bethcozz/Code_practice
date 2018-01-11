def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_crackers
  print "Man that's enough for a party!"
  print "Get a blanket.\n"
#define function (blue = cheese & crackers)
#orange = variables within the function   

print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)
# filling in the function directly with values

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#filling in variables, defined as part of the function with values
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#can do math inside of the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# or variables and math together...
