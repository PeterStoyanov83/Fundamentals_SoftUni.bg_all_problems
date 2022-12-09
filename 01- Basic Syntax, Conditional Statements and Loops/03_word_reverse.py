word = input()
reversed_w = ""

for i in range(len(word) -1, -1, -1):
    reversed_w += word[i]
print(reversed_w)



'''

3. Word Reverse
Write a program that receives a single word, reverses it, and prints it.

Example:

Input       Output

Python      nohtyP

banana      ananab
'''