# problem : https://dmoj.ca/problem/dmopc14c7p2

no_of_tides = int(input())
tides_list = list(map(int, input().split()))

#print(tides_list)

min_index = tides_list.index(min(tides_list))
max_index = tides_list.index(max(tides_list))

#print(f'min at {min_index}; max at {max_index}')

if min_index < max_index:
    for i in range(min_index, max_index):
        if tides_list[i] < tides_list[i+1]:
            if i == max_index - 1:
                print(f'{tides_list[max_index] - tides_list[min_index]}')

        else:
            print('unknown')
            break

else:
    print('unknown')