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


"""
9. Sorting Hat

Help out the sorting hat to sort the newhealth students in the houses of Hogwarts. You will be receiving names until the command "Welcome!". The length of each name determines in which house the student is going:

· If the name is less than 5 chars, the student is going into Gryffindor

o Print "{name} goes to Gryffindor."

· If the name is exactly 5 chars, the student is going into Slytherin

o Print "{name} goes to Slytherin."

· If the name is exactly 6 chars, the student is going into Ravenclaw

o Print "{name} goes to Ravenclaw."

· If the name is more than 6 chars, the student is going into Hufflepuff

o Print "{name} goes to Hufflepuff."

While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program. No more sorting for today!

If all students are sorted successfully, print "Welcome to Hogwarts."

Examples

Input Output
Harry
Ron
Ginny
Draco
Welcome! Harry goes to Slytherin. Ron goes to Gryffindor. Ginny goes to Slytherin. Draco goes to Slytherin. Welcome to Hogwarts.

Luna

Hermione

Neville

Voldemort Luna goes to Gryffindor. Hermione goes to Hufflepuff. Neville goes to Hufflepuff. You must not speak of that name!"""