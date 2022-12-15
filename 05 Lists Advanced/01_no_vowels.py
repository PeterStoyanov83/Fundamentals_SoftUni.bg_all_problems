
string = input()

vowels = ['a', 'o', 'e', 'i', 'u']

result = [char for char in string if char.lower() not in vowels]

print(''.join(result))



"""
1. No Vowels

Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

Examples

Input           Output

Python          Pythn

ILovePython     LvPythn
"""