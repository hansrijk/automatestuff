import re



phoneNumRegex = re.compile(r'''
# 06-27369384, 0627369384, 06(-)27369384, 0320-288215, 038-1234567


# eerste gedeelte: 06, (06), 038, (038), 0320, (0320)

((\d\d)|(\(\d\d\))|(\d\d\d)|(\(\d\d\d\))|(\d\d\d\d)|(\(\d\d\d\d\)))?  



# spatie of streepje (optioneel)

(\s|-)



# tweede gedeelte: 27369384, 288215, 1234567

((\d\d\d\d\d\d\d\d)|(\d\d\d\d\d\d)|(\d\d\d\d\d\d\d))+


''',re.VERBOSE)

print(phoneNumRegex.findall('Bel me morgen op dit nummer: of 1234567890,  23-45678901,  of op mijn kantoornummer: 34 56789012 of 456-7890123 of 5678-901234 of (67)89012345 of (7890)123456'))

