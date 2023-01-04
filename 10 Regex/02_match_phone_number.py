import re

phone_numbers = input()

search_pat = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

result = re.findall(search_pat, phone_numbers)

print(", ".join(result))

"""The regular expression r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b' is used to match phone numbers from 
Sofia with the following characteristics:

It starts with "+359"
Then, it is followed by the area code "2"
After that, it is followed by a 7-digit number, separated into two groups of 3 and 4 digits, respectively
The different parts are separated by either a hyphen or a space
The phone number is followed by a word boundary
The regular expression consists of two alternatives:

\+359-2-\d{3}-\d{4}\b: This matches a phone number with hyphens as delimiters. It consists of the following parts:
\+359-2-: This matches the "+359-2-" prefix of the phone number.
\d{3}: This matches the first group of 3 digits.
-: This matches the hyphen.
\d{4}: This matches the second group of 4 digits.
\b: This matches the word boundary.
\+359 2 \d{3} \d{4}\b: This matches a phone number with spaces as delimiters. It consists of the following parts:
\+359 2 : This matches the "+359 2 " prefix of the phone number.
\d{3}: This matches the first group of 3 digits.
: This matches the space.
\d{4}: This matches the second group of 4 digits.
\b: This matches the word boundary.
The | symbol separates the two alternatives and allows the regular expression to match either of them."""
