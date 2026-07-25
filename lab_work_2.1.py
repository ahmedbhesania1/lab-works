# Q-1
num = int(input("enter a number: "))

if num % 2==0:
    print("even")
else:
    print("odd")

# Q-2 
age =int(input("enter your age: "))
if age <=12:
    print("child")
else:
    if age<=19:
        print("teenager")
    else:
        if age<=59:
            print("adult")
        else:
            print("old age")



# Q-3
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
num3=int(input("enter 3rd number: "))

if num1>=num2 and num1>=num3:
    print(f"{num1} is greatest")
elif num2>=num3:
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")

# Q-4
num=int(input("enter a number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("neutral")
    
