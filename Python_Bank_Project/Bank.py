import Employee
import Customer
import Account
import Service

class Bank:
    def __init__(self, accounts=set(), employees=set(), customers=set(), services=set()):
        self._accounts = accounts
        self._employees = employees
        self._customers = customers
        self._services = services

    def add_employee(self, first_name, last_name, address, salary):
        new_employee_id = len(self._employees) + 1
        new_employee = Employee.Employee(first_name, last_name, address, new_employee_id, salary)
        self._employees.add(new_employee)

    def add_customer(self, first_name, last_name, address):
        new_customer_id = len(self._customers) + 1
        new_customer = Customer.Customer(first_name, last_name, address, new_customer_id)
        self._customers.add(new_customer)

    def add_account(self, customer_id, account_type="checking"):
        if self._validating_customer_id(customer_id) is not None:
            new_account_id = len(self._accounts) + 1
            new_account = Account.Account(new_account_id, customer_id, account_type)
            self._accounts.add(new_account)
            return True
        else:
            return False

    def _validating_customer_id(self, customer_id):
        for customer in self._customers:
            if customer.customer_id == customer_id:
                return customer
        return None


    def remove_customer_from_account(self, customer_id, account_id):
        account = self._validating_Account_id(account_id)
        customer = self._validating_customer_id(customer_id)
        if account is not None and customer_id is not None and self._validate_minimum_account_users(account):
            if self._validate_minimum_account_users(account):
                account.remove_customer(customer_id)
                customer.remove_account(account_id)
                return True
        return False

    def add_customer_to_account(self, customer_id, account_id ):
        account = self._validating_Account_id(account_id)
        customer = self._validating_customer_id(customer_id)

        if account is not None and customer_id is not None:
            account.add_customer(customer_id)
            customer.add_account(account_id)
            return True
        return False


    def _validating_Account_id(self, account_id):
        for account in self._accounts:
            if account.account_id == account_id:
                return account
        return None


    def _validate_minimum_account_users(self, account):
        return len(account.get_customers()) > 1


    def add_service(self, customer_id, service_type="creditcard", interest_rate=.2):
        if self._validating_customer_id(customer_id):
            new_service_id = len(self._services) + 1
            new_service = Service.Service(new_service_id, customer_id, service_type, interest_rate)
            self._services.add(new_service)
            return True
        else:
            return False

    def display_all_employees(self):
        print("==Employees==")
        for employee in self._employees:
            print(f"id={employee.employee_id}, {employee.first_name}, {employee.last_name}, ${employee.salary}")

    def display_all_customers(self):
        print("==Customers==")
        for customer in self._customers:
            print(f"id={customer.customer_id}, {customer.first_name}, {customer.last_name}")

    def display_all_accounts(self):
        print("==Accounts==")
        for account in self._accounts:
            customers = account.get_customers()
            print(f"id={account.account_id}, account type={account.account_type}, customer associations={len(customers)}")
            self._print_list_of_customer_ids(customers)

    def _print_list_of_customer_ids(self, customer_ids):
        print(" -> Customer id(s):", end="")
        print(", ".join(str(customer_id) for customer_id in customer_ids))

    def display_all_services(self):
        print("==Services==")
        for service in self._services:
            customers = service.get_customers()
            print(f"id={service.service_id}, account type={service.service_type}, customer associations={len(customers)}")
            self._print_list_of_customer_ids(customers)

    def save(self):
        pass

    def load(self):
        pass
