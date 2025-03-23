class Person:
    def __init__(self, first_name, last_name, address):
        """
        Constructor for class Person. class person will be a base class so
        class Customer and Employee can derive from this class

        :param first_name (str): first name of the person
        :param last_name (str): last name of the person
        :param address (str): address for person
        """
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address




