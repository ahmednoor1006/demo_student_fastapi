from fastapi import APIRouter

# Import sub-routers
from .routers.students import router as students_router
from .routers.teachers import router as teachers_router
from .routers.auth import router as auth_router

api_v1_router = APIRouter()

# Mount feature routers
api_v1_router.include_router(students_router, prefix="/students", tags=["students"])
api_v1_router.include_router(teachers_router, prefix="/teachers", tags=["teachers"])
# Auth router already defines paths starting with "/auth"; include without extra prefix
api_v1_router.include_router(auth_router, prefix="", tags=["auth"])


