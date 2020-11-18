import copy

spam = ['apples', 'bananas','tofu','cats', 'pastrami']
superImportantListOfThings=[]

spam = copy.copy(superImportantListOfThings)

if(len(spam) > 0):
    for i in range(len(spam) - 1):
        print(spam[i], end=', ')
    print(' and ' + spam[-1] + '.')
else:
    print('This list holds nothing, you just handed me an empty piece of paper.')