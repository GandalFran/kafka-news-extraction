module.exports = (mongoose) => {
  const schema = mongoose.Schema({
    date: Date,
    request: {
      keywords: String,
      id: String
    },
    sentiment: {
      neg: Number,
      pos: Number,
      compound: Number,
      neu: Number
    },
    author: String,
    source: String,
    title: String,
    url: String,
    content: String
  });

  return mongoose.model('news', schema);
};
