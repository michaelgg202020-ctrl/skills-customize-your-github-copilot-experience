# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to manage a list of tasks. Students will learn how to define routes, validate request data, and return JSON responses from an API.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Create a new FastAPI app and add a basic health check endpoint so the service can respond to requests.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Add a `GET /health` route that returns `{"status": "ok"}`
- Run the app locally with Uvicorn
- Confirm the endpoint responds successfully in a browser or with `curl`

### 🛠️ Build Task CRUD Endpoints

#### Description
Add endpoints that let a client create, read, update, and delete tasks in an in-memory list.

#### Requirements
Completed program should:

- Create a list to store task records in memory
- Add a `GET /tasks` endpoint to return all tasks
- Add a `POST /tasks` endpoint to create a new task
- Add a `GET /tasks/{task_id}` endpoint to fetch one task by ID
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task
- Return JSON data in a clear, consistent format

### 🛠️ Validate Inputs and Improve the API

#### Description
Use request models and validation so the API accepts clean data and returns useful error responses.

#### Requirements
Completed program should:

- Define a `Task` or `TaskCreate` model using Pydantic
- Require a task title and optional completion status
- Prevent invalid input such as empty titles or missing required fields
- Return clear HTTP status codes like `200`, `201`, and `404`
- Test the API using FastAPI's interactive docs at `/docs`

