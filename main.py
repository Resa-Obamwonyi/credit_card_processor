import sys


def sort_line(line, cache):
    line = line.split(" ")
    command = line[0]
    username = line[1]
    amount = int(line[-1].split('$')[-1])

    if command == 'Add':
        credit_card_no = line[2]
        account_details = [command, username, amount, credit_card_no]
    else:
        account_details = [command, username, amount]


def read_direct_input(s_input):
    # if direct input
    for line in s_input:
        trans_res = sort_line(line)
    return 


def read_file(filename):
    # if file name
    with open(filename, 'r') as file:
        for line in file:
            trans_res = sort_line(line)
        return

if __name__ == "__main__":
    if len(sys.argv) > 1:
       filename = sys.argv[1]
       read_file(filename)
    else:
        read_direct_input(sys.stdin)

