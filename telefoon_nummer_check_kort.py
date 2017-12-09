import re



phoneNumRegex=re.compile(r'(\d\d(-)?\d(-)?\d(-)?\d\d\d\d\d\d)')
print(phoneNumRegex.findall('Bel me morgen op dit nummer: 06-33843423, of 0634825693 of op mijn kantoornummer: 0320-288215 of 032-0288215.'))

