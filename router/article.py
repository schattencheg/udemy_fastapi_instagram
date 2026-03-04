from typing import List, Optional
from schemas import ArticleBase, ArticleDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article

router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create article
@router.post('/', response_model=ArticleDisplay)
def create(request: ArticleBase, db: Session = Depends(get_db)):
    article = db_article.create(request, db)
    return article


# Get all articles
@router.get('/all', response_model=List[ArticleDisplay])
def get_all(db: Session = Depends(get_db)):
    articles = db_article.get_all(db)
    return articles


# Get article by id
@router.get('/{id}', response_model=ArticleDisplay)
def get(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(id, db)


# Publish article (admin feature)
@router.post('/{id}/publish')
def publish_article(id: int, db: Session = Depends(get_db)):
    return db_article.set_published(id, True, db)
