def send_message(numbers, text):
    message = ""
    for num in numbers:
        index = sum(int(digit) for digit in str(num)) % len(text)
        message += text[index]
        text = text[:index] + text[index + 1:]
    return message


numbers = list(map(int, input().split()))
text = input().strip()
print(send_message(numbers, text))
