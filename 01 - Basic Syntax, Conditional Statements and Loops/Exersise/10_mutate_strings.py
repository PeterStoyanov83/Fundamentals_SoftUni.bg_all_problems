first_str = input()

second_str = input()

last_printed_str = first_str

for character in range( len(first_str)):
    left_part = second_str[:character+1]
    right_part = first_str[character+1:]
    current_str = left_part + right_part
    if current_str == last_printed_str:
        continue
    last_printed_str = current_str
    print(current_str)
