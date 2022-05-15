# problem : https://dmoj.ca/problem/dmopc19c5p2

data = list(map(int, input().split()))
no_of_moves = data[0]
initial_health = data [1]

charlie_action_list = []
charlie_damage_list = []
opponent_action_list = []
opponent_damage_list = []

for i in range(no_of_moves):
    charlie_data = input().split()

    charlie_action_list.append(charlie_data[0])
    charlie_damage_list.append(int(charlie_data[1]))

for i in range(no_of_moves):
    opponent_data = input().split()

    opponent_action_list.append(opponent_data[0])
    opponent_damage_list.append(int(opponent_data[1]))


# print(charlie_action_list)
# print(charlie_damage_list)
# print("")
# print(opponent_action_list)
# print(opponent_damage_list)

c_health = initial_health
o_health = initial_health
c_hit_taken = False
o_hit_taken = False
next_move = 'C' #C -> Charlie, O -> opponent
i = 0
while c_health > 0 and o_health > 0 and i < no_of_moves:
    if next_move == 'C':
        if charlie_action_list[i] == 'A' and not c_hit_taken:
            o_health -= charlie_damage_list[i]
        elif charlie_action_list[i] == 'D' and opponent_action_list[i] == 'A':
            o_health -= charlie_damage_list[i]
            o_hit_taken = True
        elif charlie_action_list[i] == 'D' and opponent_action_list[i] == 'D':
            c_health -= charlie_damage_list[i]
        elif c_hit_taken:
            c_hit_taken = False


        next_move = 'O'

    elif next_move == 'O':
        if opponent_action_list[i] == 'A' and not o_hit_taken:
            c_health -= opponent_damage_list[i]
        elif opponent_action_list[i] == 'D' and i != no_of_moves - 1 and charlie_action_list[i+1] == 'A':
            c_health -= opponent_damage_list[i]
            c_hit_taken = True
        elif i == no_of_moves - 1:
            if opponent_action_list[i] == 'A':
                #c_health -= opponent_damage_list[i]
                pass
            elif opponent_action_list[i] == 'D':
                o_health -= opponent_damage_list[i]
        elif opponent_action_list[i] == 'D' and i != no_of_moves - 1 and charlie_action_list[i+1] == 'D':
            o_health -= opponent_damage_list[i]

        elif o_hit_taken:
            o_hit_taken = False



        next_move = 'C'
        i += 1

    #print(f'Charlie: {c_health}, Opponent: {o_health}')

if c_health <= 0:
    print("DEFEAT")
elif o_health <= 0:
    print("VICTORY")
else:
    print("TIE")
