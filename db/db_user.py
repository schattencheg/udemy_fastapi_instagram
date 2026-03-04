from typing import List
from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser


def create(request: UserBase, db: Session):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def request_all(db: Session) -> List[DbUser]:
    return db.query(DbUser).all()


def request_by_id(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if user is not None:
        return user
    return None


def update_by_id(id: int, request: UserBase, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return user.first()


def delete_by_id(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.delete()
    db.commit()
    return 'ok'
