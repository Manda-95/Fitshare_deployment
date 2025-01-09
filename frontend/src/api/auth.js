import axios from "@/utils/http";

export const login = (username, password) => {
  try{
    const data = new URLSearchParams();
    data.append("username", username);
    data.append("password", password);
  
    return axios.post("/auth/token", data, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  }catch (error) {
    console.error("Erreur lors de la connexion :", error.response || error);
  }
};

export const register = (data) => {
  try{
    return axios.post("/users/", data, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  }catch (error) {
    console.error("Erreur lors de l'inscription :", error.response || error);
  }
};
