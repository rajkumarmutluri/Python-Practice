inp = input().split()

N = int(inp[0])
k = int(inp[1])

arr = input().split()

count = 0

for x in arr:
    if int(x) == k:
        count+=1

print(count)