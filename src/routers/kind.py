from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from src.database.models import Kind, KindWrite
from src.database.connection import get_session
from src.services.kind_service import kind_by_id, kind_all, kind_add

kind_router = APIRouter()


@kind_router.get("/")
async def list_kinds(session: Session = Depends(get_session)) -> list[Kind]:
    return kind_all(session)


@kind_router.get("/{kind_id}")
async def get_kind(kind_id: int, session: Session = Depends(get_session)) -> Kind:
    if kind := kind_by_id(kind_id, session):
        # Convert
        return kind
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Kind not found (id {kind_id})",
    )

@kind_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_kind(new_kind: KindWrite, session: Session = Depends(get_session)) -> Kind:
    added_kind = kind_add(Kind(name=new_kind.name), session)
    return added_kind