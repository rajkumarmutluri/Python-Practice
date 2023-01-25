num = input()
sum = 0
prod = 1

for x in num:
    sum+=int(x)
    prod*=int(x)

print(prod-sum)