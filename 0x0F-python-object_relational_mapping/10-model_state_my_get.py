#!/usr/bin/python3

"""
a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    # Get configure info
    u = argv[1]
    p = argv[2]
    db = argv[3]
    ht = "@localhost:3306"
    engine = create_engine(f"mysql+mysqldb://{u}:{p}{ht}/{db}",
                           pool_pre_ping=True)

    # bind the configure info to this .py process and connect
    session = sessionmaker(bind=engine)()
    s = argv[4]
    res = session.query(State).filter(State.name == s).all()
    if res:
        for obj in res:
            print(f"{obj.id}")
    else:
        print("Not found")
    session.commit()
    session.close()
