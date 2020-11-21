import re


def regStrip(words, *args):
    if not args:
        regexStrip = re.compile(r'\w+(\s\w+)*')

        return regexStrip.search(words).group()
    else:

        regexStripSpecific = re.compile(r'' + args[0])

        return regexStripSpecific.sub('',words)

        

stronsk = regStrip('         wanotwa     ','notw')

print(stronsk)