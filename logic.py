account_cache = {}

def luhn_validation(number):
    # validate the credit card numbers using luhn's algorithm
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    
    return True if checksum % 10 == 0 else False


def debit(username, amount):
    # get user account
    if account_cache.get(username):
        account_cache[username]['account_balance'] = account_cache[username]['account_balance'] - amount
    else:
        print(f"Account with name {username} does not exist")

def credit(username, amount):
    # get user account
    if account_cache.get(username):
        account_cache[username]['account_balance'] = account_cache[username]['account_balance'] + amount
    else:
        print(f"Account with name {username} does not exist")

def add_new_account(username, amount, cc_num):
    # validate account number here using Luhn 10 algorithm
    is_valid = luhn_validation(cc_num)
    if is_valid:
        # add username and account number to amount
        account_cache[username] = {"account_balance": amount, "account_num": cc_num}
    else:
        print(f"The account number {cc_num} is invalid")





def process(command, username, amount, credit_card_no=None):
    """ This function processes each logic and stores it for later"""
    amount = int(amount.split('$')[-1])
    print(amount)
    actions = {
        'Charge': credit(username, amount),
        'Credit': debit(username, amount),
        'Add': add_new_account(username, amount, credit_card_no)
    }

    # if credit_card_no: # then it is a new user addition
    #     func = actions[command]
    # else: # then it is either a charge or credit
    #     pass

    result = actions[command]

