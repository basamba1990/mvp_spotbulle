from fastapi import APIRouter

router = APIRouter(prefix="/profiles", tags=["profiles"])

@router.get("/{user_id}/disc")
async def get_disc_profile(user_id: int):
    # Implementation à compléter
    return {"profile": "DISC_RESULTS"}
