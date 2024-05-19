<script setup>
import { onMounted, reactive } from 'vue';
import ArticleItem from './ArticleItem.vue';

// const props = defineProps({
//   articleList: Array,
// });

const articleList = reactive([
  {
    "title": "AUDI3",
    "date": "2023-01-03",
    "violation": false
  },
]);
</script>

<template>
  <ul class="articleList">
    <ArticleItem 
      v-for="item in articleList"
      :title="item.title"
      :date="item.date"
      :isViolation="violation"
    />
  </ul>
</template>
<style scoped>
.articleList {
  margin-top: 3vw;
  display: grid;
  grid-template-columns: repeat(4, 20vw);
  gap: 2vw;
  padding-bottom: 1vw;
}

@media (max-width: 1000px) {
  .articleList {
    margin-top: 3vw;
    display: grid;
    grid-template-columns: repeat(3, 27vw);
    gap: 2vw;
    padding-bottom: 1vw;
  }
}


@media (max-width: 720px) {
  .articleList {
    margin-top: 4vw;
    display: grid;
    grid-template-columns: repeat(2, 43vw);
    gap: 3vw;
    padding-bottom: 2vw;
  }
}

@media (max-width: 500px) {
  .articleList {
    margin-top: 7vw;
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 5vw;
    padding-bottom: 5vw;
  }
}
</style>