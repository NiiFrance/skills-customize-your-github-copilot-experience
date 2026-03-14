# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI so you can practice creating endpoints, handling request parameters, and returning JSON responses. By the end of this assignment, you will understand how to design and test simple API routes for real applications.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI app and implement core endpoints for a simple "Book Library" API.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run it locally.
- Implement `GET /` that returns a short welcome message in JSON.
- Implement `GET /books` that returns all books as a list of objects.
- Implement `GET /books/{book_id}` that returns one book by id, or an error message if not found.


### 🛠️	Add Data Validation and Create Operation

#### Description
Add an endpoint for creating books and validate incoming data using a Pydantic model.

#### Requirements
Completed program should:

- Define a `Book` model with fields: `id` (int), `title` (str), `author` (str), and `year` (int).
- Implement `POST /books` to add a new book and return the created object.
- Prevent duplicate `id` values when adding a new book.
- Return clear status responses for success and validation or conflict errors.
