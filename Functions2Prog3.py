# Program 3 using functions that return multiple values

def getMoneyAplprice():
    moneyAmount = float(input("How much money do you have?: "))
    aplPrice = float(input("Enter the price of one apple: "))
    return moneyAmount, aplPrice

def getMaxApples(money, price):
    maxApls = int(money//price)
    return maxApls

def getChange(money, price):
    change = money%price
    return change

amountOfMoney, applePrice = getMoneyAplprice()
max_apples = getMaxApples(amountOfMoney, applePrice)
total_change = getChange(amountOfMoney, applePrice)

print(f"You can buy {max_apples} apples and your change is {total_change} pesos.")
