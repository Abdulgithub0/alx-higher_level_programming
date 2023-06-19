#!/usr/bin/python3

"""
 a script that lists all cities from the database hbtn_0e_4_usa
"""


if "__main__" == __name__:
    import MySQLdb as mysql
    from sys import argv

    use_db = mysql.connect(host="localhost", user=argv[1], passwd=argv[2],
                           database=argv[3])
    navigate = use_db.cursor()
    navigate.execute("SELECT cities.id, cities.name, states.name FROM \
                     cities c, states s WHERE c.state_id = s.id \
                     ORDER BY c.id ASC")
    for i in navigate.fetchall():
        print(i)
    navigate.close()
    use_db.close()
