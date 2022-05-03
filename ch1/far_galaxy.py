#get total no. of far
input_no_far = int(input())

#create last far
last_far = 'far '

#create remaining fars
remaining_far_no = input_no_far - 1
remaining_far = 'far, ' * remaining_far_no

#create complete string
string = ' A long time ago in a galaxy ' + remaining_far + last_far + 'away...'

#print

print(string)