# Program 1 using functions that return multiple values

def getNameAgeAddress():
    name_ = input("Name: ")
    age_ = int(input("Age: "))
    add_ = input("Address: ")
    return name_, age_, add_

def display(nameF, ageF, addF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF}.")

#steps
# 1. ask for name, age, and address
name, age, add = getNameAgeAddress()

# 2. display
display(name, age, add)
