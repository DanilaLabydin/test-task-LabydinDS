from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Calculation
from database import SessionLocal, engine
from schemas import Postin
from typing import Optional


import crud
import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/history')
def get_operation_history(status: Optional[str] = None, skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    if status:
        history = db.query(Calculation).filter(Calculation.status == status)
    else:
        history = db.query(Calculation).all()
    return history[skip: skip + limit]


@app.post('/calc')
def add_operation(postin: Postin, db: Session = Depends(get_db)):
    return crud.add_calculation(db=db, postin=postin)
