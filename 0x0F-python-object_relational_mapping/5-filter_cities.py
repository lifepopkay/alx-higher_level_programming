#!/usr/bin/python3

"""
    list name of states and cities
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=sys.argv[1], host='localhost',
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    sql = """SELECT cities.name
           FROM states
           JOIN cities
           ON states.id = cities.id;
           WHERE states.name = {}
           ORDER BY cities.id""".format(sys.argv[4],)

    cur.execute(cur)
    result = cur.fetchall()
    for line in result:
        print(line)

    cur.close()
    db.close()
