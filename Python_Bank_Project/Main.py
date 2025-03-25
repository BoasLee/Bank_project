import Bank


def display_everything(bank):
    """
    Displays all customers, employees, accounts, and services

    :param bank: bank object that holds all the information.
    """
    bank.display_all_customers()
    bank.display_all_employees()
    bank.display_all_accounts()
    bank.display_all_services()


def display_main_menu():
    """
    Displays menu option for user
    """
    print("""(1) Create a customer
(2) Create an account
(3) Create a service
(4) Create a new employee
(5) Add Customer to Account
(6) Remove Customer from Account
(7) Display Everything
(0) Quit """)


def create_customer(bank):
    """
    Asks user for first name, last name, addresss, and creates customer based on the input.

    :param bank: bank object that holds all the information.
    """
    print("--Creating Customer--")
    first_name = input("First Name: ")
    last_name = input("Last Name:")
    address = input("Address:")
    bank.add_customer(first_name, last_name, address)
    print("--Customer Created--")


def create_account(bank):
    """
    Asks user for desired account type and creates an account based on the input.

    :param bank: bank object that holds all the information.
    """
    print("--Creating Account--")
    customer_id = int(input("customer_id: "))
    account_type = input('For Savings account, enter "s" or the account will default to checking: ')
    if account_type == 's':
        result = bank.add_account(customer_id,"savings")
    else:
        result = bank.add_account(customer_id)

    if result:
        print("--Account Created--")
    else:
        print("--Account NOT Created--")


def create_service(bank):
    """
    Asks user for account type and creates account based on the input.

    :param bank: bank object that holds all the information.
    """
    print("--Creating Service--")
    customer_id = int(input("customer_id: "))
    account_type = input('For a loan, enter "l" or the service will default to a creditcard: ')
    if account_type == 'l':
        result = bank.add_account(customer_id, "loan")
    else:
        result = bank.add_account(customer_id)

    if result:
        print("--Service Created--")
    else:
        print("--Service NOT Created--")


def create_employee(bank):
    """
    Asks user for first name, last name, addresss, and employee based on the input.

    :param bank: bank object that holds all the information.
    """
    print("--Creating Employee--")
    first_name = input("First Name: ")
    last_name = input("Last Name:")
    address = input("Address:")
    salary = int(input("Address:"))
    bank.add_employee(first_name, last_name, address, salary)
    print("--Employee Created--")


def add_customer_to_account(bank):
    """
    Asks user for customer id and account id. If customer id and account id are valid, customer is added to the account.

    :param bank: bank object that holds all the information.
    """
    print("--Adding Customer to Account--")
    customer_id = int(input("customer_id: "))
    account_id = int(input("account_id: "))
    if bank.add_customer_to_account(customer_id, account_id):
        print("--Customer added to Account--")
    else:
        print("--Customer was NOT added to Account--")


def remove_customer_from_account(bank):
    """
    Asks user for customer id and account id. If customer id and account id are valid, customer is removed from account.

    :param bank: bank object that holds all the information.
    """
    print("--Removing Customer from Account--")
    customer_id = int(input("customer_id: "))
    account_id = int(input("account_id: "))
    if bank.remove_customer_from_account(customer_id, account_id):
        print("--Customer was removed from Account--")
    else:
        print("--Customer was NOT removed from Account--")


if __name__ == "__main__":
    my_bank = Bank.Bank()
    user_input = None

    while user_input != 0:
        display_main_menu()
        user_input = int(input("Please choose one of the following options:"))
        match user_input:
            case 1:
                create_customer(my_bank)
            case 2:
                create_account(my_bank)
            case 3:
                create_service(my_bank)
            case 4:
                create_employee(my_bank)
            case 5:
                add_customer_to_account(my_bank)
            case 6:
                remove_customer_from_account(my_bank)
            case 7:
                display_everything(my_bank)
            case 0:
                pass
            case _:
                print("invlaid input entered")
        print()




