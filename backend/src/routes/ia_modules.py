from fastapi import APIRouter

router = APIRouter(prefix="/ia", tags=["ia"])

@router.get("/match")
async def get_matches():
    # Implementation à compléter
    return {"matches": []}
