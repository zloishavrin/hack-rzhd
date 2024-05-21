import axios from "axios";

export const API_URL = 'http://95.163.222.110:8080/api';

const $host = axios.create({
  baseURL: API_URL,
  headers: {
    "Access-Control-Allow-Origin": "*"
  }
})

const $authHost = axios.create({
  baseURL: API_URL,
  headers: {
    "Access-Control-Allow-Origin": "*"
  }
})

const authInterceptor = config => {
  config.headers.authorization = `Bearer ${localStorage.getItem('token')}`
  return config
}

$authHost.interceptors.request.use(authInterceptor)

export {
  $host,
  $authHost
}