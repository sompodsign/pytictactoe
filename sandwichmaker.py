

# Sandwich maker
import pyinputplus as pyip, re

currSign = 'US$'

#Gives pyip.inputMenu a nice list to print
def forPrint(dic): 
    lPrdct = len(max(list(dic.keys()), key=len)) #len of longest product
    lPrice = len(str(max(dic.values()))) #len of longest price
    ppList = [] #Product-and-price list
    
    for prdct, price in dic.items():
        ppList.append(prdct.ljust(lPrdct + 3, '.') + currSign + '  ' + str(price).rjust(lPrice))
    return ppList
    
    
#Dictionary of products and prices
ingredients = {
    'bread': {'wheat': 5,'white': 4,'sourdough': 6},
    'protein': {'chicken': 8, 'turkey': 10, 'ham': 5, 'tofu': 7},
    'yncheese': {'cheddar': 2, 'swiss': 3, 'mozzarella': 2},
    'yncondiment': {'mayo': 0.5, 'ketchup': 0.5, 'mustard': 0.5},
    'ynvegetables': {'lettuce': 1,'tomato': 1}
}

total = qty = 0
for ingredient in ingredients:
    #if ingredient starts with 'yn', ask if they want it
    if re.search(r'^yn', ingredient):
        #remove 'yn' from ingredient's name
        choice = pyip.inputYesNo(prompt = 'Do you want %s? (Y/N)\n' % ingredient[2:])
        if choice == 'yes':
            print('Choose your {}.'.format(ingredient[2:]))
            choice = pyip.inputMenu(forPrint(ingredients[ingredient]), numbered = True)
            total += ingredients[ingredient][re.search(r'^\w+', choice).group()]
            print('You chose {} for {}.\nRunning total is: {} {}\n'.format(choice, ingredient[2:], currSign, total))
            continue
        else:
            continue
    #ingredients[ingredient] is a dictionary
    print('Choose your {}.'.format(ingredient))
    choice = pyip.inputMenu(forPrint(ingredients[ingredient]), numbered = True)
    total += ingredients[ingredient][re.search(r'^\w+', choice).group()]
    print('You chose {} for {}.\nRunning total is: {} {}\n'.format(choice, ingredient, currSign, total))
else:
    print('A sandwich like that is {} {}'.format(currSign, total))
    qty = pyip.inputNum(prompt = 'How many do you want?', min = 1)
    print('Your total is {} {}'.format(currSign, total * qty))