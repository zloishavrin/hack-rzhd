import { defineStore } from "pinia";
import { authService } from "@/service/authService";

export const useAuth = defineStore("auth", {
  state: () => ({
    errorLogin: "",
    isAuth: false,
    isLoading: true,
    user: {},
  }),
  getters: {},
  actions: {
    async login({ login, password }) {
      try {
        const data = await authService.login(login, password);
        console.log(data);
        this.user = data.sub;
        this.isAuth = true;
        this.errorLogin = "";
      } catch (e) {
        this.errorLogin = e.message;
      } finally {
        this.isLoading = false;
      }
    },

    async logout() {
      localStorage.removeItem("token");
      this.user = {};
      this.isAuth = false;
      this.errorLogin = "";
      this.errorReg = "";
    },
  },
  persist: true,
});
