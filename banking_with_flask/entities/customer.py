class Customer:
    def __init__(self, username, customer_id):
        self.username = username
        self.customer_id = customer_id

    def convert_to_dictionary_cust(self):
        return {
            "username": self.username,
            "customerId": self.customer_id,
        }