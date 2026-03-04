from typing import List, Optional
from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create user


@router.post('/', response_model=UserDisplay)
def create(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create(request, db)

# Read


@router.get('/all', response_model=List[UserDisplay])
def request_all(db: Session = Depends(get_db)):
    return db_user.request_all(db)


@router.get('/{id}', response_model=Optional[UserDisplay])
def request(id: int, db: Session = Depends(get_db)):
    return db_user.request_by_id(id, db)

# Update


@router.post('/{id}/update', response_model=UserDisplay)
def update(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_by_id(id, request, db)

# Delete


@router.post('/{id}/delete')
def delete(id: int, db: Session = Depends(get_db)):
    return db_user.delete_by_id(id, db)
