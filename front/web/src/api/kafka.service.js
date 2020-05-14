import axios from 'axios';

const api = 'http://backend.novatrends.me:20000/etl/kafka';

class KafkaService {
  requestNews(keywords) {
    const formData = new FormData();
    formData.set('q', keywords);

    return new Promise((resolve, reject) => {
      axios
        .post(`${api}`, formData)
        .then(res => resolve(res))
        .catch(err => reject(err));
    });
  }
}

export const kafkaService = new KafkaService();
