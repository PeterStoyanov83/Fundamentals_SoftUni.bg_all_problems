parking = {}

number_of_cars = int(input())

for car in range(number_of_cars):
    current_driver = input().split()
    action = current_driver[0]

    if action == "register":
        driver = current_driver[1]
        license_plate_number = current_driver[2]
        if driver in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[driver] = license_plate_number  # adding to list
            print(f"{driver} registered {license_plate_number} successfully")
    if action == "unregister":
        driver = current_driver[1]
        if driver not in parking.keys():
            print(f"ERROR: user {driver} not found")
        else:
            print(f'{driver} unregistered successfully')
            del parking[driver]
for driver, license_plate_number in parking.items():
    print(f'{driver} => {license_plate_number}')
