import { defineStore } from "pinia";
import { login } from "@/api/auth";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || null,
  }),
  actions: {
    async authenticate(username, password) {
      const response = await login(username, password);
      const { access_token } = response.data;
      this.token = access_token;
      localStorage.setItem("token", access_token);
    },
    logout() {
      this.token = null;
      localStorage.removeItem("token");
    },
    isAuthenticated() {
      return !!this.token;
    },
  },
});
