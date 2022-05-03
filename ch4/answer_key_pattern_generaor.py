questions = int(input())
answer_key = input()

adrian_key = ''
bruno_key = ''
goran_key = ''

adrian_key_length = 0
bruno_key_length = 0
goran_key_length = 0

#create adrian key
while adrian_key_length < len(answer_key):
    inter = adrian_key_length % 3
    if inter == 0:
        adrian_key += 'A'
    elif inter == 1:
        adrian_key += 'B'
    elif inter == 2:
        adrian_key += 'C'

    adrian_key_length += 1


#create bruno key
toggle = 0
while bruno_key_length < len(answer_key):
    inter = bruno_key_length % 2
    if inter == 0:
        bruno_key += 'B'
    else:
        if toggle == 0:
            bruno_key += 'A'
        else:
            bruno_key += 'C'

        toggle ^= 1

    bruno_key_length += 1


#create goran key
while goran_key_length < len(answer_key):
    inter = goran_key_length % 6

    if inter == 0 or inter == 1:
        goran_key += 'C'
    elif inter == 2 or inter == 3:
        goran_key += 'A'
    elif inter == 4 or inter == 5:
        goran_key += 'B'

    goran_key_length += 1

#print(adrian_key)
#print(bruno_key)
#print(goran_key)

adrian_score = 0
bruno_score = 0
goran_score = 0

for i in range(len(answer_key)):
    if(answer_key[i] == adrian_key[i]):
        adrian_score += 1

    if (answer_key[i] == bruno_key[i]):
        bruno_score += 1

    if (answer_key[i] == goran_key[i]):
        goran_score += 1


max_score = max(adrian_score, bruno_score, goran_score)
print(max_score)

if(adrian_score == max_score):
    print('Adrian')
if(bruno_score == max_score):
    print('Bruno')
if(goran_score == max_score):
    print('Goran')