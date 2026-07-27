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