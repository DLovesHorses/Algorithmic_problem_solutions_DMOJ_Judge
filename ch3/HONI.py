#get input
input_string = input()

next_detect = 'H'

honi_instance = 0
for i in range(len(input_string)):

    if(input_string[i] == 'H' and next_detect == 'H'):
        next_detect = 'O'
    elif(input_string[i] == 'O' and next_detect == 'O'):
        next_detect = 'N'
    elif(input_string[i] == 'N' and next_detect == 'N'):
        next_detect = 'I'
    elif(input_string[i] == 'I' and next_detect == 'I'):
        next_detect = 'H'
        honi_instance += 1


print(honi_instance)
