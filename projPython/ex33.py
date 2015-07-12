def while_loop (range,increment):
	element = []
	i = 0
	print "Current list is:" , element
	while i < range:
		print "At the top i is: %d" % i
		element.append(i)
		
		print "Current list is:" , element
		i += increment
		print "At the bottom i is %d" % i
		
print "Enter range and increment"
range = int(raw_input("range >"))
increment = int(raw_input("increment >"))
while_loop(range,increment)