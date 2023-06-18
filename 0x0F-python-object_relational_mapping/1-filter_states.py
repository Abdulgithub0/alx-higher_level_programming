#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa when state[0] = N
"""


if "__main__" == __name__:
    import MySQLdb as mysql
    from sys import argv

    use_db = mysql.connect(host="localhost", user=argv[1], passwd=argv[2],
                           database=argv[3])
    navigate = use_db.cursor()
    navigate.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for i in navigate.fetchall():
        print(i)
    navigate.close()
    use_db.close()
