from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Rahul Dey",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast",
        "date_posted": "January 13, 2026",
    },
    {
        "id": 2,
        "author": "Admin",
        "title": "New Edge Web Development With Python",
        "content": "Python is really great for web development and FastAPI framework makes it even better.",
        "date_posted": "December 31, 2025",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home() -> HTMLResponse:
    return HTMLResponse(content=f"<h1>{posts[0]['title']}</h1>")


@app.get("/api/posts")
def get_posts() -> list[dict]:
    return posts
