import pyinputplus as pyip 

print('HELLO AND WELCOME TO BREAD CREATOR 2020')
print('PLEASE ASSEMBLE YOUR SANDWICH BY HELP OF THE FOLLOWING PROMPTS')

price = 0

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt = 'Please pick a BREAD type:')
if bread == 'wheat':
    price += 0.8
elif bread == 'white':
    price += 0.65
else:
    price += 0.85

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],prompt='Please pick a PROTEIN type:')

if protein == 'chicken':
    price += 1.2
elif protein == 'turkey':
    price += 1.5
elif protein == 'ham':
    price += 0.75
else:
    price += 2

verifyCheese = pyip.inputYesNo(prompt='Would you like some CHEESE with that?')
if verifyCheese == 'yes':
    cheese = pyip.inputMenu(['cheddar','Swiss','mozzarella'], prompt='Which CHEESE would you like?')
    if cheese == 'cheddar':
        price += 0.3
    elif cheese == 'Swiss':
        price += 0.5
    else:
        price += 0.35

verifyMayo = pyip.inputYesNo(prompt='Would you like some MAYO?')
if verifyMayo == 'yes':
    price += 0.1

verifyMustard = pyip.inputYesNo(prompt='How about some MUSTARD?')
if verifyMustard == 'yes':
    price += 0.1

verifyLettuce = pyip.inputYesNo(prompt = 'We also have some LETTUCE her if you wanted some?')
if verifyLettuce == 'yes':
    price += 0.25

verifyTomato = pyip.inputYesNo(prompt = 'Tomato, tom- ah -to. However you humans pronounce it...Would you like some slices?')
if verifyTomato == 'yes':
    price += 0.4

amount = pyip.inputInt(prompt='How many of these bad boys do you want in your order?')

print('YOUR ORDER AMOUNTS TO %s$ WITH THE BASE PRICE OF ONE SANDWICH BEING %s$.' % (price*amount,price))
