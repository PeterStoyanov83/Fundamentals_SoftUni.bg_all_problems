n = int(input())

for i in range(0, n + 1):
    for k in range(0, n + 1):
        for j in range(0, n + 1):
            for k in range(0, n + 1):
                print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 +j)}{chr(97+k)}')
