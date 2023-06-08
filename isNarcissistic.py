def isNarcissistic(x):
  
  s = str(x)
  
  if len(s) == 1:
    return True
  else:
    sum = 0
    for i in s:
      sum+= int(i)**len(s)
    
    return sum == x
  

print(isNarcissistic(153))