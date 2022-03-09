class Account:
    def __init__(self, acct_id, customer_id, balance):
        self.acct_id = acct_id
        self.customer_id = customer_id
        self.balance = balance

    def convert_to_dictionary_acct(self):
        return {
            "acctId": self.acct_id,
            "customerId": self.customer_id,
            "balance": self.balance
        }

    def convert_to_dictionary_acct_id(self):
        return {
            "acctId": self.acct_id
        }

    def convert_to_dictionary_acct_balance(self):
        return {
            "balance": self.balance
        }

    def convert_to_dictionary_cust_id(self):
        return {
            "customerId": self.customer_id
        }

    def convert_to_dictionary_acct_id_and_balance(self):
        return {
            "acctId": self.acct_id,
            "balance": self.balance
        }