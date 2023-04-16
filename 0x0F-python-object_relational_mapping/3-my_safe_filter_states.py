#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
and it is safe from MySQL injections"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cr = db.cursor()
    myQuery = "SELECT * FROM states WHERE name=%(name)s ORDER BY states.id"
    cr.execute(myQuery, {'name': sys.argv[4]})
    res = cr.fetchall()
    for rows in res:
        print(rows)
    cr.close()
    db.close()
