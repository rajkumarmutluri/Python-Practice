student = {'name':"Rajkumar", 'rollNumber': 23, 'courses':['math', 'physics','chemistry'] }

# print(student.keys())

# if 'name' in student.keys():
student['courses'].extend(['english','sanskrit'])
#   print(student['courses'])

student['as'] = 67
  
print(student.get('gjd',"doesnt exist"))