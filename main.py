from fastapi import FastAPI

from routes.route import router


app = FastAPI(
    title="Audiobooks API",
    version="0.1.0",
    description="An Audiobook API",
    docs_url="/",
    redoc_url="/redoc",
)


app.include_router(router)


@app.get("/hello")
def read_root():
    return {"Hello": "World"}