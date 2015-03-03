x = float(input("Enter a x coordinate between -10 and 10: "))
y = float(input("Enter a y coordinate between -10 and 10: "))

import math

if math.sqrt(x**2+y**2) <= 8:
	print("It is in!!!")