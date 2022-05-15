# problem :

for z in range(10):

    # get input
    input_list = input().split()
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])

    # print(input_list)

    day_per_box = input_list[0]
    total_days = input_list[1]

    # create a list of all the days with B and E (Box and Empty) data.
    day_data = []
    for i in range(total_days):
        day_data.append(input())

    # print(day_data)

    # itrate over day_data and create a list containing all the possible
    # days that willow can spend.
    counter = []
    for i in day_data:
        if i == 'B':
            counter.append(day_per_box)

    # print(counter)

    # main logic
    prev = 0
    cur = 0
    play_day = []
    for i in day_data:
        if i == 'E' and prev == 0:
            cur = 0

        if i == 'B' and prev == 0:
            cur = day_per_box - 1

        if i == 'E' and prev != 0:
            cur = prev - 1

        if i == 'B' and prev != 0:
            cur = prev + day_per_box - 1

        prev = cur
        play_day.append(prev)

    #print(play_day)
    print(play_day[-1])

