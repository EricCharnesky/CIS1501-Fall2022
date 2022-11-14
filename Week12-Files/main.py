import os
import csv

# looks for a file named test.txt

# will crash if the file doesn't exist

# absolute path has the drive and all folders
# relative path, just has the file name
test_file = open('c:/temp/test.txt')

contents = test_file.readlines()

for line in contents:
    # avoid the extra new line when printing file contents
    print(line, end='')

# after you are done with the file, close it explicitly
test_file.close()

# similar to above, with will call close at the end of the block
with open("test.txt") as test_file:

    contents = test_file.readlines()

    for line in contents:
        # avoid the extra new line when printing file contents
        print(line, end='')

filename = input("Enter the name of a file to write")

if os.path.exists(filename):
    choice = input("There is already a file with that name, do you want to overwrite it?")

    if choice.lower() == 'y':
        # use 'w' for writing - WARNING this will overwrite a file
        file_to_write = open(filename, 'w')

        # when writing, be sure to add your own new lines
        file_to_write.write("here's line 1 from python\n")
        file_to_write.write("here's line 2 from python\n")

with open('tempdata.csv', 'r') as csvfile:
    temp_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in temp_reader:
        print(f'Row #{row_num}:', row)
        row_num += 1