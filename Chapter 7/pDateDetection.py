import re

testDate = '25/11/2020'

testFDate = '40/11/2020'

dateDetecRegex = re.compile(r'([0-3][1-9])/([01][1-9])/([0-2][0-9]{3})')

if dateDetecRegex.search(testDate) == None:
    print('You goofed')
else:
    print(dateDetecRegex.search(testDate).group(0))

if dateDetecRegex.search(testFDate) == None:
    print('The fake date is indeed false')

rDay, rMonth, year = dateDetecRegex.findall(testDate)[0]

month = int(rMonth)
day = int(rDay)


if month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
    print('Your date is wrong.')
elif month == 2 and day > 29:
    print('Your date is wrong')
elif day > 31:
    print('Your months have too many days.')
else:
    print('Nice date! Carry on.')

print(rDay + ' ' + rMonth + ' ' + year)