<script setup>
import logoSVG from '../assets/logo.svg'
import { ref } from 'vue';

const login = ref('');
const password = ref('');

</script>

<template>
  <main>
    <div class="loginContainer">
      <div class="loginContent">
        <div class="loginFormContain">
          <div class="loginBoxImg">
            <img :src="logoSVG" alt="logo">
          </div>
          <div class="loginForm">
            <label>
              <p>Логин</p>
              <input type="text" class="loginInput" v-model.trim="login">
            </label>
            <label>
              <p>Пароль</p>
              <input type="password" class="loginInput" v-model.trim="password">
            </label>
          </div>
          <button class="loginBtn">Войти</button>
        </div>
      </div>
      <div class="loginImg"></div>
    </div>
  </main>
</template>

<style scoped>
.loginContainer {
  display: flex;
}

.loginContent {
  padding: 10vw;
}

.loginFormContain {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 28vw;
  height: 28vw;
  border: 0.1vw solid rgb(189, 189, 189);
  padding: 2.6vw;
  border-radius: 0.4vw;
}

.loginBoxImg {
  width: 10vw;
  height: 5vw;
  margin-bottom: 3vw;
}

.loginBoxImg img {
  width: 100%;
  height: 100%;
}

.loginForm label {
  display: flex;
  flex-direction: column;
  margin-bottom: 1vw;
}

.loginForm label p {
  font-weight: 500;
  font-size: 1.25vw;
}

.loginForm label:last-child {
  margin-bottom: 0;
}

.loginInput {
  border: 0.2vw solid rgb(189, 189, 189);
  width: 18vw;
  height: 3vw;
  padding: 0.5vw;
  border-radius: 0.4vw;
  transition: border 0.2s ease;
  margin-top: 0.5vw;
}

.loginInput:focus {
  border: 0.2vw solid rgb(255, 15, 0);
}

.loginBtn {
  box-sizing: border-box;
  border: 0.2vw solid rgb(255, 15, 0);
  border-radius: 0.4vw;
  background: rgb(255, 0, 0);
  color: #ffffff;
  padding: 0.5vw 3vw;
  text-transform: uppercase;
  font-size: 1.25vw;
  transition: all 0.2s ease;
  margin-top: 2.3vw;
}

.loginBtn:hover {
  background-color: #ffffff;
  color: rgb(255, 15, 0);
} 

.loginImg {
  position: relative;
  width: 60vw;
  height: 48vw;
  background-image: url('../assets/frameLogin.jpeg');
  background-size: cover;
  background-position: right center;
  filter: brightness(50%) opacity(90%) contrast(90%);
}

</style>