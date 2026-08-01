# Q-1
fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
print(f"Hello, {fname} {lname}!")

# Q-2
fruit="apple"
price=5.50
print(f"The price of {fruit} is {price:.2f}")

# Q-3
str=input("enter your string: ")
print(f" your reversed string: {str[::-1]}")
if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Q-4
str=input("enter your string: ")
print(f" uppercase: {str.upper()}")
print(f" lowercase: {str.lower()}")
print(f" title: {str.title()}")

# Q-5
sent="Machine Learning and AI are trending"
print(sent.find("AI"))
print(sent.replace("AI", "Artificial Intelligence"))

word="data data mining and big data"
print(f"the word data appears {word.count("data")} times")

# Q-6
fruits="apple,banana,grapes"
print(fruits.split(","))

sent=["Python", "is", "awesome"]
print(" ".join(sent))

multiline='''pyhton
java
c
c++'''

lines=multiline.split("\n")
for i in lines:
    print(i)
# Q-7
sent="hello this is world"
print(f"does sententce starts with hello? {sent.startswith("hello")}")
print(f"does sentence end with world? {sent.endswith("world")}")

sent="Data123#Science!"
empty=""
for i in sent:
    if i.isalpha():
        empty+=i
    else:
        continue

print(f"String with non-alphabetic characters removed: {empty}")

s="python"
print(f"your reverse string is {s[::-1]}")