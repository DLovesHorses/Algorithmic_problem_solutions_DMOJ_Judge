#get input
choice_burger = int(input())
choice_side = int(input())
choice_drink = int(input())
choice_dessert = int(input())
calories_count = 0

#burger calories
if(choice_burger == 1):
    calories_count += 461
elif(choice_burger == 2):
    calories_count += 431
elif(choice_burger == 3):
    calories_count += 420
else:
    pass

#sides calories
if(choice_side == 1):
    calories_count += 100
elif(choice_side == 2):
    calories_count += 57
elif(choice_side == 3):
    calories_count += 70
else:
    pass

#drink calories
if(choice_drink == 1):
    calories_count += 130
elif(choice_drink == 2):
    calories_count += 160
elif(choice_drink == 3):
    calories_count += 118
else:
    pass

#dessert calories
if(choice_dessert == 1):
    calories_count += 167
elif(choice_dessert == 2):
    calories_count += 266
elif(choice_dessert == 3):
    calories_count += 75
else:
    pass

print('Your total Calorie count is '+ str(calories_count) + '.')