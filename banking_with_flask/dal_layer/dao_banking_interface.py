from abc import ABC, abstractmethod


class AccountDAOInterface(ABC):

    # create
    # read
    @abstractmethod
    def create_account(self, acct):
        pass

    @abstractmethod
    def add_customer(self, cust):
        pass

    @abstractmethod
    def create_more_accts_for_a_customer(self, acct):
        pass

    @abstractmethod
    def get_first_account_information_acct_id(self, acct_id):
        pass

    @abstractmethod
    def get_account_number_and_balance_cust_id(self, cust_id):
        pass

    @abstractmethod
    def get_account_information_balance(self, cust_id):
        pass


    # put money in



    # delete
