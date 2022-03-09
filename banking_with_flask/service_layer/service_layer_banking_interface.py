from abc import ABC, abstractmethod
from banking_with_flask.entities.customer import Customer
from banking_with_flask.entities.account import Account

class BankingServiceInterface(ABC):

    @abstractmethod
    def create_account(self, acct): #
        pass

    @abstractmethod
    def add_customer(self, cust): #
        pass

    # @abstractmethod
    # def create_more_accts_for_a_customer(self, acct):
    #     pass

    @abstractmethod
    def update_account_deposit_by_id(self, cust_id, amount):
        pass


    @abstractmethod
    def update_account_withdraw_by_id(self, cust_id, amount):
        pass

    @abstractmethod
    def delete_account_by_id(self, cust_id):
        pass

    @abstractmethod
    def transfer_money_between_accounts_from_acct1_to_acct2(self, withdraw_acct, deposit_acct, amount):
        pass