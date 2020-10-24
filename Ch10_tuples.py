# tuples are like lists, but are in ( )
x = ('John', 'Sally', 'Mark')
print(x)
print(x[2])

# tuples are not mutable, unlike Lists
x_lst = ['e', 2, 'we', 'cyp']
x_lst[2] = 12
print(x_lst)

x_tupl = ('x', 'e', 2, 3, 10)
x_tupl[2] = 'max'       # gives traceback

#strings also not mutable
x_str = 'FAIR'
x_str[3] = 0        # traceback

# cannot append, sort or reverse a tuple
# but can count and index
t = tuple()
print(dir(t))

# can assign values to 2 tuples at the same time
#       Simultaneous assignment statement
(x, y) = ('Fred', 4)
print(x)
print(y)

# the dict.items() function returns a list of tuples
d = dict()
d['csev'] = 4
d['zhen'] = 5
for (k,v) in d.items():
    print(k,v)
print(d.items())

#tuples are comparable: compared in an order, so: 'is 4 > 1?'
print((4, 'Fred', 'No') > (1, 'Abbey', 'Yes'))      #prints True

# dictionaries an unsorted: to sort them:
d = {"a" : 10, "b" : 1, "c" : 22}
print(d.items())
print(sorted(d.items()))        # sorts based on the key value of the dictionary

#looping through a dictionary in key order
d = {"a" : 10, "b" : 1, "c" : 22}
for k,v in sorted(d.items()):
    print(k,v)

# looping through a dictionary in value order:
c = {"a" : 10, "b" : 1, "c" : 22}
tmp = list()
for k,v in c.items():
    tmp.append( (v,k) )
print(tmp)

tmp= sorted(tmp, reverse=True)      # reverse = True makes ordering from high to low
print(tmp)


# example: counting the 10 most common Words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key,value in counts.items():
    new_tup = ( value, key)
    lst = lst.append(new_tup)           #might need to remove 'lst ='

lst = sorted(lst, reverse = True)

for val,key in lst[:10]:            # because the order is val,key
    print( key, val)                # reverse the pritning order

# lines 69-77 could be written in a single line using List Comprehension
c = {"a" : 10, "b" : 1, "c" : 22}

print( sorted([ (v,k) for k,v in c.items() ], reverse = True ) )



# exercise: Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
#for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
#the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time_of_day = dict()

for line in handle:
    if line.startswith('From '):                #selects lines that start with 'From'
        time = line.split()[5]                  #selects index 5 which is the time of sent email
        hour = time.split(":")[0]               #seperates time into hh:mm:ss and selects hh
        #print(hour)
        time_of_day[hour] = time_of_day.get(hour, 0) + 1    #adds hh into time of day dict

new_lst = list()                                #temp list
for k,v in time_of_day.items():                 #
    newtupl= (v, k)                             #reverses key and value positions into a tuple
    new_lst.append(newtupl)                     #adds tuples into the list

new_lst = sorted(new_lst, reverse = True)       #sorts based on value
                                                #descending order - (desc order not needed for exercise)
solution = list()                               # reverses from v,k to k, v
for v, k in new_lst:
    newertup = (k,v)
    solution.append(newertup)

sorted_solution = sorted(solution)              #sorts based on k, v

for k,v in sorted_solution:                     #prints as asked
    print(k,v)
