#get the number of o's
num_of_o = int(input())

#create the string of o's
spooky_o = ''
for x in range(0, num_of_o, 1):
    spooky_o = spooky_o + 'o'

#print the spooky word
print('Sp' + spooky_o + 'ky')