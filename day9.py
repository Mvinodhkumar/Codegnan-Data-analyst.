'''
elif statement
---------------
-->This statment gives more options to get result of
that program
marks_stu = int(input("Enter your marks:"))
if marks_stu >=90:
 print("a+")
elif marks_stu >=80:
 print("a")
elif marks_stu >=70:
 print("b+")
elif marks_stu >=60:
 print ("b")
elif marks-stu >=50:
 print ("c+")
else:
 print("failed")

Nested if statement
--------------------
-->if statement in side another if statement is called
nested if statement 

user_SBI_info = {"ATM PIN" : "9999"}
user_pin = input ("Enter your ATM:")
if len (user_pin)==4:
    if user_pin in user_SBI_info['ATM PIN']:
        print("WELCOME tO SBI ATM")
    else:
        print("pls enter the correct pin")
else:
    print("pls enter 4 digit pin")

For statement
-------------
-->A for statement used ton iterate over items like
(string,list,tuple) with fixed number of itterations


Else statement in for
----------------------
-->After completing all itteration this else statement will
excute
any=[9,8,7,6]
for j in any:
    print(j)
else:
    print("loop finished")'''

so = "vinodh"
empty = ""
for j in so:
    empty = j + empty
if empty ==so:
    print("palindrome")
else:
    print("not a palindrome")


















