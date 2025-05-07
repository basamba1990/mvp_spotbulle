from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, users, profiles, pods, ia_modules

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(pods.router)
app.include_router(ia_modules.router)

@app.get("/")
def read_root():
    return {"message": "SpotBulle API"}
