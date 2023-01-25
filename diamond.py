
n = int(input())

for i in range(2*n-1):
    if i < n:
        j = i
        print(" "*(n-j-1) + "*"*(2*j+1) + " "*(n-j-1))
    else:
        j = i-n+1
        print(" "*j + "*"*(2*(n-j)-1) + " "*j)