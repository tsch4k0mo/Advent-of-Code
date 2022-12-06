data = open('input.txt', 'r')
lines = list(data.readlines()[0])
for position in range(4, lines.__len__()):
    if len(set(lines[position - 4:position])) == 4:
        print(position)
        break
