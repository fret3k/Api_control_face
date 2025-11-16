from pydantic import BaseModel
from typing import Optional

class StaffCreateDTO(BaseModel):
    document_id: str
    first_name: str
    last_name: str
    position: Optional[str] = None
    department: Optional[str] = None

class StaffUpdateDTO(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    position: Optional[str]
    department: Optional[str]
    status: Optional[bool]

class StaffResponseDTO(BaseModel):
    id: int
    document_id: str
    first_name: str
    last_name: str
    position: Optional[str]
    department: Optional[str]
    status: bool

    model_config = {
        "from_attributes": True
    }
