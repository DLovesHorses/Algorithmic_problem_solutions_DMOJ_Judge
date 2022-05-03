playlist = 'ABCDE'
button = int(input())
presses = int(input())
while (button != 4 or presses != 1):
    for i in range(presses):
        if(button == 1):
            playlist = playlist[1:] + playlist[0]

        elif(button == 2):
            playlist = playlist[-1] + playlist[:-1]

        elif(button == 3):
            playlist = playlist[1] + playlist[0] + playlist[2:]

    button = int(input())
    presses = int(input())

output = ''
for i in range(len(playlist)):
    output += playlist[i] + ' '
output = output[:-1]
print(output)
