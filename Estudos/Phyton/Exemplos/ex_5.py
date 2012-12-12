# Exercise 5: Variables and printing

my_name = 'Harumi Tominaga'
my_age = 27 # not a lie
my_height = 57.5 # kg
my_weight = 1.60
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = "Brown"

print "Let's talk about %s." % my_name # For string, you should always use %s
print "She's %d kg tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that's not too heavy"
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)

# This line is tricky(confuse), try to get it exactly right
print "If I add %d, %r and %r I get %r." %(my_age, my_height, my_weight, my_age + my_height + my_weight)