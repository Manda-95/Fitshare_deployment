import axios from "@/utils/http";

export const login = (username, password) => {
    const data = new URLSearchParams();
    data.append("username", username);
    data.append("password", password);
  
    return axios.post("/auth/token", data, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  };

export const register = (data) => {
  return axios.post("/auth/register", data);
};
