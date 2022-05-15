# problem : https://dmoj.ca/problem/ecoo19r1p1

for z in range(10):
    # get inputs
    first_list = input().split()
    for i in range(len(first_list)):
        first_list[i] = int(first_list[i])

    #print(first_list)
    initial_shirts = first_list[0]
    upcoming_events = first_list[1]
    days = first_list[2]

    event_list = input().split()
    for i in range(len(event_list)):
        event_list[i] = int(event_list[i])

    event_list.sort()
    #print(event_list)

    # trackers
    total_shirts = initial_shirts
    clean_shirts = total_shirts
    laundary_day = 0
    prev = clean_shirts

    total_list = []
    clean_list = []
    laundary_list = []
    day_list = []

    for i in range(1, days + 1):
        # print(i)
        #before

        if clean_shirts == 0:
            laundary_list.append(i)
            clean_shirts = total_shirts
        clean_shirts -= 1

        j = 0
        total_list.append(total_shirts)
        while len(event_list) != 0 and event_list[j] <= i:
            #print(j, event_list[j])
            total_shirts += 1
            clean_shirts += 1
            event_list.pop(j)

        day_list.append(i)


    #print(day_list)
    #print(total_list)
    #print(clean_list)
    #print(laundary_list)

    #print(laundary_list[-1] + 1)
    print(len(laundary_list))
