import sys
from logic import process


def _direct_input(s_input):
    # if direct input
    for line in s_input:
        line = line.split(" ")
        command = line[0]
        username = line[1]
        amount = line[-1]
        if command == 'Add':
                credit_card_no = line[2]
                process(command, username, amount, credit_card_no)
        
        print("{} {} to {}'s account".format(command,amount,username))


def _file(filename):
    # if file name
    with open(filename, 'r') as file:
        for line in file:
            line = line.split(" ")
            command = line[0]
            username = line[1]
            amount = line[-1]

            if command == 'Add':
                credit_card_no = line[2]
                process(command, username, amount, credit_card_no)
            
            process(command, username, amount)
            print("{} {} to {}'s account".format(command,amount,username))


if __name__ == "__main__":
    if len(sys.argv) > 1:
       filename = sys.argv[1]
       _file(filename)
    else:
        _direct_input(sys.stdin)

