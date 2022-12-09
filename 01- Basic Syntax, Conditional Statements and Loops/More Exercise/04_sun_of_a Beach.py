word = input().lower()
words_to_check = "sand", "water", "fish", "sun"
counter = 0
counter += word.count("sand")
counter += word.count("water")
counter += word.count("fish")
counter += word.count("sun")
print(counter)


"""
4. Sum of a Beach

Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", 
"Fish", and "Sun" appear (case insensitive).

Examples
Input                       Output

WAtErSlIde                  1
GolDeNSanDyWateRyBeaChSuNN  3
gOfIshsunesunFiSh           4
cItYTowNcARShoW             0
"""