#!/usr/bin/python3

"""
a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    res = session.query(State).filter(State.id == 2
                                      ).update({"name": "New Mexico"})
    session.commit()
    session.close()
