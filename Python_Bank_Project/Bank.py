import Employee
import Customer
import Account
import Service

class Bank:
    def __init__(self, accounts=set(), employees=set(), customers=set(), services=set()):
        """
        Holds all information about the "virtual bank"

        :param accounts: set of all the account(s) objects
        :param employees: set of all the employee(s) objects
        :param customers: set of all the customer(s) objects
        :param services: set of all the service(s) objects
        """
        self._accounts = accounts
        self._employees = employees
        self._customers = customers
        self._services = services

    def add_employee(self, first_name, last_name, address, salary):
        """
        Adds an employee to the bank

        :param first_name: employee's first name
        :param last_name: employee's last time
        :param address: employee's address
        :param salary: employee's salary
        :return: employee instance created
        """
        new_employee_id = len(self._employees) + 1
        new_employee = Employee.Employee(first_name, last_name, address, new_employee_id, salary)
        self._employees.add(new_employee)
        return new_employee

    def add_customer(self, first_name, last_name, address):
        """
        Adds a customer to the bank

        :param first_name: customer's first name
        :param last_name: customer's last time
        :param address: customer's address
        :return: customer instance created
        """
        new_customer_id = len(self._customers) + 1
        new_customer = Customer.Customer(first_name, last_name, address, new_customer_id)
        self._customers.add(new_customer)
        return new_customer


    def add_account(self, customer_id, account_type="checking"):
        """
        Adds an account to the bank

        :param customer_id: customer's id that is associated with this account
        :param account_type: desired account type (checking, saving)
        :return: account instance created (or none if failed)
        """
        if self._validating_customer_id(customer_id) is not None:
            new_account_id = len(self._accounts) + 1
            new_account = Account.Account(new_account_id, customer_id, account_type)
            self._accounts.add(new_account)
            return new_account
        else:
            return None

    def _validating_customer_id(self, customer_id):
        """
        Checking to see if a customer exsist in the bank

        :param customer_id: customer id that is being checking
        :return: returns customer object if account exsists else, None
        """
        for customer in self._customers:
            if customer.customer_id == customer_id:
                return customer
        return None


    def remove_customer_from_account(self, customer_id, account_id):
        """
        removes customer association from account

        :param customer_id: customer id
        :param account_id: account id
        :return: tre if customer was removed, false if customer was not removed
        """
        account = self._validating_Account_id(account_id)
        customer = self._validating_customer_id(customer_id)
        if account is not None and customer_id is not None and self._validate_minimum_account_users(account):
            if self._validate_minimum_account_users(account):
                account.remove_customer(customer_id)
                customer.remove_account(account_id)
                return True
        return False

    def add_customer_to_account(self, customer_id, account_id ):
        """
        Adds custoemr to account if account id and customer id are valid

        :param customer_id: customer id
        :param account_id: account id
        :return: return true if it exsists, returns false customer was not added to account
        """

        account = self._validating_Account_id(account_id)
        customer = self._validating_customer_id(customer_id)

        if account is not None and customer_id is not None:
            account.add_customer(customer_id)
            customer.add_account(account_id)
            return True
        return False


    def _validating_Account_id(self, account_id):
        """
        Verifies that the account id exsists in bank.

        :param account_id:
        :return: returns account object if account exsists else, None
        """
        for account in self._accounts:
            if account.account_id == account_id:
                return account
        return None


    def _validate_minimum_account_users(self, account):
        """
        verifies if 2 or more customers are associated with an account.

        :param account:
        :return: if there are more than 1 customer associated with an account, returns true
        """
        return len(account.get_customers()) > 1


    def add_service(self, customer_id, service_type="creditcard", interest_rate=.2):
        """
        Adds a service to the bank

        :param customer_id: customer associated with service
        :param service_type: type of service, "creditcard/loan"
        :param interest_rate: interest rate of the service
        :return: returns service object if the service was added to the bank
        """
        if self._validating_customer_id(customer_id):
            new_service_id = len(self._services) + 1
            new_service = Service.Service(new_service_id, customer_id, service_type, interest_rate)
            self._services.add(new_service)
            return new_service
        else:
            return None

    def display_all_employees(self):
        """
        displays all employees in the bank
        """
        print("==Employees==")
        for employee in self._employees:
            print(f"id={employee.employee_id}, {employee.first_name}, {employee.last_name}, ${employee.salary}")

    def display_all_customers(self):
        """
        displays all customers in the bank
        """
        print("==Customers==")
        for customer in self._customers:
            print(f"id={customer.customer_id}, {customer.first_name}, {customer.last_name}")

    def display_all_accounts(self):
        """
        displays all accounts in the bank but also customers associated with the account
        """
        print("==Accounts==")
        for account in self._accounts:
            customers = account.get_customers()
            print(f"id={account.account_id}, account type={account.account_type}, customer associations={len(customers)}")
            self._print_list_of_customer_ids(customers)

    def _print_list_of_customer_ids(self, customer_ids):
        """
        displays all customer ids in the bank
        """
        print(" -> Customer id(s):", end="")
        print(", ".join(str(customer_id) for customer_id in customer_ids))

    def display_all_services(self):
        """
        displays all services in the bank
        """

        print("==Services==")
        for service in self._services:
            customers = service.get_customers()
            print(f"id={service.service_id}, account type={service.service_type}, customer associations={len(customers)}")
            self._print_list_of_customer_ids(customers)

    def save(self):
        pass

    def load(self):
        pass
