import { jwtDecode } from "jwt-decode";
import { $authHost } from "./api";

export class authService {
  static async login(login, password) {
    const { data } = await $authHost.post(`/login`, { login, password });
    localStorage.setItem('token', data);
    return jwtDecode(data);
  };

  static async logout(token) {
    const { data } = await $authHost.post(`/logout`, { token });
    localStorage.removeItem('token');
    return data;
  };
}
