from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.config import settings
from routes import evaluation_router, session_router
from models import init_db

import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/api/docs" if settings.ENVIRONMENT == "development" else None,
    redoc_url=None
)

# Initialize Database
@app.on_event("startup")
def on_startup():
    try:
        init_db()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")

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
