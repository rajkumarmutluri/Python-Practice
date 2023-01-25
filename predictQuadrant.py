t = int(input())
for x in range(t):
	a = input().split(" ")
	x = int(a[0])
	y = int(a[1])
	if x > 0 and y > 0:
		print("Q1")
	elif x < 0 and y > 0:
		print("Q2")
	elif x < 0 and y < 0:
		print("Q3")
	else:
		print("Q4")