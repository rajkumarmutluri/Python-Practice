def fold_array(array):
    n = len(array)
    new = []
    for i in range(n//2):
        new.append(array[i]+array[n-1-i])
    if n%2 == 1:
        new.append(array[n//2])
    return new

n = int(input())
arr = []
for x in range(n):
    arr.append(int(input()))

num_folds = int(input())

for folds in range(num_folds):
    arr = fold_array(arr)


print(len(arr))

for x in arr:
    print(x)