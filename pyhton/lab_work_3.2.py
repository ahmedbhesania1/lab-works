# Q-1
fruits=["apple","banana","cherry","watermelon","grape"]
print(fruits[1],fruits[4])

fruits.append("mango")
print(fruits)
fruits.pop(0)
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)


# Q-2
num=(1,2,3,4,5)
print(num[2])
# num[1]=10 # it will give error because tuples are immutable


# Q-3
l=[1,2,3]
t=(1,2,3)

l[0]=10
print(l)
# t[0]=10 # this will give an error because tuples are immutable

# Q-4
sq=[i*i for i in range(1,11)]
print(sq)

num=[i for i in range(1,21)]
print(num)
new=[i for i in num if i %2==0]
print(new)


str=["hello","WORLD","PytHoN"]
new=[i.lower() for i in str]
print(new)