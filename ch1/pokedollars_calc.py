#get number of liters of paint available
total_paint = int(input())

#get number of litres required for each badge
badge_paint = int(input())

#get the price of one badge
badge_price = int(input())

#calculate the number of badge that can be made
total_badge_produced = total_paint // badge_paint

#calculate the leftover paint
leftover_paint = total_paint % badge_paint

#calculate the income by selling only badges
badge_selling_income = total_badge_produced * badge_price

#calculate the income by selling leftover paint
leftover_paint_income = leftover_paint * 1

#calculate total incole
total_income = badge_selling_income + leftover_paint_income

#print the incole
print(total_income)