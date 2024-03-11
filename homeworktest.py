

class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, job_title, email, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.job_title = job_title.title()
        self.salary = salary
        self.email = email.lower()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

    def give_raise(self):
        self.salary = (self.salary * Employee.raise_amount)
        print(f"Good job {self.first_name}! You've earned a raise! Your new salary is {self.salary}.")

e =(Employee("john", "doe", "developer", "somethingrandom@gmail.com", 52000))

e.give_raise()