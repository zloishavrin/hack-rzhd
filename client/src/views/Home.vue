<script setup>
import Header from '@/components/Header.vue';
import ArticleList from '@/components/ArticleList.vue';
import { ref, onUnmounted } from 'vue';

const articleSearch = ref('');
const articleDate = ref('');

const clearSearchInput = () => {
  articleSearch.value = '';
}

const clearDateInput = () => {
  articleDate.value = '';
}

onUnmounted(clearDateInput);

</script>

<template>
  <div class="container">
    <Header />
    <div class="articleSearch">
      <input type="text" v-model.trim="articleSearch" class="articleInputSearch" placeholder="Поиск"
        @blur="clearSearchInput" />
      <div class="dateBox">
        <input type="date" v-model.trim="articleDate" class="articleInputDate">
      </div>
    </div>
    <ArticleList />
  </div>
</template>

<style scoped>
.articleSearch {
  display: flex;
  align-items: center;
}

.articleInputSearch {
  border: 0.2vw solid rgb(189, 189, 189);
  width: 60vw;
  padding: 1vw;
  height: 4vw;
  border-radius: 0.4vw;
  margin-right: 3vw;
  font-size: 1.25vw;
  transition: border 0.2s ease;
}

.articleInputSearch:focus {
  border: 0.2vw solid rgb(255, 15, 0);
}

.dateBox {
  border: 0.2vw solid rgb(189, 189, 189);
  padding: 1vw 0.5vw;
  border-radius: 0.5vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.articleInputDate {
  font-size: 1.25vw;
}


@media (max-width: 1000px) {
  .articleInputSearch {
    padding: 1.2vw;
    height: 5vw;
    border-radius: 0.7vw;
    margin-right: 4vw;
    font-size: 1.7vw;
  }

  .dateBox {
    padding: 1.2vw 0.8vw;
    border-radius: 0.7vw;
  }

  .articleInputDate {
    font-size: 1.7vw;
  }
}

@media (max-width: 720px) {
  .articleInputSearch {
    border: 0.4vw solid rgb(189, 189, 189);
    padding: 1.7vw;
    width: 75vw;
    height: 7vw;
    border-radius: 0.9vw;
    margin-right: 4vw;
    font-size: 2.5vw;
  }

  .articleInputSearch:focus {
    border: 0.4vw solid rgb(255, 15, 0);
  }

  .dateBox {
    border: 0.4vw solid rgb(189, 189, 189);
    padding: 1.7vw 1.2vw;
    border-radius: 0.9vw;
  }

  .articleInputDate {
    font-size: 2.5vw;
  }
}

@media (max-width: 500px) {

  .articleSearch {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .articleInputSearch {
    border: 0.6vw solid rgb(189, 189, 189);
    width: 100%;
    padding: 5vw 2vw;
    border-radius: 2vw;
    margin-right: 0;
    margin-bottom: 4vw;
    font-size: 5vw;
  }

  .articleInputSearch:focus {
    border: 0.6vw solid rgb(255, 15, 0);
  }

  .dateBox {
    border: 0.6vw solid rgb(189, 189, 189);
    padding: 1.7vw 3vw;
    border-radius: 2vw;
  }

  .articleInputDate {
    font-size: 5vw;
  }
}
</style>