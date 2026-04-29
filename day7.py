'''
Set data type
--------------
-->set is collection of unordered elements or unique elements
unlike list or tuple set is not permit duplicates in side.

methods
--------------
add()
-->this method is used to add new item into the set
syntax-->variable_name.add(item)
sn = {1,2,3,2}
sn.add(4)
print(sn)

remove
--------------
-->this method is used to delete an item in the set
syntax-->variable_name.remove(value)
sn = {1,2,3,2}
sn.add(4)
print(sn)
sn.remove(3)
print(sn)

pop()
-------------
-->this is also used to delete element in the set,but we can not
specify the element
syntax-->variable_name.pop(no arguments)
sn={1,2,3,4,5}
sn.pop()
print(sn)

clear
--------------
-->This method is used to delete all elements in the set
syntax-->variable_name.clear()
sn={1,2,3,4,5}
sn.clear()
print(sn)

update
-------------
-->same like add,but this method will add more than one
element
syntax-->variable_name.update([elements])
sn={1,2,3,4,5}
sn.update([6,7,8,])
print(sn)

union
------------
-->this method will return a set all elements from both sets
duplicates
syntax-->set_1.union(set2) or set_1 | set_2
sn={1,2,3,4,5}
vn={4,6,8}
print(sn.union(vn))
print (sn | vn)

intersection()
-------------
-->This method will give only the common elements from both
sets
syntax-->set_1.intersection(set_2) or set_1or set_2 
sn={1,2,3,4,5}
vn={2,4,6}
print(sn.intersection(vn))
print(sn & vn)

difference()
-------------
-->This method is used to get the different elements from
both sets
syntax-->set_1.difference(set_2) or set 1-set2
sn={1,2,3,4,5,}
vn={2,4,6}
print(sn.difference(vn))

Type convertions
---------------
-->converting one data type into another data type
int-->string and float
a =9
b =str(a)
c =float(a)
print(c)

float-->string and int
s= 90.20
v= int(s)
i= str(s)
print(i)
print(type(i))

string-->int,float,list,tuple '''
v="99"
i=list(v)
print(i)
print(type(i))






































