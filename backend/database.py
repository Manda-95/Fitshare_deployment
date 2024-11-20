from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = "mysql+mysqlconnector://myuser:mypassword@localhost/fitshare_database"
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
