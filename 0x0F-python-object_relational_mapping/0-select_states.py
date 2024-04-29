#!/usr/bin/python3

import MySQLdb
import sys
"""
    A script that lists all staes from database
"""

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], 
                               passwd=sys.argv[2],
                               db=sys.argv[3], port=3306)

    cur = database.cursor()
    code = """SELECT * FROM states;"""

    cur.execute(code)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    database.close()
