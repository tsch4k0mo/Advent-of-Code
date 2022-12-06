data = open('input.txt', 'r')
lines = data.readlines()
points = 0

for line in lines:
    [first, second] = [line[len(line) // 2:], line[:len(line) // 2]]
    intersection = set(first) & set(second)
    points += sum(ord(i) - 38 for i in intersection if ord(i) < 97)
    points += sum(ord(i) - 96 for i in intersection if ord(i) > 96)
print(points)
