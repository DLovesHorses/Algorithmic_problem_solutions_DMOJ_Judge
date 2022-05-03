no_of_EOB = 0
colour_list = ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']
test_case_string = ''
hand_limit = 7
normal_time = 13
red_time = 16

while(no_of_EOB < 10):
    input_string = input()

    if(input_string != 'end of box'):
        test_case_string += input_string + ' '

    else:
        no_of_EOB += 1
        total_sec = 0

        for i in colour_list:
            if(i != 'red'):
                #print(f'color: {i}, freq: {test_case_string.count(i)}')
                int_part = test_case_string.count(i) // hand_limit
                frac_part = test_case_string.count(i) % hand_limit
                multiplier = 0
                if(frac_part == 0):
                    multiplier = int_part
                else:
                    multiplier = int_part + 1

                total_sec += normal_time * multiplier
                #print(f'{normal_time} * {multiplier} = {normal_time * multiplier}, accumulated time = {total_sec}')

            else:
                total_sec += red_time * test_case_string.count(i)

        print(total_sec)
        test_case_string = ''

#print(test_case_string)