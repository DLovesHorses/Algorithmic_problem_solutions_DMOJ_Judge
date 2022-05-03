#get width of pizza W
width = int(input())

#get extra cheesiness
cheeseiness = int(input())

#placeholder string
middlestring = ''

if(width == 3 and cheeseiness >= 95):
    middlestring = 'absolutely'
elif(width == 1 and cheeseiness <=50):
    middlestring = 'fairly'
else:
    middlestring = 'very'


print('C.C. is ' + middlestring +' satisfied with her pizza.')
