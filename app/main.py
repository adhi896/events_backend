from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth_routes
from .routes import event_routes


app = FastAPI(title="Event Management API")

app.include_router(auth_routes.router)
app.include_router(event_routes.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Event API Running"}