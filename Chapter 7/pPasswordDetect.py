import re, time

def passTrial(passwort):

    regexLength = re.compile(r'^\w+$')
    regexUppercase= re.compile(r'[a-z]*')
    regexLowercase = re.compile(r'[A-Z]*')
    regexDigit = re.compile(r'[0-9]')

    flags = 0

    if regexLength.search(passwort) and len(regexLength.search(passwort).group()) >= 8:
        print('Good length')
        flags +=1
        time.sleep(0.5)
        if regexUppercase.findall(passwort):
            print('Got some UPPERCASE letters, nice.')
            flags += 1
            time.sleep(0.5)
        if regexLowercase.findall(passwort):
            print('ooooh some lowercasies, how cute')
            flags += 1
            time.sleep(0.5)
        if regexDigit.search(passwort):
            print('DIGITized, use those numbers well, chief!')
            flags +=1
            time.sleep(0.5)
    print('Churning password strength...')
    time.sleep(2)
    if flags != 4:
        print('Weak pass, buddy. Try again!')
    else:
        print('Acceptably bulky pass, bro. Keep it up!')


passTrial('Wandm4nn')