import sys
from database.db import AccountDB

def sort_line(line, db):
    line = line.split(" ")
    command = line[0]
    username = line[1]
    amount = int(line[-1].split('$')[-1])

    if command == 'Add':
        credit_card_no = line[2]
        db.add_new_account(username, amount, credit_card_no)
    elif command == 'Charge':
        db.make_charge_transaction(username, amount)
    else:
        db.make_credit_transaction(username, amount)
    


def read_direct_input(s_input):
    db =  AccountDB()
    # if direct input
    for line in s_input:
        sort_line(line, db)
    print(db.generate_account_statement()) 


def read_file(filename):
    db =  AccountDB()
    # if file name
    with open(filename, 'r') as file:
        for line in file:
            sort_line(line, db)
        # return
    print(db.generate_account_statement())

if __name__ == "__main__":
    if len(sys.argv) > 1:
       filename = sys.argv[1]
       read_file(filename)
    else:
        read_direct_input(sys.stdin)

