def check_data_type(a, b):
    if a == "int":
        result = int(b) * 2
        return result
    elif a == "real":
        result = float(b) * 1.5
        return f"{result:.2f}"
    else:
        return f"${b}$"


data_type = input()
data_value = input()

print(check_data_type(data_type, data_value))
