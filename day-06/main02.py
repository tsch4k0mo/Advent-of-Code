data = open('input.txt', 'r')
lines = list(data.readlines()[0])
for position in range(14, lines.__len__()):
    if len(set(lines[position - 14:position])) == 14:
        print(position)
        break
