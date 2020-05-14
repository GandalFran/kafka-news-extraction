var express = require('express');
var app = express();
app.use(express.static('/opt/tie/front/web/dist'));
app.listen(8080, function () {});