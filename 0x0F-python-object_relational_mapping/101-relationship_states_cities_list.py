#!/usr/bin/python3

"""
 a script that lists all State objects, and corresponding
 City objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv

    u = argv[1]
    p = argv[2]
    ht = f"@localhost:3306/{argv[3]}"

    # create engine
    engine = create_engine(f"mysql+mysqldb://{u}:{p}{ht}", pool_pre_ping=True)

    # mapped classes to their corresponding tables then store on engine
    Base.metadata.create_all(engine)

    # open communication channel to the dialect
    session = sessionmaker(bind=engine)()

    res = session.query(State).join(City).order_by(State.id, City.id).all()
    for s in res:
        print(s.id, s.name, sep=": ")
        for c in s.cities:
            print("    ", end="")
            print(c.id, c.name, sep=": ")
    session.commit()
    session.close()
