#get the 4 digit input
number = int(input())

#get first digit
n1 = number // 1000

#get second digit
n2 = (number // 100) % 10

#get third digit
n3 = (number // 10) % 10

#get fourth digit
n4 = (number % 10)

print(n1)
print(n2)
print(n3)
print(n4)