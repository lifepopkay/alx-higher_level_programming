#!/usr/bin/python3

"""
    A script that takes in an argument and
    displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE '{}'
                ORDER BY states.id;""".format(sys.argv[4]))
    data = cur.fetchall()

    for state in data:
        print(state)

    cur.close()
    db.close
