data = open('input.txt', 'r')
lines = data.readlines()
score = 0

for line in lines:
    enemy, me = line.split()
    enemy = ord(enemy) - 65
    result = ord(me) - ord('X')
    if result == 0:
        score += (enemy + 2) % 3 + 1
    elif result == 1:
        score += 3 + enemy + 1
    elif result == 2:
        score += 6 + (enemy + 1) % 3 + 1
print(score)
