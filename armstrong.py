# your code goes here
num = input()
sum = 0
for x in num:
    sum+=int(x)**3

# print(sum)
if sum == int(num):
	print("Yes")
else:
	print("No")