message = input()
index = 0
decoded_text = ''
while(index < len(message)):
    decoded_text += message[index]
    if(message[index] in 'AaEeIiOoUu'):
        index += 3
    else:
        index += 1


print(decoded_text)