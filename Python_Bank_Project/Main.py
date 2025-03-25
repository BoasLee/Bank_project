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
    :return: returns newly created customer object
    """
    print("--Creating Customer--")
    first_name = input("First Name: ")
    last_name = input("Last Name:")
    address = input("Address:")
    new_customer = bank.add_customer(first_name, last_name, address)
    print("--Customer Created--")
    return new_customer


def create_account(bank):
    """
    Asks user for desired account type and creates an account based on the input.

    :param bank: bank object that holds all the information.
    : return: instance of newly created account
    """
    print("--Creating Account--")
    customer_id = int(input("customer_id: "))
    account_type = input('For Savings account, enter "s" or the account will default to checking: ')
    if account_type == 's':
        new_account = bank.add_account(customer_id,"savings")
    else:
        new_account = bank.add_account(customer_id)

    if new_account:
        print("--Account Created--")
    else:
        print("--Account NOT Created--")

    return new_account


def create_service(bank):
    """
    Asks user for account type and creates account based on the input.

    :param bank: bank object that holds all the information.
    """
    print("--Creating Service--")
    customer_id = int(input("customer_id: "))
    service_type = input('For a loan, enter "l" or the service will default to a creditcard: ')
    if service_type == 'l':
        new_service = bank.add_account(customer_id, "loan")
    else:
        new_service = bank.add_account(customer_id)

    if new_service:
        print("--Service Created--")
    else:
        print("--Service NOT Created--")
    return new_service


def create_employee(bank):
    """
    Asks user for first name, last name, addresss, and employee based on the input.

    :param bank: bank object that holds all the information.
    :return: employee object
    """
    print("--Creating Employee--")
    first_name = input("First Name: ")
    last_name = input("Last Name:")
    address = input("Address:")
    salary = int(input("salary:"))
    new_employee = bank.add_employee(first_name, last_name, address, salary)
    print("--Employee Created--")
    return new_employee


def add_customer_to_account(bank):
    """
    Asks user for customer id and account id. If customer id and account id are valid, customer is added to the account.

    :param bank: bank object that holds all the information.
    :return: returns true if the customer was added to the account
    """
    print("--Adding Customer to Account--")
    customer_id = int(input("customer_id: "))
    account_id = int(input("account_id: "))
    result = bank.add_customer_to_account(customer_id, account_id)
    if result:
        print("--Customer added to Account--")
    else:
        print("--Customer was NOT added to Account--")
    return result


def remove_customer_from_account(bank):
    """
    Asks user for customer id and account id. If customer id and account id are valid, customer is removed from account.

    :param bank: bank object that holds all the information.
    :return: returnst true if the customer was removed from account
    """
    print("--Removing Customer from Account--")
    customer_id = int(input("customer_id: "))
    account_id = int(input("account_id: "))
    result = bank.remove_customer_from_account(customer_id, account_id)
    if result:
        print("--Customer was removed from Account--")
    else:
        print("--Customer was NOT removed from Account--")
    return result


if __name__ == "__main__":
    my_bank = Bank.Bank()
    user_input = None

with open("Log.txt", "a") as file:
    while user_input != 0:
        display_main_menu()
        user_input = int(input("Please choose one of the following options:"))
        match user_input:
            case 1:
                if create_customer(my_bank) is not None:
                    file.write("customer was created\n")
                else:
                    file.write("customer was NOT created\n")
            case 2:
                if create_account(my_bank) is not None:
                    file.write("account was created\n")
                else:
                    file.write("account was NOT created\n")
            case 3:
                if create_service(my_bank) is not None:
                    file.write("service was created\n")
                else:
                    file.write("service was NOT created\n")
            case 4:
                if create_employee(my_bank) is not None:
                    file.write("employee was created\n")
                else:
                    file.write("employee was NOT created\n")
            case 5:
                if add_customer_to_account(my_bank):
                    file.write("customer was added to account\n")
                else:
                    file.write("customer was NOT added to account\n")
            case 6:
                if remove_customer_from_account(my_bank):
                    file.write("customer was removed form account\n")
                else:
                    file.write("customer was NOT removed from account\n")
            case 7:
                display_everything(my_bank)
            case 0:
                pass
            case _:
                print(f"invlaid input {user_input} entered")
        print()




