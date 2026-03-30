import uvicorn
from fastapi import FastAPI
from src.api import auth
from src.config import Config

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Config.PORT)