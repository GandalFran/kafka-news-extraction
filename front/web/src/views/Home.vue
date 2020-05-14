<template>
  <div class="home">
    <background-video>
      <b-jumbotron class="centered">
        <div>
          <img
            class="logo"
            src="https://img.icons8.com/cute-clipart/512/000000/news.png"
            alt="logo"
          />
          <h1 class="title">News scraping and sentimental analysis</h1>
          <h5>
            A small application to scrape web pages and perform it sentiment
            analysis.
          </h5>
        </div>
        <div v-if="!loading && !redirecting">
          <b-input-group class="mt-3">
            <b-form-tags v-model="topics"></b-form-tags>
            <b-button
              variant="info"
              @click="onClickSearch"
              :disabled="topics.length === 0"
              >Search</b-button
            >
          </b-input-group>
        </div>
        <div v-else-if="loading && !redirecting">
          <h1>Kafkating things...</h1>
          <b-spinner></b-spinner>
        </div>
        <div v-else>
          <h1>Redirecting you to the news found...</h1>
        </div>
      </b-jumbotron>
    </background-video>
  </div>
</template>

<script>
import BackgroundVideo from '../components/BackgroundVideo.vue';
import { kafkaService } from '../api/kafka.service';

export default {
  name: 'Home',
  components: {
    BackgroundVideo
  },
  data: function() {
    return {
      topics: [],
      loading: false,
      redirecting: false
    };
  },
  methods: {
    onClickSearch: function() {
      this.loading = true;
      kafkaService
        .requestNews(this.topics.join(' '))
        .then(res => {
          this.loading = false;
          this.redirecting = true;
          setTimeout(() => {
            this.$router.push(`/news/${res.data.id}`);
            this.redirecting = false;
          }, 5000);
        })
        .catch(err => {
          this.loading = false;
          console.log(
            `An error has ocurred when requesting kafka etl. Err: ${err}`
          );
        });
    }
  }
};
</script>

<style>
.centered {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(233, 236, 239, 0.8);
}

.logo {
  height: 128px;
  width: 128px;
}
</style>
