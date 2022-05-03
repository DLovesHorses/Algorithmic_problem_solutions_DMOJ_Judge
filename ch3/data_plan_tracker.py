#get mb available each monts
mb_available = int(input())

#get number of months since active
active_months = int(input())

#total used data
total_used_data = 0

#logic
for i in range(active_months):
    data_used = int(input())
    total_used_data += data_used

data_available = mb_available * (active_months + 1)
print(data_available - total_used_data)