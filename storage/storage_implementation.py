from sqlalchemy.orm import Session

from interactor.storage_interface.storage_interface import StorageInterface
from models import Word, CorrectWord, GuessWord
from populate import SessionLocal


class StorageImplementation(StorageInterface):
    def __init__(self):
        self.db: Session = SessionLocal()



    def get_all_words(self):
        words = self.db.query(Word).all()
        return words

    def store_correct_word(self, content:str):
        word = self.db.query(Word).filter_by(content=content).first()
        if word:
            correct_word = CorrectWord(word=word)
            self.db.add(correct_word)
            self.db.commit()


    def store_guessed_word(self, username:str, guessed_word:str):
        guessed_word = GuessWord(content=guessed_word)
        self.db.add(guessed_word)
        self.db.commit()

    def get_latest_word(self):
        correct_word_obj = self.db.query(CorrectWord).all()[-1]
        correct_word_id = correct_word_obj.word_id
        word_content = self.db.query(Word).filter_by(id=correct_word_id).first().content
        return word_content

    def get_user_by_username(self, username:str):
        # user = User.query.filter_by(username=username).first()
        # return user
        pass
