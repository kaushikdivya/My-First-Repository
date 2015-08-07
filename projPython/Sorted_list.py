from sys import exit
print "Enter sorted first list:"

list1 = raw_input("> ")
print list1
list1_split = list1.split(' ')
list1_sorted = sorted(list1.split(' '))
print list1_sorted
if list1_sorted != list1_split:
	print "Enter sorted list baby"
	exit(0)

print "Enter sorted second list"

list2 = raw_input("> ")
list2_sorted = sorted(list2.split(' '))
list2_split = list2.split(' ')
if list2_sorted != list2_split:
	print "Enter sorted list dumbo"
	exit(0)
	
print "Making one list with sorted numbers"

len1_len = len(list1_split)
len2_len = len(list2_split)
print len1_len, len2_len
x = 0
y = 0
list3 = []
while x < len1_len or y < len2_len:
	print x, y
	if x == len1_len and y != len2_len:
		list3.append(list2_split[y])
		y += 1
	elif x != len1_len and y == len2_len:
		list3.append(list2_split[x])
		x += 1
	else:
		if list1_split[x] < list2_split[y]:
			list3.append(list1_split[x])
			x +=1
		elif list1_split[x] > list2_split[y]:
			list3.append(list2_split[y])
			y += 1
		else:
			list3.append(list1_split[x])
			list3.append(list2_split[y])
			x += 1
			y += 1

print list3