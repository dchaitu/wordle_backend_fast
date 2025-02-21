import random

from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from interactor.match_word_interactor import MatchWordInteractor
from models import Word, GuessWord
from populate import get_db
from fastapi.middleware.cors import CORSMiddleware


from models import CorrectWord
from storage.storage_implementation import StorageImplementation

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    #Add specific origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/word/")
async def get_word(db: Session = Depends(get_db)) -> JSONResponse:
    words = db.query(Word).all()
    word = random.choice(words)
    word_id = word.id
    db.add(CorrectWord(word_id=word_id))
    db.commit()

    return JSONResponse({"status": "201",
                         "response": f"word created {word.content}"})


@app.post("/guess/")
async def guess_word(request:Request, db: Session = Depends(get_db)):
    data = await request.json()
    print("Data: ", data)

    print("Guessed word: ", data.get('content'))
    username = data.get('username')
    guessed_word = data.get('content')
    print(f"username: {username}, guessed_word: {guessed_word}")
    storage = StorageImplementation()
    interactor = MatchWordInteractor(storage=storage)
    storage.store_guessed_word(username=username, guessed_word=guessed_word)
    color_dict = interactor.check_is_word_matched(guessed_word)
    print(f"color_dict {color_dict}")

    return JSONResponse({"status": "Success",
                         "data": color_dict})