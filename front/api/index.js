const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const db = require('./app/models');

// Express APP
const app = express();

// CORS options
const corsOptions = {
  origin: '*'
};

// Middlewares
app.use(cors(corsOptions));

// Parse request with content type json
app.use(bodyParser.json());

// Connect to the database
db.mongoose
  .connect(db.url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((err) => {
    console.log('Could not connect to MongoDB', err);
    process.exit();
  });

// Routes
require('./app/routes/')(app);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
