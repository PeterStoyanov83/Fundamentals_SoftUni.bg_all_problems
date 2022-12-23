exams_info = {
    'submissions': {},
    'points': {}
}

command = input()
while command != "exam finished":
    command = command.split("-")
    if "banned" not in command:
        name, language, points = [int(name) if name.isdigit() else name for name in command]

        exams_info['submissions'][language] = exams_info['submissions'].get(language, 0) + 1
        exams_info['points'][name] = exams_info['points'].get(name, points)

        if exams_info['points'][name] < points:
            exams_info['points'][name] = points

    elif "banned" in command:
        name = command[0]
        del exams_info['points'][name]

    command = input()

print(f"Results:")
[print(f"{user} | {exams_info['points'][user]}") for user in exams_info['points']]
print(f"Submissions:")
[print(f"{language} - {exams_info['submissions'][language]}") for language in exams_info['submissions']]