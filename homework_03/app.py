from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",
    tags=["test"],)


@router.get("")
def get_pong():
    return {"message": "pong"}
