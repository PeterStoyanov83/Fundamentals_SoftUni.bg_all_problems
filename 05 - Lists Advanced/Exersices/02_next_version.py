
version = [int(number) for number in input().split(".")]

version[-1] += 1

for current_index in range(len(version) - 1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        version[current_index-1] += 1

print(".".join(str(s) for s in version))

# version = input()
# version = version.replace(".", "")
# print(".".join(int(version))+1)


"""
2. Next Version

You are fed up with changing the version of your software manually. Instead, you will create a little script that
will make it for you.

You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".

The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the
previous number. For more clarification, see the examples below.

Note: there will be no case in which the first number will become greater than 9.

Example

Input           Output

1.2.3           1.2.4

1.3.9           1.4.0

3.9.9           4.0.0
"""
