#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id):
        print(f'{state.name}: ({city.id}) {city.name}')