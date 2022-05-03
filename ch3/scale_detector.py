#get input
composition = input()

#make list
sequence = composition.split('|')

#count variables
a_minor_count = 0
c_major_count = 0

#print(sequence)
#get first character of each sequence
for i in range(len(sequence)):
    first_char = sequence[i][0]
    #print(sequence[i][0])
    if first_char in 'ADE':
        a_minor_count += 1

    if first_char in 'CFG':
        c_major_count += 1


#decision logic
scale = ''
if(a_minor_count > c_major_count):
    scale = 'A-mol'

elif(c_major_count > a_minor_count):
    scale = 'C-dur'

else:
    #get the last char of the last element of the list
    char = sequence[len(sequence) - 1][len(sequence[len(sequence) - 1]) - 1]

    if (char == 'A'):
        scale = 'A-mol'
    if (char == 'C'):
        scale = 'C-dur'

    #print(char)

print(scale)
