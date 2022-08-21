import sys
from logic import process
# if direct input

# if file name
filename = sys.argv[1]
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
        # print("{} {} to {}'s account".format(command,amount,username))