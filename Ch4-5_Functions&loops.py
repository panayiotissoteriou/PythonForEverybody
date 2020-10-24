# Functions
# Defining a function is like creating a variable
# Used for reusable code
def thing():
    print("Hello")
    print("Fun")

thing()
print("sup")
thing()

# Example: Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
#Do not name your variable sum or use the sum() function.
def computepay(h,r):
    if h < 40:
        pay = f_r * f_h                 # h and r could be used instead of f_r and f_h - Works
        return pay
    elif h > 40:
        pay_2 = (40 * f_r) + ((f_h-40) * (f_r * 1.5))
        return pay_2


hrs = input("Enter Hours:")
f_h = float(hrs)
rate = input("Enter Rate:")
f_r = float(rate)

p = computepay(f_h,f_r)
print("Pay",p)

# loops and iteration

# while loops run until some logical condition is false or hits a break
# while loops: break skips out of the loop & continue skips at the beginning of the loop
# while loop example:
while True:
    line == input("> ")
    if line == "done" :
        break
    print(line)
print("Done")

while True:
    line = raw_input('> ')
    if line[0] == "#" :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# for loops: aka definite loop - i refers to integer, but any other letter/word can be used
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

#example 2
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:',friend)
print("Done")

# finding the lagest value
largest_so_far = -1                     # there is an improvement to this
print("Before", largest_so_far)
for number in [9, 41, 12, 3, 74, 15]:
    if number > largest_so_far:
        largest_so_far = number
    print largest_so_far,number

print"After", largest_so_far

# finding the smallest value
smallest_so_far = 100                   # there is an improvement to this
print "Before", smallest_so_far
for number in [9, 41, 12, 3, 74, 15]:
    if number < smallest_so_far:
        smallest_so_far = number
    print smallest_so_far,number

print "After", smallest_so_far

# using None
smallest = None
print "Before"
for number in [1, 12,4, 6,2 ,35, 46, 7, 36, 26, 25]:
    if smallest is None:               # V important to use is, or ==. must give boolean value
        smallest = number
    elif number < smallest:
        smallest = number
        print smallest, number
print "After", smallest

# Counting
count = 0
print("Before",count)
for i in [9, 23, 82, 34, 22, 18, 1]:
    count = count + 1
    print(count, i)
print('After',count)

# summing
sum = 0
print("Before", sum)
for i in [2,3,234,25,1,4,5,2,4,4]:
    sum = sum + i                   # this is the difference between counting
    print(sum, i)
print("Total",sum)

# averaging
count = 0
sum = 0
print "Before",count,sum
for i in [10, 10, 15, 25, 50]:
    count = count + 1
    sum = sum + i
    print count,sum,i
print "After",count,sum,sum/count

# Filtering
print("Before")
for i in [34, 10, 20, 19, 84, 23, 23, 5, 1, 0]:
    if i > 20:
        print "large value",i
print("After")

# Filtering using Boolean values
# output is whether a 4 exists at least once
four = False
print "Before", four
for i in [1, 2, 3, 4, 5, 6]:
    if i == 4:
        four = True
    print four, i
print "After",four


# Exercise: Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than
# a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below
largest = None
smallest = None
myset = []
while True:
    num = input("Enter a number: ")
    if num == "done":
    	break
    try:
        inum = int(num)             # float() could be used as well
    except:
        inum = -1
    if inum < 0:
    	print("Invalid input")
    else:
        myset.append(inum)

for i in myset:
    if largest is None:
        largest = i
    elif largest < i:
        largest = i
print("Maximum is",largest)

for i in myset:
    if smallest is None:
        smallest = i
    elif smallest > i:
        smallest = i
print("Minimum is",smallest)

# another example that prints total, count and average (simplified)
total = 0
count = 0
while True:
    sval = input('Enter number: ')
    if sval == "done":
        break
    try:
        float_val = float(sval)
    except:
        print("Invalid input")
        continue                    #restarts the loop
        #  print(float_val)
    total = total + float_val
    count = count + 1

print(total,count, total/count)
