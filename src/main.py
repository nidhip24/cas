"""
Main module of the server file
"""

from fastapi import FastAPI
# from pydantic import BaseModel

from src.api.routes.app_user import router as app_user

app = FastAPI(title="CAS API", version="1.0.0")


app.include_router(app_user, prefix="/v1/api/user", tags=["users"])


# @app.get("/")
# def root():
#     return {"Hello": "World"}
