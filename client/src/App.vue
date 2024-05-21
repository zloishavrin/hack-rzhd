<script setup>
import { useAuth } from './stores/AuthStore';
import Login from './views/Login.vue';
const auth = useAuth();


</script>

<template>
  <div class="wrapper">
    <main>
      <router-view v-if="auth.isAuth"/>
      <router-view v-else>
        <Login />
      </router-view>
    </main>
  </div>
</template>

<style scoped></style>
