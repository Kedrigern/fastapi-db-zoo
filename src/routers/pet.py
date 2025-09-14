from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from src.database.models import Pet, PetWrite
from src.database.connection import get_session
from src.services.pet_service import pets_all, pet_by_id, pet_add

pets_router = APIRouter()


@pets_router.get("/")
async def list_pets(session: Session = Depends(get_session)) -> list[Pet]:
    return pets_all(session)


@pets_router.get("/{pet_id}")
async def get_pet(pet_id: int, session: Session = Depends(get_session)) -> Pet:
    if pet := pet_by_id(pet_id, session):
        return pet
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pet not found (id {pet_id})",
    )

@pets_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_pet(new_pet: PetWrite, session: Session = Depends(get_session)) -> Pet:
    try:
        added_pet = pet_add(Pet.model_validate(new_pet), session)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Kind not found (id {new_pet.kind_id})",
        )
    return added_pet