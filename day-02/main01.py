data = open('input.txt', 'r')
lines = data.readlines()
score = 0

for line in lines:
    enemy, me = line.split()
    enemy = ord(enemy) - 65
    me = ord(me) - ord('X')
    if enemy == me:
        score += 3
    if (me - enemy) % 3 == 1:
        score += 6
    score += me + 1
print(score)
