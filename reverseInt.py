def reverseInt(num):
    rev = 0
    temp = num
    while temp>0:
        rev = rev*10 + (temp%10)
        temp = int(temp/10)
    return rev


num = int(input())

if num<0:
    print(-1*reverseInt(-1*num))
else:
    print(reverseInt(num))