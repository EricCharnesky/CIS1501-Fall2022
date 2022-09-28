import random

number = int(input("enter a number to count down from"))

while number < 1:
    print("Invalid entry, try again")
    number = int(input("enter a number to count down from"))

# pre-test loop
# if the condition is true, it runs
while number != 0:
    print(number)
    number -= 1
    # when the loop body is done, go back to the top and check again

print('blast off!')


play_again = 'y'

while play_again != 'n':
    largest_value = int(input("How high of a number do you want to guess to?"))

    while largest_value < 10 or largest_value > 1_000_000:
        largest_value = int(input("How high of a number do you want to guess to?"))

    magic_number = random.randint(1, largest_value)

    guess = int(input(f"Guess a number 1-{largest_value}"))
    guess_count = 1

    while guess != magic_number:
        if guess < magic_number:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input(f"Guess a number 1-{largest_value}"))
        guess_count += 1

    print(f"You guessed it in {guess_count}")

    play_again = input("Do you want to play again? y/n").lower()

    # validation loop - if not valid, run again
    while play_again != 'y' and play_again != 'n':
        play_again = input("Do you want to play again? y/n").lower()

    valid_options = ['y', 'n']
    while play_again not in valid_options:
        play_again = input("Do you want to play again? y/n").lower()


total_receipts = 0

all_done = 'n'

while all_done != 'y':
    receipt = float(input("Enter a receipt value"))
    total_receipts += receipt
    all_done = input("Are you all done entering receipts? y/n")

# sentinel value - invalid value with special meaning
while receipt != 0:
    receipt = float(input("Enter a receipt value or 0 to stop"))
    total_receipts += receipt

some_collection = [42, 7, 23, 107]

# run once per value in the some_collection
# essentially is a copy of the value
for item in some_collection:
    item += 42
    # in the loop body, the current value is the variable item
    print(item)

print(some_collection)

            # range gives a collection from 0 up to but not including the number
for index in range(len(some_collection)):
    # you can change values in a list by index
    some_collection[index] += 42
    print(some_collection[index])

print(some_collection)

some_word = input("Enter a word to get the magic value of")

sum = 0
for letter in some_word:
    sum += ord(letter)

print(f'The magic value of {some_word} is {sum}')


classes = { "CIS 1501" : "CS1 for Data Scientists",
            "MAT 115" : "Calculus 1",
            "STAT 325" : "Intro to Statistics" }

# when using a for loop on dictionaries, you get keys
for item in classes:
    print(f'key: {item} - associated value: {classes[item]}')

count = 5
while count != 0:

    count -= 1

# for loops can pretty much never be infinite
for count in range(5):
    print("Please do abc")

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(f'{hour:02d}:{minute:02d}:{second:02d}')

length = int(input("How long of a rectangle do you want?"))
height = int(input("How tall of a rectangle do you want?"))

for row in range(height):
    for character in range(length):
        print('*', end="") # doesn't go down a line
    print() # gives a new line


print("or the easy way")
for row in range(height):
    print("*" * length)

# start is optional, the end is required, the count by is optional
for skip_count in range(1, 11, 2):
    print(skip_count)

# if you want to use count by, you have to include start, end, count by
for backwards_count in range(10, 0, -1):
    print(backwards_count)

    # this doesn't work, it thinks the start is 10, and the end is 2
for value in range(10, 2):
    print(value)
else:
    print("that's all folks")

while True:
    number = int(input("Enter a number"))
    if number == 42:
        break # means end the loop, hard stop
else: # only runs if the loop ends normally - doesn't break
    print("This loop else is running")

number = 1
count_of_odd_numbers = 0
# python is truth-y - every value is true or false
# 0 is false, anything other than 0 is true
while number % 2: # odd
    number = int(input("Enter an odd value"))
    if number % 2 == 0:
        continue # causes the loop body to stop, and jump up to the loop expression
    count_of_odd_numbers += 1
print(f'You entered {count_of_odd_numbers} odd numbers')


names = ['Eric', 'Jasmine', 'Joy', 'Jeb', 'Vivi' ]

for index in range(len(names)):
    print(f'index: {index} value: {names[index]}')

    # value is a copy from the list
for index, value in enumerate(names):
    value = value.upper()
    print(f'index: {index} value: {value}')

print(names)