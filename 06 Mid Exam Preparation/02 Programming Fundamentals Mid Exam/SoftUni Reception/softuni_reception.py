emp1Eff = int(input())
emp2Eff = int(input())
emp3Eff = int(input())
people = int(input())
needed_hours = 0
answer_per_hour = emp1Eff + emp2Eff + emp3Eff
while people > 0:
    people -= answer_per_hour
    needed_hours += 1
    if needed_hours % 4 == 0:
        needed_hours += 1
        continue

print(f"Time needed: {needed_hours}h.")