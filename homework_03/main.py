from fastapi import FastAPI
from app import router as app_router
app = FastAPI()
app.include_router(app_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

