import sys

number_of_villages = int(sys.stdin.readline())
list_of_villages = []

#crate a list
for i in range(number_of_villages):
    village = int(sys.stdin.readline())
    list_of_villages.append(village)

#print(list_of_villages)

#sort the list
list_of_villages.sort()
#print(list_of_villages)

#count = 1
min = 2000000000
for i in range(1, number_of_villages - 1, 1):

    current_village = list_of_villages[i]
    left_village = list_of_villages[i-1]
    right_village = list_of_villages[i+1]

    left_neighbourhood = (current_village - left_village) / 2
    right_neighbourhood = (right_village - current_village) / 2

    neighbourhood_size = left_neighbourhood + right_neighbourhood

    '''if count == 1:
        min = neighbourhood_size
        count += 1'''
    if neighbourhood_size < min:
        min = neighbourhood_size

print(min)