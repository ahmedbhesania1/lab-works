# Q-1

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1>num2:
    if num1>num3:
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else:
    if num2>num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

# Q-2
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1<num2:
    if num1<num3:
        print(f"{num1} is smallest")
    else:
        print(f"{num3} is smallest")
else:
    if num2<num3:
        print(f"{num2} is smallest")
    else:
        print(f"{num3} is smallest")    

# Q-3

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
num4=int(input("Enter the fourth number: "))

if num1>num2:
    if num1>num3:
        if num1>num4:
            print(f"{num1} is greatest")
        else:
            print(f"{num4} is greatest")
    else:
        if num3>num4:
            print(f"{num3} is greatest")
        else:
            print(f"{num4} is greatest")
else:
    if num2>num3:
        if num2>num4:
            print(f"{num2} is greatest")
        else:
            print(f"{num4} is greatest")
    else:
        if num3>num4:
            print(f"{num3} is greatest")
        else:
            print(f"{num4} is greatest")

# Q-4
operator=input("enter any operator(+,-,*,/): ")
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))

match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("Invalid operator")

# Q-5
print("press 1 for pizza")
print("press 2 for burger")
print("press 3 for pasta")
choice=int(input("enter your choice: "))
match choice:
    case 1:
        print("press 1 for thin crust pizza")
        print("press 2 for cheese burst pizza")
        print("press 3 for veggie pizza")
        choices=int(input("enter your choice: "))
        match choices:
            case 1:
                print("You have selected thin crust pizza")
            case 2:
                print("You have selected cheese burst pizza")
            case 3:
                print("You have selected veggie pizza")
            case _:
                print("Invalid choice")
    case 2:
        print("you have selected burger")
    case 3:
        print("you have selected pasta")
    case _:
        print("Invalid choice")

# Q-6
print("1. English")
print("2. Hindi")
print("3. Gujarati")

lang = int(input("Choose Language: "))

match lang:

    case 1:
        print("1. Balance")
        print("2. Recharge")

        option = int(input("Choose: "))

        match option:
            case 1:
                print("Your balance is $50")
            case 2:
                print("Recharge Successful")
            case _:
                print("Invalid Option")

    case 2:
        print("1. बैलेंस")
        print("2. रिचार्ज")

        option = int(input("चुनें: "))

        match option:
            case 1:
                print("आपका बैलेंस $50 है")
            case 2:
                print("रिचार्ज सफल")
            case _:
                print("अमान्य विकल्प")

    case 3:
        print("1. બેલેન્સ")
        print("2. રિચાર્જ")

        option = int(input("પસંદ કરો: "))

        match option:
            case 1:
                print("તમારું બેલેન્સ $50 છે")
            case 2:
                print("રિચાર્જ સફળ")
            case _:
                print("અમાન્ય વિકલ્પ")

    case _:
        print("Invalid Language")