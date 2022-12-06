data = open('input.txt', 'r')
lines = data.readlines()
sums = []
value = 0

for line in lines:
    line = line.rstrip()
    if line == '':
        sums.append(int(value))
        value = 0
    else:
        value += int(line)

print(max(sums))
