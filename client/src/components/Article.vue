<script setup>
import downloadSVG from '../assets/download.svg'

</script>
<template>
  <div class="articleContainer">
    <div class="articleAbout">
      <p class="articleTitle">Название файла</p>
      <a href="https://www.susu.ru/" class="articleLink" target="_blank">
        <img :src="downloadSVG" alt="download" class="articleDownlSVG">
      </a>
    </div>
    <div class="articleDateContain">
      <p>Дата</p>
      <p>18.01.2024 15:35</p>
    </div>
    <div class="articleDuration">
      <p>Продолжительность</p>
      <p>3:35</p>
    </div>
    <div class="articleViolation">
      <p>Нарушения</p>
      <p>23</p>
    </div>
    <ul class="articleViolationList">
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Аеае</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
      <li class="articleViolationItem">
        <p class="articleViolationNumber">Пункт 2</p>
        <p class="articleViolationText">Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные
          тексты.</p>
      </li>
    </ul>
  </div>
</template>
<style scoped>
.articleContainer {
  padding-top: 5vw;
  padding-left: 1vw;
  padding-right: 1vw;
  display: flex;
  flex-direction: column;
  font-size: 1.25vw;
}

.articleAbout {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2vw;
}

.articleTitle {
  font-size: 1.7vw;
}

.articleLink {
  width: 2.5vw;
  height: 2.5vw;
  border-radius: 0.4vw;
  background: rgb(255, 15, 0);
}

.articleDownlSVG {
  width: 100%;
  height: 100%;
}

.articleDateContain,
.articleDuration {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2.25vw;
}

.articleViolation {
  display: flex;
  align-items: center;
  margin-bottom: 2.25vw;
}

.articleViolation p:last-child {
  margin-left: 0.7vw;
  color: rgba(150, 9, 0, 0.93);
}

.articleViolationList {
  overflow-y: auto;
  height: 27.66vw;
}

.articleViolationList::-webkit-scrollbar {
  width: 0.4vw;
}

.articleViolationList::-webkit-scrollbar-track {
  background: transparent;
}

.articleViolationList::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.4vw;
}

.articleViolationItem {
  border: 0.1vw solid rgb(128, 128, 128);
  border-radius: 0.4vw;
  margin-bottom: 1vw;
  margin-right: 0.5vw;
}

.articleViolationNumber {
  color: #ffffff;
  padding: 1vw;
  background: rgb(255, 15, 0);
  margin-bottom: 1vw;
  border-top-left-radius: 0.4vw;
  border-top-right-radius: 0.4vw;
}

.articleViolationText {
  padding: 1vw;
}

@media (max-width: 1200px) {
  .articleViolationList {
    height: 37.66vw;
  }
}

@media (max-width: 1000px) {
  .articleViolationList {
    height: 42.66vw;
  }
}

/* --------- 780 --------------*/

@media (max-width: 780px) {
  .articleContainer {
    padding-top: 10vw;
    padding-left: 2.5vw;
    padding-right: 2.5vw;
    display: flex;
    flex-direction: column;
    font-size: 2.25vw;
  }

  .articleAbout {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2.5vw;
  }

  .articleTitle {
    font-size: 2.7vw;
  }

  .articleLink {
    width: 4.5vw;
    height: 4.5vw;
    border-radius: 0.4vw;
    background: rgb(255, 15, 0);
  }

  .articleDownlSVG {
    width: 100%;
    height: 100%;
  }

  .articleDateContain,
  .articleDuration {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 3.25vw;
  }

  .articleViolation {
    display: flex;
    align-items: center;
    margin-bottom: 3.25vw;
  }

  .articleViolation p:last-child {
    margin-left: 1.2vw;
    color: rgba(150, 9, 0, 0.93);
  }

  .articleViolationList {
    height: 44.66vw;
  }

  .articleViolationList::-webkit-scrollbar {
    width: 1.4vw;
  }

  .articleViolationItem {
    border: 0.5vw solid rgb(128, 128, 128);
    border-radius: 1.4vw;
    margin-bottom: 3vw;
    margin-right: 1.5vw;
  }

  .articleViolationNumber {
    padding: 3vw;
    margin-bottom: 3vw;
    border-top-left-radius: 1vw;
    border-top-right-radius: 1vw;
  }

  .articleViolationText {
    padding: 3vw;
  }
}


@media (max-width: 680px) {
  .articleViolationList {
    height: 57.66vw;
  }
}

/* --------- 500 --------------*/

@media (max-width: 500px) {
  .articleContainer {
    padding-top: 15vw;
    padding-left: 4vw;
    padding-right: 4vw;
    display: flex;
    flex-direction: column;
    font-size: 3.25vw;
  }

  .articleAbout {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 4.5vw;
  }

  .articleTitle {
    font-size: 3.7vw;
  }

  .articleLink {
    width: 6.5vw;
    height: 6.5vw;
    border-radius: 0.4vw;
    background: rgb(255, 15, 0);
  }

  .articleDownlSVG {
    width: 100%;
    height: 100%;
  }

  .articleDateContain,
  .articleDuration {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 5.25vw;
  }

  .articleViolation {
    display: flex;
    align-items: center;
    margin-bottom: 5.25vw;
  }

  .articleViolation p:last-child {
    margin-left: 1.7vw;
    color: rgba(150, 9, 0, 0.93);
  }

  .articleViolationList {
    padding: 0 5vw;
    height: 58vh;
  }

  .articleViolationList::-webkit-scrollbar {
    width: 1.4vw;
  }

  .articleViolationItem {
    border: 0.5vw solid rgb(128, 128, 128);
    border-radius: 1.4vw;
    margin-bottom: 3vw;
    margin-right: 1.5vw;
  }

  .articleViolationNumber {
    padding: 3vw;
    margin-bottom: 3vw;
    border-top-left-radius: 1vw;
    border-top-right-radius: 1vw;
  }

  .articleViolationText {
    padding: 3vw;
  }
}
</style>