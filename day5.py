'''
any=[1," python is a language",67,68,[34,["this is python class"],78,"I'm looking for good bat"],[2,"this is 5th class",3],56]
print(any[4][1][0] [13])
list methods
---------------
1.append()
-->this method is used to add  new item into list,but it will add in the index position
syntax-->variable_name.append(item)
an =[1,2,3,4]
an.append(9)
print(an)
string is a mutable
so="python is a programming language"
print(so.replace("python","java"))

2. extend()
--------------
-->this methods is also used  to add new item into list, but this
extend add as each position to each index in the list
-->extend only takes itterables
syntax-->variable_name.extend(item(itterables))
a=[1,2,3,4]
a.extend("python")
print(a)

3.pop()
-------------
-->this is used delete an item from the list, this pop() remove the
value based on the index position mentioned in the parameters
-->if nothing is mentioned in the parameters, it will remove last
syntax-->variable_name.pop(index position)
list=[1,2,3,4,5]
list.pop(4)
print(list)

4. remove()
-------------
-->this is also used to delete item from the list,but remove()
method will delete value
list= [1,2,3,4,5]
list.remove(2)
print(list)

5.slicing()
-------------
-->this is used to get particular part of the list , string or tuple
-->this will work based on index position
syntax-->var[start index:end index]


len()
------------
-->method is used to find the number of items present in the list
list=[1,2,3,4,5]
print(len(list))
















