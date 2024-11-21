import { login } from "@/api/auth";

export const authenticateUser = async (username, password) => {
  const response = await login(username, password);
  const { access_token } = response.data;
  localStorage.setItem("token", access_token);
  return access_token;
};
