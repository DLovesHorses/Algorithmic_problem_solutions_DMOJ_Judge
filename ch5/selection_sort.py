ip_list = list(map(int, input().split()))
print(ip_list)

i = 0
while i < len(ip_list):
    #min = ip_list[i]
    min_index = i
    for j in range(i+1, len(ip_list)):
        if ip_list[j] < ip_list[min_index]:
            min_index = j

    min = ip_list[min_index]
    ip_list[min_index] = ip_list[i]
    ip_list[i] = min
    i += 1
    print(ip_list)