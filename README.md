INTRODUCTION
A lightweight Human Resource Management System (HRMS) backend built using FastAPI and SQLAlchemy.
This API provides employee management and attendance tracking functionalities with proper HTTP status handling and validation.
FEATURES
Add new employees
View all employees
Delete employees
Mark employee attendance
Get employee attendance records
Duplicate employee prevention
Proper HTTP status codes
Automatic request validation
CORS enabled
TECHNOLOGIES
FastAPI
Database ORM: SQLAlchemy
SQLite / MySQL (configurable)
Pydantic
Uvicorn
STRUCTURE
hrms/
├── backend/ │ 
├── main.py │ 
├── database.py │ 
├── models.py │
├── schemas.py │ 
└── requirements.txt │ 
├── frontend/ │  
├── src/ │  
├── package.json │ 
└── vite.config.js │
API AND ERROR HANDLING
Designed RESTful APIs using FastAPI with proper HTTP method usage.
Implemented structured error handling using HTTPException for business validations such as duplicate records and missing resources.
Ensured consistent API responses and integrated frontend error display for seamless user feedback.
HTTP RESPONSES 
200 OK – Successful data retrieval
201 Created – Resource created successfully
400 Bad Request – Duplicate or invalid input data
404 Not Found – Resource does not exist
422 Unprocessable Entity – Validation failure
