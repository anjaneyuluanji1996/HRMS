import axios from "axios";
 
const API = axios.create({
  baseURL: "https://hrms-kwp3.onrender.com",
});
 
export default API;
 