#get the number of eaters
eaters = int(input())

#candies per eater
candy_per_eater = int(input())

#get total number of candies
total_candies = int(input())

#calculate remaining candies
remaining_candies = total_candies - (eaters * candy_per_eater)

#print
print(remaining_candies)