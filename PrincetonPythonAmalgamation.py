#import stdio
import sys
import math
#import random
import turtle

'''while True:
	a = raw_input("Enter a float: ")
	b = math.sin(float(a))**2 + math.cos(float(a))**2
	print b
	if a == '0':
		sys.exit(1)'''	

'''if (float(sys.argv[1]) % float(sys.argv[2]) == 0) or \
		(float(sys.argv[2]) % float(sys.argv[1]) == 0):
	stdio.writeln("True")'''

'''if (float(sys.argv[1]) + float(sys.argv[2]) < float(sys.argv[3])) \
		or (float(sys.argv[1]) + float(sys.argv[3]) < \
		float(sys.argv[2])) or (float(sys.argv[2]) \
		+ float(sys.argv[3]) < float(sys.argv[1])): 
	print("False")'''	

'''a = int(sys.argv[1])
b = int(sys.argv[2])
print("%d") % random.randint(a, b)'''

'''print("Continous compound interest calculator: p*e^(r*t)")
p = sys.argv[1]
r = sys.argv[2]
t = sys.argv[3]
I = float(p) * math.e ** (float(r) * float(t))
print("The money you have acculumated is: %.2f") % I''' 

'''print("Cartesian to Polar coordinate converter")
x = sys.argv[1]
y = sys.argv[2]
r = math.hypot(float(x), float(y))
theta = math.atan2(float(y), float(x))
print("r = %.1f, theta = %s") % (r, theta)'''

'''u = random.random()
v = random.random()
Z = math.sin(2*math.pi*v) * (-2*math.log(u))**.5
print("%.2f") % Z'''

'''print("RGB to CMYK converter")
r = float(sys.argv[1])
g = float(sys.argv[2])
b = float(sys.argv[3])
w = max(r / 255, g / 255, b / 255)
c = (w - r / 255) / w
m = (w - g / 255) / w
y = (w - b / 255) / w
k = 1 - w
print("cyan = %.2f\nmagenta = %.2f\nyellow = %.2f\n"
	   "black = %.2f") % (c, m, y, k)'''

'''a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
list = [a, b, c]
list.remove(max(list))
list.remove(min(list))
print("%.2f, %.2f, %.2f") % (min(a,b,c), list[0], max(a,b,c))'''


