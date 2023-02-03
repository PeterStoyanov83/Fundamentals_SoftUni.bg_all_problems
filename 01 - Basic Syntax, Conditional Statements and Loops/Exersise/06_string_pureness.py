unpure_symbols = {
    "forbitten symbols": [",", ".", "_"]
}
number_of_strings = int(input())

for word  in range(number_of_strings):
    string_input = input()
    for letter in string_input:
        if letter in unpure_symbols["forbitten symbols"]:
            print(f"{string_input} is not pure!")
            break

    else:
        print(f"{string_input} is pure.")

