data = open('input.txt', 'r')
lines = data.readlines()
points = 0
j = 0

while j < lines.__len__():
    [first, second, third] = [lines[j], lines[j + 1], lines[j + 2]]
    intersection = set(first.strip()) & set(second.strip()) & set(third.strip())
    i = intersection.pop()
    if ord(i) < 97:
        points += ord(i) - 38
    if ord(i) > 96:
        points += ord(i) - 96
    j += 3
print(points)
