from datetime import date
from typing import Literal
 
from pydantic import BaseModel, EmailStr
 
 
AttendanceStatus = Literal["Present", "Absent"]
 
class EmployeeCreate(BaseModel):
    employeeId: str
    fullName: str
    email: EmailStr
    department: str
 
 
class EmployeeRead(BaseModel):
    employeeId: str
    fullName: str
    email: EmailStr
    department: str
 
    model_config = {"from_attributes": True}
 
 
class AttendanceCreate(BaseModel):
    employeeId: str
    date: date
    status: AttendanceStatus
 
 
class AttendanceRead(BaseModel):
    employeeId: str
    date: date
    status: AttendanceStatus
 
    model_config = {"from_attributes": True}
 
 
 