import sys
from logic import process


def sort_line(line):
    line = line.split(" ")
    command = line[0]
    username = line[1]
    amount = line[-1]

    if command == 'Add':
        credit_card_no = line[2]
        res = process(command, username, amount, credit_card_no)
    else:
        res = process(command, username, amount)
    
    return res
    # print("{} {} to {}'s account".format(command,amount,username))


def _direct_input(s_input):
    result = {}
    # if direct input
    for line in s_input:
        trans_res = sort_line(line)
        result.update(trans_res)
    return result


def _file(filename):
    result = {}
    # if file name
    with open(filename, 'r') as file:
        for line in file:
            trans_res = sort_line(line)
            result.update(trans_res)
        return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
       filename = sys.argv[1]
       _file(filename)
    else:
        _direct_input(sys.stdin)

