'''
pattern programs
------------------
num = int(input("Enter number:"))
for j in range(1,num+1):
    for j in range(1,j+1):
        print("*",end ="")
    print()

num = int(input("Enter number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


num = int(input("Enter number:"))
for i in range (num):
    for j in range(num-i-1,0,-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()'''

num_1 = 8
num_2 = 9
choice_ = int(input("\n1.add \n2.sub :"))
if choice_==1:
    print(num_+ num_2)
elif choice_==2:
    print(num_- num2)
