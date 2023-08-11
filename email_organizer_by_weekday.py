

file_name = input('Enter the name of the file: ')

fhand = open(file_name)
counts = dict()                                 # add an empty dictionary
for line in fhand:
    words = line.split()                        # separate the text into individual words
    if len(words) < 3 or words[0] != 'From':    # Discard words smaller than 3 digits or that do not start with 'From'
        continue
    else:
        if words[2] not in counts:              #if the word is not in the dictionary, add it and assign value 1
            counts[words[2]] = 1
        else:
            counts[words[2]] +=1                 # Else, Take the third word, which correspond to the day of the week, 
#                                                #add it to the dictionary and assign value 1'''
print(counts)

