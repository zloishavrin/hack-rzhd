import { defineStore } from "pinia";
import { authService } from "@/service/authService";

export const useAuth = defineStore("auth", {
  state: () => ({
    errorReg: "",
    errorLogin: "",
    isAuth: true,
    isLoading: true,
    user: {},
  }),
  getters: {},
  actions: {
    async login({ login, password }) {
      try {
        const data = await authService.login(login, password);
        this.user = data;
        this.isAuth = true;
        this.errorLogin = "";
      } catch (e) {
        this.errorLogin = e.message;
      } finally {
        this.isLoading = false;
      }
    },

    async logout() {
      const token = localStorage.getItem("token");
      await authService.logout(token);
      this.user = {};
      this.isAuth = false;
      this.errorLogin = "";
      this.errorReg = "";
    },
  },
  persist: true,
});
