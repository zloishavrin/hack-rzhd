<script setup>
  import { onMounted, reactive } from 'vue';
  import ArticleItem from './ArticleItem.vue';

  const articleList = reactive([
  {
    "название": "Проект 1",
    "дата": "2023-01-01",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 2",
    "дата": "2023-01-02",
    "обнаружено_нарушение": true
  },
  {
    "название": "Проект 3",
    "дата": "2023-01-03",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 1",
    "дата": "2023-01-01",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 2",
    "дата": "2023-01-02",
    "обнаружено_нарушение": true
  },
  {
    "название": "Проект 3",
    "дата": "2023-01-03",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 1",
    "дата": "2023-01-01",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 2",
    "дата": "2023-01-02",
    "обнаружено_нарушение": true
  },
  {
    "название": "Проект 3",
    "дата": "2023-01-03",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 2",
    "дата": "2023-01-02",
    "обнаружено_нарушение": true
  },
  {
    "название": "Проект 3",
    "дата": "2023-01-03",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 2",
    "дата": "2023-01-02",
    "обнаружено_нарушение": true
  },
  {
    "название": "Проект 3",
    "дата": "2023-01-03",
    "обнаружено_нарушение": false
  },
  {
    "название": "Проект 2",
    "дата": "2023-01-02",
    "обнаружено_нарушение": true
  },
  {
    "название": "Проект 3",
    "дата": "2023-01-03",
    "обнаружено_нарушение": false
  },
]);

  // async function fetchData(){
  //   const resp = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=10');
  //   const data = await resp.json();
  //   items.values = data;
  //   console.log(data);
  // }

  // onMounted(fetchData);

</script>
<template>
  <ul class="articleList">
    <ArticleItem 
      v-for="item in articleList"
      :title="item.название"
      :date="item.дата"
      :isViolation="item.обнаружено_нарушение"
    />
  </ul>
</template>
<style scoped>
  .articleList{
    margin-top: 3vw;
    display: grid;
    grid-template-columns: repeat(4, 20vw);
    gap: 2vw;
    padding-bottom: 1vw;
  }
</style>