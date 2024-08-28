var express = require('express');
var router = express.Router();
const User = require('../models/user');
const Product = require('../models/product');
const { env } = require('process');

function requireLogin(req, res, next) {
  if (!req.session.userId) {
    res.redirect('/login');
  } else {
    next();
  }
}

router.get('/', async (req, res) => {
  if(req.session.userId) {
    try {
      const user = await User.findById(req.session.userId);
      if (user) {
        return res.render('index', { username: user.username, user_balance: user.user_balance });
      } else {
        return res.send('User not found.');
      }
    } catch (error) {
      console.log(error)
      return res.send('Error occurred while fetching user data.');
    }
  }

  res.render('index')
});

router.get('/register', (req, res) => {
    res.render('register');
  });
  
router.post('/register', async (req, res) => {
    const { username, password } = req.body;
  
    try {
      const existingUser = await User.findOne({ username });
      if (existingUser) {
        res.send('Username already exists. Please choose a different username.');
      } else {
        const user = new User({ username, password });
        await user.save();
        res.send('Registration successful! Now you can <a href="/login">login</a>.');
      }
    } catch (error) {
      console.log(error)
      res.send('Error occurred while registering.');
    }
  });

router.get('/login', (req, res) => {
    res.render('login');
  });
  
router.post('/login', async (req, res) => {
      const { username, password } = req.body;
      try {
        const user = await User.findOne({ username, password });
        if (user) {
          req.session.userId = user._id;
          res.redirect('/');
        } else {
          res.send('Invalid username or password. Please try again.');
        }
      } catch (error) {
        console.log(error)
        res.send('Error occurred while logging in.');
      }
  });

router.get('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      res.send('Error occurred while logging out.');
    } else {
      res.redirect('/login');
    }
  });
});



router.get('/store', async (req, res) => {
    try {
      const products = await Product.find({});
      res.render('store', { products });
    } catch (error) {
      res.send('Error occurred while fetching products.');
    }
  });

router.get('/product/:id', requireLogin, async (req, res) => {
  try {
    const { id } = req.params;
    const products = await Product.findById(id);
    if(!products) return res.status(404).send();
    res.render('product', { products });
  } catch (error) {
    res.send('Error occurred while fetching products.');
  }
});

router.post('/checkout', requireLogin, async (req, res) => {
  try {
    const { productId, quantity } = req.body;
    const user = await User.findById(req.session.userId);
    const products = await Product.findById(productId);

    if(user.user_balance > (products.product_price * quantity)) {
      const updatedBalance = user.user_balance - (products.product_price * quantity)
      await User.findByIdAndUpdate(req.session.userId, { user_balance: updatedBalance }, { new: true });
      res.send('Success!');
    } else {
      res.send('User balance is not enough!');
    }
  } catch (error) {
    console.log(error)
    res.send('Error occurred while buying product.');
  }
});

router.get('/vip', requireLogin, async(req, res) => {
  const user = await User.findById(req.session.userId);
  const userBalance = user.user_balance
  flag = env.flag
  if (userBalance >= '1337') {
    res.render('flag', {flag: flag})
  } else {
    res.status(403).render('403', { error: "Your balance is too low!" });
  }
})
  
module.exports = router;
