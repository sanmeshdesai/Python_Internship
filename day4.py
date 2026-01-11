#type casting: converting one data type to another

age = '20'
print(age)
print(type(age))
print(int(age))

a, b = 20, "30"

print(a + int(b))

empId = 1234

print(type(str(empId)))

a, b = '10', '10'
print(a+b)


# concatenation
# '+', ',','f string' 

name = 'aditya'
message = 'python'
print('your name is' + name)
print('your name is', name)
print(f'your name is {name}')

n1 = 230
n2 = '20'

print(n1, n2)

empRole = 'python full stack developer'
empAdd = 'Pune'


print(f'your role is {empRole} your address is {empAdd}')
print('your role is',empRole, 'your address is', empAdd)


empAge = 30
empCTC = "20LPA"

print(f'Your age is {empAge} and empCTC is {empCTC}')

age = '20'
name = 'sanmesh'
skill = 'mern'
role = 'developer'

print('Your name is ' + name + ' age is ' + age + ' skill is '+ skill + ' role is ' + role) 
print('Your name is' , name, 'age is' ,age, 'skill is', skill, 'role is', role) 
print(f'Your name is {name} age is {age} skill is {skill} role is {role}')

# inout() : input from user, return data string type
name = input('Enter your name ')
print('Your name is',  name)

n1 = int(input('Enter number 1'))
n2 = int(input('Enter number 2'))

print(f'Sum is {n1+n2}')


# import keyword
# print(keyword.kwlist)

x, b = 20, 30
print(x, b)

print(id(x))
print(id(b))

# id(): check memory location of variable 
a = 10
print(id(a))
