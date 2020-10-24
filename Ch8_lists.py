print('Hello World')

# the range() function - returns a list
print(range(4))         # 0 up to, but not including 4!

#iteraton loop example:
friends = ['John', 'Tony', 'Andrew']

for friend in friends:                  #if we ised i instead of friends, we don't know what i is
    print("Happy birthday,",friend)

friends = ['John', 'Tony', 'Andrew']
print(range(len(friends)))
# the same loop, using range, aka counted loop
for i in range(len(friends)):
    friend = friends[i]                 #using this method, we know the what i is
    print("Happy birthday,",friend)

# concatenating lists
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# slicing lists using [] - from, up to and not including
c = [2, 4, 6, 7, 8, 9, 10]
print(c[1:4])
print(c[:])

# methods in a list object
x = list()
print(type(x))
print(dir(x))

# list.append() adds things into a list
empty_list = []
empty_list.append("not anymore")
empty_list.append(2)
empty_list.append(5)
empty_list.append(99)
empty_list.append(102)
empty_list.append("what")
print(empty_list)

# searching in a list using: in & not in
some_list = ["what", "bro", 2, 222, 340, 2341]
some_list
print("what" in some_list)
print(999 in some_list)
print(1 not in some_list)

# list.sort()
list_friends = ['Phoebe', 'Rachel', "Ross", "Chandler", "Joey"]
list_friends.sort()
print(list_friends)
print(list_friends[1])

#useful built-in functions: len, max, min, sum, sum/len

# splitting a string, and forming a list - splits on whitespace, each block of whitespace is considered 1 character
string = "with three words"
stuff = string.split()
print(stuff)
print(len(stuff))
print(stuff[1])

        # can split based on a defined character
char_string = "what;is;up;people"
split_string = char_string.split(';')
print(split_string)


# Exercise 1: Open the file romeo.txt and read it line by line. For each line, split the line into a list of words
# using the split() method. The program should build a list of words. For each word on each line check to see
# if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
    # solution 1
fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    words = line.strip()
    #print("lines: ",words)
    ind_words = line.split()
    #print("words",ind_words)
    lst = lst + ind_words

lst.sort()
#print(lst)

# converting list into a set removes duplicates
ListSet = set(lst)
back_to_list = list(ListSet)
back_to_list.sort()
print(back_to_list)

    #   solution 2
fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = []
for line in fh:
    words = line.strip()
    #print("lines: ",words)
    for word in line.split() :
        if word not in lst:         #only adds words that are not in lst
            lst.append(word)
lst.sort()
print(lst)

# Exercise 2: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From '
# like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 You will parse the From line using split()
# print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out
# a count at the end. Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.
fname = input("Enter file name: ")
fh = open(fname, 'r')

count = 0
for line in fh:
    line = line.rstrip()
    #print('Line:',line)
    if line == '' :             #skips blank lines
        #print("skip blank")
        continue
    wrds = line.split()
    #print("words:",wrds)
    # guardian
    if len(wrds) < 1 or wrds[0] != 'From:':      #skips lines that are empty, by increasing the number you make the guardian stronger
        continue                                 #skips lines that don't start with 'From:'
                                                #can combine both if statements, and works in order
    count = count + 1
    print(wrds[1])

print("There were", count, "lines in the file with From as the first word")
