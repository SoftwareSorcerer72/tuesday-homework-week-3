

class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, job_title, email, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.job_title = job_title.title()
        self.salary = salary
        self.email = email.lower()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def give_raise(self):
        self.salary = round(self.salary * Employee.raise_amount)
        print(f"Good job {self.first_name}! You've earned a raise! Your new salary is {self.salary}")



class Sales(Employee):
    def __init__(self, first_name, last_name, job_title, email, salary, phone_number):
        super().__init__(first_name, last_name, job_title, email, salary)
        self.phone_number = phone_number

    def send_followup_email(self, customer_name):
        print(f"\tDear {customer_name}, \nThank you for your interest in our product. Please let me know if you have any questions. My email is {self.email} and my phone number is {self.phone_number}. \n\n Thanks, \n {self}")

class Developer(Employee):
    def write_code(self):
        print(f"{self} is writing code!")



sales_employee = Sales('Jane', 'Doe', 'Sales', 'anotheremail@gmail.com', 50000, '(123) 456-7890')

sales_employee.send_followup_email("Mike O'Neil")

sales_employee = Sales('Jane', 'Doe', 'Sales', 'anotheremail@gmail.com', 50000, '(123) 456-7890')

sales_employee.send_followup_email("Hannah Stern")

sales_employee.give_raise()

developer_employee = Developer('James', 'Doe Jr.', 'Software Developer','james.doe@gmail.com', 100000) 

developer_employee.write_code()

developer_employee.give_raise()