from datetime import date

from pydantic import BaseModel, model_validator


class EmployeeIn(BaseModel):
    name: str
    department: str
    startDate: date
    role: str = "employee"


class LeaveIn(BaseModel):
    startDate: date
    endDate: date
    note: str = ""

    @model_validator(mode="after")
    def end_not_before_start(self) -> "LeaveIn":
        if self.endDate < self.startDate:
            raise ValueError("endDate must be on or after startDate")
        return self


class LeaveUpdate(BaseModel):
    endDate: date
    note: str = ""


class TimeOffRequestIn(BaseModel):
    user_id: str
    start_date: date
    end_date: date


class HrRequestIn(BaseModel):
    user_id: str
    prompt: str
