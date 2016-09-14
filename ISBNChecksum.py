import sys

num = raw_input("Input a 9-digit number: ")
if len(num) > 9:
	print "Please enter a 9-digit number."
	sys.exit(1)
else: 
	sum = 0
	j = 2
	for i in range(1, len(num)+1):
		sum += j * int(num[-i])
		j += 1

	print sum

	for i in range(0, 11):
		if (sum + i) % 11 == 0:
			if i == 10:
				print ("ISBN #: %s") % (num + str(0))
			else:
				print ("ISBN #: %s") % (num + str(i))
		else: 
			continue
