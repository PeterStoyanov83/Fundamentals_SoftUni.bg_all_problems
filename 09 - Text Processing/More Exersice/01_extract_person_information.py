import re
def extract_person_info(line):
    # Use a regular expression to find the name and age in the string
    name_regex = r"@(.+?)\|"
    age_regex = r"#(.+?)\*"
    name = re.search(name_regex, line).group(1)
    age = re.search(age_regex, line).group(1)


    # Print the extracted information
    print(f"{name} is {age} years old.")

# Read N lines of input from the user
N = int(input())
for i in range(N):
    line = input()
    extract_person_info(line)