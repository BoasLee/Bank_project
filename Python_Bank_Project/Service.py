class Service:
    def __init__(self, service_id, customer_id, service_type, interest_rate):
        """
        Represents a service for a customer

        :param service_id: service unique identifier
        :param customer_id: customer associated with service
        :param service_type: description/type of service
        :param interest_rate: interest rate for the service
        """

        self._service_id = service_id
        self._service_type = service_type
        self._customers = set()
        self._interest_rate = interest_rate
        self._balance = 0

        self._add_customer(customer_id)

    def add_customer(self, customer_id):
        self._customers.add(customer_id)

    def get_customers(self):
        return self._customers

    @property
    def balance(self):
        return self._balance

    @property
    def service_id(self):
        return self._service_id

    @property
    def service_type(self):
        return self._service_type

    def make_payment(self, amount):
        self._balance += amount

    def re_calcualte_pricincle(self):
        self._balance *= 1 + self._interest_rate
