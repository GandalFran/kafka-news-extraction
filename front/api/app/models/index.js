const mongoose = require('mongoose');
const config = require('../config/db.config');

const db = {};
db.mongoose = mongoose;
db.url = config.url;
db.news = require('./news.model')(mongoose);

module.exports = db;
