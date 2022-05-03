#get input
input_string = input()

#get number of happy face
happy_face_num = input_string.count(':-)')

#get number of sad face
sad_face_num = input_string.count(':-(')

if(happy_face_num == 0 and sad_face_num == 0):
    print('none')
elif(happy_face_num == sad_face_num):
    print('unsure')
elif(happy_face_num > sad_face_num):
    print('happy')
else:
    print('sad')

