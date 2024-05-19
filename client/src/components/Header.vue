<script setup>
import logoSVG from '../assets/logo.svg'
import { ref } from 'vue';
import { useAuth } from '@/stores/AuthStore';

const auth = useAuth();

</script>

<template>
  <header class="header">
    <div class="headerContent">
      <div class="headerBoxImg">
        <img :src="logoSVG" alt="logo">
      </div>
      <div class="headerUser">
        <p class="headerUserName">{{ auth.user }}</p>
        <button class="headerBtnExit" @click="auth.logout">
          <svg width="47.000000" height="47.000000" viewBox="0 0 47 47" fill="none" xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink">
            <desc>
              Created with Pixso.
            </desc>
            <defs>
              <clipPath id="clip2_79">
                <rect id="exit-svgrepo-com (2) 1" width="47.000000" height="47.000000" fill="white" fill-opacity="0" />
              </clipPath>
            </defs>
            <rect id="exit-svgrepo-com (2) 1" width="47.000000" height="47.000000" fill="#FFFFFF" fill-opacity="0" />
            <g clip-path="url(#clip2_79)">
              <path id="rect348"
                d="M10.18 0C4.59 0 0 4.59 0 10.18L0 36.81C0 42.4 4.59 47 10.18 47L23.62 47C28.81 47 33.14 43.03 33.73 37.99L27.37 37.99C26.89 39.61 25.43 40.73 23.62 40.73L10.18 40.73C7.95 40.73 6.26 39.04 6.26 36.81L6.26 10.18C6.26 7.95 7.95 6.26 10.18 6.26L23.62 6.26C25.43 6.26 26.89 7.38 27.37 9L33.73 9C33.14 3.96 28.81 0 23.62 0L10.18 0Z"
                fill="#FFFFFF" fill-opacity="1.000000" fill-rule="nonzero" />
              <path id="path1073"
                d="M37.35 14.09C36.94 14.09 36.53 14.18 36.15 14.33C35.77 14.49 35.42 14.72 35.13 15.01C34.84 15.3 34.61 15.65 34.45 16.03C34.3 16.41 34.22 16.82 34.22 17.23C34.22 17.64 34.3 18.05 34.45 18.43C34.61 18.81 34.84 19.15 35.13 19.44L36.05 20.36L12.82 20.36C11.99 20.36 11.19 20.69 10.6 21.28C10.02 21.87 9.69 22.66 9.69 23.49C9.69 24.33 10.02 25.12 10.6 25.71C11.19 26.3 11.99 26.63 12.82 26.63L36.05 26.63L35.13 27.55C34.84 27.84 34.61 28.18 34.45 28.56C34.3 28.94 34.22 29.35 34.22 29.76C34.22 30.17 34.3 30.58 34.45 30.96C34.61 31.34 34.84 31.69 35.13 31.98C35.42 32.27 35.77 32.5 36.15 32.66C36.53 32.81 36.94 32.9 37.35 32.9C37.76 32.9 38.17 32.81 38.55 32.66C38.93 32.5 39.27 32.27 39.56 31.98L45.27 26.28C45.78 26.02 46.22 25.62 46.52 25.13C46.83 24.64 46.99 24.07 47 23.49C46.99 22.91 46.83 22.33 46.52 21.84C46.21 21.34 45.76 20.94 45.23 20.68L39.56 15.01C39.27 14.72 38.93 14.49 38.55 14.33C38.17 14.18 37.76 14.09 37.35 14.09Z"
                fill="#FFFFFF" fill-opacity="1.000000" fill-rule="nonzero" />
            </g>
          </svg>
        </button>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  padding: 2vw 0;
}

.headerBoxImg {
  width: 10vw;
  height: 5vw;
}

.headerBoxImg img {
  width: 100%;
  height: 100%;
}

.headerContent {
  display: flex;
  justify-content: space-between;
}

.headerUser {
  display: flex;
  align-items: center;
}

.headerUserName {
  font-size: 1.25vw;
  font-weight: 500;
  margin-right: 2vw;
}

.headerBtnExit {
  border: 0.2vw solid rgb(255, 15, 0);
  background-color: rgb(255, 15, 0);
  padding: 0.7vw;
  border-radius: 0.5vw;
  text-align: center;
  transition: all 0.3s ease;
}

.headerBtnExit svg {
  display: block;
  width: 2vw;
  height: 2vw;
  margin: 0 auto;
  transition: all 0.3s ease;
}

.headerBtnExit svg path {
  transition: all 0.3s ease;
}

.headerBtnExit:hover {
  background-color: #ffffff;
}

.headerBtnExit:hover svg path {
  fill: rgb(255, 15, 0);
  fill-opacity: "1";
}

@media (max-width: 1000px) {
  .header {
    padding: 4vw 0;
  }

  .headerBoxImg {
    width: 13vw;
    height: 8vw;
  }

  .headerContent {
    display: flex;
    justify-content: space-between;
  }

  .headerUser {
    display: flex;
    align-items: center;
  }

  .headerUserName {
    font-size: 1.75vw;
    font-weight: 500;
    margin-right: 4vw;
  }

  .headerBtnExit {
    border: 0.2vw solid rgb(255, 15, 0);
    padding: 1vw;
    border-radius: 0.5vw;
  }

  .headerBtnExit svg {
    width: 3vw;
    height: 3vw;
  }
}


@media (max-width: 720px) {
  .header {
    padding: 4vw 0;
  }

  .headerBoxImg {
    width: 17vw;
    height: 12vw;
  }

  .headerUserName {
    font-size: 3vw;
    font-weight: 500;
    margin-right: 5vw;
  }

  .headerBtnExit {
    border: 0.2vw solid rgb(255, 15, 0);
    padding: 1vw;
    border-radius: 0.5vw;
  }

  .headerBtnExit svg {
    width: 4vw;
    height: 4vw;
  }
}

@media (max-width: 500px) {
  .headerContent {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .headerBoxImg {
    width: 27vw;
    height: 22vw;
  }

  .headerUserName {
    font-size: 7vw;
    font-weight: 500;
    margin-right: 6vw;
  }

  .headerBtnExit {
    border: 0.4vw solid rgb(255, 15, 0);
    padding: 1.6vw;
    border-radius: 1.2vw;
  }

  .headerBtnExit svg {
    width: 6vw;
    height: 6vw;
  }

}
</style>