command = ""
voldemort = False
while command != "Welcome!":
    name_of_student = command
    if name_of_student == "Voldemort":
        print("You must not speak of that name!")
        voldemort = True
        break

    if len(name_of_student) != 0 and len(name_of_student) < 5:
        print (f"{name_of_student} goes to Gryffindor.")
    elif len(name_of_student) == 5:
        print (f"{name_of_student} goes to Slytherin.")
    elif len(name_of_student) == 6:
        print(f"{name_of_student} goes to Ravenclaw.")
    elif len(name_of_student) > 6:
        print(f"{name_of_student} goes to Hufflepuff.")
    command = input()

if voldemort == False:
    print ("Welcome to Hogwarts.")
