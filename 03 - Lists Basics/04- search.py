n = int(input())
search_word = input()
list_of_words = []

for i in range(n):
    current_string = input()
    list_of_words.append(current_string)

print(list_of_words)
for i in range(len(list_of_words) - 1, -1, -1):
    element = list_of_words[i]
    if search_word not in element:
        list_of_words.remove(element)

print(list_of_words)


"""
4. Search

On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
you will be given some strings. You should add them to a list and print them. After that, you should filter
out only the strings that include the given word and print that list too.

Example

Input                               Output

3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni           ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
                                    ["I study at SoftUni", "I learn Python at SoftUni"]
"""