"""
CP1404 Prac 04 files.py
Code to demonstrate use of files
"""
# 1
OUTPUT_FILE = "name.txt"
outfile = open(OUTPUT_FILE, 'w')
name = input("Please enter your name: ")
print(name, file=outfile)
outfile.close()
# 2
INPUT_FILE = "name.txt"
infile = open(INPUT_FILE, 'r')
name_from_file = (infile.readline())
print(f"Your name is {name_from_file}")
infile.close()
# 3
NUMBER_FILE = "numbers.txt"
number_infile = open(NUMBER_FILE, 'r')
number_1 = int(number_infile.readline())
number_2 = int(number_infile.readline())
number_infile.close()
print(number_1 + number_2)
# 4
NUMBER_FILE = "numbers.txt"
number_infile = open(NUMBER_FILE, 'r')
count = 0
for line in number_infile:
    count += int(line)
number_infile.close()
print(count)