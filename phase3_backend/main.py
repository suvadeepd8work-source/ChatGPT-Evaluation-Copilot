from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.config import settings
from routes import evaluation_router, session_router
from models import init_db

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Initialize Database
@app.on_event("startup")
def on_startup():
    init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(evaluation_router, prefix=settings.API_V1_STR)
app.include_router(session_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} Phase 3 API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
