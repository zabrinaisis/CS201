name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

line1 = name + ", you are eligible to vote!"
line2 = name + ", you are not eligible to vote."

if age > 18:
	print(line1)
else:
	print(line2)