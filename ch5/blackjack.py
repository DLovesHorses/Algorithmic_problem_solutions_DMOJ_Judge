# problem:

# value       2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Index       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
card_count = [0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

no_of_draws = int(input())
total = 0

for i in range(no_of_draws):
    draw_value = int(input())
    total += draw_value
    card_count[draw_value - 1] -= 1

# difference
difference = 21 - total

cards_lower_than_diff = sum(card_count[:difference])
cards_higher_than_diff = sum(card_count[difference:])
# cards_lower_than_diff = 52 - no_of_draws - cards_higher_than_diff

# print(f'cards lower than {difference} = {cards_lower_than_diff}')
# print(f'cards higher than {difference} = {cards_higher_than_diff}')

if cards_higher_than_diff >= cards_lower_than_diff:
    print('DOSTA')
else:
    print('VUCI')
