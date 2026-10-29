import re
from datetime import date

from fastapi import APIRouter, HTTPException

from models import LeaveIn, LeaveUpdate
from services import leave_service

router = APIRouter(tags=["leave"])

MONTH_RE = re.compile(r"^\d{4}-\d{2}$")


@router.post("/employees/{employee_id}/leave", status_code=201)
def create_leave(employee_id: str, payload: LeaveIn):
    body = payload.model_dump(mode="json")
    return leave_service.save(employee_id, str(body["startDate"]), body)


@router.get("/employees/{employee_id}/leave")
def list_leave(employee_id: str, month: str | None = None):
    if month and not MONTH_RE.match(month):
        raise HTTPException(status_code=422, detail="month must be in YYYY-MM format")
    return {"leave": leave_service.list_for_employee(employee_id, month)}


@router.put("/employees/{employee_id}/leave/{start_date}")
def save_leave(employee_id: str, start_date: date, payload: LeaveUpdate):
    return leave_service.save(
        employee_id, start_date.isoformat(), payload.model_dump(mode="json")
    )
