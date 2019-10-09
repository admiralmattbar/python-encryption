#Transposition Cypher


def getMessage():
    action = input("(e)ncode, (d)ecode, or (q)uit?")
    if action == 'e':
        m = input("Type message to encode.")
    elif action == 'd':
        m = input("Type message to decode.")
    elif action == 'q':
        exit()
    else:
        print("Please type 'e' or 'd'!")
        selectAction()
    return m, action;

def roundNum(num):
    new = round(num, 0)
    if new >= num:
        return new
    elif new < num:
        return new + 1

message, a = getMessage()

key = int(input("What is the key?"))

def encode(mess, k):
    code = [""] * k
    for col in range(k):
        char = col
        while char < len(mess):
            code[col] += mess[char]
            char += k
    print(code)
    return ''.join(code)

def decode(mess, k):
    col = roundNum(len(mess)/k)
    row = k
    code = [""] * 

if a == 'e':
    print(encode(message, key))
elif a == 'd':
    print(decode(message, key))

