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
    <Article/>
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
        <button 
          class="articleViolationBtn" 
          :class="{ articleViolationBtnMistake: isViolation }"
          @click="showPopup"
          >
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

.articleViolationBtn:hover{
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

.articleViolationBtnMistake:hover{
  background-color:rgb(255, 15, 0);
  border: 0.2vw solid rgb(255, 255, 255);
  border-radius: 0.4vw;
  color: rgb(255, 255, 255);
}
</style>