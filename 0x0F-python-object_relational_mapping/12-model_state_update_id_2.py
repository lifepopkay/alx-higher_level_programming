#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    """
    Script that takes 3 arguments: username, password, and database name
    and updates the name of a state object with id=2.
    """

    if len(sys.argv) != 4:
        print('Use: username, password database_name')
        exit(1)

    username, password, database_name = sys.argv[1:]

    # Connect to the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the state object with id=2 (or None if not found)
    state = session.query(State).filter_by(id=2).first()

    # Update the state name if it exists
    if state:
        state.name = "New Mexico"
        session.commit()  # Commit changes to the database
        print("State with id {} updated".format(state.id))
    else:
        print("State with id 2 not found")

    # Close the session
    session.close()
