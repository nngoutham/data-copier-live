import sys
from config import DB_DETAILS
from util import get_table

def main():
    """program takes at lest one argument"""
    env =sys.argv[1]
    db_details = DB_DETAILS[env]
    tables=get_table('table_list')
    for table in tables["table_name"]:
        print(table)


if __name__=='__main__':
    main()