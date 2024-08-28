const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const initializeDB = require('./db'); 
const path = require('path');
const { env } = require('process');

initializeDB();

const app = express();

app.use(session({ secret: env.secret, resave: false, saveUninitialized: false }));
app.use((req,res,next) => {
    res.locals.isLogin = req.session.userId
    return next();
})
var indexRouter = require('./routes/index');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views')); 
app.use('/', indexRouter);

app.use((req, res) => {
    res.render('404');
  });
  
module.exports = app;