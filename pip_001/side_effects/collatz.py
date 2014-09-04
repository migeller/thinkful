def collatz(n):
	yield n
	while n != 1:
		n = n / 2 if n % 2 == 0 else 3 * n + 1
		yield n

for i in collatz(79):
	print i
