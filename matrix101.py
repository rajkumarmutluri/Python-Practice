arr = []

a = input().split()
n = int(a[0])
m = int(a[1])

for x in range(n):
    arr.append(input().split())

sum = 0

for i in range(n):
    for j in range(m):
        if int(arr[i][j])%2 != 0:
            sum+=int(arr[i][j])

print(sum)