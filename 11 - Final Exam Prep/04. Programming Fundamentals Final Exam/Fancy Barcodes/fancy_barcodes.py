import re

number_of_barcode = int(input())
for _ in range(number_of_barcode):
    data = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'

    """"@+#+[A-Z][A-Za-z0-9]{4,}[A-Z]#+@+"
    This RegEx will match a string that starts with "@" followed by one or more "#" symbols, then a capital letter, 
    followed by 4 or more characters that are either letters (upper or lowercase) or digits, followed by a capital 
    letter, followed by one or more "#" symbols, and ending with "@"."""

    result = re.match(pattern, data)

    if not result:
        print('Invalid barcode')
    else:
        extract_numbers = re.findall('\d', result.group())

        if not extract_numbers:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_numbers)}")



