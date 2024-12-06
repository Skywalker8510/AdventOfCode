number_list = open("input.txt", "r")

list1 = []
list2 = []
final_answer = 0

for lines in number_list:
    i = lines.strip().split()
    list1.append(int(i[0]))
    list2.append(int(i[1]))

list1.sort()
list2.sort()

if len(list1) == len(list2):
    for i in range(len(list1)):
        final_answer += abs(list1[i] - list2[i])
else:
    print("number of elements in list1 and list2 are not equal unable to do calculations")

print(final_answer)