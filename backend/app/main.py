from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from bson import ObjectId
from .api import auth, finance, ml

app = FastAPI(title="Finance App API", version="1.0.0")

# Custom JSON serializer for ObjectId
app.json_encoders = {
    ObjectId: str
}

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(finance.router, prefix="/api/finance", tags=["finance"])
app.include_router(ml.router, prefix="/api/ml", tags=["ml"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Finance App API"}
