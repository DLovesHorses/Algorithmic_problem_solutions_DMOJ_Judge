# problem: https://dmoj.ca/problem/coci19c5p1
input_data = list(map(int, input().split()))
no_of_lines = input_data[0]
no_of_chars = input_data[1]

master_rect_list = []
astrict_list = []

for line in range(no_of_lines):
    line_astrict_list = []
    ip_string = input()
    prev_char = '@'

    for j in range(no_of_chars):
        if ip_string[j] == '*':
            line_astrict_list.append(j)
            prev_char = '*'
        elif ip_string[j] == '.' and prev_char == '*':
            #print(line_astrict_list)
            astrict_list.append(line_astrict_list)
            line_astrict_list = []
            prev_char = '.'

    if len(line_astrict_list) != 0:
        astrict_list.append(line_astrict_list)
    master_rect_list.append(astrict_list)
    astrict_list = []

    #print(astrict_list)

#print(master_rect_list)
rect_count = 0
for i in range(len(master_rect_list)):
    #print(master_rect_list[i])




    while len(master_rect_list[i]) != 0:
        rect_count += 1
        current_coord = master_rect_list[i][0].copy()
        j = i
        while j < len(master_rect_list) and current_coord in master_rect_list[j]:
            #print(master_rect_list[j])
            master_rect_list[j].remove(current_coord)
            j += 1


print(rect_count)

