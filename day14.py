'''
num=0
num_1=1
any = int(input("Enter a number:"))
print(num,num_1,end=" ")
for j in range(1,any+1):
    num2 = num+num_1
    num=num_1
    num_1=num_2
    print(num_2,end=" ")


Amstrong=int(input("Enter number:"))
print(len(str(Amstrong)))


Amstrong  = 999
total=0
length = len(str(Amstrong))
for j in str(Amstrong):
    total +=int(j) ** length
if total == Amstrong:
    print(f"{Amstrong} is a Amstrong number")
else:
    print(f"{Amstrong} is not Amstrong number")


num= int(input("Enter a number:"))
if num%3==0 and num%5==0:
    print(f" divisible by 3 and 5 {num}")
else:
    print("Not")

num = 9
def divi (num):
    for i in range(1,num+1):
        if i%3==0 and 5==0:
            print(f"{i} is divi by 3 and 5")
divi(num)

any = [1,2,3,4,5]
def sum_even(any):
    total = 0
    for j in any:
        if j%2==0:
            total += j
    print(total)
sum_even(any)

Lambda Function
----------------
-->A lambda function is a small anonymus function
-->This lambda function can take n number of arguments but
can only have one expression
syntax-->lambda keyword (arguments)"expression
'''
an =  lambda a,b:a*b
print(an(9))















        
