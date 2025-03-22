import Person

class Employee(Person.Person):
    def __init__(self, first_name, last_name, address, employee_id, salary = None):
        """
        This class represents an Employee and is a sub class of class Person.

        :param employee_id (int): this paramter should be auto generated during creation
        :param salary (int): salary of employee
        """
        super().__init__(first_name, last_name, address)
        self._employee_id = employee_id
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id
    @property
    def salary(self):
        return  self._salary