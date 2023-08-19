#!/usr/bin/python3

"""
 Creates the State “California” with the City “San Francisco”  on db
"""

if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    u = argv[1]
    p = argv[2]
    db = argv[3]
    ht = "@localhost:3306"
    engine = create_engine(f"mysql+mysqldb://{u}:{p}{ht}/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instan_state = State(name="California")
    instan_city = City(name="San Francisco")
    instan_state.cities += [instan_city]
    session.add(instan_state)
    session.commit()
    session.close()
