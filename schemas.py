from typing import List, Optional
from pydantic import BaseModel


# Article for UserDisplay
class Article(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    user_id: int

    class Config():
        from_attributes: bool = True


class ArticleBase(BaseModel):
    title: str
    content: str
    user_id: int


# User for ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config():
        from_attributes: bool = True


class ArticleDisplay(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    user_id: int

    class Config():
        from_attributes: bool = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    articles: List[Article] = []

    class Config():
        from_attributes: bool = True
