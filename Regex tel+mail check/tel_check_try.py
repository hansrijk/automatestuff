#! python 3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 06-27369384, 0627369384, 06(-)27369384, 0320-288215, 038-1234567


# eerste gedeelte: 06, (06), 038, (038), 0320, (0320)
(
(\d\d\d\d\d\d\d\d\d\d)|(\(\d\d\)\d\d\d\d\d\d\d\d)|(\d\d-\d\d\d\d\d\d\d\d)|(\(\d\d\d\)\d\d\d\d\d\d\d)|(\d\d\d-\d\d\d\d\d\d\d)|(\d\d\d\d-\d\d\d\d\d\d)|(\(\d\d\d\d\)\d\d\d\d\d\d)
)


''',re.VERBOSE)

phoneRegex.findall('Bel me morgen op dit nummer: 06-33843423, of 0634825693 of op mijn kantoornummer: 0320-288215 of 032-0288215.')

# List results, etc
