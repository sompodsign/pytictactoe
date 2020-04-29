import pyinputplus as pyip

wheatPrice = 1.50
whiteprice = 1.00
sourdoughPrice = 1.60

print('What type of breed would you like?')
breed = pyip.inputMenu(['wheat', 'white', 'sourdough'])
print(f"You've choosen {breed}.")

if breed == 'wheat':
    breedPrice = wheatPrice
elif breed == 'white':
    breedPrice = whiteprice
elif breed == 'sourdough':
    breedPrice = sourdoughPrice

chickenPrice = 2.00
turkeyPrice = 1.75
hamPrice = 2.20
tofuPrice = 1.00

print('What type of protein would you like? ')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
print("You have chosen " + protein + ".")

if protein == 'chicken':
    proteinPrice = chickenPrice
elif protein == 'turkey':
    proteinPrice = turkeyPrice
elif protein == 'ham':
    proteinPrice = hamPrice
elif protein == 'tofu':
    proteinPrice = tofuPrice


print(f"Your Sandwich has now {breed} and {protein}.")

cheddarPrice = 0.40
swissPrice = 0.50
mozzarellaPrice = 0.70
noCheese = 0.00

print("Would you like cheese? ")
response = pyip.inputYesNo()

if response == "yes":
    cheese = pyip.inputMenu(['cheddar','swiss','mozzarella'])
else:
    cheese = 'no Cheese'

print(f"You have choosen {cheese}.")

if cheese == 'cheddar':
    cheesePrice = cheddarPrice
elif cheese == 'swiss':
    cheesePrice = swissPrice
elif cheese == 'mozzarella':
    cheesePrice = mozzarellaPrice
elif cheese == 'no Cheese':
    cheesePrice = noCheese

mayoPrice = 0.40
musturdPrice = 0.50
lettucePrice = 0.88
tomatoPrice = 1.00
noCondimentPrice = 0.00

print("Would you like a condiment? ")
response = pyip.inputYesNo()
if response == 'yes':
    condiment = pyip.inputMenu(['mayo', 'musturd', 'lettuce', 'tomato'])
else:
    condiment = 'no condiment'

print(f"You have choosen {condiment}.")

if condiment == 'mayo':
    condimentPrice = mayoPrice
elif condiment == 'musturd':
    condimentPrice == musturdPrice
elif condiment == 'lettuce':
    condimentPrice == lettucePrice
elif condiment == 'tomato':
    condimentPrice = tomatoPrice
elif condiment == 'no condiment':
    condimentPrice = noCondimentPrice

print(f"Your sandwich will be made with {breed} breed, {protein}, {cheese}, and {condiment}.")

print("How many sandwiches would you like?")
quantityofSandwiches = pyip.inputInt(min=1)
print(f"Great! we will make {str(quantityofSandwiches)} for you.")

sandwichPrice = breedPrice + proteinPrice + cheesePrice + condimentPrice
totalPrice = quantityofSandwiches * sandwichPrice

print(f"Each Sandwich has a price of ${str(sandwichPrice)}. Your total price comes to ${str(totalPrice)}.")
    