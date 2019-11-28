import re

dateRegex = re.compile(r'''
    (\d|\d{2}|\d{4}) #first group of numbers
    ([-\s./])        #separator
    (\d{2}|\d{4})    #second group of numbers
    ([-\s./])        #separator2: elecric boogaloo
    (\d{4}|\d{2})    #third group of numbers

    ''', re.VERBOSE)

dateText = '''
            Is it 11/28/2019, 11-28-2019, 2019/11/28, 2019/28/11,
            2019.11.28, or 2019.28.11.
            Which date format should be the best?
           '''


matches= []
for groups in dateRegex.findall(dateText):
    dates = '/'.join([groups[0],groups[2],groups[4]])
    matches.append(dates)
print(matches)
