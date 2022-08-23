from utils.logic import luhn_validation


class AccountDB():
    def __init__(self):
        self._db = {}
        self.error = "error"

    def get_account(self, key):
        pass
    
    def add_new_account(self, account_details):
        pass

    def validate_acc_number(self, number):
        is_valid = luhn_validation(number)
        return is_valid

    def validate_acc_exists(self, acc_name):
        pass

    def validate_acc_limit(self, acc_name):
        pass
    
    def make_debit_transaction(self, account_details):
        pass

    def make_credit_transaction(self, account_details):
        pass

    def generate_account_statement(self):
        pass