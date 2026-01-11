# comments 
# used to explain code
# non executable code
# useful for debuggin and documentation

# single line comment: #
# 
# multiline comment: 
''' 
    multiline
    comment
'''



# identifiers: unique name given to variable, function, class
# starts with _ or letter
# dynamic type no need to pass data type
# camel case: empId 
# pascal case: EmpId

name = 20
age = 'abc'
_skill = 'Python'


print(name)
print(age)
print(_skill)

# variables: 
# container that stores value. stores/hold data in memory
# primitive data types: built in, pre defined
# int, float, string, boolean, none
# non primitive: user defined, derived from premitive.
# list, tuple, dictionary, set
# type(): check data type. 

# int
empId = 123456
print (type(empId))

# float
age = 20.5
print(type(age))

# string
skill = 'react'
print(type(age))

# boolean True/False
isEligible = True

# list = []
skills = ['html','css','js','python']
print(skills)

# multiple variable assignment
a, b, c = 10, 20, 30
print(a,b,c)

# assign one value to multiple variables
x = y = z = "Intern"
print(x,y,z)

t = None
print(type(t))

