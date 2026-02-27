import { useState } from "react";
import API from "../Api/Api";
 
function AttendanceForm() {
  const [form, setForm] = useState({
    employeeId: "",
    date: "",
    status: "Present",
  });
 
  const handleSubmit = async (e) => {
    e.preventDefault();
    await API.post("/attendance", form);
    alert("Attendance marked");
  };
 
  return (
    <div>
      <h2>Mark Attendance</h2>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Employee ID"
          onChange={(e) => setForm({ ...form, employeeId: e.target.value })}
          required
        />
        <input
          type="date"
          onChange={(e) => setForm({ ...form, date: e.target.value })}
          required
        />
        <select
          onChange={(e) => setForm({ ...form, status: e.target.value })}
        >
          <option>Present</option>
          <option>Absent</option>
        </select>
        <button type="submit">Mark Attendance</button>
      </form>
    </div>
  );
}
 
export default AttendanceForm;
 