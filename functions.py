# function declaration in python
# Arguments passing in python


def my_function():
    print("Hello from the function")
my_function()

def my_function(arg):
    print("Hello "+arg)
my_function("Bittu")

def my_function(lname,fname):
    print("Hello beta ",fname,lname)
my_function("Chincholkar","Akshay")

def my_function(*kids):
    print("Youngest kid is "+kids[2])
my_function("Akshay","Manam","Nita","Subhash")

# Naming of formal parameters should match
def my_function(c,a,b):
    print("c:",c," b:",b)
my_function(a=1,b=2,c=3)

# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
def my_function(**args):
    print(args["fname"],args["lname"])
my_function(fname = "Akshay",lname = "Chincholkar")