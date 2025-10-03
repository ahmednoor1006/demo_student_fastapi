from fastapi import APIRouter

# Reuse new auth package router
from ....auth import router as auth_router_pkg

router = APIRouter()

# Mount auth endpoints under /auth (paths already include /auth)
router.include_router(auth_router_pkg, prefix="")


