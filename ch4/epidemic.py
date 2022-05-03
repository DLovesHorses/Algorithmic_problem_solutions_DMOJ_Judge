max_limit = int(input())

day = 0
infected = int(input())
contegeous_level = int(input())
count = 0

while count <= max_limit:
    count += infected
    infected *= contegeous_level
    day += 1
    #print(count)






#print(infected)
print(day-1)