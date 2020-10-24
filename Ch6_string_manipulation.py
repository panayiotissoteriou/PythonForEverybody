print("Hello, World!")

# Manupulating strings using libraries

# length of a string
fruit = "banana"
length_of_fruit = len(fruit)
print(length_of_fruit)

# writing a for loop for length of strings - my code
fruit = 'banana'
count = 0
for letter in fruit:
    count = count + 1
    print(count, letter)
print("the length of string:", fruit, "is", str(count))

# a function for finding the indexes of a string - code from Edx
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# simplifying code from Edx using my code for length and index range
fruit = 'banana'
count = 0
index = 0
for letter in fruit:
    count = count + 1
    index = count -1
    print(range, count, letter)
print("the length of string:", fruit, "is", str(count))
print("the index range of string:", fruit, "is", str(index))


# looping and counting letters
fruit = "banana"
count = 0
for letter in fruit:
    if letter == "a" :
        count = count + 1
    print(count)

print("Number of a's:",count)


# slicing strings - "from[] until up to and not including[]"
s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[5:30])
print(s[:3])
print(s[4:])

# using in in a logical operator
fruit = 'banana'
print('n' in fruit)        # should print True

if 'm' in fruit:
    print(False)    # should print false

stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))       # methods to use in str object type
stuff.twist()

# searching for a string using str.find()
fruit = 'banana'
print(fruit.find('na'))     # print 2 (NB: python uses 0 index numbering)
                            # but only prints the position of the first 'na'

print(fruit.find('aa'))     # prints -1, which means did not find it

# str.replace
say = 'Hello Bob'
new_say = say.replace('Bob', 'Jane')
print(new_say)

new_new_say = say.replace('o', 'X')
print(new_new_say)

# removing whitespace w/ str.strip (or str.lstrip [for left whitespace], or str.rstrip [right whitespace])
greet = '   Hello Bob   '
print(greet.strip())

# searching for strings starting with a specific prefix using str.startswith()
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))         # Case sensitive! - prints False

# Parsing and extracting - the hard way
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
at_position = data.find('@')
print(at_position)

space_after_at_position = data.find(' ',at_position)
print(space_after_at_position)

host = data[at_position : space_after_at_position]
print(host)

#splitting text Exercise: must print 0.8475 as a float
text = "X-DSPAM-Confidence:    0.8475";
zero_in_text = str(text.find('0'))
print(zero_in_text)
numbers_in_text = text[23:]
print(float(numbers_in_text))
