#get inputs
a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

#calculate total
a_total = (a3 * 3) + (a2 * 2) + a1
b_total = (b3 * 3) + (b2 * 2) + b1

#logic

if(a_total > b_total):
    print('A')
elif(a_total < b_total):
    print('B')
else:
    print('T')


    #end of prog