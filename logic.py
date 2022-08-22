account_cache = {}

def luhn_validation(number):
    # validate the credit card numbers using luhn's algorithm
    print(number)
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
    account_cache = {}
    # get user account
    if account_cache.get(username):
        account_cache[username]['account_balance'] = account_cache[username]['account_balance'] - amount
    # else:
    #     print(f"1 Account with name {username} does not exist")
    return account_cache
   

def credit(username, amount):
    account_cache = {}
    # get user account
    if account_cache.get(username):
        account_cache[username]['account_balance'] = account_cache[username]['account_balance'] + amount
    # else:
    #     print(f"2 Account with name {username} does not exist")
    return account_cache

def add_new_account(username, amount, cc_num):
    account_cache = {}
    # validate account number here using Luhn 10 algorithm
    is_valid = luhn_validation(cc_num)
    if is_valid:
        # add username and account number to amount
        account_cache[username] = {"account_balance": amount, "account_num": cc_num}
    else:
        print(f"The account number {cc_num} is invalid")
    return account_cache




def process(command, username, amount, credit_card_no=None):
    """ This function processes each logic and stores it for later"""
    amount = int(amount.split('$')[-1])
    actions = {
        'Charge': credit(username, amount),
        'Credit': debit(username, amount),
        'Add': add_new_account(username, amount, credit_card_no)
    }
    if command:
        return actions[command]

    # if credit_card_no: # then it is a new user addition
    #     func = actions[command]
    # else: # then it is either a charge or credit
    #     pass

    # result = actions[command]
    # print(account_cache)
    # return account_cache

