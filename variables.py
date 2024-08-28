# Rules for Python variables
# A Python variable name must start with a letter or the underscore character.
# A Python variable name cannot start with a number.
# A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
# The reserved words(keywords) in Python cannot be used to name the variable in Python.

a = 10
b = "Soutik"
c = 2.34
print(a+c)

_var = "qw123"
print(_var)
v_ar = 1245
print(v_ar)

# Local and Global Variables

#Local

def fun():
    a = "Soutik"
    print(a)

a = "Sudipa"
fun()
# Output Soutik

# Global

def f():
    print(a)

a ="Ronaldo"
f()

# Rules of global keyword
# If a variable is assigned a value anywhere within the function’s body, it’s assumed to be local unless explicitly declared as global.
# Variables that are only referenced inside a function are implicitly global.
# We use a global in Python to use a global variable inside a function.
# There is no need to use a global keyword in Python outside a function.

x = 10

def fun1():

    global x
    x= x + 10
    print(x)

fun1()
print(x)

# Built-in Python Data types are:
# Numeric
# Text Type
# Sequence Type (Python list, Python tuple, Python range)
# Boolean
# Set
# Dictionary


