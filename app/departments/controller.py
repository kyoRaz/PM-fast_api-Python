from fastapi import HTTPException
from app.departments.model import Department

departments_db = {}

def create_department(department: Department) -> Department:
    if department.id in departments_db:
        raise HTTPException(status_code=400, detail="Le d\u00e9partement existe d\u00e9j\u00e0.")
    departments_db[department.id] = department
    return department

def get_department(dept_id: int) -> Department:
    dept = departments_db.get(dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="D\u00e9partement non trouv\u00e9.")
    return dept
