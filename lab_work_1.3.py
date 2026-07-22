# Q-1
a=input("enter one: ")
a=int(a)
print(int(a),type(a))
a=float(a)
print(float(a),type(a))
a=bool(a)
print(bool(a),type(a))

# Q-2
a = float(input("enter a floating point number: "))
b = int(a)
print(a,"as an integer is",b)

# Q-3
a= bool(input("enter a boolean value (True / false) t and f should be capital: "))
inte=int(a)
str=str(a)
print(a,inte,str)

# Q-4
a=1
b=3.14
c="ahmed"
d=True
e=[1,2,3,4]
f=(1,2,3,4)
g={"name":"ahmed","age":20}
print("value:",a,"type:",type(a),"memory address:",id(a))
print("value:",b,"type:",type(b),"memory address:",id(b))
print("value:",c,"type:",type(c),"memory address:",id(c))
print("value:",d,"type:",type(d),"memory address:",id(d))
print("value:",e,"type:",type(e),"memory address:",id(e))
print("value:",f,"type:",type(f),"memory address:",id(f))
print("value:",g,"type:",type(g),"memory address:",id(g))

# Q-5
a=10
b=10
print(id(a))
print(id(b)) # memory address is same because both variables reference the same object in memory

a=10
b=20
print(id(a))
print(id(b)) # memory address is different because the variables reference different objects in memory
