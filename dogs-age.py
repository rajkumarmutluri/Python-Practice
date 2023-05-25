import math

def calculate_dog_age_in_human_years(dog_age):
    human_years = 0
    try:
              
        if dog_age < 0:
            raise ValueError()
        
        if dog_age > 5:
            human_years = (36+(dog_age-5)*7)
        elif dog_age > 4:
            human_years = dog_age*7.2          
        elif dog_age > 3:
            human_years = dog_age*8
        elif dog_age > 2:
            human_years = dog_age*9.3
        elif dog_age > 1:
            human_years = dog_age*12
        elif dog_age >= 0:
            human_years = dog_age*15
            
        
        if int(dog_age) == dog_age:
          dog_age = int(dog_age)
            
        print(f"The given dog age {dog_age} is {round(human_years,1) if human_years == int(human_years) else round(human_years,2)} in human years.") 
      
    except ValueError:
        print("Age cannot be a negative number.")
      


dog_age = input("Please enter the dog age in dog years : ")

try:
  dog_age = float(dog_age)
  calculate_dog_age_in_human_years(dog_age)
  
except ValueError:
  print(f"{dog_age} is invalid")

