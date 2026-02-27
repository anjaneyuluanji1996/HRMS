from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI(title="HRMS Lite API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
Base.metadata.create_all(bind=engine)
 
# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# ---------------- Employees ----------------
 
@app.post("/employees", status_code=status.HTTP_201_CREATED)
def add_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    new_emp = models.Employee(**emp.model_dump())
    db.add(new_emp)
    try:
        db.commit()
        db.refresh(new_emp)
    except IntegrityError:
        db.rollback()
        existing_emp_id = db.query(models.Employee).filter(
            models.Employee.employeeId == emp.employeeId
        ).first()
        if existing_emp_id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")
 
        existing_email = db.query(models.Employee).filter(
            models.Employee.email == emp.email
        ).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")
 
        raise HTTPException(status_code=400, detail="Invalid employee data")
    return {"message": "Employee added successfully"}
 
 
@app.get("/employees", response_model=list[schemas.EmployeeRead])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()
 
 
@app.delete("/employees/{employeeId}")
def delete_employee(employeeId: str, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(
        models.Employee.employeeId == employeeId
    ).first()
 
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
 
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}
 
# ---------------- Attendance ----------------
 
@app.post("/attendance", status_code=status.HTTP_201_CREATED)
def mark_attendance(att: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.employeeId == att.employeeId
    ).first()
 
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
 
    existing_attendance = db.query(models.Attendance).filter(
        models.Attendance.employeeId == att.employeeId,
        models.Attendance.date == att.date,
    ).first()
 
    if existing_attendance:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this employee on this date",
        )
 
    new_att = models.Attendance(**att.model_dump())
    db.add(new_att)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this employee on this date",
        )
    return {"message": "Attendance marked"}
 
 
@app.get("/attendance/{employeeId}", response_model=list[schemas.AttendanceRead])
def get_attendance(employeeId: str, db: Session = Depends(get_db)):
    return db.query(models.Attendance).filter(
        models.Attendance.employeeId == employeeId
    ).all()