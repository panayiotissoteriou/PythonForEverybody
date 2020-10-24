#dictionaries
print("hello world!")

ExDict = dict()         # or {}
ExDict['age'] = 23
ExDict['name'] = "Pan"
ExDict['Study'] = "Bio"
ExDict[4] = "woah"
ExDict[True] = False
print(ExDict)

ExList = list()         # or []
ExList.append(23)
ExList.append("Pan")
ExList.append("Bio")
print(ExList)

#Main diff b/t Dicts and Lists is the key, the value is the same(23, "Pan", 'Bio', etc):
# Lists are numeric starting from 0
print(ExList[1])
# Dicts' keys are what you label them
print(ExDict['name'])
print(ExDict[4])
print(ExDict[True])

#Empty dictionary
empty = { }
print(empty)

#filling the dictionary:
filling = {'Jan' : 1, 'Feb' : 2, 'March' : 3}
print(filling)

# counting names
counts = {}
names = ['John', 'Papa', 'Mike', 'Mike', 'Faye', 'John']
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# Important with dictionaries: if there is no key in the dictionary, put one; if there is, do something to existing value

# the dict.get() method: 0 is the default value - what you get if variable doesnt exist
x = counts.get(name, 0)
print(x)

# simpified way of counting names:
#   if new name (not in dict), then = 0, hence adds 1
#   if already in dict, gets the number, and adds 1
counts = {}
names = ['John', 'Papa', 'Mike', 'Mike', 'Faye', 'John']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


# counting words in a file
word_count = {}
line = input('Enter a line of text:')

words = line.split()
print("Words:",words)

print('Counting...')
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("counts",word_count)


# for loops: goes through the key, unlike in lists (where it goes through the values)
names_dict = {'John' : 1, 'Papa' : 10, 'Mike' : 20, 'Mikey' : 40, 'Faye' : 50, 'Johnny' : 100}
for key in names_dict:
    print key, names_dict[key]

# Retrieviing lists from dictionaries
names_dict = {'Jon' : 1, 'Papa' : 10, 'Mikey' : 20, 'Mike' : 40, 'Faye' : 50, 'John' : 100}
print(list(names_dict))     # prints the keys in a list
print(names_dict.keys())    # prints the keys in a list
print(names_dict.values())  # prints the valyes in a list
print(names_dict.items())   #prints both values and keys in a list


# key-value pairs
names_dict = {'Johnny' : 1, 'Papa' : 10, 'Mike' : 20, 'Mikee' : 40, 'Faye' : 50, 'John' : 100}
for kkk,vvv in names_dict.items():
    print(kkk,vvv)

# counting and printing the most frequent word and its count
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigword = None
bigcount = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


# Exercise 1: Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear
#in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the
#most prolific committer.
data = input('Enter file:')
if len(data) < 1:
    data = 'mbox-short.txt'     # only need to press Enter to import this mbox-short.txt
dh = open(data)

senders_names = dict()

for line in dh:
    line = line.rstrip()        # makes lines
    #if line == '' :             #skips blank lines
        #continue
    #print("lines:",line)
    words = line.split()        #sepates lines into words
    #print("words:",words)
    if len(words) < 1 or words[0] != 'From:':      #skips lines that are empty, by increasing the number you make the guardian stronger
        continue
    #print(words)                                 #skips lines that don't start with 'From:'
                                                #can combine both if statements, and works in order
    for word in words :                          #shortened version: retrieve/create/update counter
        senders_names[word] = senders_names.get(word,0) + 1        #when new word: 1 is assigned to it, then adds 1 when reappears
print(senders_names)

 # finding the most common sender
largest = -1
thesender = None
#print(senders_names.items())
for k,v in senders_names.items():
    if v > 10 :
        continue
    print(k,v)
    if thesender is None or v > largest :
        largest = v
        thesender = k             #capture/remember the word that was largest
print(thesender,largest)



# Exercise 2: finding the most common word
data = input('Enter file:')
if len(data) < 1:
    data = 'mbox-short.txt'     # only need to press Enter to import this mbox-short.txt
dh = open(data)

senders_names = dict()
for line in dh:
    line = line.rstrip()
    #print("lines:",line)
    words = line.split()
    #print("words:",words)
    for word in words :
                                            #shortened version: retrieve/create/update counter
        senders_names[word] = senders_names.get(word,0) + 1        #when new word: 1 is assigned to it, then adds 1 when reappears
        print(word, 'new', senders_names[word])

largest = -1
theword = None
for k,v in senders_names.items():
    if v > largest :
        largest = v
        theword = k             #capture/remember the word that was largest
print("largest:",theword,largest)

        #LONG WAY
#        if word in senders_names:
#            senders_names[word] = senders_names[word] + 1       #if it exists, then you add 1 to its value
            #print("*Existing*")
#        else:
#            senders_names[word] = 1                         #if not in dict, you set its value to 1
            #print("*NEW*")
#        print(word, senders_names[word])        # skips lines w/o 'From' at start

        #ALTERNATIVE LONG WAY                                  #alternative way:
#        oldcount = senders_names.get(word,0)    # if key is not there, then 0 is assigned 0
#        print(word, 'old', oldcount)
#        newcount = oldcount + 1
#        senders_names[word] = newcount
#        print(word, 'new', newcount)
