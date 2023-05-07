
# <h1 align="center">FastAPI: To-do list</h1>

This repository contains a FastAPI-based API for a To-do list app. The API allows for CRUD operations on user authentication and todo items.

Frontend and database components are still under development!.

## API endpoints

## 👩‍💻 Run locally

To run the backend locally, you will need to set up a virtual environment with the dependencies installed.

1. Clone this repo.
```bash
$ git clone https://github.com/alyshapm/react-todo-2.0
```

2. Switch directory to the server folder.
```bash
$ cd react-todo-2.0/server
```

3. Create and activate venv
```bash
$ virtualenv venv
$ source venv/bin/activate
```

4. Pip install requirements
```bash
$ pip install -r requirements.txt
```

5. Run the entry point file with uvicorn and navigate to  localhost:8000/docs for the API documentation
```bash
$ uvicorn main:app --reload
```
