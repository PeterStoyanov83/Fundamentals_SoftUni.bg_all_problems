first_list = input().split(', ')
second_list = input().split(', ')

substring = []

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_word in substring:
            substring.append(first_word)

print(substring)
