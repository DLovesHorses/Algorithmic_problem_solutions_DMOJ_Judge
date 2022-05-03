#get lines to be read
lines = int(input())

student_response = ''
answer_key = ''
marks = 0

for i in range(0, lines, 1):
    student_response += input()

for i in range(lines, 2 * lines, 1):
    answer_key += input()

for i in range(0, lines, 1):
    if(student_response[i] == answer_key[i]):
        marks += 1


print(marks)