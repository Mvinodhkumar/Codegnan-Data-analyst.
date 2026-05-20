'''
Inheritance
------------
-->Inheriting the methods fromm the base to child

class parent:
    pass
class child(parent):
    pass

single inheritance
------------------

class animal:
    def sound(self):
        print("Animal make sounds")
class dog(animal):
    def bark(self):
        print("Dog bark")
D = dog()
D.sound()
D.bark()

Multiple inheritance
---------------------
class father:
    def skill_1(self):
        print("Driving")
class mother:
    def skill_2(self):        print("cooking")
class child(father,mother):
    def all_skill(self):
        print("coding")
c = child()
c.skill_1()
c.skill_2()
c.all_skills()

Hierarchical inheritance
------------------------
-->multiple child classes inherits from one base class

class father:
    def property(self):
        print("father property")
class child_1(father):
    def car(self):
        print("first child car")
class child_2(father):
    def flat(self):
        print("second child flat")
c1 = child_1()
c2 = child_2()
c1.property()
c1.car()
c2.property()
c2.flat()

Hybrid inheritance
------------------
-->'''
class A:
    def methodA(self):
        print("class A")
class B(A):
    def methodB(self):
        print("class B")
class C(A):
    def methodC(self):
        print("class C")
class D(B,C):
    def methodD(self):
        print("class D")

any = D()
any.methodA()
any.methodB()
any.methodC()
any.methodD()

super()method
---------------
-->the super () method is used to call methods or constructor from
the parent class
class parent:
    def __init__(self):
        print("parent constructor")
class child(parent):
    def __init__(self):
        super





        

































































