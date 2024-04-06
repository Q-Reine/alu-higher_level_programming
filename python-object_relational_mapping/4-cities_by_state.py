#!/usr/bin/python3
"""
List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    c = database.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
               FROM cities INNER JOIN states
               ON states.id = cities.state_id
               ORDER BY cities.id ASC;""")
    states = cur.fetchall()

    for state in states:
        print(state)
