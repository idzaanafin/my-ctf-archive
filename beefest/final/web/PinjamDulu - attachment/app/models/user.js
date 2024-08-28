const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  username: String,
  password: String,
  user_balance: {
    type: Number,
    default: 100,
  },
});

const User =  mongoose.model('User', UserSchema);
module.exports = User