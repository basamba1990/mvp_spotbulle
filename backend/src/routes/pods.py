from fastapi import APIRouter

router = APIRouter(prefix="/pods", tags=["pods"])

@router.post("/")
async def create_pod():
    # Implementation à compléter
    return {"message": "Pod created"}
