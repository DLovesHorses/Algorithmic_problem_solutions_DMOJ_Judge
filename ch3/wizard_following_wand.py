#get initial wizard
won_wizard = input()

#get number of duals
matches = int(input())

#unique wizards
unique_won_wizard = won_wizard

#main logic

for i in range(matches):
    result = input()
    if(result[-1] == won_wizard):
        won_wizard = result[0]
        if won_wizard not in unique_won_wizard:
            unique_won_wizard += won_wizard


#output
print(won_wizard)
print(len(unique_won_wizard))
#print(unique_won_wizard)