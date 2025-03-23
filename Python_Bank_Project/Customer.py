import Person

class Customer(Person.Person):
    def __init__(self, first_name, last_name, address, customer_id):
        """
        This class represents a customer and is a sub class of class Person.

        :param customer_id (int): this paramter should be auto generated during creation
        :param accounts list(): a set of accounts that the customer is associated with (default is null set)
        """
        super().__init__(first_name, last_name, address)
        self._customer_id = customer_id
        self._accounts = set()

    @property
    def customer_id(self):
        return self._customer_id
    @property
    def accounts(self):
        return self._accounts

    def add_account(self, account_id):
        self._accounts.add(account_id)

    def remove_account(self,account_id):
        self._accounts.discard(account_id)


