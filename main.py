from fastapi import FastAPI, Response, status
from router import blog_get, blog_post, user, article
from db import models
from db.database import engine


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


# type: ignore[misc]
@app.get("/", status_code=status.HTTP_200_OK, tags=['no_tag'])
def root() -> dict[str, str]:
    return {"message": "Welcome to the API"}


# type: ignore[misc]
@app.get("/health", status_code=status.HTTP_200_OK, tags=['no_tag'])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


models.Base.metadata.create_all(engine)
