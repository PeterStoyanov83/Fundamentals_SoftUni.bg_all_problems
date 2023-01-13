activation_key = input()

data = input()

while not data == "Generate":
    split_data = data.split(">>>")
    if split_data[0] == "Contains":
        substring = split_data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif split_data[0] == "Flip":
        state, start_index, end_index = split_data[1:]
        start_index, end_index = int(start_index), int(end_index)
        if state == "Upper":
            activation_key = activation_key[0:start_index] + \
                             activation_key[start_index:end_index].upper() + activation_key[end_index:]
        else:
            activation_key = activation_key[0:start_index] + \
                             activation_key[start_index:end_index].lower() + activation_key[end_index:]
        print(activation_key)
    elif split_data[0] == "Slice":
        start_index, end_index = int(split_data[1]), int(split_data[2])
        activation_key = activation_key[0:start_index] + activation_key[end_index:]
        print(activation_key)
    data = input()

print(f"Your activation key is: {activation_key}")