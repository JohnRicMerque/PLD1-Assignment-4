# Program 2 using functions that return multiple values

def getNaplNorg():
    nOfApls = int(input("Enter the number of apples you want to buy: "))
    nOfOrgs = int(input("Enter the number of oranges you want to buy: "))
    return nOfApls, nOfOrgs

def getPrice(apl_number, org_number):
    apl_price = apl_number * 20
    org_price = org_number * 25
    total = apl_price + org_price
    return total

# start, calling functions and assigning them to variables
applesN, orangesN = getNaplNorg()
totalPrice = getPrice(applesN, orangesN)

print(f"The total amount is {totalPrice} pesos.")
