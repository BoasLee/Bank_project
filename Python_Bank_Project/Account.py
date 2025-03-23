class Account:
    def __init__(self, account_id, customer_id, account_type):
        self._account_id = account_id
        self._account_type = account_type
        self._customers = set()
        self._balance = 0

        self._customers.add(customer_id)

    def get_customers(self):
        return self._customers

    @property
    def balance(self):
        return self._balance

    @property
    def account_id(self):
        return self._account_id

    @property
    def account_type(self):
        return self._account_type

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            return None
        else:
            self._balance -= amount
