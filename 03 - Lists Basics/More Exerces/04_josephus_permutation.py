def josephus_permutation(people, k):
    result = []
    index = 0
    while len(people) > 0:
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))
    return "[" + ",".join(map(str, result)) + "]"


people = list(map(int, input().split()))
k = int(input().strip())
print(josephus_permutation(people, k))
