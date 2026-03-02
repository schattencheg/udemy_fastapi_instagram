from fastapi import FastAPI, Response, status
from router import blog_get
from router import blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/", status_code=status.HTTP_200_OK, tags=['no_tag'])  # type: ignore[misc]
def root(response: Response) -> dict[str, str]:
    return {"message": "Welcome to the API"}


@app.get("/health", status_code=status.HTTP_200_OK, tags=['no_tag'])  # type: ignore[misc]
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
