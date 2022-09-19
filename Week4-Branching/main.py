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


