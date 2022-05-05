briefcases_opened = int(input())

#get opened briefcase ids in a list
opened_briefcase_list = []
for i in range(briefcases_opened):
    briefcase_id = int(input())
    opened_briefcase_list.append(briefcase_id)
#print(opened_briefcase_list)

#get the banker offer
banker_offer = int(input())

#eliminate the opened briefcase values
values = [100, 500, 1000, 5000,
          10000, 25000, 50000,
          100000, 500000, 1000000]
#print(values)
values_remaining = values.copy()
for i in range(len(opened_briefcase_list)):
    values_remaining.remove(values[opened_briefcase_list[i] - 1])
#print(values_remaining)
average = sum(values_remaining) / len(values_remaining)
#print(average)
if(average < banker_offer ):
    print('deal')
else:
    print('no deal')


