# a = 12
# b = 7

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)


#relational operators
a = 50
b = 20
print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False


#assignment operators
num = 10
num **= 10
# num = num + 10 #10+10 => 20
print("num : ", num)


a = 50
b = 30
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("AND operator:",val1 and val2)

print("AND operator:",val1 or val2)


#type conversion
a = float("2")
b = 4.25

print(type(a))
print(a + b)


a = 3.14
a = str(a)

print(type(a))



name = input("Enter your age: ")
print("you entered", name)


name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("welcome", name)
print("age", age)
print("marks", marks)


side = float(input("enter square side : "))
print("area =", side ** 2)


a = float(input("enter first : "))
b = float(input("enter second : "))

print("avg =", (a+b)/2)


a = int(input("enter second : "))
b = int(input("enter second : "))

print(a >= b)