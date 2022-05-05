#problem : https://dmoj.ca/problem/ccc00s2
no_of_rivers = int(input())
flow = []
for i in range(no_of_rivers):
    flow.append(int(input()))

flow.insert(0, 0)
#print(flow)

#logic
command = int(input())
while command != 77:
    #if split...
    if command == 99:
        index = int(input())
        #print(index)
        left_stream_proportion = int(input()) / 100

        init_flow = flow.pop(index)
        left_stream_flow = left_stream_proportion * init_flow
        right_stream_flow = init_flow - left_stream_flow

        flow.insert(index, right_stream_flow)
        flow.insert(index, left_stream_flow)


    elif command == 88:
        index = int(input())

        right_stream_flow = flow.pop(index + 1)
        left_stream_flow = flow.pop(index)
        net_flow = right_stream_flow + left_stream_flow
        flow.insert(index, net_flow)

    else:
        pass

    #print(flow)
    command = int(input())


#print(flow)
output_buff = ''
for i in range(1, len(flow)):
    output_buff += f'{round(flow[i])} '
    #print(round(flow[i]), end=' ')

print(output_buff[:-1])



