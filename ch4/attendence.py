next_number = int(input())

text = input()

no_of_takes = 0
no_of_serve = 0

while(text != 'EOF'):
    if(text == 'TAKE'):
        no_of_takes += 1
        next_number += 1
        if((next_number % 999) == 0):
            next_number = 0

    if(text == 'SERVE'):
        no_of_serve += 1

    if(text == 'CLOSE'):
        print(no_of_takes, no_of_takes - no_of_serve, next_number)
        no_of_takes = 0
        no_of_serve = 0

    text = input()

