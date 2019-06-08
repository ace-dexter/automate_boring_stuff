
#   415-555-4242
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True


message = 'Call me at 415-555-9999 tomorrow. 415-555-9999 is my office'
print('lenof messgae is ', len(message))
for i in range(len(message)):
    chunk = message[i:i+12]
    print('chunk is: ', chunk)
    if is_phone_number(chunk):
        print('phone number found: ' + chunk)


print('Done')
