from fastapi import FastAPI
from app.routes import users,onboarduser,auth
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(onboarduser.router)
app.include_router(users.router) 
app.include_router(auth.router)
@app.get("/")
def read_root():
    return {"message": "FastAPI User Management API is Running 🚀"}
