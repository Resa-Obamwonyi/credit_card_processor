import sys
from database.db import AccountDB
from utils.logic import sort_line


def read_direct_input(s_input):
    db =  AccountDB()
    for line in s_input:
        sort_line(line, db)
    
    summary = db.generate_account_summary()
    
    print("\n")
    for line in summary:
        print(line)


def read_file(filename):
    db =  AccountDB()
    with open(filename, 'r') as file:
        for line in file:
            sort_line(line, db)
            
    summary = db.generate_account_summary()
    for line in summary:
        print(line)

if __name__ == "__main__":
    # determine if file or direct input, and process accordingly
    if len(sys.argv) > 1:
       filename = sys.argv[1]
       read_file(filename)
    else:
        read_direct_input(sys.stdin.readlines())

