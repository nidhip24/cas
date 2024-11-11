"""
Session module for database connection
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


def get_engine(database_url: str, echo=False) -> Engine:
    """
    Creates and returns a SQLAlchemy Engine object for connecting
    to a database.

    Parameters:
        database_url (str): The URL of the database to connect to.
        Defaults to SQLALCHEMY_DATABASE_URL.
        echo (bool): Whether or not to enable echoing of SQL statements.
        Defaults to False.

    Returns:
        Engine: A SQLAlchemy Engine object representing the
        database connection.
    """
    engine = create_engine(database_url, echo=echo)
    return engine


def get_local_session(database_url: str, echo=False) -> sessionmaker:
    """
    Create and return a sessionmaker object for a local database session.

    Parameters:
        database_url (str): The URL of the local database.
        Defaults to `SQLALCHEMY_DATABASE_URL`.
        echo (bool): Whether to echo SQL statements to the console.
        Defaults to `False`.

    Returns:
        sessionmaker: A sessionmaker object configured for the local
        database session.
    """
    engine = get_engine(database_url, echo)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/CAS"
