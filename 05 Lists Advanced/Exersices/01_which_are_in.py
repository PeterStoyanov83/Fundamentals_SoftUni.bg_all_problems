first_list = input().split(', ')
second_list = input().split(', ')

substring =[]

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_word in substring:
            substring.append(first_word)

print(substring)

"""
1. Which Are In?

You will be given two sequences of strings, separated by ", ". Print a newhealth list containing only the strings from the
 first input line, which are substrings of any string in the second input line.

Example
Input                                       Output

arp, live, strong
lively, alive, harp, sharp, armstrong       ['arp', 'live', 'strong']

tarp, mice, bull
lively, alive, harp, sharp, armstrong       []
"""