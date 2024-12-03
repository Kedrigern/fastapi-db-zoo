from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from src.database.models import PetRead
from src.database.connection import get_session
from src.services.pet_service import get_all_pets, pet_by_id

pets_router = APIRouter()

@pets_router.get('/')
async def list_pets(session: Session = Depends(get_session)) -> List[PetRead]:
    return get_all_pets(session)


@pets_router.get('/{pet_id}')
async def get_pet(pet_id: int, session: Session = Depends(get_session)) -> PetRead:
    if (pet := pet_by_id(pet_id, session)):
        return pet
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pet not found (id {pet_id})",
    )