#!/usr/bin/python3
"""
This module that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities\
                INNER JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id")
    rows = cur.fetchall()
    string = ""
    for row in rows:
        if row[4] == argv[4]:
            string += row[2] + ', '

    string = string[:-2]
    print(string)