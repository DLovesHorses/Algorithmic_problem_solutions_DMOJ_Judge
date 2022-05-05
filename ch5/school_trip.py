
brunch_cost = [12, 10, 7, 5]
#for each test case, do following

for i in range(10):
    #get total trip cost
    total_cost = int(input())

    #get list of proportion of students for each year.
    proportions = input().split()

    #get total number of students coming for brunch
    total_students = int(input())

    #modify the proporitons list so that it has float values instead of strings
    for j in range(len(proportions)):
        proportions[j] = float(proportions[j])
    #print(proportions)

    #calculate rounded number of student for each year
    rounded_list = []
    for j in range(len(proportions)):
        rounded_no = (proportions[j] * total_students)
        rounded_list.append(int(rounded_no))
    #print(rounded_list)

    #calculate sum of rounded number of students
    counted_students = sum(rounded_list)
    #print(counted_students)

    #calculate students not accounted for
    uncounted_students = total_students - counted_students
    #print(uncounted_students)

    #add thie uncounted students with the students of year having max count
    rounded_list[rounded_list.index(max(rounded_list))] += uncounted_students
    #print(rounded_list)

    #calculate the sum
    total_received = 0
    for i in range(len(rounded_list)):
        total_received += rounded_list[i] * brunch_cost[i]

    #print(sum/2)
    if (total_received/2) < total_cost:
        print('YES')
    else:
        print('NO')
