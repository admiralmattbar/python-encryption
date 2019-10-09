#Caesar Decode
message = input("Give me a message to decode.")
output = ""
key = int(input("Give me a key."))
for letter in message:
    new = ord(letter) - key
    newchar = chr(new)
    output += newchar
print(output)
