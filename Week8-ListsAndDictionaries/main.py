lotto_numbers = [5, 4, 3, 2, 1]

# what index do you want to insert at, value
lotto_numbers.insert(2, 11)

print(lotto_numbers)

lotto_numbers.sort() # modifies the list in place

print(lotto_numbers)


your_lotto_numbers = []

while(len(your_lotto_numbers) < 5):
    number = int(input("Enter a number"))
    if len(your_lotto_numbers) == 0:
        your_lotto_numbers.append(number)
    else:
        for index in range(len(your_lotto_numbers)):
            if number < your_lotto_numbers[index]:
                your_lotto_numbers.insert(index, number)
                break
        else: # only runs if you don't break
            your_lotto_numbers.append(number)


lotto_numbers.remove(1)

if 1 in lotto_numbers: # avoid a value error
    index_of_1 = lotto_numbers.index(1)

    lotto_numbers.pop(index_of_1)

print(lotto_numbers)

# gets both index and value at the same time
for index, value in enumerate(lotto_numbers):
    print(value, "is at index", index)

for index in range(len(lotto_numbers)):
    print(lotto_numbers[index], "is at index", index)




    # 2 dimensional list
tic_tac_toe_board = [
    ['O', 'X', 'X'],
    ['X', 'O', 'O'],
    ['X', 'O', 'X']
]

for index in range(len(tic_tac_toe_board)):
    print("|".join(tic_tac_toe_board[index]))
    if index < 2:
        print("-----")

print()
print()

for index, row in enumerate(tic_tac_toe_board):
    print("|".join(row))
    if index < 2:
        print("-----")


def add_value_to_list(some_list):
    some_list.append(42)

some_numbers = [10, 20]

# if you want to give a copy of your list to a function, slice it
add_value_to_list(some_numbers[:])

print(some_numbers)


new_numbers = []
for number in some_numbers:
    new_numbers.append(number+5)

# list comprehension
more_new_number = [ number + 5 for number in some_numbers ]

print(new_numbers)
print(more_new_number)

scores = [70, 80, 90, 100]
average_score = sum(scores) / len(scores)

new_scores = []
for score in scores:
    if score < average_score:
        new_scores.append( score + 5 )

more_new_scores = [ score + 5 for score in scores if score < average_score ]

print(new_scores)
print(more_new_scores)

some_list = range(10)
even_numbers = [ number for number in some_list if number % 2 == 0]
odd_numbers = [ number for number in some_list if number % 2] # 0 is false

# sorted gives a copy
new_list = sorted(some_numbers)