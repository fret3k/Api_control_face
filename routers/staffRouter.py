from fastapi import APIRouter
from services.staffService import StaffService
from dto.staffDto import StaffCreateDTO, StaffUpdateDTO, StaffResponseDTO
from typing import List

router = APIRouter(prefix="/staff", tags=["Staff"])

@router.get("/", response_model=List[StaffResponseDTO])
def list_staff():
    return StaffService.get_all_staff()

@router.get("/{staff_id}", response_model=StaffResponseDTO)
def get_staff(staff_id: int):
    return StaffService.get_staff_by_id(staff_id)

@router.post("/", response_model=StaffResponseDTO)
def create_staff(dto: StaffCreateDTO):
    return StaffService.create_staff(dto)

@router.put("/{staff_id}", response_model=StaffResponseDTO)
def update_staff(staff_id: int, dto: StaffUpdateDTO):
    return StaffService.update_staff(staff_id, dto)

@router.delete("/{staff_id}")
def delete_staff(staff_id: int):
    return StaffService.delete_staff(staff_id)
