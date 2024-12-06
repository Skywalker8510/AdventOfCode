number_list = open("input.txt", "r")

list1 = []
list2 = []
final_answer = 0

for lines in number_list:
    i = lines.strip().split()
    list1.append(int(i[0]))
    list2.append(int(i[1]))

for i in list1:
    number_of_i = 0
    for j in list2:
        if i == j:
            number_of_i += 1
    final_answer += i * number_of_i

print(final_answer)