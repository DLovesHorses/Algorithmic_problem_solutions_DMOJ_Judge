# problem : https://dmoj.ca/problem/dmopc20c2p1
# similar to problem : https://dmoj.ca/problem/coci20c2p1 (icon_coder)

days = int(input())
daily_status = input()

net_worth_list = []
total = 0
net_worth_list.append(total) # for first element
for i in range(days):

    if daily_status[i] == '^':
        total += 1
    elif daily_status[i] == 'v':
        total -= 1
    else:
        pass
    net_worth_list.append(total)

#net_worth_list.sort()
#print(net_worth_list)

#create a row list
net_worth_row = []
while len(net_worth_list) != 0:
    curNetWorth = net_worth_list[0]
    net_worth_row.append(curNetWorth)

    while curNetWorth in net_worth_list:
        net_worth_list.remove(curNetWorth)

#print(net_worth_row)
net_worth_row.sort(reverse=True)
#print(net_worth_row)

#create day list
day_list = []
for i in range(days):
    day_list.append(i+1)
#print(day_list)



charMatrix = []

for row in net_worth_row:
    row_matrix = []
    for col in range(days):
        row_matrix.append('.')
    charMatrix.append(row_matrix)

#for i in range(len(charMatrix)):
    #print(charMatrix[i])

#print(' ')
#print(' ')

# charMatrix[net_worth_row.index(2)][day_list.index(2)] = '/' # just testing
#for i in range(len(charMatrix)):
    #print(charMatrix[i])


#drawing logic
calcNetWorth = 0
used_net_worth = []

for j in day_list:
    curChar = daily_status[day_list.index(j)]

    if curChar == '^':
        used_net_worth.append(calcNetWorth)
        charMatrix[net_worth_row.index(calcNetWorth)][day_list.index(j)] = '/'
        calcNetWorth += 1
    elif curChar == 'v':
        calcNetWorth -= 1
        charMatrix[net_worth_row.index(calcNetWorth)][day_list.index(j)] = '\\'
        used_net_worth.append(calcNetWorth)

    else:
        charMatrix[net_worth_row.index(calcNetWorth)][day_list.index(j)] = '_'
        used_net_worth.append(calcNetWorth)

#print(' ')
#print(' ')

#for i in range(len(charMatrix)):
     #print(charMatrix[i])

str = ''
for i in range(len(charMatrix[0])):
    str += charMatrix[1][i]

#print(str)
#print(used_net_worth)
#used_net_worth.sort()

used_net_worth_to_draw = []
while len(used_net_worth) != 0:
    curNet = used_net_worth[0]
    used_net_worth_to_draw.append(curNet)
    while curNet in used_net_worth:
        used_net_worth.remove(curNet)


used_net_worth_to_draw.sort(reverse=True)
#print(used_net_worth_to_draw)

op_str = ''
for i in used_net_worth_to_draw:

    for col in range(len(charMatrix[net_worth_row.index(i)])):
        op_str += charMatrix[net_worth_row.index(i)][col]

    op_str += '\n'

print(op_str)