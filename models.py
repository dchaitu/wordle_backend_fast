from operator import index
from wsgiref.validate import validator

from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column


# class User(BaseModel):
#     id: int
#     name: str
#     password: str
#     email: str
#
class WordModel(BaseModel):
    id: int
    content: str
#
#     @validator('content')
#     def validate_content(cls, v):
#         if len(v) < 5 or v.islower():
#             raise ValueError('content must be at least 5 characters')
#         return v
#
# class GuessWord(BaseModel):
#     # user: User
#     content: str
#
#
# class CorrectWord(BaseModel):
#     word: Word
class WordResponse(BaseModel):
    id: int
    content: str

    class Config:
        from_attributes = True

Base = declarative_base()

class Word(Base):
    __tablename__ = "word"
    id: Mapped[int] = mapped_column(default=None, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String(5), unique=True)


class CorrectWord(Base):
    __tablename__ = "correct_word"
    id: Mapped[int] = mapped_column(default=None, primary_key=True, autoincrement=True)
    word_id: Mapped[int] = mapped_column(ForeignKey('word.id', ondelete="CASCADE"))
    # word: Mapped[Word] = relationship(Word, cascade="all, delete", back_populates="correct_word")


class GuessWord(Base):
    __tablename__ = "guess_word"
    id: Mapped[int] = mapped_column(default=None, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String)