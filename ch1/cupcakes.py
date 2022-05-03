#get regular boxes
number_of_reg_box = int(input())

#get small boxes
number_of_small_box = int(input())

#calculate total cupcakes
total_cupcakes = (number_of_reg_box * 8) + ( number_of_small_box * 3 )

#calculate remaining cupcakes
total_cupcakes_remaining = total_cupcakes - 28

#print
print(total_cupcakes_remaining)