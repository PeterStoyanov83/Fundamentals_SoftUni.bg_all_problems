text = input().split(" ")

filtered_words = [word for word in text if len(word) % 2 == 0]

print('\n'.join(filtered_words))


"""
3. Word Filter

Using comprehension, write a program that receives some text, separated by space, and take only those words whose
length is even. Print each word on a new line.

Examples

Input                           Output

kiwi orange banana apple        kiwi orange banana

pizza cake pasta chips          cake
"""