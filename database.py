from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create a database URL for SQLAlchemy(connecting to a sql db
# the db file will be located at the same directory with name sql_app.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_history_operations.db"

# create the sqlalchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# create a sessionlocal class. Each instance of the sessionlocal class will be
# a database session. The class itself is not a database yet.
# when we create an instance of the SessionLocal, it will be the actual db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a Base class to create each of the db models or classes(orm-models)
Base = declarative_base()
