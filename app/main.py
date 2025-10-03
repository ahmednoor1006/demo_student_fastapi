import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.middleware.sessions import SessionMiddleware
import database
from models import Base
from api.v1.router import api_v1_router

Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Student Teacher Management System")

# Add session middleware for OAuth
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "your-secret-key"))

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include versioned API under /api/v1
app.include_router(api_v1_router, prefix="/api/v1")

# Serve frontend
@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_dir, 'index.html'))

@app.get("/dashboard")
async def read_dashboard():
    return FileResponse(os.path.join(static_dir, 'dashboard.html'))

@app.get("/student")
async def read_student():
    return FileResponse(os.path.join(static_dir, 'student.html'))

@app.get("/teacher")
async def read_teacher():
    return FileResponse(os.path.join(static_dir, 'teacher.html'))

# Resource routes moved under /api/v1
