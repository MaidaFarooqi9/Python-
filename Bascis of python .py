print("hello") #just printing
x=5 #variable #no command for declaring
print(type(x)) #print  data type of x

a=2
b=5
print(a*b)

y=input("enter kro kuch bhi") #y will store input value

if(y==""):
    print("y is a string")
else:
    print("y is integer or maybe string or maybe mujhy nh pta")
z=6
if(z > 4 and z < 8):
    print("correct")
else:
    print("not correct")

#functions
def say_hi(name):
    print("hello my name is "+name)

say_hi("maida")
t=input("your name")
say_hi(t)

#classes and objects

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def actual_func(a):
         print(a.name+" "+a.age)

u=input("name")
v=input("age")
p1=Person(u,v)
p1.actual_func()

#inheritance
class Car(Person):
    pass #no own func if class car
class vehicle(Person):
    def __init__(self,vname,vno):
        self.vn=vname
        self.vnum=vno

    def Details(b):
        print(b.vn+""+b.vnum)

C1=Car("david","45")
C1.actual_func()
s=input("name of vehicle")
t=input("Id of vehicle")

V1=vehicle(s,t)
V1.Details()
