import { useEffect, useState } from "react";
import API from "../Api/Api";
 
function AttendanceList({ employeeId }) {
  const [records, setRecords] = useState([]);
 
  useEffect(() => {
    if (!employeeId) return;
 
    API.get(`/attendance/${employeeId}`)
      .then((res) => setRecords(res.data))
      .catch(() => setRecords([]));
  }, [employeeId]);
 
  return (
    <div>
      <h2>Attendance Records</h2>
 
      {!employeeId ? (
        <p>Select employee to view attendance</p>
      ) : records.length === 0 ? (
        <p>No attendance records</p>
      ) : (
        <ul>
          {records.map((r, i) => (
            <li key={i}>
              {r.date} — {r.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
 
export default AttendanceList;
 