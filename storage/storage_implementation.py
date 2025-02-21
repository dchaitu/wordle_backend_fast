
from interactor.storage_interface.storage_interface import StorageInterface
from models import Word, CorrectWord, GuessWord, User
from initialize import db



class StorageImplementation(StorageInterface):

    def get_all_words(self):
        words = Word.query.all()
        return words

    def store_correct_word(self, content:str):
        word = Word.query.filter_by(content=content).first()
        correct_word = CorrectWord(word=word)
        db.session.add(correct_word)
        db.session.commit()


    def store_guessed_word(self, username:str, guessed_word:str):
        user = User.query.filter_by(username=username).first()
        guessed_word = GuessWord(content=guessed_word)
        db.session.add(guessed_word)
        db.session.commit()

    def get_latest_word(self):
        correct_word_obj = CorrectWord.query.all()[-1]
        correct_word = correct_word_obj.word.content
        print("Current Word ", correct_word)
        return correct_word

    def get_user_by_username(self, username:str):
        user = User.query.filter_by(username=username).first()
        return user

