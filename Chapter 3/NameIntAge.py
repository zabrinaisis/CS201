first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Your initials are:",first[0],last[0])

year = int(input("What year were you born?: "))
if year < 1998:
	print("You can get a drivers license in Iowa.")
else:
	print("You cannot get a drivers license in Iowa yet.")