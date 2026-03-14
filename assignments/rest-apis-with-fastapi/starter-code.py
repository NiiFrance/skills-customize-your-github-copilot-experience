# Starter code for REST APIs with FastAPI assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Library API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# In-memory starter dataset
books: list[Book] = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999),
]


@app.get("/")
def read_root():
    # TODO: Customize this message if you want
    return {"message": "Welcome to the Book Library API"}


@app.get("/books")
def get_books():
    # TODO: Return the complete books list
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return one book by id
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    # TODO: Prevent duplicate IDs before appending
    for existing_book in books:
        if existing_book.id == book.id:
            raise HTTPException(status_code=409, detail="Book ID already exists")

    books.append(book)
    return book
