module.exports = (app) => {
  const router = require('express').Router();
  const news = require('../controllers');

  // Get news associated to a request id
  router.get('/news/:id', news.getNews);

  // Get news with specified id
  router.get('/news/detail/:id', news.getNewsDetail);

  app.use('/api/v1', router);
};
