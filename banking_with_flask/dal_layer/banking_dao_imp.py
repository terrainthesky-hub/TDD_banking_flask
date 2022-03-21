from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo
from banking_with_flask.dal_layer.dao_banking_interface import AccountDAOInterface
from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.customer import Customer
import re
import json


class AccountDAOImp(AccountDAOInterface):
    # username = "terra"

    # for account in acct_list:
    #     if account.acc_id == account_id: return it
    # acct_list = []
    # customer_list = []
    # acct_id_generator = 1
    # customer_id_gen = 1000
    # acct_customer_list = []

    def __init__(self):
        self.acct_list = []
        self.acct_multiple_lists = []
        self.customer_list = []
        self.acct_id_generator = 1
        self.customer_id_gen = 1000
        self.acct_customer_list = []
        self.customer_name_list = []

    def create_account(self, acct):
        if isinstance(acct, bool) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(acct, Account) != True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(acct.acct_id, int) != True:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in an integer for your Id")
        elif isinstance(acct.customer_id, int) != True:  # checking for data type of customer_id
            raise BadAccountInfo("Please pass in an integer for your Id")
        acct.acct_id = self.acct_id_generator  # assigns acct_id to the number in acct_id_generator
        acct.customer_id = self.customer_id_gen  # assigns customer_id to customer_id_gen
        self.acct_id_generator += 1  # increments id_generator after assignment
        self.acct_list.append(acct)  # adds the account object to the acct_list
        return acct

    def add_customer(self, cust):
        if isinstance(cust, bool) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(cust, Customer) != True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if type(cust.username) != str:
            raise BadAccountInfo("Please use a string (letters and words)")
        if type(cust.customer_id) != int:
            raise BadAccountInfo("Please enter in a valid integer for your ID")
        if len(cust.username) > 20:  # username can't be over 20 characters
            print("username cannot be over 20 characters")
        # else:
        #     # for existing_customer_id in self.customer_name_list:  # looping through customer_list
        #     #     if existing_customer_id.customer_id == cust.customer_id:  # checking if there's duplicates
        #     #         raise BadAccountInfo("Please pass in a different integer for your Id")
        #         # if existing_customer_id.username in self.customer_name_list:  # checks for duplicate usernames in customer_list
        #         #     raise BadAccountInfo("Please pass in a different username")
        #     # self.customer_name_list.append(cust.username)
        cust.customer_id = self.customer_id_gen  # sets the new customer_id of the input parameter
        self.customer_id_gen += 1  # increments customer_id_generator
        self.customer_list.append(cust)  # adds customer object to customer_list with a modified customer_id
        return cust

    def create_more_accts_for_a_customer(self, acct):
        if isinstance(acct, bool) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(acct, Account) != True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(acct.acct_id, int) != True:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in an integer for your Id")
        elif isinstance(acct.customer_id, int) != True:  # checking for data type of customer_id
            raise BadAccountInfo("Please pass in an integer for your Id")
        elif isinstance(acct.balance, int) != True:
            raise BadAccountInfo("Please pass in an integer for your balance")
        for existing_customer_id in self.customer_list:  # loops through customer_list
            if existing_customer_id.customer_id == acct.customer_id:  # checks if the input customer_id matches the looped
                new = self.acct_id_generator
                self.acct_id_generator += 1
                new_acct = Account(new, acct.customer_id, acct.balance)
                self.acct_list.append(new_acct)
                # assigns customer_id to customer_id_gen
                # increments id_generator after assignment
                # adds the new acct_id account object to the acct_list
                return new_acct.convert_to_dictionary_acct()
            elif existing_customer_id not in self.customer_list:
                raise IdNotFound("Please pass in an integer for your account and customer Id")


    def get_first_account_information_acct_id(self, acct_id):
        # for customer in self.customer_list:
        # if type(acct) != object:
        #     raise BadAccountInfo("Please pass in an integer for your Id")
        regex = '^[0-9]+$'
        if acct_id == str(acct_id) and (re.search(regex, acct_id)):
            acct_id = int(acct_id)
        if isinstance(acct_id, bool) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(acct_id, Account) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(acct_id, int) != True:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in an integer for your Id")
        for customer in self.customer_list:
            if customer.customer_id == acct_id:
                for account in self.acct_list:
                    if account.customer_id == customer.customer_id:
                        return account.convert_to_dictionary_acct_id()  # return account acct_id balance



    def get_account_number_and_balance_cust_id(self, cust_id):
        try:
            # if type(cust_id) == object:
            #     raise BadAccountInfo("Please pass in an integer for your Id")
            regex = '^[0-9]+$'
            new_cust = cust_id
            if cust_id == str(cust_id) and (re.search(regex, cust_id)):
                cust_id = int(cust_id)
            if type(cust_id) != int:
                raise BadAccountInfo("Please provide a valid customer Id as an integer")
            if isinstance(cust_id, bool) == True:
                raise BadAccountInfo("Please pass in an integer for your Id")
            if isinstance(cust_id, Customer) == True:
                raise BadAccountInfo("Please pass in an integer for your Id")
            if type(cust_id) == int:
                for customer in self.customer_list:  # loops through customer_list
                    if customer.customer_id == cust_id:
                        new_cust = customer
                        break
                    if customer.customer_id != cust_id and customer == self.customer_list[-1]:
                        raise BadAccountInfo("Please enter in a valid customer Id")
                for account in self.acct_list:  # checks if customer customer_id equals the acct customer_id
                    if new_cust.customer_id == account.customer_id:
                        self.acct_customer_list.append(account)
                    if account == self.acct_list[-1] and new_cust.customer_id != account.customer_id:
                        raise BadAccountInfo("Account not found")
                for acct_cust_balance in self.acct_customer_list:
                    self.acct_multiple_lists.append(acct_cust_balance.convert_to_dictionary_acct())
                # for json_accts in self.acct_multiple_lists:
                return self.acct_multiple_lists
        finally:
            self.acct_customer_list = []
            self.acct_multiple_lists = []

    def get_account_information_balance(self, cust_id):
        # if type(cust_id) == object:
        #     raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(cust_id, bool) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(cust_id, Customer) == True:
            raise BadAccountInfo("Please pass in an integer for your Id")
        new_cust = cust_id
        regex = '^[0-9]+$'
        if cust_id == str(cust_id) and (re.search(regex, cust_id)):
            cust_id = int(cust_id)
        if isinstance(cust_id, int) != True:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in an integer for your Id")
        if isinstance(cust_id, int) == True:
            for customer in self.customer_list:  # loops through customer_list
                new_cust = customer
                if customer.customer_id == cust_id:
                    break
                if new_cust == self.customer_list[-1] and customer.customer_id != cust_id:
                    raise BadAccountInfo("Customer Id not found")
            for account in self.acct_list:
                if new_cust.customer_id == account.customer_id:
                    return account.convert_to_dictionary_acct_balance()
                if account == self.acct_list[-1] and new_cust.customer_id != account.customer_id:
                    raise BadAccountInfo("Account not found")