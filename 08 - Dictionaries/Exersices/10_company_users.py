company_info = {}

company_employee = input()
while company_employee != "End":
    company_employee = company_employee.split(" -> ")
    company, employee = company_employee[0], company_employee[1]

    company_info[company] = company_info.get(company, [])
    if employee not in company_info[company]:
        company_info[company].append(employee)

    company_employee = input()

for key in company_info:
    print(key)
    [print(f"-- {employee}") for employee in company_info[key]]
