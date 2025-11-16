from dto.staffDto import StaffCreateDTO, StaffUpdateDTO
from dao.staffDao import StaffDAO
from fastapi import HTTPException

class StaffService:

    @staticmethod
    def get_all_staff():
        res = StaffDAO.get_all()
        return res.data

    @staticmethod
    def get_staff_by_id(staff_id: int):
        res = StaffDAO.get_by_id(staff_id)
        if res.data is None:
            raise HTTPException(status_code=404, detail="Staff not found")
        return res.data

    @staticmethod
    def create_staff(dto: StaffCreateDTO):
        data = dto.dict()
        res = StaffDAO.create(data)
        return res.data[0]

    @staticmethod
    def update_staff(staff_id: int, dto: StaffUpdateDTO):
        data = {k: v for k, v in dto.dict().items() if v is not None}
        res = StaffDAO.update(staff_id, data)
        if len(res.data) == 0:
            raise HTTPException(status_code=404, detail="Staff not found")
        return res.data[0]

    @staticmethod
    def delete_staff(staff_id: int):
        res = StaffDAO.delete(staff_id)
        if len(res.data) == 0:
            raise HTTPException(status_code=404, detail="Staff not found")
        return {"message": "Deleted successfully"}
