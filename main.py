from fastapi import FastAPI
from routers.staffRouter import router as staff_router

app = FastAPI(
    title="Staff Attendance API",
    version="1.0"
)

app.include_router(staff_router)
