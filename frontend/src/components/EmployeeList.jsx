import { useEffect, useState, useCallback } from "react";
import API from "../Api/Api";
 
function EmployeeList({ onSelectEmployee }) {
  const [employees, setEmployees] = useState([]);
 
  const fetchEmployees = useCallback(async () => {
    try {
      const res = await API.get("/employees");
      setEmployees(res.data);
    } catch (err) {
      console.error("Error fetching employees", err);
    }
  }, []);
 
  const handleDelete = async (id) => {
    await API.delete(`/employees/${id}`);
    fetchEmployees();
  };
 
  useEffect(() => {
    fetchEmployees();
  }, [fetchEmployees]);
 
  return (
    <div>
      <h2>Employees</h2>
 
      {employees.length === 0 ? (
        <p>No employees found</p>
      ) : (
        <table cellPadding="8">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Dept</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {employees.map((emp) => (
              <tr key={emp.employeeId}>
                <td>{emp.employeeId}</td>
                <td>{emp.fullName}</td>
                <td>{emp.email}</td>
                <td>{emp.department}</td>
                <td>
                  <button onClick={() => onSelectEmployee(emp.employeeId)}>
                    View Attendance
                  </button>
                  <button onClick={() => handleDelete(emp.employeeId)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
 
export default EmployeeList;
 