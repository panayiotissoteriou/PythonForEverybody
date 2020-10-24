# cmd + i to run the code
# to print on Terminal
print("Hello Python")

# while loop
n = 5
while n > 0:
    print(n)
    n = n-1
print("Blastoff!")

# Inputs - asks for input when ran on Terminal
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:",pay)

# indenting
x = 5
if x > 2 :
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2")

# indenting 2 - range 5 includes 0-4
# using an if loop within a for loop is called nesting
for i in range (5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
print("All done")

# 2-way decisions
x = 5
if x > 4:
    print("Bigger than 4")
else:
    print("not bigger than 4")
print("All Done")

# multi-way decisions - code runs in the order of code written
x = 3
if x > 10:
    print("Bigger than 10")
elif x > 5:
    print("bigger than 5")
elif x < 2:
    print("smaller than 2")
# else, instead of elif, could be used here
elif x > 2:
    print("between 2 and 5")
# will never run
else:
    print("i don't even know")


# Try / Except example
number = input("Enter Number: ")
try:
    ival = int(number)      # this code might fail when letters are written
except:                     # if there is a traceback this code runs
    ival = -1

if ival > 0:
    print("Nice work")
else:                       # ival = -1, so < 0, so "not a number" prints
    print("Not a number")
