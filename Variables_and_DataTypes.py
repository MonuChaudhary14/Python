a = 1 
b= 3

print(a+b)

name = "Monu Chaudhary"


# Data Types

# | Data Type  | Description                      | Example           |
# | ---------- | -------------------------------- | ----------------- |
# | `int`      | Integer numbers                  | `x = 10`          |
# | `float`    | Decimal (floating-point) numbers | `pi = 3.14`       |
# | `complex`  | Complex numbers                  | `z = 2 + 3j`      |
# | `str`      | Text or string                   | `name = "Monu"`   |
# | `bool`     | Boolean (True/False)             | `is_valid = True` |
# | `NoneType` | Represents a null value          | `x = None`        |   This means that notihing is present in varible


# Naming Rules 

# | Rule No. | Rule Description                                                                       |
# | -------- | -------------------------------------------------------------------------------------- |
# | 1️⃣      | **Names must start with a letter** (A–Z, a–z) or an underscore `_`                     |
# | 2️⃣      | The rest of the name can include **letters, digits (0–9), or underscores**             |
# | 3️⃣      | **Names are case-sensitive** — `Name` and `name` are different                         |
# | 4️⃣      | You **cannot use Python reserved keywords** (like `if`, `while`, `def`, etc.) as names |



# Logical Operator are used by names. There are only 3 logical operators

c = True or False
d = True and False
e = not False
#Another method to use not operator
f = not(True)

print(e)
print(f)



# Type-Casting

r = 12

t = type(r)  # class <int>

print(t)

s = float(r)

j = 12.23

u = int(j)  #Conversion of float into int

print(s)

num = "21"
val = str(num)  # Conversion of String into val

print(val)


num1 = input("Enter number 1 ")  # This will take input it as a string
num2 = input("Enter number 2 ")
 
print("The sum is " , num1+num2)   #It will conacat the string

intnum = int(input("Enter the first number "))
intnum1 = int(input("Enter the second number "))

print("The sum is ", intnum + intnum1)
