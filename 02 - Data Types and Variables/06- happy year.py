year = int(input())

happy_year = False

while not happy_year:
    year += 1
    set_year = set()  #this is a set - it is a data type that keeps and returns only unique values assigned to it

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year = len(set_year) == len(str(year))

print(year)