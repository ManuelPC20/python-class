class SoftwareEngineer:
    def __init__(self, name, salary_hr, xp, hours):
        self.name = name
        self._salary_hr = salary_hr  # private
        self.xp = xp
        self.hours = hours
        # private int salary; in java
        self._num_bugs_solved = 0  # private

    def code(self):
        self._num_bugs_solved += 1

    def get_salary(self):
        return self._salary_hr * self.hours * 4  # calculate monthly salary

    # setter function for salary
    def set_salary(self, new_salary_hr):
        self._salary_hr = new_salary_hr

    def calculate_bonus(self):
        if self.xp < 8:
            return 0
        elif self.xp > 15:
            return self.get_salary() * 0.03  # 3% bonus
        else:
            return 0  # no bonus

    def calculate_tax(self, total_salary):
        if total_salary <= 50000:
            return 0.05 * total_salary
        elif total_salary > 50000 and total_salary <= 100000:
            return 0.1 * total_salary
        else:
            return 0.15 * total_salary


def employeeCreator():
    name = input('Enter Employee Name: ')
    salary = int(input('Enter salary per hour: '))
    hours_worked = int(input('Enter the number of hours per week: '))
    xp = int(input('Years of experience: '))
    user1 = SoftwareEngineer(name, salary, xp, hours_worked)
    return user1


def SalaryCalculator(n):
    monthly_salary = n.get_salary()
    bonus = n.calculate_bonus()
    total_salary = monthly_salary + bonus
    tax = n.calculate_tax(total_salary)
    net_salary = total_salary - tax
    print(f"{n.name} earns {monthly_salary} per month.")
    if bonus:
        print(f"{n.name} also received a bonus of {bonus:.2f}.")
    print(f"The total salary of {n.name} is {total_salary:.2f} per month.")
    print(f"The tax on {n.name}'s salary is {tax:.2f}.")
    print(f"The net salary of {n.name} is {net_salary:.2f} per month.")


employee = employeeCreator()
SalaryCalculator(employee)