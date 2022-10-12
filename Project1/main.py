number_of_turns_spent = 0

command = ""

print("Welcome to our terrible game, it's not zork, but it's fun!")

while command != "exit":

    command = input("What do you want to do?")
    number_of_turns_spent += 1

    if command == "go north":
        print("you go north!")
    elif command == "go east":
        print("you go east")
    elif command == "go south":
        print("you go south")
    elif command == "go west":
        print("you go west")
    elif command == "jump":
        print("You jump")
    elif command == "run":
        print("you run")
    elif command == "climb a tree":
        print("You climb a tree and get splinters - you are wounded!!")
        while command != "sleep":
            command = input("What do you want to do")
            if command != "sleep":
                print("You are too wounded to do that, please sleep first")

        print("You sleep and your splinters feel all better now")
        number_of_turns_spent += 1

    elif command == "kick a tree":
        print("You kick the tree, poor tree")
    else:
        print("You can: go north, go east, go south, go west, jump, run, climb a tree, or kick a tree")
        number_of_turns_spent -= 1

print(f"You made it out of the terrible game in {number_of_turns_spent} turns!")