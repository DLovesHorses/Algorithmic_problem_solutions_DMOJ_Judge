# for each dataset
for dataset in range(10):
    # get number of days of sale and number of franchises
    details = input().split()
    franchises = int(details[0])
    days = int(details[1])

    #create master_data table
    master_data = []
    for i in range(days):
        sales_entry = input().split()
        #make it integer
        for j in range(franchises):
            sales_entry[j] = int(sales_entry[j])

        #append to master table
        master_data.append(sales_entry)


    #calculate bonus across sales for each days
    bonus_across_days = 0
    for i in range(days):
        total_sales = 0
        #calculate total sales
        for j in range(franchises):
            total_sales += master_data[i][j]

        #bonus logic
        if total_sales % 13 == 0:
            bonus_across_days += total_sales // 13

    #calculate bonus across franchises
    bonus_across_franchises = 0
    for i in range(franchises):
        total_sales = 0
        # calculate total sales
        for j in range(days):
            total_sales += master_data[j][i]

        # bonus logic
        if total_sales % 13 == 0:
            bonus_across_franchises += total_sales // 13

    #total bonus
    bonus = bonus_across_days + bonus_across_franchises

    print(bonus)
