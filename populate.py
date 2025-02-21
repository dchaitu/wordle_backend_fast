import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker

from models import Word, Base

engine = sa.create_engine('sqlite:///words.db')
connection = engine.connect()
metadata = sa.MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def create_words(db: Session = Depends(get_db)):
    words = ['grain', 'water', 'dance', 'overs', 'milky', 'jazzy', 'dream']


    try:
        word_objects = [Word(content=word.upper()) for word in words]
        db.add_all(word_objects)  # Add all words at once
        db.commit()  # Commit after all additions
    except Exception as e:
        db.rollback()  # Rollback if any error occurs
        print("Error:", e)





if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # create_words()