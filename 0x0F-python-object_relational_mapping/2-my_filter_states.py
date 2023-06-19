#!/usr/bin/python3

"""
 a script that takes in an argument and displays all values in the
 states table of hbtn_0e_0_usa where name matches the argument.
"""


if "__main__" == __name__:
    import MySQLdb as mysql
    from sys import argv

    use_db = mysql.connect(host="localhost", user=argv[1], passwd=argv[2],
                           database=argv[3])
    navigate = use_db.cursor()
    arg = argv[4]
    string = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(arg)
    navigate.execute(string)
    for i in navigate.fetchall():
        print(i)
    navigate.close()
    use_db.close()
