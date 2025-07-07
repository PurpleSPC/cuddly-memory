from fastapi import APIRouter, HTTPException, Query, Depends
from sqlmodel import select, Session
from pydantic import BaseModel
from typing import Optional, List
from app.db.database import get_session
from app.db.crud import (create_surgeon, 
                         assign_surgeon_npi, 
                         assign_surgeon_account, 
                         get_surgeon,
                         create_account,
                         update_account,
                         )
from app.models import (Surgeon,
                        Account
                        )

router = APIRouter()

class SurgeonCreate(BaseModel):
    name: str
    npi_no: int

class SurgeonNPIUpdate(BaseModel):
    id: int
    npi_no: int

class SurgeonACCTUpdate(BaseModel):
    id: int
    acct_id: int

class AccountCreate(BaseModel):
    name: str
    address: Optional[str]

@router.post("/surgeons/create")
def create_surgeon_endpoint(data: SurgeonCreate):
    try:
        surgeon = create_surgeon(name=data.name, npi_no=data.npi_no)
        return surgeon
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.get("/surgeons/id")
def get_surgeon_by_id_endpoint(surgeon_id:int):
    try:
        surgeon = get_surgeon(surgeon_id=surgeon_id)
        return surgeon
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/surgeons/search",response_model=List[Surgeon])
def search_surgeons_endpoint(
    name: Optional[str] = Query(None, min_length=2),
    npi_no: Optional[int] = None,
    specialty: Optional[str] = None,
    active_only: bool = False,
    limit: int = Query(50, ge=1, le=200),
    offset: int  = Query(0, le=50),
    session: Session = Depends(get_session)
):
    statement = select(Surgeon)

    if name: 
        statement = statement.where(Surgeon.name.ilike(f"%{name}%"))
    if npi_no:
        statement = statement.where(Surgeon.npi_no == npi_no)
    if specialty:
        statement = statement.where(Surgeon.specialty == specialty)
    if active_only:
        statement = statement.where(Surgeon.is_active.is_(True))
    
    statement = statement.limit(limit).offset(offset)
    return session.exec(statement).all()

@router.post("/surgeons/assign_npi")
def assign_surgeon_npi_endpoint(data: SurgeonNPIUpdate):
    try:
        assign_npi = assign_surgeon_npi(surgeon_id=data.id, npi_no=data.npi_no)
        return assign_npi
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.post("/surgeons/assign_acct")
def assign_surgeon_acct_endpoint(data: SurgeonACCTUpdate):
    try:
        surg_acct = assign_surgeon_account(surgeon_id=data.id, account_id=data.acct_id )
        return surg_acct
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.post("/accounts/create")
def create_account_endpoint(data: AccountCreate):
    try:
        account = create_account(name=data.name, address=data.address)
        return account
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.get("/accounts/search", response_model=List[Account])
def search_account_endpoint(
    name: Optional[str] = Query(None, min_length=2),
    session: Session = Depends(get_session)
):
    statement = select(Account)
    if name:
        pattern = f"%{name}%"
        statement = statement.where(Account.name.ilike(pattern))
    accounts = session.exec(statement).all()
    return accounts

@router.post("/accounts/update")
def update_account_endpoint(data: Account):
    try:
        acct = update_account(data.id, data.name, data.address)
        return acct 
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    