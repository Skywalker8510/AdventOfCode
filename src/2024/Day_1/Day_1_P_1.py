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
    array_length = len(list1)
    for i in range(array_length):
        calculation_array = [list1[i], list2[i]]
        calculation_array.sort()
        final_answer += calculation_array[1] - calculation_array[0]
else:
    print("number of elements in list1 and list2 are not equal unable to do calculations")

print(final_answer)