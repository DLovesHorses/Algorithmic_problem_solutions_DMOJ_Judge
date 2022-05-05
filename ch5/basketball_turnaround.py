#problem : https://dmoj.ca/problem/coci18c2p1

total_score = []
time_stamp = []
combined_stamp = []

for i in range(2):
    total_score.append(int(input()))
    individual_score = []
    for j in range(total_score[i]):
        individual_score.append(int(input()))
    time_stamp.append(individual_score)
    combined_stamp += individual_score
    #print(individual_score)

#print(total_score)
#print(time_stamp[0])
#print(time_stamp[1])

#sort combined stamp
combined_stamp.sort()
#print(combined_stamp)

#scores before half-time
half_time_score = 0
for i in range(len(combined_stamp)):
    if combined_stamp[i] <= 1440:
        half_time_score += 1

#score trackers
score_a = 0
score_b = 0

score_a_list = []
score_b_list = []

for i in range(len(combined_stamp)):
    if(combined_stamp[i] in time_stamp[0]):
        score_a += 1
    else:
        score_b += 1

    score_a_list.append(score_a)
    score_b_list.append(score_b)

#print(score_a_list)
#print(score_b_list)
score_list = []
score_list.append(score_a_list)
score_list.append(score_b_list)
#print(score_list[0])
#print(score_list[1])

#count trunaround
cur_leading = 'A'
leading_list = []
if score_list[0][0] < score_list[1][0]:
    cur_leading = 'B'

turnaround = 0

for i in range(1, len(combined_stamp)):
    if cur_leading == 'A' and score_list[1][i] > score_list[0][i]:
        cur_leading = 'B'
        turnaround += 1
        leading_list.append(cur_leading)

    elif cur_leading == 'B' and score_list[0][i] > score_list[1][i]:
        cur_leading = 'A'
        turnaround += 1
        leading_list.append(cur_leading)

#print(leading_list)
print(half_time_score)
print(turnaround)
