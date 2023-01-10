number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car_info = input().split("|")
    car_name = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars[car_name] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break

    elif command[0] == "Drive":
        car_name = command[1]
        distance = int(command[2])
        fuel_needed = int(command[3])
        if cars[car_name]["fuel"] < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            cars[car_name]["fuel"] -= fuel_needed
            cars[car_name]["mileage"] += distance
            print(f"{car_name} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
            if cars[car_name]["mileage"] >= 100000:
                del cars[car_name]
                print(f"Time to sell the {car_name}!")

    elif command[0] == "Refuel":
        car_name = command[1]
        fuel_needed = int(command[2])

        if fuel_needed + cars[car_name]["fuel"] > 75:
            fuel_needed = 75 - cars[car_name]["fuel"]

        cars[car_name]["fuel"] += fuel_needed
        print(f"{car_name} refueled with {fuel_needed} liters")

    elif command[0] == "Revert":
        car_name = command[1]
        distance = int(command[2])
        cars[car_name]["mileage"] -= distance

        if cars[car_name]["mileage"] <= 10000:
            cars[car_name]["mileage"] = 10000
            continue

        print(f"{car_name} mileage decreased by {distance} kilometers")

for car, value in cars.items():
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
