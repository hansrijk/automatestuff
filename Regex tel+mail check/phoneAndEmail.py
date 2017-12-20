#! python 3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 06-27369384, 0627369384, 06(-)27369384, 0320-288215, 038-1234567


# eerste gedeelte: 06, (06), 038, (038), 0320, (0320)
(
((\d\d)|(\(\d\d\))|(\d\d\d)|(\(\d\d\d\))|(\d\d\d\d)|(\(\d\d\d\d\)))? 



# spatie of streepje (optioneel)

(\s|-)?



# tweede gedeelte: 27369384, 288215, 1234567, 0627369384

(\d\d\d\d\d\d\d\d)|(\d\d\d\d\d\d)|(\d\d\d\d\d\d\d)|(\d\d\d\d\d\d\d\d\d\d)

)
''',re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+   # name part
@                 # @ symbol
[a-zA-Z0-9_.+]+   # domain name part

''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
