no_of_lines = int(input())
op_string = ''
for line in range(no_of_lines):
    string = input()
    string += ' '
    i = 0
    j = 0
    char_count = 0
    scanned_part = 0
    cur_char = string[0]

    while scanned_part < len(string):


        iterator = string[j]

        if iterator == cur_char:
            j += 1
            char_count += 1
        else:
            op_string += str(char_count) + ' ' + str(cur_char) + ' '
            #print(op_string)
            i = j
            cur_char = string[i]
            char_count = 0

        '''if (scanned_part == len(string)-1):
            op_string += str(char_count) + ' ' + str(cur_char)
            #print(op_string)
            #print(len(string) - 1)
'''
        scanned_part = j
    op_string = op_string[:-1] + '\n'

print(op_string)