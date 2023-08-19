#!/usr/bin/python3

"""
prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
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
    res = session.query(City).order_by(City.id).all()
    for obj in res:
        print(f"{obj.state.name}: ({obj.id}) {obj.name}")
    session.commit()
    session.close()
