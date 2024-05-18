import $host from "./api";

export class authService {
  static async getArticle(search, date) {
    const { data } = await $host.get(`/content`, {
      params: {
        search,
        date
      },
    });
    return data;
  }

  static async getArticleById(search, date) {
    const { data } = await $host.get(`/article`, {
      params: {
        search,
        date
      },
    });
    return data;
  }
}
