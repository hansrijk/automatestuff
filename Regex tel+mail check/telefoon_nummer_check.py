def isPhoneNumber(text): # 415-333-5548
    if len(text)!=12:
        return False #niet lang genoeg
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #geen area code
        if text [3]!='-':
            return False #geen 1e streepje
        for i in range (4,7):
            if not text[i].isdecimal():
                return False #geen eerste 3 cijfers
            if text [7]!='-':
                return False #geen 2e streepje
            for i in range (8,12):
                if not text[i].isdecimal():
                    return False #geen laatste 4 cijfers
            return True

message='Bel me morgen op dit nummer: 063-384-3423 of op mijn kantoornummer: 032-028-8215.'
foundNumber=False
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('telefoon nummer gevonden: '+chunk)
        foundNumber=True
if not foundNumber:
        print('geen telefoonnummer gevonden')
        
