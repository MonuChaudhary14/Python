# Module is the file containing code written by someone else which we can install using PIP


# Different types of Modules
'''
Type	Description	Example
Built-in	Pre-installed with Python	math, random, os
User-defined	Custom module created by you	mymodule.py
External	Third-party modules (via pip)	numpy, pandas, flask
'''

# PIP is a package manager for python , used to install modules


import pyjokes
joke = pyjokes.get_joke()
print(joke)




# We can directly use calculator using this python by just opening terminal and typing python and perform any calc

# This opens REPL or Road Evaluate Print Loop (means this read, then evaluate then print and then move to loop(again))


print(''' This is used to print multiple lines 
      like i can write like this 
      i can add more number of lines''')

print("This is a string")

print(56)


import pyttsx3
engine = pyttsx3.init()


engine.say("This is a module which convert text into voice")
engine.runAndWait()





import os

# Get the current working directory
path = os.getcwd()

# OR specify a custom path
# path = "C:/Users/YourUsername/Desktop"

print(f"Contents of directory: {path}\n")

try:
    # List all files and directories in the given path
    contents = os.listdir(path)

    for item in contents:
        print(item)

except FileNotFoundError:    # There is no need to add this try block in this we can directly use this
    print("The specified path does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")


