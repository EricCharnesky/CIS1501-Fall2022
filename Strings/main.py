import random


def make_secret_message(some_string):
    return some_string[::2] + some_string[1::2]


def undo_secret_message(secret_message):
    first_half = secret_message[:len(secret_message)//2]
    second_half = secret_message[len(secret_message)//2:]

    message = ''

    for index in range(len(first_half)):
        message += first_half[index] + second_half[index]

    return message


def jumble(some_string, chunk_size):
    chunks = []
    start_index = 0
    while start_index < len(some_string):
        chunks.append(some_string[start_index:start_index+chunk_size])
        start_index += chunk_size

    while len(chunks) > 0:
        random_index = random.randint(0, len(chunks)-1)
        print(chunks[random_index], end='')
        chunks.pop(random_index)
    print()

sentence = 'one fish two fish red fish blue fish'

secret_sentence = make_secret_message(sentence)

print(secret_sentence)

undo_message = undo_secret_message(secret_sentence)

print(undo_message)

jumble(sentence, 4)

fish_index = sentence.find('fish')
fish_count = 0

while fish_index >= 0:
    fish_count += 1
    fish_index = sentence.find('fish', fish_index+1)

print(fish_count)

print(sentence.count('fish'))

print()

# start and end are optional, default to 0 and len(string)
first_4_letters = sentence[:4]

print(first_4_letters)

# negatives are characters from the end
last_4_letters = sentence[-4:]


every_other_letter = sentence[::2]
other_every_other_letter = sentence[1::2]

print(every_other_letter)
print(other_every_other_letter)

print(last_4_letters)

name = 'Eric'

for character in name:
    print(character)

for index in range(len(name)):
    print(name[index])

print(name[0:1])
print(name[1:2])
print(name[2:3])
print(name[3:4])

    # start index - end index not included
print(name[0:2])
print(name[2:len(name)])

names = input("Enter a bunch of names, comma separated")

names_list = names.split(',')

print(names_list)

for index in range(len(names_list)):
    names_list[index] = names_list[index].strip()

print(names_list)


names = input("Enter names with space separations")

names_list = names.split()

print(names_list)

names_string = ", ".join(names_list)

print(names_string)


character_to_split_on = input("Enter the character to split on")
sentence = input("Enter a sentence to split")

# splitting the hard way
chunks = []

index_of_character_to_split = sentence.find(character_to_split_on)
last_split_index = 0

while index_of_character_to_split >= 0:
    chunks.append(sentence[last_split_index:index_of_character_to_split])
    last_split_index = index_of_character_to_split + len(character_to_split_on)
    index_of_character_to_split = sentence.find(character_to_split_on, last_split_index)
chunks.append(sentence[last_split_index:])

print(chunks)

character_to_join_with = " "

string_result = ""
for item in chunks:
    string_result += item + character_to_join_with

string_result = string_result[:(len(character_to_join_with)*-1)]

print(string_result)