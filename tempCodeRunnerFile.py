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
