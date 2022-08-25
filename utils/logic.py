
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

def sort_line(line, db):
    line = line.split(" ")
    command = line[0]
    username = line[1]
    # get the amount from the input statement, convert to int, exclude the dollar sign
    amount = int(line[-1].strip("\n").split('$')[-1])

    if command == 'Add':
        credit_card_no = line[2]
        db.add_new_account(username, amount, credit_card_no)
    elif command == 'Charge':
        db.make_charge_transaction(username, amount)
    else:
        db.make_credit_transaction(username, amount)
    