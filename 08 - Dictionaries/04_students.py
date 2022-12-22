students = {}

command = input().split(":")

while len(command) > 1:

    name, id, course = command[0], command[1], command[2]  # identifying all the variables

    if course not in students.keys():  # structutring the list in dictionary
        students[course] = []

    students[course].append(f'{name} - {id}')

    command = input().split(":")

searched_course = command[0].replace("_", " ")

for student in students[searched_course]:
    print(student)
