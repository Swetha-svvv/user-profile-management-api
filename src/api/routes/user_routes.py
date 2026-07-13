from fastapi import APIRouter, HTTPException

from src.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from src.services.user_service import UserService

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

service = UserService()


@router.post("", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    try:
        return service.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user: UserUpdate):
    try:
        return service.update_user(user_id, user)
    except ValueError as e:
        message = str(e)

        if message == "User not found":
            raise HTTPException(status_code=404, detail=message)

        raise HTTPException(status_code=409, detail=message)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: str):
    try:
        service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/{user_id}/enriched")
def get_enriched_user(user_id: str):
    try:
        return service.get_enriched_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))