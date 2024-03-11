

class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, job_title, email, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.job_title = job_title.title()
        self.salary = salary
        self.email = email.lower()

        def give_raise(self):
            self.salary = (self.salary * Employee.raise_amount)