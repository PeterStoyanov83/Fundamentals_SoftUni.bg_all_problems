morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}


def translate_to_english(message):
    words = message.split(" | ")
    result = ""

    for word in words:
        for letter in word.split():
            for key, value in morse_code.items():
                if letter == value:
                    result += key.upper()
        result += " "

    return result


message = input()
english_message = translate_to_english(message)
print("".join(english_message))