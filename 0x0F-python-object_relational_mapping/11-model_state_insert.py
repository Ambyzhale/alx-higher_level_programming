#!/usr/bin/python3
"""Script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s1 = State(name="Louisiana")
    session.add(s1)
    session.commit()
    print(f"{s1.id}")
    session.close()
