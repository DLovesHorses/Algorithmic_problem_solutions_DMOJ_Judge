#get number of lines to be read
lines = int(input())

count_s = 0
count_t = 0

#logic
for line in range(lines):
    cur_line = input()
    count_s += cur_line.count('s') + cur_line.count('S')
    count_t += cur_line.count('t') + cur_line.count('T')


if(count_t > count_s):
    print("English")
else:
    print("French")
