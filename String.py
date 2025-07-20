# String are immutable

name = "Monu"
name1 = 'Monu'
name2 = '''Monu
Chaudhary
'''


# M   O    N    U 
# 0   1    2    3
# -4  -3  -2   -1
# The index in String Start from 0 to length-1 in python (when counting from front)



# Slicing of String

nameshort = name[0:3]   # Start from index 0 to 2 (3 is excluded)  

char = name[1]
print(char)

# Negative Slicing

test = 'MonuChauhdary'

print(test[-4:-1])  #convert this value into positive value
print(test[9:12])   # Always check the value

print(test[:3])  # It means start from 0  to 3
print(test[1:])  # It means start from 1 to length-1


# Slicing with Skip Value

print(test[2:12:4])

# string[start : stop : step] 

# abcdefghijk    [1, 9, 2]  =>  bdfhj



# String functions

check = 'monu Chaudhary'

print(len(check))

print(check.endswith('nu'))
print(check.startswith('Mo'))  #This is case sensitive hence it will give a false

print(check.capitalize())    # It does NOT care about spaces — it only works on the first character of the entire string

#Learm more functions



#Method to write fstring

print(f"Good Morning {name}")   # In this f is necessary


letter = ''' Dear |Name| , 
                You are selected!
                |Date|
                '''

print(letter.replace('|Name|', 'Monu Chaudhary').replace("|Date|" , "14-02-2006" ))





# | Function               | Description                                 | Example                                        |
# | ---------------------- | ------------------------------------------- | ---------------------------------------------- |
# | `len(s)`               | Returns the length of the string            | `len("hello")` → `5`                           |
# | `s.lower()`            | Converts to lowercase                       | `"HELLO".lower()` → `'hello'`                  |
# | `s.upper()`            | Converts to uppercase                       | `"hello".upper()` → `'HELLO'`                  |
# | `s.capitalize()`       | Capitalizes first letter                    | `"hello world".capitalize()` → `'Hello world'` |
# | `s.title()`            | Capitalizes first letter of each word       | `"hello world".title()` → `'Hello World'`      |
# | `s.strip()`            | Removes leading/trailing whitespace         | `"  hello  ".strip()` → `'hello'`              |
# | `s.replace(old, new)`  | Replaces substring                          | `"apple".replace("a", "b")` → `'bpple'`        |
# | `s.find(sub)`          | Returns index of first occurrence (or -1)   | `"hello".find("e")` → `1`                      |
# | `s.index(sub)`         | Like `find()` but raises error if not found | `"hello".index("l")` → `2`                     |
# | `s.count(sub)`         | Counts occurrences of substring             | `"hello".count("l")` → `2`                     |
# | `s.startswith(prefix)` | Checks if string starts with prefix         | `"hello".startswith("he")` → `True`            |
# | `s.endswith(suffix)`   | Checks if string ends with suffix           | `"hello".endswith("lo")` → `True`              |


# | Function              | Description                        | Example                                    |
# | --------------------- | ---------------------------------- | ------------------------------------------ |
# | `s.split(delimiter)`  | Splits string into list            | `"a,b,c".split(",")` → `['a', 'b', 'c']`   |
# | `s.rsplit(delimiter)` | Splits from right                  | `"a,b,c".rsplit(",", 1)` → `['a,b', 'c']`  |
# | `s.join(list)`        | Joins elements of list into string | `" ".join(["hi", "there"])` → `'hi there'` |


# | Function      | Description                     | Example                       |
# | ------------- | ------------------------------- | ----------------------------- |
# | `s.isalpha()` | All characters are alphabets    | `"abc".isalpha()` → `True`    |
# | `s.isdigit()` | All characters are digits       | `"123".isdigit()` → `True`    |
# | `s.isalnum()` | All characters are alphanumeric | `"abc123".isalnum()` → `True` |
# | `s.isspace()` | All characters are whitespace   | `" \t\n".isspace()` → `True`  |
# | `s.islower()` | All characters are lowercase    | `"abc".islower()` → `True`    |
# | `s.isupper()` | All characters are uppercase    | `"ABC".isupper()` → `True`    |





