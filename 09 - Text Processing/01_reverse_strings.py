while True:
    text = input()
    if text == "end":
        break
    print(f"{text} = {text[::-1]}")
    # rev_text = text[::-1]
    # print(f'{text} = {rev_text}')
