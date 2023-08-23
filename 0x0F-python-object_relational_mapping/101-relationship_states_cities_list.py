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
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).join(City).order_by(State.id, City.state_id).all()
    # res = session.query(State, City).filter(State.id == City.
    for s in res:
        print(f"{s.id}:  {s.name}")
        for c in s.cities:
            print(f"     {c.id}: {c.name}")
    session.commit()
    session.close()
