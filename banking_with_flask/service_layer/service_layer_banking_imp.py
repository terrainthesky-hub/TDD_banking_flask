from abc import abstractmethod
from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo
from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
from banking_with_flask.service_layer.service_layer_banking_interface import BankingServiceInterface
from banking_with_flask.dal_layer.banking_dao_imp import AccountDAOInterface, AccountDAOImp
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.customer import Customer
import re


class ServiceAccessLayer(BankingServiceInterface):
    acct_list = []
    customer_list = []
    acct_id_generator = 1
    customer_id_gen = 1000
    acct_customer_list = []

    def __init__(self, account_dao: AccountDAOInterface):
        self.account_dao: AccountDAOImp = account_dao

    def create_account(self, acct):
        # super().create_account(acct)
        if type(acct.acct_id) != int:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in a integer for your Id")
        elif type(acct.customer_id) != int:  # checking for data type of customer_id
            raise BadAccountInfo("Please pass in a integer for your Id")
        for existing_customer_id in self.account_dao.customer_list:  # loops through customer_list
            if existing_customer_id.customer_id == acct.customer_id:  # checks if the input customer_id matches the looped
                # one in the list, avoiding duplicates
                raise BadAccountInfo("Please pass in different integer for your customer Id")
        acct.acct_id = self.account_dao.acct_id_generator
        acct.customer_id = self.account_dao.customer_id_gen
        self.account_dao.acct_id_generator += 1
        self.account_dao.acct_list.append(acct)
        return acct  # create_account is just here to set up dummy

    # accounts for other methods to check

    def add_customer(self, cust):
        # super().add_customer(cust)
        if type(cust.customer_id) != int:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in a integer for your Id")
        elif type(cust.username) != str:  # checking for data type of customer_id
            raise BadAccountInfo("Please pass in a integer for your Id")
        # for existing_customer_id in self.account_dao.customer_list:  # loops through customer_list
        #     if existing_customer_id.customer_id == cust.customer_id:  # checks if the input customer_id matches the looped
        #         # one in the list, avoiding duplicates
        #         raise BadAccountInfo("Please pass in different integer for your customer Id")
        if len(cust.username) > 20:
            raise BadAccountInfo("username cannot be over 20 characters")
        else:
            cust.customer_id = self.account_dao.customer_id_gen
            self.account_dao.customer_id_gen += 1
            self.account_dao.customer_list.append(cust)
            return cust  # add_customer is just here to set up
        # dummy customers for other methods to check

    def create_more_accts_for_a_customer(self, acct):
        if type(acct.acct_id) != int:  # checking for data type of acct_id
            raise BadAccountInfo("Please pass in a integer for your Id")
        elif type(acct.customer_id) != int:  # checking for data type of customer_id
            raise BadAccountInfo("Please pass in a integer for your Id")
        # acct.customer_id = acct.customer_id - self.customer_id_gen_count
        for existing_customer_id in self.account_dao.customer_list:  # loops through customer_list
            if existing_customer_id.customer_id == acct.customer_id:
                # checks if the input customer_id matches the looped
                acct.acct_id = self.account_dao.acct_id_generator  # assigns acct_id to the number in acct_id_generator
                # acct.customer_id = self.account_dao.customer_id_gen  # assigns customer_id to customer_id_gen
                self.account_dao.acct_id_generator += 1  # increments id_generator after assignment
                self.account_dao.acct_list.append(acct)  # adds the account object to the acct_list
                return acct
            if existing_customer_id == self.account_dao.customer_list[
                -1] and existing_customer_id.customer_id != acct.customer_id:
                raise BadAccountInfo("Sorry, wrong customer_id. Please pass in a valid integer for your Id")


    def update_account_deposit_by_id(self, cust_id, amount):
        # takes an extra parameter to add money)
        regex = '^[0-9]+$'
        if amount == str(amount) and (re.search(regex, cust_id)):
            amount = int(amount)
        if type(amount) != int:
            raise BadAccountInfo("No matches found: " "Try again with the correct information")
        if type(amount) == int:
            if cust_id == str(cust_id) and (re.search(regex, cust_id)):
                cust_id = int(cust_id)
            if type(cust_id) != int:
                raise BadAccountInfo("No matches found: " "Try again with the correct information")
            if type(cust_id) == int:
                for customer in self.account_dao.customer_list:
                    if customer.customer_id == cust_id:
                        for account in self.account_dao.acct_list:
                            if customer.customer_id == account.customer_id:
                                account.balance += amount  # adds money to acct.balance
                                return account.convert_to_dictionary_acct_balance()  # returns new input's acct.balance
                            if account == self.account_dao.acct_list[-1] and customer.customer_id != account.customer_id:
                                raise BadAccountInfo("Customer Id not found")
                    if customer == self.account_dao.customer_list[-1] and customer.customer_id != cust_id:
                        raise BadAccountInfo("Customer Id not found")

    def update_account_withdraw_by_id(self, cust_id, amount):
        new = cust_id
        regex = '^[0-9]+$'
        if amount == str(amount) and (re.search(regex, cust_id)):
            amount = int(amount)
        if type(amount) != int:
            raise BadAccountInfo("No matches found: " "Try again with the correct information")
        if type(amount) == int:
            if cust_id == str(cust_id) and (re.search(regex, cust_id)):
                cust_id = int(cust_id)
            if type(cust_id) != int:
                raise BadAccountInfo("No matches found: " "Try again with the correct information")
            if type(cust_id) == int:
                for customer in self.account_dao.customer_list:
                    if customer.customer_id == cust_id:
                        new = customer
                        break
                    if customer == self.account_dao.customer_list[-1] and customer.customer_id != cust_id:
                        raise BadAccountInfo("Customer Id not found")
                    if len(self.account_dao.customer_list) == 0:
                        raise BadAccountInfo("Customer Id not found")
                for account in self.account_dao.acct_list:
                    if new.customer_id == account.customer_id:
                        if account.balance >= amount:  # checks if there's more
                            # money in the input balance than can be removed
                            account.balance = account.balance - amount  # subtracts amount
                            # from input.balance
                            return account.convert_to_dictionary_acct_balance()
                        else:
                            raise BadAccountInfo("Not enough funds to withdraw this amount")
                    if account == self.account_dao.acct_list[-1] and customer.customer_id != account.customer_id:
                        raise BadAccountInfo("No matches found: " "Try again with the correct information")
                    if len(self.account_dao.acct_list) == 0:
                        raise BadAccountInfo("Customer Id not found")


    def delete_account_by_id(self, cust_id):
        new_cust = cust_id
        regex = '^[0-9]+$'
        if cust_id == str(cust_id) and (re.search(regex, cust_id)):
            cust_id = int(cust_id)
        if type(cust_id) != int:
            raise BadAccountInfo("Please provide a valid customer Id as an integer")
        if type(cust_id) == int:
            for customer in self.account_dao.customer_list:
                if customer.customer_id == cust_id:
                    new_cust = customer
                    break
                if customer == self.account_dao.customer_list[-1] and customer.customer_id != cust_id:
                    raise BadAccountInfo("Customer Id not found")
                # if len(self.account_dao.customer_list) == 0:
                #     raise BadAccountInfo("Customer Id not found")
            for i1, account in enumerate(self.account_dao.acct_list):
                if new_cust.customer_id == account.customer_id:
                    self.account_dao.acct_list.pop(i1)
                    return {"Sorry to lose your business": "Account removed"}
                if account == self.account_dao.acct_list[-1] and new_cust.customer_id != account.customer_id:
                    raise BadAccountInfo("No matches found: " "Try again with the correct information")

    def delete_account_and_customer_by_id(self, cust_id):
        new_cust = cust_id
        indexing = cust_id
        regex = '^[0-9]+$'
        if cust_id == str(cust_id) and (re.search(regex, cust_id)):
            cust_id = int(cust_id)
        if type(cust_id) != int:
            raise BadAccountInfo("Please provide a valid customer Id as an integer")
        if type(cust_id) == int:
            for i1, customer in enumerate(self.account_dao.customer_list):
                if customer.customer_id == cust_id:
                    new_cust = i1
                    self.account_dao.customer_list.pop(i1)
                    break
                if customer == self.account_dao.customer_list[-1] and customer.customer_id != cust_id:
                    raise BadAccountInfo("Customer Id not found")
            for i2, account in enumerate(self.account_dao.acct_list):
                if account.customer_id == cust_id:
                    self.account_dao.acct_list.pop(i2)
                    return {"Sorry to lose your business": "Account removed"}
                if account == self.account_dao.acct_list[-1] and account.customer_id != cust_id:
                    raise BadAccountInfo("No matches found: " "Try again with the correct information")

    def transfer_money_between_accounts_from_acct1_to_acct2(self, withdraw_acct, deposit_acct, amount):
        regex = '^[0-9]+$'
        if amount == str(amount) and (re.search(regex, amount)):
            amount = int(amount)
        if type(amount) != int:
            raise BadAccountInfo("Please provide a valid customer Id as an integer")
        if type(amount) == int:
            for customer in self.account_dao.customer_list:
                if customer.customer_id == withdraw_acct.customer_id:  # and deposit_acct.customer_id:
                    if withdraw_acct.balance - amount < 0:
                        raise BadAccountInfo("You do not have enough money to withdraw")
                if customer == self.account_dao.customer_list[-1] and customer.customer_id != withdraw_acct.customer_id:
                    raise BadAccountInfo("Customer Id not found")
            withdraw_acct.balance = withdraw_acct.balance - amount
            for account in self.account_dao.customer_list:
                if account.customer_id == deposit_acct.customer_id:
                    deposit_acct.balance = deposit_acct.balance + amount
            return [withdraw_acct.convert_to_dictionary_acct_balance(),
                    deposit_acct.convert_to_dictionary_acct_balance()]
