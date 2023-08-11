
file_name = input('Enter the name of the file: ')

fhand = open(file_name)
counts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in counts:
            counts[words[2]] = 1
        else:
            counts[words[2]] +=1

print(counts)