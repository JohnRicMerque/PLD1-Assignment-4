# Program 3 using functions that return multiple values

def getMoneyAplprice():
    moneyAmount = float(input("How much money do you have?: "))
    aplPrice = float(input("Enter the price of one apple: "))
    return moneyAmount, aplPrice

amountOfMoney, applePrice = getMoneyAplprice()
print(f"money = {amountOfMoney} and price = {applePrice}")