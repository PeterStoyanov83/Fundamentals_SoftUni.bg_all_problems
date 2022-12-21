words = input().split()


def merge(start_index, end_index, words):
    current_merge = []
    all_in_one_string = ""
    if start_index < 0:
        start_index = 0
    elif start_index > len(words):
        start_index = len(words) - 2
    if end_index > len(words):
        end_index = len(words) - 1
    current_merge += words[start_index:end_index + 1]
    for word in current_merge:
        all_in_one_string += word
    del words[start_index:end_index + 1]
    words.insert(start_index, all_in_one_string)


def divide(divide_index, how_many_pieces, words):
    how_long = len(words[divide_index])
    space_between = how_long // how_many_pieces
    string_to_change = words.pop(divide_index)
    result_ = []
    for x in range(how_many_pieces - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        words.insert(divide_index, x)


command = input()
while command != "3:1":
    command = command.split()
    operation = command[0]
    if operation == "merge":
        merge(int(command[1]), int(command[2]), words)
    elif operation == "divide":
        divide(int(command[1]), int(command[2]), words)
    command = input()

print(*words)


"""
9. *Anonymous Threat

Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and
 unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have
 been tasked to analyze the software of the virus and observe its actions on the data.

You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII
character except whitespace. Then you will begin receiving commands in one of the following formats:

· merge {startIndex} {endIndex}
· divide {index} {partitions}

Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
In other words, you should concatenate them. Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}

If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.

Every time you receive the divide command, you must divide the element at the given index into several small substrings
 with equal length. The count of the substrings should be equal to the given partitions.

Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}

If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal
lengths and make the last one - the longest.

Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}

The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.

Input
· The first input line will contain the array of data.
· On the next several input lines, you will receive commands in the format specified above.
· The input ends when you receive the command "3:1".

Output
· As output, you must print a single line containing the elements of the array, joined by a space.

Constrains

· The strings in the array may contain any ASCII character except whitespace.
· The startIndex and the endIndex will be in the range [-1000…1000].
· The endIndex will always be greater than the startIndex.
· The index in the divide command will always be inside the array.
· The partitions will be in the range [0…100].
· Allowed working time/memory: 100ms / 16MB.

Examples

Input Output
Ivo Johny Tony Bony Mony
merge 0 3
merge 3 4
merge 0 3
3:1 IvoJohnyTonyBonyMony
abcd efgh ijkl mnop qrst uvwx yz
merge 4 10
divide 4 5
3:1 abcd efgh ijkl mnop qr st uv wx yz
"""