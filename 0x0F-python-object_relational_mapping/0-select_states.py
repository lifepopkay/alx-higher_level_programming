#!/usr/bin/python3

"""
    A script that lists all staes from database
"""

import MySQLdb
import sys
"""
    A script that lists all staes from database
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id;""")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
