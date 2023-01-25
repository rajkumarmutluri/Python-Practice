#start your code from here
n = int(input())
arr = []
for i in range(n):
	arr.append(int(input()))

leader = [arr[n-1]]

temp = arr[n-1]
i=n-2
while i>=0:
	if arr[i]>temp:
		leader.append(arr[i])
		temp = arr[i]
	i-=1

# print(leader)

for i in leader:
	print(i)