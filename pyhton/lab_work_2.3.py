# Q-1
num = int(input("enter 0 to exit: "))
while num != 0:
    num = int(input("enter 0 to exit: "))
print("exited")

# Q-2
for i in range(1,11):
    print(f"{i} squared is {i**2}")

# Q-3
i=1
while i<=50:
    if i % 2==0:
        print(i)
    i += 1

# Q-4
for i in range(1,21,2):
    print(f"odd numbers = {i}")

# Q-5
for i in range(5,51,5):
    print(f"multiples of 5 = {i}")

# Q-6
for i in range(10,0,-1):
    print(f"reverse countdown={i}")

# Q-7
for i in range(1,51):
    if i % 2 == 0:
        if i % 3==0:
            print(f"{i} divisible by both")
        else:
            print(f"{i} divisible by 2")
    else:
        if i % 3==0:
            print(f"{i} divisible by 3")
        else:
            print(f"{i} not divisible by 2 and 3")