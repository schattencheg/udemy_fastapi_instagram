from typing import List
from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle


def create(request: ArticleBase, db: Session) -> DbArticle:
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=False,  # Default: pending admin approval
        user_id=request.user_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all(db: Session) -> List[DbArticle]:
    return db.query(DbArticle).all()


def get_article(id: int, db: Session):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    # Handle errors
    return article


def set_published(id: int, published: bool, db: Session) -> DbArticle:
    pass
