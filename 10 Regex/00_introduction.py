"""Regular expressions (regex) are a powerful tool for matching patterns in strings. They are often used for text
 processing tasks such as searching, replacing, and validating input.

A regular expression is a sequence of characters that forms a search pattern. The search pattern can be used to match
(and sometimes replace) strings, or to perform some other manipulation of strings.

To use regular expressions in Python, you will need to import the re module and use its functions such as search,
match, findall, and sub.

Here are some examples of regular expressions and their meanings:

r"\d": A digit (0-9)
r"\D": A non-digit character
r"\w": An alphanumeric character (letter or digit)
r"\W": A non-alphanumeric character
r"\s": A white space character (space, tab, newline, etc.)
r"\S": A non-white space character
r"\b": A word boundary
r"\B": A non-word boundary
r"\A": The start of the string
r"\Z": The end of the string
r"^pattern": The start of the string, followed by the pattern
r"pattern$": The pattern, followed by the end of the string
r".": Any single character (except newline)
r"\d{3}": Exactly 3 digits
r"\d{3,}": 3 or more digits
r"\d{3,5}": Between 3 and 5 digits
r"\d+": 1 or more digits
r"\d*": 0 or more digits
r"[a-z]": A lowercase letter
r"[A-Z]": An uppercase letter
r"[a-zA-Z]": An alphabetic character (letter)
r"\w+": 1 or more alphanumeric characters

re.search  - returns 1st match
re.findall - returns all matches


"""

import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

print(x)

