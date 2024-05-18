import axios from "axios";

export const API_URL = 'http://localhost:7070';

const $host = axios.create({
  baseURL: API_URL
})

const $authHost = axios.create({
  baseURL: API_URL
})

const authInterceptor = config => {
  config.headers.authorization = `${localStorage.getItem('token')}`
  return config
}

$authHost.interceptors.request.use(authInterceptor)

export {
  $host,
  $authHost
}