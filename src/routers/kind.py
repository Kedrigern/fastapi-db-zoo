from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from src.database.models import KindRead
from src.database.connection import get_session
from src.services.kind_service import kind_by_id, get_all_kinds

kind_router = APIRouter()


@kind_router.get("/")
async def list_kinds(session: Session = Depends(get_session)) -> list[KindRead]:
    return get_all_kinds(session)


@kind_router.get("/{kind_id}")
async def get_kind(kind_id: int, session: Session = Depends(get_session)) -> KindRead:
    if kind := kind_by_id(kind_id, session):
        return kind
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Kind not found (id {kind_id})",
    )
