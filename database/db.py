from utils.logic import luhn_validation


class AccountDB():
    def __init__(self):
        self._db = {}
        self.error = "error"
        self.limit = 0

    def get_account(self, key):
        return self._db.get(key, None)
    
    def add_new_account(self, username, limit, credit_card_no):
        """ Creates a new credit card for a given name, card number, and limit,
        invalid cards get balance of 'error', else balance is set to $0 """
        account_num_valid = self.validate_acc_number(credit_card_no)
        username = username.capitalize()
        if account_num_valid:
            self._db[username] = {"balance":0, 
                                    "limit":limit,
                                    "name": username,
                                    "card_number": credit_card_no}
        else:
            self._db[username] = {"balance":self.error, 
                                    "limit":self.limit,
                                    "name": username,
                                    "card_number": credit_card_no}

    def validate_acc_number(self, number):
        """ validates that a credit card number follows luhn's algorithm """
        is_valid = luhn_validation(number)
        return is_valid

    def validate_balance(self, balance):
        return True if type(balance) == int else False


    def validate_acc_limit(self, key, amount):
        """ Validates that a new charge transaction does not exceed account limit """
        limit = self._db.get(key)["limit"]
        balance = self._db.get(key)["balance"]

        #check that balance is valid
        is_balance_valid = self.validate_balance(balance)
        if is_balance_valid:
            if (amount + balance) <= limit:
                return True
        return False
    
    def make_charge_transaction(self, name, amount):
        """ Adds money to an account, ignore if it raises above limit, ignore if card is invalid """
        account = self.get_account(name)
        if account:
            balance = account["balance"]
            #check that balance is valid
            is_balance_valid = self.validate_balance(balance)
            if is_balance_valid:
                is_charge_valid = self.validate_acc_limit(name, amount)
                if is_charge_valid:
                    account["balance"] = balance + amount

    def make_credit_transaction(self, name, amount):
        """ Removes money from an account, balance can be negative, ignore if card is invalid """
        account = self.get_account(name)
        if account:
            balance = account["balance"]
            # check that balance is valid
            is_balance_valid = self.validate_balance(balance)
            if is_balance_valid:
                account["balance"] = balance - amount


    def generate_account_statement(self):
        ordered_db = dict(sorted(self._db.items()))
        for account in ordered_db:
            print(account)
            print(f'{account["name"]}:${account["balance"]}')
