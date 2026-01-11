# constant: just convention
EMP_ID = 12345   # constant
skill = 'Python'
role = 'developer'
ctc = '10LPA'




name = input('enter name')
m1 = int(input("Enter score 1"))
m2 = int(input("Enter score 2"))
m3 = int(input("Enter score 3"))
m4 = int(input("Enter score 4")) 

print(f'Your name is {name} and your total score is {m1+m2+m3+m4} and you got {( (m1+m2+m3+m4)/400)*(100)} %')


# operators

# Arithmatic
a = 100
b = 20
print(a+b) #120
print(a-b) #80
print(a*b) #2000 
print(a/b) #5.0
print(a%b) #0
print(2**3) #8

# comparison
# ==, !=, <=, >=, <, >

x=20
y=30

print(x==y) # False
print(x!=y) #True
print(x>y) # False
print(x>=y) # False
print(x<=y) # True
print(20!=20) # False
print(20=="20") # False

# logical
# and, ot, not

# and: all conditions must be true
p = 200
q = 300
r = 500

print(p>=q and q<=r)  # False

# or: any one condition true 
print(p<=q and q<=r)  # True

# not 
print(not(10<2))

# assignment operators
# +=, -=, *=, /=, %=

n1 = 20
n2 = 40

n1 += n2
print(n1) # 60

n1 *= n2 
print(n1) # 2400

n2 -= n1
print(n1) #2400
print(n2) #-2360

# bitwise operator
# convert decimal to binary
# &, |, ^, ~, >>, <<, >>>, <<<
print(5 & 3) # 1
print(5 & 8) # 0

# Ternary: 
# - value_if_true if condition else value_if_false

year = int(input("enter your birth year"))

result = "Your genz " if year > 2000 else "Your not genz"
print(result)



