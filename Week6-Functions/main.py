import random


def positivity(greeting, affirmation):
    greeting()
    print(affirmation)


def print_happy_monday():
    print("Happy Monday!")
    print("Are you excited for the week?")
    print("I hope you have something fun planned!")


# parameters are optional when making functions
def print_happy_day(day):
    print("Happy", day)


# def print_larger_number(first_number, second_number):
#     if first_number > second_number:
#         print(first_number)
#     else:
#         print(second_number)


def print_larger_number(first_number, second_number, third_number):
    print(max(first_number, second_number, third_number))


def get_random_number_1_6():
    return random.randint(1, 6)


def get_daily_affirmation():
    # https://www.berkeleywellbeing.com/daily-affirmations.html
    affirmation_list = (
        'I am inspired by things happening all around me.'
        , 'I am grateful for the people I have in my life.'
        , 'I grow and improve every day.'
        , 'I treat myself kindly and with compassion.'
        , 'I am able to find the silver linings in difficult situations.'
        , 'I always try to see the bright side of things.'
        , 'I am grateful for the things I have in life.'
    )

    random_index = random.randint(0, len(affirmation_list)-1)
    return affirmation_list[random_index]

    # https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
    return random.choice(affirmation_list)


# these are bad and will crash
def first_function():
    print("first")
    second_function()


def second_function():
    print("second")
    first_function()

# first_function()


some_number = int(input("Enter a number"))

random_number = get_random_number_1_6()


# print_larger_number(some_number, random_number)
print_larger_number(some_number, random_number, 7)

print_happy_monday

print("That's all folks!")

print_happy_day("Monday")
print_happy_day("Tuesday")
print_happy_day(10)


monday_affirmation = get_daily_affirmation()
str(monday_affirmation).title()

print(monday_affirmation)

# passes the definition of the function, doesn't run it yet,
positivity(print_happy_monday, monday_affirmation)
