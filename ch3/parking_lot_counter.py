#get inputs
n = int(input())
yesterday = input()
today = input()

#initialize the count variable
occupied = 0

#logic
for index in range(len(yesterday)):
    if((yesterday[index] == today[index]) and (yesterday[index] == 'C')):
        occupied += 1


print(occupied)