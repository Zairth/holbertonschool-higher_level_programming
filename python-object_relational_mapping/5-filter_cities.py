#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists 
all cities of that state, using the database hbtn_0e_4_usa
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
    cursor.execute("""
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;""", (state_name,))

    results = cursor.fetchall()
    city_names = ", ".join(row[0] for row in results)
    print(city_names)

    cursor.close()
    db.close()
