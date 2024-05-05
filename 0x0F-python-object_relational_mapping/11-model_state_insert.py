#!/usr/bin/python3
"""
    write a script that add state object louisiana
    to the database
"""

import dys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engin

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # create a new object instance
    Lou = State(name='Louisiana')
    session.add(Lou)
    session.commit()

    # print state.id
    state_add = session.query(State)\
                       .filter(State.name == 'Louisiana')\
                       .one()
    print(state_add.id)

    session.close()
