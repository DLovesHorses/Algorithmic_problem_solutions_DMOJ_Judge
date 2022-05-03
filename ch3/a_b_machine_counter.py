'''
#more effecient code

#get input
presses = int(input())

#initial condition
no_of_a = 1
no_of_b = 0

for i in range(presses):
    temp = no_of_a
    no_of_a = no_of_b
    no_of_b += temp

print(no_of_a, no_of_b)

'''

#second version - less effecient code
presses = int(input())

string = 'A'
temp_string = ''

for i in range(presses):
    for j in string:
        if (j == 'A'):
            temp_string += 'B'
        elif(j == 'B'):
            temp_string += 'BA'

    string = temp_string
    temp_string = ''

#print(string)
print(string.count('A'), string.count('B'))