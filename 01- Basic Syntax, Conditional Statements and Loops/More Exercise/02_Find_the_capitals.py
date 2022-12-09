word = input()

uppercase = []
uppercase_position_counter= -1

for letter in word:
    uppercase_position_counter += 1
    if letter.isupper():
        uppercase.append(uppercase_position_counter)

print(uppercase)