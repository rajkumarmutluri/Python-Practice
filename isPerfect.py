def getFactors(x):
    """Returns a list of factors of the given number x.
    Basically, finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return
    """
    
    # your code here
    output = []
    for num in range(1,x+1):
        if (x % num == 0):
            output.append(num)
            
    return output
  



def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    
    # your code here
    sum = 0
    for factor in getFactors(x):
        if factor == x:
          
            continue
        else: 
            print(factor,sum)
            sum+=factor
    
    return (sum == x)
    

print(isPerfect(6))
print(getFactors(6))