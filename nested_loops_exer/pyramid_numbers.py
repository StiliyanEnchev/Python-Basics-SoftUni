number = int(input())
counter = 1
no_more_numbers = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end = " ")
        counter += 1
        if counter > number:
            no_more_numbers = True
            break
    if no_more_numbers:
        break
    print()