#get input
swap_string = input()

#initial ball location
ball_location = 1



#logic
for swap_type in range(len(swap_string)):
    if(swap_string[swap_type] == 'A' and ball_location == 1):
        ball_location = 2
    elif(swap_string[swap_type] == 'A' and ball_location == 2):
        ball_location = 1
    elif (swap_string[swap_type] == 'B' and ball_location == 2):
        ball_location = 3
    elif (swap_string[swap_type] == 'B' and ball_location == 3):
        ball_location = 2
    elif (swap_string[swap_type] == 'C' and ball_location == 3):
        ball_location = 1
    elif (swap_string[swap_type] == 'C' and ball_location == 1):
        ball_location = 3

print(ball_location)