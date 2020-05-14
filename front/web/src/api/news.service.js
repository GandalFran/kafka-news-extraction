import axios from 'axios';

const api = 'http://backend.novatrends.me:5000/api/v1/news';

class NewsService {
  getNews(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${api}/${id}`)
        .then(res => resolve(res))
        .catch(err => reject(err));
    });
  }

  getNewsDetail(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${api}/detail/${id}`)
        .then(res => resolve(res))
        .catch(err => reject(err));
    });
  }
}

export const newsService = new NewsService();
