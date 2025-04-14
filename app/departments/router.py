from fastapi import APIRouter
from app.departments.model import Department
from app.departments.controller import create_department, get_department

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/")
def route_create_department(department: Department):
    return create_department(department)

@router.get("/{dept_id}")
def route_get_department(dept_id: int):
    return get_department(dept_id)
