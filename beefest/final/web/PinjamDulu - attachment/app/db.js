const User = require('./models/user');
const Product = require('./models/product');

async function initializeDB() {
  try {

    await User.deleteMany({});
    await Product.deleteMany({});

    const products = [
      { product_name: 'flipper zero', product_price: 50, product_image: '/src/img/flipper.jpg', product_desc: 'Flipper Zero is a versatile hacking device designed for security professionals and enthusiasts. It combines various tools and features in a compact form factor, allowing users to interact with and analyze different electronic systems, including RFID, NFC, and more. Flipper Zero is known for its programmability and adaptability, making it a valuable tool for testing and understanding various technologies.' },
      { product_name: 'hackRF', product_price: 75, product_image: '/src/img/hackrf.jpeg', product_desc: 'HackRF is a software-defined radio (SDR) platform that empowers users to explore and manipulate wireless communication systems. It provides a wide frequency range and is designed for tasks such as analyzing and experimenting with radio signals, including Wi-Fi, Bluetooth, and GSM. HackRF\'s flexibility and open-source nature make it a valuable tool for radio frequency research and security assessments.' },
      { product_name: 'flag', product_price: 1337, product_image: '/src/img/flag.png', product_desc: 'In hacking and cybersecurity, a "flag" is a digital marker or piece of information that is hidden within a system or application. Flags are typically used in capture the flag (CTF) challenges, where participants must locate and extract these hidden markers as part of a cybersecurity competition or training exercise. Flags can be in the form of text strings, files, or other data, and they serve as proof that a particular task or goal has been accomplished within the challenge. Finding and collecting flags is a common way to demonstrate one\'s skills in penetration testing and cybersecurity.' }
    ];

    await Product.insertMany(products);

    console.log('Database initialization completed.');
  } catch (error) {
    console.error('Error occurred during database initialization:', error);
  } finally {
  }
}

module.exports = initializeDB;
