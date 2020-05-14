<template>
  <background-video>
    <b-jumbotron class="container">
      <!-- Loading news -->
      <div v-if="loadingNews">
        <loading-news />
      </div>

      <!-- News not found -->
      <div v-else-if="!loadingNews && news === undefined">
        <news404 />
      </div>

      <div v-else>
        <!-- HEADER -->
        <b-jumbotron :header="news.title">
          <h2 v-show="news.author">by {{ news.author }}</h2>
          <h4>{{ dateNews }}</h4>
          <h4>
            Sentiment:
            <b-badge pill :variant="badgeVariant()">
              {{ sentiment() }}
            </b-badge>
          </h4>
          <h4>Original News: <a :href="news.url">{{ news.url }}</a></h4>
          <hr/>
          <p align="justify">{{ news.content }}</p>
        </b-jumbotron>
      </div>
    </b-jumbotron>
  </background-video>
</template>

<script>
import moment from 'moment';
import BackgroundVideo from '../components/BackgroundVideo.vue';
import LoadingNews from '../components/LoadingNews.vue';
import News404 from '../components/News404.vue';
import { newsService } from '../api/news.service';
import { newsSentiment } from '../utils/news';

export default {
  name: 'NewsDetail',
  components: {
    BackgroundVideo,
    LoadingNews,
    News404
  },
  data: function() {
    return {
      loadingNews: true,
      news: undefined
    };
  },
  created: function() {
    newsService
      .getNewsDetail(this.$route.params.id)
      .then(res => {
        this.news = res.data.news;
        this.loadingNews = false;
        console.log(this.news);
      })
      .catch(err => {
        this.loadingNews = false;
        console.log(`Something went bad when fetching news. Error: ${err}`);
      });
  },
  computed: {
    dateNews: function() {
      return moment(new Date(this.news.date)).format('YYYY/MM/DD');
    }
  },
  methods: {
    sentiment: function() {
      return newsSentiment(this.news.sentiment.compound);
    },
    badgeVariant: function() {
      if (this.sentiment(this.news) === 'positive') {
        return 'success';
      } else if (this.sentiment(this.news) === 'negative') {
        return 'danger';
      } else {
        return 'secondary';
      }
    }
  }
};
</script>

<style>
p {
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased !important;
  -moz-font-smoothing: antialiased !important;
  text-rendering: optimizelegibility !important;
  letter-spacing: .03em;
}
</style>