'''
print statement
----------------
-->This print shows output on the screen

return statement
----------------
-->Sends a value back to the caller or calling
for the program to reuse

def sum(a,b):
    return a+b
result=sum(9,10)
print(result)


Recursive function
-------------------
def fact(num):
    if num == 0 or num==-1:
        return 1
    return num * fact(num-1)
print(fact(6))'''

num = int(input("Enter Number:"))
def tables():
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
tables()
        
