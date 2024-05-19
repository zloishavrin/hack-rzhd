<script setup>
import { ref } from 'vue';
import Popup from './Popup.vue';
import Article from './Article.vue';


const isShowPopup = ref(false);

const showPopup = () => {
  isShowPopup.value = true;
}

const closePopup = () => {
  isShowPopup.value = false;
}


defineProps({
  title: String,
  date: String,
  isViolation: Boolean
})


</script>
<template>
  <Popup :show="isShowPopup" @closePopup="closePopup">
    <Article />
  </Popup>
  <li class="articleItem" :class="{ articleItemMistake: isViolation }">
    <div class="articleContain">
      <p class="articleTitle">{{ title }}</p>
      <div class="articleDateContain">
        <p class="articleDateTitle">Дата</p>
        <p class="articleDate">{{ date }}</p>
      </div>
      <div class="articleViolation">
        <p v-if="isViolation">Обнаружено нарушение</p>
        <p v-else>Нарушение не обнаружено</p>
        <button class="articleViolationBtn" :class="{ articleViolationBtnMistake: isViolation }" @click="showPopup">
          Открыть</button>
      </div>
    </div>
  </li>
</template>
<style scoped>
.articleItem {
  padding: 1vw 1.5vw;
  box-sizing: border-box;
  border: 0.2vw solid rgb(255, 15, 0);
  border-radius: 0.4vw;
  background: rgb(255, 255, 255);
  font-size: 1.15vw;
}

.articleContain {
  display: flex;
  flex-direction: column;
}

.articleTitle {
  text-align: center;
  margin-bottom: 1.5vw;
}

.articleDateContain {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5vw;
}

.articleViolation {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.articleViolation p {
  width: 9vw;
}

.articleViolationBtn {
  border: 0.2vw solid rgb(255, 15, 0);
  border-radius: 0.4vw;
  background: rgb(255, 15, 0);
  color: #ffffff;
  padding: 0.5vw 1vw;
  font-size: 1vw;
  transition: all 0.3s ease;
}

.articleViolationBtn:hover {
  background-color: #ffffff;
  color: rgb(255, 15, 0);
}

.articleItemMistake {
  background-color: rgb(255, 15, 0);
  color: #ffffff;
}

.articleViolationBtnMistake {
  background-color: #ffffff;
  color: rgb(255, 15, 0);
}

.articleViolationBtnMistake:hover {
  background-color: rgb(255, 15, 0);
  border: 0.2vw solid rgb(255, 255, 255);
  border-radius: 0.4vw;
  color: rgb(255, 255, 255);
}


@media (max-width: 1000px) {
  .articleItem {
    padding: 1.5vw 2vw;
    border-radius: 0.7vw;
    font-size: 1.55vw;
  }

  .articleTitle {
    margin-bottom: 2.5vw;
  }

  .articleDateContain {
    margin-bottom: 2.5vw;
  }

  .articleViolation p {
    width: 11vw;
  }

  .articleViolationBtn {
    padding: 1vw 1.5vw;
    font-size: 1.5vw;
    border-radius: 0.7vw;
  }
}

@media (max-width: 720px) {
  .articleItem {
    padding: 2vw 2.5vw;
    border-radius: 1vw;
    font-size: 2.5vw;
    border: 0.4vw solid rgb(255, 15, 0);
  }

  .articleTitle {
    margin-bottom: 3.5vw;
  }

  .articleDateContain {
    margin-bottom: 3.5vw;
  }

  .articleViolation p {
    width: 17vw;
  }

  .articleViolationBtn {
    padding: 1.5vw 2vw;
    font-size: 1.9vw;
    border-radius: 0.9vw;
  }
}

@media (max-width: 500px) {
  .articleItem {
    padding: 4vw;
    border-radius: 2vw;
    font-size: 5.6vw;
    border: 0.6vw solid rgb(255, 15, 0);
  }

  .articleTitle {
    margin-bottom: 6.5vw;
  }

  .articleDateContain {
    margin-bottom: 7.6vw;
  }

  .articleViolation p {
    width: 40vw;
  }

  .articleViolationBtn {
    border: 0.6vw solid rgb(255, 15, 0);
    padding: 1.5vw 2vw;
    font-size: 5vw;
    border-radius: 1.2vw;
  }

  .articleViolationBtnMistake:hover {
    border: 0.6vw solid rgb(255, 255, 255);
    border-radius: 1.2vw;
  }
}
</style>