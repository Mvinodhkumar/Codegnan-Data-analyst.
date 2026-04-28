'''
Tuple
-------------
-->Tuple is a collection of different data types that represent by
() and the item in the tuple is separate by comma..
-->And tuple is immutable.
so=(1,"python",[7,8],(5,0),1)
print(so [1])
s1=(1,2,3,4,5)
s2=(6,7,8)
print(s1+s2)

Dictionary
-------------
-->Dict is a collection of key : value pair, where keys are immutable
(string ,int and tuple) and value are any data type this is represented
by{}
Methods
------------
Keys()
-----------
-->this is method is used to access only keys in the dictionary
syntax-->dict.keys()
my =  {"name": "vinodh",
       "age": 22,
       "edu": "b.tech"}
print (my.keys())


Values()
-----------
-->This is used to access only values in  the  dictionary
syntax-->dict.values()
my =  {"name": "vinodh",
       "age": 22,
       "edu": "b.tech"}
print (my.values())

item()
-----------
-->this method is used to access key: value pair in the dictionary
syntax-->dict.item()
my =  {"name": "vinodh",
       "age": 22,
       "edu": "b.tech"}
print (my.items())

clear()
------------
-->this clear () method is used to delete all the items in the dict
syntax-->dict.clear()
my =  {"name": "vinodh",
       "age": 22,
       "edu": "b.tech"}
print (my.clear())

update()
------------
-->This method is used to add new item (key : value) into the
dictionary
syntax-->
my =  {"name": "vinodh",
       "age": 22,
       "edu": "b.tech"}
print (my.update({"role" : "python developer"}))
print(my)

























