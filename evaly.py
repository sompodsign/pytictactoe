import pyinputplus as pyip

price = pyip.inputInt('Please Enter the product price: ')
discount = pyip.inputInt('Please enter the discount percentage: ')

divident = 1

if discount == 50:
    divident = 1.5
elif discount == 60:
    divident = 1.6
elif discount == 70:
    divident == 1.7
elif discount == 80:
    divident = 1.8
elif discount == 90:
    divident = 1.9
elif discount == 100:
    divident = 2

fullPayReturn = price * (discount/100)
parTialPay = price / divident
partialCashback = parTialPay * (discount/100)
save = price - parTialPay
print('\n')
print("-----FULL PAYMENT-----")
print(f"If you pay the full amount '{price} TAKA' you will receive cashback: {fullPayReturn} TAKA \n")
print("-----PARTIAL PAYMENT-----")
print(f"If you want to pay partial amount you have to pay {parTialPay} TAKA. You will get cashback {partialCashback}."
      f" So you get {partialCashback} TAKA discount.")

