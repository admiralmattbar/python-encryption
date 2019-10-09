#Caesar Cypher Program

action = input("(e)ncode or (d)ecode?")

user_message = input("Insert code here.")
key = int(input("What is the key?"))

def encode(message):
    output = ""
    for x in message:
        if isCap(x):
            code = ord(x) + key
            if code > ord('Z'):
                code = ord('A') + (code - ord('Z')) - 1
            elif code < ord('A'):
                code = ord('Z') - (ord('A') - code) + 1
        elif isLower(x):
            code = ord(x) + key
            if code > ord('z'):
                code = ord('a') + (code - ord('z')) - 1
            elif code < ord('a'):
                code = ord('z') - (ord('a') - code) + 1
        else:
            code = ord(x)
        output += chr(code)
    return output

def decode(message):
    output = ""
    for x in message:
        if isCap(x):
            code = ord(x) - key
            if code > ord('Z'):
                code = ord('A') + (code - ord('Z')) - 1
            elif code < ord('A'):
                code = ord('Z') - (ord('A') - code) + 1
        elif isLower(x):
            code = ord(x) - key
            if code > ord('z'):
                code = ord('a') + (code - ord('z')) - 1
            elif code < ord('a'):
                code = ord('z') - (ord('a') - code) + 1
        else:
            code = ord(x)
        output += chr(code)
    return output

def isCap(letter):
    if ord(letter) <= ord('Z') and ord(letter) >= ord('A'):
        return True
    else:
        return False

def isLower(letter):
    if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
        return True
    else:
        return False

if action == "e":
    print(encode(user_message))
elif action == "d":
    print(decode(user_message))
