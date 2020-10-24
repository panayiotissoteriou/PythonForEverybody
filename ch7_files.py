print("Hello World")

# new line statement: /n ; NB: \n is counted as 1 character
new_line_text = 'Hello\nWorld'
new_line_text
print(new_line_text)

# opening a file: the variable name we give to the txt file is called a file handle
# a file handle reads the contents of a file as a sequence of lines
file = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt', 'r')

file = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt', 'r')
count = 0
for lines in file:          # it reads all lines of the .txt file and adds 1 to count for every line
    count = count + 1
    print(count)
print("line count:",count)


# reading a file as a single string, with the enters read as \n  [the 'r' in the open command should be missing]
file_2 = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt')
read_file_2 = file_2.read()
print(len(read_file_2))
print(read_file_2[:15])

file_2 = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt')
for line in file_2:
    if line.startswith('From:'):
        print(line)                 # print() adds \n too, so we get 2 spaces between lines starting with 'From:'
                                    # we can deal with these whitespaces with .strip
# without whitespace:
file_2 = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt')
for line in file_2:
    line = line.rstrip()                #.strip could also be used # str.command() makes a copy of str (under a new varaible)
                                                # does not change str
    if line.starts with('From:'):
        print(line)

# if not loops: - prints the exact same thing
file_2 = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt')
for line in file_2:
    line = line.rstrip()                #.strip could also be used
    if not line.startswith('From:'):    #skips all lines without 'From:'
        continue
    print(line)

# if not loop example 2
file_2 = open('/Users/panayiotissoteriou/Desktop/panayiotis/online courses/bioinformatics specialisation/Data structures_python/for_ch7.txt')
for line in file_2:
    line = line.rstrip()                #.strip could also be used
    if not ':' in line :                #skips all lines without ':'
        continue
    print(line)


# opening a file using an input name
input_file = input("Enter file name: ")
input_file_handle = open(input_file)
count = 0
for lines in input_file_handle:
    if lines.startswith("From:"):
        count = count + 1
print('There are', count, "lines in", input_file)

# dealing with bad inputs with try except
input_file = input("Enter file name: ")
try:
    input_file_handle = open(input_file)
except:
    print("File cannot be opened: ",input_file)
    quit()

count = 0
for lines in input_file_handle:
    if lines.startswith("From:"):
        count = count + 1
print('There are', count, "lines in", input_file)


# exercise: Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
floats = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue # skips all lines without "X-DSPAM ..."
    count = count + 1
    floats = float(line[20:]) + floats                  # print(line.find('0.'))

#print("Count is:",count, "float total is:",floats, "average is:",floats/count)
print("Average spam confidence:",floats/count)
