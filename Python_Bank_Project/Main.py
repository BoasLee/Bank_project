import Bank

my_bank = Bank.Bank()
my_bank.add_employee("boas","lee", "123", 200)
my_bank.add_customer("abc","abc", "123")
my_bank.add_account(1)
my_bank.add_service(1)

my_bank.display_all_customers()
my_bank.display_all_employees()
my_bank.display_all_accounts()
my_bank.display_all_services()