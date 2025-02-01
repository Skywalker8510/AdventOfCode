
number_list = open("input.txt", "r")
array = []

for lines in number_list:
    i = lines.strip().split()
    array.append(i)

safe_counter = 0

for i in range(len(array)):
    Safe = True
    first_run = True
    for j in range(len(array[i])-1):

        next_j = j+1

        current_number = int(array[i][next_j])
        last_number = int(array[i][j])

        if current_number >= last_number >= (current_number - 3):
            #print(array[i][j] + " " + str(array[i][next_j]))
            direction = True
        elif current_number <= last_number <= (current_number + 3):
            #print(array[i][j] + " " + str(array[i][next_j]))
            direction = False
        else:
            #print(array[i][j] + " " + str(array[i][next_j]))
            Safe = False
            break

        #print(str(last_j) + " " + str(array[i][next_j]))

        if first_run:
            first_run = False
        else:
            if  direction != last_direction:
                Safe = False
                break
        last_direction = direction

    print(str(Safe))
    if Safe:
        safe_counter += 1

print(safe_counter)
