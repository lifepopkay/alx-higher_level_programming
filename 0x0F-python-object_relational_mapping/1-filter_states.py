#!/usr/bin/python3

import MySQLdb
import sys
"""
    A script that lists all staes from database
"""

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], 
                               passwrd=sys.argv[2],
                               db=sys.argv[3], port=3306)

    cur = database.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)
