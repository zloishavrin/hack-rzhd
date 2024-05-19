<script setup>
import logoSVG from '../assets/logo.svg'
import { ref } from 'vue';
import { useAuth } from '@/stores/AuthStore';

const login = ref('');
const password = ref('');

const auth = useAuth();

const sumbitForm = async () => {
  try {
    await auth.login({ login: login.value, password: password.value });
    if (auth.errorLogin.length === 0) {
      router.push({ name: 'home' });
    }
  } catch (error) {
    console.log(error);
  }
}


const validateForm = () => {
  const isAlphaNumeric = /^[0-9A-ZА-ЯЁ]+$/i.test(login.value);
  if (!isAlphaNumeric) {
    alert('Заполните логин!');
  } else if (password.value == '') {
    alert('Заполните пароль!');
  } else {
    sumbitForm();
  }
}

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
          <button class="loginBtn" @click="validateForm">Войти</button>
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
  height: 100vh;
  background-image: url('../assets/frameLogin.jpeg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: right center;
  filter: brightness(50%) opacity(90%) contrast(90%);
}


@media (max-width: 1200px) {
  .loginFormContain {
    width: 32vw;
    height: 32vw;
    border: 0.1vw solid rgb(189, 189, 189);
    padding: 2.6vw;
    border-radius: 0.4vw;
  }

  .loginBoxImg {
    width: 12vw;
    height: 7vw;
    margin-bottom: 4vw;
  }

  .loginForm label {
    margin-bottom: 1vw;
  }

  .loginForm label p {
    font-weight: 500;
    font-size: 1.7vw;
  }

  .loginForm label:last-child {
    margin-bottom: 0;
  }

  .loginInput {
    width: 20vw;
    height: 3.5vw;
    padding: 0.75vw;
    border-radius: 0.4vw;
    transition: border 0.2s ease;
    margin-top: 0.7vw;
  }

  .loginBtn {
    padding: 0.5vw 3vw;
    font-size: 1.7vw;
    margin: 2.6vw 0;
  }
}

@media (max-width: 1000px) {
  .loginContainer {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .loginFormContain {
    width: 45vw;
    height: 45vw;
    border: 0.1vw solid rgb(189, 189, 189);
    padding: 2.6vw;
    border-radius: 0.6vw;
  }

  .loginBoxImg {
    width: 17vw;
    height: 11vw;
    margin-bottom: 4vw;
  }

  .loginForm label {
    margin-bottom: 2vw;
  }

  .loginForm label p {
    font-size: 2.5vw;
  }

  .loginInput {
    font-size: 2.5vw;
    width: 27vw;
    height: 5vw;
    padding: 1vw;
    border-radius: 0.8vw;
    transition: border 0.2s ease;
    margin-top: 0.7vw;
  }

  .loginBtn {
    padding: 0.5vw 3vw;
    font-size: 2.5vw;
    margin: 2.6vw 0;
    border-radius: 0.8vw;
  }

  .loginImg {
    display: none;
  }
}

@media (max-width: 720px) {
  .loginFormContain {
    width: 65vw;
    height: 60vw;
    border: 0.1vw solid rgb(189, 189, 189);
    padding: 2.6vw;
    border-radius: 0.8vw;
  }

  .loginBoxImg {
    width: 24vw;
    height: 18vw;
    margin-bottom: 6vw;
  }

  .loginForm label {
    margin-bottom: 4vw;
  }

  .loginForm label p {
    font-size: 4vw;
  }

  .loginInput {
    font-size: 4vw;
    border: 0.4vw solid rgb(189, 189, 189);
    width: 40vw;
    height: 6.5vw;
    padding: 1.5vw;
    border-radius: 1vw;
    margin-top: 0.7vw;
  }

  .loginInput:focus {
    border: 0.4vw solid rgb(255, 15, 0);
  }

  .loginBtn {
    border: 0.4vw solid rgb(255, 15, 0);
    padding: 0.5vw 3vw;
    font-size: 4vw;
    margin: 4vw 0;
    border-radius: 1vw;
  }

  .loginImg {
    display: none;
  }
}

@media (max-width: 500px) {

  .loginContainer {
    display: flex;
    align-items: flex-start;
  }

  .loginFormContain {
    width: 100vw;
    height: 100vh;
    border: none;
    padding: 2.6vw;
    border-radius: 0.8vw;
  }

  .loginContent {
    padding: 0;
    height: 100%;
  }

  .loginBoxImg {
    width: 45vw;
    height: 35vw;
    margin-bottom: 0;
    margin: 15vw 0;
  }

  .loginForm label {
    margin-bottom: 12vw;
    text-align: center;
  }

  .loginForm label p {
    font-size: 8vw;
  }

  .loginInput {
    font-size: 8vw;
    border: 0.6vw solid rgb(189, 189, 189);
    width: 80vw;
    padding: 7vw 2vw;
    border-radius: 2vw;
    margin-top: 3vw;
  }

  .loginInput:focus {
    border: 0.6vw solid rgb(255, 15, 0);
  }

  .loginBtn {
    border: 0.6vw solid rgb(255, 15, 0);
    padding: 1vw 5vw;
    font-size: 7.5vw;
    margin: 10vw 0;
    border-radius: 2vw;
  }

  .loginImg {
    display: none;
  }
}
</style>