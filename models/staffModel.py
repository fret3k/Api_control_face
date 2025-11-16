from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StaffBase(BaseModel):
    document_id: str
    first_name: str
    last_name: str
    position: Optional[str] = None
    department: Optional[str] = None
    status: Optional[bool] = True

class StaffCreate(StaffBase):
    pass

class StaffRead(StaffBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True