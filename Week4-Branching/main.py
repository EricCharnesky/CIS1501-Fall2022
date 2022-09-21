temp = int(input("What's the temperature outside?"))
raining = input("Is it raining? (yes/no)")

# boolean expression is either true or false

if raining == "yes":
    print("Bring an umbrella")
    if temp < 60:
        print("Bring a jacket")
        print("don't wear crocks")
else:
    if temp < 50:
        print("Bring a jacket")
        print("don't wear crocks")


score = int(input("Please enter your score 0-100"))

if score >= 70:
    print("pass")
else:
    print("fail")


# conditional expression - this is confusing for a while
score_as_text = "pass" if score > 70 else "fail"

# same as above
if score > 70:
    score_as_text = 'pass'
else:
    score_as_text = 'fail'

# still mutually exclusive, one and only one will run
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("fail")

average = int(input("Enter the average score"))

if score > (average+10):
    print("A")
elif (average - 10) <= score <= (average+10):
    print("B")
else:
    print("C")

tired = input("Are you tired? (yes/no)")
how_much_coffee_have_you_had_already = \
    int(input("How many cups of coffee have you had already?"))

# logical operator combines boolean expressions
if tired == 'yes' and how_much_coffee_have_you_had_already < 4:
    print("Drink another cup of coffee")
else:
    print("Drink some water!")

# same as above - without the logical operator
if tired == 'yes':
    if how_much_coffee_have_you_had_already < 4:
        print("Drink another cup of coffee")
    else:
        print("Drink some water!")
else:
    print("Drink some water!")


# AND - both sides need to be true
# true and true == true
# true and false == false
# false and true == false
# false and false == false

# OR - either side is true
# true or true == true
# true or false == true
# false or true == true
# false or false == false

# not - opposite
# not true == false
# not false == true


classes = {'CIS 1501': [], 'CIS 200': []}

class_you_are_taking = input("What class are you taking?")
name = input("Enter your name")

# membership operator 'in' - is the value in the collection
# with dictionaries, it only checks the KEYS - not the associated values
if class_you_are_taking in classes:
    print("You are in Eric's class")
    classes[class_you_are_taking].append(name)
else:
    print("That's so sad you aren't in Eric's class")
    print("Good news, Eric will teach that class!")
    # if the key doesn't exist, it adds the item with associated value
    classes[class_you_are_taking] = [name]

print(classes)

secret_word = 'ghost'
secret_word_uppercase = "GHOST"

if 'ost' in secret_word:
    print("contains ost")

if '' in secret_word:
    print("You have an empty string?")

# if you are getting user input and need to check against other strings, use .lower()
first_letter = input('Please enter a letter to guess').lower()


if first_letter.lower() in secret_word or first_letter.upper() in secret_word_uppercase:
    print("You checked the hard way for case")

if len(first_letter) > 1:
    print("You can't read directions can you?")
else:
    if first_letter in secret_word:
        print(first_letter, "is in the secret word!")
    else:
        print(first_letter, "is not in the secret word!")

if len(first_letter) != 1:
    print("You can't read directions can you?")

elif first_letter in secret_word:
    print(first_letter, "is in the secret word!")
else:
    print(first_letter, "is not in the secret word!")


kids = ["Joy", 'Jeb', 'Jenavieve', 'Journey', 'Jubilee', "Jackson", 'Jasper']

name = input("Enter a J name")

if name in kids:
    print("You have the same name as one of Eric's kids!")
else:
    print("That's a unique J name!")

test_value = 10

other_value = 2

print(id(test_value))
print(id(other_value))

other_value += 8

print(id(test_value))
print(id(other_value))

first = [1, 2, 3]
last = [7, 8, 9]

print(id(first))
print(id(last))

last = [1, 2, 3]

print(id(first))
print(id(last))

last = first

print(id(first))
print(id(last))

print("first contents", first)
print('lst contents', last)

first.append(42)

print("first contents", first)
print('lst contents', last)

player = 'rock'
computer = 'spock'

# order of operations is important for logical operators
player == "rock" and (computer == 'paper' or computer == 'spock')



if 'CIS' < 'Eric':
    print("Eric is greater than CIS")

print("Eric's minimum kid", min(kids))

number = 0

if number: # non 0 numbers are true
    print("You have the answer")

word = 'Test'

if word: # non empty string is true
    print("It's not false")

word = '' # empty string is false
if word:
    print("It's not false")

classes = {}
classes['CIS 1501'] = {}
classes['CIS 1501']['Meeting Time'] = "Monday/Wednesday 12:30pm-1:45pm"
classes['CIS 1501']['Description'] = "CS 1 for Data Scientists"

classes_with_list = {}
classes['CIS 1501'] = []
classes['CIS 1501'].append("Monday/Wednesday 12:30pm-1:45pm")
classes['CIS 1501'].append("CS 1 for Data Scientists")