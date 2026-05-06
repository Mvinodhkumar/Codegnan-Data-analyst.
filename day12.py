'''
Functions
----------
-->This is a block of code that can be reusable
-->A function can only run when it is called
-->def is the keyword is to define the function
def func_name(parameters):
    ----------
    ----------
    func_name(arguments)
num=9
def even_odd(num):
    if num % 2 ==0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
even_odd(num)
even_odd(120)

Required arguments
-------------------
-->A function must called with the correct number of
arguments, that means if function expect 2 arguments,
we have to call the function  with 2 arguments not less or
not more
eg-
def even_odd(num,num_2):
    print(num+num_2)
even_odd(9,10)

Default Arguments
------------------
-->By default, value is taken from the calling function
def even_odd(name="vinodh"):
    print(f"hai {name}")
even_odd("kumar")

keyword
--------
-->Here, we can send arguments with key = value
syntax-
by this, the order of argument does  not matter
def even_odd(num,num_2,num_3):
    print(num+num_2+num_3)
even_odd(num=9,num_2=9,num_3=9)

Variable length argument
-------------------------
-->Adding a star(*) before the parameter name in the
function, receive a tuple of arguments and can be access
item with indexes'''
def name(name)
    print(name[])
name("vinodh","kumar")
































