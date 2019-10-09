#Caesar Cypher
message = input("Give me a message to encode.")
output = ""
key = int(input("Give me a key."))
for letter in message:
    new = ord(letter) + key
    newchar = chr(new)
    output += newchar
print(output)
    
