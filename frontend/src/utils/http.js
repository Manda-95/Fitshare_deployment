import axios from "axios";

const http = axios.create({
  baseURL: import.meta.env.VUE_APP_API_BASE_URL,
});

http.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default http;
