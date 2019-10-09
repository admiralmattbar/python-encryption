#Caesar Cypher Brute Force

message = input("What is the coded message?")

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

for num in range(1,26,1):
    output = ""
    for x in message:
        if isCap(x):
            code = ord(x) - num
            if code > ord('Z'):
                code = ord('A') + (code - ord('Z')) - 1
            elif code < ord('A'):
                code = ord('Z') - (ord('A') - code) + 1
        elif isLower(x):
            code = ord(x) - num
            if code > ord('z'):
                code = ord('a') + (code - ord('z')) - 1
            elif code < ord('a'):
                code = ord('z') - (ord('a') - code) + 1
        else:
            code = ord(x)
        output += chr(code)
    print(str(num) + ": ")
    print(output)


