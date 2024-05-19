import { $authHost } from "./api";

export class articleService {
  static async getArticle(search) {
    const { data } = await $authHost.get(`/Article/content`, {
      params: {
        search
      },
    });
    return data;
  }

  static async getArticles() {
    const { data } = await $authHost.get(`/Article/articles`);
    return data;
  }

  static async getArticleById(search, date) {
    const { data } = await $authHost.get(`/Article/article`, {
      params: {
        search,
        date
      },
    });
    return data;
  }
}
