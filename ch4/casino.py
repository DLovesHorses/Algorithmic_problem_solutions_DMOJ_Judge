#initial number of quarters
no_of_quarters = int(input())

#initial number of times slots machines were played
initial_A = int(input())
initial_B = int(input())
initial_C = int(input())

#tracker variables
num_played_A = 0
num_played_B = 0
num_played_C = 0

next_machine = 'A'

while(no_of_quarters != 0):
    #print(no_of_quarters)
    no_of_quarters -= 1

    if(next_machine == 'A'):
        num_played_A += 1
        if(((num_played_A + initial_A) % 35) == 0):
            no_of_quarters += 30


        next_machine = 'B'

    elif (next_machine == 'B'):
        num_played_B += 1
        if ((num_played_B + initial_B) % 100 == 0):
            no_of_quarters += 60


        next_machine = 'C'

    elif (next_machine == 'C'):
        num_played_C += 1
        if ((num_played_C + initial_C) % 10 == 0):
            no_of_quarters += 9


        next_machine = 'A'


total_plays = num_played_A + num_played_B + num_played_C
print('Martha plays',total_plays,'times before going broke.')