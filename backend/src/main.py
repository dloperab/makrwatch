import uvicorn

from rest.app import create_app

app = create_app()

"""
    This is the entry point for the application.
"""
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
