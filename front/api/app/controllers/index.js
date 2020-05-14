const mongoose = require('mongoose');
const db = require('../models');
const News = db.news;

module.exports = {
  // GET /news/:id
  getNews: (req, res) => {
    const id = req.params.id;
    const query = { 'request.id': { $eq: id } };
    News.find(query)
      .then((data) => {
        res.send({ news: data });
      })
      .catch((err) => {
        res.status(500).send({
          message: err.message || 'Some error ocurred while retrieving news.'
        });
      });
  },
  // GET /news/detail/:id
  getNewsDetail: (req, res) => {
    const id = req.params.id;
    const query = { _id: { $eq: id } };
    console.log(id);
    News.findById(new mongoose.Types.ObjectId(id))
      .then((data) => res.send({ news: data }))
      .catch((err) => {
        res.status(500).send({
          message:
            err.message || 'Some error ocurred while retrieving the news.'
        });
      });
  }
};
