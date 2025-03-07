#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         password=mysql_password,
                         db=database_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '%{}%' \
    ORDER BY id ASC".format(state_name))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
