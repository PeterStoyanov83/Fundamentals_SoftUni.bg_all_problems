targets = list(map(int, input().split()))

shots = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)

    if index >= len(targets):
        continue
    last_shot = 0

    if targets[index] != -1:
        last_shot = targets[index]
        targets[index] = -1
        shots += 1
    for num in range(len(targets)):
        if targets[num] > last_shot:
            targets[num] -= last_shot
        else:
            targets[num] += last_shot

print(f'Shot targets: {shots} ->', *targets)
