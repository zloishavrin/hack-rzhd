import { jwtDecode } from "jwt-decode";
import { $host } from "./api";

export class authService {
  static async login(login, password) {
    const { data } = await $host.post(`/Auth/login`, { login, password });
    localStorage.setItem('token', data.token);
    return jwtDecode(data.token);
  };
}
