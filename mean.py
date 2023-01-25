# your code goes here
import math
n = int(input())
sum = 0
a = input().split(" ")
for x in a:
	sum+=int(x)

print(math.floor(sum/n))