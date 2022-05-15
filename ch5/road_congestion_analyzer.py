# problem : https://dmoj.ca/problem/ecoo18r1p2

for z in range(10):
    no_of_routes = int(input())

    route_id_list = []
    routes_list = []
    min_value_list = []
    for i in range(no_of_routes):
        input_list = list(map(int, input().split()))
        route_id = input_list[0]
        route_id_list.append(route_id)

        routes = input_list[2:].copy()
        routes_list.append(routes)

        # find min value of this route and save it
        min_value_list.append(min(routes_list[i]))

    #print(no_of_routes)
    #print(route_id_list)
    #print(routes_list)
    #print(min_value_list)

    # find overall minimum value and create the
    # list of routes containing that value

    min_value = min(min_value_list)
    selected_route_id_list = []
    for i in range(no_of_routes):
        if min_value_list[i] == min_value:
            selected_route_id_list.append(route_id_list[i])

    # sort
    selected_route_id_list.sort()

    # convert to string so that 'join()' can work
    selected_route_id_list = list(map(str, selected_route_id_list))
    output_id = ','.join(selected_route_id_list)
    # print the output
    print(f'{min_value} {{{output_id}}}')

    #print (selected_route_id_list)
    # print the output : "min_value {selected_route_id}
'''    output_string = f'{min_value} {{'
    for i in selected_route_id_list:
        output_string += f'{i},'
    output_string = output_string[:-1]
    output_string += '}'
'''



