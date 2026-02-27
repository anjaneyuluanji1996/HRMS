from sqlalchemy import Column, Date, Integer, String, UniqueConstraint
from database import Base
 
class Employee(Base):
    __tablename__ = "employees"
 
    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(String, unique=True, index=True)
    fullName = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
class Attendance(Base):
    __tablename__ = "attendance"
    __table_args__ = (
        UniqueConstraint("employeeId", "date", name="uq_attendance_employee_date"),
    )
 
    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(String)
    date = Column(Date)
    status = Column(String)
 
 