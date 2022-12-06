import re
data = open('input.txt', 'r')
lines = data.readlines()
containers = [['R', 'C', 'H'], ['F', 'S', 'L', 'H', 'J', 'B'], ['Q', 'T', 'J', 'H', 'D', 'M', 'R'],
              ['J', 'B', 'Z', 'H', 'R', 'G', 'S'],
              ['B', 'C', 'D', 'T', 'Z', 'F', 'P', 'R'], ['G', 'C', 'H', 'T'], ['L', 'W', 'P', 'B', 'Z', 'V', 'N', 'S'],
              ['C', 'G', 'Q', 'J', 'R'], ['S', 'F', 'P', 'H', 'R', 'T', 'D', 'L']]
result = []
for line in lines:
    numbers = re.findall(r'\d+', line)
    containers[int(numbers[2]) - 1] = containers[int(numbers[1]) - 1][:int(numbers[0])][::-1] + (containers[int(numbers[2]) - 1])
    del containers[int(numbers[1]) - 1][:int(numbers[0])]
for container in containers:
    result.append(container[0])
print(result)
