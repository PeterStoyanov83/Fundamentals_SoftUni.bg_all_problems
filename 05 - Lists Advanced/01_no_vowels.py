string = input()

vowels = ['a', 'o', 'e', 'i', 'u']

result = [char for char in string if char.lower() not in vowels]

print(''.join(result))
