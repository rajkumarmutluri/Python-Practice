def clockwise_rotation(arr):
    n = len(arr)
    last_elem = arr[n-1]
    arr.pop()
    arr.insert(0,last_elem)
    return arr

arr = input().split()

num_rotations = int(input())

new = []

for x in range(num_rotations):
    new = clockwise_rotation(arr)
    arr = new

for x in arr:
    print(x)