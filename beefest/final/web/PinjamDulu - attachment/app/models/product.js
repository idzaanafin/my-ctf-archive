const mongoose = require('mongoose');

const ProductSchema = new mongoose.Schema({
  product_name: String,
  product_price: Number,
  product_image: String,
  product_desc: String
});

const Product =  mongoose.model('Product', ProductSchema)
module.exports = Product