passengers = int(input())

capacity = int(input())

courses_of_elevator = passengers // capacity
if passengers % capacity != 0:
    courses_of_elevator += 1

print(courses_of_elevator)
