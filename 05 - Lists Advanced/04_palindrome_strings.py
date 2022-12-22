def palindrome_filter(word):
    if word == word[::-1]:
        return word


list_of_strings = input().split(" ")

palindrome = input()
palindromes = [word for word in list_of_strings if palindrome_filter(word)]

print(f'{palindromes}')
print(f'Found palindrome {palindromes.count(palindrome)} times')
