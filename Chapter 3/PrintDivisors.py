n = int(input("Please provide a positive integer n: "))

for i in range(n,0,-1):
	if n%i == 0:
		print(int(n/i))