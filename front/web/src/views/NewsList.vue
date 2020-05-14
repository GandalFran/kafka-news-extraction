<template>
  <background-video>
    <b-jumbotron class="container">
      <!-- Loading news -->
      <div v-if="loadingNews">
        <loading-news />
      </div>

      <!-- News not found -->
      <div v-else-if="!loadingNews && news.length === 0">
        <news404 />
      </div>

      <!-- News loaded -->
      <div v-else>
        <!-- HEADER -->
        <b-jumbotron header="News Found" :lead="`Keywords: ${keywords}`">
        </b-jumbotron>

        <!-- NEWS -->
        <b-jumbotron>
          <b-row
            v-for="(newsRow, rowIndex) in newsPage"
            :key="`row${rowIndex}`"
            style="margin-bottom: 25px;"
          >
            <b-col
              v-for="(news, newsIndex) in newsRow"
              :key="`news${newsIndex}`"
            >
              <b-card
                :title="news.title"
                tag="article"
                style="max-width: 20rem;"
                class="mb-2 news-card"
                align="left"
              >
                <p v-show="news.author">by {{ news.author }}</p>
                <div class="bottom-div">
                  <router-link :to="`/news/detail/${news._id}/`">
                    <b-button size="sm" class="news-button"
                      >Go to the news</b-button
                    ></router-link
                  >
                  <b-badge
                    class="news-badge"
                    pill
                    :variant="badgeVariant(news)"
                  >
                    {{ sentiment(news) }}
                  </b-badge>
                </div>
              </b-card>
            </b-col>
          </b-row>
          <b-pagination
            v-model="currentPage"
            :total-rows="totalNews"
            :per-page="perPage"
            align="center"
          ></b-pagination>
        </b-jumbotron>
      </div>
    </b-jumbotron>
  </background-video>
</template>

<script>
import BackgroundVideo from '../components/BackgroundVideo.vue';
import LoadingNews from '../components/LoadingNews.vue';
import News404 from '../components/News404.vue';
import { newsService } from '../api/news.service';
import { newsSentiment } from '../utils/news';

const NEWS_PER_PAGE = 9;
const NEWS_PER_ROW = 3;

export default {
  name: 'NewsList',
  components: {
    BackgroundVideo,
    LoadingNews,
    News404
  },
  data: function() {
    return {
      perPage: NEWS_PER_PAGE,
      currentPage: 1,
      news: [],
      totalNews: 0,
      loadingNews: true,
      keywords: '',
      newsPage: [],
      rowsInThisPage: 0
    };
  },
  created: function() {
    // Retrieve news
    newsService
      .getNews(this.$route.params.id)
      .then(res => {
        this.news = this.news.concat(res.data.news);
        this.totalNews = this.news.length;
        if (this.totalNews > 0) {
          this.keywords = this.news[0].request.keywords;
        }
        // Get the news from this page
        this.newsForThisPage();
        this.loadingNews = false;
      })
      .catch(err => console.log('err', err));
  },
  watch: {
    currentPage: function() {
      // Update news for this page
      this.newsForThisPage();
    }
  },
  methods: {
    newsForThisPage: function() {
      const start = (this.currentPage - 1) * NEWS_PER_PAGE;
      const end = start + NEWS_PER_PAGE;
      const newsPage = this.news.slice(start, end);
      for (let i = 0; i < NEWS_PER_ROW; i++) {
        const rowStart = i * 3;
        const rowEnd = rowStart + NEWS_PER_ROW;
        this.newsPage[i] = newsPage.slice(rowStart, rowEnd);
      }
    },
    sentiment: function(news) {
      return newsSentiment(news.sentiment.compound);
    },
    badgeVariant: function(news) {
      if (this.sentiment(news) === 'positive') {
        return 'success';
      } else if (this.sentiment(news) === 'negative') {
        return 'danger';
      } else {
        return 'secondary';
      }
    }
  }
};
</script>

<style>
.news-card {
  height: 100%;
}

.bottom-div {
  position: absolute;
  bottom: 0px;
  margin-bottom: 10px;
}

.news-badge {
  float: right;
  margin-left: 50px;
}

.loading-spinner {
  margin-top: 100px;
}
</style>
